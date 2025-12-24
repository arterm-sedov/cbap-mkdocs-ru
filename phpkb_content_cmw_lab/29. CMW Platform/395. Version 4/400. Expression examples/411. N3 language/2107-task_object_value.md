---
title: Calculating the Display Value of an Object Associated with a Task
kbId: 2107
---


# Calculating the Display Value of an Object Associated with a Task

In **CMW Platform** one can calculate the system task table in a separate record template in order to display more task parameters and set up more convenient grouping (for example, by related object). At the same time, each of the attribute/parameters must be created in such a record template, and in each of them a calculated expression in the N3 language must be configured. This article provides an example of an expression to calculate the display name of the record that the task is associated with.

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
