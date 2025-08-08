---
title: Creating a Scenario
kbId: 2108
---


# Creating a Scenario

## Creating a Scenario from the Application Scenario List

1. Open the scenario list in an application. See [Viewing the Scenario List](https://kb.cmwlab.com/article.php?id=2110#mcetoc_1ginkc2is3).
2. Click **Create**.
3. The **New scenario** window will be displayed.
4. Configure the [scenario properties](#mcetoc_1gjo9vh451).

   _![   New scenario properties windowподпись](https://kb.cmwlab.com/assets/img_638ef4685ff7a.png)_
5. Click   ***Sa*****v*****e***.
6. The scenario designer will open.
7. Configure the scenario, see [Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109).

## Creating a Scenario for a Business Process Diagram Element

1. Open a business process diagram.
2. Select a diagram element.
3. In the item menu, click **Entry scenario***![](https://kb.comindware.ru/assets/img_6387209488025.png) or* **Exit scenario***![](https://kb.comindware.ru/assets/img_638720b096fbd.png)*.
4. The diagram element entry or exit scenario will be automatically generated.
5. The scenario designer will be displayed.
6. Configure the scenario. See [Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109).

   ![Creating the scenarios for process diagram element entry and exit](https://kb.cmwlab.com/assets/img_638efd311a50e.png)

   Creating the scenarios for process diagram element entry and exit

## Scenario Properties

- **Name**  — a descriptive name of the script.
- **System name** — a unique scenario name, transliterated automatically from the scenario name.
- **Description**  — an optional comment about the scenario's purpose.
- **Execution context**  — the account on behalf of which the scenario will be executed:
  - **By system** — the scenario will be executed with full rights of the **System** account, ignoring the role and permissions of the user who initiated the start event of the scenario. That is, the scenario will be able to *perform any actions*.
  - **By initiator** — the scenario will be executed if the user who initiated the start event has sufficient rights. If the user has insufficient rights, the system will generate an error.
- **Status**  — state of the scenario:
  - **Active**— every time the start event triggers, the configured action sequence will be executed.
  - **Suspended**— when the start event triggers, the configured action sequence will not be executed.

## Related Articles

**[Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109)**

**[Scenario Definition and List](https://kb.comindware.ru/article.php?id=2110)**

**[Scenario Actions](https://kb.comindware.ru/article.php?id=2106)**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
