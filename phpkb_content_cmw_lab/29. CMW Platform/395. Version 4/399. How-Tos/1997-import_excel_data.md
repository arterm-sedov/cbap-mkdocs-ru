---
title: Importing Linked Records From an Excel Spreadsheet
kbId: 1997
---


# Importing Linked Records From an Excel Spreadsheet

## Use Case

In the **CMW Platform,**you can import data to a record template and link the imported records to the records in other templates.

In this article, we will import an Excel sheet containing several clients' requests and link the imported requests to the corresponding client records.

## Prerequisites

To link the records imported from an Excel spreadsheet to the records in another template, you must specify the linked records' key values in the spreadsheet. As the key values, specify the values of the **ID** system attribute or an attribute **used as a record title**.

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template** | **Attribute name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Clients* | *Client requests* | **Record** | Linked to the *Requests* template, the **Store multiple values** box is checked.  This *Client requests*attribute is placed as a table on the *Client* form. |
| *Name* | **Text** | The **Use as record title** box is checked for the *Name*attribute.  The *Clients* template contains two records with the following *Name* attribute values: *Client A* and *Client B*.  The *Name* attribute values will be used as the key values for Excel data import. |
| *Requests* | *Client* | **Record** | Linked to the *Clients* template. |
| *Name* | **Text** | Stores the request name. |
| *Sum* | **Number** | Stores the request amount. |

## Instructions

1. Create the Excel spreadsheet to import, as shown below. In the *Client* column, specify the *Name* attribute values stored in the *Clients* template: *Client A* or *Client B*.   These are the key values to link the *Clients* template records with the *Requests* template records. 

   ![The Excel spreadsheet iwht clients' requests to import](https://kb.cmwlab.com/assets/2021-12-30_14h20_56.png)

   The Excel spreadsheet with clients' requests to import
2. Open the *Requests* record template.
3. Go to the **Import** tab.
4. Load the Excel file to import.
5. In the **Data mapping** section, map the spreadsheet columns to the *Requests* template attributes:
   - Map the *Client* column to the Client attribute and specify ***name***as the value **format**  .
   - Map the *Name* column to the *Name* attribute.
   - Map the *Sum* column to the *Sum* attribute and specify ***currency*** as the value **format**.
6. Click **Upload** to import the data.

   ![Mapping the imported Excel spreadsheet columns to the record template attributes ](https://kb.cmwlab.com/assets/img_64468c71cc130.png)

   Mapping the imported Excel spreadsheet columns to the record template attributes
7. The imported requests will appear in the *Requests* record template, each linked to its client.

   ![Imported records in the Requests template](https://kb.cmwlab.com/assets/img_64468946eea69.png)

   Imported records in the Requests template
8. Open the *Client A* record.
9. In the *Client requests* table, you should see the imported requests for *Client A.*

   ![The table of requests linked to the client record](https://kb.cmwlab.com/assets/img_64468af96d1f6.png)

   The table of requests linked to the client record

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
