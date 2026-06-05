---
title: 'Вычисление всех аккаунтов группы'
kbId: 4991
url: 'https://kb.comindware.ru/article.php?id=4991'
updated: '2024-11-07 12:12:09'
---

# Вычисление всех аккаунтов группы

Для вычисления аккаунтов, входящих в определённую группу без учёта подгрупп и их участников (в случае, если в группе нет вложенности), введите следующее выражение:

```
(from ag in db->_AccountGroup where OR (ag->groupName == "users",ag->groupName == "admins") select ag->groupUsers->id)
```

**где:**

**"users", "admins"** — названия групп.

Альтернатива статье `![](https://kb.comindware.ru/images/marker.png){Article-ID:4936}`.