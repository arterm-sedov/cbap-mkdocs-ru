---
title: Navigating to the object from the storefront widget
kbId: 2101
---


# Navigating to the object from the storefront widget

In order to be able to switch from the product card in the storefront widget to the object form, enter the following expression:

```

using System; 
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    { 
                    var objectid = userCommandContext.ObjectIds[0];
        var result = new UserCommandResult()
        {

Success = true,
            Messages =  null,

ResultType = UserCommandResultType.Navigate ,
            NavigationResult = new UserCommandNavigationResult
            {
                ContainerId = "oa.8",
                ObjectId = objectid,
                Context = ContextType.Record
            }
        };
        return result;
    }
}

```

**where:**

***oa.8*** — ID of the record template where the objects from the storefront are located.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
