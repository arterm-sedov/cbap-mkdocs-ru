---
title: Вычисление объекта, инициировавшего триггер
kbId: 4947
---

# Вычисление объекта, инициировавшего триггер

Для того, чтобы вычислить объект, по которому был запущен текущий триггер (например, чтобы проставить ссылку на изначальную запись), введите следующее выражение:

```
@prefix cmwsession: <http://comindware.com/ontology/session#>.
@prefix var: <http://comindware.com/ontology/session/variable#>.
{
cmwsession:context cmwsession:origin ?value.
}
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
