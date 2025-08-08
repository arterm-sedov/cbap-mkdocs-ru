---
title: Configuring Color Indicator
kbId: 1999
---


# Configuring Color Indicator

## Use Case

In some cases, you might want to display a color indicator in a field to quickly understand whether a date has passed, a status has changed, a deadline is overdue, etc. To achieve this, use an HTML text attribute that changes its formatting conditionally.

In this article, we will create an indicator that will be red when the actual project completion date is past the planned completion date, or green otherwise.

## Prerequisites

To proceed with the example, create the attributes as shown in the table below:

| **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- |
| *Actual\_date* | **Date & time** | The actual project completion date. |
| *Planned\_date* | **Date & time** | The planned project completion date. |

## Instructions

1. Create a new **Text** attribute *Overdue indicator*:
   - **Display format** — **HTML text**
   - **Calculate using an expression** — checked.
2. In the **Calculated value**, enter the **formula**:

   | `IF(GREATEREQ($Actual_date, $Planned_date),`  `"<span style='color:#B22222; font-size: 200%; text-shadow: 0 0 1px black;`  `position: absolute; top:0px;'> ● </span>",`  `"<span style='color:#45A521; font-size: 200%; text-shadow: 0 0 1px black;`  `position: absolute; top:0px;'> ● </span>"`  `)` |
   | --- |

   Note: If you export this value to an Excel file, it will be displayed as unformatted HTML code. To export an HTML-formatted value to Excel, you need to reformat it using C#.
3. Place the *Overdue indicator*attribute on a form or in a table.

### Formula Syntax

| Element | Description |
| --- | --- |
| `IF(Argument1, Argument2, Argument3)` | `IF()` function takes three arguments. If `Argument1` resolves to `true`, it returns `Argument2`. Otherwise, it returns `Argument3`. |
| `GREATEREQ($Actual_date, $Planned_date)` | `Argument1` — condition. The `GREATEREQ()` function returns `true`if `Actual_date` is greater than or equal to the `Planned_date`. |
| `$` | The `$` prefix refers to an attribute in the current record context. |
| `"<span style = 'color: #B22222; font-size: 200%; text-shadow: 0 0 1px black; position: absolute; top: 0px;'> ● </span>"` | `Argument2` — red indicator HTML code:  ●. The `color: #B22222` CSS statement sets red color. Other CSS statements define the indicator size and position. |
| `"<span style = 'color: #45A521; font-size: 200%; text-shadow: 0 0 1px black; position: absolute; top: 0px;'> ● </span>"` | `Argument3` — green indicator HTML code:  ●. The `color: #45A521`CSS statement sets green color. Other CSS statements define the indicator size and position. |

## See Also

[Configuring Conditional Coloring of an Attribute Value](https://kb.comindware.ru/article.php?id=2009)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
