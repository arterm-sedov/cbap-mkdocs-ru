---
kbId: 5033
tags:
  - выражения
  - формулы
  - функции
  - шаблоны
  - атрибуты
  - вычисляемые атрибуты
  - список значений
  - проверка значения
  - предиктивный ввод
  - подсказки
  - редактор выражений
  - операторы
  - переменные
  - переменные в сценарии
  - сценарии
hide:
  - tags
---

# Ввод имён переменных в сценарии

При редактировании формул в сценариях предиктивный ввод подсказывает имена локальных переменных в текущем сценарии.

1. Введите символы `$$`.
2. Отобразится список системных и локальных переменных, доступных в текущем сценарии. См. «**[Использование переменных в сценарии][scenario_variables]**».
3. Дважды нажмите имя переменной, чтобы вставить его в формулу.

*![Список локальных переменных в сценарии](formula_editor_local_variables.png)*

```mysql title="Пример: формула, прибавляющая 1 день к текущей дате"
ADDDAYS($$requestTime, 1)
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Редактор выражений][expression_editor]_

</div>

**[Примеры использования формул. База знаний Comindware][formula_use_examples]**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
