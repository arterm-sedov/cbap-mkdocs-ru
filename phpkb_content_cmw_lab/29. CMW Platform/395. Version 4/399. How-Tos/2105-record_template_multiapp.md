---
title: Working with a record template from different applications
kbId: 2105
---


# Working with a record template from different applications

Record template in **CMW Platform** is a data registry, like an Excel sheet or table in a relational database.

Application in **CMW Platform** is a separate business solution, which has its own set of templates, diagrams, roles and variables, as well as its own navigation, integration and data path sections.

**CMW Platform** provides many options for how applications interact. This article will consider the scenario of working with one record template in different applications. This may be necessary when the same record template must be used in two applications, for example: CRM and SRM applications use a single directory "Clients". In order not to duplicate data and not create two "Clients" record templates, you can create one such record template in one application, specify all the necessary relationships, and then transfer it to another application. Old links will remain, but you can build new links in another application.

**1.** To move a record template to another application, go to the properties of the record template and click the "***Change the application***" button.

_![Record template properties](https://kb.cmwlab.com/assets/2022-11-11_10h00_08.png)_

**2.** Then select a new application, click the "***Save***" button in the application change window and the "***Save***" button in the properties of the record template.

_![Application change](https://kb.cmwlab.com/assets/2022-11-11_10h00_25.png)_

In the current record templates in the CRM application, all links to the "Clients" record template are preserved and continue to work, and now you can create attributes in the SRM application that refer to the "Clients" record template. In order to create new links to the "Clients" record template in the CRM application, you need to change the application again.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
