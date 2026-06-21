---
title: 'Ввод типа литерала'
kbId: 2476
url: 'https://kb.comindware.ru/article.php?id=2476'
updated: '2023-08-23 11:41:08'
---

# Ввод типа литерала

## Инструкции

1. Введите литерал в кавычках, например `"P1D"` (1 день в формате ISO).
2. После кавычек введите символы `^^`.
3. Нажмите клавиши `Ctrl` `Пробел`.
4. Отобразится список доступных типов литералов.

_![Список доступных типов литералов](https://kb.comindware.ru/assets/n3_editor_literal_autocomplete.png)_

4. Дважды нажмите тип литерала, например `duration`, чтобы вставить его в выражение.

**Пример: выражение, возвращающее конец текущего дня**

```
@prefix session: <http://comindware.com/ontology/session#>.
@prefix cmwutc: <http://comindware.com/logics/time/utc#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix cmwdur: <http://comindware.com/logics/time/duration#>.
{
  # Текущее время в UTC
  session:context session:requestTime ?nowUTC.
  # Время начала текущего дня
  ?nowUTC cmwutc:startOfDay ?startOfTodayUTC.
  # Начало следующих суток = время начала текущего дня + 1 сутки
  (?startOfTodayUTC "P1D"^^xsd:duration) cmwdur:add ?value.
}
```

--8<-- "related_topics_heading.md"

**[Редактор выражений](https://kb.comindware.ru/article.php?id=2463)**

**[Примеры использования языка N3](https://kb.comindware.ru/category.php?id=408)**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
