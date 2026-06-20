---
title: 'Фильтр списка по процессам с ошибками'
kbId: 4934
url: 'https://kb.comindware.ru/article.php?id=4934'
updated: '2026-06-20 20:26:16'
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