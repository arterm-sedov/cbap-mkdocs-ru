---
title: Фильтр списка по создателю
kbId: 4933
---

# Фильтр списка по создателю

Для того, чтобы настроить фильтр отображения записей в списке, где текущий пользователь - создатель записи, введите следующее выражение:

```

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

**где:**

**eventorder** – системное имя текущего шаблона записи;

**\_creator** – системное имя системного атрибута типа «Аккаунт», вычисляющий создателя записи.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
