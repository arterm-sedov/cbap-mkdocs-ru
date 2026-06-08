---
title: 'Отображение кнопки при пустом исполнителе'
kbId: 4951
url: 'https://kb.comindware.ru/article.php?id=4951'
updated: '2023-12-21 14:50:29'
---

# Отображение кнопки при пустом исполнителе

Для настройки отображения кнопки в Шаблоне процесса при условии отсутствия назначенного исполнителя, введите данное выражение:

- на языке выражений:

```
 EMPTY($assignee)
```

- на языке N3

```
@prefix cmw: <http://comindware.com/logics#>.
{
not{?item cmw:assignee ?.}.
true -> ?value.
}
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
