"""
Shared utilities for scrape-sanitize pipeline scripts.
Import from this module to avoid code duplication across ingestor/sanitizer.
"""
import os
import json
import argparse
from datetime import datetime

# --- Paths ---
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
        'start_url': 'https://www.cmwlab.com/sitemap/',
        'url_filter': 'https://www.cmwlab.com',
        'title': 'cmwlab.com knowledge base for AI ingestion',
    },
}

ARTICLE_SEP = '================================================'
DATE_SUFFIX = datetime.now().strftime('%Y%m%d')


def resolve_paths(site, date_suffix=None):
    """Return dict of paths for the given site and date."""
    if date_suffix is None:
        date_suffix = DATE_SUFFIX
    scraping_dir = os.path.join(REPO_ROOT, 'scraping', site)
    return {
        'scraping_dir': scraping_dir,
        'dirty_input': os.path.join(SCRATCH_DIR, f'{site}_dirty_{date_suffix}.md'),
        'dirty_output': os.path.join(SCRATCH_DIR, f'{site}_dirty_{date_suffix}.md'),
        'sanitized': os.path.join(scraping_dir, f'{site}_sanitized_{date_suffix}.md'),
        'progress': os.path.join(scraping_dir, f'progress_{date_suffix}.json'),
        'checkpoint': os.path.join(scraping_dir, 'sanitize_checkpoint.json'),
        'url_cache': os.path.join(SCRATCH_DIR, 'ralph', 'url_titles.json'),
        'failures': os.path.join(SCRATCH_DIR, 'ralph', f'{site}_failures.log'),
    }


def add_common_args(parser):
    """Add --site, --date, --fresh to an argparse parser."""
    parser.add_argument('--site', required=True, choices=list(SITES.keys()),
                        help='Site key to process.')
    parser.add_argument('--date', type=str, default=DATE_SUFFIX,
                        help=f'Date suffix YYYYMMDD (default: {DATE_SUFFIX}).')
    parser.add_argument('--fresh', action='store_true',
                        help='Delete progress/checkpoint and output, start from black state.')
    return parser


def load_json(path):
    """Load JSON file, return None if not found."""
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


def save_json(data, path):
    """Save JSON to file, creating dirs as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json_set(path):
    """Load JSON array as a set (for crawl progress)."""
    data = load_json(path)
    return set(data) if data else set()


def save_json_set(data_set, path):
    """Save a set as a JSON array."""
    save_json(list(data_set), path)


def append_output(text, filepath):
    """Append text to file with fsync. Creates dirs as needed."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    mode = 'a' if os.path.exists(filepath) else 'w'
    with open(filepath, mode, encoding='utf-8') as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())


def fresh_start(paths, labels=()):
    """Delete files if --fresh: progress/checkpoint + outputs."""
    deleted = []
    files_to_check = [
        paths.get('checkpoint'),
        paths.get('progress'),
        paths.get('sanitized'),
        paths.get('dirty_output'),
    ]
    for f in files_to_check:
        if f and os.path.exists(f):
            os.remove(f)
            deleted.append(os.path.basename(f))
    if deleted:
        print(f'[FRESH] Deleted: {", ".join(deleted)}')
        print('[FRESH] Starting from black state.')
    elif labels:
        print(f'[{"|".join(labels)}] Starting.')
