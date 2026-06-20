---
title: 'Изменение статуса и завершение пользовательской задачи'
kbId: 5207
url: 'https://kb.comindware.ru/article.php?id=5207'
updated: '2026-06-20 17:34:07'
---

# Изменение статуса и завершение пользовательской задачи

Для того чтобы по кнопке можно было менять статус записи и завершать связанную с ней пользовательскую задачу, введите следующее выражение:

```
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

public class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext)
    {
        // ID целевой записи, переданной в контексте кнопки
        var objectId = userCommandContext.ObjectIds.FirstOrDefault();

        // Получаем статус приложения «Отменена» из справочника ApplicationStatus
        var disapprovedStatusData = Api.TeamNetwork.ObjectService.Get("ApplicationStatus", new Dictionary<string,object>('Name', 'Отменена'), null, new []{"id"});
        // Извлекаем ID найденного статуса; если статус не найден — присваиваем null
        var disapprovedStatus = disapprovedStatusData.TryGetValue("id", out object statusObject) && statusObject != null ? statusObject.ToString() : null;

        // Формируем данные для обновления: в атрибут ApprovalStatus запишем новый статус
        var data = new Dictionary<string, object>
        {
            { "ApprovalStatus", disapprovedStatus }
        };
        // Сохраняем новое значение статуса в целевой записи
        Api.TeamNetwork.ObjectService.EditWithAlias("SingleApproval", objectId, data);

        // Формируем результат выполнения команды
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
                    Text = "Application disapproved"  // сообщение пользователю об успехе
                }
            }
        };

        // Находим активную (в работе) пользовательскую задачу, связанную с записью
        var activeTask = Api.Process.ProcessObjectService.GetReferencedTasks(objectId)
            .Where(x => x.Status == UserTaskStatus.InProgress)
            .FirstOrDefault().Id;
        // Завершаем найденную задачу
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

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
