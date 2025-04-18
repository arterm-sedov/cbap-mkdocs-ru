---
kbId: 4737
tags:
  - диаграмма процесса
  - элементы диаграммы процесса
  - события
  - диаграмма бизнес-процесса
  - шаблон процесса
  - процесс
  - бизнес-процесс
  - начальное событие-таймер
hide:
  - tags
---

# Начальное событие-таймер {: #process_diagram_elements_timer_start_event }

<div class="admonition question" markdown="block">
## Определения {: .admonition-title #definitions}

**Начальное событие-таймер периодически** запускает процесс при наступлении заданного времени по расписанию.

</div>

*![Начальное событие-таймер и его меню элемента](timer_start_event.png)*

## Операции в меню элемента «Начальное событие-таймер»

- **Действия**
    - **Свойства** <i class="fa-light fa-gear"></i> — переход к окну [свойств начального события-таймера](#свойства-начального-события-таймера).
    --8<-- "process_diagram_exit_scenario.md"
    --8<-- "process_diagram_delete_element.md"
- **Изменить тип** — смена типа события.
--8<-- "process_diagram_quick_create.md"

## Свойства начального события-таймера {: .pageBreakBefore }

В окне свойств **начального события-таймера** предусмотрены перечисленные ниже вкладки.

### Основные

На этой вкладке можно настроить [общие свойства элемента диаграммы процесса][process_diagram_element_common_properties].

*![Основные свойства начального события-таймера](timer_start_event_general_properties.png)*

### Дополнительные

На этой вкладке можно настроить специфические свойства **начального события-таймера**.

- **Тип таймера** — выберите интервал срабатывания таймера. Для типа таймера задаются отдельные параметры расписания запуска процесса.
    - **По минутам** — процесс будет запускаться ежедневно в заданное **начальное время**, а затем регулярно с указанным интервалом до **конечного времени**. Например, ежедневно с 06:15 включительно до 20:00 каждые 2 часа 15 минут.
        - **Начальное время** — укажите время ежедневного запуска таймера. В это время будет ежедневно происходить первый запуск процесса, последующие запуски будут происходить с указанным **интервалом**.
        - **Конечное время** — укажите время ежедневной остановки таймера.
        - **Интервал** — укажите временной интервал запуска процесса. Интервал отсчитывается от начального времени.
        !!! Note "Примечание"
            Если опубликовать диаграмму **_после_** начального времени, **интервал** будет отсчитываться **_с момента публикации диаграммы_** до конечного времени.

    *![Параметры таймера по минутам](timer_start_event_minutes.png)*

    - **По дням** — процесс будет запускаться в заданное время: либо с указанным дневным интервалом, либо каждый рабочий день. Например: в 9:00 раз в три дня.
        - **Время запуска процесса** — укажите время суток для запуска процесса.
        - **С интервалом** — выберите этот режим, чтобы запускать процесс с указанным интервалом в днях.
        - **По рабочим дням** — выберите этот режим, чтобы запускать процесс каждый рабочий день. Этот режим **выбран по умолчанию**.

    *![Параметры таймера по дням](timer_start_event_days.png)*

    - **По неделям** — процесс будет запускаться в заданное время с указанным недельным интервалом в выбранные дни недели. Например: в 15:00 каждую неделю по понедельникам, средам и пятницам.
        - **Время запуска процесса** — укажите время суток для запуска процесса.
        - **Интервал в неделях** — укажите интервал и дни недели, по которым будет запускаться процесс.

    *![Параметры таймера по неделям](timer_start_event_weeks.png)*

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

    - **По месяцам** — процесс будет запускаться в заданное время с указанным месячным интервалом: либо в определённое число месяца, либо в определённый день недели. Например: в 19:00 второй пятницы каждого второго месяца.
        - **По определённым числам** — выберите этот режим, чтобы запускать процесс в указанное число месяца с заданным интервалом в месяцах.
        - **В определённый день недели** — выберите этот режим, чтобы запускать процесс в указанный день недели с заданным интервалом в месяцах. Этот режим **выбран по умолчанию**.

    *![Параметры таймера по месяцам](timer_start_event_months.png)*

    - **По годам** — процесс будет запускаться в заданное время раз в год: либо в указанный день, либо в каждый указанный день недели выбранного месяца. Например: ежегодно, в 00:00 последней пятницы марта.
        - **В определённый день** — выберите этот режим, чтобы запускать процесс в указанное число выбранного месяца.
        - **В определённый день недели указанного месяца** — выберите этот режим, чтобы запускать процесс в указанный день недели выбранного месяца. Этот режим **выбран по умолчанию**.

    *![Параметры таймера по годам](timer_start_event_years.png)*

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[События][process_diagram_elements_events]_
- _[Типы начальных событий][типы-начальных-событий]_
- _[Общие свойства элементов диаграммы процесса][process_diagram_element_common_properties]_
- _[Элементы диаграммы процесса][process_diagram_elements]_
- _[Редактирование диаграммы процесса][process_diagram_designer]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
