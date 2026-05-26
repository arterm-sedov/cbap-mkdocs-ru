"""Import PHPKB articles for RAG corpora (phpkb_content_rag).

Shares category/filename resolution and CLI with phpkb_import.py.
RAG-specific: markdown-only export, minimal frontmatter, no product-name
placeholders, hyperlink-map footer, or kb.comindware.ru link rewriting.
"""

from tools.ssh_kb_ru import establish_connection_interactive
from tools.graceful_interrupt import safe_input, ensure_cleanup
import argparse
import html
import bs4
from markdownify import MarkdownConverter
import re
try:
    from pathvalidate import sanitize_filename
except ImportError:
    def sanitize_filename(value):
        return str(value)
from pathlib import Path
import shutil
import os
import os.path
import json

KB_ID_TO_FILENAME_MAP = None
KB_ID_TO_TITLE_MAP = None
KB_ID_TO_CATEGORY_FOLDER_MAP = None
KB_ID_TO_TITLE_MAP_FILE = '.article_id_filename_map_v6.json'
THIS_FILE_DIR = os.path.dirname(os.path.realpath(__file__))
IMPORT_PATH_DEFAULT = 'phpkb_content_rag'
KB_DIR = IMPORT_PATH_DEFAULT
TOTAL_PAGES_IMPORTED = 0
CONNECTION = None
DOCS_RU_FOLDER = 'docs/ru'
HYPERLINKS_FILE = os.path.join(DOCS_RU_FOLDER, '.snippets/hyperlinks_mkdocs_to_kb_map.md')
LEGACY_PREFIX_PATTERN = re.compile(r'^(\d+)-(.+)$')


def normalize_import_stem(article_id, stem):
    """Drop legacy numeric prefix when it is not the current PHPKB article id."""
    article_id = str(article_id)
    stem = str(stem).strip()
    match = LEGACY_PREFIX_PATTERN.match(stem)
    if match and match.group(1) != article_id:
        return match.group(2)
    return stem


def build_import_base_name(article_id, stem):
    stem = normalize_import_stem(article_id, stem)
    article_id = str(article_id)
    if stem.startswith(f"{article_id}-"):
        return stem
    return f"{article_id}-{stem}"


def category_child_filters_import(include_private=False):
    parts = ["category_show='yes'", "phpkb_categories.language_id = 2"]
    if not include_private:
        parts.insert(1, "category_status = 'public'")
    return " AND ".join(parts)


def parse_mapping_file(mapping_json):
    """Return (articles_map, categories_map) from flat or structured JSON."""
    if not mapping_json:
        return {}, {}
    if isinstance(mapping_json, dict) and (
        "Articles" in mapping_json or "Categories" in mapping_json
    ):
        articles = mapping_json.get("Articles") or {}
        categories = mapping_json.get("Categories") or {}
        return articles, categories
    return mapping_json, {}


def build_category_dir_name(category_id, title, category_folder_map=None):
    """Build import folder name: '{id}-{ascii_slug}' (same id-stem pattern as article files)."""
    category_id = str(category_id)
    folder_map = category_folder_map if category_folder_map is not None else KB_ID_TO_CATEGORY_FOLDER_MAP
    slug = (folder_map or {}).get(category_id)
    if slug:
        return sanitize_filename(f"{category_id}-{slug}")
    return sanitize_filename(f"{category_id}-{title}")


# Function to search for pattern in hyperlinks file and replace
def find_url_in_snippet(article_id, anchor):
    url = ''
    try:
        with open(HYPERLINKS_FILE, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        for line in lines:
            # Search for the url with articleId
            match = None
            if anchor:
                match = re.search(fr'(\[.*?\]):.*kbArticleURLPrefix.*{article_id}#{anchor}\n', line)
            #     print (f"articleId {article_id} and anchor {anchor}")
            if not match:
                match = re.search(fr'(\[.*?\]):.*kbArticleURLPrefix.*{article_id}\n', line)
            if match and match.group(1):
                url = match.group(1)
                #print(f"Found link and URL for articleId {article_id}: {url}")
                break  # Found the match, no need to continue searching
        return url
    except (IOError, UnicodeDecodeError):
        return url


def importCategoryChildren(parent, categoryDirectory, include_private=False):
    id = parent[0]
    title = parent[1]
    c4 = CONNECTION.cursor()
    c4.execute(f"""
            SELECT DISTINCT (category_id), category_name, parent_id
            FROM phpkb_categories 
            WHERE {category_child_filters_import(include_private)}
            AND parent_id = {id}
            """)
    children = c4.fetchall()
    print("\n-----\n\nCategory {}. {}. Children: {}\n".format(id, title, children))
    dirName = build_category_dir_name(id, title)
    categoryDir = os.path.join(categoryDirectory, dirName)
    if os.path.exists(categoryDir):
        print('Deleting dir:' + categoryDir)
        shutil.rmtree(categoryDir, ignore_errors=True)
    Path(categoryDir).mkdir(parents=True, exist_ok=True)
    print('Importing articles to dir: ' + categoryDir + '\n')
    importArtciclesInCategory(id, categoryDir)
    for child in children:
        importCategoryChildren(child, categoryDir, include_private=include_private)
    return children


def importArtciclesInCategory(categoryId, categoryDir):
    c = CONNECTION.cursor()
    c.execute(f"""
            SELECT DISTINCT (phpkb_articles.article_id), phpkb_articles.article_content, phpkb_articles.article_title, phpkb_articles.article_last_updation
            FROM phpkb_articles, phpkb_relations, phpkb_categories 
            WHERE article_show='yes' 
            AND article_status='approved'
            AND phpkb_relations.category_id = {categoryId} 
            AND phpkb_relations.article_id = phpkb_articles.article_id
            """)

    articles = c.fetchall()
    print(f"Found {len(articles)} articles in category {categoryId}")
    global TOTAL_PAGES_IMPORTED
    pages = 0
    for id, content, title, last_updation in articles:
        print(f"Processing article {id}: {title}")
        sanitizedTitle = sanitize_filename(str(title))
        print(f"Looking up existing filename for article {id}...")
        existingFilename = findFilenameByArticleId(id, DOCS_RU_FOLDER)
        if existingFilename:
            sanitizedTitle = existingFilename
            print(f"Found existing filename: {existingFilename}")
        else:
            sanitizedTitle = normalize_import_stem(id, sanitizedTitle)
            updateMappingJson(id, sanitizedTitle, KB_ID_TO_TITLE_MAP, KB_ID_TO_TITLE_MAP_FILE)
            print(f"Using new filename: {sanitizedTitle}")

        # Avoid duplicate kbId prefix in the target filename
        base_name = build_import_base_name(id, sanitizedTitle)
        filename = os.path.join(categoryDir, f"{base_name}.md")
        print('    Importing article: ' + filename)

        with open(filename, "w+", encoding="utf-8") as b:
            print(f"  Starting BeautifulSoup processing for article {id}...")
            p = bs4.BeautifulSoup(html.unescape(content), 'html.parser')
            print(f"  BeautifulSoup completed for article {id}")

            article_title = p.new_tag("h1")
            article_title.string = title
            p.insert(0, article_title)
            print(f"  Added title tag for article {id}")

            # Discard PHPKB TOC within <div class="mce-toc">
            for toc in p.find_all('div', class_='mce-toc'):
                toc.decompose()

            # Remove redundant TOC, created manually
            # Find headers that say "Содержание" and remove them and their subsequent list.
            potential_headers = p.find_all(['h2', 'p'])
            for header in list(potential_headers):
                # Check if the element's text is "Содержание" or "Содержание:", ignoring case and whitespace.
                text = header.get_text(strip=True).lower()
                if text in ('содержание', 'содержание:', 'содержание.'):
                    next_sibling = header.find_next_sibling()

                    # The next sibling could be a NavigableString (e.g., whitespace).
                    # We need to find the next actual tag.
                    while next_sibling and isinstance(next_sibling, bs4.NavigableString):
                        next_sibling = next_sibling.find_next_sibling()

                    if next_sibling and next_sibling.name in ['ol', 'ul']:
                        # This is a TOC. Decompose both the header and the list.
                        print(
                            f"  Decomposing standalone TOC header '{header.name}' "
                            f"and subsequent list '{next_sibling.name}'."
                        )
                        header.decompose()
                        next_sibling.decompose()

            # Convert tables with class 'source_code_container' into a single <pre> with plain text
            # and avoid nested <code> that leads to duplicate Markdown fences
            # These tables were used as a workaround for code blocks.
            for table in p.find_all('table', class_='source_code_container'):
                print(f"  Converting source code table to <pre> block for article {id}...")
                pre = p.new_tag("pre")
                code_text_parts = []
                for td in table.find_all('td', class_='source_code'):
                    # Extract text preserving line breaks within the cell
                    td_text = td.get_text(separator='\n', strip=False)
                    code_text_parts.append(td_text)
                # Join parts with newlines; assign as text content of <pre>
                pre.string = "\n".join(code_text_parts).strip("\n")
                table.replace_with(pre)
                pre.insert_before(p.new_tag("p"))

            print(f"  Starting markdown conversion for article {id}...")
            markdown = MarkdownConverter(heading_style='ATX', bullets='-', escape_misc=False).convert_soup(p)
            print(f"  Markdown conversion completed for article {id}")

            print(f"  Starting regex processing for article {id}...")
            try:
                # Remove redundant new lines
                print(f"    Processing redundant new lines for article {id}...")
                pattern = re.compile(r'^\n^\n\n*', flags=re.MULTILINE)
                markdown = re.sub(pattern, r'\n', markdown)
                print(f"    Redundant new lines processed for article {id}")

                # Remove redundant spaces before new lines
                print(f"    Processing redundant spaces for article {id}...")
                pattern = re.compile(r' +\n', flags=re.MULTILINE)
                markdown = re.sub(pattern, r'\n', markdown)
                print(f"    Redundant spaces processed for article {id}")

                # Remove redundant [*‌* К началу](#) links.
                print(f"    Processing redundant 'К началу' links for article {id}...")
                pattern = re.compile(r'\s*\[[^\]]*К началу[^\]]*\]\(#\)\s*')
                markdown = re.sub(pattern, r'', markdown)
                print(f"    Redundant 'К началу' links processed for article {id}")

                # Replace \t with four spaces
                print(f"    Processing tabs for article {id}...")
                markdown = markdown.replace('\t', '    ')
                print(f"    Tabs processed for article {id}")

                # Reformat images with captions
                print(f"    Processing image captions for article {id}...")
                pattern = re.compile(r'(!\[(.*)\]\(.*\))\n\n\2', flags=re.MULTILINE)
                markdown = re.sub(pattern, r'_\1_', markdown)
                print(f"    Image captions processed for article {id}")

                # Sanitize fenced code blocks to use 3 backticks instead of 4 or more, preserving indentation.
                print(f"    Sanitizing fenced code blocks for article {id}...")
                markdown = re.sub(r'`{4,}', r'```', markdown, flags=re.MULTILINE)
                # Collapse duplicated triple fences produced on a single line: "``` ```" -> "```"
                markdown = markdown.replace('``` ```', '```')
                print(f"    Fenced code blocks sanitized for article {id}")

                # Final cleanup of excessive newlines.
                print(f"    Cleaning up excessive newlines for article {id}...")
                markdown = re.sub(r'\n{3,}', '\n\n', markdown)
                print(f"    Excessive newlines cleaned up for article {id}")

                print(f"  Regex processing completed for article {id}")
            except Exception as e:
                print(f"  Warning: Regex processing failed for article {id}: {e}")
                print(f"  Continuing with original markdown for article {id}")
                # Continue with the original markdown if regex processing fails

            print(f"  Adding frontmatter for article {id}...")
            # Compile and add frontmatter
            frontmatter_lines = [
                '---',
                f"title: '{title}'",
                f'kbId: {id}',
                f"url: 'https://kb.comindware.ru/article.php?id={id}'",
            ]
            if last_updation:
                frontmatter_lines.append(f"updated: '{last_updation}'")
            frontmatter_lines += ['---', '\n']
            frontmatter = '\n'.join(frontmatter_lines)
            markdown = frontmatter + markdown.rstrip()
            print(f"  Frontmatter added for article {id}")

            print(f"  Writing markdown file for article {id}...")
            b.write(markdown)
            print(f"  Markdown file written for article {id}")
            # print(html.escape(str(p)))
            pages += 1
            print(f"Completed article {id}")
    TOTAL_PAGES_IMPORTED += pages
    print("\nImported {} articles, total {}\n\n-----\n".format(pages, TOTAL_PAGES_IMPORTED))
    return pages


def fetchCategories(show='yes', status='public', language_id=2, parent_id=''):
    c = CONNECTION.cursor()
    c.execute(f"""
            SELECT DISTINCT category_id, category_name, parent_id
            FROM phpkb_categories 
            WHERE category_show='{show}' 
            AND category_status = '{status}'
            AND phpkb_categories.language_id = {language_id}
            AND parent_id = '{parent_id}'
            """)
    categories = c.fetchall()
    return categories


def fetchCategoryById(category_id):
    c = CONNECTION.cursor()
    c.execute(
        """
            SELECT category_id, category_name, parent_id
            FROM phpkb_categories
            WHERE category_id = %s
            """,
        (str(category_id),),
    )
    return c.fetchone()


def listCategories(categories):
    index = 1
    for id, title, parent_id in categories:
        print(f"{index}. {id}. {title}")
        index += 1


def prompt_include_private():
    """Ask whether to walk category_status='private' children during import."""
    answer = safe_input("Include private categories? (Y/n)", default="n").strip().lower()
    return answer in ("y", "yes")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Import PHPKB categories/articles for RAG (markdown-only, minimal transforms)."
    )
    parser.add_argument(
        "--category-id",
        help="Import this PHPKB category tree non-interactively (e.g. 896 for V6).",
    )
    parser.add_argument(
        "--kb-dir",
        default=IMPORT_PATH_DEFAULT,
        help=f"Output root directory. Default: {IMPORT_PATH_DEFAULT}",
    )
    parser.add_argument(
        "--article-map",
        default=KB_ID_TO_TITLE_MAP_FILE,
        help=f"Gap-fill article id to filename stem map. Default: {KB_ID_TO_TITLE_MAP_FILE}",
    )
    parser.add_argument(
        "--include-private",
        action="store_true",
        help="Import private categories (e.g. V6 root category 896).",
    )
    return parser.parse_args(argv)


def initialize_article_map(mapping_file):
    global KB_ID_TO_TITLE_MAP, KB_ID_TO_CATEGORY_FOLDER_MAP, KB_ID_TO_TITLE_MAP_FILE
    KB_ID_TO_TITLE_MAP_FILE = mapping_file
    articles, categories = parse_mapping_file(loadMappingJson(KB_ID_TO_TITLE_MAP_FILE) or {})
    KB_ID_TO_TITLE_MAP = articles
    KB_ID_TO_CATEGORY_FOLDER_MAP = categories


def run_cli_import(category_id, kb_dir, include_private=False):
    global KB_DIR, KB_ID_TO_FILENAME_MAP, CONNECTION, TOTAL_PAGES_IMPORTED

    KB_DIR = kb_dir
    KB_ID_TO_FILENAME_MAP = None
    TOTAL_PAGES_IMPORTED = 0
    server = None

    try:
        CONNECTION, server = establish_connection_interactive()
        category = fetchCategoryById(category_id)
        if not category:
            print(f"Category {category_id} not found.")
            return 1
        print(f"Importing RAG corpus from category tree {category[0]}. {category[1]} into {KB_DIR}")
        importCategoryChildren(category, KB_DIR, include_private=include_private)
        print(f"Import finished. Total articles imported: {TOTAL_PAGES_IMPORTED}")
        return 0
    except KeyboardInterrupt:
        return 1
    finally:
        ensure_cleanup(CONNECTION, server)


def main():
    global KB_ID_TO_TITLE_MAP, KB_DIR

    initialize_article_map(KB_ID_TO_TITLE_MAP_FILE)

    import_path = safe_input(
        f'Path to import (default `{IMPORT_PATH_DEFAULT}`)',
        default=IMPORT_PATH_DEFAULT,
    )
    KB_DIR = import_path.strip() if import_path and import_path.strip() else IMPORT_PATH_DEFAULT

    global CONNECTION
    server = None

    try:
        CONNECTION, server = establish_connection_interactive()

        importChildren = ''
        categoryId = ''
        categoryTitle = ''
        parent_category = ''
        categoryChoice = ''

        print('\nRoot categories:\n')

        while importChildren != 'y':
            categoryChoice = ''

            categories = fetchCategories(parent_id=categoryId)
            if parent_category:
                print("\nParent: {}. {}\n".format(categoryId, categoryTitle))

            if len(categories) == 0:
                print("No categories found. Exiting.")
                break
            elif len(categories) == 1:
                # If there's only one category, automatically select it
                categoryChoice = 0
                categoryId = categories[0][0]
                categoryTitle = categories[0][1]
                childrenCategories = fetchCategories(parent_id=categoryId)
                childrenCategoriesNumber = len(childrenCategories)

                print(f"\nOnly one category found: {categoryId}. {categoryTitle}")
                if childrenCategoriesNumber > 0:
                    print(f'\nIt has {childrenCategoriesNumber} child categories:\n')
                    listCategories(childrenCategories)
                    importChildren = safe_input(
                        f"\nEnter `Y` to import all child categories and articles. \n"
                        f" Or choose a category to browse (1 to {childrenCategoriesNumber})"
                    ).lower()
                else:
                    print('\nIt has no child categories')
                    importChildren = safe_input(
                        "\nEnter `Y` to import all articles from this category"
                    ).lower()
                    if importChildren != 'y':
                        print('Imported nothing')
                        break
            elif len(categories) > 1:
                parent_category = categories[0]
                listCategories(categories)
                print("\n---------\n")

                if importChildren.isnumeric() and int(importChildren) <= len(categories):
                    categoryChoice = int(importChildren) - 1
                    importChildren = 'y'
                else:
                    while not (categoryChoice.isnumeric() and int(categoryChoice) <= len(categories)):
                        categoryChoice = safe_input(
                            "Choose category to browse (1 to {})".format(len(categories))
                        )
                        if categoryChoice.isnumeric() and int(categoryChoice) <= len(categories):
                            categoryChoice = int(categoryChoice) - 1
                            break
                        categoryChoice = ''
                        print('Wrong category choice')

                categoryId = categories[categoryChoice][0]
                categoryTitle = categories[categoryChoice][1]
                childrenCategories = fetchCategories(parent_id=categoryId)
                childrenCategoriesNumber = len(childrenCategories)

                print("\nChosen category: {} {}".format(categoryId, categoryTitle))
                if childrenCategoriesNumber > 0:
                    print('\nIt has {} child categories:\n'.format(childrenCategoriesNumber))
                    listCategories(childrenCategories)
                    importChildren = safe_input(
                        "\nEnter `Y` to import all child categories and articles. \n"
                        " Or choose a category to browse (1 to {})".format(childrenCategoriesNumber)
                    ).lower()
                else:
                    print('\nIt has no child categories')
                    importChildren = safe_input(
                        "\nEnter `Y` to import all articles from this category"
                    ).lower()
                    if importChildren != 'y':
                        print('Imported nothing')
                        break

        else:
            include_private = prompt_include_private()
            if len(categories) > 1 and categories[categoryChoice]:
                importCategoryChildren(
                    categories[categoryChoice],
                    KB_DIR,
                    include_private=include_private,
                )
            elif len(categories) == 1:
                importCategoryChildren(
                    categories[0],
                    KB_DIR,
                    include_private=include_private,
                )
    except KeyboardInterrupt:
        # Connection cleanup handled in finally block
        pass
    finally:
        # Always ensure connections are closed, even on interrupt
        ensure_cleanup(CONNECTION, server)


def findFilenameByArticleId(article_id, docs_dir):
    """
    Find the filename in the specified docs directory containing the specified kbId.
    Uses a cached dictionary to speed up subsequent lookups.

    Args:
        article_id (str): The kbId to search for.
        docs_dir (str): The directory to scan for markdown files.

    Returns:
        str: The filename without the .md extension if found, else None.
    """
    global KB_ID_TO_FILENAME_MAP

    # Initialize and populate the mapping if not already done
    if KB_ID_TO_FILENAME_MAP is None:
        KB_ID_TO_FILENAME_MAP = {}
        if not os.path.isdir(docs_dir):
            raise FileNotFoundError(f"The directory '{docs_dir}' does not exist.")

        # Build the mapping from kbId to filenames (includes index.md, e.g. kbId 5161)
        for root, _, files in os.walk(docs_dir):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    filename = os.path.splitext(file)[0]
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            for line in f:
                                match = re.match(r"kbId:\s*(\S+)", line.strip())
                                if match:
                                    kb_id = match.group(1)
                                    KB_ID_TO_FILENAME_MAP[kb_id] = filename
                                    break  # Stop scanning this file after finding kbId
                    except (UnicodeDecodeError, IOError):
                        # Skip files that can't be read
                        continue

    foundFilename = KB_ID_TO_FILENAME_MAP.get(str(article_id))
    foundTitle = KB_ID_TO_TITLE_MAP.get(str(article_id))
    if not foundFilename:
        try:
            articleAnchor = find_url_in_snippet(article_id, None)
            if articleAnchor:
                articleAnchor = re.sub(r'\[(.*)\]', r'\1', articleAnchor)
                KB_ID_TO_FILENAME_MAP[str(article_id)] = normalize_import_stem(
                    article_id, articleAnchor
                )
            elif foundTitle:
                KB_ID_TO_FILENAME_MAP[str(article_id)] = normalize_import_stem(
                    article_id, foundTitle
                )
        except (IOError, UnicodeDecodeError):
            # If hyperlinks file can't be read, use title as fallback
            if foundTitle:
                KB_ID_TO_FILENAME_MAP[str(article_id)] = normalize_import_stem(
                    article_id, foundTitle
                )

    # Lookup in the cached dictionary
    return KB_ID_TO_FILENAME_MAP.get(str(article_id))


def updateMappingJson(key, value, mapping, mappingFilename):
    key = str(key)
    mapping[key] = value
    existing = loadMappingJson(mappingFilename) or {}
    articles, categories = parse_mapping_file(existing)
    articles[key] = value
    payload = {"Articles": articles, "Categories": categories}
    with open(mappingFilename, "w", encoding="utf-8") as mapping_file:
        json.dump(payload, mapping_file, indent=4, ensure_ascii=False)
        mapping_file.write("\n")
    print(f"Updated article map entry {key} -> {value}")


def loadMappingJson(mappingFilename):
    with open(mappingFilename, "r", encoding="utf-8") as mapping_json_file:
        mapping_json_file_content = mapping_json_file.read()
        return json.loads(mapping_json_file_content) if mapping_json_file_content else dict()


if __name__ == "__main__":
    cli_args = parse_args()
    if cli_args.category_id:
        initialize_article_map(cli_args.article_map)
        raise SystemExit(
            run_cli_import(
                cli_args.category_id,
                cli_args.kb_dir,
                include_private=cli_args.include_private,
            )
        )
    main()
