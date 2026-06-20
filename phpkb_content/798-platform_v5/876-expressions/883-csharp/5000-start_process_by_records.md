---
title: 'Старт процесса по записям таблицы'
kbId: 5000
url: 'https://kb.comindware.ru/article.php?id=5000'
updated: '2026-06-20 18:06:22'
---

# Старт процесса по записям таблицы

Для того чтобы запустить процесс по каждой из записей определенной таблицы, введите следующее выражение:

```
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
class Script
{
    public static void Main(Comindware.Process.Api.Data.ScriptContext context)
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

**Здесь:**

| Значение | Описание |
| --- | --- |
| `lst.74` | ID таблицы, по записям которой нужно запустить экземпляры процесса. |
| `pa.2` | ID шаблона процесса, экземпляры которого нужно создать по записям из выбранной таблицы. |

Фильтр таблицы

Если для таблицы требуется фильтр, задайте его на языке N3. Иначе экземпляры процесса будут запущены по всем записям шаблона записи, в котором находится таблица.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
