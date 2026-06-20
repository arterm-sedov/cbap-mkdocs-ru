---
title: 'Кнопка «Мой профиль»'
kbId: 5006
url: 'https://kb.comindware.ru/article.php?id=5006'
updated: '2026-06-20 18:06:23'
---

# Кнопка «Мой профиль»

Для того чтобы поместить на боковую панель навигации ссылку на профиль пользователя, создайте кнопку с операцией «**C#-скрипт**» в шаблоне аккаунтов и введите следующее выражение:

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
        var result = new UserCommandResult()
        {
            Success = true,
            ResultType = UserCommandResultType.Navigate,
            NavigationResult = new UserCommandNavigationResult
            {
                ContainerId = "aa.1",
                ObjectId = userCommandContext.CurrentUserId,
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
| `aa.1` | ID шаблона аккаунтов. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
