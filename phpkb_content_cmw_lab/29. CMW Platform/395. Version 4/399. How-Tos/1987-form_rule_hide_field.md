---
title: Configuring Form Rule Using Formula
kbId: 1987
---


# Configuring Form Rule Using Formula

## Use Case

In the **CMW Platform**, you can define a set of rules for any form to control its element behavior.

Each rule can include several conditional actions:

- Set field values
- Show field validation warnings and error messages
- Change element access mode: require entry, allow entry, read-only
- Hide elements

In this article, we will create a form rule to hide the *Recipient* field from the form when this field is empty and the *Enter new customer details* box is checked.

## Prerequisites

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template system name** | **Attribute and field display name (system name)** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Request* | *Recipient (recipient)* | **Record** | Place this attribute on the form as the *Recipient* field. |
| *Enter new customer details (create\_flag)* | **Boolean** | Place this attribute on the form as the *Enter new customer details* checkbox. |

 
## Instructions

1. In the *Request* template, open the default form.
2. Open the ***Form rules*** designer using the dropdown next to the form heading.
3. Add a rule and an action to the rule.
4. Select the action to display the **Action properties** pane.
5. From the **Form element** dropdown, select the *Recipient* field**.**
6. From the **Action** dropdown, select **Change access****.**
7. From the **New value**dropdown, select **Hide****.**
8. In the **Execution condition** field, enter the [**formula**](#mcetoc_1gtqijebq0):
   ```
   AND(EMPTY($recipient),$create_flag == true)
   ```
9. Click ***Save***.

### Formula Syntax

| Element | Description |
| --- | --- |
| `AND()` | This function takes two arguments and returns `true` if both arguments resolve to `true`, i.e., when the *Recipient* field is empty and the *Enter new customer details* box is checked. |
| `$` | This prefix refers to an attribute in the current record context. |
| `EMPTY()` | This function returns `true` if its argument has an empty value, i.e., when the *Recipient* attribute value is null. |

## See Also

[Configuring Dynamic Field Display Using a Form Rule](https://kb.comindware.ru/article.php?id=2070)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
