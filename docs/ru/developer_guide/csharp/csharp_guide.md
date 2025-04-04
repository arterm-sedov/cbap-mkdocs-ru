---
title: Написание скриптов на языке C#
kbId: 4864
---

# Написание скриптов на языке C# {: #csharp_guide}

## Введение

Для расширения функциональности в ПО  **{{ productName }}** предусмотрены инструменты написания и использования скриптов на языке C#. ПО позволяет внедрять C#-скрипты при настройке различных сущностей и функций приложения.

## Возможности использования C#-скриптов

ПО позволяет использовать C#-скрипты при настройке следующих сущностей и функций:

- Шаблон любого типа → Кнопка → [Скрипт операции](#шаблон-любого-типа--кнопка--скрипт-операции)
- Шаблон процесса → Задача-выполнение сценария → [Скрипт задачи](#шаблон-процесса--задача-выполнение-сценария--скрипт-задачи)
- Шаблон процесса → Пользовательская задача → [Вычисление заголовка задачи](#шаблон-процесса--пользовательская-задача--вычисление-заголовка-задачи)
- Шаблон процесса → Пользовательская задача → [Вычисление исполнителей задачи](#шаблон-процесса--пользовательская-задача--вычисление-исполнителей-задачи)
- Шаблон процесса → Пользовательская задача → [Вычисление продолжительности задачи](#шаблон-процесса--пользовательская-задача--вычисление-продолжительности-задачи)
- Сценарий → [Изменение значений атрибутов скриптом](#сценарий--изменение-значений-атрибутов-скриптом)
- Сценарий → [Проверка результата скрипта](#сценарий--проверка-результата-выполнения-скрипта)
- Шаблон процесса → Развилка «или/или» → [Вычисление условий выбора потоков](#шаблон-процесса--развилка-илиили--вычисление-условий-выбора-потоков)
- Шаблон процесса → Конечное событие и промежуточное событие → [Вычисление продолжительности процесса](#шаблон-процесса--конечное-событие-и-промежуточное-событие--вычисление-продолжительности-процесса)
- Шаблон процесса → Конечное событие-отправка сообщения и промежуточное событие-отправка сообщения → Тип сообщения → [Вычисление экземпляра процесса, в который отправляется сообщение сообщения](#шаблон-процесса--конечное-событие-отправка-сообщения-и-промежуточное-событие-отправка-сообщения--тип-сообщения--вычисление-экземпляра-процесса-в-который-отправляется-сообщение)
- Шаблон процесса → Конечное событие-отправка сообщения и промежуточное событие-отправка сообщения → [Вычисление значения атрибута сообщения](#шаблон-процесса--конечное-событие-отправка-сообщения-и-промежуточное-событие-отправка-сообщения--вычисление-значения-атрибута-сообщения)

## Входные и выходные данные C#-скрипта

Скрипт оформляется как `public class` с предопределённым именем `Script`. При выполнении скрипта вызывается метод `public static Main` этого класса. Скрипт компилируется при сохранении настраиваемой сущности.

Перед компиляцией тело скрипта помещается в уникальное пространство имён (`namespace`) во избежание интерференции между скриптами. Для удобства разработчика в том же пространстве имён автоматически создаётся вспомогательный класс коротких синонимов для обращения к API вида:

``` cs
static class Api {
  public static Comindware.TeamNetwork.Api.PublicServices TeamNetwork;
  public static Comindware.Process.Api.IPublicServices Process;
  public static Comindware.Platform.Api.IPublicServices Base;
}
```

Если скомпилировать скрипт не удалось, выводятся предупреждение и детализированное описание ошибок компиляции в области «**Журнал действий и ошибок**» <i class="fal fa-flag">‌</i> в информационной панели.

Перекомпиляция и проверка её успешности происходят каждый раз при сохранении, проверке или публикации сущности, в которую внедрён скрипт.

### Описание скриптов для различных сущностей

#### Шаблон любого типа → Кнопка → Скрипт операции

**Заготовка скрипта**

``` cs
public class Script {
  public static UserCommandResult Main (UserCommandContext userCommandContext, Comindware.Entities entities) {
    // Тело скрипта
  }
}
```

**Входные данные**

``` cs
UserCommandContext userCommandContext {
  string[] ObjectIds, // массив ID выбранных записей в списке
           // (пустой массив, если записи не выбраны)
           // или массив из одного элемента с ID записи на форме
  string[] SelectedIds, // массив ID записей, выбранных в таблице на форме
           // (пустой массив, если записи не выбраны)
  string CurrentUserId, // ID аккаунта текущего пользователя
  string DocumentTemplateId, // ID шаблона, к которому относится команда
  dateTime CurrentRequestTime, // дата и время текущего запроса
  bool ExportAsPdf, // флаг экспорта в PDF
  string FileName, // имя файла при выгрузке данных по шаблону экспорта
  DatasetQuery Query // список, с которого произошел запуск операции
},
Comindware.Entities entities // используется для доступа к данным шаблонов записей
```

**Выходные данные**

``` cs
UserCommandResult {
  bool Success, // флаг успешного завершения операции
  bool Commited, // флаг необходимости коммита операции
  enum UserCommandResultType ResultType, // тип возвращаемого результата.
  // В зависимости от значения производятся действия:
      // DataChange — обновление данных
      // Notificate — сообщение пользователю
      // Navigate — переход на страницу
      // File — скачивание файла

  // набор данных для перехода на другую страницу
  UserCommandNavigationResult NavigationResult {
    string Title, // заголовок
    string ObjectId, // ID записи
    string ContainerId, // ID контейнера
    ContextType Context // тип отображения
      // Undefined, Void, Any, Task, Case, Record, Process, List, Form, Page, Container
  },

  // объект выгружаемого файла
  UserCommandFileResult File {
    string Name, // имя файла
    string Type,
    byte[] Content // тело файла
  },

  // сообщение об окончании операции
  UserCommandMessage[] Messages {
    enum Severity, // уровень важности сообщения
      // SeverityLevel (Critical, Fatal, Low, Major, None, Normal)
    string Text
  }
}
```

#### Шаблон процесса → Задача-выполнение сценария → Скрипт задачи

**Заготовка скрипта**

``` cs
public class Script {
   public static void Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities) {
     // Тело скрипта
  }
}
```

**Входные данные**

``` cs
Comindware.Process.Api.Data.ScriptContext context {
   string ProcessID,  // ID экземпляра процесса
   string BusinessObjectID,  // ID записи, связанной с экземпляром процесса
},
Comindware.Entities entities // используется для доступа к данным шаблонов записей
```

**Выходные данные**

``` cs
void
// Возвращаемые параметры отсутствуют
```

#### Шаблон процесса → Пользовательская задача → Вычисление заголовка задачи

**Заготовка скрипта**

``` cs
public class Script {
   public static string Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities) {
     // Тело скрипта
  }
}
```

**Входные данные**

``` cs
Comindware.Process.Api.Data.ScriptContext context {
  string ProcessID,  // ID экземпляра процесса
  string BusinessObjectID,  // ID записи, связанной с экземпляром процесса
},
Comindware.Entities entities // используется для доступа к данным шаблонов записей
```

**Выходные данные**

``` cs
string
// Заголовку задачи присваивается возвращённое строковое значение
```

#### Шаблон процесса → Пользовательская задача → Вычисление исполнителей задачи

**Заготовка скрипта**

``` cs
public class Script {
  public static IEnumerable<string> Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities) {
    // Тело скрипта
  }
}
```

**Входные данные**

``` cs
Comindware.Process.Api.Data.ScriptContext context {
  string ProcessID, // ID экземпляра процесса
  string BusinessObjectID // ID записи, связанной с экземпляром процесса
},
Comindware.Entities entities // используется для доступа к данным шаблонов записей
```

**Выходные данные**

``` cs
IEnumerable<string>
// Скрипт должен вернуть список ID аккаунтов


```

#### Шаблон процесса → Пользовательская задача → Вычисление продолжительности задачи

**Заготовка скрипта**

``` cs
public class Script  {
  public  static TimeSpan Main (Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities) {
    // Тело скрипта
  }
}
```

**Входные данные**

``` cs
Comindware.Process.Api.Data.ScriptContext context {
  string ProcessID, // ID экземпляра процесса
  string BusinessObjectID, // ID записи, связанной с экземпляром процесса
},
Comindware.Entities, // используется для доступа к данным шаблонов записей
```

**Выходные данные**

``` cs
TimeSpan
// Продолжительности задачи присваивается возвращённое значение длительности
```

#### Сценарий → Изменение значений атрибутов скриптом

**Заготовка скрипта**

``` cs
public class Script {
  public static string // string, int, decimal, dateTime, bool, TimeSpan или IEnumerable<string>
    Main(string ObjectID, [Comindware.Entities entities]) {
    // Тело скрипта
  }
}
```

**Входные данные**

``` cs
string ProcessID, // ID экземпляра процесса,
string ObjectID, // ID записи,
Comindware.Entities entities // необязательный аргумент, используется для доступа к данным шаблонов записей
```

**Выходные данные**

``` cs
string, int, decimal, dateTime, TimeSpan, bool, IEnumerable<string>
// Атрибуту присваивается возвращённое значение соответствующего типа
```

#### Сценарий → Проверка результата выполнения скрипта

**Заготовка скрипта**

``` cs
public class Script
{
    public static bool Main([Object fullObjectID])
    { 
        var ObjectID = fullObjectID.ToString().Replace("user.", "");
        // Тело скрипта
    }
}
```

**Входные данные**

``` cs
string fullObjectID // ID записи с префиксом, необязательный аргумент
```

**Выходные данные**

``` cs
bool
// В зависимости от результата выполения возвращается true или false
```

#### Шаблон процесса → Развилка «или/или» → Вычисление условий выбора потоков

**Заготовка скрипта**

``` cs
public class Script {
  public static bool Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities) {
    // Тело скрипта
  }
}
```

**Входные данные**

``` cs
Comindware.Process.Api.Data.ScriptContext context {
  string ProcessID, // ID экземпляра процесса
  string BusinessObjectID, // ID записи, связанной с экземпляром процесса
},
Comindware.Entities entities // используется для доступа к данным шаблонов записей
```

**Выходные данные**

``` cs
bool
// Если скрипт вернул true, токен идёт по этому потоку управления
```

#### Шаблон процесса → Конечное событие и промежуточное событие → Вычисление продолжительности процесса

**Заготовка скрипта**

``` cs
public class Script {
  public static TimeSpan Main (Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities) {
    // Тело скрипта
  }
}
```

**Входные данные**

``` cs
Comindware.Process.Api.Data.ScriptContext context {
  string ProcessID, // ID экземпляра процесса
  string BusinessObjectID, // ID записи, связанной с экземпляром процесса
},
Comindware.Entities entities // используется для доступа к данным шаблонов записей
```

**Выходные данные**

``` cs
TimeSpan
// Продолжительности процесса присваивается возвращённое значение длительности
```

#### Шаблон процесса → Конечное событие-отправка сообщения и промежуточное событие-отправка сообщения → Тип сообщения → Вычисление экземпляра процесса, в который отправляется сообщение

**Заготовка скрипта**

``` cs
public class Script {
  public static void Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities) {
  // Тело скрипта
  }
}
```

**Входные данные**

``` cs
Comindware.Process.Api.Data.ScriptContext context {
  string ProcessID, // ID экземпляра процесса
  string BusinessObjectID, // ID записи, связанной с экземпляром процесса
},
Comindware.Entities entities // используется для доступа к данным шаблонов записей
```

**Выходные данные**

``` cs
string
// Скрипт должен вернуть ID экземпляра процесса
```

#### Шаблон процесса → Конечное событие-отправка сообщения и промежуточное событие-отправка сообщения → Вычисление значения атрибута сообщения

**Заготовка скрипта**

``` cs
public class Script {
  public static string Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities) {
    // Тело скрипта
  }
}
```

**Входные данные**

``` cs
Comindware.Process.Api.Data.ScriptContext context {
  string ProcessID, // ID экземпляра процесса
  string BusinessObjectID // ID записи, связанной с экземпляром процесса
},
Comindware.Entities entities // используется для доступа к данным шаблонов записей
```

**Выходные данные**

``` cs
string, number, dateTime, TimeSpan, bool
// Атрибуту присваивается возвращённое строковое значение
```

## Пространство используемых библиотек

Во всех пользовательских C#-скриптах ПО позволяет подключать перечисленные ниже библиотеки и использовать их публичные классы.

### API для взаимодействия с {{ productName }}

- Comindware.Logics.Transaction
- Comindware.Data.Entity.ITransaction
- Comindware.Data.Entity.IEntitySet
- Comindware.Platform.Common
- Comindware.Logics
- Comindware.Data.Entity
- Comindware.Data.Api
- Comindware.Teamnetwork.Api
- Comindware.Process.Api
- Comindware.Platform.Api

### Системные библиотеки и классы .Net Framework

- netstandard — API-интерфейс .NET
- System.Runtime — основные примитивы, классы и базовые классы .NET
- mscorlib — базовые классы .NET
- System.Core — базовые классы .NET
- System.Xml — обработка XML- документов
- System.Xml.Linq — обработка XML-документов посредством LINQ to XML
- System — базовые классы .NET
- System.object — исходный базовый класс .NET
- System.Linq.Enumerable — запросы к объектам с интерфейсом IEnumerable<T>

### Вспомогательные библиотеки и классы

- System.Xml. XmlDocument — обработка XML- документов
- System.Xml.Linq. XDocument — обработка XML- документов
- System.Net. HttpWebRequest — формирование HTTP -запросов
- Newtonsoft.Json. JsonSerializerSettings — определение параметров объекта JsonSerializer
- System.IO.Compression.ZipArchive — обработка ZIP -архивов
- System.DirectoryServices. DirectoryEntry — взаимодействие с Active Directory
- System.Data.SqlClient. SqlConnection — взаимодействи с базой данных
- System.Drawing.Bitmap — обработка изображений
- RestSharp.RestRequest — формирование HTTP- запросов
- RestSharp.Authenticators.HttpBasicAuthenticator — аутентификация HTTP-запросов
- NLog.Logger — подсистема журналирования
- Aspose.BarCode — обработка штрихкодов
- Aspose.Cells — обработка файлов в формате Excel
- Aspose.Words — обработка файлов в формате Word

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
