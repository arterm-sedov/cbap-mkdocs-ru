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
import os, argparse

from common import (
    SITES, DATE_SUFFIX, ARTICLE_SEP, resolve_paths, add_common_args,
    load_json_set, save_json_set, append_output, fresh_start,
)

BATCH_SIZE = 5
BATCH_TIMEOUT = 120
ARTICLE_TIMEOUT = 15

PARSER = argparse.ArgumentParser(description='Crawl website sitemap for AI ingestion.')
add_common_args(PARSER)


def count_tokens(text):
    return len(tiktoken.get_encoding("cl100k_base").encode(text))


async def extract_urls_from_sitemap(crawler, url, url_filter):
    config = CrawlerRunConfig(scraping_strategy=LXMLWebScrapingStrategy(), verbose=False)
    result = await crawler.arun(url, config=config)
    links = []
    if hasattr(result, '__iter__'):
        for r in result:
            links.extend([l['href'] for l in r.links.get('internal', []) if 'href' in l])
    else:
        links = [l['href'] for l in result.links.get('internal', []) if 'href' in l]
    return sorted(set(l for l in links if l.startswith(url_filter)))


async def crawl_article(url, config, crawler):
    try:
        print(f"[CRAWL] {url}")
        results = await asyncio.wait_for(crawler.arun_many([url], config=config), timeout=ARTICLE_TIMEOUT)
        for r in results:
            print(f"[RESULT] {getattr(r, 'url', None)} - {getattr(r, 'success', False)}")
        return results
    except asyncio.TimeoutError:
        print(f"[TIMEOUT] {url}")
        return []
    except Exception as e:
        print(f"[FAIL] {url}: {e}")
        return []


async def main():
    args = PARSER.parse_args()
    cfg = SITES[args.site]
    paths = resolve_paths(args.site, args.date)
    if args.fresh:
        fresh_start(paths)
    output_md = paths['dirty_output']
    progress_file = paths['progress']

    processed = load_json_set(progress_file)
    total_tokens, total_words, total_articles = 0, 0, 0
    ingestion_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not os.path.exists(output_md):
        append_output(
            f"\n----------------------\n\n"
            f"Ingestion date: {ingestion_date}\n"
            f"Title: {cfg['title']}\n"
            f"Source: {cfg['start_url']}\n"
            f"----------------------\n\n"
            "## Articles\n\n",
            output_md)

    async with AsyncWebCrawler() as crawler:
        print(f"[SITEMAP] {cfg['start_url']}")
        all_urls = await extract_urls_from_sitemap(crawler, cfg['start_url'], cfg['url_filter'])
        print(f"[SITEMAP] Found {len(all_urls)} URLs.")
        urls = [u for u in all_urls if u not in processed]
        print(f"[CRAWL] {len(urls)} to process.")

        for i in range(0, len(urls), BATCH_SIZE):
            batch = urls[i:i + BATCH_SIZE]
            print(f"[BATCH {i//BATCH_SIZE+1}] {len(batch)} URLs")
            config = CrawlerRunConfig(scraping_strategy=LXMLWebScrapingStrategy(), verbose=False)
            articles = []
            for u in batch:
                results = await crawl_article(u, config, crawler)
                for r in results:
                    rurl = getattr(r, 'url', None)
                    try:
                        if not getattr(r, 'success', False):
                            print(f"[FAIL] {rurl}")
                            continue
                        md = getattr(r, 'markdown', None)
                        md = md.raw_markdown if md and hasattr(md, 'raw_markdown') else str(md or '')
                        t = count_tokens(md)
                        wc = len(md.split())
                        total_tokens += t; total_words += wc; total_articles += 1
                        title = getattr(r, 'title', '') or ''
                        articles.append(
                            f"{ARTICLE_SEP}\n---\ntitle: {title}\nurl: {rurl}\n"
                            f"tokens: {t}\nwords: {wc}\n---\n\n"
                            f"### [{title}]({rurl})\n\n{md}\n\n---\n")
                        processed.add(rurl)
                    except Exception as e:
                        print(f"[FAIL] {rurl}: {e}")
            if articles:
                append_output(''.join(articles), output_md)
            save_json_set(processed, progress_file)
            print(f"[BATCH] {len(articles)} written, {total_articles} total, {total_tokens} tokens.")

    # Update header with totals
    with open(output_md, 'r', encoding='utf-8') as f:
        content = f.read()
    h1 = content.find('----------------------')
    h2 = content.find('----------------------', h1 + 1)
    if h1 != -1 and h2 != -1:
        nh = ("----------------------\n\n"
              f"Ingestion date: {ingestion_date}\n"
              f"Title: {cfg['title']}\n"
              f"Source: {cfg['start_url']}\n"
              f"Total tokens: {total_tokens}\n"
              f"Total words: {total_words}\n"
              f"Total articles: {total_articles}\n"
              "----------------------\n\n")
        content = nh + content[h2 + 22:]
        with open(output_md, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"Done. {total_articles} articles, {total_tokens} tokens.")

if __name__ == "__main__":
    asyncio.run(main())
