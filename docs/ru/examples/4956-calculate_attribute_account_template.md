---
title: Вычисление значения атрибута из шаблона пользователя
kbId: 4956
---

# Вычисление значения атрибута из шаблона пользователя

Для того чтобы получить значение какого-либо атрибута из Шаблона пользователя (через атрибут типа "Пользователь", ссылающийся на данный Шаблон пользователя), введите следующее выражение:

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

**где:**

**RecordTemplate** – системное имя текущего Шаблона записи;

**assignee** – системное имя атрибута типа "Пользователь" в текущем Шаблоне записи;

**Sotrudniki** – системное имя Шаблона пользователя, на который ссылается **assignee**;

**LaborCosts** – системное имя атрибута типа "Длительность" в Шаблоне пользователя, значение которого нужно получить.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
