---
title: Configuring a Scenario
kbId: 2109
---


# Configuring a Scenario

## Scenario Designer

**{{ productName }}** provides an easy-to-use visual scenario designer.

There are two ways to open the scenario designer:

1. Double-click the scenario row in the scenario list (see [Scenario Definition and List](https://kb.comindware.ru/article.php?id=2110)).
2. Click ***Entry scenario*** or ***Exit******scenario*** in the business process diagram element menu (see [Creating a Scenario for a Business Process Diagram Element](https://kb.cmwlab.com/article.php?id=2108#mcetoc_1gj3ssj8l2)).

_![Scenario designer](https://kb.cmwlab.com/assets/img_63906ed9d0478.png)_

## Scenario Configuration Buttons

The scenario designer provides the following buttons to configure the scenario.

1. ***Properties** —* configure the scenario properties. See [Scenario Properties](https://kb.cmwlab.com/article.php?id=2108#mcetoc_1gjo9vh451).
2. ***Clean*** — permanently delete all scenario elements. When you click this button, an empty ***Button click*** start event is placed in the scenario, as if the scenario was re-created.
3. ***Delete***— permanently delete the scenario.
4. ***Validate*** — check the scenario's integrity and functioning. Click this button to see the ***Validation result*** panel with a list of scenario errors.

   ![Scenario validation result](https://kb.cmwlab.com/assets/img_63907963b6c6c.png)

   Scenario validation result

## Scenario Element Configuration Buttons

Hover the mouse pointer over a scenario element to display the element configuration buttons.

1. ***Edit*** — configure the scenario element properties. See [Configuring the Scenario Elements](#mcetoc_1giv6huua1).
2. ***Go to context template*** — view the context template for scenario element execution.
3. ***Delete***  — permanently delete the scenario element.
4. ***Add action*** — create an action nested in or after the current scenario element.

   ![Scenario element configuration buttons](https://kb.cmwlab.com/assets/img_63907dcef1270.png)

   Scenario element configuration buttons

## Configuring the Scenario Elements

When you configure a scenario, the changes are saved and applied automatically.
### Configuring the Start Event

_![Scenario start event properties window](https://kb.cmwlab.com/assets/img_63908adf02d7d.png)_

1. Hover the mouse pointer over the scenario start event and click ***Edit***.
2. The start event properties window appears with the following properties.

- ***Description*** — a brief start event's purpose description.
- ***Type*** — a type of event that triggers the scenario. See the [Scenario Start Event Types and Properties](#mcetoc_1gj1c4ck70).
- ***Context template*** — the scenario will run in this record or process template when the specified event triggers.

#### Scenario Start Event Types and Properties

The start event types available in scenarios are listed below.

Some event types have additional properties to configure.

- ***Button******click*** — the scenario will run when the specified button in the ***context template*** is clicked***.***
  - ***Button*** — the button clicked to run the scenario.
- ***Record creation*** — the scenario will run when a record is created in the ***context template***.
- ***Record change*** — the scenario will run when the specified record attribute values in the ***context template*** change. If the attributes are not specified, the scenario will run when any attribute value in the ***context template*** is changed.
  - ***Attributes***— a list of ***context template*** attributes. Changes to these attribute values will trigger the scenario.
- ***Process start*** — the scenario will run when the ***context template***process instance is started.
- ***Message receipt*** — the scenario will run when a message is received through the specified connection and communication route.
  - ***Connection*** — the scenario will run when a message is received through this connection.
  - ***Communication route****—* a communication route to parse the message.
  - ***Variable name*** — a variable to store the message content parsed by the communication route.
- ***Token entry***— the scenario will run when a token enters the selected element of the ***context*** process ***template***diagram.
  - ***Diagram*** ***element*** — a token entering this process diagram element will trigger the scenario.
- ***Token exit***— the scenario will run when a token exits the selected element of the ***context*** process ***template*** diagram.
  - ***Diagram*** ***element*** — a token exiting this process diagram element will trigger the scenario.

## Configuring the Actions

### Creating an Action

1. Hover the mouse pointer over the scenario element to add an action after or inside it.
2. Click ***Add action***.
3. An of available actions will appear.
4. Select the desired action.
5. A new action will appear in the scenario designer.
6. Configure the action. See [Setting Up Action Properties](#mcetoc_1giv6k5ut4).

For detailed information about action properties, see `_![](https://kb.cmwlab.com/images/marker.png){Article-ID:2106}`[`.`](https://kb.comindware.ru/article/%d0%a2%d0%b8%d0%bf%d1%8b-%d0%b0%d0%ba%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d1%81%d1%82%d0%b5%d0%b9-1775.html)__![Creating an action in a scenario](https://kb.cmwlab.com/assets/img_63eb6556f41b0.png)_

### Creating Nested Actions

Other actions can be nested inside the ***Change the context**,* ***Execute on conditions***, ***Counter loop***, and ***Object loop*** actions.

To create a nested action, click the ***Add action*** button inside an action.

_![Creating a nested action in a scenario](https://kb.cmwlab.com/assets/img_63eb67cfc6608.png)_

### Setting Up Action Properties

1. Hover the mouse pointer over an action.
2. Click ***Edit***.
3. The action properties window appears.
4. Configure the action properties.
5. Click ***Save***.

_![Opening action properties in a scenario](https://kb.cmwlab.com/assets/img_63908d0e3269e.png)_

For detailed information about action properties, see `_![](https://kb.cmwlab.com/images/marker.png){Article-ID:2106}`[`.`](https://kb.comindware.ru/article/%d0%a2%d0%b8%d0%bf%d1%8b-%d0%b0%d0%ba%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d1%81%d1%82%d0%b5%d0%b9-1775.html)_### Deleting an Action

1. Hover the mouse pointer over the action to be deleted.
2. Click ***Delete***.
3. A delete confirmation window will appear.
4. Confirm the action deletion.

_![Deleting a scenario action](https://kb.cmwlab.com/assets/img_639094ddad17b.png)_

## Related Articles

**[Creating a Scenario](https://kb.comindware.ru/article.php?id=2108)**

**[Scenario Definition and List](https://kb.comindware.ru/article.php?id=2110)**

**[Scenario Actions](https://kb.comindware.ru/article.php?id=2106)**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
