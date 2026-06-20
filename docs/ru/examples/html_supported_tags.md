---
title: Перечень поддерживаемых тегов и элементов HTML
kbId: 5373
tags:
    - C#
    - HTML
    - N3
    - атрибуты
    - выражение на N3
    - пример
    - формулы
hide: tags
---

# Перечень поддерживаемых тегов и элементов HTML {: #html_supported_tags }

## Введение {: #html_supported_tags_intro }

В **{{ productName }}** предусмотрена возможность использования языка HTML в значениях атрибутов типа «**Текст**», текстовых полях и статичном тексте на форме, сообщениях электронной почты и тому подобных текстовых элементах. При этом в целях обеспечения безопасности разрешено использовать ограниченный набор тегов и атрибутов. Неподдерживаемые элементы HTML удаляются при сохранении записей.

Помимо тегов допустимо использовать HTML-мнемоники вида `&charname;`. Например, мнемоника неразрывного пробела: `&nbsp;`. С перечнем HTML-мнемоник можно ознакомиться в статьях [HTML-символы][w3docs_html_symbols] и [HTML Entities][symbl_html_entities].

В этой статье перечислены теги и атрибуты HTML, которые можно вводить в текстовые поля с HTML-форматированием, а также использовать в формулах, выражениях на N3 и скриптах на C#, которые возвращают HTML-текст.

## Допустимые теги и атрибуты {: #html_supported_tags_dopustimye_tegi_i_atributy }

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

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Атрибут типа «Текст»][attribute_text]
- [Цветовой индикатор в таблице. Настройка отображения][example_list_color_indicator_formula]
- [Язык формул][formula_guide]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
