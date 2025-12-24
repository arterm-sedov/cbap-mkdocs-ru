---
title: Uploading attachments to a local folder
kbId: 2097
---


# Uploading attachments to a local folder

To save the attached file(s) from an attribute with the "Document" data type to a local folder, enter the following expression:

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
                                             var path = @"C:\document\";
                                             var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new string[] {userCommandContext.ObjectIds[0]}, new string[] {"Document"});
                                             var documentIdsObj = data[userCommandContext.ObjectIds[0]]["Document"];
               var documentIds = documentIdsObj as IEnumerable<object>;
                                             if (documentIds == null)
                                             {
                                                            documentIds = new string[] {documentIdsObj as string};
                                             }
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
                                                                              Text = "Failed to upload"
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
                                                               Text = "Success"
                                                }
                                             }
                  };
                  return result;
    }
}

```

**where:**

***C:\document\*** — path for uploading file/s;

***Document*** – system name of the attribute with the "Document" data type.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
