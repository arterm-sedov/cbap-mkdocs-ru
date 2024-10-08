---
tags:
  - диаграммы
  - диаграмма процесса
  - диаграмма бизнес-процесса
  - шаблон процесса
  - процесс
  - бизнес-процесс
  - диаграмма
hide:
  - tags
---

# Поток управления

**Поток управления** — соединяет два последовательных элемента процесса. Предусмотрено два типа потоков:

- **Поток управления** — обычный поток управления, соединяющий любые два элемента. Если поток выходит из **[развилки «или/или»](exclusive_gateway.md)**, то для него можно [задать условие](#дополнительные), при выполнении которого по нему пойдёт токен.
- **Поток управления «иначе»** — если поток выходит из **[развилки «или/или»](exclusive_gateway.md)**, то его можно назначить [потоком «иначе»](#дополнительные). Токен идёт по потоку «иначе», если не выполнены условия ни для одного другого потока, выходящего из развилки.

*![Потоки управления и их меню элемента](sequence_flow.png)*

## Изменение формы потока управления

1. Наведите указатель мыши на границу потока.
2. Отобразится курсор перетаскивания <i class="fa-light fa-up-down"></i>.
3. Перетащите линию потока в необходимое положение.

## Подсоединение потока управления к элементу

1. Наведите указатель мыши на начало или конец потока.
2. На потоке отобразится круглый манипулятор.
3. Начните перетаскивать манипулятор потока.
4. На всех элементах диаграммы отобразятся доступные точки соединения.
5. Перетащите манипулятор потока на точку соединения с другим элементом

{% if pdfOutput %}
*![Подсоединение потока управления к элементу](sequence_flow_connecting.png)*
{% else %}
*![Подсоединение потока управления к элементу](sequence_flow_connecting.gif)*
{% endif %}

## Операции в меню элемента «Поток управления»

- **Действия**
    - **Свойства** <i class="fa-light fa-gear"></i> — переход к окну [свойств потока управления](#свойства-потока-управления).
    --8<-- "process_diagram_delete_element.md"
- **Изменить тип** — смена типа потока.

## Свойства потока управления

В  окне свойств **потока** предусмотрены перечисленные ниже вкладки.

### Основные

На этой вкладке можно настроить [общие свойства элемента диаграммы процесса][process_diagram_element_common_properties].

*![Основные свойства потока управления](sequence_flow_general_properties.png)*

### Дополнительные

На этой вкладке можно настроить специфические свойства **потока управления**, соединённого с **[развилкой «или/или»](exclusive_gateway.md)**. Она не отображается для потоков, соединённых с другими элементами.

- **Поток «иначе»** — если установлен этот флажок, то токен идёт по потоку, если не выполнены **условия** ни для одного другого потока, выходящего из развилки. Этот флажок можно установить только для одного потока, выходящего из развилки.
- **Условие** — введите **формулу** или скрипт **C#**, возвращающие `true`, когда токен должен идти по данному потоку. Это поле отображается, если снят флажок «**Поток «иначе»**. Это **обязательное поле** — условие необходимо указать для всех потоков, выходящих из **[развилки «или/или»](exclusive_gateway.md)** кроме **потока «иначе»**.

*![Дополнительные свойства потока управления](sequence_flow_advanced_properties.png)*

--8<-- "related_topics_heading.md"

**[Развилки][развилки]**

**[Общие свойства элементов диаграммы процесса][process_diagram_element_common_properties]**

**[Элементы диаграммы процесса][process_diagram_elements]**

**[Редактирование диаграммы процесса][process_diagram_designer]**
