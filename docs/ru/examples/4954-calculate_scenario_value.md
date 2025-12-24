---
title: Вычисление значения из объекта, инициировавшего триггер
kbId: 4954
---

# Вычисление значения из объекта, инициировавшего триггер

Для того, чтобы вычислить какое-либо значение объекта, по которому был запущен текущий триггер (например, чтобы проставить значение из изначальной записи), введите следующее выражение:

```

@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwsession: <http://comindware.com/ontology/session#>.
@prefix var: <http://comindware.com/ontology/session/variable#>.
 
{
   ("TimesheetPlan" "Performer") object:findProperty ?propTimesheetPerformer.
    
    cmwsession:context cmwsession:origin ?planWork. 
    ?planWork ?propTimesheetPerformer ?value.
}

```

**где:**

**TimesheetPlan** – системное имя Шаблона записи, в рамках которого было инициировано событие;

**Performer** – системное имя атрибута в **TimesheetPlan**, значение которого нужно получить.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
