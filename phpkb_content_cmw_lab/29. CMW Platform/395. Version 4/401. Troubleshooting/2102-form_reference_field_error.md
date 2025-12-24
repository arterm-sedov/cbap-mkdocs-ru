---
title: Unable to place some elements on a form through a reference field
kbId: 2102
---


# Unable to place some elements on a form through a reference field

In {{ productName }} there is an attribute data type called record. In the attribute settings, you can specify how many records can be stored in it: one or more, i.e., how many records in the target record template are referenced by the record in the current record template. This setting also affects the ability to add elements from an attribute with the “Record” data type to a form or a table.

If only one associated value can be stored in an attribute, any of the available elements of the target record template can be transferred to the form of the main object by expanding the attribute with the “Record” data type in the form designer. In this case, one record in the main record template corresponds to one record in the target record template.

But, if several values ​​can be stored in an attribute with the “Record” data type, then not all elements from this attribute can be transferred to the form of the main object. So, for example, you can't move a form, because the attribute stores multiple records, and the form always corresponds to just one record. The attributes of the target record template also cannot be placed on the form of the main object in an arbitrary order, but only by changing the representation of the attribute with the "Record" data type on the form to "Table" and transferring the attributes as columns of the table.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
