---
title: 'Отображение кнопки только для текущего владельца задачи'
kbId: 4963
url: 'https://kb.comindware.ru/article.php?id=4963'
---

# Отображение кнопки только для текущего владельца задачи

Для того, чтобы конкретную операцию мог видеть и выполнять только текущий владелец задачи (чтобы, например, задачу мог завершать конкретный её исполнитель, а не все, у кого есть доступ к кнопке «Завершить задачу» и к экземплярам процессов), введите следующее выражение в условии операции:

- Для системной кнопки «Завершить задачу» в Шаблоне процесса:

```
 

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
```

- Для кнопки в связанном Шаблоне записи

```
 

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
