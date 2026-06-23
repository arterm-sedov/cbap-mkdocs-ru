---
title: 'Выгрузка таблицы в локальную папку'
kbId: 5196
url: 'https://kb.comindware.ru/article.php?id=5196'
updated: '2026-06-20 17:34:25'
---

# Выгрузка таблицы в локальную папку

Для того чтобы можно было в процессе экспортировать определенную таблицу в Excel и помещать файл в локальную папку, введите следующее выражение:

```
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data;
using System.IO;
class Script
{
    public static void Main(Comindware.Process.Api.Data.ScriptContext context)
    {
        // get sessions object app
        var sessionsObjectAppId = Api.TeamNetwork.ObjectAppService.List().First(oa => oa.Alias == "Issue").Id;
        
        // get "reception"-list 
        var containerLists = Api.TeamNetwork.DatasetConfigurationService.List(sessionsObjectAppId);
        var receptionList = containerLists.FirstOrDefault(list => list.Alias == "CurrentSprint");
         var receptionQuery = new DatasetQuery{DatasetId = receptionList.Id,
                                                             Grouping = receptionList.Grouping,
                                                             Sorting = receptionList.Sorting,
                                                             Paging = receptionList.Paging,  
                                                             Filter =  receptionList.Filter,
                                                                };
    
        // export list
        var exportData = Api.TeamNetwork.DatasetExportService.ExportToExcel(receptionQuery);

        // save document to current folder
        using (var fs = new System.IO.FileStream(@"\\\\storage\\Temp\\4AP11\\CurrentSprint.xlsx", System.IO.FileMode.Create))
        {
            exportData.Stream.Position = 0;
            exportData.Stream.CopyTo(fs);
        }

    }
}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Issue` | Системное имя шаблона записи, из которого нужно выгрузить таблицу. |
| `CurrentSprint` | Системное имя таблицы для выгрузки. |
| `\\\\storage\\Temp\\4AP11\\CurrentSprint.xlsx` | Путь для выгрузки и имя выгружаемого файла. |