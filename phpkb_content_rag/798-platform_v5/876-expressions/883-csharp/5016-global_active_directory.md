---
title: 'Глобальная функция для обращения в Active Directory'
kbId: 5016
url: 'https://kb.comindware.ru/article.php?id=5016'
updated: '2026-06-20 18:06:23'
---

# Глобальная функция для обращения в Active Directory

Для того чтобы обратиться в Active Directory и получить оттуда какую-либо информацию, введите следующее выражение:

```
using System;
using System.Collections.Generic;

// class name should remain "Script"
public static partial class Script {

    // запрашивает данные пользователя из Active Directory по адресу эл. почты
    public static Dictionary<string, object> QueryAD(string text)
    {
        //создаём подключение к Active Directory
        System.DirectoryServices.DirectoryEntry entry = new System.DirectoryServices.DirectoryEntry("LDAP://url_сервера_AD", "логин", "пароль");

        //создаём поисковый запрос
        System.DirectoryServices.DirectorySearcher mySearcher = new System.DirectoryServices.DirectorySearcher(entry);

        //фильтруем по нужному параметру
        mySearcher.Filter = ($"(MAIL={text})");
        var result = new Dictionary<string, object>();

        //выбираем атрибуты, которые требуется вернуть
        mySearcher.PropertiesToLoad.Add("mail");
        mySearcher.PropertiesToLoad.Add("cn");
        var temp = mySearcher.FindOne();

        //добавляем в словарь результата
        result.Add("name", temp.GetDirectoryEntry().InvokeGet("cn"));
        return result;
}
}
```