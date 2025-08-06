---
title: Setting up periodic reminders for open tasks
kbId: 2127
---


# Setting up periodic reminders for open tasks

CMW Platform, in its basic configuration, supports sending system notifications to a user on a given task as well as process notifications with information from a business process.

Sometimes it becomes necessary to set up reminders for an employee about his open tasks, for example, every day at a certain time.

For this setup, it is necessary to create 2 business processes:

- Search for employees to send a reminder
- Sending daily reminder

The first process will be started by timer every day, for example, at 7am and search for employees who have open tasks at this point in time, and for each employee the system will initiate the subprocess "Sending daily reminder", which in its turn will form and send the list of the employee's open tasks in the form of a table by email.

**Configuring the "Sending daily reminder" process**

**1.** Create a new Process Template.

_![New Process Template](https://kb.cmwlab.com/assets/remind_eng5.jpg)_

**2.** In the associated Record Template, create the following attributes:

- ***Employee*** — an attribute of the "Account" data type to whom the reminder will be sent;
- ***Body*** — a calculated text attribute of the HTML text display format that will contain a task table. Tick the box "Calculate using an expression" and insert the following expression in the "Calculated value":

```
 
@prefix cmw: <http://comindware.com/logics#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix configuration: <http://comindware.com/ontology/configuration#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
 
{
           ?confid a configuration:Configuration.
           ?confid configuration:baseUri ?baseUri.
           ("Searchesforemployeestosendareminder" "Employee") object:findProperty ?Employee.
 
           ?item ?Employee ?EmployeeVal.
                      
    #First table
    ("<p style='font-size: 100%' >List of tasks</p>" "<table border='1' style='width: 60%; border-collapse: collapse; border: 1px solid black' ><tbody> <tr><td style='padding: 2px; width: 200px; border: 1px solid black'>Task</td> <td style='width: 200px; padding: 2px; border: 1px solid black'>Срок</td></tr>") string:concatenation ?firstHeaderRow.
 
    from {
                       ?tasks a cmw:UserTask.
                       or {?tasks cmw:assignee ?EmployeeVal.}
                       or {?tasks cmw:possibleAssignee ?EmployeeVal.}.
                       ?tasks cmw:taskStatus taskStatus:inProgress.
                       ?tasks cmw:title ?title.
                       ?tasks cmw:id ?id.
        ("{0}" ?title) string:format ?titleVal.
        ("{0}" ?id) string:format ?idVal.
                      
                       or {?tasks cmw:dueDate ?dueDate.}
                       or {"" -> ?dueDate.}.
                      
        ("{0}" ?dueDate) string:format ?dueDateVal.
                      
        ("<tr><td class='A' style='padding: 2px; border: 1px solid black; '><a href='" ?baseUri "#task/" ?idVal "'>" ?titleVal "</a></td><td align='right' style='padding: 2px; border: 1px solid black; text-align: right'>" ?dueDateVal "</td></tr>") string:concatenation ?firstRow.
    } select ?firstRow -> ?firstFactrow.
    (" " ?firstFactrow) cmwstring:join ?firstFact.
    (?firstHeaderRow ?firstFact "</tbody></table> <br/>") string:concatenation ?first.
    ?first  -> ?value.
}

```

- ***To*** — a calculated text attribute that will contain the employee’s email address. Tick the box "Calculate using an expression" and insert the following expression in the "Calculated value":

```
 $Employee->cmw.account.mbox
```

**3.** Create a process diagram as follows:

_![Process scheme](https://kb.cmwlab.com/assets/remind_eng6.jpg)_

**4.** Configure the settings for the sending message event.

**5.** Publish the process.

**Configuring the "Search for employees to send a reminder" process**

**1.** Create a new Process Template.

_![New Process Template](https://kb.cmwlab.com/assets/remind_eng1.jpg)_

**2.** In the associated Record Template, create an attribute:

- ***Employees*** — an attribute of the "Account" data type. Tick the boxes "Store multiple values" and "Calculate using an expression" and insert the following expression in the "Calculated value":

```
 
@prefix cmw: <http://comindware.com/logics#>.
@prefix container: <http://comindware.com/ontology/container#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
 
{
            ?class cmw:className "Account".
            ?value a ?class.
            ?value account:active true.
            not {?value cmw:isDisabled true.}.
            or {?tasks cmw:assignee ?value.}
            or {?tasks cmw:possibleAssignee ?value.}.
            ?tasks cmw:taskStatus taskStatus:inProgress.
}

```

- ***Reminders*** — an attribute with the "Record" data type, linked template is "Daily reminders". Establish a relationship with the new interlinking attribute — Search. Tick the box "Store multiple values".

**3.** Create a process diagram as follows:

_![Process scheme](https://kb.cmwlab.com/assets/remind_eng2.jpg)_

**4.** Configure the start timer event.

_![Timer configuration](https://kb.cmwlab.com/assets/remind_eng3.jpg)_

**Note :** If needed, also provide a plain start event to be able to manually start the process without having to wait for a new work day.

**5.**Set up a scenario at the entrance to the reusable subprocess to create records that the subprocess will then run on.

_![Scenario setup](https://kb.cmwlab.com/assets/2023-02-09_12h50_34.png)_

**5.1.** The first two actions are added by default, so start by adding the "Object loop" action and setting it up.

_![Action "Object loop"](https://kb.cmwlab.com/assets/2023-02-09_12h54_30.png)_

The variable "local" will store one instance from the specified selection at a loop. At the bottom, specify the "Employees" attribute, in which employees with active tasks are calculated.

**5.2.** Add the "Create a record" action and configure it.

_![Action "Create a record"](https://kb.cmwlab.com/assets/2023-02-09_12h57_57.png)_

- Target record template — Specify the record template "Daily Reminders"
- New record reference — specify the "Reminders" attribute created in step 3.
- Operation on the values — specify "Add".

**5.3.**Add the "Change attribute values" action and configure it.

_![Action "Create attribute values"](https://kb.cmwlab.com/assets/2023-02-09_13h17_47.png)_

Click "Create", select the "Employee" attribute, select "Replace" for "Operation on the values", and paste the $$local formula in the last column.

**6.** Configure the reusable subprocess.

_![Subprocess configuration](https://kb.cmwlab.com/assets/2023-02-09_13h21_21.png)_

In the "Record to execute the process", specify the attribute "Reminders", and in the "Called process template" — "Sending daily reminder".

**7.** Publish the process and test.

Before starting testing, check the operability of the E-mail sending connection and the correct configuration of the outgoing communication route.

**Note :** for the correct computation of the calculated fields and the sub-process launch formulas, check the exact match of the system name of each Record Template and attribute, as well as Process Templates.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
