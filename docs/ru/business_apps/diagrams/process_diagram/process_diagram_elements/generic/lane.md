---
title: Дорожка
kbId: 4751
tags:
  - диаграммы
  - диаграмма процесса
  - диаграмма бизнес-процесса
  - шаблон процесса
  - процесс
  - бизнес-процесс
  - диаграмма
  - дорожка
  - элементы диаграммы процесса
  - исполнители
  - пользовательская задача
hide:
  - tags
---

# Дорожка {: #process_diagram_elements_lane}

<div class="admonition question" markdown="block">
## Определения {: .admonition-title #definitions}

**Дорожка** — используется для упорядочивания элементов внутри пула в соответствии с бизнес-функциями и ролями их исполнителей.

</div>

*![Дорожка и её меню элемента](lane.png)*

## Операции в меню элемента «Дорожка»

- **Действия**
    - **Свойства** <i class="fa-light fa-gear"></i> — переход к окну [свойств дорожки](#свойства-дорожки).
    --8<-- "process_diagram_delete_element.md"

## Свойства дорожки

В окне свойств **дорожки** можно настроить [общие свойства элемента диаграммы процесса][process_diagram_element_common_properties], а также указать **исполнителей**.

**Исполнители** — выберите в этом поле **[роль][roles]**, которая будет автоматически назначаться **[пользовательским задачам][process_diagram_elements_user_task]**, создаваемым на данной дорожке. Название назначенной роли будет отображаться на диаграмме рядом с названием дорожки.

*![Свойства дорожки](lane_general_properties.png)*

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Общие свойства элементов диаграммы процесса][process_diagram_element_common_properties]_
- _[Элементы диаграммы процесса][process_diagram_elements]_
- _[Редактирование диаграммы процесса][process_diagram_designer]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
