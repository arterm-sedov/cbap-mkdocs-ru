---
title: Deleting a related object when a condition is met
kbId: 2099
---


# Deleting a related object when a condition is met

In order to delete the associated object in the context of a process if a certain condition is met (in this article the condition is the following: the value in the attribute with the data type "Number" in the associated object is zero), enter the following expression:

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
var deleteid = data[id]["Link"].ToString();

var atr = Api.TeamNetwork.ObjectService.GetPropertyValues(new []{data[id]["Link"] as string}, new[]{"Qty"});
var val = atr[data[id]["Link"] as string]["Qty"];

if(int.Parse(val.ToString()) == 0)
{
Api.TeamNetwork.ObjectService.Delete(deleteid);
}
}
catch
{}
}
}

```

**where:**

***Link***— system name of the attribute with the "Record" data type in the current record template;

***Qty***— system name of the attribute with the "Number" data type in the associated record template.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
