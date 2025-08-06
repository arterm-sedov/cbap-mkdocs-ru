---
title: Setting up coloring logic for chevrons
kbId: 2096
---


# Setting up coloring logic for chevrons

{{ productName }} has a tool for visually displaying stages — chevrons. A distinctive feature of chevrons is the ability to paint each stage with a different color according to a specified rule.

To correctly set the color representation of the chevron, it is important to set the correct conditions. The coloring logic is the same for all chevrons, it is recommended not to use the attributes of the main record template where the collection is planned to be displayed.

Let's analyze an example of visualization of the stages of an application for a car.

**1.** In the record template referenced by the chevron attribute, create two attributes:

- Stage start date (data type — Date and time, display format — any);
- Stage completion date (data type - Date and time, display format — any).

**2.** On the diagram of the main process for approving an application for a car, configure the filling of the attributes created in step 1 for each stage (at the entrance and exit of the corresponding tasks).

**3.** On the form where the chevron is located, in the attribute properties, add the rules for coloring entries:

- Color #efbb3a — Condition ***AND(NOT(EMPTY($StartDate)),EMPTY($EndDate))*** (the chevron will be colored orange if the stage has started);
- Color #338320 — Condition ***AND(NOT(EMPTY($EndDate)),NOT(EMPTY($StartDate)))*** (the chevron will be colored green if the stage is completed);
- Color #a8a8a8 - Condition **AND(EMPTY($StartDate),EMPTY($EndDate))** (the chevron will be gray if the stage has not started).

These conditions set the order of coloring individual chevron windows, that is, for each stage, a check for these conditions will be carried out, the chevron element will change color in accordance with the dates filled in.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
