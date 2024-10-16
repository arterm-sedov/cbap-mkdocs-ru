---
title: Общие свойства элементов диаграммы процесса
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
kbId: 2364
---

# Общие свойства элементов диаграммы процесса {: #process_diagram_element_common_properties}

У всех элементов диаграммы процесса предусмотрены перечисленные ниже свойства.

- **Название** — наглядное наименование элемента.
- **Системное имя** — уникальное имя элемента. **Обязательное поле**. Может содержать только буквы латинского алфавита (a-z A-Z), цифры (0—9) и знак «_», не должно начинаться с цифры. Заполняется автоматически с помощью транслитерации названия.
- **Состояние элемента диаграммы** — отображается в [окне свойств элемента][element_properties_setting].
    - **Активен** — элемент выполняется, когда на него приходит токен.
    - **Приостановлен** — токен останавливается на элементе и не идет на последующие элементы.
    - **Пропуск** — токен проходит через элемент без выполнения элемента.
- **Описание** — необязательный комментарий относительно назначения элемента.

Общие свойства элемента (кроме статуса активности) отображаются в панели свойств элемента при его выборе в [конструкторе диаграммы процесса][process_diagram_designer], а также в [окне свойств элемента][element_properties_setting].

_![Свойства выбранного элемента в панели свойств элемента](process_diagram_element_common_properties_in_properties_panel.png)_

## Настройка свойств элемента {: #element_properties_setting}

1. Нажмите элемент диаграммы.
2. Нажмите кнопку «**Свойства**» <i class="fa-light fa-gear"></i> в [меню элемента][process_diagram_call_element_menu].

    _![Кнопка «Свойства» в меню элемента](process_diagram_element_common_properties_congigure_button.png)_

3. Отобразится окно свойств элемента
  
    _![Общие свойства элемента диаграммы в окне его свойств](process_diagram_element_common_properties.png)_

--8<-- "related_topics_heading.md"

**[Элементы диаграммы процесса][process_diagram_elements]**

**[Диаграмма процесса][process_diagram]**

**[Конструктор диаграммы процесса][process_diagram_designer]**
