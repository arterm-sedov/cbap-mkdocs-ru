---
title: 'Сравнение двух атрибутов типа «Аккаунт»'
kbId: 4932
url: 'https://kb.comindware.ru/article.php?id=4932'
updated: '2026-06-20 20:26:16'
---

# Сравнение двух атрибутов типа «Аккаунт»

Для сравнения двух пользователей (например, менеджер проекта и руководитель сотрудника), введите следующее выражение:

```
#EQUALS($WorkPlanOriginalRef->Curator, $Manager)

@prefix sort: <http://comindware.com/ontology/dataset/sort#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
@prefix ui: <http://comindware.com/ontology/ui#>.
@prefix object: <http://comindware.com/ontology/object#>.
{
    ("WorkPlan" "Curator") object:findProperty ?curatorProperty.
    ("WorkPlanDuplicate" "WorkPlanOriginal") object:findProperty ?workPlanOriginalProperty.
    ("WorkPlanDuplicate" "Manager") object:findProperty ?managerProperty.
    from {
        ?item ?managerProperty ?manager1.
          ?manager1 ui:toClientString ?manager.
    } select ?manager -> ?managerList.

    (?managerList sort:stringComparer) assert:sort ?managerSort.
    ("," ?managerSort) cmwstring:join ?managerStr.

    from {
    ?item ?workPlanOriginalProperty ?workPlan.
        ?workPlan ?curatorProperty ?curator1.
          ?curator1 ui:toClientString ?curatorStrg.
    } select ?curatorStrg -> ?curatorList.

    (?curatorList sort:stringComparer) assert:sort ?curatorSort.
    ("," ?curatorSort) cmwstring:join ?curatorStr.

    if {?curatorDuplicateStr == ?curatorStr}
    then {true -> ?value}
    else {false -> ?value}.
}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `WorkPlan` | Системное имя шаблона записи, где хранится запись о менеджере проекта. |
| `Curator` | Системное имя атрибута типа «**Аккаунт**» с менеджером проекта. |
| `WorkPlanDuplicate` | Системное имя текущего шаблона записи, где выполняется сравнение. |
| `WorkPlanOriginal` | Системное имя атрибута типа «**Запись**» в шаблоне записи `WorkPlanDuplicate`. Атрибут ссылается на шаблон `WorkPlan`. |
| `Manager` | Системное имя атрибута типа «**Аккаунт**» с руководителем сотрудника, с которым выполняется сравнение. |