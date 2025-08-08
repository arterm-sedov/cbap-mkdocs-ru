---
title: Вычисление фактического исполнителя у последней завершенной задачи
kbId: 4953
---

# Вычисление фактического исполнителя у последней завершенной задачи

Для того, чтобы вычислить пользователя, который завершил последнюю задачу из списка задач связанного с текущим объектом экземпляра процесса, введите следующее выражение:

```

@prefix cmw: <http://comindware.com/logics#>.
@prefix task: <http://comindware.com/ontology/task#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
@prefix cmwmath: <http://comindware.com/logics/math#>.
@prefix ui: <http://comindware.com/ontology/ui#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.

{
     from {
    ?task task:objectId ?item.
    ?task cmw:taskStatus taskStatus:completed.
    ?task cmw:scheduledEndDate ?taskDate.                
     } select ?taskDate -> ?taskList.
    ?taskList cmwmath:max ?max.    
    ?taskmax cmw:scheduledEndDate ?max.          
    ?taskmax cmw:completedBy ?value.
    }

```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
