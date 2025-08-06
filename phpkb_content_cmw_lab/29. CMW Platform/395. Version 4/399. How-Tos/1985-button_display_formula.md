---
title: Configuring Button Display Condition with Formula
kbId: 1985
---


# Configuring Button Display Condition with Formula

## Use Case

You can show or hide a button depending on the application context. For this, define the button **Display condition** using a **formula** or an **N3 expression.**

In this article, we will create and configure the **Add new item**button to be visible only when the *Request* *Status* is *New*or *AddedToCart*.

## Prerequisites

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Request* | *Status* | **Record** | The *Status* attribute is linked to the *Request\_status* template. |
| *Request\_status* | *Status\_code* | **Text** | The *Request\_status* template contains records with the following *Status\_code* values:   - *New* - *AddedToCart* - *Pending* |

## Instructions

1. In the *Request* record template, go to the ***Buttons*** tab.
2. Create the **Add new item** button.
3. On the ***Display condition*** tab enter the [**formula**](#mcetoc_1gtntho192):
   ```
   OR($Status->Status_code == "New",$Status->Status_code == "AddedToCart")
   ```
4. Click **Save** to save the button.
5. Place the **Add new item** button on the default form toolbar in the *Request* record template.
6. Test the resulting button:
   - Create a *Request* with the *New* or *AddedToCart*status: the **Add new item** button should be visible.
   - Create a *Request* with the *Pending*status: the **Add new item** button should not appear.

### Formula Syntax

| Element | Description |
| --- | --- |
| `OR()` | This function takes two arguments and returns `true` if any of the arguments is `true`. In our case, we evaluate if the *Status\_code* attribute value equals *New*or *AddedToCart*. |
| `$` | This prefix refers to an attribute in the current record context. |
| `->` | This operator refers to an attribute of the linked *Request\_status* template. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
