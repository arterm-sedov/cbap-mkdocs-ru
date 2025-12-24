---
title: Configure an Export Template with C# Data Processing
kbId: 1943
---


# Configure an Export Template with C# Data Processing

## Use Case

In addition to the standard export template feature, you can configure a custom data export using a C# script with more flexible data processing. For example, you can apply data filters, replace data, or reformat the values.

In this article, we will configure the Excel and Word export templates and C# scripts to export the files with each collection element on a separate line (by default, all collection elements are listed on one line separated by a space). The export templates and C# scripts slightly differ for Word and Excel formats.

## Prerequisites

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Clients* | *Contracts\_collection* | **Record** | The *Contracts* attribute is linked to the *Contracts* template and stores multiple values (a *collection*). |
| *Title, Contact, Phone, Email* | **Text** | The client details. |
| *Contracts* | *Status* | Record | The *Status* attribute is linked to the *Contract Statuses* template. |
| *Title, Date, Total* | Text | The contract details. |
| *Contract Statuses* | **Title** | **Text** | The status name. |

## Instructions

### Create an Excel Export Template

1. Create an XLSX document as shown below:

_![Example of an Excel export template](https://kb.cmwlab.com/assets/exp1_en.png)_

In the Excel export template the `&=data.class_property` placeholders are the `MainData` class property references filled by the C# script.

**Note:** You must specify the required cell format in the Excel file. Otherwise, the data will not be exported correctly. For numeric attributes set a numeric format, for date & time attributes set a date format, etc.

1. Add the XLSX document as an export template to the *Clients* record template.

_![The export template listed on the export templates tab](https://kb.cmwlab.com/assets/img_6437fe0b2b90d.png)_

1. A button with the **Export record** operation will be automatically added to the *Clients* template:

_![The button for the Export record operation](https://kb.cmwlab.com/assets/img_643800d4628a9.png)_

1. Open the button properties, and on the **Script** tab, enter the following C# code:

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
var objectsData = Api.TeamNetwork.ObjectService.ListWithAlias("Clients"); // system name of the Clients record template
var dataToExport = new List();
foreach (var objectDict in objectsData)
{
var ContractDataInIds = getterListSTR("Contracts_collection", objectDict); // system name of the Contracts_collection record attribute in the Clients records template
     
if(ContractDataInIds.Count == 0) {ContractDataInIds.Add("tempID");}
var ContractDataInList = new List();
foreach (var ContractDataInId in ContractDataInIds)
{
var ContractDataInData = GetData(ContractDataInId);
      
var Status_Id = getterSTR("Status", ContractDataInData); // system name of the Status record attribute in the Contracts record template
var Status_Data = GetData(Status_Id);
      
var ContractDataInT = new ContractData
{
Name = getterSTR("Title", ContractDataInData), // system name of the Title attribute in the Contracts record template
Date = getterDT("Date", ContractDataInData), // system name of the Date attribute in the Contracts record template
Total = getterDC("Total", ContractDataInData), // system name of the Total attribute in the Contracts record template
      
Status = getterSTR("Title", Status_Data) // system name of the Title attribute in the Contract Status record template
      
};
ContractDataInList.Add(ContractDataInT);
}
      
var Data_ = new MainData
{
Client = getterSTR("Title", objectDict), // system name of the Title attribute in the Clients record template
Contact = getterSTR("Contact", objectDict), // system name of the Contact person attribute in the Clients record template
Phone = getterSTR("Phone", objectDict), // system name of the Phone attribute in the Clients record template
Email = getterSTR("Email", objectDict), // system name of the Email attribute in the Clients record template
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
Text = "Generated the file"
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
      
public static IList getterListSTR(string key, IDictionary<string, object> dictionary = null)
{
var result = new List();
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
public List Contract { get; set; }
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
**Note:**In the script above, the lines with the attribute and template system names are marked with comments. In these lines, substitute the actual system names from your application.
### Create a Word Export Template

1. Create a DOCX document as shown below:

_![Example of a Word export template](https://kb.cmwlab.com/assets/img_643801f95205b.png)_

In the Word export template:

- The `row.class_property` placeholders are `MainData` class property references filled by the C# script.
- The `row` variable is the iterator for `MainData_` array, that contains `MainData` class instances.

1. Add the DOCX document as an export template to the *Clients* record template.
2. A button with the **Export record** operation will be automatically added to the *Clients* template.
3. Open the button properties, and on the **Script** tab, enter the following C# code:

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
      
class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
var objectsData = Api.TeamNetwork.ObjectService.ListWithAlias("Clients"); // system name of the Clients record template
List Data_ = new List();
foreach (var objectDict in objectsData)
{
var ContractDataInIds = getterListSTR("Contracts_collection", objectDict); // system name of the attribute-collection in the Clients record template
if(ContractDataInIds.Count == 0) {ContractDataInIds.Add("tempID");}
bool first_element = true;
foreach (var ContractDataInId in ContractDataInIds)
{
var ContractDataInData = GetData(ContractDataInId);
      
var Status_Id = getterSTR("Status", ContractDataInData); // system name of the Status record attribute in the Contracts record template
var Status_Data = GetData(Status_Id);
      
if(first_element == true)
{
first_element = false;
var temp = new MainData
{
Client = getterSTR("Title", objectDict), // system name of the Title attribute in the Clients record template
Contact = getterSTR("Contact", objectDict), // system name of the Contact person attribute in the Clients record template
Phone = getterSTR("Phone", objectDict), // system name of the Phone attribute in the Clients record template
Email = getterSTR("Email", objectDict), // system name of the Email attribute in the Clients record template
      
Name = getterSTR("Title", ContractDataInData), // system name of the Title attribute in the Contracts record template
Date = getterDT("Date", ContractDataInData), // system name of the Date attribute in the Contracts record template
Total = getterDC("Total", ContractDataInData), // system name of the Total attribute in the Contracts record template
Status = getterSTR("Title", Status_Data) // system name of the Title attribute in the Contract statuses record template
};
             Data_.Add(temp);
}
else
{
var temp = new MainData
{
Name = getterSTR("Title", ContractDataInData), // system name of the Status attribute in the Contracts record template
Date = getterDT("Date", ContractDataInData), // system name of the Date attribute in the Contracts record template
Total = getterDC("Total", ContractDataInData), // system name of the Total attribute in the Contracts record template
Status = getterSTR("Title", Status_Data) // system name of the Title attribute in the Contract statuses record template
};
Data_.Add(temp);
}
}
}
      
var dataToExport = new RESULT
{
MainData_ = Data_
};
      
        var content = Api.TeamNetwork.ObjectAppExportService.ExecuteWordExportTemplate(userCommandContext.DocumentTemplateId,dataToExport,false);
      
var result = new UserCommandResult
        {
            Success = true,
            Commited = true,
            File=new UserCommandFileResult(){
                Content = content,
Name = "Word_Data.doc",
Type = "Word"
            },
            ResultType = UserCommandResultType.Notificate,
            Messages = new[]
            {
                new UserCommandMessage
                {
                    Severity = SeverityLevel.Normal,
                    Text = "Generated the file"
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
      
public static IList getterListSTR(string key, IDictionary<string, object> dictionary = null)
{
var result = new List();
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
    public List MainData_ { get; set; }
}
```
**Note:**In the script above, the lines with the attribute and template system names are marked with comments. In these lines substitute the actual system names from your application.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
