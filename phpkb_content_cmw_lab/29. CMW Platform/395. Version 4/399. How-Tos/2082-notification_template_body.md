---
title: Generate Notification Body Using a Template with Placeholders
kbId: 2082
---


# Generate Notification Body Using a Template with Placeholders

## Use Case

You might want to generate the e-mail body using a template with placeholders for variable data, for example, to notify the users about work results or deadline changes.

In this article, we will generate the notification text sent to employees during the vacation request approval process.

## Prerequisites

To proceed with the example, create the attributes as shown in the table below:

| **Record template name** | **Attribute name** | **Attribute system name** | **Attribute type** |
| --- | --- | --- | --- |
| *Vacation Requests* | *Notification template* | *message**Template* | **Text** |
| *Employee's full name* | *employeefullname* | **Text** |
| *Signing date* | *signingD**ate* | **Date & time** |
| *HR's full name* | *HRfullname* | **Text** |
| *Notification body* | *notificationbody* | **Text** |

## Instructions

1. In the *Vacation Requests* template, place the *Notification template, Employee's full name, Signing date, HR's full name,*and *Notification body*attributes on the form.
2. In the *Notification body* attribute properties, check the **Auto calculate** box.
3. In the **Calculated value**, enter the following [**formula**](#mcetoc_1gtqijebq0):
   ```
   FORMAT($messageTemplate, LIST($employeefullname, $signingDate, $HRfullname))
   ```

   Note

   Instead of calculating the attribute value, you can populate the message template using form rules or scenarios.
4. Create a record in the *Vacation Requests* template and fill in the *Notification template* field with the following text
   ```

   Good day, {0}!
   Please come to the HR Director's office on {1} to sign the vacation leave paperwork.
   Sincerely, Human Resources Specialist {2}

   ```

   Here the numbers in curly brackets `{0}` denote the placeholders to substitute with the *Employee's full name, Signing date,* and *HR's full name*.
5. Fill in the *Employee's full name, Signing date,* and *HR's full name* on the form.
6. The *Notification body*field should now contain the message body filled with the data you filled in.
7. Use the resulting *Notification body* attribute value in the notification messages.

### Formula Syntax

| Element | Description |
| --- | --- |
| `FORMAT(originalText, replacerTextList)` | The `FORMAT()` function takes two arguments:   - `originalText` — a string with numbered placeholders in curly braces: `{0}...{N}`. The placeholders are numbered from 0. - `replacerTextList` — an array of strings to replace the placeholders in the `originalText`.   The `FORMAT()` function looks up the placeholders in the `originalText`, replaces them with the corresponding `replacerTextList` elements and returns the resulting string. |
| `LIST(argument1, ..., argumentN)` | The `LIST()` function takes several arguments and returns an array of the argument values. |
| `$` | The `$` prefix refers to an attribute system name in the current record context. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
