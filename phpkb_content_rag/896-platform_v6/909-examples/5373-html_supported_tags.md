---
title: 'Перечень поддерживаемых тегов и элементов HTML'
kbId: 5373
url: 'https://kb.comindware.ru/article.php?id=5373'
updated: '2026-06-20 17:34:16'
---

# Перечень поддерживаемых тегов и элементов HTML

## Введение

В **Comindware Platform** предусмотрена возможность использования языка HTML в значениях атрибутов типа «**Текст**», текстовых полях и статичном тексте на форме, сообщениях электронной почты и тому подобных текстовых элементах. При этом в целях обеспечения безопасности разрешено использовать ограниченный набор тегов и атрибутов. Неподдерживаемые элементы HTML удаляются при сохранении записей.

Помимо тегов допустимо использовать HTML-мнемоники вида `&charname;`. Например, мнемоника неразрывного пробела: `&nbsp;`. С перечнем HTML-мнемоник можно ознакомиться в статьях [HTML-символы](https://ru.w3docs.com/uchebnik-html/html-simvoly.html) и [HTML Entities](https://symbl.cc/ru/html-entities/).

В этой статье перечислены теги и атрибуты HTML, которые можно вводить в текстовые поля с HTML-форматированием, а также использовать в формулах, выражениях на N3 и скриптах на C#, которые возвращают HTML-текст.

## Допустимые теги и атрибуты

| Тег | Атрибуты |
| --- | --- |
| `a` | `style`, `href`, `target`, `name`, `title`, `class`, `id` |
| `address` |  |
| `b` |  |
| `blockquote` | `dir` |
| `br` |  |
| `caption` |  |
| `center` | `style` |
| `div` | `align`, `style` |
| `em` |  |
| `font` | `color`, `size`, `face` |
| `h1` | `align` |
| `h2` | `align` |
| `h3` | `align` |
| `h4` | `align` |
| `h5` | `align` |
| `h6` | `align` |
| `hr` |  |
| `i` |  |
| `iframe` | `src`, `frameborder`, `allowfullscreen` |
| `img` | `src`, `alt`, `title`, `style` |
| `li` |  |
| `ol` |  |
| `p` | `align`, `dir`, `style` |
| `pre` |  |
| `progress` (поддерживается только в таблицах) | `id`, `max`, `value` |
| `s` |  |
| `span` | `align`, `style` |
| `strike` |  |
| `strong` |  |
| `style` | `align`, `text-align`, `color`, `font-weight`, `font-style`, `font-size`, `font-family`, `text-decoration`, `type`, `media`, `border-color`, `height`, `width`, `border-width`, `background-color`, `border-style` |
| `sub` |  |
| `sup` |  |
| `table` | `class`, `style`, `border`, `cellspacing`, `cellpadding`, `align` |
| `tbody` | `style` |
| `td` | `style`, `rowspan` |
| `th` | `style` |
| `tr` | `style`, `colspan` |
| `u` |  |
| `ul` |  |

## Связанные статьи

- [Атрибут типа «Текст»](https://kb.comindware.ru/article.php?id=5710)
- [Цветовой индикатор в таблице. Настройка отображения](https://kb.comindware.ru/article.php?id=5349)
- [Язык формул](https://kb.comindware.ru/category.php?id=901)