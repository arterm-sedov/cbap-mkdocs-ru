---
title: Изменение переиспользуемой переменной по кнопке
kbId: 5005

tags:
    - C#
    - скрипт
    - C#-скрипт
    - пример скрипта
hide: tags
---

# Изменение переиспользуемой переменной по кнопке {: #button-change-variable }

Для того чтобы можно было по кнопке изменять переиспользуемую переменную , создайте кнопку типа «Скрипт» в текущем Шаблоне записи и введите следующее выражение:

```cs
 
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;
public class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext)
    {
var objectId = userCommandContext.ObjectIds.FirstOrDefault();    
var temp = (decimal)Api.Solution.SolutionVariableService.GetValue("svar.1");
Api.Solution.SolutionVariableService.SetValue("svar.1", temp+1);
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
                    Text = "Переиспользуемая переменная инкрементирована"
                    }
            }
        };
        return result;
   
    }
}

```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| `svar.1` | ID переиспользуемой переменной, которую нужно изменить. В данном примере это число. |
| `+1` | Число, которое добавляется к значению переиспользуемой переменной. |
| `Переиспользуемая переменная инкрементирована` | Сообщение, которое отобразится при успешном выполнении скрипта. |

!!! note "Обработка записей"

    Скрипт работает только с одной записью. Если в таблице выбрано несколько записей, скрипт обработает первую из них. Для обработки нескольких записей доработайте скрипт.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
