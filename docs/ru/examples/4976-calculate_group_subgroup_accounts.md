---
title: Вычисление всех пользователей группы и её подгрупп
kbId: 4976
---

# Вычисление всех пользователей группы и её подгрупп

Для того, чтобы получить всех пользователей из определенной группы, включая пользователей подгрупп первого уровня, которые включены в состав указанной группы, введите следующее выражение:

```
UNION(from a in (from b in db->_AccountGroup where b->groupName == "Менеджеры" select b->subGroups->id) select a->cmw.account.groupUsers,
    (from b in db->_AccountGroup where b->groupName == "Менеджеры" select b->cmw.account.groupUsers))
```

**где:**

**"Менеджеры"** — название группы, пользователей которой требуется получить.

Альтернатива статье [Вычисление всех пользователей группы и её подгрупп](https://kb.comindware.ru/article.php?id=4938).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
