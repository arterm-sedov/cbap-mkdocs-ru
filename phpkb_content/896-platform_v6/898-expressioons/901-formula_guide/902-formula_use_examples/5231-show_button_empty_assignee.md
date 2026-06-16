---
title: 'Отображение кнопки при пустом исполнителе'
kbId: 5231
url: 'https://kb.comindware.ru/article.php?id=5231'
updated: '2026-06-16 19:17:07'
---

# Отображение кнопки при пустом исполнителе

Для настройки отображения кнопки в Шаблоне процесса при условии отсутствия назначенного исполнителя, введите данное выражение:

- на языке выражений:

```
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
