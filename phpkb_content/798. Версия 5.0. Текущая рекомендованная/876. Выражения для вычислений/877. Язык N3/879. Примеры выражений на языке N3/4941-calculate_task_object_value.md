---
title: Вычисление отображаемого значения связанного с задачей объекта
kbId: 4941
---

# Вычисление отображаемого значения связанного с задачей объекта

В **Comindware** **Platform** существует возможность вычисления таблицы системных задач в отдельном шаблоне записи для отображения большего количества параметров задачи и настройки более удобной группировки (например, по связанному объекту). При этом, каждый из параметров-атрибутов должен быть создан в таком шаблоне записи, и в каждом из них должно быть настроено вычисляемое выражение на языке N3. В данной статье дан пример выражения для вычисления отображаемого названия записи, с которой связана задача.

```

@prefix task: <http://comindware.com/ontology/task#>.
@prefix cmwui: <http://comindware.com/ontology/ui#>.
@prefix cmw: <http://comindware.com/logics#>.

{

?item task:objectId ?objectId.
?objectId cmw:container ?cmwcontainer.
?cmwcontainer cmwui:displayNamePredicate ?cmwuidisplayNamePredicate.
?objectId ?cmwuidisplayNamePredicate ?value.

}

```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
