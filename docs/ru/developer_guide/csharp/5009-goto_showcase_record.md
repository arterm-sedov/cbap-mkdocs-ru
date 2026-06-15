---
title: Переход в объект с витрины
kbId: 5187

tags:
    - C#
    - скрипт
    - C#-скрипт
    - пример скрипта
hide: tags
---

# Переход в объект с витрины {: #goto-showcase-record }

Для того, чтобы по кнопке можно было перейти из карточки товара на витрине на форму объекта, введите следующее выражение:

```cs

using System; 
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext)
    { 
                    var objectid = userCommandContext.ObjectIds[0];
        var result = new UserCommandResult()
        {

            Success = true,
            Messages =  null,

            ResultType = UserCommandResultType.Navigate ,
            NavigationResult = new UserCommandNavigationResult
            {
                ContainerId = "oa.8",
                ObjectId = objectid,
                Context = ContextType.Record
            }
        };
        return result;
    }
}

```

где:

***oa.8*** — ИД шаблона записи, где находятся объекты из витрины.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
