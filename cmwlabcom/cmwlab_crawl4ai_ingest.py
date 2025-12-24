import requests
from bs4 import BeautifulSoup
import tiktoken
import os
import json
from datetime import datetime
from urllib.parse import urlparse, urlunparse, unquote
import logging
import re
try:
    from markdownify import markdownify as md
except ImportError:
    print("ERROR: Please install 'markdownify' (pip install markdownify)")
    exit(1)

# --- Logging setup ---
logging.basicConfig(filename="cmwlab_ingest.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

# --- Config ---
OUTPUT_MD = "cmwlab_com_for_llm_ingestion.md"
PROGRESS_FILE = "cmwlab_com_progress.json"
START_URL = "https://www.cmwlab.com/sitemap/"
BATCH_SIZE = 2
MAX_URLS = None  # For testing, process only 2 URLs

# --- Utility functions ---
def count_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_progress(processed_urls):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(list(processed_urls), f)

def write_batch(articles):
    if not articles:
        return
    with open(OUTPUT_MD, "a", encoding="utf-8") as f:
        for article in articles:
            f.write(article)
        f.flush()
        os.fsync(f.fileno())
    log_message(f"Wrote {len(articles)} articles.")

def log_message(msg, level='info'):
    if level == 'info':
        logging.info(msg)
        print(msg)
    elif level == 'error':
        logging.error(msg)
        print('ERROR:', msg)
    elif level == 'warning':
        logging.warning(msg)
        print('WARNING:', msg)
    else:
        logging.debug(msg)
        print('DEBUG:', msg)

# --- Core logic ---
def fetch_html(url):
    try:
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        log_message(f"Failed to fetch {url}: {e}", level='error')
        return None

def extract_title(html):
    soup = BeautifulSoup(html, "lxml")
    title = ''
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    if not title:
        h1 = soup.find('h1')
        if h1 and h1.get_text(strip=True):
            title = h1.get_text(strip=True)
    return title

def clean_html(html):
    soup = BeautifulSoup(html, "lxml")
    # If <article> exists, extract and clean only that
    article_tag = soup.find('article')
    if article_tag:
        soup = BeautifulSoup(str(article_tag), "lxml")
    # Remove all modal dialogs (divs with both 'modal' and 'fade' classes)
    for tag in soup.find_all("div", class_=lambda c: c and 'modal' in c.split() and 'fade' in c.split()):
        tag.decompose()
    # Remove sticky nav/header
    for tag in soup.find_all("div", class_=lambda c: c and 'container-fluid' in c.split() and 'sticky-top' in c.split()):
        tag.decompose()
    # Remove footer
    for tag in soup.find_all("footer"):
        tag.decompose()
    # Remove to-top button
    for tag in soup.find_all("div", id="to-top"):
        tag.decompose()
    # Remove breadcrumbs
    for tag in soup.select("ol.bc"):
        tag.decompose()
    # Remove scripts
    for tag in soup.find_all("script"):
        tag.decompose()
    # Remove related topics and CTA sections
    for tag in soup.find_all("div", class_=lambda c: c and 'container-fluid' in c.split() and 'gradient-double' in c.split()):
        tag.decompose()
    # Remove <div class="container py-3 mb-3">
    for tag in soup.find_all("div", class_=lambda c: c and all(x in c.split() for x in ["container", "py-3", "mb-3"])):
        tag.decompose()
    # Remove all <jdiv> blocks
    for tag in soup.find_all("jdiv"):
        tag.decompose()
    # Remove nav blocks
    for tag in soup.find_all("nav"):
        tag.decompose()
    # Remove all <div> with modal IDs
    modal_ids = ["pricingModal", "trialModal", "demoModal", "contactModal", "newsModal"]
    for modal_id in modal_ids:
        for tag in soup.find_all("div", id=modal_id):
            tag.decompose()
    # Remove all elements with class 'sticky-top'
    for tag in soup.find_all(class_="sticky-top"):
        tag.decompose()
    # Remove all elements with class 'side-block'
    for tag in soup.find_all(class_=lambda c: c and 'side-block' in c.split()):
        tag.decompose()
    # Remove all <aside> elements
    for tag in soup.find_all('aside'):
        tag.decompose()
    # Remove all elements with class 'author'
    for tag in soup.find_all(class_=lambda c: c and 'author' in c.split()):
        tag.decompose()
    return str(soup)

def html_to_markdown_lean(html, url):
    log_message('Using markdownify')
    return md(html)

def extract_urls_from_sitemap(sitemap_url):
    html = fetch_html(sitemap_url)
    if not html:
        return []
    soup = BeautifulSoup(html, "lxml")
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    # Only keep links that start with the main domain
    return sorted(set([l for l in links if l and l.startswith("https://www.cmwlab.com")]))

def process_article(url):
    html = fetch_html(url)
    if not html:
        return None
    title = extract_title(html)
    cleaned_html = clean_html(html)
    markdown = html_to_markdown_lean(cleaned_html, url)
    # Improved cleanup: collapse any sequence of 3+ blank lines (with optional spaces/tabs) to two newlines
    markdown = re.sub(r'(\s*\n){3,}', '\n\n', markdown)
    # Remove leading blank lines from markdown
    markdown = re.sub(r'^\s*\n', '', markdown)
    tokens = count_tokens(markdown)
    word_count = len(markdown.split())
    article = (
        f"================================================\n"
        f"---\n"
        f"title: {title}\n"
        f"url: {url}\n"
        f"tokens: {tokens}\n"
        f"words: {word_count}\n"
        f"---\n\n"
        f"### {title}\n"
        f"{markdown}\n\n---\n"
    )
    log_message(f"Processed article: {url} (title: {title})")
    return article

def main():
    ingestion_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    processed_urls = load_progress()
    total_tokens = 0
    total_words = 0
    files_analyzed = 0
    total_articles = 0
    # Write header if file doesn't exist
    if not os.path.exists(OUTPUT_MD):
        with open(OUTPUT_MD, "w", encoding="utf-8") as f:
            f.write(
                f"\n----------------------\n\n"
                f"Ingestion date: {ingestion_date}\n"
                f"Title: Cmwlab.com knowledge base for AI ingestion\n"
                f"Description: Provide this file to your AI agent. For better results, add the prompt below\n"
                f"Source: {START_URL}\n"
                f"----------------------\n\n"
                "## Prompting instructions\n\n"
                "- Answer the following question: <YOUR_QUESTION>\n"
                "- In your answer, provide links to the referenced articles in the format:\n"
                "  `[URL]`\n\n"
                "## Articles\n\n"
            )
    # Get URLs to crawl
    all_urls = extract_urls_from_sitemap(START_URL)
    urls_to_crawl = [u for u in all_urls if u not in processed_urls][:MAX_URLS]
    #urls_to_crawl = ["https://www.cmwlab.com/"]
    log_message(f"Found {len(urls_to_crawl)} URLs to process.")
    articles = []
    for url in urls_to_crawl:
        article = process_article(url)
        if article:
            articles.append(article)
            processed_urls.add(url)
            total_articles += 1
            total_tokens += count_tokens(article)
            total_words += len(article.split())
    write_batch(articles)
    save_progress(processed_urls)
    # Update header in output file with totals
    with open(OUTPUT_MD, "r", encoding="utf-8") as f:
        content = f.read()
    header_start = content.find('----------------------')
    header_end = content.find('----------------------', header_start + 1)
    if header_start != -1 and header_end != -1:
        new_header = (
            "----------------------\n\n"
            f"Ingestion date: {ingestion_date}\n"
            "Title: Cmwlab.com knowledge base for AI ingestion\n"
            "Description: Provide this file to your AI agent. For better results, add the prompt below\n"
            f"Source: {START_URL}\n"
            f"Total tokens: {total_tokens}\n"
            f"Total words: {total_words}\n"
            f"Total articles: {total_articles}\n"
            "----------------------\n\n"
        )
        content = new_header + content[header_end+22:]
        with open(OUTPUT_MD, "w", encoding="utf-8") as f:
            f.write(content)
    log_message(f"Done. {files_analyzed} files, {total_tokens} tokens.")
    log_message(f"Progress saved in {PROGRESS_FILE}")

if __name__ == "__main__":
    main() 