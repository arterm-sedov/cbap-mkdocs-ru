---
title: Изменение e-mail у всех пользователей в системе
kbId: 5019
---

# Изменение e-mail у всех пользователей в системе

Для того, чтобы поменять e-mail у всех пользователей в системе, введите следующее выражение:

```

using System; 
using System.Collections.Generic; 
using System.Linq; 
using System.Text.RegularExpressions; 
using Comindware.Data.Entity; 
using Comindware.TeamNetwork.Api.Data.UserCommands;

class Script 
{ 
    public static UserCommandResult Main(UserCommandContext userCommandContext,        Comindware.Entities entities) 
    { 
        var accounts = Api.Base.AccountService.List(); 
            foreach (var account in accounts) 
            { 
               account.Mbox = account.Mbox + "test"; 
               Api.Base.AccountService.Edit(account); 
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
                    Text = "Email changed!" 
                    } 
                } 
            }; 
            return result; 
    } 
}

```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
