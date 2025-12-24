---
title: Вычисление всех пользователей шаблона пользователя
kbId: 4967
---

# Вычисление всех пользователей шаблона пользователя

Для того, чтобы получить всех пользователей из определенного шаблона пользователя, введите следующее выражение:

```

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

**где:**

**Polzovateli** – системное имя Шаблона пользователя.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
