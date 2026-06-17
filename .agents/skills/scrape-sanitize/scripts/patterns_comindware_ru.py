"""Boilerplate/noise patterns for comindware.ru (Russian-language site)."""
import re

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

CTA_BUTTON_RE = re.compile(
    r'(?i)\[ Заказать демо \]|\[ Заказать звонок \]|\[ Оставить заявку \]|'
    r'\[ Напишите нам \]|\[ Свяжитесь с нами \]'
)

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
