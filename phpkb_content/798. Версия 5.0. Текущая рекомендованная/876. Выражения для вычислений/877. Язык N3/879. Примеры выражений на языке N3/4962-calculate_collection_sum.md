---
title: Вычисление суммы значений столбца коллекции
kbId: 4962
---

# Вычисление суммы значений столбца коллекции

Для того, чтобы рассчитать сумму значений определенного столбца коллекции, за исключением заархивированных записей, введите следующее выражение:

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

**где:**

**Project** — системное имя текущего шаблона записи;

**ProjectPlans**— системное имя атрибута типа «Коллекция» в текущем шаблоне записи;

**Plans**— системное имя шаблона записи, на который ссылается **ProjectPlans**;

**Prodolzhitelnost**— системное имя атрибута для сложения в **Plans**;

**\_isDisabled** — системное имя системного атрибута «В архиве» (для скрытия архивных записей).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
