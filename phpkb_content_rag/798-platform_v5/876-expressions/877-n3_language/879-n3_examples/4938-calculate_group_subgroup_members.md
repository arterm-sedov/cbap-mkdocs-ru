---
title: 'Вычисление всех пользователей группы и её подгрупп'
kbId: 4938
url: 'https://kb.comindware.ru/article.php?id=4938'
updated: '2026-06-17 14:09:53'
---

# Вычисление всех пользователей группы и её подгрупп

Для того чтобы получить всех пользователей из определенной группы, включая пользователей подгрупп первого уровня, которые включены в состав указанной группы, введите следующее выражение:

```
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
| --- | --- |
| "Менеджеры" | Название группы, пользователей которой требуется получить. |

Альтернатива статье [Вычисление всех пользователей группы и её подгрупп](4976-calculate_group_subgroup_accounts.html#calculate_group_subgroup_accounts).