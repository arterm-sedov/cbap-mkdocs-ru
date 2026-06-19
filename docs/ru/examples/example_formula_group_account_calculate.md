---
title: Вычисление всех аккаунтов группы
kbId: 4991
tags:
    - пример
    - формулы
hide: tags
---

# Вычисление всех аккаунтов группы {: #example_formula_group_account_calculate }

Для вычисления аккаунтов, входящих в определённую группу без учёта подгрупп и их участников (в случае, если в группе нет вложенности), введите следующее выражение:

```sql
(from ag in db->_AccountGroup where OR (ag->groupName == "users",ag->groupName == "admins") select ag->groupUsers->id)
```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| "users", "admins" | Названия групп. |

Альтернатива статье [Вычисление всех пользователей группы](https://kb.comindware.ru/article.php?id=4936).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
