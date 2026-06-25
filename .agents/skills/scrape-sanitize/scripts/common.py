"""
Shared utilities for scrape-sanitize pipeline scripts.
Import from this module to avoid code duplication across ingestor/sanitizer.
"""
import os
import sys
import json
import argparse
from datetime import datetime

# --- Paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR))))
SCRATCH_DIR = os.path.join(REPO_ROOT, '.scratch')

if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.text_io import (
    open_text_append,
    open_text_write,
    write_text as write_repo_text,
)

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
    with open_text_write(path) as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)


def load_json_set(path):
    """Load JSON array as a set (for crawl progress)."""
    data = load_json(path)
    return set(data) if data else set()


def save_json_set(data_set, path):
    """Save a set as a JSON array."""
    save_json(list(data_set), path)


def append_output(text, filepath):
    """Append text to file with fsync. Creates dirs as needed."""
    opener = open_text_append if os.path.exists(filepath) else open_text_write
    with opener(filepath) as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())


def write_output(path, content):
    """Overwrite a text file with repository-standard LF endings."""
    write_repo_text(path, content)


def fresh_start(paths, what=('checkpoint', 'dirty_output', 'progress', 'sanitized')):
    """Delete files to start fresh. `what` limits which path keys to clear.
    Sanitizer should use what=('checkpoint', 'sanitized') to avoid deleting crawl artifacts.
    Crawler should use what=('dirty_output', 'progress', 'sanitized', 'checkpoint').
    """
    keys = set(what)
    deleted = []
    for key, path in paths.items():
        if key not in keys or not isinstance(path, str):
            continue
        if os.path.exists(path):
            os.remove(path)
            deleted.append(os.path.basename(path))
    if deleted:
        print(f'[FRESH] Deleted: {", ".join(deleted)}')
        print('[FRESH] Starting from black state.')
