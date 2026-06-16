---
name: scrape-sanitize
description: Crawl and sanitize external websites for LLM ingestion. Use when needing to crawl comindware.ru or cmwlab.com, sanitize scraped content, or manage the crawl→sanitize pipeline. Supports --fresh (from scratch) and --resume (checkpoint) workflows.
---

# Scrape & Sanitize Pipeline

Crawl external websites and sanitize the output for LLM ingestion.

## Architecture

```
scraping/{site}/
├── progress_{date}.json           # Crawl progress (tracked, for resumability)
├── sanitize_checkpoint.json        # Sanitizer checkpoint (tracked, for resumability)
└── sanitized_{date}.md             # Final sanitized output (tracked)

.scratch/
└── {site}_dirty_{date}.md          # Raw crawl output (gitignored, disposable)
```

## Scripts

| Script | Purpose |
|---|---|
| `scripts/crawl4ai_ingest.py` | Async crawl via crawl4ai (sitemap → markdown) |
| `scripts/http_bs4_ingest.py` | Sync crawl via requests+BS4 (markdownify conversion) |
| `scripts/sanitize.py` | Boilerplate pruning, URL decoding, title resolution |

## Usage

### Crawl (crawl4ai)
```bash
python .agents/skills/scrape-sanitize/scripts/crawl4ai_ingest.py --site comindware_ru
python .agents/skills/scrape-sanitize/scripts/crawl4ai_ingest.py --site comindware_ru --fresh  # start from scratch
```

### Sanitize
```bash
python .agents/skills/scrape-sanitize/scripts/sanitize.py --site comindware_ru --date 20260616
python .agents/skills/scrape-sanitize/scripts/sanitize.py --site comindware_ru --date 20260616 --fresh
```

### Full pipeline
```bash
python scripts/crawl4ai_ingest.py --site comindware_ru --fresh
python scripts/sanitize.py --site comindware_ru --date 20260616 --fresh
```

## Resumability

- **Crawl**: `scraping/{site}/progress_{date}.json` tracks processed URLs. Resume with `--resume` (default). Clear with `--fresh`.
- **Sanitize**: `scraping/{site}/sanitize_checkpoint.json` tracks processed articles. Resume with `--resume` (default). Clear with `--fresh`.

## Site config

| Site key | Target | Crawler |
|---|---|---|
| `comindware_ru` | https://www.comindware.ru | crawl4ai |
| `cmwlab_com` | https://kb.cmwlab.com | http_bs4 |
