---
title: Отображение кнопки при пустом исполнителе
kbId: 4951
tags:
    - N3
    - выражение на N3
    - кнопки
    - пример
    - процессы
    - формулы
hide: tags
---

# Отображение кнопки при пустом исполнителе {: #show_button_empty_assignee }

Для настройки отображения кнопки в Шаблоне процесса при условии отсутствия назначенного исполнителя, введите данное выражение:

- на языке выражений:

```sql
 EMPTY($assignee)
```turtle
- на языке N3

```turtle
@prefix cmw: <http://comindware.com/logics#>.
{
not{?item cmw:assignee ?.}.
true -> ?value.
}
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
