---
title: Очистка атрибута типа Пользователь в процессе
kbId: 5193

tags:
    - C#
    - скрипт
    - C#-скрипт
    - пример скрипта
hide: tags
---

# Очистка атрибута типа Пользователь в процессе {: #clear-account-attribute }

Для того, чтобы в рамках процесса можно было очистить атрибут типа Пользователь (например, очистить ответственного), введите следующее выражение:

```cs

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
public static void Main(Comindware.Process.Api.Data.ScriptContext context)
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

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
