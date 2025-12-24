---
title: Вычисление последней даты изменения записей в древовидной коллекции
kbId: 4964
---

# Вычисление последней даты изменения записей в древовидной коллекции

Для того, чтобы вывести последнюю дату изменения в рамках записей во вложенной коллекции (например, чтобы показать последнюю дату изменения работы или подработы, входящей в общий план), введите следующее выражение:

```

@prefix object: <http://comindware.com/ontology/object#>.
@prefix math: <http://comindware.com/logics/math#>.
@prefix cmw: <http://comindware.com/logics#>.
{
    ("Workitem" "WorkPlan") object:findProperty ?workPlanProperty.
    ("Workitem" "ParentWorkitem") object:findProperty ?parentProperty.
    ("Workitem" "_lastWriteDate") object:findProperty ?lastWriteDate.

    from
    {
        ?WorkitemTemplate object:alias "Workitem".
        ?WorkitemItems cmw:container ?WorkitemTemplate.
        (?WorkitemItems ?parentProperty) object:getRootByParentProperty ?rootTask.
        ?rootTask ?workPlanProperty ?item.
        ?WorkitemItems ?lastWriteDate ?lastWriteDateVal.
    } select ?lastWriteDateVal -> ?lastWriteDateList.

?lastWriteDateList math:max ?m.
    ?m -> ?value.
}

```

**где:**

**Workitem** – системное имя Шаблона записи с записями коллекции;

**WorkPlan** – системное имя атрибута типа "Ссылка" на текущий Шаблон записи;

**ParentWorkitem** – системное имя атрибута типа "Ссылка" на родительскую запись в Шаблоне записи **Workitem**;

**\_lastWriteDate** – системное имя системного атрибута "Дата изменения".

**Примечание :** в данном примере только родительский объект связан с текущей записью по ссылке.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
