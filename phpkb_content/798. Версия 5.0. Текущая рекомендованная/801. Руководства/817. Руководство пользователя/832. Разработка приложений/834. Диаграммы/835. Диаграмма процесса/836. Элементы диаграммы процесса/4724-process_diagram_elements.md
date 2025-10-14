---
title: 'Типы элементов диаграммы процесса'
kbId: 4724
url: 'https://kb.comindware.ru/article.php?id=4724'
---

# Типы элементов диаграммы процесса

## Типы элементов

Для построения диаграммы процесса предусмотрены следующие элементы:

- [Действия][process_diagram_elements_actions]
  - [Пользовательская задача][process_diagram_elements_user_task]
  - [Задача-выполнение сценария][process_diagram_elements_script_task]
  - [Вызов процесса][process_diagram_elements_process_call]
  - [Встроенный подпроцесс][process_diagram_elements_embedded_subprocess]
- [События][process_diagram_elements_events]
  - [Начальные события][process_diagram_elements_events_start]
    - [Простое начальное событие][process_diagram_elements_none_start_event]
    - [Начальное событие-таймер][process_diagram_elements_timer_start_event]
    - [Начальное событие-получение сообщения][process_diagram_elements_receive_message_start_event]
  - [Промежуточные события][process_diagram_elements_events_intermediate]
    - [Промежуточное событие-таймер][process_diagram_elements_timer_intermediate_event]
    - [Промежуточное событие-отправка сообщения][process_diagram_elements_send_message_intermediate_event]
    - [Промежуточное событие-получение сообщения][process_diagram_elements_receive_message_intermediate_event]
    - [Простое событие][process_diagram_elements_none_intermediate_event]
  - [Конечные события][process_diagram_elements_events_end]
    - [Простое конечное событие][process_diagram_elements_none_end_event]
    - [Конечное событие-остановка процесса][process_diagram_elements_stop_process_end_event]
    - [Конечное событие-отправка сообщения][process_diagram_elements_send_message_end_event]
- [Развилки][process_diagram_elements_gateways]
  - [Развилка «или/или»][process_diagram_elements_gateway_exclusive]
  - [Развилка «и»][process_diagram_elements_gateway_parallel]
- [Общие элементы][process_diagram_elements_generic]
  - [Пул][process_diagram_elements_pool]
  - [Дорожка][process_diagram_elements_lane]
  - [Поток управления][process_diagram_elements_sequence_flow]
  - [Комментарий][process_diagram_elements_text_annotation]

--8<-- "related_topics_heading.md"

- *[Общие свойства элементов диаграммы процесса][process_diagram_element_common_properties]*
- *[Диаграмма процесса][process_diagram]*
- *[Просмотр диаграммы процесса][process_diagram]*
- *[Редактирование диаграммы процесса][process_diagram]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
