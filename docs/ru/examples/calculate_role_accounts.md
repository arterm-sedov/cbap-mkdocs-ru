---
title: Вычисление аккаунтов, входящих в роль
kbId: 4957
---

# Вычисление аккаунтов, входящих в роль

Чтобы получить список всех аккаунтов (пользователей), входящих в определенную роль (например, для назначения задачи), используйте следующее выражение на языке **N3**:

```
@prefix cmwui: <http://comindware.com/ontology/ui#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix role: <http://comindware.com/ontology/role#>.
{
    "role.1" cmwui:toQName ?role.
    ?value a account:Account.
    ?role role:isRoleMember ?value.
}
```

**Здесь:**

`role.1` — ID роли, отображается в адресной строке браузера при просмотре свойств роли.

`value` — выходное значение, в которое будут помещён список аккаунтов, входящих в роль.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
