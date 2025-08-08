---
title: Configuring Dynamic Field Display Using a Form Rule
kbId: 2070
---


# Configuring Dynamic Field Display Using a Form Rule

## Use Case

In the **CMW Platform**, you can define a set of rules for any form to control its element behavior.

Each rule can include several conditional actions:

- Set field values
- Show field validation warnings and error messages
- Change element access mode: require entry, allow entry, read-only
- Hide elements

In this article, we will define a form rule to show the hidden fields only when the preceding fields are filled.

## Prerequisites

In the example scenario, when creating a business trip request, an employee selects the destination country, city, and airport.

To streamline the user experience, we initially show the *Country* hide field and hide the *City* and *Airport* fields. When the user selects the country, the *City* field appears. When the user selects the city, the *Airport* field appears.

To proceed with the example, set up the template, attributes, and form fields as shown in the table below:

| **Record template name** | **Attribute and field display name (system name)** | **Field Access setting on the form** |
| --- | --- | --- |
| *Travel requests* | *Country (request\_country)* | **Require entry** |
| *City (request\_city)* | **Hide** |
| *Airport (request\_airport).* | **Hide** |

## Instructions

1. In the *Travel requests*template, open the default form.
2. Open the ***Form rules*** designer using the dropdown next to the form heading.
3. Add a rule and an action to the rule.
4. Configure the **Action properties**.
   - From the **Form element** dropdown, select the *City (request\_city)* field**.**
   - From the **Action** dropdown, select **Change access****.**
   - From the **New value**dropdown, select **Require entry**.
   - In the **Execution condition** field, enter the [**formula**](#mcetoc_1gtqijebq0):
     ```
     NOT(EMPTY($request_country))
     ```
5. Add a second action to the rule.
6. Configure the **Action properties**.
   - From the **Form element** dropdown, select the *Airport**(request\_airport)* field**.**
   - From the **Action** dropdown, select **Change access****.**
   - From the **New value**dropdown, select **Require entry**.
   - In the **Execution condition** field, enter the [**formula**](#mcetoc_1gtqijebq0):
     ```
     NOT(EMPTY($request_city))
     ```
7. Click ***Save***.

### Formula Syntax

| Element | Description |
| --- | --- |
| `NOT()` | This function returns `true` if its argument resolves to `false`. |
| `$` | This prefix refers to an attribute in the current record context. |
| `EMPTY()` | This function returns `true` if its argument has an empty value. |

## See Also

[Configuring Context-Dependent Filter for Record Attribute](https://kb.comindware.ru/article.php?id=2022)

[Configuring Form Rule Using Formula](https://kb.comindware.ru/article.php?id=1987)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
