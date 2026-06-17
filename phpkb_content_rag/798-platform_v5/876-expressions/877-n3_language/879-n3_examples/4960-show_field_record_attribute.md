---
title: 'Отображение поля при определенном значении ссылочного атрибута'
kbId: 4960
url: 'https://kb.comindware.ru/article.php?id=4960'
updated: '2026-06-17 14:09:55'
---

# Отображение поля при определенном значении ссылочного атрибута

Для того чтобы установить условие на отображение поля / вкладки / столбца и т.д., если в ссылочном поле стоит определенное значение, введите следующее выражение:

```
@prefix object: <http://comindware.com/ontology/object#>.
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
{
("Issue" "IssueTypeLink") object:findProperty ?IssueTypeProperty.
("IssueType" "Title") object:findProperty ?TitleProperty.

 ?item ?IssueTypeProperty ?IssueType.
 ?IssueType ?TitleProperty ?Title.

if{?Title math:equalTo "Task".}
then{true -> ?value.}
else{false -> ?value.}
       }
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Issue` | Системное имя текущего Шаблона записи. |
| `IssueTypeLink` | Системное имя атрибута типа «**Ссылка**» в текущем Шаблоне записи. |
| `IssueType` | Системное имя Шаблона записи, на который ссылается **IssueTypeLink**. |
| `Title` | Системное имя отображаемого атрибута в Шаблоне записи **IssueType**. |
| `Task` | Нужное значение атрибута **Title**. |