---
title: 'Фильтр списка по процессам с ошибками'
kbId: 5297
url: 'https://kb.comindware.ru/article.php?id=5297'
updated: '2026-06-20 17:34:13'
---

# Фильтр списка по процессам с ошибками

Для фильтрации списка шаблона процесса, который бы показывал записи процессов с ошибками, введите следующее выражение:

```
@prefix process: <http://comindware.com/ontology/process#>.
@prefix cmw: <http://comindware.com/logics#>.
{
?item process:businessObject ?.
?item process:hasTokenError true.
}
```