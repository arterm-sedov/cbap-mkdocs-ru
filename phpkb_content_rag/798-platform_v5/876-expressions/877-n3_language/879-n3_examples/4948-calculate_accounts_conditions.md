---
title: 'Вычисление пользователей с определенным параметром'
kbId: 4948
url: 'https://kb.comindware.ru/article.php?id=4948'
updated: '2026-06-20 18:06:08'
---

# Вычисление пользователей с определенным параметром

Для того чтобы вычислить всех пользователей из Шаблона Пользователя, у которых проставлен какой-либо параметр (чекбокс, в данном случае) для, например, запуска подпроцесса по сотрудникам с определенными характеристиками, введите следующее выражение:

```
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
| --- | --- |
| `Sotrudniki` | Системное имя Шаблона пользователя. |
| `Uchastvuet` | Системное имя атрибута типа «**Логический**». |