---
title: 'Кнопка «Моя компания»'
kbId: 5023
url: 'https://kb.comindware.ru/article.php?id=5023'
updated: '2026-06-20 20:26:33'
---

# Кнопка «Моя компания»

Для того чтобы поместить на боковую панель навигации ссылку на компанию пользователя, создайте кнопку с операцией «**C#-скрипт**» в текущем Шаблоне записи и введите следующее выражение:

```
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;

public class Script
{

    public static UserCommandResult Main(UserCommandContext userCommandContext)
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

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Kontaktyklientov` | Системное имя шаблона аккаунта, в котором хранятся контактные лица клиентов. |
| `company` | Системное имя атрибута типа «**Запись**» в шаблоне аккаунта. Атрибут ссылается на текущий шаблон записи. |
| `oa.4` | ID текущего шаблона записи. |