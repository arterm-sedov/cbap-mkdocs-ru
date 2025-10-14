---
title: Вычисление состава группы
kbId: 4937
---

# Вычисление состава группы

Для вычисления пользователей и подгрупп, входящих в определённую группу, введите следующее выражение:

```
@prefix account: <http://comindware.com/ontology/account#>.
{
    ?projectOffice account:groupName "Менеджеры".
    ?value account:userGroupMembership ?projectOffice.
 }
```

**где:**

**"Менеджеры"** — название группы, пользователей которой требуется получить.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
