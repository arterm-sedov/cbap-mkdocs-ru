---
title: Фильтр списка по процессам с ошибками
kbId: 4934
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

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
