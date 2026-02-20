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
import datetime
# import paramiko

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
    global CONNECTION
    server = None
    
    try:
        CONNECTION, server = establish_connection_interactive()
        
        choice = safe_input('Update specific articles? Y/N').lower()
        
        if choice == 'y':
            article_id = ''
            while article_id.lower() != 'e':
                article_id = safe_input('Enter article ID to update or E to exit')
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
                                print(f'MkDocs tags length exceeds 250 chars:  {len(tags)}')
                                removed_tag = tag_list.pop()
                                print(f'Popping tag: {removed_tag}')
                                tags = ','.join(tag_list)
                        print(f'MkDocs title: {title}')
                        print(f'MkDocs tags:  {tags}')
                        return content, title, tags
                    else: content = None

    return None
        

if __name__ == "__main__":
    main()