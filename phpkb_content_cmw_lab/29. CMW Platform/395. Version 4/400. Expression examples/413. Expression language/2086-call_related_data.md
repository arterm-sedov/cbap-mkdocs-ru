---
title: Retrieving Related Data
kbId: 2086
---


# Retrieving Related Data

In order to retrieve the data of an associated record template using an attribute with the “Record” data type that references the required record template, add the "***->***" character and the system name of the associated record template attribute that needs to be called.

| Record template | Attributes |
| --- | --- |
| Car | Driver – system name of the attribute of the "Record" type that references the “Staff” record template |
| Staff | Name – system name of the attribute |

To retrieve the name of a driver from thr “Car” entry, use the following expression: ***$Driver->Name***.

You can use the links an unlimited number of times, but be careful not to create a loop.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
