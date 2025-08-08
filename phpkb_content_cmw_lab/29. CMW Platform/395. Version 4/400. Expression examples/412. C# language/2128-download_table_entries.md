---
title: Exporting Selected Records from a Custom Table
kbId: 2128
---


# Exporting Selected Records from a Custom Table

This script is designed to download selected records from the table, taking into account user settings. That is, the user selects the columns and records that should be uploaded to Excel. Records are selected with a checkmark in the leftmost column, and columns are configured through the "***My settings***"-> "***Customize display***" button.

The script works with attributes with data type:

- Boolean;
- Number;
- Duration;
- Text;
- Record;
- Date and time;
- Account.

```

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;
using Comindware.TeamNetwork.Api.Data.Forms;
using Comindware.Platform.Api.Data;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Tables;

class Script
{
public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
{
var items = userCommandContext.ObjectIds as string[];
if(items.Count() > 0)
{
try
{
var listId = userCommandContext.Query.DatasetId;
var paging = userCommandContext.Query.Paging;
var sorting = userCommandContext.Query.Sorting;
var filtr = userCommandContext.Query.Filter;
var containerId = Api.Base.OntologyService.GetAxioms(items.First())["container"].First().ToString();
var dataTablts = Api.TeamNetwork.DatasetService.GetQueries(containerId);

Dataset dataset;
Workbook workbook = new Workbook();
Worksheet wh = workbook.Worksheets[0];

var style = workbook.CreateStyle();
var flag = new StyleFlag();
flag.NumberFormat = true;

foreach(var table in dataTablts)
{
table.Paging = paging;
table.Sorting = sorting;
table.Filter = filtr;
if(table.DatasetId == listId)
{
var personaldataset = Api.TeamNetwork.DatasetConfigurationService.GetPersonalDataset(table.DatasetId);
dataset = Api.TeamNetwork.DatasetService.QueryData(table);
var columnsTabale = new Container[personaldataset.Columns.Count()];
var i=0;
foreach(var coll in personaldataset.Columns)
{
if(!coll.IsHidden)
{
columnsTabale[i] = new Container(coll.DataSourceInfo.Id, i);
wh.Cells[0,i].PutValue(coll.Name);
var prop = coll.DataSourceInfo.PropertyPath.Last().ToString();

if(prop != "id" && prop != "lastWriteDate" && prop != "creationDate" && prop != "archived" && prop != "creator")
{
var propData = Api.Base.OntologyService.GetAxioms(prop);
prop = propData["propertyType"].Last().ToString();
}

switch(prop)
{
case "xsd.decimal":
{
style.Number = 1;
wh.Cells.Columns[i].ApplyStyle(style, flag);
}break;
case "lastWriteDate":
{
style.Number = 22;
wh.Cells.Columns[i].ApplyStyle(style, flag);
wh.Cells.Columns[i].Width = 15;
}break;
case "creationDate":
{
style.Number = 22;
wh.Cells.Columns[i].ApplyStyle(style, flag);
wh.Cells.Columns[i].Width = 15;
}break;
case "xsd.dateTime":
{
style.Number = 22;
wh.Cells.Columns[i].ApplyStyle(style, flag);
wh.Cells.Columns[i].Width = 15;
}break;
}
i++;
}
}
var j=1;
var y = 0;
foreach(var coll in dataset.Columns)
{
try
{
var ds = coll.DataSourceInfo.Id;
var t = Array.Find(columnsTabale, x=> x.DS == ds).Id;
columnsTabale[t].Place = y;
}catch{}
y++;
}

foreach(var row in dataset.Rows)
{
if(Array.Find(items, v => v == row.Id) != null)
{
var rowData = row.Data;
for(var jj = 0; jj < i; jj++)
{
var ii = columnsTabale[jj].Place;
if(rowData[ii] != null)
{
if(rowData[ii].GetType() != typeof(Comindware.TeamNetwork.Api.Data.Forms.AccountReference) && rowData[ii].GetType() != typeof(System.Boolean) && rowData[ii].GetType() != typeof(Comindware.Platform.Api.Data.Reference))
{
wh.Cells[j,jj].PutValue(rowData[ii]);
}
else if (rowData[ii].GetType() == typeof(Comindware.TeamNetwork.Api.Data.Forms.AccountReference))
{
wh.Cells[j,jj].PutValue(((AccountReference)rowData[ii]).Name);
}
else if(rowData[ii].GetType() == typeof(System.Boolean))
{
if((bool)rowData[ii])
{
wh.Cells[j,jj].PutValue("True");
}
else
{
wh.Cells[j,jj].PutValue("False");
}
}
else if(rowData[ii].GetType() == typeof(Comindware.Platform.Api.Data.Reference))
{
wh.Cells[j,jj].PutValue(((Comindware.Platform.Api.Data.Reference)rowData[ii]).Name);
}
}
}
j++;
}
}
ListObject listObject = wh.ListObjects[wh.ListObjects.Add(0,0, j-1,i-1, true)];
}
}

MemoryStream stream = new MemoryStream();
workbook.Save(stream, SaveFormat.Xlsx);

var result = new UserCommandResult
{
Success = true,
Commited = true,

File=new UserCommandFileResult(){
Content = stream.ToArray(),
Name = "File.xlsx"
},

Messages = new[]
{
new UserCommandMessage
{
Severity = SeverityLevel.Normal,
Text = "Success"
}
}
};
return result;

}
catch
{
var result1 = new UserCommandResult
{
Success = false,
Commited = true,
Messages = new[]
{
new UserCommandMessage
{
Severity = SeverityLevel.Normal,
Text = "Failure"
}
}
};
return result1;
}
}
else
{
var result1 = new UserCommandResult
{
Success = false,
Commited = true,
Messages = new[]
{
new UserCommandMessage
{
Severity = SeverityLevel.Normal,
Text = "Failure"
}
}
};
return result1;
}
}

public class Container
{
public int Id {get;set;}
public int Place {get;set;}
public string DS {get;set;}

public Container(string ds , int id )
{
DS = ds; Id = id;
}
}
}

```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
