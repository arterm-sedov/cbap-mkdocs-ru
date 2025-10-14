---
title: Отображение поля при определенном значении ссылочного атрибута
kbId: 4960
---

# Отображение поля при определенном значении ссылочного атрибута

Для того, чтобы установить условие на отображение поля / вкладки / столбца и т.д., если в ссылочном поле стоит определенное значение, введите следующее выражение:

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

**где:**

**Issue** – системное имя текущего Шаблона записи;

**IssueTypeLink** – системное имя атрибута типа "Ссылка" в текущем Шаблоне записи;

****IssueType****– системное имя Шаблона записи, на который ссылается **IssueTypeLink** ;

**Title**– системное имя отображаемого атрибута в Шаблоне записи **IssueType**;

**Task** – нужное значение атрибута **Title**.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
