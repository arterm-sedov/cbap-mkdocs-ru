---
title: Заполнение коллекции выбранным списком
kbId: 5013
---

# Заполнение коллекции выбранным списком

Для того, чтобы в рамках процесса заполнить коллекцию в текущем объекте каким-либо списком, введите следующее выражение:

```

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
    public static void Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities)
    {     
        var query = new Comindware.TeamNetwork.Api.Data.DatasetQuery
        {
            DatasetId = "lst.53"
        };
        var sessionsData = Api.TeamNetwork.DatasetService.QueryData(query).Rows;
        if (sessionsData == null) { return; } //проверяем, что в списке есть записи
        
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

**где:**

**lst.53** - ИД списка, на основе которого будет заполняться коллекция;

**Applications** - **системное имя атрибута типа Коллекция в текущем Шаблоне записи, которую нужно заполнить в текущем объекте;**

**Register** - системное имя текущего Шаблона записи.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
