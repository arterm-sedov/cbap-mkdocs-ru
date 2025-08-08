import re
from urllib.parse import urlparse, urlunparse, unquote
import requests
from bs4 import BeautifulSoup

MD_FILE = 'comindware_ru_for_llm_ingestion_dirty.md'
MD_FILE_SANITIZED = 'comindware_ru_for_llm_ingestion_sanitized2.md'

# Pattern to match blocks with title and url
BLOCK_PATTERN = re.compile(r'(title:\s*)(.*?)\n(url:\s*)(https?://[^\s]+)', re.DOTALL)
# Pattern to match markdown links [text](url)
MD_LINK_PATTERN = re.compile(r'\[(.*?)\]\((https?://[^\s\)]+)\)')

def decode_url(url):
    parsed = urlparse(url)
    # Decode punycode domain if present
    try:
        netloc = parsed.netloc.encode('ascii').decode('idna')
    except Exception:
        netloc = parsed.netloc
    # Decode percent-encoded path
    path = unquote(parsed.path)
    # Decode percent-encoded query and fragment as well
    query = unquote(parsed.query)
    fragment = unquote(parsed.fragment)
    return urlunparse(parsed._replace(netloc=netloc, path=path, query=query, fragment=fragment))

def get_page_title(url):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.title.string.strip() if soup.title and soup.title.string else ''
        return title
    except Exception as e:
        return f'ERROR: {e}'

def process_blocks(text):
    def replacer(match):
        title_prefix, _, url_prefix, url = match.groups()
        decoded_url = decode_url(url)
        page_title = get_page_title(decoded_url)
        return f'{title_prefix}{page_title}\n{url_prefix}{decoded_url}'
    return BLOCK_PATTERN.sub(replacer, text)

def process_md_links(text):
    def replacer(match):
        link_text, url = match.groups()
        decoded_url = decode_url(url)
        if link_text.strip() == '':
            page_title = get_page_title(decoded_url)
            return f'[{page_title}]({decoded_url})'
        else:
            return f'[{link_text}]({decoded_url})'
    return MD_LINK_PATTERN.sub(replacer, text)

def main():
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    # First process blocks, then markdown links
    #new_content = process_blocks(content)
    new_content = process_md_links(content)
    with open(MD_FILE_SANITIZED, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Titles and markdown links updated for all URLs.')

if __name__ == '__main__':
    main() 