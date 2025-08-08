---
title: Глобальная функция для обращения в Active Directory
kbId: 5016
---

# Глобальная функция для обращения в Active Directory

Для того чтобы обратиться в Active Directory и получить оттуда какую-либо информацию, введите следующее выражение:

```

using System;
using System.Collections.Generic;

// class name should remain "Script"
public static partial class Script {

    // method name should remain "Main"
    public static Dictionary<string, object> begaemvAD(string tekst)
    {

 

//создаём подключение к ад
        System.DirectoryServices.DirectoryEntry entry = new System.DirectoryServices.DirectoryEntry("LDAP://сервер ад", "логин", "пароль");

//создаём серчер
            System.DirectoryServices.DirectorySearcher mySearcher = new System.DirectoryServices.DirectorySearcher(entry);

//фильтруем по нужному параметру
            mySearcher.Filter = ($"(MAIL={tekst})");
            var result = new Dictionary<string, object>();

//выбираем проперти, которые хотим вернуть
            mySearcher.PropertiesToLoad.Add("mail");
            mySearcher.PropertiesToLoad.Add("cn");
            var temp = mySearcher.FindOne();

//добавляем в словарь результата
            result.Add("name", temp.GetDirectoryEntry().InvokeGet("cn"));
            return result;
    }
}

```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
