---
title: 'Изменение статусов в коллекции и завершение пользовательской задачи'
kbId: 5199
url: 'https://kb.comindware.ru/article.php?id=5199'
updated: '2026-06-16 19:15:15'
---

# Изменение статусов в коллекции и завершение пользовательской задачи

Для того чтобы по кнопке можно было менять статус записей в коллекции в зависимости от определенного условия и завершать связанную с основной записью пользовательскую задачу, введите следующее выражение:

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
        var data = Api.TeamNetwork.ObjectService.GetWithAlias("Register", objectId);
        object[] Applications = data["Applications"] as object[];
        var allApplications = new List<string>();

        foreach (var app in Applications)
        {
            var apps = app as string;
            allApplications.Add(apps);
        }

        var LevelRef = data["RegisterLevel"];
        var Level = Api.TeamNetwork.ObjectService.GetWithAlias("RegisterLevels", LevelRef as string);
        var LevelNum = (decimal)Level["Level"];

        if (LevelNum == 1)
        {
            var approvedStatus = entities.ApplicationStatus.Where(x => x.Name == "Согласована в первом реестре").Select(x => x.id).FirstOrDefault();
            foreach(var a in allApplications) 
            {
                var data1 = new Dictionary<string, object>
                {
                    { "Status", approvedStatus}
                };
                Api.TeamNetwork.ObjectService.EditWithAlias("Application", a, data1);
            }
        }
        else
        {
            var approvedStatus = entities.ApplicationStatus.Where(x => x.Name == "Согласована во втором реестре").Select(x => x.id).FirstOrDefault();
            foreach(var a in allApplications) 
            {
                var data1 = new Dictionary<string, object>
                {
                    { "Status", approvedStatus}
                };
                Api.TeamNetwork.ObjectService.EditWithAlias("Application", a, data1);
            }
        }
        
        var result = new UserCommandResult
        {
            Success = true,
            Commited = true,
            ResultType = UserCommandResultType.Navigate,
            NavigationResult = new UserCommandNavigationResult
            {
                Title = "Register",
                ObjectId = objectId,
                ContainerId = "oa.13",
                Context = ContextType.Record 
            },
            Messages = new[]
            {
                new UserCommandMessage
                {
                    Severity = SeverityLevel.Normal,
                    Text = "Register approved"
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
| `Register` | Системное имя текущего шаблона записи. |
| `Applications` | Системное имя атрибута типа «**Коллекция**» в текущем шаблоне записи. |
| `RegisterLevel` | Системное имя атрибута типа «**Ссылка**» в текущем шаблоне записи для условия. |
| `RegisterLevels` | Системное имя шаблона записи, на который ссылается `RegisterLevel`, для условия. |
| `Level` | Системное имя атрибута типа «**Число**» в шаблоне записи `RegisterLevels` для условия. |
| `Согласована в первом реестре` / `Согласована во втором реестре` | Значение статуса для записи в коллекции, на которое нужно поменять статус при выполнении условия. |
| `Application` | Системное имя шаблона записи, на который ссылается `Applications`. |
| `Status` | Системное имя атрибута типа «**Ссылка**» в шаблоне записи `Application`, значение которого нужно поменять. |
| `oa.13` | ID текущего шаблона записи для навигации. |
| `Register approved` | Текст сообщения при успешном выполнении кнопки. |

Примечание

Скрипт работает только с одной записью (выбирает первую запись, если в таблице было выбрано несколько элементов). Для обработки нескольких записей скрипт нужно дописать.