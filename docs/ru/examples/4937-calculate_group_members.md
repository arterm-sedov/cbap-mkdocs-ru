---
title: Вычисление состава группы
kbId: 5264
tags:
    - N3
    - выражение на N3
    - пример
hide: tags
---

# Вычисление состава группы {: #calculate_group_members }

Для вычисления пользователей и подгрупп, входящих в определённую группу, введите следующее выражение:

```turtle
@prefix account: <http://comindware.com/ontology/account#>.
{
    ?projectOffice account:groupName "Менеджеры".
    ?value account:userGroupMembership ?projectOffice.
 }
```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| "Менеджеры" | Название группы, пользователей которой требуется получить. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
