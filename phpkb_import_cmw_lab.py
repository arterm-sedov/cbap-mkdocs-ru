import mysql.connector
from sshtunnel import SSHTunnelForwarder
from getpass import getpass
import html
from html.parser import HTMLParser
import bs4
from markdownify import markdownify as md
from markdownify import MarkdownConverter
import re
from pathvalidate import sanitize_filename
from pathlib import Path
import shutil
from cryptography.fernet import Fernet
import os
import os.path
import json
from sshtunnel import SSHTunnelForwarder
import paramiko

KB_ID_TO_FILENAME_MAP = None
KB_ID_TO_TITLE_MAP = None
KB_ID_TO_TITLE_MAP_FILE = '.article_id_filename_map_v4_cmw_lab.json'
THIS_FILE_DIR = os.path.dirname(os.path.realpath(__file__))
IMPORT_PATH_DEFAULT = 'phpkb_content_cmw_lab'
importPath = input(f'Path to import (default `{IMPORT_PATH_DEFAULT}`): ') 
KB_DIR = os.path.dirname(importPath) if importPath else IMPORT_PATH_DEFAULT
TOTAL_PAGES_IMPORTED = 0
CONNECTION = None
DOCS_RU_FOLDER = 'docs/ru'
HYPERLINKS_FILE = os.path.join(DOCS_RU_FOLDER, '.snippets/hyperlinks_mkdocs_to_kb_map.md')

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

def importCategoryChildren(parent, categoryDirectory, show='yes', status='public'):
        id = parent[0]
        title = parent[1]
        c4 = CONNECTION.cursor()    
        c4.execute(f"""
            SELECT DISTINCT (category_id), category_name, parent_id
            FROM phpkb_categories 
            WHERE category_show='{show}' 
            AND category_status = '{status}'
            AND phpkb_categories.language_id = 1
            AND parent_id = {id}
            """)
        children = c4.fetchall()
        print("\n-----\n\nCategory {}. {}. Children: {}\n".format(id, title, children))
        dirName = sanitize_filename('{}. {}'.format(id, str(title)))
        categoryDir = os.path.join(categoryDirectory, dirName)
        if os.path.exists(categoryDir): 
            print('Deleting dir:' + categoryDir)
            shutil.rmtree(categoryDir, ignore_errors=True)
        Path(categoryDir).mkdir(parents=True, exist_ok=True)
        print('Importing articles to dir: ' + categoryDir + '\n')
        importArtciclesInCategory(id, categoryDir)
        for child in children:
            importCategoryChildren(child, categoryDir)
        return children
    
        
def importArtciclesInCategory (categoryId, categoryDir):
    c = CONNECTION.cursor()
    c.execute(f"""
            SELECT DISTINCT (phpkb_articles.article_id), phpkb_articles.article_content, phpkb_articles.article_title 
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
    for id, content, title in articles:
        print(f"Processing article {id}: {title}")
        sanitizedTitle = sanitize_filename(str(title))
        print(f"Looking up existing filename for article {id}...")
        existingFilename = findFilenameByArticleId(id, DOCS_RU_FOLDER)
        if existingFilename:
            sanitizedTitle = existingFilename
            print(f"Found existing filename: {existingFilename}")
        else: 
            updateMappingJson(id, sanitizedTitle, KB_ID_TO_TITLE_MAP, KB_ID_TO_TITLE_MAP_FILE)
            print(f"Using new filename: {sanitizedTitle}")
        filename = os.path.join(categoryDir, f"{id}-{sanitizedTitle}.md")
        filename_html = os.path.join(categoryDir, f"{id}-{sanitizedTitle}.html")
        print ('    Importing article: ' + filename)
        
        with open(filename, "w+") as b:
            print(f"  Starting BeautifulSoup processing for article {id}...")
            p = bs4.BeautifulSoup(html.unescape(content), 'html.parser')
            print(f"  BeautifulSoup completed for article {id}")
            
            article_title = p.new_tag("h1")
            article_title.string=title
            p.insert(0, article_title)
            print(f"  Added title tag for article {id}")
            
            with open(filename_html, "w+") as html_file:
                html_file.write(str(p))    
            print(f"  Wrote HTML file for article {id}")
            
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
                        print(f"  Decomposing standalone TOC header '{header.name}' and subsequent list '{next_sibling.name}'.")
                        header.decompose()
                        next_sibling.decompose()
            
            # Convert tables with class 'source_code_container' to <pre><code> blocks
            # These tables were used as a workaround for code blocks.
            for table in p.find_all('table', class_='source_code_container'):
                print(f"  Converting source code table to <pre> block for article {id}...")
                pre = p.new_tag("pre")
                # Convert <td> with 'source_code' class to <code>.
                for td in table.find_all('td', class_='source_code'):
                    td.name = "code"
                    for par in table.find_all('p'):
                        if par.string:
                            par.replace_with(par.string)
                    pre.append(td)
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
                
                # Replace Related Articles heading with placeholder
                print(f"    Processing 'Связанные статьи' for article {id}...")
                markdown = markdown.replace('## Связанные статьи', '--8<-- "related_topics_heading.md"')
                print(f"    'Связанные статьи' processed for article {id}")
                
                # Replace product names with placeholders
                print(f"    Processing product names for article {id}...")
                markdown = markdown.replace('Comindware Platform', '{{ productName }}')
                markdown = markdown.replace('Comindware Business Application Platform', '{{ productName }}')
                markdown = markdown.replace('Comindware Platform Enterprize', '{{ productNameEnterprize }}')
                markdown = markdown.replace('Корпоративная архитектура', '{{ productNameArchitect }}')
                print(f"    Product names processed for article {id}")
                
                # Reformat images with captions
                print(f"    Processing image captions for article {id}...")
                pattern = re.compile(r'(!\[(.*)\]\(.*\))\n\n\2', flags=re.MULTILINE)
                markdown = re.sub(pattern, r'_\1_', markdown)
                print(f"    Image captions processed for article {id}")

                # Reformat images in italics with trailing caption (special for kb.cmwlab.com/assets)
                print(f"    Processing italics images with trailing captions for article {id}...")
                pattern = re.compile(r'(_!\[]\((https://kb\.cmwlab\.com/assets/[^)]+)\)_)([^\n]+)', flags=re.MULTILINE)
                markdown = re.sub(pattern, r'_![\3](\2)_', markdown)
                print(f"    Italics images with trailing captions processed for article {id}")

                # Sanitize fenced code blocks to use 3 backticks instead of 4 or more, preserving indentation.
                print(f"    Sanitizing fenced code blocks for article {id}...")
                markdown = re.sub(r'`{4,}', r'```', markdown, flags=re.MULTILINE)
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
            frontmatter = '\n'.join([
                '---',
                f'title: {title}',
                f'kbId: {id}',
                '---',
                '\n'
                ])
            # Add link map to the bottom
            footer = '{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}\n'
            markdown = frontmatter + markdown.rstrip() + '\n\n' + footer
            print(f"  Frontmatter added for article {id}")
            
            print(f"  Processing article links for article {id}...")
            pattern = re.compile(r'`!\[.*\]\(.*\) *(.*?) *\{Article-ID:(\d+)\}.*?`', flags=re.MULTILINE)
            # markdown = re.sub(pattern, r'[\2](https://kb.comindware.ru/article.php?id=\3)', markdown)
            # markdown = re.sub(pattern, r'[\1](https://kb.comindware.ru/article.php?id=\2)', markdown)
            for result in re.finditer(pattern, markdown):
                articleId = result.group(2)
                c.execute(f"""
                    SELECT phpkb_articles.article_title 
                    FROM phpkb_articles
                    WHERE article_show='yes' 
                    AND phpkb_articles.article_id={articleId}
                    LIMIT 1
                    """)
                
                foundArticle = c.fetchall()
                if foundArticle:
                    articleName = foundArticle[0][0]
                    replacementRegex = fr'[{articleName}](https://kb.comindware.ru/article.php?id=\2)'
                    markdown = re.sub(pattern, replacementRegex, markdown, count=1)
            print(f"  Article links processed for article {id}")
            
            print(f"  Processing hyperlinks for article {id}...")
            # Replace article links in markdown with URL from hyperlinks map
            pattern = r'\(https://kb\.comindware\.ru.+?((article\\?\.php\\?\?id=)|-)(\d+)(?(2)|\.html)(#?)(.*?)\)'
            foundLinks = re.finditer(pattern, markdown)
            for link in foundLinks:
                article_id = link.group(3)
                anchor = ''
                if link.group(4) == '#':
                    anchor = link.group(5)
                url = find_url_in_snippet(article_id, anchor)
                if url:
                    pattern = r'\(https://kb\.comindware\.ru.+?((article\\?\.php\\?\?id=)|-)({0})(?(2)|\.html).*?\)'.format(article_id)
                    markdown = re.sub(pattern, url, markdown, count=1)
                    print (f'Replaced {link.group(0)} with {url}')
            print(f"  Hyperlinks processed for article {id}")
            
            print(f"  Writing markdown file for article {id}...")
            #markdown = markdown.replace('https://kb.comindware.ru/category.php?id=', '{{ kbCategoryURLPrefix }}')
            b.write(markdown)
            print(f"  Markdown file written for article {id}")
            # print(html.escape(str(p)))
            pages += 1
            print(f"Completed article {id}")
    TOTAL_PAGES_IMPORTED += pages
    print("\nImported {} articles, total {}\n\n-----\n".format(pages, TOTAL_PAGES_IMPORTED))
    return pages


def fetchCategories(show='yes', status='public', language_id=1, parent_id=''):

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


def listCategories(categories):
    index = 1
    for id, title, parent_id in categories:
        print(f"{index}. {id}. {title}")
        index += 1

def main():
    
    global KB_ID_TO_TITLE_MAP
        
    KB_ID_TO_TITLE_MAP = loadMappingJson(KB_ID_TO_TITLE_MAP_FILE)
    
    if len(KB_ID_TO_TITLE_MAP) == 0:
        KB_ID_TO_TITLE_MAP = dict()
    
    with open(".serverCredentialsCmwlab.json", "r") as serverCredentialsFile: 
        
        serverCredentialsFileContent = serverCredentialsFile.read()
        serverCredentials = json.loads(serverCredentialsFileContent) if serverCredentialsFileContent else dict()
    
    sql_hostname = serverCredentials['sql_hostname'] or input("SQL_hostname:\n")
    ssh_host = serverCredentials['ssh_host'] or input("PHPKB host:\n")
    ssh_username = serverCredentials['ssh_username'] or input('SSH username:\n')

    sql_username = serverCredentials['sql_username'] or input("SQL username:\n")
    sql_password = getpass("SQL password:\n")
    sql_database = serverCredentials['sql_database'] or input("Database name:\n")
    sql_port = serverCredentials['sql_port'] or input("SQL remote port:\n")
    sql_port_local = serverCredentials['sql_port_local'] or input("SQL local port:\n")
    sql_ip = serverCredentials['sql_ip'] or input("SQL remote IP:\n")  
        
    # if input('Save credentials? Y / N').lower() == 'y':
    #     with open(".serverCredentials.json", "w") as serverCredentialsFile: 
    #         credentialsJson = json.dumps(serverCredentials, indent = 4)
    #         serverCredentialsFile.write(credentialsJson)

    # Setup SSHTunnelForwarder. It will automatically use your ~/.ssh/config.
    # If the key is passphrase-protected, you might be prompted for it.
    server = SSHTunnelForwarder(
        ssh_host,
        ssh_username=ssh_username,
        remote_bind_address=(sql_ip, sql_port),
        local_bind_address=(sql_ip, sql_port_local)
    )

    server.start()
    # print(server.local_bind_port)
    global CONNECTION
    # with server as tunnel:
    CONNECTION = mysql.connector.MySQLConnection(
        user = sql_username,
        password = sql_password,
        host = sql_ip,
        port = server.local_bind_port,
        database = sql_database
    )
    
    importChildren = ''
    categoryId = ''
    parent_category = ''
    categoryChoice = ''

    print('\nRoot categories:\n')

    while importChildren != 'y':
        
        
        categoryChoice = ''
        
        categories = fetchCategories(parent_id=categoryId)
        if parent_category: print("\nParent: {}. {}\n".format(categoryId, categoryTitle))
        
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
                importChildren = input(f"\nEnter `Y` to import all child categories and articles. \n Or choose a category to browse (1 to {childrenCategoriesNumber}). \n").lower()
            else:
                print('\nIt has no child categories')
                importChildren = input(f"\nEnter `Y` to import all articles from this category. ").lower()
                if importChildren != 'y':
                    print('Imported nothing')
                    break
        elif len(categories) > 1:
            parent_category = categories[0]
            listCategories(categories)
            print("\n---------\n")
            
            if importChildren.isnumeric() and int(importChildren) <= len(categories):
                    categoryChoice = int(importChildren)-1
                    importChildren = 'y'
            else:    
                while not (categoryChoice.isnumeric() and int(categoryChoice) <= len(categories)):
                    categoryChoice = input("Choose category to browse (1 to {}): ".format(len(categories)))
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
                importChildren = input("\nEnter `Y` to import all child categories and articles. \n Or choose a category to browse (1 to {}). \n".format(childrenCategoriesNumber)).lower()
            else: 
                print ('\nIt has no child categories')
                importChildren = input("\nEnter `Y` to import all articles from this category. ".format(categoryId, categoryTitle)).lower()
                if importChildren !='y': 
                    print('Imported nothing')
                    break

    else:
        if len(categories) > 1 and categories[categoryChoice]:
            importCategoryChildren(categories[categoryChoice], KB_DIR)
        elif len(categories) == 1:
            importCategoryChildren(categories[0], KB_DIR)
        
    
    CONNECTION.close()
    server.close()
    server.stop()
    
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
        
        # Build the mapping from kbId to filenames
        for root, _, files in os.walk(docs_dir):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    filename = os.path.splitext(file)[0]
                    if not filename=='index':
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
                    KB_ID_TO_FILENAME_MAP[str(article_id)] = articleAnchor
                elif foundTitle:
                    KB_ID_TO_FILENAME_MAP[str(article_id)] = foundTitle
            except (IOError, UnicodeDecodeError):
                # If hyperlinks file can't be read, use title as fallback
                if foundTitle:
                    KB_ID_TO_FILENAME_MAP[str(article_id)] = foundTitle
                
                
    # Lookup in the cached dictionary
    return KB_ID_TO_FILENAME_MAP.get(str(article_id))

def updateMappingJson(key, value, mapping, mappingFilename):
    mapping.update({str(key):value})
    with open(mappingFilename, "w") as mappingFile: 
        mappingJson = json.dumps(mapping, indent = 4, ensure_ascii=False)
        print(mappingJson)
        mappingFile.write(mappingJson)
        
def loadMappingJson(mappingFilename):

    with open(mappingFilename, "r") as mappingJsonFile: 
        mappingJsonFileContent = mappingJsonFile.read()
        mappingJson = json.loads(mappingJsonFileContent) if mappingJsonFileContent else dict()
        return mappingJson

if __name__ == "__main__":
    main()