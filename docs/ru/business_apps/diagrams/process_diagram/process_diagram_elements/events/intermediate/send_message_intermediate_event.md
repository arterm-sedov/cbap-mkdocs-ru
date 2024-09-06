---
title: Промежуточное событие-отправка сообщения
tags:
  - диаграмма процесса
  - элементы диаграммы процесса
  - события
  - диаграмма бизнес-процесса
  - шаблон процесса
  - процесс
  - бизнес-процесс
  - промежуточное событие-отправка сообщения
  - путь передачи данных
hide:
  - tags
kbId: 2381
---

# Промежуточное событие-отправка сообщения {: #send_message_intermediate_event}

<div class="admonition question" markdown="block">
## Определения {: .admonition-title #definitions}

**Промежуточное событие-отправка сообщения** служит для отправки внутрипроцессных, межпроцессных и внешних сообщений. При входе токена в этот элемент отправляется настроенное сообщение. Токен не останавливается на этом элементе и переходит на следующий.

</div>

*![Промежуточное событие-отправка сообщения и его меню элемента](send_message_intermediate_event.png)*

## Операции в меню элемента «Промежуточное событие-отправка сообщения»

- **Действия** :
    - **Свойства** <i class="fa-light fa-gear"></i> — переход к окну [свойств промежуточного события-отправки сообщения](#свойства-промежуточного-события-отправки-сообщения).
    --8<-- "process_diagram_exit_scenario.md"
    --8<-- "process_diagram_delete_element.md"
- **Изменить тип** — смена типа события.
--8<-- "process_diagram_quick_create.md"

## Свойства промежуточного события-отправки сообщения

В окне свойств **промежуточного события-отправки сообщения** предусмотрены перечисленные ниже вкладки.

### Основные

На этой вкладке можно настроить [общие свойства элемента диаграммы процесса][process_diagram_element_common_properties].

*![Основные свойства промежуточного события-отправки сообщения](send_message_intermediate_event_general_properties.png)*

### Дополнительные

На этой вкладке можно настроить специфические свойства **промежуточного события-отправки сообщения**.

- **Место назначения** — укажите, куда будет отправлено сообщение.

    - **Промежуточное событие** — укажите **имя сообщения** (такое же как в [промежуточном событии-получении сообщения](receive_message_intermediate_event.md)) и ID **экземпляра процесса**, который получит сообщение (задайте фиксированное **значение** ID, либо **формулу** или скрипт **C#**, возвращающие ID экземпляра процесса).

    --8<-- "process_message_event_name.md"

    *![Настройка целевого промежуточного события и экземпляра процесса для промежуточного события-отправки сообщения](send_message_intermediate_event_process_instance.png)*

    - **Начальное событие** — укажите **имя сообщения** (такое же как в [начальном событии-получении сообщения](receive_message_start_event.md)) и выберите процесс, который будет запущен отправленным сообщением.

    *![Настройка целевого начального события и процесса для промежуточного события-отправки сообщения](send_message_intermediate_event_process.png)*

  - **Внешний сокет** — выберите или создайте **[путь передачи данных](communication_routes.md)** типа «**Отправка эл. почты из процесса**» для отправки сообщения.
  - **Общие уведомления** — выберите или создайте **[путь передачи данных](communication_routes.md)** типа «**Общие уведомления**» для отправки сообщения.

    *![Настройка целевого пути передачи данных для промежуточного события-отправки сообщения](send_message_intermediate_event_communication_route.png)*

### Данные сообщения

На этой вкладке можно настроить передачу данных из процесса в сообщение.

- **Атрибуты для передачи данных сообщения** — в этой таблице следует настроить соответствие между атрибутами отправляемого сообщения и атрибутами шаблона записи, связанного с шаблоном процесса. Если на вкладке «**Дополнительные**» выбрано место назначения «**Внешний сокет**» или «**Общее уведомление**» и указан путь передачи данных, эта таблица автоматически заполняется строками с вкладки «**Атрибуты сообщения**» пути передачи данных. Для остальных мест назначения таблицу следует заполнить вручную.
    - **Создать** — эта кнопка позволяет создать строку для сопоставления атрибутов сообщения и шаблона записи.
    - **Удалить** — эта кнопка позволяет удалить строки таблицы, выбранные с помощью флажков в первом столбце.
    - **Название** — задайте наглядное наименование атрибута сообщения. **Обязательное поле**.
    - **Системное имя** — задайте уникальное имя атрибута сообщения.
    --8<-- "system_name_requrements.md"
    - **Тип данных** — укажите тип данных атрибута сообщения. **Обязательное поле**.
    - **Значение** — задайте значение атрибута сообщения, соблюдая соответствие типов данных:
        - **Атрибут** — присвойте атрибуту сообщения значение атрибута шаблона записи, связанного с шаблоном процесса.
        - **Формула** — введите формулу, возвращающую значение атрибута сообщения.
        - **C#** — введите скрипт, возвращающий значение атрибута сообщения.

    *![Настройка данных сообщения для промежуточного события-отправки сообщения](send_message_intermediate_event_message_data.png)*

--8<-- "related_topics_heading.md"

**[События][события]**

**[Типы промежуточных событий][типы-промежуточных-событий]**

**[Пути передачи данных](communication_routes.md)**

**[Общие свойства элементов диаграммы процесса][process_diagram_element_common_properties]**

**[Элементы диаграммы процесса][process_diagram_elements]**

**[Редактирование диаграммы процесса][process_diagram_designer]**