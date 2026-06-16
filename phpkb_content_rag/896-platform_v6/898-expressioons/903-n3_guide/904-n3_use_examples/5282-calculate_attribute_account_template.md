---
title: 'Вычисление значения атрибута из шаблона пользователя'
kbId: 5282
url: 'https://kb.comindware.ru/article.php?id=5282'
updated: '2026-06-16 19:17:13'
---

# Вычисление значения атрибута из шаблона пользователя

Для того чтобы получить значение какого-либо атрибута из Шаблона пользователя (через атрибут типа «**Пользователь**», ссылающийся на данный Шаблон пользователя), введите следующее выражение:

```
@prefix account: <http://comindware.com/ontology/account#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix container: <http://comindware.com/ontology/container#>.

{
    ("RecordTemplate" "assignee") object:findProperty ?assigneeProp.
    ("Sotrudniki" "LaborCosts") object:findProperty ?LaborCostsProp.
?item ?assigneeProp ?assignee.
  ?polz container:alias "Sotrudniki".
  ?assignee account:extendedBy ?polz.
?assignee ?LaborCostsProp ?value.
}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `RecordTemplate` | Системное имя текущего Шаблона записи. |
| `assignee` | Системное имя атрибута типа «**Пользователь**» в текущем Шаблоне записи. |
| `Sotrudniki` | Системное имя Шаблона пользователя, на который ссылается **assignee**. |
| `LaborCosts` | Системное имя атрибута типа «**Длительность**» в Шаблоне пользователя, значение которого нужно получить. |