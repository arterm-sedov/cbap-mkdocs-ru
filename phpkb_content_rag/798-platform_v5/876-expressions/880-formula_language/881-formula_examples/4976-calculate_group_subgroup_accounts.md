---
title: 'Вычисление всех пользователей группы и её подгрупп'
kbId: 4976
url: 'https://kb.comindware.ru/article.php?id=4976'
updated: '2023-08-24 09:02:30'
---

# Вычисление всех пользователей группы и её подгрупп

Для того, чтобы получить всех пользователей из определенной группы, включая пользователей подгрупп первого уровня, которые включены в состав указанной группы, введите следующее выражение:

```
UNION(from a in (from b in db->_AccountGroup where b->groupName == "Менеджеры" select b->subGroups->id) select a->cmw.account.groupUsers,
    (from b in db->_AccountGroup where b->groupName == "Менеджеры" select b->cmw.account.groupUsers))
```

**где:**

**"Менеджеры"** — название группы, пользователей которой требуется получить.

Альтернатива статье `![](https://kb.comindware.ru/images/marker.png){Article-ID:4938}`.