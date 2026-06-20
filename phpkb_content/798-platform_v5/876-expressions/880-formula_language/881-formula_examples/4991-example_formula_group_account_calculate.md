---
title: 'Вычисление всех аккаунтов группы'
kbId: 4991
url: 'https://kb.comindware.ru/article.php?id=4991'
updated: '2026-06-20 20:26:26'
---

# Вычисление всех аккаунтов группы

Для вычисления аккаунтов, входящих в определённую группу без учёта подгрупп и их участников (в случае, если в группе нет вложенности), введите следующее выражение:

```
(from ag in db->_AccountGroup where OR (ag->groupName == "users",ag->groupName == "admins") select ag->groupUsers->id)
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| "users", "admins" | Названия групп. |

Альтернатива статье [Вычисление всех пользователей группы](https://kb.comindware.ru/article.php?id=4936).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
