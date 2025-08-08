---
title: Understanding and changing the context in CMW Platform
kbId: 2085
---


# Understanding and changing the context in CMW Platform

The concept of context is always used to set up business logic and calculations in CMW Platform. First of all, any information system has a database, and in order to get some data from it, you need to write a query to the database.

The context is the starting point of a database query. Context boundaries are record templates, process templates, and user tasks and are defined in the query (in the form of calculated attributes, form rules, filters, etc.), and they must be distinguished so that the expression is written correctly.

**$** is the designation of the original context.

To change the context, use attributes with the "Record" data type or expressions of the "***from a in db***" type. To change the context to a related entry, use the system name of the attribute with the "Record" data type after "***$***" and the characters "***->***" after the system name. In scenarios, you can change the context by specifying the actual attribute with the "Record" data type or by writing an expression of the "***from a in db***" type.

**Context Change Examples**

**Example 1:** the attribute you are looking for is in a different record template, and the current context (record template) has a reference to this record template.

```
$link->field
```

where *link* is the system name of the attribute with the “Record” data type and *field* is the system name of the attribute in the linked entry.

Read more about calling related data in the article [Retrieving Related Data](https://kb.comindware.ru/article.php?id=2086).

**Example 2:** The attribute you are looking for is in another record template, but the current context (record template) does not refer to this record template.

```
from a in db->recordtemplate_systemname where EQUALS(a->field1, $field2) select a->id
```

where *recordtemplate\_systemname* is the system name of the record template you want to search in, *field1* is the system name of the attribute in this record template, and *field2* is the system name of the attribute in the current record template against which *field1* is to be compared.

Read more about customizing a select expression in the article [List of Comindware Expression Language Operators](https://kb.comindware.ru/article.php?id=2087).

**Example 3:** The current context is a task context, and the attribute you are looking for is in the record template associated with the process template.

```
$cmw.task.objectId->op.11
```

where op.11 is the ID of the attribute in the associated record template.

**Example 4:** The current context is a process context and the attribute you are looking for is in the associated record template.

```
$$BusinessObject->field
```

where *field* is the system attribute name in the associated record template.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
