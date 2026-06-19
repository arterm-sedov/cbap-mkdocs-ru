---
title: Вычисление всех пользователей шаблона пользователя
kbId: 5293
tags:
    - N3
    - выражение на N3
    - пример
hide: tags
---

# Вычисление всех пользователей шаблона пользователя {: #calculate_account_template_accounts }

Для того чтобы получить всех пользователей из определенного шаблона пользователя, введите следующее выражение:

```turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix cmw: <http://comindware.com/logics#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix container: <http://comindware.com/ontology/container#>.

{

  ?polz container:alias "Polzovateli".
  ?value account:extendedBy ?polz.
    }
```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| `Polzovateli` | Системное имя Шаблона пользователя. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
