import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
import tiktoken
from datetime import datetime
import os
import json

OUTPUT_MD = "comindware_ru_for_llm_ingestion_dirty.md"
PROGRESS_FILE = "comindware_ru_progress_dirty.json"
START_URL = "https://www.comindware.ru/sitemap/"
BATCH_SIZE = 5
BATCH_TIMEOUT = 120  # seconds
ARTICLE_TIMEOUT = 15  # seconds

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
    print(f"[WRITE] Wrote {len(articles)} articles.")

async def extract_urls_from_sitemap(crawler, url):
    config = CrawlerRunConfig(scraping_strategy=LXMLWebScrapingStrategy(), verbose=False)
    result = await crawler.arun(url, config=config)
    links = []
    if hasattr(result, '__iter__'):
        for r in result:
            links.extend([l['href'] for l in r.links.get('internal', []) if 'href' in l])
    else:
        links = [l['href'] for l in result.links.get('internal', []) if 'href' in l]
    return sorted(set([l for l in links if l.startswith("https://www.comindware.ru")]))

async def crawl_article_with_timeout(url, config, crawler):
    try:
        print(f"[CRAWL] About to crawl: {url}")
        results = await asyncio.wait_for(
            crawler.arun_many([url], config=config),
            timeout=ARTICLE_TIMEOUT
        )
        for result in results:
            print(f"[RESULT] {getattr(result, 'url', None)} - {getattr(result, 'success', False)}")
        return results
    except asyncio.TimeoutError:
        print(f"[TIMEOUT] {url} timed out after {ARTICLE_TIMEOUT} seconds. Skipping.")
        return []
    except Exception as e:
        print(f"[FAIL] {url} - Exception: {e}")
        return []

# --- Main batch crawling logic ---
async def main():
    ingestion_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    source_line = f"Source: {START_URL}"
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
                f"Title: Comindware.ru knowledge base for AI ingestion\n"
                f"Description: Provide this file to your AI agent. For better results, add the prompt below\n"
                f"{source_line}\n"
                f"----------------------\n\n"
                "## Prompting instructions\n\n"
                "- Answer the following question: <YOUR_QUESTION>\n"
                "- In your answer, provide links to the referenced articles in the format:\n"
                "  `[URL]`\n\n"
                "## Articles\n\n"
            )

    async with AsyncWebCrawler() as crawler:
        print(f"[SITEMAP] Crawling sitemap to get all URLs...")
        all_urls = await extract_urls_from_sitemap(crawler, START_URL)
        print(f"[SITEMAP] Found {len(all_urls)} URLs in sitemap.")
        urls_to_crawl = [u for u in all_urls if u not in processed_urls]
        print(f"[CRAWL] {len(urls_to_crawl)} URLs to process (excluding already done).")

        for i in range(0, len(urls_to_crawl), BATCH_SIZE):
            batch = urls_to_crawl[i:i+BATCH_SIZE]
            batch_num = i // BATCH_SIZE + 1
            print(f"[BATCH] Crawling batch {batch_num}: {len(batch)} URLs")
            config = CrawlerRunConfig(scraping_strategy=LXMLWebScrapingStrategy(), verbose=False)
            articles = []
            for url in batch:
                results = await crawl_article_with_timeout(url, config, crawler)
                for result in results:
                    url = getattr(result, 'url', None)
                    try:
                        if not getattr(result, 'success', False):
                            print(f"[FAIL] {url} - {getattr(result, 'error_message', 'Unknown error')}")
                            continue
                        md_content = getattr(result, 'markdown', None)
                        if md_content and hasattr(md_content, 'raw_markdown'):
                            md_content = md_content.raw_markdown
                        elif md_content:
                            md_content = str(md_content)
                        else:
                            md_content = ""
                        tokens = count_tokens(md_content)
                        word_count = len(md_content.split())
                        total_tokens += tokens
                        total_words += word_count
                        files_analyzed += 1
                        total_articles += 1
                        title = getattr(result, 'title', '') or ''
                        article = (
                            f"================================================\n"
                            f"---\n"
                            f"title: {title}\n"
                            f"url: {url}\n"
                            f"tokens: {tokens}\n"
                            f"words: {word_count}\n"
                            f"---\n\n"
                            f"### [{title}]({url})\n\n"
                            f"{md_content}\n\n---\n"
                        )
                        articles.append(article)
                        processed_urls.add(url)
                    except Exception as e:
                        print(f"[FAIL] {url} - Exception during article processing: {e}")
            write_batch(articles)
            save_progress(processed_urls)
            print(f"[BATCH] Done batch {batch_num}: {len(articles)} articles written, {files_analyzed} total, {total_tokens} tokens.")

    print(f"Done. {files_analyzed} files, {total_tokens} tokens.")
    print(f"Progress saved in {PROGRESS_FILE}")

    # Update header in output file with totals
    with open(OUTPUT_MD, "r", encoding="utf-8") as f:
        content = f.read()
    header_start = content.find('----------------------')
    header_end = content.find('----------------------', header_start + 1)
    if header_start != -1 and header_end != -1:
        new_header = (
            "----------------------\n\n"
            f"Ingestion date: {ingestion_date}\n"
            "Title: Comindware.ru knowledge base for AI ingestion\n"
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

if __name__ == "__main__":
    asyncio.run(main()) 