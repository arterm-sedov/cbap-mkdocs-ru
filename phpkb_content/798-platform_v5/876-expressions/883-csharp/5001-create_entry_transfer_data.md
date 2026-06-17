---
title: 'Создание записи и передача данных из выбранного объекта'
kbId: 5001
url: 'https://kb.comindware.ru/article.php?id=5001'
updated: '2026-06-17 14:09:48'
---

# Создание записи и передача данных из выбранного объекта

Для того чтобы по кнопке можно было по выбранному объекту/ам создать запись в каком-либо Шаблоне записи и передать туда какие-либо данные, введите следующее выражение:

```
using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;

public class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext)
    {
        var currentObjectid = userCommandContext.ObjectIds;
        foreach(var id in currentObjectid)
        {
            var request = Api.TeamNetwork.ObjectService.Get(id);
            object descriptionObject;
            request.TryGetValue("op.93", out descriptionObject);
            object name;
            request.TryGetValue("op.92", out name);
            var propertyDictionary = new Dictionary<string, object>();
            propertyDictionary.Add("Description", descriptionObject);
            propertyDictionary.Add("title", name);
            Api.TeamNetwork.ObjectService.CreateWithAlias("Issue", propertyDictionary);
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
                    Text = "Успешно"
                }
            }
        };
        return result;
    }
}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `op.93` | ID атрибута в текущем шаблоне записи, значение которого нужно передать в новую запись. |
| `op.92` | ID атрибута в текущем шаблоне записи, значение которого нужно передать в новую запись. |
| `Issue` | Системное имя шаблона записи, в котором будут создаваться новые записи. |
| `Description` | Системное имя атрибута в шаблоне записи `Issue`, в который будет передаваться значение из `op.93`. |
| `title` | Системное имя атрибута в шаблоне записи `Issue`, в который будет передаваться значение из `op.92`. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
