---
title: Запуск глобальной функции из операции
kbId: 5024
---

# Запуск глобальной функции из операции

Для того, чтобы запустить глобальную функцию по кнопке, введите следующее выражение:

```

using System; 
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {     
          var CurrentObjectid = userCommandContext.ObjectIds[0];
        var CurrentObjectData = Api.TeamNetwork.ObjectService.Get(CurrentObjectid);
        var Gosnomer = CurrentObjectData["op.11"].ToString();
    var bo = Api.TeamNetwork.GlobalFunctionService.ExecuteByAlias("Systemsolution", "Poisk", new Dictionary<string, object>(){{"Nomer", Gosnomer}});
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

**где:**

**op.11 -** ИД атрибута в текущем Шаблоне записи, которое передается на вход ГФ;

**Systemsolution** – системное имя текущего Бизнес-приложения;

**Poisk** – системное имя Глобальной функции;

**Nomer** - переменная в шаблоне сообщения на входе;

**Kartochkivyzovov** - имя текущего шаблона записи, откуда вызывается операция;

**VIN найден успешно** - текст сообщения, которое высветится пользователю в случае успешного исполнения скрипта.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
