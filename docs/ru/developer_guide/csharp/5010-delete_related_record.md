---
title: Удаление связанного объекта при выполнении условия
kbId: 5010
---

# Удаление связанного объекта при выполнении условия

Для того, чтобы можно было в процессе удалять связанный объект/ы при определенном условии (в данной статье рассмотрено условие, если значение в атрибуте с типом данных «Число» в связанном объекте/ах равно нулю), введите следующее выражение:

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
try
{
var id = context.BusinessObjectId;
var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new []{id}, new[]{"Link"});
var deletearray = data[id]["Link"] as object[];

foreach(var i in deletearray)
{
try
{
var atr = Api.TeamNetwork.ObjectService.GetPropertyValues(new []{i.ToString()}, new[]{"Qty "});
var val = atr[i.ToString()]["Qty "];

if(int.Parse(val.ToString()) == 0)
{
Api.TeamNetwork.ObjectService.Delete(i.ToString());
}
}
catch{}
}
}
catch
{}
    }
}

```

**где:**

***Link*** — системное имя атрибута с типом данных «Запись» в текущем шаблоне записи;

***Qty*** — системное имя атрибута с типом данных «Число» в связанном шаблоне записи.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
