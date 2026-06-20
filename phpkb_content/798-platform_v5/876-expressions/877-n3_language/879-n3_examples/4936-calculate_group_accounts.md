---
title: 'Вычисление всех пользователей группы'
kbId: 4936
url: 'https://kb.comindware.ru/article.php?id=4936'
updated: '2026-06-20 18:06:09'
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

Альтернатива статье [Вычисление всех аккаунтов группы][example_formula_group_account_calculate].

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
