---
kbId: 4735
title: Начальные события
tags:
  - диаграмма процесса
  - элементы диаграммы процесса
  - события
  - диаграмма бизнес-процесса
  - шаблон процесса
  - процесс
  - бизнес-процесс
  - начальное событие
hide:
  - tags
---

# Начальные события {: #process_diagram_elements_events_start}

<div class="admonition question" markdown="block">
## Определения {: .admonition-title #definitions}

**Начальное событие** создаёт и запускает экземпляр процесса. При этом создаётся токен, который переходит на следующий элемент диаграммы процесса. На диаграмме должно быть хотя бы одно начальное событие.

</div>

## Типы начальных событий

- **[Простое начальное событие][process_diagram_elements_none_start_event]**
- **[Начальное событие-таймер][process_diagram_elements_timer_start_event]**
- **[Начальное событие-получение сообщения][process_diagram_elements_receive_message_start_event]**

## Создание начального события на диаграмме

1. Перетащите начальное событие с панели элементов на поток управления или пустое место диаграммы.
2. Будет создано **простое начальное событие**.
3. При необходимости смените [тип события](#типы-начальных-событий) с помощью [меню элемента][process_diagram_call_element_menu].

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[События][process_diagram_elements_events]_
- _[Элементы диаграммы процесса][process_diagram_elements]_
- _[Редактирование диаграммы процесса][process_diagram_designer]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
