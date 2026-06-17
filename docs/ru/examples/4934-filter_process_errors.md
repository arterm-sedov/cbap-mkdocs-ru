---
title: Фильтр списка по процессам с ошибками
kbId: 4934
tags:
    - N3
    - выражение на N3
    - пример
    - процессы
hide: tags
---

# Фильтр списка по процессам с ошибками {: #filter_process_errors }

Для фильтрации списка шаблона процесса, который бы показывал записи процессов с ошибками, введите следующее выражение:

```turtle
@prefix process: <http://comindware.com/ontology/process#>.
@prefix cmw: <http://comindware.com/logics#>.
{
?item process:businessObject ?.
?item process:hasTokenError true.
}
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
