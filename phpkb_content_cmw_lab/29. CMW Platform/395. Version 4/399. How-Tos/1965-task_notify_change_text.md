---
title: Customizing Notification E-mail Message
kbId: 1965
---


# Customizing Notification E-mail Message

## Use Case

The **CMW Platform** can send users notifications about the tasks assigned to them.

You can use the [default task notification e-mail](#mcetoc_1gtl1ap9e2) or create a [custom task notification e-mail](#mcetoc_1gtl9cege4).

## Enabling Task Notification Sending

1. Set up **E-mail sending** connection under **E-mail connections** in **Administration – Connections**.
2. Check the **Use by default box** in the **E-mail sending** connection properties to use it for task notification sending.
3. Check the **Enable task notifications** box in **Administration –** **Global configuration**.

## Default Task Notification E-mail

The default new task notification e-mail is shown below and contains the following details:

- *Subject* *line* — the task type and title.
- *Task title*(e.g., *Approve Capex Request*) — set on the **Advanced** tab of the **user task** properties on the process diagram. The task title is a hyperlink to the **user task form**.
- *Record title*(e.g., *item 9794*) — the value of the attribute **used as a record title** of the record linked to the process instance. The record title is a hyperlink to the record template **default form**.
- *Task link* — generated automatically. It leads to the **user task form**, defined on the process diagram.
- *Deadline*(e.g., *Dec 17*) — calculated from the **Duration** value on the **Advanced** tab of the **user task** properties on the process diagram.
- *Process name*(e.g., *Capex Approval process*) — set in the **process template**properties.

_![Default new task e-mail notification](https://kb.cmwlab.com/assets/img_6433b85fce381.png)_

To open the task form, click ***Go to the task***or the task title (*Approve Capex Request* in the illustration).

To open the record form linked to the task, click the record title (*item 9794* in the illustration).

## Customizing the Task Notification E-mail

To customize the subject or body of the task notification e-mail (e.g., to include specific information):

1. Go to **Administration — Communication routes**.
2. Create a new **Task notification** communication route under **System connections**.
3. In properties of the **Task notification** communication route:
   - On the **Message attributes**tab, configure the attributes to use in the e-mail.
   - On the **Message properties** tab, configure the e-mail **Subject**and **Body** using the attributes from the **Message attributes**tab.
4. Open the **user task** properties on the process diagram.
   - On the **Message data** tab:
     - Specify the communication route created in Step 2.
     - Configure the attribute values to substitute in the task notification e-mail (configured in Step 3).
5. Publish the process diagram.
6. Test the process task notifications.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
