---
title: 'Редактирование диаграммы ОШС'
kbId: 4848
tags:
    - процессная архитектура
    - конструктор организационных единиц
    - конструктор оргструктуры
    - конструктор диаграммы оргструктуры
    - конструктор ОШС
    - операции в конструкторе оргструктуры
hide:
    - tags
---

# Просмотр и редактирование диаграммы ОШС {: #architect_organizational_structure_diagram_edit }

## Введение

В **{{ productNameEnterprise }}** для моделирования организационно-штатной структуры (ОШС) предприятия предусмотрен визуальный конструктор диаграммы ОШС.

!!! warning "Внимание!"

    Изменения, внесённые в диаграмму ОШС, сохраняются автоматически.

## Переход к диаграмме ОШС {: #architect_organizational_structure_diagram_designer }

1. Откройте реестр оргединиц, выбрав пункт «**Оргструктура**» — «**Реестр**» в панели навигации выберите.
2. Выберите оргединицу в панели навигации или дважды нажмите её в реестре.
3. Откроется диаграмма ОШС выбранной оргединицы в режиме просмотра.
4. При необходимости перейдите к любой из оргединиц на диаграмме, нажав значок <i class="fa-solid fa-user"></i> или <i class="fa-solid fa-sitemap"></i>.
5. Нажмите кнопку «**Редактировать**» <i class="fa-light fa-pen-nib" aria-hidden="true"></i>.
6. Отобразится конструктор диаграммы ОШС для выбранной оргединицы.
7. [Отредактируйте оргструктуру][architect_organizational_structure_design].

_![Переход к конструктору диаграммы ОШС](img/organizationa_structure_modeling_edit_diagram.png)_

## Элементы конструктора диаграммы ОШС

_![Конструктор диаграммы ОШС](img/organizational_structure_modeling_designer.png)_

1. **Кнопки типовых операций**:

    - **Просмотр** <i class="fa-light fa-eye"></i> — переход в режим просмотра диаграммы.
    - **Очистить** <i class="fa-light fa-trash"></i> — безвозвратное удаление всех элементов организационной единицы. При нажатии этой кнопки отобразится запрос подтверждения.
    - **Обсуждение** <i class="fa-light fa-comment-dots"></i> — отображение чата для обсуждения организационной единицы.
    - **Свойства** <i class="fa-light fa-sidebar-flip"></i> — [настройка свойств][architect_organizational_structure_design_unit_configure] выбранного элемента или всей организационной единицы.

    Cм. также _«[Настройка кнопок типовых операций](#настройка-кнопок-типовых-операций)»_.

2. **Кнопки работы с диаграммой**:

    - **Указатель** <i class="fa-light fa-arrow-pointer"></i>  — режим выбора одного элемента.
    - **Лассо** <i class="fa-light fa-square-dashed"></i>  — режим захвата нескольких элементов.
    - **Отменить** <i class="fa-light fa-arrow-rotate-left"></i>  — отмена последнего действия.
    - **Повторить** <i class="fa-light fa-arrow-rotate-right"></i>  — повтор последнего отменённого действия.

3. **Палитра элементов** — содержит элементы в нотации организационно-штатной структуры, которые можно перетащить на диаграмму.
--8<-- "process_architecture_diagram_zoom_controls.md"
6. **Панель свойств** — здесь отображаются свойства выбранного элемента, а также панель обсуждения.

## Управление с помощью клавиатуры { .pageBreakBefore }

В конструкторе оргструктуры можно использовать следующие сочетания клавиш:

--8<-- "enterprise_architecture_keyboard_shortcuts.md"

{% include-markdown ".snippets/enterprise_architecture_chrome_clipboard_admonition.md" %}

## Меню элемента {: #architect_organizational_structure_diagram_edit_element_menu }

При выборе оргединицы на диаграмме отображается контекстное меню с перечисленными ниже пунктами.

_![Меню элемента для оргединицы](img/organizational_structure_modeling_designer_element_menu.png)_

- **Быстрое создание** — создание оргединицы, связанной с выбранной оргединицей. Можно создать **должность** или **подразделение**.
- **Изменить цвет** — выбор цвета рамки и фона оргединицы.
- **Удалить** — удаление выбранной оргединицы.

## Настройка кнопок типовых операций { .pageBreakBefore }

Кнопки типовых операций для конструктора диаграммы ОШС можно настроить следующим образом:

1. Откройте список шаблонов.
2. Откройте требуемый **шаблон организационной единицы**.
3. Откройте вкладку «**Область кнопок**».
4. Откройте **область кнопок для диаграммы моделей**.
5. Поместите на область кнопки, которые должны отображаться в конструкторе оргструктуры.
6. При необходимости создайте новые кнопки, нажав значок <i class="fa-light fa-plus"></i> рядом с заголовком «**Кнопки**» в панели элементов слева.
7. Удалите ненужные кнопки.
8. Сохраните область кнопок.

_![Настройка кнопок типовых операций для диаграммы ОШС](img/architect_process_organizational_structure_designer_button_area.png)_

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Редактирование оргструктуры][architect_organizational_structure_design]_
- _[Области кнопок. Определение, настройка, клонирование, удаление][button_area]_
- _[Кнопки. Определение, настройка, удаление][buttons]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
