---
title: Making changes to a workflow in real time
kbId: 1993
---


# Making changes to a workflow in real time

Over time, your company may need to adjust previously configured business processes. This could be due to a change in company structure, industry standards, or business requirements. One way or another, you need to promptly make the required changes to the processes. A key benefit of the **CMW Platform** is the ability to change your workflow on the fly.

Thanks to the Elastic Data technology, you don't need to have programming skills and special knowledge to do this. You can simply go into the workflow settings and change them.

If your business process has become more complex, for example, another department (a group of employees) has been added or a certain role has to perform a new task, you can easily add the necessary steps and transitions, as well as delete them with one click.

To do this, go to the settings of the required process template and open the «***Diagram***» tab. Here you can adjust your business process: add and remove steps, change responsible persons and deadlines, indicate possible scenarios for token movement, and much more.

_![«Diagram» tab](https://kb.cmwlab.com/assets/2021-12-29_09h00_24.png)_

Then click the «***Edit***» button to enable the ability to make changes. The next step is, in fact, making changes to the executable process. After all the necessary changes have been made, click the «***Publish***» button and you will have two options: «***Change current version***» and «***Create new version***».

_![Choosing publishing option](https://kb.cmwlab.com/assets/2021-12-29_09h04_36.png)_

When you change the current version, the new diagram will be applied to the already running process instances from the previous version. It is important to consider the position of tokens in running instances. Tokens will be moved to their previous positions on the diagram (position is the system name of the process element on which the token is located). Accordingly, tokens for which no previous positions will be found will be deleted. The missing tokens will need to be manually placed using the token management feature in each process instance.

When you choose to create a new version, all new instances will be launched according to the new version, and the process instances launched according to the old version of the process diagram will be finalized according to their version.

**Diagram versioning**

In addition, **CMW Platform** supports versioning of process diagrams, which means that every published version is saved in the system. If you need to restore any of the versions, just click «***Select version***» in the ribbon, double-click on the required version and click «***Edit***» and then «***Publish***».

_![Selecting a version](https://kb.cmwlab.com/assets/2021-12-29_09h10_17.png)_

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
