import mysql.connector
from sshtunnel import SSHTunnelForwarder
from getpass import getpass
from html.parser import HTMLParser
import bs4
from markdownify import markdownify as md
import re
from pathvalidate import sanitize_filename
from pathlib import Path
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

MAPPING = dict()
CATEGORY_MAPPING = dict()
ARTICLE_MAPPING = dict()
# CATEGORY_COUNTER = 0

def cloneCategoryChildren(parent, newParentId=''):
    c = CONNECTION.cursor(buffered=True)
    
    id = parent[0]
    title = parent[1]
    parentId = parent[2]
    
    if newParentId:
        parentId = newParentId
    
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
        c.execute(f"""
                DROP TABLE tmp;
                """)
        c.execute(f"""
                SELECT MAX(article_id) FROM phpkb_articles;
                """)
        
        newArticleId = str(c.fetchone()[0])
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
            INSERT INTO phpkb_relations (article_id, category_id, article_priority)
            VALUES ({newArticleId}, {newCategoryId}, {article_priority});
            """)

    return newArticleId

def cloneCategory(category_id, newParentId):
    c = CONNECTION.cursor(buffered=True)
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
    c.execute(f"""
            DROP TABLE tmp;
            """)
    c.execute(f"""
            SELECT MAX(category_id) FROM phpkb_categories;
            """)
    
    newCategoryId = str(c.fetchone()[0])
    
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


def listCategories(categories):
    index = 1
    for id, title, parent_id in categories:
        print(f"{index}. {id}. {title}")
        index += 1

def clone_specific_article(article_id):
    c = CONNECTION.cursor(buffered=True)
    c.execute(f"SELECT category_id FROM phpkb_relations WHERE article_id={article_id} LIMIT 1")
    result = c.fetchone()
    if not result:
        print(f"Article {article_id} is not in any category and cannot be cloned.")
        return False
    original_category_id = result[0]

    newCategoryId = input(f"Enter target category ID to clone article {article_id} into (or press Enter to clone to the same category {original_category_id}): ")
    
    if not newCategoryId:
        newCategoryId = original_category_id
    elif not newCategoryId.isnumeric():
        print("Invalid Category ID. It must be a number.")
        return False
        
    suffix = "_CLONE"
    newArticleId = cloneArticle(article_id, original_category_id, newCategoryId, suffix, show=False)
    if newArticleId:
        print(f"Article {article_id} cloned as new article {newArticleId} into category {newCategoryId}")
        ARTICLE_MAPPING.update({article_id:newArticleId})
        return True
    return False

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
    
    if input('Clone specific articles? Y/N\n').lower() == 'y':
        article_id = ''
        while article_id.lower() != 'e':
            article_id = str(input('Enter article ID to clone or E to exit: '))
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
                    cloneChildren = input("\nEnter `Y` to clone the category and all its child categories and articles. \n Or choose a category to browse (1 to {}). \n".format(childrenCategoriesNumber)).lower()
                else: 
                    print ('\nIt has no child categories')
                    cloneChildren = input("\nEnter `Y` to clone the category and all articles from this category. ".format(categoryId, categoryTitle)).lower()
                    if cloneChildren !='y': 
                        print('Cloned nothing')
                        break

        else:
            if categories[categoryChoice]:
                # cloneParent = input("\nEnter `Y` to clone the parent category itself along with its children. ".format(categoryId, categoryTitle)).lower() == 'y'
                cloneCategoryChildren(categories[categoryChoice])
        
    
    CONNECTION.close()
    server.close()
    server.stop()
    updateMappingJson()

def updateMappingJson():
    MAPPING.update({'Categories':CATEGORY_MAPPING, 'Articles':ARTICLE_MAPPING})
    #if input('Save mapping? Y / N\n').lower() == 'y':
    with open(".mapping.json", "w") as mappingFile: 
        mappingJson = json.dumps(MAPPING, indent = 4, ensure_ascii=False)
        print(mappingJson)
        mappingFile.write(mappingJson)

if __name__ == "__main__":
    main()