---
title: Using a Local Variable to Mass Process Records
kbId: 2098
---


# Using a Local Variable to Mass Process Records

In {{ productName }} you can configure the ability to mass process multiple records in a table, for example, if you need to change the status of several requests at the same time, confirm the payment of several invoices, etc. This article considers an example of the mass assignment of responsible persons for requests and the subsequent launch of the process for each of the request.

Since it is impossible to open any form when selecting several records (the form shows only the attributes of one record), it is proposed to use the mechanism of local variables. You can put a certain value in a local variable, which can then be applied or duplicated for all the selected records.

**Initial data:**

- Record template "Requests".
- Attribute of the "Accounts" data type — "Responsible".
- Process template "Request processing".

**Set-up:**

**1.** In the "Requests" record template, create a button with the following parameters:

- Display name — Assign responsible;
- Operation context — Record;
- Operation — Save;
- Operation result — Update data;
- Show the dialog— check this checkbox.

Save the button settings and go to the "Local variables" tab. Create a variable "Responsible" (data type — Account).

Go to the "Properties" tab and click on "Configure the dialog". Move the created local variable to the central area. Save the settings and move the button to the toolbar for tables.

**2.** Go to the application settings and click "Scenarios". Create a new scenario with the following parameters:

- Name — Assign responsible for requests
- Execution context — By initiator;
- Status — Active.

**3.** Set up the beginning of the scenario upon the button click that was created in step 1, add an action to change attribute values. Select the "Responsible" attribute, specify the operation on the values — Replace and in the "Value" field, select N3 and insert the following expression:

```

@prefix cmwsession: <http://comindware.com/ontology/session#>.
@prefix user: <http://comindware.com/ontology/user#>.
@prefix variable: <http://comindware.com/ontology/session/variable#>.
@prefix debug: <http://comindware.com/ontology/debug#>.

{
    cmwsession:context variable:dialogVariables ?v1.
    ?v1 variable:responsible ?value.
}

```

It is important to specify the system name written in the local variable after "***variable:***".

Then add the "Start a Process" action, select the "Request processing" process. Go to the "Additional" tab and check the boxes "Execute separately from the scenario" and "Ignore all errors", if this is not done, the process will not start on each of the entries, but only one of them.

**4.** Test. Select several requests, click on the "Assign responsible" button. A dialog box will open with the local variable "Responsible". Select a user, confirm the operation.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
