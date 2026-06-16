---
title: 'Переход в объект с витрины'
kbId: 5187
url: 'https://kb.comindware.ru/article.php?id=5187'
updated: '2026-06-16 19:14:53'
---

# Переход в объект с витрины

Для того чтобы по кнопке можно было перейти из карточки товара на витрине на форму объекта, введите следующее выражение:

```
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

**Здесь:**

| Значение | Описание |
| --- | --- |
| `oa.8` | ID шаблона записи, в котором находятся объекты из витрины. |