---
title: 'Сравнение двух атрибутов типа «Аккаунт»'
kbId: 4932
url: 'https://kb.comindware.ru/article.php?id=4932'
updated: '2024-11-06 15:54:55'
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

**где:**

**WorkPlan** – системное имя шаблона записи, где хранится запись о менеджере проекта;

**Curator**– системное имя атрибута типа «Аккаунт» (менеджер проекта);

**WorkPlanDuplicate** – системное имя текущего шаблона записи, где производится сравнение;

**WorkPlanOriginal** – системное имя атрибут типа «Запись» в шаблоне записи **WorkPlanDuplicate**, ссылающийся на **WorkPlan***;*

**Manager** – системное имя атрибута типа «Аккаунт» (руководитель сотрудника), с которым сравниваем.