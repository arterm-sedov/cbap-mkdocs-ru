---
title: 'Кнопка «Моя компания»'
kbId: 5023
url: 'https://kb.comindware.ru/article.php?id=5023'
updated: '2022-02-18 06:29:33'
---

# Кнопка «Моя компания»

Для того, чтобы разместить на боковую панель навигации ссылку на компанию пользователя, создайте операцию типа Скрипт в текущем Шаблоне записи и введите следующее выражение:

```
 

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;

public class Script
{

    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
        var user = Api.TeamNetwork.ObjectService.GetWithAlias("Kontaktyklientov", userCommandContext.CurrentUserId);
        var error = user == null ? "У пользователя нет компании" : null;
        var companyId = error == null ? user["company"] as string : null;
        var result = new UserCommandResult()
        {
            Success = error == null,
            Messages = error == null ? null : new[]
            {
                new UserCommandMessage
                {
                    Severity = SeverityLevel.Normal,
                    Text = error
                }
            },
            ResultType = error == null ? UserCommandResultType.Navigate : UserCommandResultType.Notificate,
            NavigationResult = new UserCommandNavigationResult
            {
                ContainerId = "oa.4",
                ObjectId = companyId,
                Context = ContextType.Record
            }
        };
        return result;
    }
}
```

**где:**

**Kontaktyklientov** - системное имя Шаблона пользователя, где хранятся все контактные лица клиентов в системе;

**company** - системное имя атрибута типа Ссылка в Шаблоне пользователя, ссылающийся на текущий Шаблон записи;

**oa.4** - ИД текущего Шаблона записи.