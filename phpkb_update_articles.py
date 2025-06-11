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
import datetime 

TOTAL_PAGES_UPDATED = 0
CONNECTION = None
KB_CONTENT_FOLDER = 'for_kb_import_ru'


def updateCategoryChildren(parent):
    c = CONNECTION.cursor(buffered=True)
    
    id = parent[0]
    title = parent[1]
    parentId = parent[2]
  
    c.execute(f"""
        SELECT DISTINCT (category_id), category_name, parent_id
        FROM phpkb_categories 
        WHERE 
        -- category_show='yes' 
        -- AND category_status = 'public'
        -- AND 
        phpkb_categories.language_id = 2
        AND parent_id = {id}
        """)
    children = c.fetchall()
    print(f"\n-----\n\nCategory {id}. {title}. Children: {children}\n")
    print(f'Updating articles from Category {id}. {title}.')
    updateArticlesInCategory(id)
    for child in children:
        updateCategoryChildren(child)
    return children
    
        
def updateArticlesInCategory (category_id):
    c = CONNECTION.cursor(buffered=True)
    c.execute(f"""
            SELECT DISTINCT (phpkb_articles.article_id), phpkb_articles.article_content, phpkb_articles.article_title 
            FROM phpkb_articles, phpkb_relations, phpkb_categories 
            WHERE 
            -- article_show='yes' 
            -- AND 
            phpkb_relations.category_id = {category_id} 
            AND phpkb_relations.article_id = phpkb_articles.article_id
            """)
    
    articles = c.fetchall()
    global TOTAL_PAGES_UPDATED
    pages = 0
    for id, content, title in articles:
        sanitizedTitle=sanitize_filename(title)
        filename = f"{id} - {sanitizedTitle}"
        print ('    Updating article: ' + filename)
        pages += 1
        updateArticle(id)
    TOTAL_PAGES_UPDATED += pages
    print(f"\nUpdated {pages} articles, total {TOTAL_PAGES_UPDATED}\n\n-----\n")
    return pages


def updateArticle(article_id):
    
    contentFound = False
    article_content = None
    
    c = CONNECTION.cursor() #(buffered=True)
    c.execute(f"""
            SELECT article_content, article_title, article_keywords from phpkb_articles WHERE article_id={article_id};
            """)
    
    result = c.fetchone()
    
    if not result:
        print(f'Article {article_id} not found in the PHPKB database')
        return False
    
    article_title = result[1]
    article_keywords = result[2]
    content_result = getArticleContentById(article_id)
    
    if content_result is None:
        print(f'Content for article {article_id} not found in files')
        return False
        
    article_content, mkdocs_title, mkdocs_tags = content_result
    
    # Escape the HTML and backslashes for MySQL
    article_content = html.escape(article_content).replace('\\','\\\\')
    mkdocs_title = html.escape(mkdocs_title).replace('\\','\\\\')
    contentFound = True
    
    if contentFound:
        try:
            update = input(f"KB title:     {article_title}\nKB tags:      {article_keywords}\nUpdate article {article_id} content, title and tags? Y/N\n").lower() == 'y'
            if update:
                article_last_updation = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                c.execute("""
                        UPDATE phpkb_articles 
                        SET 
                        article_title=%s,
                        article_content=%s,
                        article_last_updation=%s,
                        article_status='approved',
                        article_show='yes',
                        article_keywords=%s
                        WHERE article_id=%s;
                        """, (mkdocs_title, article_content, article_last_updation, mkdocs_tags, article_id))
                CONNECTION.commit()
                print(f"Updated article {article_id} updated")
                return True
        except:
            print(f"Failed to update the article {article_id}")
            return False

    return False

def fetchCategories(show='yes', status='public', language_id=2, parent_id=''):

    c = CONNECTION.cursor()    

    c.execute(f"""
            SELECT DISTINCT category_id, category_name, parent_id
            FROM phpkb_categories 
            WHERE 
            -- category_show = '{show}' 
            -- AND category_status = '{status}'
            -- AND 
            phpkb_categories.language_id = {language_id}
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
    
    
    with open(".serverCredentials.json", "r") as serverCredentialsFile: 
        
        serverCredentialsFileContent = serverCredentialsFile.read()
        serverCredentials = json.loads(serverCredentialsFileContent) if serverCredentialsFileContent else dict()
    
    sql_hostname = serverCredentials['sql_hostname'] or input("SQL_hostname:\n")
    ssh_host = serverCredentials['ssh_host'] or input("PHPKB host:\n")
    ssh_username = serverCredentials['ssh_username'] or input('SSH username:\n')
    ssh_password = getpass("SSH password:\n")
    sql_username = serverCredentials['sql_username'] or input("SQL username:\n")
    sql_password = getpass("SQL password:\n")
    sql_database = serverCredentials['sql_database'] or input("Database name:\n")
    sql_port = serverCredentials['sql_port'] or input("SQL remote port:\n")
    sql_port_local = serverCredentials['sql_port_local'] or input("SQL local port:\n")
    sql_ip = serverCredentials['sql_ip'] or input("SQL remote IP:\n")  

    server = SSHTunnelForwarder(
        ssh_host,
        ssh_username=ssh_username,
        ssh_password=ssh_password,
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
    

    if input('Update specific articles? Y/N\n').lower() == 'y':
        article_id = ''
        while article_id.lower() != 'e':
            article_id = str(input('Enter article ID to update or E to exit: '))
            if article_id.lower() == 'e':
                break
            if article_id.isnumeric():
                success = updateArticle(article_id)
                if not success:
                    print("Please try another article ID or press 'E' to exit")
            else:
                print("Please enter a valid numeric article ID or 'E' to exit")
    else:
        updateChildren = ''
        categoryId = ''
        parent_category = ''
        categoryChoice = ''
        
        print('\nRoot categories:\n')

        while updateChildren != 'y':
            
            
            categoryChoice = ''
            categories = fetchCategories(parent_id=categoryId)
            if parent_category: print("\nParent: {}. {}\n".format(categoryId, categoryTitle))
            if len(categories)>1: 
                parent_category = categories[0]
                listCategories(categories)
                print("\n---------\n")
                
                if updateChildren.isnumeric() and int(updateChildren) <= len(categories):
                        categoryChoice = int(updateChildren)-1
                        updateChildren = 'y'
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
                    updateChildren = input("\nEnter `Y` to update the category and all its child categories and articles. \n Or choose a category to browse (1 to {}). \n".format(childrenCategoriesNumber)).lower()
                else: 
                    print ('\nIt has no child categories')
                    updateChildren = input("\nEnter `Y` to update the category and all articles from this category. ".format(categoryId, categoryTitle)).lower()
                    if updateChildren !='y': 
                        print('Updated nothing')
                        break

        else:
            if categories[categoryChoice]:
                updateCategoryChildren(categories[categoryChoice])
        
    
    CONNECTION.close()
    server.close()
    server.stop()
       

def getArticleContentById(article_id):
    
    content = None
    foundMatch = None
    
    if not os.path.isdir(KB_CONTENT_FOLDER):
        raise FileNotFoundError(f"The directory '{KB_CONTENT_FOLDER}' does not exist.")
    
    for root, _, files in os.walk(KB_CONTENT_FOLDER):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    kbIdPattern = re.compile(fr'<div.*kb-id="({article_id})".*?>', flags=re.MULTILINE)
                    foundMatch = kbIdPattern.search(content)
                    if foundMatch:
                        print(f'Found content for article {foundMatch.group(1)}')
                        titlePattern = re.compile(fr'<div.*kb-title="(.+?)".*?>', flags=re.MULTILINE)
                        title = titlePattern.search(content).group(1)
                        print(f'MkDocs title: {title}')
                        
                        # Extract tags from the HTML content
                        tags = ""
                        kb_tags_pattern = re.compile(r'kb-tags="([^"]*)"')
                        tags_match = kb_tags_pattern.search(content)
                        if tags_match:
                            tags = tags_match.group(1)
                            # Ensure tags don't exceed varchar(250) while keeping complete tags
                            tag_list = tags.split(',')
                            while len(tags) > 250:
                                # Split tags and keep only those that fit within 250 chars      
                                tag_list.pop(len(tag_list)-1)
                                tags = ','.join(tag_list)
                        print(f'MkDocs tags:  {tags}')
                        return content, title, tags
                    else: content = None

    return None
        

if __name__ == "__main__":
    main()