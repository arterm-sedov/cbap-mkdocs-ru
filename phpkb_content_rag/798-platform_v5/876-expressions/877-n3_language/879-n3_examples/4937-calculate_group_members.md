---
title: 'Вычисление состава группы'
kbId: 4937
url: 'https://kb.comindware.ru/article.php?id=4937'
updated: '2026-06-17 14:09:53'
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

**Здесь:**

| Значение | Описание |
| --- | --- |
| "Менеджеры" | Название группы, пользователей которой требуется получить. |