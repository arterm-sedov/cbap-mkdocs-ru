---
title: Вычисление гиперссылки на историю процесса
kbId: 4959
---

# Вычисление гиперссылки на историю процесса

Для того, чтобы вычислить ссылку на историю текущего процесса, введите следующее выражение:

```
@prefix cmw: <http://comindware.com/logics#>.
@prefix process: <http://comindware.com/ontology/process#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix configuration: <http://comindware.com/ontology/configuration#>.
@prefix cmwlist: <http://comindware.com/logics/list#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
@prefix task: <http://comindware.com/ontology/task#>.
{
    once 
    {
        ?task task:objectId ?item.
        ?task cmw:parent ?proc.
        ("{0}" ?proc) string:format ?s.
        ("." ?s) cmwstring:split ?resultlist.
        (?resultlist 1) cmwlist:at ?resultString.
        ("#process/{0}/map'>Ссылка на процесс</a>" ?resultString) string:format ?tempLink2.   
        ?configObject a configuration:Configuration.
        ?configObject configuration:baseUri ?addressLink.
        ("<a href='{0}" ?addressLink) string:format ?tempLink1.    
        (?tempLink1 ?tempLink2) string:concatenation ?resultLink.
        ?resultLink == ?value.
    }
}
```

**где:**

**Ссылка на процесс** – название для отображаемой ссылки.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
