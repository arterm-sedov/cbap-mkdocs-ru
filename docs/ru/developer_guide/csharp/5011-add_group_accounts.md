---
title: Добавление пользователей в группу
kbId: 5189

tags:
    - C#
    - скрипт
    - C#-скрипт
    - пример скрипта
hide: tags
---

# Добавление пользователей в группу {: #add-group-accounts }

Для того чтобы в рамках процесса можно было добавить пользователя или пользователей в определенную системную группу (например, для управления ролевой моделью), введите следующее выражение:

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
        string[] OA = new string[] {
            "Kontragenty"
        };
        string[] OP = new string[] {
            "Podpisant"
        };
        string[] GROUP = new string[] {
            "group.28"
        };

        for (int j = 0; j < GROUP.Length; j++)
        {
            var group = GROUP[j];
            var old_users = Api.Base.AccountGroupService.Get(group);
            Api.Base.AccountGroupService.ExcludeMembers(group, old_users.Users);

            var my_list = Api.TeamNetwork.ObjectService.ListWithAlias(OA[j]);
            foreach (var i in my_list)
            {
                var data = i as Dictionary<string, object>;
                data.TryGetValue(OP[j], out object obj);
                if (obj == null)
                {
                    continue;
                }

                if (obj is string)
                {
                    Api.Base.AccountGroupService.IncludeMembers(group, new List<string>() { obj.ToString() });
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

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| `Kontragenty` | Системное имя шаблона записи. |
| `Podpisant` | Системное имя атрибута типа «**Аккаунт**» в шаблоне записи `Kontragenty`. В этом атрибуте хранится пользователь, которого нужно добавить в группу. |
| `group.28` | ID системной группы, в которую нужно добавить пользователя из атрибута `Podpisant`. |

## Логика работы скрипта {: #add-group-accounts_script_logic }

При вызове скрипт сначала удаляет всех пользователей из группы, затем проходит по всем записям указанного шаблона записи и добавляет в группу пользователей из указанного атрибута. Так скрипт обновляет состав системной группы.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
