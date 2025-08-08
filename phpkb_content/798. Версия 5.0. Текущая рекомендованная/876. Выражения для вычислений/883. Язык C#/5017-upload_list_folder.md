---
title: Выгрузка списка в локальную папку
kbId: 5017
---

# Выгрузка списка в локальную папку

Для того, чтобы можно было в процессе экспортировать определенный список в excel и помещать файл в локальную папку, введите следующее выражение:

```

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data;
using System.IO;
class Script
{
    public static void Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities)
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
        using (var fs = new System.IO.FileStream(@"\\storage\Temp\4AP11\CurrentSprint.xlsx", System.IO.FileMode.Create))
        {
            exportData.Stream.Position = 0;
            exportData.Stream.CopyTo(fs);
        }

    }
}

```

**где:**

**Issue** - системное имя Шаблона записи, где нужно взять список для выгрузки;

**CurrentSprint** - системное имя списка для выгрузки;

**\\storage\Temp\4AP11\CurrentSprint.xlsx** - путь для выгрузки и имя выгружаемого файла.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
