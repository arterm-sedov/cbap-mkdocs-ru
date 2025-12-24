---
title: Reference field is empty
kbId: 1951
---


# Reference field is empty

When configuring the attributes for a record template in **CMW Platform**, it is possible to create a reference attribute to select values from a list of records in another record template.

Sometimes a user may face a situation when there is no possibility of choosing any of the values in the reference field on the form. One of the reasons may be an incorrectly configured property of the displayed attribute in the referenced record template. Another reason may be insufficient role permissions configuration.

**Solution:**

1. Go to the settings of the record template that the attribute refers to and open the «Attributes» tab.
2. In the opened list, find the displayed attribute whose values ​​will be shown when referencing the current record template. As a rule, this is a text field with the name of the entry, which uniquely identifies it, for example, the name of the Client, Project or Agreement.
3. If the displayed attribute is calculated, check that the expression you wrote is correct.
4. If items 1-3 have been worked out, and the values ​​in the reference field did not appear for the user, check the settings of permissions in his/her role. The template referenced by the link attribute must have view permissions.

**Note:** If there is no display attribute chosen, the record IDs will be displayed in the reference field by default.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
