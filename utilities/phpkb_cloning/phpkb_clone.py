"""Clone PHPKB categories/articles and keep a resumable ID mapping.

This is the main DB-mutating utility in the PHPKB cloning workflow. It connects
to PHPKB through `tools.ssh_kb_ru.establish_connection_interactive()` and can
clone either a whole category tree or selected articles.

Core behavior:
- clones full `phpkb_categories` rows except regenerated `category_id`;
- clones full `phpkb_articles` rows except regenerated `article_id`;
- inserts `phpkb_relations` rows that point cloned articles to cloned or
  selected target categories;
- copies article-owned backrefs from `phpkb_attachments` and
  `phpkb_custom_data`, remapping only `article_id`;
- does not duplicate physical attachment files;
- writes old-to-new IDs into a mapping JSON with `Categories` and `Articles`
  sections.

Resume behavior:
- `--mapping` selects the mapping file, default `.mapping.json`;
- existing mappings are loaded by default, so interrupted clone runs can be
  resumed without recloning already mapped categories/articles;
- `--fresh` refuses to run when the selected mapping file already exists;
- mapping writes are atomic via temporary file replacement.

Generated article/category IDs are captured from `cursor.lastrowid`, which is
the auto-increment value produced by this connection's INSERT. Do not replace
that with `SELECT MAX(...)`, because global MAX queries can pick up another
process's concurrent insert.
"""

import mysql.connector
import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.ssh_kb_ru import establish_connection_interactive, close_connection
from tools.graceful_interrupt import safe_input, ensure_cleanup
from html.parser import HTMLParser
import bs4
from markdownify import markdownify as md
import re
try:
    from pathvalidate import sanitize_filename
except ImportError:
    def sanitize_filename(value):
        return str(value)
from cryptography.fernet import Fernet

class myparser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			print("IMG tag with attrs %s\n" % repr(attrs))

import os

import os.path

import json

TOTAL_PAGES_CLONED = 0
CONNECTION = None
DEFAULT_MAPPING_FILE = ".mapping.json"
MAPPING_FILE = DEFAULT_MAPPING_FILE

MAPPING = dict()
CATEGORY_MAPPING = dict()
ARTICLE_MAPPING = dict()
ARTICLE_CHILD_CLONE_SPECS = (
    {
        "label": "attachments",
        "table": "phpkb_attachments",
        "columns": ("article_id", "file_guid", "file_name", "file_type", "file_views", "file_status"),
    },
    {
        "label": "custom data",
        "table": "phpkb_custom_data",
        "columns": ("field_id", "article_id", "field_data"),
    },
)
# CATEGORY_COUNTER = 0

def numeric_id(value):
    value = str(value).strip()
    if not value.isdigit():
        raise argparse.ArgumentTypeError(f"Expected numeric ID, got: {value}")
    return value

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Clone PHPKB categories or articles and write .mapping.json.",
    )
    parser.add_argument("--profile", choices=("cmw", "cmwlab"), help="PHPKB server profile. Defaults to SERVER_PROFILE from .env.")
    parser.add_argument("--mapping", default=DEFAULT_MAPPING_FILE, help=f"Mapping JSON to read/write. Default: {DEFAULT_MAPPING_FILE}")
    parser.add_argument("--fresh", action="store_true", help="Start a fresh clone and refuse to run if the mapping file already exists.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--category-id", type=numeric_id, help="Clone this category and all child categories/articles.")
    mode.add_argument("--article-id", action="append", type=numeric_id, help="Clone an article. Can be used multiple times.")
    parser.add_argument("--target-parent-id", type=numeric_id, help="Parent category for --category-id clones. Defaults to the source parent.")
    parser.add_argument("--target-category-id", type=numeric_id, help="Target category for --article-id clones. Defaults to each source article category.")
    parser.add_argument("--suffix", default="_CLONE", help="Title suffix for --article-id clones. Defaults to _CLONE.")
    parser.add_argument("--show", action="store_true", help="Make --article-id clones visible. By default they are hidden.")
    return parser.parse_args(argv)

def has_cli_action(args):
    return bool(args.category_id or args.article_id)

def normalize_mapping(mapping):
    return {str(source_id): str(target_id) for source_id, target_id in (mapping or {}).items()}

def loadMappingJson(mapping_file):
    path = Path(mapping_file)
    if not path.exists():
        return {"Categories": {}, "Articles": {}}

    with path.open("r", encoding="utf-8") as mappingFile:
        mappingJson = json.load(mappingFile) if path.stat().st_size else {}
    return {
        "Categories": normalize_mapping(mappingJson.get("Categories")),
        "Articles": normalize_mapping(mappingJson.get("Articles")),
    }

def initializeMapping(mapping_file=DEFAULT_MAPPING_FILE, fresh=False):
    global MAPPING_FILE, MAPPING, CATEGORY_MAPPING, ARTICLE_MAPPING

    MAPPING_FILE = mapping_file
    if fresh and Path(mapping_file).exists():
        raise FileExistsError(f"Mapping file '{mapping_file}' already exists. Use a new --mapping path or omit --fresh to resume.")

    loaded_mapping = {"Categories": {}, "Articles": {}} if fresh else loadMappingJson(mapping_file)
    CATEGORY_MAPPING = loaded_mapping["Categories"]
    ARTICLE_MAPPING = loaded_mapping["Articles"]
    MAPPING = {"Categories": CATEGORY_MAPPING, "Articles": ARTICLE_MAPPING}

    mode = "fresh" if fresh else "resume"
    print(f"Mapping: {mapping_file}")
    print(f"Mode: {mode}")
    print(f"Loaded mapped categories: {len(CATEGORY_MAPPING)}")
    print(f"Loaded mapped articles: {len(ARTICLE_MAPPING)}")

def sql_name(identifier):
    if not identifier.replace("_", "").isalnum():
        raise ValueError(f"Unsafe SQL identifier: {identifier}")
    return f"`{identifier}`"

def clone_article_child_rows(cursor, old_article_id, new_article_id, spec):
    table = sql_name(spec["table"])
    columns = spec["columns"]
    insert_columns = ", ".join(sql_name(column) for column in columns)
    select_columns = ", ".join("%s" if column == "article_id" else sql_name(column) for column in columns)

    cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE `article_id`=%s", (old_article_id,))
    row_count = cursor.fetchone()[0]
    if not row_count:
        return 0

    cursor.execute(
        f"""
            INSERT INTO {table} ({insert_columns})
            SELECT {select_columns}
            FROM {table}
            WHERE `article_id`=%s
            """,
        (new_article_id, old_article_id),
    )
    return row_count

def clone_article_dependents(cursor, old_article_id, new_article_id):
    for spec in ARTICLE_CHILD_CLONE_SPECS:
        cloned = clone_article_child_rows(cursor, old_article_id, new_article_id, spec)
        if cloned:
            print(f"Cloned {cloned} {spec['label']} rows for article {old_article_id} -> {new_article_id}")

def cloneCategoryChildren(parent, newParentId=''):
    c = CONNECTION.cursor(buffered=True)
    
    id = str(parent[0])
    title = parent[1]
    parentId = str(parent[2])
    
    if newParentId:
        parentId = str(newParentId)
    
    newCategoryId = cloneCategory(id, parentId)
    CATEGORY_MAPPING.update({id:newCategoryId})
    updateMappingJson()
    
    #for id, title, parent_id, in parent:
    c.execute(f"""
        SELECT DISTINCT (category_id), category_name, parent_id
        FROM phpkb_categories 
        WHERE category_show='yes' 
        AND category_status = 'public'
        AND phpkb_categories.language_id = 2
        AND parent_id = {id}
        """)
    children = c.fetchall()
    print(f"\n-----\n\nCategory {id}. {title}. Children: {children}\n")
    print(f'Cloning articles from Category {id}. {title}.')
    cloneArticlesInCategory(id, newCategoryId)
    for child in children:
        cloneCategoryChildren(child, newCategoryId)
    return children
    
        
def cloneArticlesInCategory (category_id, newCategoryId):
    c = CONNECTION.cursor(buffered=True)
    c.execute(f"""
            SELECT DISTINCT (phpkb_articles.article_id), phpkb_articles.article_content, phpkb_articles.article_title 
            FROM phpkb_articles, phpkb_relations, phpkb_categories 
            WHERE article_show='yes' 
            AND phpkb_relations.category_id = {category_id} 
            AND phpkb_relations.article_id = phpkb_articles.article_id
            """)
    
    articles = c.fetchall()
    global TOTAL_PAGES_CLONED
    pages = 0
    for id, content, title in articles:
        id = str(id)
        sanitizedTitle=sanitize_filename(title)
        filename = f"{id} - {sanitizedTitle}"
        print ('    Cloning article: ' + filename)
        pages += 1
        newArticleId = cloneArticle(id, category_id, newCategoryId)
        ARTICLE_MAPPING.update({id:newArticleId})
        updateMappingJson()
    TOTAL_PAGES_CLONED += pages
    print(f"\nCloned {pages} articles, total {TOTAL_PAGES_CLONED}\n\n-----\n")
    return pages

def cloneArticle(article_id, category_id, newCategoryId, suffix="", show=True):
    
    c = CONNECTION.cursor(buffered=True)    
    article_created = False
    article_id = str(article_id)
    category_id = str(category_id)
    newCategoryId = str(newCategoryId)
    
    if not article_id in ARTICLE_MAPPING:
        c.execute(f"""
                CREATE TEMPORARY TABLE tmp SELECT * from phpkb_articles WHERE article_id={article_id};
                """)
        c.execute(f"""
                ALTER TABLE tmp DROP article_id;
                """)
        if suffix:
            c.execute("UPDATE tmp SET article_title = CONCAT(article_title, %s)", (suffix,))
        
        article_show_status = 'yes' if show else 'no'
        c.execute("UPDATE tmp SET article_show = %s", (article_show_status,))

        c.execute(f"""
                INSERT INTO phpkb_articles SELECT 0,tmp.* FROM tmp;
                """)
        newArticleId = str(c.lastrowid)
        if not newArticleId or newArticleId == "0":
            raise RuntimeError("Could not determine cloned article ID from cursor.lastrowid.")
        c.execute(f"""
                DROP TABLE tmp;
                """)
        article_created = True
        ARTICLE_MAPPING.update({article_id:newArticleId})
    else:
        newArticleId = ARTICLE_MAPPING[article_id]
    
    print(newArticleId)

    c.execute(f"""
            SELECT article_priority from phpkb_relations 
            WHERE article_id={article_id}
            AND category_id={category_id};
            """)
    
    article_priority = str(c.fetchone()[0])
    print(article_priority)
    
    c.execute(f"""
            SELECT COUNT(*) FROM phpkb_relations
            WHERE article_id={newArticleId}
            AND category_id={newCategoryId};
            """)

    relation_exists = c.fetchone()[0]
    if relation_exists:
        print(f"Relation already exists for article {newArticleId} in category {newCategoryId}")
    else:
        c.execute(f"""
                INSERT INTO phpkb_relations (article_id, category_id, article_priority)
                VALUES ({newArticleId}, {newCategoryId}, {article_priority});
                """)

    if article_created:
        clone_article_dependents(c, article_id, newArticleId)

    return newArticleId

def cloneCategory(category_id, newParentId):
    c = CONNECTION.cursor(buffered=True)
    category_id = str(category_id)
    newParentId = str(newParentId)

    if category_id in CATEGORY_MAPPING:
        newCategoryId = CATEGORY_MAPPING[category_id]
        print(f"Reusing mapped category {category_id} -> {newCategoryId}")
        return newCategoryId

    c.execute(f"""
            CREATE TEMPORARY TABLE tmp SELECT * from phpkb_categories WHERE category_id={category_id};
            """)
    c.execute(f"""
            ALTER TABLE tmp DROP category_id;
            """)
    c.execute(f"""
            UPDATE tmp SET parent_id ={newParentId};
            """)
    c.execute(f"""
            INSERT INTO phpkb_categories SELECT 0,tmp.* FROM tmp;
            """)
    newCategoryId = str(c.lastrowid)
    if not newCategoryId or newCategoryId == "0":
        raise RuntimeError("Could not determine cloned category ID from cursor.lastrowid.")
    c.execute(f"""
            DROP TABLE tmp;
            """)
    CATEGORY_MAPPING.update({category_id:newCategoryId})
    
    print(newCategoryId)

    return newCategoryId

def fetchCategories(show='yes', status='public', language_id=2, parent_id=''):

    c = CONNECTION.cursor()    

    c.execute(f"""
            SELECT DISTINCT category_id, category_name, parent_id
            FROM phpkb_categories 
            WHERE category_show='yes' 
            AND category_status = 'public'
            AND phpkb_categories.language_id = 2
            AND parent_id = '{parent_id}'
            """)

    categories = c.fetchall()
    return categories

def fetchCategory(category_id):
    c = CONNECTION.cursor()
    c.execute(f"""
            SELECT category_id, category_name, parent_id
            FROM phpkb_categories
            WHERE category_id = {category_id}
            """)
    return c.fetchone()


def listCategories(categories):
    index = 1
    for id, title, parent_id in categories:
        print(f"{index}. {id}. {title}")
        index += 1

def clone_specific_article(article_id):
    return clone_specific_article_to(article_id)

def clone_specific_article_to(article_id, target_category_id=None, suffix="_CLONE", show=False):
    c = CONNECTION.cursor(buffered=True)
    article_id = str(article_id)
    c.execute(f"SELECT category_id FROM phpkb_relations WHERE article_id={article_id} LIMIT 1")
    result = c.fetchone()
    if not result:
        print(f"Article {article_id} is not in any category and cannot be cloned.")
        return False
    original_category_id = result[0]

    newCategoryId = target_category_id or safe_input(f"Enter target category ID to clone article {article_id} into (or press Enter to clone to the same category {original_category_id})", default=str(original_category_id))
    
    if not newCategoryId:
        newCategoryId = original_category_id
    elif not str(newCategoryId).isnumeric():
        print("Invalid Category ID. It must be a number.")
        return False
        
    newArticleId = cloneArticle(article_id, original_category_id, newCategoryId, suffix, show=show)
    if newArticleId:
        print(f"Article {article_id} cloned as new article {newArticleId} into category {newCategoryId}")
        ARTICLE_MAPPING.update({article_id:newArticleId})
        return True
    return False

def run_cli(args):
    if args.category_id:
        category = fetchCategory(args.category_id)
        if not category:
            print(f"Category {args.category_id} not found.")
            return False
        cloneCategoryChildren(category, args.target_parent_id or '')
        return True

    for article_id in args.article_id or ():
        clone_specific_article_to(
            article_id,
            target_category_id=args.target_category_id,
            suffix=args.suffix,
            show=args.show,
        )
    return True

def run_interactive():
    if safe_input('Clone specific articles? Y/N').lower() == 'y':
        article_id = ''
        while article_id.lower() != 'e':
            article_id = safe_input('Enter article ID to clone or E to exit')
            if article_id.lower() == 'e':
                break
            if article_id.isnumeric():
                success = clone_specific_article(article_id)
                if not success:
                    print("Please try another article ID or press 'E' to exit")
            else:
                print("Please enter a valid numeric article ID or 'E' to exit")
    else:
        cloneChildren = ''
        categoryId = ''
        parent_category = ''
        categoryChoice = ''

        print('\nRoot categories:\n')

        while cloneChildren != 'y':
            categoryChoice = ''
            categories = fetchCategories(parent_id=categoryId)
            if parent_category: print("\nParent: {}. {}\n".format(categoryId, categoryTitle))
            if len(categories)>1: 
                parent_category = categories[0]
                listCategories(categories)
                print("\n---------\n")
                
                if cloneChildren.isnumeric() and int(cloneChildren) <= len(categories):
                        categoryChoice = int(cloneChildren)-1
                        cloneChildren = 'y'
                else:    
                    while not (categoryChoice.isnumeric() and int(categoryChoice) <= len(categories)):
                        categoryChoice = safe_input("Choose category to browse (1 to {})".format(len(categories)))
                        if categoryChoice.isnumeric() and int(categoryChoice) <= len(categories):
                            categoryChoice = int(categoryChoice)-1
                            break
                        else:
                            categoryChoice = ''
                            print ('Wrong category choice')
                    
                
                categoryId = categories[categoryChoice][0]
                categoryTitle = categories[categoryChoice][1]  
                childrenCategories = fetchCategories(parent_id=categoryId)
                childrenCategoriesNumber = len(childrenCategories)
            
                print ("\nChosen category: {} {}".format(categoryId, categoryTitle))
                if childrenCategoriesNumber > 0:
                    print ('\nIt has {} child categories:\n'.format(childrenCategoriesNumber))
                    listCategories(childrenCategories)
                    cloneChildren = safe_input("\nEnter `Y` to clone the category and all its child categories and articles. \n Or choose a category to browse (1 to {})".format(childrenCategoriesNumber)).lower()
                else: 
                    print ('\nIt has no child categories')
                    cloneChildren = safe_input("\nEnter `Y` to clone the category and all articles from this category.".format(categoryId, categoryTitle)).lower()
                    if cloneChildren !='y': 
                        print('Cloned nothing')
                        break

        else:
            if categories[categoryChoice]:
                # cloneParent = safe_input("\nEnter `Y` to clone the parent category itself along with its children. ".format(categoryId, categoryTitle)).lower() == 'y'
                cloneCategoryChildren(categories[categoryChoice])

def main(argv=None):
    
    global CONNECTION
    server = None
    args = parse_args(argv)
    
    try:
        initializeMapping(args.mapping, args.fresh)
        server_profile = args.profile or os.getenv("SERVER_PROFILE", "cmw")
        print(f"Using PHPKB server profile: {server_profile}")
        CONNECTION, server = establish_connection_interactive(args.profile)
        
        if has_cli_action(args):
            run_cli(args)
        else:
            run_interactive()
        
        updateMappingJson()
    except KeyboardInterrupt:
        # Connection cleanup handled in finally block
        pass
    finally:
        # Always ensure connections are closed, even on interrupt
        ensure_cleanup(CONNECTION, server)

def updateMappingJson(mapping_file=None):
    MAPPING.update({'Categories':CATEGORY_MAPPING, 'Articles':ARTICLE_MAPPING})
    #if input('Save mapping? Y / N\n').lower() == 'y':
    target = Path(mapping_file or MAPPING_FILE)
    temp = target.with_suffix(target.suffix + ".tmp")
    with temp.open("w", encoding="utf-8") as mappingFile:
        mappingJson = json.dumps(MAPPING, indent = 4, ensure_ascii=False)
        print(mappingJson)
        mappingFile.write(mappingJson)
    temp.replace(target)

if __name__ == "__main__":
    main()
