---
title: Optimizing Calculated Attributes
kbId: 1967
---


# Optimizing Calculated Attributes

One possible reason for the performance degradation of CMW Platform is the use of calculated attributes. According to the existing logic, the value in the calculated attribute is not stored, but is calculated every time it is referred to. Depending on the complexity and correctness of the written expression, for example, a cyclic formula, recalculation can take a significant amount of time, and a calculated attribute can significantly affect the performance of some sections of the system:

- Table of records — when a calculated attribute is displayed on a table of records, at the moment the table is opened, all values ​​are recalculated according to the specified calculated expression;
- Record form — when a calculated attribute is displayed on a record form, the value is recalculated not only at the moment the form is opened, but also at any click on the attribute, changing the value of any other attribute, adding a record to the collection, etc .;
- API, C# scripts — when accessing data through the API, for example, obtaining information on a specific record or an array of records, the value for a calculated attribute will be recalculated before sending the request, which may increase the time it takes to receive a response to a request.

**Solution**

1. Whenever possible, we recommend not to transfer calculated attributes to tables frequently used by employees to obtain operational information. Drag them out only for reports with warning users about a possible increase in data loading time.
2. When writing a calculated expression in Comindware Expression Language, we recommend rewriting it in N3 (you can find examples of expressions in N3 in the [N3 language](https://kb.cmwlab.com/category/411/) category).
3. Use alternative options for obtaining a similar result instead of using calculated fields (items 4 and 5).
4. When using a calculated attribute in a process, it is possible to replace it with setting an entry or exit scenarios for a process element.
5. When using a calculated attribute on a record form, it is possible to replace it with setting a value in the rules for a specific form.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
