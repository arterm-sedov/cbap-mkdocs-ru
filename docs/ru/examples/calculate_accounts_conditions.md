---
title: Вычисление пользователей с определенным параметром
kbId: 4948
tags:
    - N3
    - атрибуты
    - выражение на N3
    - пример
    - процессы
hide: tags
---

# Вычисление пользователей с определенным параметром {: #calculate_accounts_conditions }

Для того чтобы вычислить всех пользователей из Шаблона Пользователя, у которых проставлен какой-либо параметр (чекбокс, в данном случае) для, например, запуска подпроцесса по сотрудникам с определенными характеристиками, введите следующее выражение:

```turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix account: <http://comindware.com/ontology/account#>.
{

    ("Sotrudniki" "Uchastvuet") object:findProperty ?Uchastvuet.

    ?value a account:Account.
    ?value ?Uchastvuet true.

}
```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| `Sotrudniki` | Системное имя Шаблона пользователя. |
| `Uchastvuet` | Системное имя атрибута типа «**Логический**». |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
