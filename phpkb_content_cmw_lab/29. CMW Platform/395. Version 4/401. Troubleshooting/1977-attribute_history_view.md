---
title: Calculated attribute change log cannot be viewed
kbId: 1977
---


# Calculated attribute change log cannot be viewed

In the settings of the attribute there is a «***Track changes***» flag, after applying which any changes in the attribute will be recorded. This flag can be set only for non-calculated attributes. History cannot be saved for calculated attributes, since calculated attributes are subject of computation and their value is always unstable.

All changes to the attribute values ​​are saved in the system change log. To view the change log, open a record, click on the «Information» button on the ribbon of the form and select «***Change log***».

**Solution**

If you still need to store change log of calculated attributes, then:

1. Create a non-calculated attribute (for each calculated one).
2. Manually (or by scenario) write the calculated value in the new attribute.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
