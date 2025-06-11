---
title: Развилка «и»
kbId: 4749
tags:
  - диаграммы
  - диаграмма процесса
  - диаграмма бизнес-процесса
  - шаблон процесса
  - процесс
  - бизнес-процесс
  - диаграмма
  - развилка «и»
  - развилка
  - параллельная развилка
hide:
  - tags
---
# Развилка «и» {: #process_diagram_elements_gateway_parallel}

<div class="admonition question" markdown="block">
## Определения {: .admonition-title #definitions}

**Развилка «и»** используется двумя способами:

* **Расходящаяся развилка «и»** — у развилки имеется несколько исходящих потоков. При входе в расходящуюся развилку «и» токена из неё выходит одновременно несколько токенов по всем исходящим [потокам][process_diagram_elements_sequence_flow].
* **Сходящаяся развилка «и»** — у развилки имеется один исходящий поток. Сходящаяся развилка «и» ожидает входа токенов по всем входящим потокам, после чего из развилки выходит один токен по исходящему [потоку][process_diagram_elements_sequence_flow].

</div>

!!! Note "Примечание"
    Количество входящих и исходящих потоков у развилки «и» может быть любым. Но _не рекомендуется одновременно использовать несколько входящих и исходящих потоков_. Рекомендуется соединять развилку либо с одним входящим потоком, либо с одним исходящим.

*![Развилка «и» и её меню элемента](parallel_gateway.png)*

*![Пример использования развилок «и»](parallel_gateway_example.png)*

## Операции в меню элемента «Развилка «и» {: .pageBreakBefore }

- **Действия**
    - **Свойства** <i class="fa-light fa-gear"></i> — переход к окну [свойств развилки «и»](#свойства-развилки-и).
    --8<-- "process_diagram_exit_scenario.md"
    --8<-- "process_diagram_delete_element.md"
- **Изменить тип** — смена типа развилки.
--8<-- "process_diagram_quick_create.md"

## Свойства развилки «и»

В окне свойств **развилки «и»** можно настроить только [общие свойства элемента диаграммы процесса][process_diagram_element_common_properties].

*![Свойства развилки «и»](parallel_gateway_general_properties.png)*

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Развилка «или/или»][process_diagram_elements_gateway_exclusive]_
- _[Общие свойства элементов диаграммы процесса][process_diagram_element_common_properties]_
- _[Элементы диаграммы процесса][process_diagram_elements]_
- _[Редактирование диаграммы процесса][process_diagram_designer]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
