---
title: 'Вычисление пользователей, у которых есть активные задачи (с учетом замещений)'
kbId: 1785
url: 'https://kb.comindware.ru/article.php?id=1785'
updated: '2023-12-21 14:46:52'
---

# Вычисление пользователей, у которых есть активные задачи (с учетом замещений)

Для того, чтобы вычислить всех пользователей у которых на данный момент есть активные задачи, учитывая все замещения (чтобы, например, запустить по ним подпроцесс отправки уведомления по задачам (см. [эту статью](https://kb.comindware.ru/article/%d0%9d%d0%b0%d1%81%d1%82%d1%80%d0%be%d0%b9%d0%ba%d0%b0-%d0%bf%d0%b5%d1%80%d0%b8%d0%be%d0%b4%d0%b8%d1%87%d0%b5%d1%81%d0%ba%d0%b8%d1%85-%d0%bd%d0%b0%d0%bf%d0%be%d0%bc%d0%b8%d0%bd%d0%b0%d0%bd%d0%b8%d0%b9-%d0%be%d0%b1-%d0%be%d1%82%d0%ba%d1%80%d1%8b%d1%82%d1%8b%d1%85-%d0%b7%d0%b0%d0%b4%d0%b0%d1%87%d0%b0%d1%85-1355.html)), введите следующее выражение:

```
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix log: <http://www.w3.org/2000/10/swap/log#>.
@prefix cmw:  <http://comindware.com/logics#>.
@prefix substitution: <http://comindware.com/ontology/substitution#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix session: <http://comindware.com/ontology/session#>.
@prefix timelocal: <http://comindware.com/logics/time/local#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
@prefix account: <http://comindware.com/ontology/account#>.
{
    ?class cmw:className "Account".
    ?value a ?class.
    ?value account:active true.
    cmw:securityContext cmw:currentUser ?user.
    session:context session:requestTime ?now.
    ?task a cmw:UserTask.
    not {?value cmw:isDisabled true.}.
    
   or
    {
      ?task cmw:assignee ?value.
    }
    or
    {
       ?task cmw:possibleAssignee ?value.
    }
    or
    {
        ?substitut a substitution:Substitution.
        ?substitut substitution:startDate ?startDate.
        ?substitut substitution:endDate ?endDate. 
        ?now timelocal:between (?startDate ?endDate).
        ?substitut substitution:deputies ?value.
        ?substitut substitution:absentee ?abs.
          ?task cmw:assignee ?abs.
    }
    or
    {
        ?substitut a substitution:Substitution.
        ?substitut substitution:startDate ?startDate.
        ?substitut substitution:endDate ?endDate. 
        ?now timelocal:between (?startDate ?endDate).
        ?substitut substitution:deputies ?value.
        ?substitut substitution:absentee ?abs.
       ?task cmw:possibleAssignee ?abs.
    }.
?task cmw:taskStatus taskStatus:inProgress.

}
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
