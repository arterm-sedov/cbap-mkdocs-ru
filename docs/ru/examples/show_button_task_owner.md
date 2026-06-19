---
title: Отображение кнопки только для текущего владельца задачи
kbId: 5289
tags:
    - N3
    - выражение на N3
    - кнопки
    - пример
    - процессы
hide: tags
---

# Отображение кнопки только для текущего владельца задачи {: #show_button_task_owner }

Для того чтобы конкретную операцию мог видеть и выполнять только текущий владелец задачи (чтобы, например, задачу мог завершать конкретный её исполнитель, а не все, у кого есть доступ к кнопке «Завершить задачу» и к экземплярам процессов), введите следующее выражение в условии операции:

- Для системной кнопки «Завершить задачу» в Шаблоне процесса:

```turtle
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
@prefix task: <http://comindware.com/ontology/task#>.
@prefix cmw: <http://comindware.com/logics#>.

{
cmw:securityContext cmw:currentUser ?user.

?item cmw:taskStatus taskStatus:inProgress.
?item cmw:assignee ?user2.

if{?user == ?user2.}
then {true -> ?value.}
else {false -> ?value.}.
}
```turtle
- Для кнопки в связанном Шаблоне записи

```turtle
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
@prefix task: <http://comindware.com/ontology/task#>.
@prefix cmw: <http://comindware.com/logics#>.

{
cmw:securityContext cmw:currentUser ?user.
?task task:objectId ?item.
?task cmw:taskStatus taskStatus:inProgress.
?task cmw:assignee ?user2.

if{?user == ?user2.}
then {true -> ?value.}
else {false -> ?value.}.
}
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
