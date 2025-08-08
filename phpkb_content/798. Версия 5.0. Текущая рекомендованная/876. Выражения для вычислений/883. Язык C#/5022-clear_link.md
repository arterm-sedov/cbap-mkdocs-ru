---
title: Очистка ссылки
kbId: 5022
---

# Очистка ссылки

Для того, чтобы на входе на задачу очистить ссылку, введите следующее выражение:

```

 

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
    public static void Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities)
    {
    
    Dictionary<string, object> d = new Dictionary<string, object>();
    d["SoglasovanoLink"] = null;
    Api.TeamNetwork.ObjectService.EditWithAlias("StoreOpeningLocation", context.BusinessObjectId, d);
  }
}

```

**где:**

**SoglasovanoLink**  = системное имя атрибута-ссылка (при необходимости можно указать в столбец несколько ссылок);

**Location**  = системное имя текущего шаблона записи.

Данное выражение не сделает ссылку EMPTY, а всего лишь заменит её на какое-то пустое значение. Если Вы хотите сделать ссылку полностью пустой, создайте в текущем шаблоне записи ссылку на любой из шаблонов и при входе на задачу заполните нужную Вам ссылку вновь созданной (которая всегда будет пустой).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
