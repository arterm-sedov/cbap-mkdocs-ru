import os
import re

# Define file paths and folder locations
docs_ru_folder = 'docs/ru'
hyperlinks_file = os.path.join(docs_ru_folder, '.snippets/hyperlinks_mkdocs_to_kb_map.md')

# Function to find articleId in a given file
def find_article_id(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Search for the URL pattern in the markdown file
        matches = re.finditer(r'\(https://kb\.comindware\.ru.+((id=)|-)(\d+)(?(2)|\.html).*\)', content)
        return matches
    return None

# Function to search for the file with kbId: articleId in docs/ru
def search_kbId_in_docs(article_id):
    for root, dirs, files in os.walk(docs_ru_folder):
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    # Search for kbId: {articleId} pattern
                    if re.search(fr'kbId:\s*{article_id}', content):
                        return file_path
    return None

# Function to search for pattern in hyperlinks file and replace
def find_hyperlink_in_snippet(article_id):
    with open(hyperlinks_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for line in lines:
        # Search for the url with articleId
        match = re.search(fr'(\[.*?\]):.*{article_id}', line)
        if match and match.group(1):
            url = match.group(1)
            print(f"Found linkd and URL for articleId {article_id}: {url}")
            return url
    return None

# Main function to process markdown file
def process_markdown_file(md_file_path):
    article_ids = find_article_id(md_file_path)   
    if not article_ids:
        print("No articleId found in the file.")
        return

    for result in article_ids:
        article_id = result.group(3)
        url = find_hyperlink_in_snippet(article_id)
        
md_file_path = 'article-2198.md'
process_markdown_file(md_file_path)
