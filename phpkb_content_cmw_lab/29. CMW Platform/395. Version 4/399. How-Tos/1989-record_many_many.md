---
title: Configuring Many-To-Many Relationship
kbId: 1989
---


# Configuring Many-To-Many Relationship

## Use Case

In the **CMW Platform**, you can define a many-to-many relationship between two record templates.

A many-to-many relationship links several records from one template to several records in another template.

For example, several employees may work on a project, and each employee can work on several projects.

In this article, we will configure a many-to-many relationship between the *Projects* and *Employees* templates using two different approaches: a direct link and an intermediate template.

## Prerequisites

To proceed with the example, create the templates as shown in the table below:

| **Record template** | **Description** |
| --- | --- |
| *Projects* | Stores the project records. |
| *Employees* | Stores the employee records. |

## Instructions

### Link the Templates Directly

1. In the *Projects*template, create the *Project Employees* attribute:
   - **Data type** — **Record**.
   - **System name**— *Project\_employees*.
   - **Linked template** — *Employees*.
   - Store multiple values — checked.
   - **Attribute interlinking** — **With a new one**.
     - **New attribute properteies**:
       - **Name** — *Employee Projects*.
       - **System name** — *Employee\_projects*.
       - Store multiple values — checked.

_![Configuring a many-to-many relationship with direct template linking](https://kb.cmwlab.com/assets/img_643e56f571d70.png)_

**Note**

This approach has certain limitations:

- You cant store project-specific employee details, such as their project role, rate, or workload percentage.
- You cant process or filter the interlinked attribute values in some contexts.
### Link the Templates via an Intermediate Template

1. Create the *Projects and Employees*record template.
2. In the *Projects and Employees*template, create the *Project* attribute:
   - **Data type** — **Record**.
   - **System name**— *Project*.
   - **Linked template** — *Projects*.
   - Store multiple values — unchecked.
   - **Attribute interlinking** — **With a new one**.
     - **New attribute properteies**:
       - **Name** — *Employee Link*.
       - **System name** — *Employee\_link*.
       - Store multiple values — checked.
3. In the *Projects and Employees*template, create the *Employee*attribute:
   - **Data type** — **Record**.
   - **System name**— *Employee*.
   - **Linked template** — *Employees*.
   - Store multiple values — unchecked.
   - **Attribute interlinking** — **With a new one**.
     - **New attribute properteies**:
       - **Name** — *Project Link*.
       - **System name** — *Project\_link*.
       - Store multiple values — checked.

**Note**

Using this approach, you can store project-specific employee data in the *Projects and Employees*template, such as time spent on the project, employee role, payment rate, etc.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
