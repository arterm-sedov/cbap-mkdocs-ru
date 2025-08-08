---
title: Scenario Definition and List
kbId: 2110
---


# Scenario Definition and List

## Scenario Definition

A **S****cenario**is a validation and data processing algorithm executed when a certain event is triggered. The scenario contains an action sequence executed when the specified event is triggered.

Use the convenient visual designer to configure the scenarios.

_![A scenario example](https://kb.cmwlab.com/assets/img_63909fe24c9bf.png)_

## Viewing the Scenario List

Click **Scenarios** on the application ***Administration*** page.

_![Scripts button on the application administration page](https://kb.cmwlab.com/assets/img_638f011d12f29.png)_

_![List of scenarios in the application](https://kb.cmwlab.com/assets/img_638f00b790f11.png)_

## Details and Operations in the Scenario List

- **ID** — a unique scenario identifier.
- **Title**— a descriptive scenario name.
- **Event** — a description of the event that triggers the scenario.
- **Execution context**— the account on behalf of which the scenario will be executed:
  - **By system** — the scenario will be executed with full rights of the **System** account, ignoring the role and permissions of the user who initiated the start event of the scenario. That is, the scenario will be able to *perform any actions*.
  - **By initiator** — the scenario will be executed if the user who initiated the start event has sufficient rights. If the user has insufficient rights, the system will generate an error.
- **Status**
  - **Active**— the scenario is executed every time the specified event occurs.
  - **Paused**— the scenario is not executed when the specified event occurs.
- New — click this button to create a new scenario. See [Creating a Scenario](https://kb.comindware.ru/article.php?id=2108).
- **Delete** — check the boxes for the scenarios to be deleted and click this button to delete them.
- **Properties**— check the box for a scenario and click this button to configure its properties. See [Scenario Properties](https://kb.cmwlab.com/article.php?id=2108#mcetoc_1gjo9vh451).
- **Open**  — double-click the scenario row to open the scenario designer. See [Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109).

## Related Articles

**[[Creating a Scenario](https://kb.comindware.ru/article.php?id=2108)](https://kb.comindware.ru/article.php?id=2152)**

**[Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109)**

**[Scenario Actions](https://kb.comindware.ru/article.php?id=2106)**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
