---
title: 'Вычисление всех пользователей шаблона пользователя'
kbId: 5293
url: 'https://kb.comindware.ru/article.php?id=5293'
updated: '2026-06-20 17:34:00'
---

# Вычисление всех пользователей шаблона пользователя

Для того чтобы получить всех пользователей из определенного шаблона пользователя, введите следующее выражение:

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

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Polzovateli` | Системное имя Шаблона пользователя. |