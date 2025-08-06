---
title: Usage of account templates
kbId: 2089
---


# Usage of account templates

Information about all users of the system is contained in the system section "Accounts". The "Account" form displays some basic information:

- Full name
- Login
- Email
- Manager
- etc.

When creating your own solution, you may want to extend the user information with additional attributes. For example:

- for the HR personnel: employee number, date of entry to work, current number of vacation days, personal documents, etc.
- for the IT department: preferred way of contact, level of service, etc.

Within the application you can create several templates with the "Account template" type, for example, "Employees of the company", "Employees of the clients/partners", "Outsourcers", etc., within which you can expand the attributive composition of the system accounts. One user of the system can belong to several templates with the "Account Template" type.

When creating an attribute with the "Account" data type in the record template, you can additionally select an associated template with the "Account Template" type. This setting will allow you to use additional information about the user for:

- displaying in the record forms
- displaying in the tables
- building reports
- calculation of other attributes
- setting up business logic for the processes

Also, when you select an associated template with the "Account Template" type on the form in the "Accounts" drop-down list, this field will display only users attached to the associated template with the "Account Template" type.

In the settings of the template with the "Account template" type, sections similar to the template with the "Record template" type are displayed, with the exception of the import function, because in order to create a user, additional parameters are required, such as login and password.

In the button area for tables in the template with the "Account template" type, by default there is a “Create” button that allows you to create a new user and automatically add him/her to the current template with the "Account template" type.

Adding a user to a template with the "Account template" type is available:

- In the button area for tables in a template with the "Account template" type, by clicking on the "Add to template" button. It is possible to add several users at once to the current template with the "Account template" type.
- In the "Accounts" section, by selecting a user and clicking on the "Link to template" button. It is possible to add multiple users to multiple templates with the "Account Template" type.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
