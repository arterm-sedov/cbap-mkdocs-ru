---
title: Старт процесса по записям списка (кнопка)
kbId: 5018
---

# Старт процесса по записям списка (кнопка)

Для того, чтобы на запустить процесс по каждой из записей определенного списка, введите следующее выражение:

```

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
{
string result_ = "Операция выполнена";
var result = new UserCommandResult
{
Success = true,
Commited = true,
ResultType = UserCommandResultType.Navigate,
NavigationResult = new UserCommandNavigationResult
{
Context = ContextType.Task,
ObjectId = null
},
Messages = new[]
{
new UserCommandMessage
{
Severity = SeverityLevel.Normal,
Text = result_
}
}
};

var sessionsObjectAppId = Api.TeamNetwork.ObjectAppService.List().First(oa => oa.Alias == "TEMP_VAR").Id; 
var containerLists = Api.TeamNetwork.DatasetConfigurationService.List(sessionsObjectAppId);
var receptionList = containerLists.FirstOrDefault(list => list.Alias == "newList1"); 
var query = new Comindware.TeamNetwork.Api.Data.DatasetQuery
{
DatasetId = receptionList.Id,
Filter = receptionList.Filter
};
var sessionsData = Api.TeamNetwork.DatasetService.QueryData(query).Rows;

if (sessionsData == null)
{
result_ = "Список пуст";
result.Success = false;
return result;
}
foreach (var row in sessionsData)
{
Api.Process.ProcessObjectService.CreateWithObjectId("pa.2", null, row.Id); 
}
return result;
}
}

```

**где:**

**"TEMP\_VAR"** - системное имя Шаблона записи, где хранится нужный список;

**"newList1"** - системное имя необходимого списка;

**"pa.2"** - ИД Шаблона процесса, который нужно запустить для каждой записи из выбранного списка.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
