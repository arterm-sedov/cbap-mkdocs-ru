---
title: 'Вычисление всех аккаунтов группы'
kbId: 2644
url: 'https://kb.comindware.ru/article.php?id=2644'
updated: '2024-11-07 12:12:09'
---

# Вычисление всех аккаунтов группы

Для вычисления аккаунтов, входящих в определённую группу без учёта подгрупп и их участников (в случае, если в группе нет вложенности), введите следующее выражение:

```
(from ag in db->_AccountGroup where OR (ag->groupName == "users",ag->groupName == "admins") select ag->groupUsers->id)
```

**где:**

**"users", "admins"** — названия групп.

Альтернатива статье [Вычисление всех пользователей группы](https://kb.comindware.ru/article.php?id=2488).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
