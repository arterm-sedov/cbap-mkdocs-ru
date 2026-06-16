"""
Async crawl4ai-based site crawler. Crawls sitemap → markdown output.
Usage:
  python crawl4ai_ingest.py --site comindware_ru
  python crawl4ai_ingest.py --site comindware_ru --fresh
"""
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
import tiktoken
from datetime import datetime
import os, sys, json, argparse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR))))
SCRATCH_DIR = os.path.join(REPO_ROOT, '.scratch')

# --- Site config ---
SITES = {
    'comindware_ru': {
        'start_url': 'https://www.comindware.ru/sitemap/',
        'url_filter': 'https://www.comindware.ru',
        'title': 'Comindware.ru knowledge base for AI ingestion',
    },
    'cmwlab_com': {
        'start_url': 'https://kb.cmwlab.com/sitemap/',
        'url_filter': 'https://kb.cmwlab.com',
        'title': 'cmwlab.com knowledge base for AI ingestion',
    },
}

DATE_SUFFIX = datetime.now().strftime('%Y%m%d')
BATCH_SIZE = 5
BATCH_TIMEOUT = 120
ARTICLE_TIMEOUT = 15

PARSER = argparse.ArgumentParser(description='Crawl website sitemap for AI ingestion.')
PARSER.add_argument('--site', required=True, choices=list(SITES.keys()), help='Site key to crawl.')
PARSER.add_argument('--fresh', action='store_true', help='Delete progress and output, start from black state.')

def resolve_paths(site):
    return {
        'output': os.path.join(SCRATCH_DIR, f'{site}_dirty_{DATE_SUFFIX}.md'),
        'progress': os.path.join(REPO_ROOT, 'scraping', site, f'progress_{DATE_SUFFIX}.json'),
    }

def count_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

def load_progress(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_progress(processed, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(list(processed), f)

def write_batch(articles, output_md):
    if not articles:
        return
    with open(output_md, "a", encoding="utf-8") as f:
        for article in articles:
            f.write(article)
        f.flush()
        os.fsync(f.fileno())
    print(f"[WRITE] Wrote {len(articles)} articles.")

async def extract_urls_from_sitemap(crawler, url, url_filter):
    config = CrawlerRunConfig(scraping_strategy=LXMLWebScrapingStrategy(), verbose=False)
    result = await crawler.arun(url, config=config)
    links = []
    if hasattr(result, '__iter__'):
        for r in result:
            links.extend([l['href'] for l in r.links.get('internal', []) if 'href' in l])
    else:
        links = [l['href'] for l in result.links.get('internal', []) if 'href' in l]
    return sorted(set([l for l in links if l.startswith(url_filter)]))

async def crawl_article_with_timeout(url, config, crawler):
    try:
        print(f"[CRAWL] About to crawl: {url}")
        results = await asyncio.wait_for(
            crawler.arun_many([url], config=config), timeout=ARTICLE_TIMEOUT)
        for result in results:
            print(f"[RESULT] {getattr(result, 'url', None)} - {getattr(result, 'success', False)}")
        return results
    except asyncio.TimeoutError:
        print(f"[TIMEOUT] {url} timed out after {ARTICLE_TIMEOUT}s. Skipping.")
        return []
    except Exception as e:
        print(f"[FAIL] {url} - Exception: {e}")
        return []

async def main():
    args = PARSER.parse_args()
    site_config = SITES[args.site]
    paths = resolve_paths(args.site)
    output_md = paths['output']
    progress_file = paths['progress']
    start_url = site_config['start_url']
    url_filter = site_config['url_filter']
    site_title = site_config['title']

    if args.fresh:
        for f in [progress_file, output_md]:
            if os.path.exists(f):
                os.remove(f)
                print(f'[FRESH] Deleted {os.path.basename(f)}')
        print('[FRESH] Starting crawl from black state.')

    ingestion_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    processed_urls = load_progress(progress_file)
    total_tokens = 0
    total_words = 0
    total_articles = 0

    if not os.path.exists(output_md):
        os.makedirs(os.path.dirname(output_md), exist_ok=True)
        with open(output_md, "w", encoding="utf-8") as f:
            f.write(
                f"\n----------------------\n\n"
                f"Ingestion date: {ingestion_date}\n"
                f"Title: {site_title}\n"
                f"Description: Provide this file to your AI agent.\n"
                f"Source: {start_url}\n"
                f"----------------------\n\n"
                "## Prompting instructions\n\n"
                "- Answer the following question: <YOUR_QUESTION>\n"
                "- In your answer, provide links to the referenced articles.\n\n"
                "## Articles\n\n"
            )

    async with AsyncWebCrawler() as crawler:
        print(f"[SITEMAP] Crawling sitemap: {start_url}")
        all_urls = await extract_urls_from_sitemap(crawler, start_url, url_filter)
        print(f"[SITEMAP] Found {len(all_urls)} URLs.")
        urls_to_crawl = [u for u in all_urls if u not in processed_urls]
        print(f"[CRAWL] {len(urls_to_crawl)} URLs to process.")

        for i in range(0, len(urls_to_crawl), BATCH_SIZE):
            batch = urls_to_crawl[i:i+BATCH_SIZE]
            batch_num = i // BATCH_SIZE + 1
            print(f"[BATCH {batch_num}] {len(batch)} URLs")
            config = CrawlerRunConfig(scraping_strategy=LXMLWebScrapingStrategy(), verbose=False)
            articles = []
            for url in batch:
                results = await crawl_article_with_timeout(url, config, crawler)
                for result in results:
                    rurl = getattr(result, 'url', None)
                    try:
                        if not getattr(result, 'success', False):
                            print(f"[FAIL] {rurl} - {getattr(result, 'error_message', '?')}")
                            continue
                        md_content = getattr(result, 'markdown', None)
                        if md_content and hasattr(md_content, 'raw_markdown'):
                            md_content = md_content.raw_markdown
                        elif md_content:
                            md_content = str(md_content)
                        else:
                            md_content = ""
                        tokens = count_tokens(md_content)
                        total_tokens += tokens
                        total_words += len(md_content.split())
                        total_articles += 1
                        title = getattr(result, 'title', '') or ''
                        articles.append(
                            f"================================================\n"
                            f"---\n"
                            f"title: {title}\n"
                            f"url: {rurl}\n"
                            f"tokens: {tokens}\n"
                            f"words: {len(md_content.split())}\n"
                            f"---\n\n"
                            f"### [{title}]({rurl})\n\n"
                            f"{md_content}\n\n---\n"
                        )
                        processed_urls.add(rurl)
                    except Exception as e:
                        print(f"[FAIL] {rurl} - Exception: {e}")
            write_batch(articles, output_md)
            save_progress(processed_urls, progress_file)
            print(f"[BATCH {batch_num}] Done: {len(articles)} written, {total_articles} total, {total_tokens} tokens.")

    print(f"Done. {total_articles} articles, {total_tokens} tokens.")
    print(f"Progress: {progress_file}")

    with open(output_md, "r", encoding="utf-8") as f:
        content = f.read()
    header_start = content.find('----------------------')
    header_end = content.find('----------------------', header_start + 1)
    if header_start != -1 and header_end != -1:
        new_header = (
            "----------------------\n\n"
            f"Ingestion date: {ingestion_date}\n"
            f"Title: {site_title}\n"
            f"Source: {start_url}\n"
            f"Total tokens: {total_tokens}\n"
            f"Total words: {total_words}\n"
            f"Total articles: {total_articles}\n"
            "----------------------\n\n"
        )
        content = new_header + content[header_end+22:]
        with open(output_md, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    asyncio.run(main())
