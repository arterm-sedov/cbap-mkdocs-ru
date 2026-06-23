---
title: 'Старт процесса по записям таблицы (кнопка)'
kbId: 5197
url: 'https://kb.comindware.ru/article.php?id=5197'
updated: '2026-06-20 17:34:22'
---

# Старт процесса по записям таблицы (кнопка)

Для того чтобы запустить процесс по каждой из записей определенной таблицы, введите следующее выражение:

```
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext)
    {
        string result_ = "Кнопка выполнена";
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
            result_ = "Таблица пуста";
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

**Здесь:**

| Значение | Описание |
| --- | --- |
| `TEMP_VAR` | Системное имя шаблона записи, в котором хранится нужная таблица. |
| `newList1` | Системное имя таблицы. |
| `pa.2` | ID шаблона процесса, который нужно запустить для каждой записи из выбранной таблицы. |