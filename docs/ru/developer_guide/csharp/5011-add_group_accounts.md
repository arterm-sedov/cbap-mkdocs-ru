---
title: Добавление пользователей в группу
kbId: 5011
---

# Добавление пользователей в группу

Для того, чтобы в рамках процесса можно было добавить пользователя или пользователей в определенную системную группу (например, для управления ролевой моделью), введите следующее выражение:

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
"Kontragenty"
};
string[] OP = new string[] {
"Podpisant"
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

**где:**

***Kontragenty*** — системное имя шаблона записи;

***Podpisant*** — системное имя атрибута с типом данных «Аккаунт» из шаблона записи ***Kontragenty***, хранящее пользователя;

***group.28*** — ИД системной группы, куда необходимо добавить пользователя из поля ***Podpisant***.

Данный скрипт при вызове сначала удаляет всех пользователей из группы, а затем проходит по всем записям в указанном шаблоне записи и добавляет пользователей из указанного атрибута в группу, т. о., обновляя состав системной группы.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
