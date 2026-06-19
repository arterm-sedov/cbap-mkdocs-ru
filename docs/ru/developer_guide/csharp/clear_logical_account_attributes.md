---
title: Очистка значений атрибутов типа Логический и Пользователь
kbId: 5003

tags:
    - C#
    - скрипт
    - C#-скрипт
    - пример скрипта
hide: tags
---

# Очистка значений атрибутов типа Логический и Пользователь {: #clear-logical-account-attributes }

Для того чтобы по кнопке можно было очистить атрибуты типа Логический и Пользователь (например, очистить флаги и ответственных), введите следующее выражение:

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

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| `indsOwners` | Системное имя текущего шаблона записи. |
| `noCoordinatorFlag`, `coordinator`, `substitutes`, `dateFrom`, `taskFlag`, `assigmentCoordinatorsLink`, `primaryAssignFlag` | Системные имена атрибутов текущей записи, которые нужно очистить. |
| `Данные успешно обновлены` | Сообщение, которое отобразится при успешном выполнении скрипта. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
