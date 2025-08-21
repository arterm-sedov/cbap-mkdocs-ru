---
title: Загрузка картинки из атрибута типа документ в HTML поле
kbId: 5014
---

# Загрузка картинки из атрибута типа документ в HTML поле

Для того, чтобы выгрузить картинку в HTML поле, введите следующее выражение:

```

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
        var imagePropertyAlias = "Document";
        var currentObjectid = userCommandContext.ObjectIds[0];
        var response = Api.TeamNetwork.ObjectService.GetPropertyValues(new List<string> { currentObjectid }, new List<string> { imagePropertyAlias });
        Dictionary<string, object> currentObjectPropertyValues;
        response.TryGetValue(currentObjectid, out currentObjectPropertyValues);
        object multivalueDocument;
        currentObjectPropertyValues.TryGetValue(imagePropertyAlias, out multivalueDocument);
        var documentsList = (object[])multivalueDocument;
        var documentId = documentsList.First();
        var content = (Api.TeamNetwork.DocumentService.GetContent((string)documentId)).Data;

        var docHTML = $"<p><span style=\"font-size:11pt;\"><span><span style=\"font-family:Calibri,sans-serif;\"><img src=\"data:image/png;base64,{Convert.ToBase64String(content)}\" style=\"height:500px; width:1000px\" /></span></span></span></p><p>&nbsp;</p>";

        var data = new Dictionary<string, object>
        {
          { "HTML", docHTML}
        };
        Api.TeamNetwork.ObjectService.EditWithAlias("ExportImport", currentObjectid, data);

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
                    Text = "Картинка загружена!"
                }
            }
        };
        return result;
    }
}

```

**где:**

**Document**   = Атрибут типа документ, куда загружается картинка

**HTML**  = Атрибут типа текст в HTML формате

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
