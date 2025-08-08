---
title: Adding users to a group
kbId: 2095
---


# Adding users to a group

In order to enable a process to add a user or users to a specific system group (for example, to manage the role model), enter the following expression:

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
string[] OA = new string[] {
"Clients"
};
string[] OP = new string[] {
"Manager"
};
string[] GROUP = new string[] {
"group.28"
};

for(int j = 0; j < GROUP.Length; j++)
{
var group = GROUP[j];
var old_users = Api.Base.AccountGroupService.Get(group);
Api.Base.AccountGroupService.ExcludeMembers(group, old_users.Users);

var my_list = Api.TeamNetwork.ObjectService.ListWithAlias(OA[j]);
foreach (var i in my_list)
{
var data = i as Dictionary<string,object>;
data.TryGetValue(OP[j], out object obj);
if (obj == null)
{
continue;
}

if (obj is string)
{
Api.Base.AccountGroupService.IncludeMembers(group, new List<string>(){ obj.ToString() }); ÿ
}
else
{
var accounts = obj as object[];
var accountsIds = accounts.Select(x => x.ToString());
Api.Base.AccountGroupService.IncludeMembers(group, accountsIds);
}
}
}
}
}

```

**where:**

***Clients*** — system name of the record template;

***Manager*** — system name of the attribute of the "Account" data type in the specified record template;

***group.28*** — ID of a system group.

This script, when called, firstly removes all users from the group, and then iterates through all records in the specified record template and adds users from the specified attribute to the group, thus updating the composition of the system group.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
