"""
Unified incremental sanitizer with Ralph-loop checkpointing.
Usage:
  python sanitize.py --site comindware_ru --date 20260616
  python sanitize.py --site comindware_ru --date 20260616 --fresh
"""
import re, os, sys, json, time, argparse
from urllib.parse import urlparse, urlunparse, unquote
from datetime import datetime

try:
    import requests
except ImportError:
    requests = None

# --- Paths (resolved per --site flag) ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR))))
SCRATCH_DIR = os.path.join(REPO_ROOT, '.scratch')

def resolve_paths(site, date_suffix):
    return {
        'input':    os.path.join(SCRATCH_DIR, f'{site}_dirty_{date_suffix}.md'),
        'output_scratch': os.path.join(SCRATCH_DIR, f'{site}_sanitized_{date_suffix}.md'),
        'output_tracked': os.path.join(REPO_ROOT, 'scraping', site, f'sanitized_{date_suffix}.md'),
        'checkpoint': os.path.join(REPO_ROOT, 'scraping', site, 'sanitize_checkpoint.json'),
        'url_cache': os.path.join(SCRATCH_DIR, 'ralph', 'url_titles.json'),
        'failures':  os.path.join(SCRATCH_DIR, 'ralph', f'{site}_failures.log'),
    }

# --- CLI ---
PARSER = argparse.ArgumentParser(description='Sanitize crawled website for LLM ingestion.')
PARSER.add_argument('--site', required=True, help='Site key (comindware_ru, cmwlab_com, ...)')
PARSER.add_argument('--date', type=str, default=datetime.now().strftime('%Y%m%d'),
                    help='Date suffix YYYYMMDD for file lookup.')
PARSER.add_argument('--fresh', action='store_true', help='Delete checkpoint and output, start from black state.')

BATCH_SIZE = 10
HTTP_TIMEOUT = 8
ARTICLE_SEP = '================================================'

# --- Boilerplate patterns ---
BOILERPLATE = [
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
    re.compile(r'^[-=_*]{20,}$'),
    re.compile(r'^\*{2}(Поддержка|Пресса|Адрес|Время\s*работы|Реквизиты|Контакты):?\*{2}$'),
    re.compile(r'(?i).*\b(Поделиться|Share|Tweet|Нравится|Комментари[ея]|обсудить).*'),
    re.compile(r'(?i).*\[(Запросить\s*демо|Заказать\s*звонок|Оставить\s*заявку|Напишите\s*нам|Свяжитесь|Отправить\s*запрос|Получить\s*консультацию)\].*'),
    re.compile(r'(?i).*\b\[Цены\]\(https?://.*\).*'),
]
SUSPECT_PHRASES = re.compile(
    r'(?i)(заказать|заявк[уа]|demo|consult|консультаци[юя]|свяжитесь|позвоните|напишите|'
    r'кейс[ыов]|casestud|отзыв[ыов]|истори[ия]\s*успеха|наши\s*проекты|'
    r'bpm-систем|low.code|no.code|реестр.*ПО|импортозамещ|цен[ыа]|прайс|стоимость|тариф)'
)
CTA_BUTTON_RE = re.compile(r'(?i)\[ Заказать демо \]|\[ Заказать звонок \]|\[ Оставить заявку \]|\[ Напишите нам \]|\[ Свяжитесь с нами \]')

FOOTER_FINGERPRINTS = [
    re.compile(r'(?i).*\b(обработку\s*персональных|персональных\s*данных).*'),
    re.compile(r'(?i).*\b(reCaptcha|re\.captcha|капч).*'),
    re.compile(r'(?i).*\b(все\s*поля\s*требуют|форма\s*защищена|сообщите\s*нам).*'),
    re.compile(r'(?i).*\b(privacy|data-consent|mail-consent|согласи[ею]|конфиденциальност).*'),
    re.compile(r'(?i).*\b(подпи[сш]к[ау]|subscribe|подписаться|я\s*согласен|нажимая\s*кнопку).*'),
    re.compile(r'(?i).*\b(8-800|\+7\s*800|бесплатный\s*звонок).*'),
    re.compile(r'(?i).*\b(адрес:\s*\*{0,2}\d{6}|москва|долгопрудненское|офис\s*comindware|как\s*добраться).*'),
    re.compile(r'(?i).*\b(время\s*работы|пресса|поддержка):\s*\*{0,2}.*'),
    re.compile(r'(?i).*!\[.*\]\(.*/(search-icon|icon-|logo-|share-|rating).*\).*'),
    re.compile(r'(?i).*!\[.*\]\(.*/(cta|banner|landing|cover|demo|consult).*\).*'),
]

# --- Globals set in main() ---
PATHS = {}
CHECKPOINT_FILE = ''
FAILURES_LOG = ''
URL_CACHE_FILE = ''

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
        match = re.search(r'<title[^>]*>(.*?)</title>', resp.text, re.IGNORECASE | re.DOTALL)
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

def is_footer_line(line):
    stripped = line.strip()
    if not stripped:
        return False
    for fp in FOOTER_FINGERPRINTS:
        if fp.search(stripped):
            return True
    return False

def has_enough_footer_lines(window_lines):
    return sum(1 for l in window_lines if is_footer_line(l)) >= 3

def strip_footer_block(lines):
    if len(lines) < 20:
        return lines
    scan_start = max(0, len(lines) - int(len(lines) * 0.3))
    footer_cut = len(lines)
    found_heading = False
    for i in range(len(lines) - 1, max(0, len(lines) - 60), -1):
        line = lines[i].strip()
        if re.match(r'^#{1,4}\s+\S', line):
            found_heading = True
            footer_cut = i
            break
        if has_enough_footer_lines(lines[max(0, i-10):min(len(lines), i+10)]):
            footer_cut = i - 5
            break
    if found_heading:
        return lines[:footer_cut]
    for i in range(scan_start, len(lines)):
        if has_enough_footer_lines(lines[i:min(len(lines), i+15)]):
            while i > scan_start and lines[i-1].strip() and (i - scan_start) < 8:
                i -= 1
            return lines[:i]
    return lines

def strip_nav_blogs(lines):
    result = list(lines)
    nav_cut = 0
    for i in range(min(50, len(lines))):
        line = lines[i].strip()
        if not line:
            continue
        if re.match(r'^#{1,4}\s+\S', line):
            nav_cut = max(0, i - 2)
            break
        if not re.match(r'^\* \[.*\]\(.*\)$', line) and len(line) > 30:
            nav_cut = i
            break
    if nav_cut > 0:
        result = lines[nav_cut:]
    return result

def repair_body(body):
    if len(body.strip()) < 30:
        return None
    lines = body.split('\n')
    lines = strip_nav_blogs(lines)
    lines = strip_footer_block(lines)
    result = []
    blank_count = 0
    suspect_count = 0
    for line in lines:
        if is_boilerplate_line(line):
            continue
        stripped = line.strip()
        if CTA_BUTTON_RE.search(stripped) and len(stripped) < 120:
            continue
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
    while result and not result[0].strip():
        result.pop(0)
    while result and not result[-1].strip():
        result.pop()
    return '\n'.join(result)

def split_articles(content):
    parts = content.split(ARTICLE_SEP)
    header = parts[0].rstrip()
    articles = [p.lstrip() for p in parts[1:] if p.strip()]
    return header, articles

def process_article(block, url_cache):
    yaml_match = re.search(r'^---\n(.*?)\n---', block, re.DOTALL)
    if not yaml_match:
        return block
    yaml_content = yaml_match.group(1)
    after = block[yaml_match.end():]
    url_match = re.search(r'url:\s*(https?://[^\s]+)', yaml_content)
    url = url_match.group(1) if url_match else ''
    decoded_url = decode_url(url) if url else ''
    title = ''
    if decoded_url:
        title = url_cache.get(decoded_url)
        if title is None:
            title = fetch_title(decoded_url)
            url_cache[decoded_url] = title or ''
    updated_yaml = yaml_content
    if url:
        updated_yaml = updated_yaml.replace(url, decoded_url)
    if title:
        if 'title:' in updated_yaml:
            updated_yaml = re.sub(r'title:\s*.*', f'title: {title}', updated_yaml)
        else:
            updated_yaml = f'title: {title}\n{updated_yaml}'
    body = repair_body(after)
    if body is None:
        return None
    return f'---\n{updated_yaml}\n---\n\n{body}\n'

def append_output(text, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    mode = 'a' if os.path.exists(filepath) else 'w'
    with open(filepath, mode, encoding='utf-8') as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())

def main():
    global CHECKPOINT_FILE, FAILURES_LOG, URL_CACHE_FILE
    args = PARSER.parse_args()
    PATHS.update(resolve_paths(args.site, args.date))
    CHECKPOINT_FILE = PATHS['checkpoint']
    FAILURES_LOG = PATHS['failures']
    URL_CACHE_FILE = PATHS['url_cache']
    input_file = PATHS['input']
    output_file = PATHS['output_tracked']

    if args.fresh:
        for f in [CHECKPOINT_FILE, output_file]:
            if os.path.exists(f):
                os.remove(f)
                print(f'[FRESH] Deleted {os.path.basename(f)}')
        print('[FRESH] Starting sanitize from black state.')

    if not os.path.exists(input_file):
        print(f'ERROR: Input file not found: {input_file}')
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    header, articles = split_articles(content)
    total = len(articles)
    print(f'[{args.site}] {total} articles in dirty file')

    cp = load_checkpoint()
    url_cache = load_url_cache()
    start_idx = cp['meta']['articles_processed'] if cp else 0

    if os.path.exists(output_file) and start_idx == 0:
        os.remove(output_file)
        print('[CLEAN] Removed previous output.')

    if start_idx > 0:
        print(f'[RESUME] Starting from article {start_idx + 1}/{total}')

    if start_idx == 0:
        append_output(f'{header}\n{ARTICLE_SEP}\n', output_file)

    batch_output = []
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
            cleaned = article

        if cleaned is None:
            save_url_cache(url_cache)
            save_checkpoint({'meta': {
                'topic': f'{args.site}_sanitize', 'status': 'in_progress',
                'articles_total': total, 'articles_processed': i + 1,
                'last_flush': datetime.now().isoformat()
            }})
            continue

        batch_output.append(f'{ARTICLE_SEP}\n{cleaned}{ARTICLE_SEP}\n')

        if len(batch_output) >= BATCH_SIZE:
            append_output(''.join(batch_output), output_file)
            save_url_cache(url_cache)
            save_checkpoint({'meta': {
                'topic': f'{args.site}_sanitize', 'status': 'in_progress',
                'articles_total': total, 'articles_processed': i + 1,
                'last_flush': datetime.now().isoformat()
            }})
            elapsed = time.time() - wave_start
            print(f'  [{i+1}/{total}] {100*(i+1)//total}% {elapsed:.0f}s — flushed')
            batch_output = []

    if batch_output:
        append_output(''.join(batch_output), output_file)

    save_url_cache(url_cache)
    save_checkpoint({'meta': {
        'topic': f'{args.site}_sanitize', 'status': 'terminal',
        'articles_total': total, 'articles_processed': total,
        'completed': datetime.now().isoformat()
    }})
    print(f'\n[DONE] {total} articles → {output_file}')

if __name__ == '__main__':
    main()
