---
title: Старт процесса по записям списка
kbId: 5000
---

# Старт процесса по записям списка

Для того, чтобы на запустить процесс по каждой из записей определенного списка, введите следующее выражение:

```
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
class Script
{
    public static void Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities)
    {
        var query = new Comindware.TeamNetwork.Api.Data.DatasetQuery
        {
            DatasetId = "lst.74"
        };
        var sessionsData = Api.TeamNetwork.DatasetService.QueryData(query).Rows;
        if (sessionsData == null) { return; }
        foreach (var row in sessionsData) 
        {
            Api.Process.ProcessObjectService.CreateWithObjectId("pa.2", null, row.Id);
        }
    }
}
```

**где:**

**lst.74** - ИД списка, по записям которого нужно запустить экземпляры процесса;

**pa.2** - ИД Шаблона процесса, экземпляры которого нужно создать по записям из выбранного списка.

**Примечание :** фильтр на списке (при его необходимости) должен быть написан на языке N3. В противном случае, запустятся экземпляры процесса по всем записям в Шаблоне записи, где находится список.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
