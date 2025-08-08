---
title: Calculated expression returns archived records
kbId: 1981
---


# Calculated expression returns archived records

When a new record template is created in **CMW Platform**, a button with the «Archive» operation is automatically generated (it archives the selected records (i.e. it sets the value of the «*\_isDisabled*» system attribute to «*true*»)) and is available for users to use.

When working with the data late on, for example, while using Comindware Expression Language, you may find out that the result of the calculated expression is incorrect. One of the reasons may be the inclusion of archived records in the result of the calculation.

**Solution**

To exclude archived records from the calculation result, add the «***EQUALS (a->\_isDisabled, false)***» condition to the calculated expression. For example, when counting the number of records and excluding archived ones.

**Note :** archived records are not displayed in the tables by default. To enable their display, select the «***Show archived records***» flag in the table properties.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
