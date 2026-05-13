---
name: csharp_api
description: Reference files and patterns for writing C# scripts in Comindware Platform
---

Use this skill when answering questions about:
- Writing C# scripts for buttons, process tasks, scenarios
- Using Comindware Platform API (Api.Base, Api.TeamNetwork, Api.Process)
- Common C# patterns for data manipulation, process management, navigation

## Key Files to Reference

### Main C# Guide
- `docs/ru/developer_guide/csharp/csharp_guide.md` — Full reference for all script types (lines 28-407)
  - Button scripts with `UserCommandResult`
  - Process task scripts with `ScriptContext`
  - Scenario scripts with `ObjectID`

### Common C# Script Examples
- `docs/ru/developer_guide/csharp/5000-start_process_by_records.md` — Start process for list records
- `docs/ru/developer_guide/csharp/5001-create_entry_transfer_data.md` — Create record with data transfer
- `docs/ru/developer_guide/csharp/5004-change_task_status.md` — Change status and complete task
- `docs/ru/developer_guide/csharp/5005-button_change_variable.md` — Modify reusable variable
- `docs/ru/developer_guide/csharp/5007-example_csharp_object_copy.md` — Clone/clone object
- `docs/ru/developer_guide/csharp/5009-goto_showcase_record.md` — Navigate to record
- `docs/ru/developer_guide/csharp/5010-delete_related_record.md` — Delete related objects
- `docs/ru/developer_guide/csharp/5013-fill_collection_selected_list.md` — Fill collection from list
- `docs/ru/developer_guide/csharp/5016-global_active_directory.md` — Active Directory integration
- `docs/ru/developer_guide/csharp/5018-start_process_button_for_list_records.md` — Start process from button
- `docs/ru/developer_guide/csharp/5019-change_all_account_emails.md` — Modify all accounts
- `docs/ru/developer_guide/csharp/5022-clear_link.md` — Clear link attribute

## Script Templates by Context

### Button Script (UserCommandContext)
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

public class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
        var objectId = userCommandContext.ObjectIds.FirstOrDefault();
        
        // Your logic here
        
        var result = new UserCommandResult
        {
            Success = true,
            Commited = true,
            ResultType = UserCommandResultType.DataChange,
            Messages = new[]
            {
                new UserCommandMessage
                {
                    Severity = SeverityLevel.Normal,
                    Text = "Operation completed"
                }
            }
        };
        return result;
    }
}
```

**Context properties:**
- `ObjectIds` — array of selected record IDs (empty if none selected, or one ID from form)
- `SelectedIds` — array of IDs selected in table on form
- `CurrentUserId` — current user account ID
- `CurrentRequestTime` — datetime of current request

**Return types:**
- `DataChange` — refresh data
- `Notificate` — show message
- `Navigate` — go to page (with `NavigationResult`)
- `File` — download file (with `File`)

### Process Task Script (ScriptContext)
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;

class Script
{
    public static void Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities)
    {
        var businessObjectId = context.BusinessObjectId;
        var processId = context.ProcessID;
        
        // Your logic here
    }
}
```

**Context properties:**
- `ProcessID` — process instance ID
- `BusinessObjectID` — associated record ID

### Scenario Script (ObjectID)
```csharp
public class Script
{
    public static string Main(string ObjectID, [Comindware.Entities entities])
    {
        // Return string, int, decimal, dateTime, bool, TimeSpan or IEnumerable<string>
    }
}
```

## Common API Patterns

### Accessing Object Properties
```csharp
var request = Api.TeamNetwork.ObjectService.Get(id);
object value;
request.TryGetValue("op.93", out value);  // by attribute ID
```

### Creating Record
```csharp
var propertyDictionary = new Dictionary<string, object>();
propertyDictionary.Add("AttributeSystemName", value);
Api.TeamNetwork.ObjectService.CreateWithAlias("RecordTemplateAlias", propertyDictionary);
```

### Editing Record
```csharp
var data = new Dictionary<string, object>
{
    { "AttributeSystemName", newValue }
};
Api.TeamNetwork.ObjectService.EditWithAlias("RecordTemplateAlias", objectId, data);
```

### Cloning Object
```csharp
Api.TeamNetwork.ObjectService.Clone(objectId, null, true);
```

### Starting Process
```csharp
Api.Process.ProcessObjectService.CreateWithObjectId("pa.2", null, objectId);
```

### Completing Task
```csharp
var activeTask = Api.Process.ProcessObjectService.GetReferencedTasks(objectId)
    .Where(x => x.Status == UserTaskStatus.InProgress)
    .FirstOrDefault().Id;
Api.TeamNetwork.UserTaskService.Complete(activeTask, true);
```

### Getting List Data
```csharp
var query = new Comindware.TeamNetwork.Api.Data.DatasetQuery
{
    DatasetId = "lst.74"
};
var rows = Api.TeamNetwork.DatasetService.QueryData(query).Rows;
```

### Navigating
```csharp
var result = new UserCommandResult
{
    Success = true,
    ResultType = UserCommandResultType.Navigate,
    NavigationResult = new UserCommandNavigationResult
    {
        ContainerId = "oa.8",
        ObjectId = objectId,
        Context = ContextType.Record
    }
};
```

### Working with Collections
```csharp
var data = new Dictionary<string, object>
{
    { "CollectionAttribute", listOfIds }  // List<string>
};
Api.TeamNetwork.ObjectService.EditWithAlias("Template", objectId, data);
```

### Account Operations
```csharp
var accounts = Api.Base.AccountService.List();
foreach (var account in accounts)
{
    account.Mbox = "new@email.com";
    Api.Base.AccountService.Edit(account);
}
```

### Reusable Variables
```csharp
var value = Api.Solution.SolutionVariableService.GetValue("svar.1");
Api.Solution.SolutionVariableService.SetValue("svar.1", newValue);
```

## Quick Answers Template

**Button that starts process for selected records:**
```csharp
foreach (var objectId in userCommandContext.ObjectIds)
{
    Api.Process.ProcessObjectService.CreateWithObjectId("pa.2", null, objectId);
}
```

**Button that creates record with data transfer:**
```csharp
var request = Api.TeamNetwork.ObjectService.Get(objectId);
object value;
request.TryGetValue("op.93", out value);
var data = new Dictionary<string, object> { { "Attribute", value } };
Api.TeamNetwork.ObjectService.CreateWithAlias("Template", data);
```

**Process task that fills collection from list:**
```csharp
var query = new DatasetQuery { DatasetId = "lst.53" };
var rows = Api.TeamNetwork.DatasetService.QueryData(query).Rows;
List<string> ids = rows.Select(r => r.Id).ToList();
var data = new Dictionary<string, object> { { "CollectionAttr", ids } };
Api.TeamNetwork.ObjectService.EditWithAlias("Template", context.BusinessObjectId, data);
```

## Notes
- Always use `FirstOrDefault()` when processing single object from `ObjectIds` array
- Use `foreach` loop when processing multiple records
- Check for null when querying datasets: `if (sessionsData == null) { return; }`
- System names use `op.N` format for attributes, `pa.N` for processes, `lst.N` for lists
- Return `UserCommandResult` from button scripts, `void` from process task scripts