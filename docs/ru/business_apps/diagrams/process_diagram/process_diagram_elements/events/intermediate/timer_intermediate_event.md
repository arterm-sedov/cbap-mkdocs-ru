---
title: Промежуточное событие-таймер
kbId: 4738
tags:
  - диаграмма процесса
  - элементы диаграммы процесса
  - события
  - диаграмма бизнес-процесса
  - шаблон процесса
  - процесс
  - бизнес-процесс
  - промежуточное событие-таймер
hide:
  - tags
---

# Промежуточное событие-таймер {: #process_diagram_elements_timer_intermediate_event}

<div class="admonition question" markdown="block">
## Определения {: .admonition-title #definitions}

**Промежуточное событие-таймер** служит для управления ходом процесса. Токен останавливается на этом элементе и переходит на следующий элемент по истечении заданного времени таймера.

*![Промежуточное событие-таймер и его меню элемента](timer_intermediate_event.png)*

</div>

## Операции в меню элемента «Промежуточное событие-таймер»

- **Действия** :
    - **Свойства** <i class="fa-light fa-gear"></i> — переход к окну [свойств промежуточного события-таймера](#свойства-промежуточного-события-таймера).
    --8<-- "process_diagram_exit_scenario.md"
    --8<-- "process_diagram_delete_element.md"
- **Изменить тип** — смена типа события.
--8<-- "process_diagram_quick_create.md"

## Свойства промежуточного события-таймера {: .pageBreakBefore }

В окне свойств **промежуточного события-таймера** предусмотрены перечисленные ниже вкладки.

### Основные

На этой вкладке можно настроить [общие свойства элемента диаграммы процесса][process_diagram_element_common_properties].

*![Основные свойства промежуточного события-таймера](timer_intermediate_event_general_properties.png)*

### Дополнительные

На этой вкладке можно настроить специфические свойства **промежуточного события-таймера**.

- **Прерывающее** — этот флажок отображается, если **промежуточное событие-таймер** [прикреплено к действию][process_diagram_elements_events_intermediate_usage]. Если флажок установлен, то при наступлении данного события прикреплённое к нему [действие][process_diagram_elements_actions] будет прервано.
- **Интервал таймера** — задайте интервал, по истечении которого токен с данного события должен переходить на следующий элемент. На событии, [прикрепленном к действию][process_diagram_elements_events_intermediate_usage], при срабатывании таймера будет создан новый токен.
    --8<-- "duration_value_formula_or_script.md"

*![Дополнительные свойства промежуточного события-таймера](timer_intermediate_event_advanced_properties.png)*

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[События][process_diagram_elements_events]_
- _[Типы промежуточных событий][process_diagram_elements_events_intermediate]_
- _[Общие свойства элементов диаграммы процесса][process_diagram_element_common_properties]_
- _[Элементы диаграммы процесса][process_diagram_elements]_
- _[Редактирование диаграммы процесса][process_diagram_designer]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}