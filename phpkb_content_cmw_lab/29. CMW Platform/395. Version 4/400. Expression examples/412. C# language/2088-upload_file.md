---
title: Uploading a file from a local folder
kbId: 2088
---


# Uploading a file from a local folder

To add a file from a local folder on your computer to an attribute with the “Document” data type, enter the following expression:

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
            var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new []{id}, new []{"Path"});
            var path = data[id]["Path"].ToString();
            var fs = new FileStream(@path, FileMode.OpenOrCreate);
            var arrayTitle = path.Split('\\','/');
            var arrayExtension = path.Split('.');
            var docData = new Document
            {
                Title = arrayTitle[arrayTitle.Length-1],
                Extension = arrayExtension[arrayExtension.Length-1]
                };
            string doc = Api.TeamNetwork.DocumentService.CreateDocumentWithStream(docData, fs, "");
            Api.TeamNetwork.ObjectService.EditWithAlias(id, new Dictionary<string,object>{{"Attachment",doc}});
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
                        Text = "Error"
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
                    Text = "Success"
                    }
            }
        };
        return result;
    }
}

```

**where:**

***Path***— system name of the attribute with the "Text" data type, which stores the path to the file that needs to be uploaded into the system (for example, *C:\myfolder\1.cs*);

***Attachment***— system name of the attribute with the "Document" data type where you want to upload the file.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
