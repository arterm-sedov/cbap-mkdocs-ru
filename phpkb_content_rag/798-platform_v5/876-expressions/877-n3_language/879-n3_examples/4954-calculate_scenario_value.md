---
title: 'Вычисление значения из объекта, инициировавшего триггер'
kbId: 4954
url: 'https://kb.comindware.ru/article.php?id=4954'
updated: '2026-06-20 20:26:17'
---

# Вычисление значения из объекта, инициировавшего триггер

Для того чтобы вычислить какое-либо значение объекта, по которому был запущен текущий триггер (например, чтобы проставить значение из изначальной записи), введите следующее выражение:

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

**Здесь:**

| Значение | Описание |
| --- | --- |
| `TimesheetPlan` | Системное имя Шаблона записи, в рамках которого было инициировано событие. |
| `Performer` | Системное имя атрибута в **TimesheetPlan**, значение которого нужно получить. |