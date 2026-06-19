---
title: Фильтр списка по создателю
kbId: 4933
tags:
    - N3
    - атрибуты
    - выражение на N3
    - пример
hide: tags
---

# Фильтр списка по создателю {: #example_n3_list_by_creator_filter }

Для того чтобы настроить фильтр отображения записей в списке, где текущий пользователь - создатель записи, введите следующее выражение:

```turtle
@prefix cmw: <http://comindware.com/logics#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix user: <http://comindware.com/ontology/user#>.

{

 ("eventorder" "_creator") object:findProperty ?propertyCreator.
 cmw:securityContext cmw:currentUser ?user.
 ?eventorderTemplate object:alias "eventorder".
 ?item cmw:container ?eventorderTemplate.
 ?item ?propertyCreator ?user.

}
```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| `eventorder` | Системное имя текущего шаблона записи. |
| `_creator` | Системное имя системного атрибута типа «**Аккаунт**», в котором хранится создатель записи. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
