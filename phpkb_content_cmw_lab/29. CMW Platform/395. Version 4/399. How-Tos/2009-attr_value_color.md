---
title: Configuring Conditional Coloring of an Attribute Value
kbId: 2009
---


# Configuring Conditional Coloring of an Attribute Value

## Use Case

In the **CMW Platform**, the applied theme defines display formatting for all fields. You cannot specify formatting for the individual fields. But you can customize the font, color, or other formatting properties for the **Text** attribute with the **HTML text** display format. The **HTML text** attribute value is displayed with the configured HTML formatting in tables and forms.

In this article, we will conditionally color the task status: when the task is overdue, highlight the status in red; otherwise highlight the status in green.

## Prerequisites

To proceed with the example, create the attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Statuses* | *Name* | **Text** | The *Name* attribute stores a status name.  The *Statuses* template contains two records:   - *Name* = Overdue - *Name* = Complete |
| *Tasks* | *StatusRef* | **Record** | The *StatusRef* attribute is linked to the *Statuses* template *.* |

## Instructions

1. In the *Tasks* template, create the *Colored Status* **Text** attribute with the following properties:
   - **Display format** —  **HTML text**
   - **Calculate using an expression** — checked
   - **Calculated value** — [**formula**](#mcetoc_1gtntho192):
     ```
     FORMAT(
     IF(EQUALS($StatusRef->Name,"Overdue"),
     "<p><span style='color:#000000'><span style='background-color:#f02626'>{0}</span></span></p>",
     "<p><span style='color:#000000'><span style='background-color:#3ee028'>{0}</span></span></p>"),
     LIST($StatusRef->Name))
     ```
2. Place the *Colored Status* attribute on a form or table. The attribute value will be colored depending on the status name.

### Formula Syntax

| Element | Description |
| --- | --- |
| `FORMAT()` | This function takes a string and array as arguments, replaces the placeholders in the string with the array values, and returns the resulting string. Placeholders are numbered from 0. |
| `IF(Argument1, Argument2, Argument3)` | This function takes three arguments. If `Argument1` resolves to `true`, it returns `Argument2`. Otherwise, it returns `Argument3`. |
| `EQUALS($StatusRef->Name,"Overdue")` | `Argument1` — condition. The `EQUALS``()` function returns `true` if the `$``StatusRef->Name` value is `Overdue`. |
| `$StatusRef` | The `$` prefix refers to the *StatusRef*attribute in the current record context. |
| `->Name` | The `->`operator refers to the *Name* attribute of the linked *Statuses* template. |
| `"<p><span style='color:#000000'><span style='background-color:#f02626'>{0}</span></span></p>"` | `Argument2` — red status HTML code. The `color:#000000` CSS statement sets the text color to white. The `background-color``: #f02626` statement sets the background color to red. |
| `"<p><span style='color:#000000'><span style='background-color:#3ee028'>{0}</span></span></p>"` | `Argument3` — green status HTML code. The `background-color``:#3ee028` statement sets the background color to green. |
| `{0}` | This placeholder is replaced with the array value returned by the `LIST()` function. |
| `LIST($StatusRef->Name)` | This function takes the `$StatusRef->Name` value and returns it as an array of one element. You have to use the `LIST()` function because the `FORMAT()` function only accepts an array of placeholder values and will not accept a single value. |

**Note:** The *Status* attribute value will not be colored, but the calculated *Colored Status*attribute.

**Tip:** You can customize the **HTML text** using most HTML features: text or background color, font family and size, HTML tags, etc.

## See Also

[Configuring Color Indicator](https://kb.comindware.ru/article.php?id=1999)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
