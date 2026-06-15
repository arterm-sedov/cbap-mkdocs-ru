---
title: Кнопка «Мой профиль»
kbId: 5006
tags:
    - C#
    - скрипт
    - C#-скрипт
    - пример скрипта
hide: tags
---

# Кнопка «Мой профиль» {: #example-csharp-my-profile-button }

Для того чтобы разместить на боковую панель навигации ссылку на профиль пользователя, создайте кнопку c операцией C#-скрипт в шаблоне аккаунтов и введите следующее выражение:

```cs

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

**где:**

**aa.1**   = ID шаблона аккаунтов

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
