---
title: Загрузка файла с компьютера в систему
kbId: 5012
---

# Загрузка файла с компьютера в систему

Для того, чтобы добавить файл из локальной папки на компьютере в атрибут с типом данных «Документ», введите следующее выражение:

```

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;
using System.IO;
 
class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
        try
        {
            var id = userCommandContext.ObjectIds[0];
            var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new []{id}, new []{"Putkfaylu"});
            var path = data[id]["Putkfaylu"].ToString();
            var fs = new FileStream(@path, FileMode.OpenOrCreate);
            var arrayTitle = path.Split('\\','/');
            var arrayExtension = path.Split('.');
            var docData = new Document
            {
                Title = arrayTitle[arrayTitle.Length-1],
                Extension = arrayExtension[arrayExtension.Length-1]
                };
            string doc = Api.TeamNetwork.DocumentService.CreateDocumentWithStream(docData, fs, "");
            Api.TeamNetwork.ObjectService.EditWithAlias(id, new Dictionary<string,object>{{"test",doc}});
        }
        catch
        {
            var result1 = new UserCommandResult
            {
                Success = true,
                Commited = true,
                ResultType = UserCommandResultType.Notificate,
                Messages = new[]
                {
                    new UserCommandMessage
                    {
                        Severity = SeverityLevel.Normal,
                        Text = "Неуспешно"
                        }
                }
            };
            return result1;
        }
        var result = new UserCommandResult
        {
            Success = true,
            Commited = true,
            ResultType = UserCommandResultType.Notificate,
            Messages = new[]
            {
                new UserCommandMessage
                {
                    Severity = SeverityLevel.Normal,
                    Text = "Успешно"
                    }
            }
        };
        return result;
    }
}

```

**где:**

***Putkfaylu*** — системное имя атрибута с типом данных «Текст», который хранит путь к файлу, который нужно загрузить в систему (например, *C:\myfolder\1.cs*);

***test*** — системное имя атрибута с типом данных «Документ»,  куда нужно загрузить файл.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
