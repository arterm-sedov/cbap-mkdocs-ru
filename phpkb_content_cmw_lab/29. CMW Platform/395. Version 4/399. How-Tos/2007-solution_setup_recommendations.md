---
title: Recommendations for setting up a business solution
kbId: 2007
---


# Recommendations for setting up a business solution

After installing **CMW Platform** and logging into the product for the first time, the administrator is granted access to all sections of the system.

Setting up a business solution starts with a business application. A business application is a collection of related sections, settings, and data, and is also the main element for transferring configurations between environments.

By default, a system application «*System business app*» is created in the new product, where all sections for configuring the system are located. It can be used to create a specific business solution, such as Contract approval, CRM, HR or MRO, but it is recommended that you create your own business applications for each specific solution.

Before you start setting up a business solution, you need a basic understanding of the following points (we use CRM system as an example):

- List of information (master data/reference information) required and used during work:
  - Counterparties;
  - Contact persons;
  - Inquiries;
  - Contracts;
  - etc.
- List of processes for automation:
  - Inquiry processing;
  - Formation of a commercial offer;
  - Contract approval;
  - etc.
- List of roles involved in the processes:
  - Sales manager;
  - Head of Sales;
  - CFO
  - etc.
- List of required reports:
  - Sales plan;
  - Managers’ workload;
  - etc.

When the list of all the necessary data, processes, roles, etc. is defined, you can proceed to creating and configuring record templates, processes, roles, etc.

For visual modeling, you can use the following diagrams:

- Business capabilities diagram;
- Class diagram;
- Data model diagram.

**Note :** keep in mind that one record template can only be stored in one business application. To transfer an record template to another business application, open the record template settings and on the «***Properties***» tab, click the «*Change the business application*» button.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
