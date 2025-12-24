---
title: Configuring a Calculated Attribute with a Formula
kbId: 1991
---


# Configuring a Calculated Attribute with a Formula

## Use Case

The **CMW Platform** can calculate an attribute value on the fly (without storing it in the database) using a **formula**, **N3** expression, **DMN** table, or another **attribute**.

In this article, we will configure the automatic client assignment for the currently logged-in user.

## Prerequisites

In our example, we have a database of clients, company managers, and requests. A client is attached to each manager. So, we can automatically assign a client when the manager creates a request.

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Request* | *ClientForCurrentUser* | **Record** | The *ClientForCurrentUser* attribute is linked to the *Clients* template and calculated based on the data stored in the *Contact\_persons*template. |
| *Contact\_persons* | *Client* | **Record** | The *Client* attribute is linked to the *Clients* template. |
| *Manager* | **Account** | The *Manager* attribute stores the manager account ID. |
| *Clients* | *Name* | **Text** | The *Clients* template contains the client records. The *Name* attribute stores the client name. |

## Instructions

1. In the *Request* template, open the *ClientForCurrentUser* attribute.
2. Check the **Calculate using an expression** box
3. In the **Calculated value** field, enter the [**formula**](#mcetoc_1gto5h8ao2):
   ```
   from a in db->Contact_persons where EQUALS(a->Manager,USER()) select a->Client->name
   ```
4. Click **Save** to save the attribute.

### Formula Syntax

| Element | Description |
| --- | --- |
| `from a in db->Contact_persons` | `from` operator defines the data source:   - Declares a local variable: **`a`** - Declares the *Contact\_persons* template as the data source: `in db->Contact_persons` - Collects all records from the *Contact\_persons* template to the variable **`a`** |
| `where EQUALS(a>Manager,USER())` | `where` operator defines the data selection condition:   - `USER()` function returns the current user ID. - `EQUALS()` function returns `true` if the *Manager*attribute value in a *Contact\_persons* record equals the current user ID. |
| `select a->Client->Name` | `select` operator collects the entities matching the selection condition:   - Returns an array of the *Name* attribute values from the *Clients* records that correspond to the current user. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
