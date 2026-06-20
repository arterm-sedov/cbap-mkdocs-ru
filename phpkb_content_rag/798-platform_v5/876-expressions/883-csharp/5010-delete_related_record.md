---
title: 'Удаление связанного объекта при выполнении условия'
kbId: 5010
url: 'https://kb.comindware.ru/article.php?id=5010'
updated: '2026-06-20 18:06:24'
---

# Удаление связанного объекта при выполнении условия

Для того чтобы можно было в процессе удалять связанный объект/ы при определенном условии (в данной статье рассмотрено условие, если значение в атрибуте типа «**Число**» в связанном объекте/ах равно нулю), введите следующее выражение:

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
        try
        {
            var id = context.BusinessObjectId;
            var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new[] { id }, new[] { "Link" });
            var deletearray = data[id]["Link"] as object[];

            foreach (var i in deletearray)
            {
                try
                {
                    var atr = Api.TeamNetwork.ObjectService.GetPropertyValues(new[] { i.ToString() }, new[] { "Qty " });
                    var val = atr[i.ToString()]["Qty "];

                    if (int.Parse(val.ToString()) == 0)
                    {
                        Api.TeamNetwork.ObjectService.Delete(i.ToString());
                    }
                }
                catch { }
            }
        }
        catch { }
    }
}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Link` | Системное имя атрибута типа «**Запись**» в текущем шаблоне записи. |
| `Qty` | Системное имя атрибута типа «**Число**» в связанном шаблоне записи. |