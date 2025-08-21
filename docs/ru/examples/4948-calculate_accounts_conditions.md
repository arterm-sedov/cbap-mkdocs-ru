---
title: Вычисление пользователей с определенным параметром
kbId: 4948
---

# Вычисление пользователей с определенным параметром

Для того, чтобы вычислить всех пользователей из Шаблона Пользователя, у которых проставлен какой-либо параметр (чекбокс, в данном случае) для, например, запуска подпроцесса по сотрудникам с определенными характеристиками, введите следующее выражение:

```

@prefix object: <http://comindware.com/ontology/object#>.
@prefix account: <http://comindware.com/ontology/account#>.
{

    ("Sotrudniki" "Uchastvuet") object:findProperty ?Uchastvuet.
            
    ?value a account:Account.
    ?value ?Uchastvuet true.
    
}

```

**где:**

**Sotrudniki** – системное имя Шаблона пользователя;

**Uchastvuet** – системное имя атрибута типа "Логический".

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
