---
title: Stopping the Process on a Button Click
kbId: 2129
---


# Stopping the Process on a Button Click

## Use Case

When setting up a process, you often get several options for its completion logic. For example, you stop the process when an inquiry may be approved or rejected. Or you might need to end the process from the outside, for instance, if the initiator wants to withdraw a contract already sent for approval. For such a case, you can create a button that will stop the whole process at any step.

**Scenario:** In the *Contract Approval* process, the initiator decides that a contract is no longer valid and wants to cancel its approval.

**Solution:** We will use inter-process communication and create a button to cancel the contract approval.

## Setting up the Processes and Templates

1. In the **record** **template** (for instance, *Contract Approvals*) linked to the main *Contract Approval* **process template**, create a **Text** attribute:  ***ProcessID***.
2. On the *Contract Approval* process diagram:
   - Open the exit scenario of the start event.
   - Add **Change attribute values** action.
   - In the action properties, specify the ***ProcessID*** attribute value using the following **formula**: `FORMAT("{0}", LIST($$ProcessObject))`. This formula returns the active process ID.
3. On the same process diagram:

- Add a parallel gateway between the **Start event** and *User Task 1*.
- To the parallel gateway, add **Receive message intermediate event** and **End event**. One token will go to the *User Task 1*, and the other will go to the **Receive message intermediate event**.
- In the **Receive message event properties**:
  - Specify a unique **Message name** (you will later use it in the **Send message event**) on the **Advanced** tab.
  - Configure the attribute mapping on the **Message data** tab if needed.

Thus, when the process starts, two tokens are active. The process will end according to the configured logic (for example, upon the contract approval) or when a cancellation message is sent to the **Receive message intermediate event**.

![Main process diagram](https://kb.cmwlab.com/assets/canceleng1.png)

Main *Contract Approval*process diagram

**Note:**For this scenario, all end events in the process must be terminators so that they stop the whole process, not just one of its tokens.

1. Create an auxiliary **process** **template** *Contract Withdrawal* with a new linked **record template** (for example, *Contract Withdrawals*).
2. In this new **record template,**create the attributes:
   - **Record** attribute *Contract* linked to the *Contact Approvals***record template** (with **attribute interlinking**)
   - **Text** attribute *Comment* (place it on the *Contract Withdrawal* process **Start form**).

![Auxiliary process diagram](https://kb.cmwlab.com/assets/img_6430203a82d6d.png)

Auxiliary *Contract Withdrawal*process diagram

1. On the *Contract Withdrawal* diagram *:*
   - Add a **Send message intermediate event** between the **Start event** and **End event.**
   - In the **Send message event properties:**
     - Specify the same **Message name** as in the [**Receive message event** **properties**](#Receive-Message-Properties) on the *Contract Approval* process diagram,
     - Specify the **Process instance** using the following **formula**: ***$Contract->ProcessID**,*where:
       - [***$Contract*** is the attribute](#Contract-Record-Attribute) linked to the *Contract Approvals* record template.
       - ***ProcessID*** is the attribute created in [step 1](#ProcessID-Attribute). It stores the active process ID.
       - Configure the attribute mapping on the **Message data** tab, if necessary.
   - Configure the **Start form** if needed.
2. In the *Contract Approvals* **record template** (linked to the *Contract Approvals* process), create a new button: *Withdraw contract**.*
3. Configure the *Withdraw contract* button properties:
   - **Operation context** — **Record**
   - **Operation** — **Start process from linked template**
   - **Operation result** — **Refresh data**
   - **Template** — *Contract Withdrawal* (**attribute**: *Contract Approval*)
   - **Display condition** — specify when to show the button if needed.
4. Place the *Withdraw contract* button on any form or table toolbar.
5. Test the process.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
