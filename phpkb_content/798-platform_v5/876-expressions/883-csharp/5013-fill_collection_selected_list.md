---
title: 'Заполнение коллекции выбранной таблицей'
kbId: 5013
url: 'https://kb.comindware.ru/article.php?id=5013'
updated: '2026-06-17 14:09:49'
---

# Заполнение коллекции выбранной таблицей

Для того чтобы в рамках процесса заполнить коллекцию в текущем объекте какой-либо таблицей, введите следующее выражение:

```
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
    public static void Main(Comindware.Process.Api.Data.ScriptContext context)
    {     
        var query = new Comindware.TeamNetwork.Api.Data.DatasetQuery
        {
            DatasetId = "lst.53"
        };
        var sessionsData = Api.TeamNetwork.DatasetService.QueryData(query).Rows;
        if (sessionsData == null) { return; } //проверяем, что в таблице есть записи
        
        var objectId = context.BusinessObjectId; //текущая запись
        List<string> ApplicationIds = new List<string>();
        foreach (var row in sessionsData) 
        {
            ApplicationIds.Add(row.Id);
        }
        var data = new Dictionary<string, object>
        {
            { "Applications", ApplicationIds} //вторым аргументом пишем лист idшников
        };
        
        Api.TeamNetwork.ObjectService.EditWithAlias("Register", objectId, data); //записываем коллекцию в текущем объекте.
    }
}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `lst.53` | ID таблицы, на основе которой будет заполняться коллекция. |
| `Applications` | Системное имя атрибута типа «**Коллекция**» в текущем шаблоне записи. В этот атрибут нужно записать выбранные записи. |
| `Register` | Системное имя текущего шаблона записи. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
