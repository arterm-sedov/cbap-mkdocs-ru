"""
Unified incremental sanitizer with Ralph-loop checkpointing.
Usage:
  python sanitize.py --site comindware_ru --date 20260616
  python sanitize.py --site comindware_ru --date 20260616 --fresh
"""
import re, os, sys, time, argparse
from urllib.parse import urlparse, urlunparse, unquote
from datetime import datetime

try:
    import requests
except ImportError:
    requests = None

from common import (
    SCRATCH_DIR, ARTICLE_SEP, resolve_paths, add_common_args,
    load_json, save_json, append_output, fresh_start,
)

PARSER = argparse.ArgumentParser(description='Sanitize crawled website for LLM ingestion.')
add_common_args(PARSER)

BATCH_SIZE = 10
HTTP_TIMEOUT = 8
PATHS = {}

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

def log_failure(msg):
    os.makedirs(os.path.dirname(PATHS['failures']), exist_ok=True)
    with open(PATHS['failures'], 'a', encoding='utf-8') as f:
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
    for fp in FOOTER_FINGERPRINTS:
        if fp.search(line.strip()):
            return True
    return False

def has_enough_footer_lines(window_lines):
    return sum(1 for l in window_lines if is_footer_line(l)) >= 3

def strip_footer_block(lines):
    if len(lines) < 20:
        return lines
    scan_start = max(0, len(lines) - int(len(lines) * 0.3))
    for i in range(len(lines) - 1, max(0, len(lines) - 60), -1):
        if re.match(r'^#{1,4}\s+\S', lines[i].strip()):
            return lines[:i]
        if has_enough_footer_lines(lines[max(0, i-10):min(len(lines), i+10)]):
            j = i - 5
            while j > scan_start and lines[j-1].strip() and (j - scan_start) < 8:
                j -= 1
            return lines[:j]
    return lines

def strip_nav_blogs(lines):
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
    return lines[nav_cut:] if nav_cut > 0 else list(lines)

def repair_body(body):
    if len(body.strip()) < 30:
        return None
    lines = body.split('\n')
    lines = strip_nav_blogs(lines)
    lines = strip_footer_block(lines)
    result, blank_count, suspect_count = [], 0, 0
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
    return parts[0].rstrip(), [p.lstrip() for p in parts[1:] if p.strip()]

def process_article(block, url_cache):
    ym = re.search(r'^---\n(.*?)\n---', block, re.DOTALL)
    if not ym:
        return block
    yaml, after = ym.group(1), block[ym.end():]
    url_m = re.search(r'url:\s*(https?://[^\s]+)', yaml)
    url = url_m.group(1) if url_m else ''
    durl = decode_url(url) if url else ''
    title = ''
    if durl:
        title = url_cache.get(durl)
        if title is None:
            title = fetch_title(durl)
            url_cache[durl] = title or ''
    updated = yaml
    if url:
        updated = updated.replace(url, durl)
    if title:
        updated = re.sub(r'title:\s*.*', f'title: {title}', updated) if 'title:' in updated else f'title: {title}\n{updated}'
    body = repair_body(after)
    return None if body is None else f'---\n{updated}\n---\n\n{body}\n'

def main():
    args = PARSER.parse_args()
    PATHS.update(resolve_paths(args.site, args.date))
    if args.fresh:
        fresh_start(PATHS)
    input_file = PATHS['dirty_input']
    output_file = PATHS['sanitized']
    checkpoint_file = PATHS['checkpoint']
    url_cache_file = PATHS['url_cache']

    if not os.path.exists(input_file):
        print(f'ERROR: Input file not found: {input_file}')
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    header, articles = split_articles(content)
    total = len(articles)
    print(f'[{args.site}] {total} articles in dirty file')

    cp = load_json(checkpoint_file)
    url_cache = load_json(url_cache_file) or {}
    start_idx = cp['meta']['articles_processed'] if cp else 0

    if os.path.exists(output_file) and start_idx == 0:
        os.remove(output_file)
    if start_idx > 0:
        print(f'[RESUME] Starting from article {start_idx + 1}/{total}')
    if start_idx == 0:
        append_output(f'{header}\n{ARTICLE_SEP}\n', output_file)

    batch_output = []
    for i in range(start_idx, total):
        article = articles[i]
        uh = ''
        try:
            uh = re.search(r'url:\s*(https?://[^\s]+)', article[:500])
            uh = uh.group(1)[:80] if uh else 'no-url'
        except: pass
        sys.stdout.write(f'  [{i+1}/{total}] {uh}\n'); sys.stdout.flush()
        try:
            cleaned = process_article(article, url_cache)
        except Exception as e:
            log_failure(f'ARTICLE_{i}_ERROR: {e}')
            cleaned = article
        if cleaned is None:
            save_json(url_cache, url_cache_file)
            save_json({'meta': {'topic': f'{args.site}_sanitize', 'status': 'in_progress',
                                'articles_total': total, 'articles_processed': i + 1}}, checkpoint_file)
            continue
        batch_output.append(f'{ARTICLE_SEP}\n{cleaned}{ARTICLE_SEP}\n')
        if len(batch_output) >= BATCH_SIZE:
            append_output(''.join(batch_output), output_file)
            save_json(url_cache, url_cache_file)
            save_json({'meta': {'topic': f'{args.site}_sanitize', 'status': 'in_progress',
                                'articles_total': total, 'articles_processed': i + 1}}, checkpoint_file)
            print(f'  [{i+1}/{total}] {100*(i+1)//total}% — flushed')
            batch_output = []

    if batch_output:
        append_output(''.join(batch_output), output_file)
    save_json(url_cache, url_cache_file)
    save_json({'meta': {'topic': f'{args.site}_sanitize', 'status': 'terminal',
                        'articles_total': total, 'articles_processed': total}}, checkpoint_file)
    print(f'\n[DONE] {total} articles → {output_file}')

if __name__ == '__main__':
    main()
