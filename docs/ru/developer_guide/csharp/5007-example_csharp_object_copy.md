---
title: Копирование объекта
kbId: 5007
---

# Копирование объекта

Для того чтобы скопировать запись, создайте в текущем шаблоне записи кнопку с операцией C#-скрипт и введите следующее выражение:

```

using System; 
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    { 
 foreach (var objectId in userCommandContext.ObjectIds)
        {

            Api.TeamNetwork.ObjectService.Clone(objectId,null, true);
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
                    Text = "Запись скопирована"
                }
            }
        };

        return result;
    }
}

```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
