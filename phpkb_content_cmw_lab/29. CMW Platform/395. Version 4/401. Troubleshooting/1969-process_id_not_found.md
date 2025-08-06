---
title: Error “Identifier “…” not found on the process diagram
kbId: 1969
---


# Error “Identifier “…” not found on the process diagram

It is important to understand the context when writing formulas as part of customizing a process diagram. The initial context within a process template is the context of the associated record template.

If, when checking or publishing a process diagram, you encounter the error ***"Identifier "..." not found, location [...]"***, this means that in some expression on this element you used an attribute that does not exist in the current context, that is, in the associated record template. In this case, the system name of such an attribute is indicated in quotes, and its positioning in the written calculated expression is indicated in square brackets.

**Solution**

1. The easiest way is to create the required attribute in the associated record template.
2. If you need to use this particular attribute located in another record template, refer to it through the expression language.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
