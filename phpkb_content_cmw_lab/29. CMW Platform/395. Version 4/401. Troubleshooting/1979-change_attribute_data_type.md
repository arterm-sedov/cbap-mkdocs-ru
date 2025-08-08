---
title: How to change the data type of an existing attribute?
kbId: 1979
---


# How to change the data type of an existing attribute?

**CMW Platform** has a useful feature for changing the data type of an attribute. Situations may occur when an attribute was quickly created and its data type was defined incorrectly, or during further design there appeared a need to change it.

There are a few things to keep in mind when changing the data type:

- Whether this attribute is used in any calculated expressions in the system;
- How many forms and tables the attribute is dragged on.

**Solution**

1. If the attribute is used in calculated expressions, then they may stop working, since some functions require only the numeric type of the attribute, or only the text type, etc. In this case, it is better to create a new attribute with the desired type.
2. If an attribute is dragged on several forms and tables, then it is also better to create a new attribute with the required type, or, after changing the type of the attribute, drag it to all the forms and tables again.

If the attribute is dragged on a large number of forms and tables and is used in a number of calculated expressions, it is better to create a new attribute with the desired type.

**Note :** when you change the display format of an attribute, you do not need to drag it on the form or on a table again, these changes are applied automatically.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
