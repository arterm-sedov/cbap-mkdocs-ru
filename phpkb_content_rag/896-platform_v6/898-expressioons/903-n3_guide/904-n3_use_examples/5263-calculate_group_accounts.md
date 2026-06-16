---
title: 'Вычисление всех пользователей группы'
kbId: 5263
url: 'https://kb.comindware.ru/article.php?id=5263'
updated: '2026-06-16 19:16:28'
---

# Вычисление всех пользователей группы

Для вычисления пользователей, входящих в определённую группу без учета подгрупп и их участников (в случае, если в группе нет вложенности), введите следующее выражение:

```
@prefix account: <http://comindware.com/ontology/account#>.
{
    ?projectOffice account:groupName "Менеджеры".
    ?users account:userGroupMembership ?projectOffice.
    ?users account:fullName ?.
    ?users -> ?value.
}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| "Менеджеры" | Название группы, пользователей которой требуется получить. |

Альтернатива статье [Вычисление всех аккаунтов группы](https://kb.comindware.ru/article.php?id=5246).