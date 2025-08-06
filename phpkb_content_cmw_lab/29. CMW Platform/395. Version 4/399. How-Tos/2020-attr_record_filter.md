---
title: Configuring Filters for Record Attributes
kbId: 2020
---


# Configuring Filters for Record Attributes

## Use Case

The **CMW Platform** allows restricting the field value display and selection using the **Filter** property in the form designer.

The field **Filter** property is available for the following attribute types:

1. **Account** — filter accounts to display.
2. **Record** — filter records to display.
3. **Record** with multiple values:
   - filter records to display
   - filter records to add

## Instructions

To configure a filter for a field on a form:

1. Select a field on the form to display its **Field properties** pane.
2. In the **Filter** property, define the filter using one of the following options:
   - **Attribute** — select an attribute from the dropdown. The values of this attribute will appear in the form field.
   - **Formula** — write an expression in the CMW formula language. The values returned by the formula ​​will appear in the form field.
   - **N3** — write an expression in the N3 language. The values returned by the expression will appear in the form field.
   - **DMN** — create a table in the DMN notation. The table output values will appear in the form field.

**Tip:** You can configure different filters for different fields on each form.

## See Also

[Configuring Context-Dependent Filter for Record Attribute](https://kb.comindware.ru/article.php?id=2022)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
