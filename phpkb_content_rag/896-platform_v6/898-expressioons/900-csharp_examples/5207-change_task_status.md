---
title: 'Изменение статуса и завершение пользовательской задачи'
kbId: 5207
url: 'https://kb.comindware.ru/article.php?id=5207'
updated: '2026-06-16 19:14:49'
---

# Изменение статуса и завершение пользовательской задачи

Для того чтобы по кнопке можно было менять статус записи и завершать связанную с ней пользовательскую задачу, введите следующее выражение:

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

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Отменена` | Значение, на которое нужно поменять статус. |
| `ApprovalStatus` | Системное имя атрибута типа «**Ссылка**» в текущем шаблоне записи на шаблон записи, где хранятся значения статусов. |
| `SingleApproval` | Системное имя текущего шаблона записи. |
| `Application disapproved` | Текст сообщения, которое отобразится пользователю после успешного выполнения скрипта. |

**Примечание:** скрипт работает только с одной записью (выбирает первую запись, если в таблице было выбрано несколько элементов). Для обработки нескольких записей скрипт нужно дописать.