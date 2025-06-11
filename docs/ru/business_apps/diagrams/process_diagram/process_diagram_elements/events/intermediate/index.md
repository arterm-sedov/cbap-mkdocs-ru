---
title: Промежуточные события
kbId: 4742
tags:
  - диаграмма процесса
  - элементы диаграммы процесса
  - события
  - диаграмма бизнес-процесса
  - шаблон процесса
  - процесс
  - бизнес-процесс
  - промежуточное событие
hide:
  - tags
---

# Промежуточные события {: #process_diagram_elements_events_intermediate}

<div class="admonition question" markdown="block">
## Определения {: .admonition-title #definitions}

**Промежуточные события** служат для управления ходом процесса и контроля его выполнения в срок, а также для обмена данными между процессами, элементами процесса и с внешними системами.

</div>

## Типы промежуточных событий

- **[Промежуточное событие-таймер][process_diagram_elements_timer_intermediate_event]**
- **[Промежуточное событие-отправка сообщения][process_diagram_elements_send_message_intermediate_event]**
- **[Промежуточное событие-получение сообщения][process_diagram_elements_receive_message_intermediate_event]**
- **[Простое промежуточное событие][process_diagram_elements_none_intermediate_event]**

## Способы использования промежуточного события {: #process_diagram_elements_events_intermediate_usage }

1. Любое промежуточное событие можно соединить с потоком управления. В этом случае токен остановится на промежуточном событии до его наступления, а после наступления события перейдёт на следующий элемент.
2. **[Промежуточное событие-таймер][process_diagram_elements_timer_intermediate_event]** и **[промежуточное событие-получение сообщения][process_diagram_elements_receive_message_intermediate_event]** можно присоединить к [действию][process_diagram_elements_actions]. В этом случае при наступлении данного события на нём будет создан новый токен, который перейдёт на элемент, соединённый с событием.

*![Варианты расположения промежуточного события](intermediate_event_pacement_types.png)*

## Создание промежуточного события на диаграмме

1. Перетащите промежуточное событие с панели элементов на поток управления, границу [действия][process_diagram_elements_actions] или пустое место диаграммы.
2. Будет создано **[промежуточное событие-таймер][process_diagram_elements_timer_intermediate_event]**.
3. При необходимости смените [тип события](#process_diagram_elements_events_intermediate) с помощью [меню элемента][process_diagram_call_element_menu].

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[События][process_diagram_elements_events]_
- _[Элементы диаграммы процесса][process_diagram_elements]_
- _[Редактирование диаграммы процесса][process_diagram_designer]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
