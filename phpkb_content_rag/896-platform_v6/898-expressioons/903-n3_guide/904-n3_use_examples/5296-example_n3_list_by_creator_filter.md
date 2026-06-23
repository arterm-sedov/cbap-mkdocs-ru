---
title: 'Фильтр списка по создателю'
kbId: 5296
url: 'https://kb.comindware.ru/article.php?id=5296'
updated: '2026-06-20 17:34:12'
---

# Фильтр списка по создателю

Для того чтобы настроить фильтр отображения записей в списке, где текущий пользователь - создатель записи, введите следующее выражение:

```
@prefix cmw: <http://comindware.com/logics#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix user: <http://comindware.com/ontology/user#>.

{

 ("eventorder" "_creator") object:findProperty ?propertyCreator.
 cmw:securityContext cmw:currentUser ?user.
 ?eventorderTemplate object:alias "eventorder".
 ?item cmw:container ?eventorderTemplate.
 ?item ?propertyCreator ?user.

}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `eventorder` | Системное имя текущего шаблона записи. |
| `_creator` | Системное имя системного атрибута типа «**Аккаунт**», в котором хранится создатель записи. |