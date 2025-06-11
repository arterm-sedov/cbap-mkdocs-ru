---
title: Встроенный подпроцесс
kbId: 4731
tags:
  - диаграммы
  - диаграмма процесса
  - элементы диаграммы процесса
  - действия
  - диаграмма бизнес-процесса
  - шаблон процесса
  - процесс
  - бизнес-процесс
  - встроенный подпроцесс
  - диаграмма
hide:
  - tags
---

# Встроенный подпроцесс {: #process_diagram_elements_embedded_subprocess}

<div class="admonition question" markdown="block">
## Определения {: .admonition-title #definitions}

**Встроенный подпроцесс** представляет собой последовательность действий, выделенную в отдельный процесс внутри текущего процесса. Встроенный подпроцесс позволяет  упростить и структурировать основную диаграмму процесса.

В отличие от **[вызова процесса][process_diagram_elements_process_call]**, встроенный подпроцесс является частью основного процесса и оперирует тем же набором данных.

По завершении выполнения подпроцесса токен переходит на следующий элемент диаграммы текущего процесса.

</div>

*![Встроенный подпроцесс на диаграмме бизнес-процесса](embedded_subprocess.png)*

## Операции в меню элемента «Встроенный подпроцесс»

- **Действия**
    - **Свойства** <i class="fa-light fa-gear"></i> — переход к окну [свойств встроенного подпроцесса](#свойства-встроенного-подпроцесса).
    --8<-- "process_diagram_entry_scenario.md"
    --8<-- "process_diagram_delete_element.md"
    --8<-- "process_diagram_subprocess_diagram.md"
--8<-- "process_diagram_quick_create.md"

## Свойства встроенного подпроцесса

В  окне свойств **вызова подпроцесса** можно настроить только [общие свойства элемента диаграммы процесса][process_diagram_element_common_properties].

*![Свойства встроенного подпроцесса](embedded_subprocess_properties.png)*

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Вызов процесса][process_diagram_elements_process_call]
- [Общие свойства элементов диаграммы процесса][process_diagram_element_common_properties]
- [Элементы диаграммы процесса][process_diagram_elements]
- [Редактирование диаграммы процесса][process_diagram_designer]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}