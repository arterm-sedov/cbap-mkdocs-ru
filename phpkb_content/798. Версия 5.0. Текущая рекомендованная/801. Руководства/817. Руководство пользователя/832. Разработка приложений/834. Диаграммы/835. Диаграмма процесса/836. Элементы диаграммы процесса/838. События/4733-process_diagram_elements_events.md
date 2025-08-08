---
title: События. Определение и типы
kbId: 4733
---

# События. Определение и типы

## Определения

**Событие** задаёт ожидаемое действие. События классифицируются по положению на диаграмме процесса: начальное, промежуточное, конечное.

## Типы событий

- [Начальные события][process_diagram_elements_events_start]
  - **[Простое начальное событие][process_diagram_elements_none_start_event]**
  - **[Начальное событие-таймер][process_diagram_elements_timer_start_event]**
  - **[Начальное событие-получение сообщения][process_diagram_elements_receive_message_start_event]**
- [Промежуточные события][process_diagram_elements_events_intermediate]
  - **[Промежуточное событие-таймер][process_diagram_elements_timer_intermediate_event]**
  - **[Промежуточное событие-отправка сообщения][process_diagram_elements_send_message_intermediate_event]**
  - **[Промежуточное событие-получение сообщения][process_diagram_elements_receive_message_intermediate_event]**
  - **[Простое событие][process_diagram_elements_none_intermediate_event]**
- [Конечные события][process_diagram_elements_events_end]
  - **[Простое конечное событие][process_diagram_elements_none_end_event]**
  - **[Конечное событие-остановка процесса][process_diagram_elements_stop_process_end_event]**
  - **[Конечное событие-отправка сообщения][process_diagram_elements_send_message_end_event]**

--8<-- "related_topics_heading.md"

- *[Элементы диаграммы процесса][process_diagram_elements]*
- *[Редактирование диаграммы процесса][process_diagram]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
