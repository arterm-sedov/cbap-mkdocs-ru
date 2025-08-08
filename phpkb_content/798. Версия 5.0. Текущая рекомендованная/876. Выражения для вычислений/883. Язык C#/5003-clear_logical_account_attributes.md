---
title: Очистка значений атрибутов типа Логический и Пользователь
kbId: 5003
---

# Очистка значений атрибутов типа Логический и Пользователь

Для того, чтобы по операции можно было очистить атрибуты типа Логический и Пользователь (например, очистить флаги и ответственных), введите следующее выражение:

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
        foreach (var objectId in userCommandContext.ObjectIds)
        {
            var editData = new Dictionary<string, object>();
            editData.Add ("noCoordinatorFlag", null);
            editData.Add ("coordinator", null);
            editData.Add ("substitutes", null);
            editData.Add ("dateFrom", null);                                    
            editData.Add ("taskFlag", null);
            editData.Add ("assigmentCoordinatorsLink", null);
            editData.Add ("primaryAssignFlag", null);
            
            Api.TeamNetwork.ObjectService.EditWithAlias("indsOwners", objectId, editData);
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
                    Text = "Данные успешно обновлены"
                }
            }
        };
        return result;
    }
}

```

**где:**

**indsOwners** - системное имя текущего Шаблона записи;

**noCoordinatorFlag, coordinator, substitutes, dateFrom, taskFlag, assigmentCoordinatorsLink, primaryAssignFlag** - системные имена атрибутов текущей записи, которые нужно очистить;

**Данные успешно обновлены** - сообщение в случае успеха.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
