---
title: Ограничение отображения дочерних записей в ссылке на родительскую запись
kbId: 4952
---

# Ограничение отображения дочерних записей в ссылке на родительскую запись

Для того чтобы ограничить возможность выбора дочерних элементов какой-то конкретной записи в ссылке на родительскую запись (например, отфильтровывать дочерние работы в ссылке на родительскую работу данной работы), в частности, чтобы избежать зацикливания, введите следующее выражение:

```

@prefix object: <http://comindware.com/ontology/object#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix log: <http://www.w3.org/2000/10/swap/log#>.
@prefix list: <http://www.w3.org/2000/10/swap/list#>.
@prefix cmw: <http://comindware.com/logics#>.

{

    ("Raboty" "Roditelskayarabota") object:findProperty ?refProp.
    ?item ?refProp ?parent.
(
   { ?parent -> ?value.  }
   { ?parent object:pt ?colValue.
    ?colValue -> ?value. } 
  ) assert:union true.
}=>{ ?item object:pt ?value }.

{
    ?template object:alias " Raboty ".
    ?value cmw:container ?template.
    not{ ?value object:pt ?item }.
    not{ ?value == ?item }.
}

```

**где:**

**Raboty** – системное имя текущего Шаблона записи;

**Roditelskayarabota** – системное имя ссылки на текущий Шаблон записи (ссылка на родительскую запись).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
