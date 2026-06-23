---
title: Вычисление объекта, инициировавшего триггер
kbId: 5274
tags:
    - N3
    - выражение на N3
    - пример
hide: tags
---

# Вычисление объекта, инициировавшего триггер {: #calculate_scenario_object }

Для того чтобы вычислить объект, по которому был запущен текущий триггер (например, чтобы проставить ссылку на изначальную запись), введите следующее выражение:

```turtle
@prefix cmwsession: <http://comindware.com/ontology/session#>.
@prefix var: <http://comindware.com/ontology/session/variable#>.
{
cmwsession:context cmwsession:origin ?value.
}
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
