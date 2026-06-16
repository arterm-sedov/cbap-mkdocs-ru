---
title: 'Старт связанного процесса по нескольким записям'
kbId: 5200
url: 'https://kb.comindware.ru/article.php?id=5200'
updated: '2026-06-16 19:15:16'
---

# Старт связанного процесса по нескольким записям

Для того чтобы запустить связанный процесс по нескольким записям (которые будут добавлены в коллекцию), введите следующее выражение:

```
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data;
using Comindware.TeamNetwork.Api.Data.UserCommands;

public class Script
{
    public static UserCommandResult Main(UserCommandContext ucContext)
    {
        var ids = ucContext.ObjectIds;
        if (ids == null || ids.Count() == 0)
        {
            return new UserCommandResult
            {
                Success = false,
                Commited = false,
                ResultType = UserCommandResultType.DataChange,
                Messages = new[]
                {
                    new UserCommandMessage
                    {
                        Severity = SeverityLevel.Major,
                        Text = "Протоколы не выбраны для отправки!"
                    }
                }
            };
        }
        var protocolDataIds = new List<string>();
        foreach (var id in ids)
        {
            // if id подходит
            var dataFromProtocol = new Dictionary<string, object> { { "Protokolispytaniy", id } };
            protocolDataIds.Add(Api.TeamNetwork.ObjectService.CreateWithAlias("OtpravkiprotokolavFGIS", dataFromProtocol));
        }
        var protocolDataCollection = new Dictionary<string, object> { { "syncDataForProtocols", protocolDataIds } };
        var packageId = Api.TeamNetwork.ObjectService.CreateWithAlias("SinkhronizatsiisFGIS", protocolDataCollection); // Создаем пакет по выбранным объектам
        var processAppId = Api.Process.ProcessAppService.GetProcessAppIdByAlias("SinkhronizatsiyasFGIS");
        var processInstanceId = Api.Process.ProcessObjectService.CreateWithObjectId(processAppId, null, packageId);
        var result = new UserCommandResult
        {
            Success = true,
            Commited = true,
            ResultType = UserCommandResultType.DataChange,
            Messages = new[]
            {
                new UserCommandMessage
                {
                    Severity = SeverityLevel.Normal,
                    Text = "По выбранным протоколам начата отправка"
                }
            }
        };
        return result;
    }
}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Protokolispytaniy` | Системное имя текущего шаблона записи. |
| `OtpravkiprotokolavFGIS` | Системное имя технического шаблона записи, связанного с текущим шаблоном записи. |
| `syncDataForProtocols` | Системное имя атрибута шаблона записи `SinkhronizatsiisFGIS`. |
| `SinkhronizatsiisFGIS` | Системное имя шаблона записи, в котором хранится коллекция записей из шаблона `Protokolispytaniy`. |
| `SinkhronizatsiyasFGIS` | Системное имя шаблона процесса по шаблону записи `SinkhronizatsiisFGIS`. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
