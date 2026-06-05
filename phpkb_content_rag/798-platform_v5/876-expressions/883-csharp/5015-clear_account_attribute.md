---
title: 'Очистка атрибута типа Пользователь в процессе'
kbId: 5015
url: 'https://kb.comindware.ru/article.php?id=5015'
updated: '2022-02-18 06:29:57'
---

# Очистка атрибута типа Пользователь в процессе

Для того, чтобы в рамках процесса можно было очистить атрибут типа Пользователь (например, очистить ответственного), введите следующее выражение:

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
var data = new Dictionary<string, object>
{
{"op.156", null}
};
Api.TeamNetwork.ObjectService.Edit(context.BusinessObjectId, data);
}
}
```

**где:**

**op.156** - ИД атрибута типа Пользователь, который нужно очистить.