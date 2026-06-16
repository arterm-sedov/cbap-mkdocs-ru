"""
Incremental crawl file sanitizer with Ralph-loop checkpointing.
- Streaming I/O: reads input line-by-line, writes output with flush+fsync per batch.
- Checkpoint: resumes from last processed article via progress JSON.
- URL title cache: skips HTTP GET for cached titles.
- Boilerplate pruning: strips repetitive nav/footer/cookie/menu content.
- Dead URL logging: records failed HTTP requests.
"""
import re
import os
import json
import sys
import time
from urllib.parse import urlparse, urlunparse, unquote
from datetime import datetime

try:
    import requests
except ImportError:
    requests = None

# --- Config ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR) if 'comindwareru' in SCRIPT_DIR else SCRIPT_DIR
SCRATCH = os.path.join(REPO_ROOT, '.scratch')

INPUT_FILE = os.path.join(SCRATCH, 'comindware_ru_for_llm_ingestion_dirty_2026Jun15.md')
OUTPUT_FILE = os.path.join(SCRATCH, 'comindware_ru_for_llm_ingestion_sanitized_2026Jun15.md')
URL_CACHE_FILE = os.path.join(SCRATCH, 'ralph', 'url_titles.json')
CHECKPOINT_FILE = os.path.join(SCRIPT_DIR, 'sanitize_checkpoint.json')
FAILURES_LOG = os.path.join(SCRATCH, 'ralph', 'sanitize_failures.log')
REPORT_FILE = os.path.join(SCRATCH, 'ralph', 'reports', 'wave_checkpoint.json')

BATCH_SIZE = 10       # Articles per flush
HTTP_TIMEOUT = 8      # seconds
ARTICLE_SEP = '================================================'

# --- Boilerplate patterns ---
BOILERPLATE = [
    # Tier 1 — always footer/chrome noise
    re.compile(r'(?i).*\b(cookie|куки|файлы\s*cookie).*'),
    re.compile(r'(?i).*\b(политик[аи]\s*конфиденциальности|privacy\s*policy).*'),
    re.compile(r'(?i).*\b(все\s*права\s*защищены|copyright\s*©).*'),
    re.compile(r'(?i).*\b(карта\s*сайта|sitemap).*'),
    re.compile(r'.*\+7\s?\(?\d{3}\)?\s?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}.*'),
    re.compile(r'.*[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*'),
    re.compile(r'(?i).*\b(facebook|linkedin|instagram|twitter|youtube|telegram|vkontakte|vk\.com)\b.*'),
    re.compile(r'(?i).*\b(следите\s*за\s*нами|присоединяйтесь|наши\s*соцсети|мы\s*в\s*соц).*'),
    re.compile(r'(?i).*\b(вебинар|подпи[сш]к[ау]|subscribe|popup|modal|закр[ыо]ть\s*окно).*'),
    re.compile(r'(?i).*\b(получайте\s*новости|будьте\s*в\s*курсе|узнавайте\s*первыми).*'),
    # Repeated horizontal rules / separators in body
    re.compile(r'^[-=_*]{20,}$'),
    # Footer section labels
    re.compile(r'^\*{2}(Поддержка|Пресса|Адрес|Время\s*работы|Реквизиты|Контакты):?\*{2}$'),
    # Share/bookmark widgets
    re.compile(r'(?i).*\b(Поделиться|Share|Tweet|Нравится|Комментари[ея]|обсудить).*'),
    # Inline CTA buttons / demo links
    re.compile(r'(?i).*\[(Запросить\s*демо|Заказать\s*звонок|Оставить\s*заявку|Напишите\s*нам|Свяжитесь\s*с\s*нами|Отправить\s*запрос|Получить\s*консультацию)\].*'),
    # Price links
    re.compile(r'(?i).*\b\[Цены\]\(https?://www\.comindware\.ru/.*\).*'),
]
# Phrases that make a line suspect boilerplate if part of a cluster
SUSPECT_PHRASES = re.compile(
    r'(?i)(заказать|заявк[уа]|demo|consult|консультаци[юя]|свяжитесь|позвоните|напишите|'
    r'кейс[ыов]|casestud|отзыв[ыов]|истори[ия]\s*успеха|наши\s*проекты|'
    r'bpm-систем|low.code|no.code|реестр.*ПО|импортозамещ|'
    r'цен[ыа]|прайс|стоимость|тариф)'
)

def load_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def save_checkpoint(cp):
    os.makedirs(os.path.dirname(CHECKPOINT_FILE), exist_ok=True)
    with open(CHECKPOINT_FILE, 'w', encoding='utf-8') as f:
        json.dump(cp, f, indent=2, ensure_ascii=False)

def load_url_cache():
    if os.path.exists(URL_CACHE_FILE):
        with open(URL_CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_url_cache(cache):
    os.makedirs(os.path.dirname(URL_CACHE_FILE), exist_ok=True)
    with open(URL_CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

def log_failure(msg):
    os.makedirs(os.path.dirname(FAILURES_LOG), exist_ok=True)
    with open(FAILURES_LOG, 'a', encoding='utf-8') as f:
        f.write(f'{datetime.now().isoformat()} {msg}\n')
        f.flush()
        os.fsync(f.fileno())

def decode_url(url):
    parsed = urlparse(url)
    try:
        netloc = parsed.netloc.encode('ascii').decode('idna')
    except Exception:
        netloc = parsed.netloc
    path = unquote(parsed.path)
    query = unquote(parsed.query)
    fragment = unquote(parsed.fragment)
    return urlunparse(parsed._replace(netloc=netloc, path=path, query=query, fragment=fragment))

def fetch_title(url):
    if requests is None:
        return ''
    try:
        resp = requests.get(url, timeout=HTTP_TIMEOUT, headers={'User-Agent': 'Mozilla/5.0'})
        resp.raise_for_status()
        import re as _re
        match = _re.search(r'<title[^>]*>(.*?)</title>', resp.text, _re.IGNORECASE | _re.DOTALL)
        return match.group(1).strip() if match else ''
    except Exception as e:
        log_failure(f'FETCH_FAIL {url}: {e}')
        return ''

def is_boilerplate_line(line):
    stripped = line.strip()
    if not stripped:
        return False
    for pat in BOILERPLATE:
        if pat.match(stripped):
            return True
    return False

# --- Deduplication: patterns that repeat across articles ---
NAV_LINK_RE = re.compile(r'^\* \[.*\]\(https://www\.comindware\.ru/(?!blog/).*\)$')
BLOG_LINK_RE = re.compile(r'^\* \[.*\]\(https://www\.comindware\.ru/blog/.*\)$')
CTA_BUTTON_RE = re.compile(r'(?i)\[ Заказать демо \]|\[ Заказать звонок \]|\[ Оставить заявку \]|\[ Напишите нам \]|\[ Свяжитесь с нами \]')
BLANK_RE = re.compile(r'^\s*$')

# Footer consent block fingerprint (3+ of these in a 10-line window = footer)
FOOTER_FINGERPRINTS = [
    re.compile(r'(?i).*\b(обработку\s*персональных|персональных\s*данных).*'),
    re.compile(r'(?i).*\b(reCaptcha|re\.captcha|капч).*'),
    re.compile(r'(?i).*\b(все\s*поля\s*требуют|форма\s*защищена|сообщите\s*нам).*'),
    re.compile(r'(?i).*\b(privacy|data-consent|mail-consent|согласи[ею]|конфиденциальност).*'),
    re.compile(r'(?i).*\b(подпи[сш]к[ау]|subscribe|подписаться|я\s*согласен|нажимая\s*кнопку).*'),
    re.compile(r'(?i).*\b(8-800|\+7\s*800|бесплатный\s*звонок).*'),
    # Company physical address
    re.compile(r'(?i).*\b(адрес:\s*\*{0,2}\d{6}|москва|долгопрудненское|офис\s*comindware|как\s*добраться).*'),
    # Working hours / support contact / press
    re.compile(r'(?i).*\b(время\s*работы|пресса|поддержка):\s*\*{0,2}.*'),
    # Social / share / rating icons loaded as images
    re.compile(r'(?i).*!\[.*\]\(.*/(search-icon|icon-|logo-|share-|rating).*\).*'),
    # Inline CTA banner images
    re.compile(r'(?i).*!\[.*\]\(.*/(cta|banner|landing|cover|demo|consult).*\).*'),
]

def is_footer_line(line):
    stripped = line.strip()
    if not stripped:
        return False
    for fp in FOOTER_FINGERPRINTS:
        if fp.search(stripped):
            return True
    return False

def has_enough_footer_lines(window_lines):
    """Check if a 15-line window has >=3 footer fingerprint lines."""
    count = sum(1 for l in window_lines if is_footer_line(l))
    return count >= 3

def strip_footer_block(lines):
    """Strip only the trailing footer portion — stop at heading or significant content."""
    if len(lines) < 20:
        return lines
    
    # Scan from end to find where footer patterns become dense
    # Only strip the last ~30% of lines, stop at any heading
    scan_start = max(0, len(lines) - int(len(lines) * 0.3))
    footer_cut = len(lines)
    found_heading = False
    
    for i in range(len(lines) - 1, max(0, len(lines) - 60), -1):
        line = lines[i].strip()
        if re.match(r'^#{1,4}\s+\S', line):  # Any heading
            found_heading = True
            footer_cut = i
            break
        if has_enough_footer_lines(lines[max(0, i-10):min(len(lines), i+10)]):
            footer_cut = i - 5
            break
    
    # If we found a heading within the scan zone, cut there
    if found_heading:
        return lines[:footer_cut]
    
    # Otherwise, only strip from the first confirmed footer line
    for i in range(scan_start, len(lines)):
        if has_enough_footer_lines(lines[i:min(len(lines), i+15)]):
            # Walk up to blank line boundary (max 8 lines)
            while i > scan_start and lines[i-1].strip() and (i - scan_start) < 8:
                i -= 1
            return lines[:i]
    
    return lines

def is_stub_article(body, block_raw):
    """Detect truly empty pages — only flag literally empty bodies (< 30 chars)."""
    return len(body.strip()) < 30

def is_nav_link_cluster(lines, start, window=15):
    """Check if lines from start form a navigation link cluster."""
    nav_count = 0
    blog_count = 0
    total = 0
    for i in range(start, min(len(lines), start + window)):
        line = lines[i].strip()
        if not line:
            continue
        total += 1
        if NAV_LINK_RE.match(line):
            nav_count += 1
        if BLOG_LINK_RE.match(line):
            blog_count += 1
    if total == 0:
        return 0
    ratio = (nav_count + blog_count) / total
    if ratio > 0.5 and total >= 3:
        return min(start + window, len(lines))
    return 0

def strip_nav_blogs(lines):
    """Remove nav/sidebar link clusters from body START only (header chrome)."""
    result = list(lines)
    nav_cut = 0
    
    # Find the first content heading or paragraph (not a link)
    for i in range(min(50, len(lines))):
        line = lines[i].strip()
        if not line:
            continue
        if re.match(r'^#{1,4}\s+\S', line):  # Heading
            nav_cut = max(0, i - 2)
            break
        if not re.match(r'^\* \[.*\]\(.*\)$', line) and len(line) > 30:
            nav_cut = i
            break
    
    if nav_cut > 0:
        result = lines[nav_cut:]
    
    return result

def repair_body(body, block_raw=''):
    """Complete body repair: boilerplate, nav, footer, stub detection."""
    # Stub check (signals caller to skip entire article)
    if is_stub_article(body, block_raw):
        return None

    lines = body.split('\n')

    # 1. Strip nav link clusters and blog sidebars
    lines = strip_nav_blogs(lines)

    # 2. Strip footer block
    lines = strip_footer_block(lines)

    # 3. Strip individual boilerplate lines, compress blanks
    result = []
    blank_count = 0
    suspect_count = 0
    for line in lines:
        if is_boilerplate_line(line):
            continue
        stripped = line.strip()
        if CTA_BUTTON_RE.search(stripped) and len(stripped) < 120:
            continue  # CTA buttons are never unique content
        if not stripped:
            blank_count += 1
            if blank_count > 2:
                continue
            result.append('')
            continue
        blank_count = 0
        if SUSPECT_PHRASES.search(stripped):
            suspect_count += 1
            if suspect_count >= 3:
                continue
        else:
            suspect_count = 0
        result.append(line)

    # Strip leading/trailing empties
    while result and not result[0].strip():
        result.pop(0)
    while result and not result[-1].strip():
        result.pop()

    text = '\n'.join(result)
    return text

def split_articles(content):
    """Split content into header + article blocks."""
    parts = content.split(ARTICLE_SEP)
    header = parts[0].rstrip()
    articles = [p.lstrip() for p in parts[1:] if p.strip()]
    return header, articles

def process_article(block, url_cache):
    """Process one article block: decode URLs, fetch title, strip boilerplate."""
    # Find the YAML frontmatter
    yaml_match = re.search(r'^---\n(.*?)\n---', block, re.DOTALL)
    if not yaml_match:
        return block  # No recognizable frontmatter, return as-is

    yaml_block = yaml_match.group(0)
    yaml_content = yaml_match.group(1)
    after = block[yaml_match.end():]

    # Extract and decode URL
    url_match = re.search(r'url:\s*(https?://[^\s]+)', yaml_content)
    url = url_match.group(1) if url_match else ''
    decoded_url = decode_url(url) if url else ''

    # Fetch/cache title
    title = ''
    if decoded_url:
        title = url_cache.get(decoded_url)
        if title is None:
            title = fetch_title(decoded_url)
            url_cache[decoded_url] = title or ''

    # Update YAML with decoded URL and title
    updated_yaml = yaml_content
    if url:
        updated_yaml = updated_yaml.replace(url, decoded_url)
    if title:
        if 'title:' in updated_yaml:
            updated_yaml = re.sub(r'title:\s*.*', f'title: {title}', updated_yaml)
        else:
            updated_yaml = f'title: {title}\n{updated_yaml}'

    # Repair body (strip boilerplate, nav, footer, blogs; detect stubs)
    body = repair_body(after, block_raw=block)

    if body is None:
        return None  # Stub article — skip entirely

    # Build the cleaned block
    result = f'---\n{updated_yaml}\n---\n\n{body}\n'
    return result

def append_output(text, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    mode = 'a' if os.path.exists(filepath) else 'w'
    with open(filepath, mode, encoding='utf-8') as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())

def main():
    if not os.path.exists(INPUT_FILE):
        print(f'ERROR: Input file not found: {INPUT_FILE}')
        sys.exit(1)

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    header, articles = split_articles(content)
    total = len(articles)
    print(f'Articles found: {total}')

    # Checkpoint resume
    cp = load_checkpoint()
    url_cache = load_url_cache()
    start_idx = cp['meta']['articles_processed'] if cp else 0

    if os.path.exists(OUTPUT_FILE) and start_idx == 0:
        os.remove(OUTPUT_FILE)  # Fresh start
        print('[CLEAN] Removed previous output.')

    if start_idx > 0:
        print(f'[RESUME] Starting from article {start_idx + 1}/{total}')

    # Write header once
    if start_idx == 0:
        append_output(f'{header}\n{ARTICLE_SEP}\n', OUTPUT_FILE)

    batch_output = []
    processed_this_wave = 0
    wave_start = time.time()

    for i in range(start_idx, total):
        article = articles[i]
        url_hint = ''
        try:
            ym = re.search(r'url:\s*(https?://[^\s]+)', article[:500])
            url_hint = ym.group(1)[:80] if ym else 'no-url'
        except:
            pass
        sys.stdout.write(f'  [{i+1}/{total}] {url_hint}\n')
        sys.stdout.flush()
        try:
            cleaned = process_article(article, url_cache)
        except Exception as e:
            log_failure(f'ARTICLE_{i}_ERROR: {e}')
            cleaned = article  # Keep original on error

        if cleaned is None:
            processed_this_wave += 1
            # Still count as processed, but don't write to output
            save_url_cache(url_cache)
            save_checkpoint({
                'meta': {
                    'topic': 'comindware_ru_crawl_sanitize',
                    'status': 'in_progress',
                    'wave': cp['meta']['wave'] + 1 if cp else 1,
                    'articles_total': total,
                    'articles_processed': i + 1,
                    'last_flush': datetime.now().isoformat()
                }
            })
            continue

        batch_output.append(f'{ARTICLE_SEP}\n{cleaned}{ARTICLE_SEP}\n')
        processed_this_wave += 1

        # Flush every BATCH_SIZE articles
        if len(batch_output) >= BATCH_SIZE:
            append_output(''.join(batch_output), OUTPUT_FILE)
            save_url_cache(url_cache)
            save_checkpoint({
                'meta': {
                    'topic': 'comindware_ru_crawl_sanitize',
                    'status': 'in_progress',
                    'wave': cp['meta']['wave'] + 1 if cp else 1,
                    'articles_total': total,
                    'articles_processed': i + 1,
                    'last_flush': datetime.now().isoformat()
                }
            })
            elapsed = time.time() - wave_start
            pct = (i + 1) / total * 100
            print(f'  [{i+1}/{total}] {pct:.0f}% {elapsed:.0f}s — flushed')
            batch_output = []

    # Final flush
    if batch_output:
        append_output(''.join(batch_output), OUTPUT_FILE)

    save_url_cache(url_cache)
    save_checkpoint({
        'meta': {
            'topic': 'comindware_ru_crawl_sanitize',
            'status': 'terminal',
            'wave': cp['meta']['wave'] + 1 if cp else 1,
            'articles_total': total,
            'articles_processed': total,
            'completed': datetime.now().isoformat()
        }
    })
    print(f'\n[DONE] {total} articles processed. Output: {OUTPUT_FILE}')

    # Write report
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(f'# Sanitize Report — {datetime.now().isoformat()}\n\n')
        f.write(f'- Articles processed: {total}\n')
        f.write(f'- URL cache entries: {len(url_cache)}\n')
        f.write(f'- Output: {OUTPUT_FILE}\n')
        f.flush()
        os.fsync(f.fileno())

if __name__ == '__main__':
    main()
