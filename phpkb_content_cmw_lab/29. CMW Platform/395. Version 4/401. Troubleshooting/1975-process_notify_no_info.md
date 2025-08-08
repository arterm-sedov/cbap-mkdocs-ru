---
title: Information in the process notification was not sent
kbId: 1975
---


# Information in the process notification was not sent

As part of the process, it is possible to configure the sending of an external notification (for example, to notify the client about the approval of the contract), with which you can transfer various kinds of data: text, attachments, or any other data connected with the process.

If, after the process has started, it turned out that some of the information was not sent, in this case it is worth paying attention to the following possible places where it could have been lost:

1. **The mapping of the message attributes and the process data was configured incorrectly.**

   On the business process diagram, go to the settings of the «***Send message event***» element and in the «***Message Data***» tab check the correctness of the data mapping.

   After making your changes, publish the process diagram.
2. **The mapping of the message attributes in the communication routes was configured incorrectly.**

   Go to the «**Communication routes**» section, select the outgoing route used in the process and check the correct use of the attributes in the «***Message properties***» tab.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
