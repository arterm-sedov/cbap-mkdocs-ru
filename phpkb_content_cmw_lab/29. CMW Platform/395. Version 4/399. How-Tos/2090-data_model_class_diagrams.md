---
title: Viewing and Editing Data Model and Class Diagrams
kbId: 2090
---


# Viewing and Editing Data Model and Class Diagrams

## Use Case

In each **CMW Platform** application, you can create **data model diagrams**and **class****diagrams**. See [Understanding the Application Data Model](https://kb.comindware.ru/article.php?id=2091).

The data model and class diagrams visually represent and help to design the application architecture and define the template relationships.

You can also use the data model and class diagrams to visualize the existing application architecture. For instance, you can view all the templates linked to a template of interest.

## Using the Data Model or Class Diagram Designer

Use the data model diagram designer to view or configure the account and record templates along with their relationships and attributes.

Use the class diagram designer to view and configure the account, process, and record templates along with their associations, cardinality, attributes, and button operations.

1. Go to the **Data model diagrams** or **Class Diagrams** tab on the application **Administration** – **Diagrams** page.
2. Create or open a diagram.
3. View, create, or configure the templates, their relationships, and attributes.

### Operations in the Diagram Designer

#### Diagram operations

- **Create a template** — drag the **New record template**, **New account template**, or **New process template** (only on the class diagram) to the diagram from the element pane.
- **Add a template to the diagram** — drag the template to the diagram from the element pane.
- **Select version** — select a saved diagram version. The current diagram will be replaced with the selected one.
- **Create new version**— save the current diagram as a new version.
- **Clone**— select a saved diagram version and duplicate it. The cloned version will appear in the diagram designer.
- **Settings** — rename the diagram or its current version *(for the class diagram)*.
- **Refresh data**— update the diagram with the newly created attributes and links.
- **Export** — save the diagram as an SVG file.
- **Show system names**— check this box to view the attribute and template system names instead of display names.
- **Clean** — permanently remove all the elements from the diagram. The templates and attributes will not be deleted.
- **Show archive** *(on the class diagram)* — check this box to show archived elements on the diagram.
- **Go to application administration** *(on the class diagram)* — go to the application **Administration** page.

#### Selected template operations

When you select a template on the diagram, the element menu appears where y can perform the following operations.

- **Add attribute** — create and configure the new attribute properties.
- **Go to template** — open the template properties page.
- **Go to template** — create a new relationship between the templates. Click this button and drag the arrow to the target template.
- **View linked items** — show the templates linked to the selected template on the diagram.
- **Collapse/expand group** *(on the data model diagram)* — minimize the template element to its header or expand to show the attributes.
- **Delete** — delete the element from the diagram. The template itself will not be deleted from the application.

**Notes**

- When you edit the data model diagram, all the changes are applied to the database automatically.
- You can save several versions of a data model diagram and recall them to have different class visualizations. Choosing a different data model or class diagram version does not change the application data model.
- You can create several data model diagrams and class diagrams for an application, for example, to show only certain record template relationships.
## See Also

[Understanding the Application Data Model](https://kb.comindware.ru/article.php?id=2091)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
