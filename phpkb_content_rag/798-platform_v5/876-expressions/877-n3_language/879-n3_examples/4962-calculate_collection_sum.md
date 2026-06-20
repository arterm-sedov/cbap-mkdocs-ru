---
title: 'Вычисление суммы значений столбца коллекции'
kbId: 4962
url: 'https://kb.comindware.ru/article.php?id=4962'
updated: '2026-06-20 18:06:07'
---

# Вычисление суммы значений столбца коллекции

Для того чтобы рассчитать сумму значений определенного столбца коллекции, за исключением заархивированных записей, введите следующее выражение:

```
@prefix object: <http://comindware.com/ontology/object#>.
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
@prefix w3math: <http://www.w3.org/2000/10/swap/math#>.
@prefix cmwmath: <http://comindware.com/logics/math#>.

{
    ("Project" "ProjectPlans") object:findProperty ?ProjectPlansProperty.
    ("Plans" "Prodolzhitelnost") object:findProperty ?ProdolzhitelnostProperty.
    ("Plans" "_isDisabled") object:findProperty ?_isDisabled.

                from {
                ?item ?ProjectPlansProperty ?ProjectPlansVal.
                ?ProjectPlansVal ?ProdolzhitelnostProperty ?ProdolzhitelnostVal.
                not{?ProdolzhitelnostVal ?_isDisabled true.}.
                                         }select ?ProdolzhitelnostVal -> ?durationList.
                ?durationList cmwmath:sum  ?value.
                }
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Project` | Системное имя текущего шаблона записи. |
| `ProjectPlans` | Системное имя атрибута типа «**Коллекция**» в текущем шаблоне записи. |
| `Plans` | Системное имя шаблона записи, на который ссылается `ProjectPlans`. |
| `Prodolzhitelnost` | Системное имя атрибута для сложения в шаблоне `Plans`. |
| `_isDisabled` | Системное имя системного атрибута «**В архиве**» для скрытия архивных записей. |