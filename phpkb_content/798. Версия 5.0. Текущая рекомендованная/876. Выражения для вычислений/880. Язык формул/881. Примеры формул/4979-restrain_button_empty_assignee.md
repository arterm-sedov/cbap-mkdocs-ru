---
title: Ограничение отображения кнопки при пустом исполнителе
kbId: 4979
---

# Ограничение отображения кнопки при пустом исполнителе

Для того, чтобы скрыть кнопку в Шаблоне процесса, если пустой исполнитель (например, для кнопки ***"Завершить задачу"***), введите следующее выражение в условии:

```
 AND(NOT(EMPTY($assignee)),$cmw.taskStatus == "cmw.taskStatus.inProgress")
```

**где:**

**assignee** – системное имя системного атрибута, хранящего исполнителя задачи;

**cmw.taskStatus** – системное имя системного атрибута – статуса задачи.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
