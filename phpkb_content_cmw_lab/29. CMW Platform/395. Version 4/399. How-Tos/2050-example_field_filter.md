---
title: Reference Attribute Filter Example
kbId: 2050
---


# Reference Attribute Filter Example

This article describes an example of a client contracts filter on the request form.

The system names of the record templates and attributes used in the example are given in the table:

| Record template | Attributes |
| --- | --- |
| Requests | contractclient\_requestor |
| Contracts | client |

The following functions and operators will be used in the expression:

- "***EQUALS()***" function to select a record that corresponds to the client in the request;
- "***from***" operator for listing all records from the "Contracts" record template;
- "***where***" operator to select records that match the condition;
- "***select***" operator for selecting attribute values.

**Step-by-step instruction:**

**1.** Create and customize record templates and attributes.

**2.** In the "*Requests*" record template, open "*Forms*".

**3.** Add the "*contract*" attribute to the form.

**4.** Enter an expression in the filter box.

```
from a in db->Contracts where EQUALS($client_requestor,a->client) select a->id
```

**Syntax**

| Element | Definition |
| --- | --- |
| from a in db->Contracts | Declaring a local variable *a*.  Declaring the "*Contracts*" record template as a data source: *db->Contracts*. Enumerate all entries from the "*Contracts*" record template. |
| where EQUALS($client\_requestor,a->client) | Selecting a record in which the value in "*client\_requestor*" of the current request matches the value of the "*client*" attribute in the “*Contracts*” record template. |
| select a->id | Select the required record IDs. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
