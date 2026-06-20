---
title: 'Запуск глобальной функции из кнопки'
kbId: 5203
url: 'https://kb.comindware.ru/article.php?id=5203'
updated: '2026-06-20 17:34:07'
---

# Запуск глобальной функции из кнопки

Для того чтобы запустить глобальную функцию по кнопке, введите следующее выражение:

```
using System; 
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext)
    {     
          var CurrentObjectid = userCommandContext.ObjectIds[0];
        var CurrentObjectData = Api.TeamNetwork.ObjectService.Get(CurrentObjectid);
        var Gosnomer = CurrentObjectData["op.11"].ToString();
    var bo = Api.TeamNetwork.GlobalFunctionService.ExecuteByAlias("Systemsolution", "Poisk", new Dictionary<string, object>()('Nomer', Undefined));
    Api.TeamNetwork.ObjectService.EditWithAlias("Kartochkivyzovov", userCommandContext.ObjectIds[0], bo);

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
          Text = "VIN найден успешно"
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
| `op.11` | ID атрибута в текущем шаблоне записи, значение которого передаётся на вход глобальной функции. |
| `Systemsolution` | Системное имя текущего приложения. |
| `Poisk` | Системное имя глобальной функции. |
| `Nomer` | Переменная в шаблоне сообщения на входе. |
| `Kartochkivyzovov` | Системное имя текущего шаблона записи, из которого вызывается кнопка. |
| `VIN найден успешно` | Текст сообщения, которое отобразится пользователю при успешном выполнении скрипта. |