---
title: Вычисление всех пользователей группы
kbId: 4936
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

**где:**

**"Менеджеры"** — название группы, пользователей которой требуется получить.

Альтернатива статье [Вычисление всех пользователей группы](https://kb.comindware.ru/article.php?id=1082).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
