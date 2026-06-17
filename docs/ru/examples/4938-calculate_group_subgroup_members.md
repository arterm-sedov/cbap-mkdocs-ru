---
title: Вычисление всех пользователей группы и её подгрупп
kbId: 4938
tags:
    - N3
    - выражение на N3
    - пример
hide: tags
---

# Вычисление всех пользователей группы и её подгрупп {: #calculate_group_subgroup_members }

Для того чтобы получить всех пользователей из определенной группы, включая пользователей подгрупп первого уровня, которые включены в состав указанной группы, введите следующее выражение:

```turtle
@prefix account: <http://comindware.com/ontology/account#>.
@prefix assert: <http://comindware.com/logics/assert#>.
{
    ?projectOffice account:groupName "Менеджеры".
    ?users account:userGroupMembership ?projectOffice.
    ?projectOffice account:subGroups ?subgroups.
    ?subusers account:userGroupMembership ?subgroups.
    (
        {?subusers account:fullName ?.
         ?subusers -> ?value.}
        {?users account:fullName ?.
         ?users -> ?value.}
    )assert:union true.
}
```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| "Менеджеры" | Название группы, пользователей которой требуется получить. |

Альтернатива статье [Вычисление всех пользователей группы и её подгрупп][calculate_group_subgroup_accounts].

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
