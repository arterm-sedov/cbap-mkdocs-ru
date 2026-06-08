---
title: 'Изменение переиспользуемой переменной по операции'
kbId: 5005
url: 'https://kb.comindware.ru/article.php?id=5005'
updated: '2022-02-18 06:28:27'
---

# Изменение переиспользуемой переменной по операции

Для того, чтобы можно было по кнопке изменять переиспользуемую переменную , создайте операцию типа Скрипт в текущем Шаблоне записи и введите следующее выражение:

```
 

using System;

using System.Collections.Generic;

using System.Linq;

using Comindware.Data.Entity;

using Comindware.TeamNetwork.Api.Data.UserCommands;

using Comindware.TeamNetwork.Api.Data;

public class Script

{

    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)

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

**где:**

**svar.1** - ИД переиспользуемой переменной, которую будем изменять (в данном случае, это число);

**+1** - к переиспользуемой переменной добавляем число;

**"Переиспользуемая переменная инкрементирована"** - сообщение в случае успеха.

**Примечание :** скрипт работает только с одной записью (выбирает первую запись, если на списке было выбрано несколько элементов). Для обработки нескольких записей скрипт нужно дописать.