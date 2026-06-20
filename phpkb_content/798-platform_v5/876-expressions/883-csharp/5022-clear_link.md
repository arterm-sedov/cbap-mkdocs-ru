---
title: 'Очистка ссылки'
kbId: 5022
url: 'https://kb.comindware.ru/article.php?id=5022'
updated: '2026-06-20 20:26:33'
---

# Очистка ссылки

Для того чтобы на входе на задачу очистить ссылку, введите следующее выражение:

```
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
    
    Dictionary<string, object> d = new Dictionary<string, object>();
    d["SoglasovanoLink"] = null;
    Api.TeamNetwork.ObjectService.EditWithAlias("StoreOpeningLocation", context.BusinessObjectId, d);
  }
}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `SoglasovanoLink` | Системное имя атрибута типа «**Запись**». При необходимости можно указать несколько таких атрибутов в столбец. |
| `Location` | Системное имя текущего шаблона записи. |

Очистка ссылки

Этот скрипт не делает ссылку `EMPTY`, а заменяет её на пустое значение. Если требуется сделать ссылку полностью пустой, создайте в текущем шаблоне записи ссылку на любой шаблон и при входе на задачу заполните нужную ссылку вновь созданной, которая всегда будет пустой.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
