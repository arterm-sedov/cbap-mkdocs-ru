---
title: Выгрузка вложений в локальную папку на сервере
kbId: 2106
---

# Выгрузка вложений в локальную папку на сервере

Чтобы сохранить один или несколько вложенных файлов из атрибута типа «**Документ**» в локальную папку **на сервере**, используйте приведённый ниже скрипт в настройках **[кнопки][buttons]**.

**Здесь:**

`C:\document\` — путь для скачивания файлов на сервере;

`Document` — системное имя атрибута типа «**Документ**».

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
        try {
//Укажите путь для скачивания файлов на сервере
              var path = @"C:\document\";
//"Document" – поменяйте на системное имя своего атрибута типа «Документ»
              var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new string[] {userCommandContext.ObjectIds[0]}, new string[] {"Document"});
//"Document" – поменяйте на системное имя своего атрибута типа «Документ»
              var documentIdsObj = data[userCommandContext.ObjectIds[0]]["Document"];
              var documentIds = documentIdsObj as IEnumerable<object>;
                  if (documentIds == null)
                     {documentIds = new string[] {documentIdsObj as string};}
                  foreach (var documentIdObj in documentIds)
                          {
                           var documentId = documentIdObj as string;
                           var documentData = Api.TeamNetwork.DocumentService.GetContent(documentId);
                           var documentInfo = Api.TeamNetwork.DocumentService.GetDocument(documentId);
                           var docData = new Document
                               {
                                Title = documentData.Name,
                                Extension = documentInfo.Extension
                               };
                                 var stream = new MemoryStream();
                                 stream.Write(documentData.Data, 0, documentData.Data.Length);
                                 stream.Seek(0, SeekOrigin.Begin);
                                 var filepath = path + documentData.Name;
                                 using(FileStream outstr = new FileStream(filepath, FileMode.Create))
                                    {
                                     stream.CopyTo(outstr);
                                     }
                                      }
                               }
                               catch
                               {
                                var badresult = new UserCommandResult
                                    {
                                      Success = true,
                                      Commited = true,
                                      ResultType = UserCommandResultType.DataChange,
                                      Messages = new[]
                                         {
                                          new UserCommandMessage
                                            {
                                             Severity = SeverityLevel.Normal,
                                             Text = "Неудачно"
                                              }
                                            }
                                  };
                                  return badresult;
                               }
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
                                         Text = "Удачно"
                                        }
                                  }
                   };
                   return result;
    }
}
```

 

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
