---
title: Ввод предиката
kbId: 5046
tags:
  - выражения
  - n3
  - тройки
  - предикаты
  - функции
  - вычисляемые атрибуты
  - проверка значения
  - предиктивный ввод
  - подсказки
  - редактор выражений
  - сценарии
hide:
  - tags
---

# Ввод предиката {: #n3_editor_predicate_autocomplete}

1. В позиции предиката нажмите клавиши ++ctrl+space++.
2. Отобразится список [объявленных префиксов][n3_editor_prefix_autocomplete].
*![Список доступных префиксов](n3_editor_predicate_prefix_autocomplete.png)*
3. Выберите префикс в списке, чтобы просмотреть его описание.
4. Дважды нажмите префикс, например `task`, чтобы вставить его в выражение.
5. В позиции после префикса введите двоеточие `:`.
6. Отобразится список функций для префикса.
*![Список функций для префикса](n3_editor_predicate_prefix_function_autocomplete.png)*
7. Дважды нажмите имя функции, например `objectId`, чтобы вставить его в выражение.

```turtle title="Пример: выражение, возвращающее ID исполнителей выполняющихся задач для текущей записи"
@prefix cmw: <http://comindware.com/logics#>.
@prefix task: <http://comindware.com/ontology/task#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
{
  # Получаем список ID задач, связанных с текущей записью
  ?task task:objectId ?item.
  # Получаем ID задач со статусом inProgress (Выполняется)
  ?task cmw:taskStatus taskStatus:inProgress.

  # Возвращаем ID назначенных исполнителей задач
  or {?task cmw:assignee ?value.}
  or {?task cmw:possibleAssignee ?value.}.
}
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Редактор выражений][expression_editor]_
- _[Примеры использования языка N3. База знаний Comindware][n3_use_examples]_

</div>


{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
