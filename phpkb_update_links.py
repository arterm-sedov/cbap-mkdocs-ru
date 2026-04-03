from tools.ssh_kb_ru import establish_connection_interactive, close_connection
from tools.graceful_interrupt import safe_input, ensure_cleanup
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

TOTAL_PAGES_UPDATED = 0
CONNECTION = None
# sshtunnel.SSH_TIMEOUT=0.5
# sshtunnel.TUNNEL_TIMEOUT=20.0
MAPPING = dict()


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
        updateArticleLinks(id)
    TOTAL_PAGES_UPDATED += pages
    print(f"\nUpdated {pages} articles, total {TOTAL_PAGES_UPDATED}\n\n-----\n")
    return pages


def updateArticleLinks(article_id):
    
    changesMade = False
    
    c = CONNECTION.cursor() #(buffered=True)
    c.execute(f"""
            SELECT article_content, article_title from phpkb_articles WHERE article_id={article_id};
            """)
    
    result = c.fetchone()
           
    article_content = html.unescape((result[0]))
    
    article_title = result[1]
      
    for oldArticleId in MAPPING['Articles'].keys():
    
        newArticleId = MAPPING['Articles'][oldArticleId]
        
        pattern = re.compile(fr'data-value="{oldArticleId}"', flags=re.MULTILINE)
        replacementRegex = fr'data-value="{newArticleId}"'
        if len(re.findall(pattern, article_content))>0:
            changesMade = True
            article_content = re.sub(pattern, replacementRegex, article_content)
            print(f'Replaced article markers {oldArticleId} : {newArticleId}')


        pattern = re.compile(fr'Article-ID:{oldArticleId}', flags=re.MULTILINE)
        replacementRegex = fr'Article-ID:{newArticleId}'
        if len(re.findall(pattern, article_content))>0:
            changesMade = True
            article_content = re.sub(pattern, replacementRegex, article_content)
            print(f'Replaced article markers {oldArticleId} : {newArticleId}')

        pattern = re.compile(fr'article\.php\?id={oldArticleId}', flags=re.MULTILINE)
        replacementRegex = fr'article\.php\?id={newArticleId}'
        if len(re.findall(pattern, article_content))>0:
            changesMade = True
            article_content = re.sub(pattern, replacementRegex, article_content)
            print(f'Replaced article links {oldArticleId} : {newArticleId}')
        
    for oldCategoryId in MAPPING['Categories'].keys():
    
        newCategoryId = MAPPING['Categories'][oldCategoryId]

        pattern = re.compile(fr'category\.php\?id={oldCategoryId}', flags=re.MULTILINE)
        replacementRegex = fr'category\.php\?id={newCategoryId}'
        if len(re.findall(pattern, article_content))>0:
            changesMade = True
            article_content = re.sub(pattern, replacementRegex, article_content)
            print(f'Replaced category links {oldCategoryId} : {newCategoryId}')
    
    pattern = re.compile(fr'Comindware Business Application Platform', flags=re.MULTILINE)
    replacementRegex = fr'Comindware Platform'
    if len(re.findall(pattern, article_content))>0:
        changesMade = True
        article_content = re.sub(pattern, replacementRegex, article_content)
        print(f'Replaced product name with Comindware Platform in article content')

    if len(re.findall(pattern, article_title))>0:
        changesMade = True
        article_title = re.sub(pattern, replacementRegex, article_title)
        print(f'Replaced product name with Comindware Platform in article title')
        
    pattern = re.compile(fr'(Comindware )?Architect', flags=re.MULTILINE)
    replacementRegex = fr'«Архитектор»'
    if len(re.findall(pattern, article_content))>0:
        changesMade = True
        article_content = re.sub(pattern, replacementRegex, article_content)
        print(f'Replaced Comindware Architect with «Архитектор»')
        
    pattern = re.compile(fr'4\.7', flags=re.MULTILINE)
    replacementRegex = fr'5.0'
    if len(re.findall(pattern, article_title))>0:
        newArticle_title = re.sub(pattern, replacementRegex, article_title)
        if safe_input(f'Replace {article_title} with {newArticle_title} ? Y/N').lower() == 'y':
            changesMade = True
            article_title = newArticle_title
            print(f'Replaced 4.7 with 5.0 in article title: {article_title}')
    
    
    pattern = re.compile(fr'(^.*)(4\.7)(.*$)', flags=re.MULTILINE)
    replacementRegex = fr'\g<1>5.0\g<3>'
    for result in re.finditer(pattern, article_content):
        foundLine = result.group(0)
        print(f'Found line: {foundLine}')
        if safe_input(f'Replace 4.7 with 5.0 ? Y/N').lower() == 'y':
            changesMade = True
            replacedLine = re.sub(pattern, replacementRegex, foundLine)
            article_content = re.sub(pattern, replacementRegex, article_content, count=1)
            print(f'Replaced 4.7 with 5.0 in article content: {replacedLine}')
    
    # # print(f'Updating links in article {article_id}')
    
    article_content = html.escape(article_content)
      
    if changesMade:
        try:
            print("Executing SQL")
            c.execute("""
                    UPDATE phpkb_articles 
                    SET article_title=%s,
                    article_content=%s 
                    WHERE article_id=%s;
                    """, (article_title, article_content, article_id))
        except:
            print("Couldn't update the article")
            exit()
    
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
    
    global MAPPING
    
    MAPPING = loadMappingJson()
    
    if len(MAPPING) == 0:
        print('Empty .mapping.json')
        exit()
    
    global CONNECTION
    server = None
    
    try:
        CONNECTION, server = establish_connection_interactive()
        
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
                    updateChildren = safe_input("\nEnter `Y` to update the category and all its child categories and articles. \n Or choose a category to browse (1 to {})".format(childrenCategoriesNumber)).lower()
                else: 
                    print ('\nIt has no child categories')
                    updateChildren = safe_input("\nEnter `Y` to update the category and all articles from this category.".format(categoryId, categoryTitle)).lower()
                    if updateChildren !='y': 
                        print('Updated nothing')
                        break

        else:
            if categories[categoryChoice]:
                updateCategoryChildren(categories[categoryChoice])
    except KeyboardInterrupt:
        # Connection cleanup handled in finally block
        pass
    finally:
        # Always ensure connections are closed, even on interrupt
        ensure_cleanup(CONNECTION, server)
       
def loadMappingJson():

    with open(".mapping.json", "r") as mappingJsonFile: 
        mappingJsonFileContent = mappingJsonFile.read()
        mappingJson = json.loads(mappingJsonFileContent) if mappingJsonFileContent else dict()
        return mappingJson

if __name__ == "__main__":
    main()