---
title: Configuring E-mail Receiving
kbId: 2001
---


# Configuring E-mail Receiving

## Use Case

The **CMW Platform** can send and receive e-mail messages with any data: requests, inquiries, etc.

In this article, we will set up the e-mail connection and communication route to receive and parse requests in a business process.

## Instructions

1. Create a new **E-mail receiving** connection. Specify the e-mail server and account to receive the requests.
   **Note:** Each unread message in this e-mail account will be processed and marked as read.
2. Create a new **Incoming messages** communication route.
   - On the **Main properties** tab:
     - Select the **Connection**, created in Step 1.
     - Select a **Process** to execute upon receiving an e-mail message.
       - To use one e-mail account for one request type (e.g., new requests only), specify the corresponding business process.
       - To use one e-mail account for different request types or subsequent responses, create an intermediate process that will handle them.
     - Based on your use case select the **Route target**:
       - To process all messages as new requests, select **New process instance**.
       - To parse subsequent responses for existing requests and send the data further to a pending process, select **Existing process instance**.

         ![Example of an intermediate process to handle new requests and subsequent responses](https://kb.cmwlab.com/assets/img_643d277cf0e5f.png)

         Example of an intermediate process to handle different new requests and subsequent responses
   - On the **Message attributes** tab, specify the attributes to store the incoming e-mail message elements:
     - **From address**
     - **From name**
     - **To address**
     - **To name**
     - **Subject**
     - **Body**
     - **CC address**
     - **CC name**
     - **BCC address**
     - **BCC name**
     - ******Attachments******

_![Mapping e-mail elements to the CMW Platform attributes](https://kb.cmwlab.com/assets/img_643d28bfee1f7.png)_

1. On the process diagram, create or select a **Receive message start event**.
   - On the **Advanced** tab, select the communication route created in [Step 2](#STEP2).
   - On the **Input mapping** tab, map the record template attributes to the e-mail message attributes.

_![Mapping the record template attributes to the e-mail message attributes](https://kb.cmwlab.com/assets/img_643d2ac91896f.png)_

**Note:** Using the CMW formula or N3 language expressions and scenarios, you might need to parse the e-mail subject line, body, or other elements (e.g., to determine the request type or decide if the message is a new request or a response regarding an existing one).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
