---
title: Вычисление значения атрибута из шаблона пользователя
kbId: 4956
tags:
    - N3
    - атрибуты
    - выражение на N3
    - пример
hide: tags
---

# Вычисление значения атрибута из шаблона пользователя {: #calculate_attribute_account_template }

Для того чтобы получить значение какого-либо атрибута из Шаблона пользователя (через атрибут типа «**Пользователь**», ссылающийся на данный Шаблон пользователя), введите следующее выражение:

```turtle
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
| -------- | -------- |
| `RecordTemplate` | Системное имя текущего Шаблона записи. |
| `assignee` | Системное имя атрибута типа «**Пользователь**» в текущем Шаблоне записи. |
| `Sotrudniki` | Системное имя Шаблона пользователя, на который ссылается **assignee**. |
| `LaborCosts` | Системное имя атрибута типа «**Длительность**» в Шаблоне пользователя, значение которого нужно получить. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
