---
title: Изменение статуса и завершение пользовательской задачи
kbId: 5004
---

# Изменение статуса и завершение пользовательской задачи

Для того, чтобы по кнопке можно было менять статус записи и завершать связанную с ней пользовательскую задачу, введите следующее выражение:

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
        var disapprovedStatus = entities.ApplicationStatus.Where(x => x.Name == "Отменена").Select(x => x.id).FirstOrDefault();
        var data = new Dictionary<string, object>
        {
            { "ApprovalStatus", disapprovedStatus }
        };
        Api.TeamNetwork.ObjectService.EditWithAlias("SingleApproval", objectId, data);
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
                    Text = "Application disapproved"
                    }
            }
        };
        var activeTask = Api.Process.ProcessObjectService.GetReferencedTasks(objectId).Where(x => x.Status == UserTaskStatus.InProgress).FirstOrDefault().Id;
        Api.TeamNetwork.UserTaskService.Complete(activeTask, true);
        return result;
    }
}

```

**где:**

**Отменена** - значение, на которое нужно поменять статус;

**ApprovalStatus** - системное имя атрибута типа Ссылка в текущем Шаблоне записи на Шаблон записи, где хранятся значения статусов;

**SingleApproval** - системное имя текущего Шаблона записи;

**Application disapproved** - текст сообщения, которое высветится пользователю в случае успешного исполнения скрипта.

**Примечание :** скрипт работает только с одной записью (выбирает первую запись, если на списке было выбрано несколько элементов). Для обработки нескольких записей скрипт нужно дописать.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
