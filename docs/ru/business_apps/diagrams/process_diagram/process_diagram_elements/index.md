---
title: Элементы диаграммы процесса
kbTitle: Типы элементов диаграммы процесса
kbId: 4724
tags:
  - диаграммы
  - диаграмма процесса
  - элементы диаграммы процесса
  - действия
  - события
  - развилки
  - дорожка
  - пул
  - комментарий
  - потоки управления
  - диаграмма бизнес-процесса
  - шаблон процесса
  - процесс
  - бизнес-процесс
  - диаграмма
hide:
  - tags
---

# Элементы диаграммы процесса {: #process_diagram_elements}

## Типы элементов

Для построения диаграммы процесса предусмотрены следующие элементы:

* [Действия][process_diagram_elements_actions]
    * [Пользовательская задача][process_diagram_elements_user_task]
    * [Задача-выполнение сценария][process_diagram_elements_script_task]
    * [Вызов процесса][process_diagram_elements_process_call]
    * [Встроенный подпроцесс][process_diagram_elements_embedded_subprocess]
* [События][process_diagram_elements_events]
    * [Начальные события][process_diagram_elements_events_start]
        * [Простое начальное событие][process_diagram_elements_none_start_event]
        * [Начальное событие-таймер][process_diagram_elements_timer_start_event]
        * [Начальное событие-получение сообщения][process_diagram_elements_receive_message_start_event]
    * [Промежуточные события][process_diagram_elements_events_intermediate]
        * [Промежуточное событие-таймер][process_diagram_elements_timer_intermediate_event]
        * [Промежуточное событие-отправка сообщения][process_diagram_elements_send_message_intermediate_event]
        * [Промежуточное событие-получение сообщения][process_diagram_elements_receive_message_intermediate_event]
        * [Простое событие][process_diagram_elements_none_intermediate_event]
    * [Конечные события][process_diagram_elements_events_end]
        * [Простое конечное событие][process_diagram_elements_none_end_event]
        * [Конечное событие-остановка процесса][process_diagram_elements_stop_process_end_event]
        * [Конечное событие-отправка сообщения][process_diagram_elements_send_message_end_event]
* [Развилки][process_diagram_elements_gateways]
    * [Развилка «или/или»][process_diagram_elements_gateway_exclusive]
    * [Развилка «и»][process_diagram_elements_gateway_parallel]
* [Общие элементы][process_diagram_elements_generic]
    * [process_diagram_elements_pool][process_diagram_elements_pool]
    * [Дорожка][process_diagram_elements_lane]
    * [Поток управления][process_diagram_elements_sequence_flow]
    * [Комментарий][process_diagram_elements_text_annotation]

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Общие свойства элементов диаграммы процесса][process_diagram_element_common_properties]_
- _[Диаграмма процесса][process_diagram]_
- _[Просмотр диаграммы процесса][process_diagram_view]_
- _[Редактирование диаграммы процесса][process_diagram_designer]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
