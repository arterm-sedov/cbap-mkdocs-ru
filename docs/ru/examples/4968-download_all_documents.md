---
title: Выгрузка всех документов стенда
kbId: 4968
---

# Выгрузка всех документов стенда

Для выгрузки всех документов стенда в один атрибут, введите следующее выражение:

```

@prefix cmwassert: <http://comindware.com/logics/assert#>.
@prefix cmwtimeL: <http://comindware.com/logics/time/utc#>.
@prefix session: <http://comindware.com/ontology/session#>.
@prefix cmw:  <http://comindware.com/logics#>.
@prefix document: <http://comindware.com/ontology/document#>.

{
    ?value a document:Document.
}

```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
