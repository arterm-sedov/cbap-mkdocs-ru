---
title: Шаблон экспорта, Настройка с использованием C#
kbId: 4793
---

# Шаблон экспорта, Настройка с использованием C#

В **{{ productName }}** помимо стандартной выгрузки отчётов предусмотрен экспорт данных с использованием скриптов на C#. Этот вариант позволяет более гибко настроить параметры экспортируемого файла, например, с дополнительной фильтрацией или заменой информации, либо с форматированным выводом атрибутов-коллекций.

**Шаблон документа в формате .xls**

Рассмотрим решение следующей задачи: написать скрипт, который формирует Excel-файл, в котором каждый элемент коллекции располагается в отдельной строчке (по умолчанию все элементы коллекции перечисляются в одной строчке через пробел).

**1.** Для начала создайте шаблон экспорта по типу:

_![Пример excel шаблона экспорта](https://kb.comindware.ru/assets/exp1.jpg)_

**&=data.свойство\_класса** (Свойства класса — структура подготовки данных, которые определяются в С# скрипте)

**Примечание :** в Excel-файле обязательно нужно указывать необходимый формат полей, иначе данные выгрузятся некорректно. Для числа — числовой, для даты и времени — дата, и т.д.

Поля «Клиент», «Контактное лицо», «Телефон» и «Email» будут заполняться из атрибутов записей шаблона «Клиенты». Поле «Договор» — коллекция в шаблоне записей «Клиенты», поле «Статус» — справочник статусов в отдельном шаблоне.

**2.** Добавьте созданный шаблон экспорта в текущий шаблон записи (в данном случае, «Клиенты»):

_![Расположение раздела «Шаблоны экспорта»](https://kb.comindware.ru/assets/2.1_2021-12-13_114132.png)_

**3.**В этом же шаблоне записи автоматически добавится кнопка с операцией «Экспорт записи»:

_![Автоматически созданная кнопка](https://kb.comindware.ru/assets/2.2_2021-12-13_124346.png)_

Перейдите на вкладку «***Скрипт***» в свойствах этой кнопки и добавьте следующий код:

```

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Aspose.Cells;
using Aspose.Cells.Pivot;

class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
var objectsData = Api.TeamNetwork.ObjectService.ListWithAlias("Clients"); // Системное имя ШЗ "Клиенты"
var dataToExport = new List<MainData>();
foreach (var objectDict in objectsData)
{
var ContractDataInIds = getterListSTR("Contracts_collection", objectDict); // Атрибут-коллекция в ШЗ "Клиенты"
if(ContractDataInIds.Count == 0) {ContractDataInIds.Add("tempID");}
var ContractDataInList = new List<ContractData>();
foreach (var ContractDataInId in ContractDataInIds)
{
var ContractDataInData = GetData(ContractDataInId);

var Status_Id = getterSTR("Status", ContractDataInData); // Атрибут-ссылка в ШЗ "Договоры"
var Status_Data = GetData(Status_Id);

var ContractDataInT = new ContractData
{
Name = getterSTR("Title", ContractDataInData), // Атрибут "Статус" в ШЗ "Договоры"
Date = getterDT("Date", ContractDataInData), // Атрибут "Дата" в ШЗ "Договоры"
Total = getterDC("Total", ContractDataInData), // Атрибут "Сумма" в ШЗ "Договоры"
Status = getterSTR("Title", Status_Data) // Атрибут "Название" в ШЗ "Статусы договора"

};
ContractDataInList.Add(ContractDataInT);
}

var Data_ = new MainData
{
Client = getterSTR("Title", objectDict), // Атрибут "Название" в ШЗ "Клиенты"
Contact = getterSTR("Contact", objectDict), // Атрибут "Контактное лицо" в ШЗ "Клиенты"
Phone = getterSTR("Phone", objectDict), // Атрибут "Телефон" в ШЗ "Клиенты"
Email = getterSTR("Email", objectDict), // Атрибут "Email" в ШЗ "Клиенты"
Contract = ContractDataInList
};
dataToExport.Add(Data_);
}

var content = Api.TeamNetwork.ObjectAppExportService.ExecuteExcelExportTemplate(userCommandContext.DocumentTemplateId, dataToExport);
var result = new UserCommandResult
{
Success = true,
Commited = true,
ResultType = UserCommandResultType.File,
File = new UserCommandFileResult()
{
Name = "Excel_Data.xlsx",
Type = "Excel",
Content = content

},
Messages = new[]
{
new UserCommandMessage
{
Severity = SeverityLevel.Normal,
Text = "Файл сформирован"
}
}
};
return result;
    }

public static Decimal getterDC(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return 0;
}
var stringValue = getterSTR(key, dictionary);
if (stringValue != null && Decimal.TryParse(stringValue, out var result))
{
return result;
}
else
{
return 0;
}
}

public static DateTime? getterDT(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return null;
}
var stringValue = getterSTR(key, dictionary);
if (stringValue != null && DateTime.TryParse(stringValue, out var result))
{
return result.AddHours(5);
}
else
{
return null;
}
}

public static string getterSTR(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return null;
}
if (dictionary.TryGetValue(key, out var result))
{
if (result == null) return null;
return result.ToString();
}
else
{
return null;
}

}

public static IList<string> getterListSTR(string key, IDictionary<string, object> dictionary = null)
{
var result = new List<string>();
if (dictionary != null && key != null)
{
if (dictionary.TryGetValue(key, out var objectData))
{
var objectDataArray = objectData as object[];
foreach (var singlObject in objectDataArray)
{
if (singlObject == null) continue;
result.Add(singlObject.ToString());
}
}
}
return result;
}

public static IDictionary<string, object> GetData(string objectId = null)
{
if (objectId == null || objectId.Contains("account") || objectId == "tempID")
{
return null;
}
var container = Api.TeamNetwork.ObjectAppService.GetByObject(objectId);
var result = Api.TeamNetwork.ObjectService.GetWithAlias(container.Alias, objectId);
return result;
}
}

[Serializable]
public class MainData
{
public string Client { get; set; }
public string Contact { get; set; }
public string Phone { get; set; }
public string Email { get; set; }
public List<ContractData> Contract { get; set; }
}

[Serializable]
public class ContractData
{
public string Name { get; set; }
public decimal Total { get; set; }
public DateTime? Date { get; set; }
public string Status { get; set; }
}

```

В коде скрипта комментариями помечены 11 мест, где при необходимости можно заменить системные имена своими.

Как выглядят данные в продукте:

_![Список клиентов](https://kb.comindware.ru/assets/2.3_2021-12-13_141658.png)_

Результат выгрузки:

_![Excel файл](https://kb.comindware.ru/assets/exp5.jpg)_

**Шаблон документа в формате .doc**

По такой же логике настраиваем выгрузку  Шаблона экспорта в формате Word.

Отличием здесь будет немного иное написание самого шаблона, а также C# скрипта.

_![Пример word шаблона экспорта](https://kb.comindware.ru/assets/exp6.jpg)_

C# скрипт:

```

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text.RegularExpressions;
using Comindware.Data.Entity;
using Comindware.Platform.Api.Data;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using System.IO;
using System.Data;

class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
var objectsData = Api.TeamNetwork.ObjectService.ListWithAlias("Clients"); // Системное имя ШЗ "Клиенты"
List<MainData> Data_ = new List<MainData>();
foreach (var objectDict in objectsData)
{
var ContractDataInIds = getterListSTR("Contracts_collection", objectDict); // Атрибут-коллекция в ШЗ "Клиенты"
if(ContractDataInIds.Count == 0) {ContractDataInIds.Add("tempID");}
bool first_element = true;
foreach (var ContractDataInId in ContractDataInIds)
{
var ContractDataInData = GetData(ContractDataInId);

var Status_Id = getterSTR("Status", ContractDataInData); // Атрибут-ссылка в ШЗ "Договоры"
var Status_Data = GetData(Status_Id);

if(first_element == true)
{
first_element = false;
var temp = new MainData
{
Client = getterSTR("Title", objectDict), // Атрибут "Название" в ШЗ "Клиенты"
Contact = getterSTR("Contact", objectDict), // Атрибут "Контактное лицо" в ШЗ "Клиенты"
Phone = getterSTR("Phone", objectDict), // Атрибут "Телефон" в ШЗ "Клиенты"
Email = getterSTR("Email", objectDict), // Атрибут "Email" в ШЗ "Клиенты"

Name = getterSTR("Title", ContractDataInData), // Атрибут "Статус" в ШЗ "Договоры"
Date = getterDT("Date", ContractDataInData), // Атрибут "Дата" в ШЗ "Договоры"
Total = getterDC("Total", ContractDataInData), // Атрибут "Сумма" в ШЗ "Договоры"
Status = getterSTR("Title", Status_Data) // Атрибут "Название" в ШЗ "Статусы договора"
};
             Data_.Add(temp);
}
else
{
var temp = new MainData
{
Name = getterSTR("Title", ContractDataInData), // Атрибут "Статус" в ШЗ "Договоры"
Date = getterDT("Date", ContractDataInData), // Атрибут "Дата" в ШЗ "Договоры"
Total = getterDC("Total", ContractDataInData), // Атрибут "Сумма" в ШЗ "Договоры"
Status = getterSTR("Title", Status_Data) // Атрибут "Название" в ШЗ "Статусы договора"
};
Data_.Add(temp);
}
}
}

var dataToExport = new RESULT
{
MainData_ = Data_
};

        var content = Api.TeamNetwork.ObjectAppExportService.ExecuteWordExportTemplate(userCommandContext.DocumentTemplateId,dataToExport,false);

var result = new UserCommandResult
        {
            Success = true,
            Commited = true,
            File=new UserCommandFileResult(){
                Content = content,
Name = "Word_Data.doc",
Type = "Word"
            },
            ResultType = UserCommandResultType.Notificate,
            Messages = new[]
            {
                new UserCommandMessage
                {
                    Severity = SeverityLevel.Normal,
                    Text = "Документ сформирован"
                }
            }
        };
        return result;
    }

public static Decimal getterDC(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return 0;
}
var stringValue = getterSTR(key, dictionary);
if (stringValue != null && Decimal.TryParse(stringValue, out var result))
{
return result;
}
else
{
return 0;
}
}

public static DateTime? getterDT(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return null;
}
var stringValue = getterSTR(key, dictionary);
if (stringValue != null && DateTime.TryParse(stringValue, out var result))
{
return result.AddHours(5);
}
else
{
return null;
}
}

public static string getterSTR(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return null;
}
if (dictionary.TryGetValue(key, out var result))
{
if (result == null) return null;
return result.ToString();
}
else
{
return null;
}
}

public static IList<string> getterListSTR(string key, IDictionary<string, object> dictionary = null)
{
var result = new List<string>();
if (dictionary != null && key != null)
{
if (dictionary.TryGetValue(key, out var objectData))
{
var objectDataArray = objectData as object[];
foreach (var singlObject in objectDataArray)
{
if (singlObject == null) continue;
result.Add(singlObject.ToString());
}
}
}
return result;
}

public static IDictionary<string, object> GetData(string objectId = null)
{
if (objectId == null || objectId.Contains("account") || objectId == "tempID")
{
return null;
}
var container = Api.TeamNetwork.ObjectAppService.GetByObject(objectId);
var result = Api.TeamNetwork.ObjectService.GetWithAlias(container.Alias, objectId);
return result;
}
}

[Serializable]
public class MainData
{
public string Client { get; set; }
public string Contact { get; set; }
public string Phone { get; set; }
public string Email { get; set; }
public string Name { get; set; }
public decimal Total { get; set; }
public DateTime? Date { get; set; }
public string Status { get; set; }
}

public class RESULT
{
    public List<MainData> MainData_ { get; set; }
}

```

Результат выгрузки:

_![Word файл](https://kb.comindware.ru/assets/exp7.jpg)_

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
