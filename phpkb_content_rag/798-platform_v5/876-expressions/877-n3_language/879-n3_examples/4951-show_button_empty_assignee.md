---
title: 'Отображение кнопки при пустом исполнителе'
kbId: 4951
url: 'https://kb.comindware.ru/article.php?id=4951'
updated: '2026-06-20 18:06:18'
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