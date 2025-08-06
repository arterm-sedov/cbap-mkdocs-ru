---
title: Configuring Export Template for Several Collections and Images Using C#
kbId: 1945
---


# Configuring Export Template for Several Collections and Images Using C#

## Use Case

In addition to the standard export template feature, you can configure a custom data export using a C# script with more flexible data processing. For example, you can export several collections or multi-value attributes from a record.

In this article, we will create a Word export template file with two tables (from two collections) and several images (from a multi-value attribute).

## Prerequisites

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
|  | *Photo\_1\_Atr* | **Image** | Stores one or several images (**Store multiple values** box is checked). |
|  | *Table\_1\_Atr* | **Record** | Linked to the *Table\_1* record template and stores multiple values (a *collection*). |
|  | *Table\_2\_Atr* | **Record** | Linked to the *Table\_2* record template and stores multiple values (a *collection*). |
| *Table\_1* | *Faсtor* | **Record** | Linked to a record template, which has the *Title* text attribute. |
| *Parameter* | **Record** | Linked to a record template, which has the *Title* text attribute. |
| *Value* | **Number** | Stores a numeric value, e.g., order amount. |
| *Table\_2* | Destination | **Text** | Stores a business trip destination. |
| Order | **Text** | Stores an order number. |
| Date | **Date** | Stores an order date. |
| Responsible | Account | Stores a user account ID. |

## Instructions

1. Create an export template as shown below using the [template.docx](https://kb.cmwlab.com/file.php?id=171) attached below the article:

_![Example template](https://kb.cmwlab.com/assets/2021-12-15_08h18_25.png)_

**Note:** In the export template, the image field is placed inside a table to accommodate several images.

1. A button with the **Export record**   operation will be automatically created.
2. Open the **Export record**button properties.
3. On the **Script** tab, paste the script attached below the article ([script for export.cs](https://kb.cmwlab.com/file.php?id=182)).

### Script Syntax

- In lines 17–24, the `GetPropertyValues()` API function is used to query the database for specific attribute values. This function improves the script performance with large datasets.

  ```

  var data_ = Api.TeamNetwork.ObjectService.GetPropertyValues(
      userCommandContext.ObjectIds, // getting an array of one or multiple record IDs
      new[] {
         "Photo_1_Atr", // the system name of an Image attribute
         "Table_1_Atr", // the system name of a Record attribute
         "Table_2_Atr" // the system name of a Record attribute
      });
  Dictionary<string, object> data = data_.FirstOrDefault().Value;

  ```
- Lines 39–40 show how to get the linked template attribute values via the **record** attributes.

```

string Faсtor_ = getByRef("Title", getString("Faсtor", Table_Data)); // getting the "Title" attribute value by reference via the "Factor" record attribute
string Parameter_ = getByRef("Title", getString("Parameter", Table_Data)); // getting the "Title" attribute value by reference via the "Parameter" record attribute

```

- Lines 56 and 67 show how to get the **FullName** attribute value via an account attribute.
  ```

  var Responsible_ = Api.Base.AccountService.Get(getString("Responsible", Table_Data)); // getting the "Responsible" Account attribute value (account ID)
  ...
  Responsible = Responsible_.FullName, // getting the responsible person's full name

  ```
- Lines 173–178 and 185–190 show how to check the image format.
  ```

  if (FileName.EndsWith("png") || FileName.EndsWith("PNG") || FileName.EndsWith("jpeg") || FileName.EndsWith("jpg") || FileName.EndsWith("JPG"))
  {
  byte[] content = (Api.TeamNetwork.DocumentService.GetContent((string)result)).Data;
  listImages.Add(content);
  }

  ```

- Lines 232–258 define the data model:
  ```

  public class IMG
  {
      public byte[] Image_data { get; set; }
  }
  public class TBL_1
  {
      public string Factor { get; set; }
      public string Parameter { get; set; }
      public string Value { get; set; }
  }
  public class TBL_2
  {
      public string Destination { get; set; }
      public string Order { get; set; }
      public string Date { get; set; }
      public string Responsible { get; set; }
  }
  public class RESULT
  {
      public List<IMG> Photo_1 { get; set; }
      public List<TBL_1> Table_1 { get; set; }
      public List<TBL_2> Table_2 { get; set; }
  }
  ```

  **Note:** Define a unique class for each table in the export template.

## See Also

[Configure an Export Template with C# Data Processing](https://kb.comindware.ru/article.php?id=1943)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
