---
title: Import Data into Excel via API
kbId: 1955
---


# Import Data into Excel via API

## Use Case

Using the **CMW Platform** API, you can import the application data to Excel (via Power Query) or BI systems.

In this article, we will import the data from a record template into an Excel file using the **CMW Platform** API and the Power Query add-in.

## Instructions

### Obtaining the GET Request URL for a Template

1. Open your **{{ productName }}** instance website.
2. To open the API web interface, type `/docs` after the domain name in the browser address bar, for instance:
   `mycompany.com/docs`
3. Go to the **Solution API**section that lists all application templates.
4. Find the template you need by its system name and click it.
5. Select the **GET** method (without the `{id}` suffix) that returns all the records from the record template.
6. Click **Try it out**.
7. Copy the value in the **Request URL** field, for example:
   `https://mycompany.com/api/public/solution/Vehiclerequests`

_![Obtaining the template GET request URL](https://kb.cmwlab.com/assets/img_6442b00578cfd.png)_

**Note:** The **CMW Platform** API presents the data in JSON format.
### Importing Data to Excel

The Power Query add-in is built into Excel 2016 and above. For earlier versions of Excel, you need to [install it](https://support.microsoft.com/en-us/office/about-power-query-in-excel-7104fbee-9e62-4cb9-a02e-5bfb1a6c536a?redirectsourcepath=%252fru-ru%252foffice%252fpower-query-%2525e2%252580%252594-%2525d0%2525be%2525d0%2525b1%2525d0%2525b7%2525d0%2525be%2525d1%252580-%2525d0%2525b8-%2525d0%2525be%2525d0%2525b1%2525d1%252583%2525d1%252587%2525d0%2525b5%2525d0%2525bd%2525d0%2525b8%2525d0%2525b5-ed614c81-4b00-4291-bd3a-55d80767f81d).

1. On the **Data** tab in the ribbon, click **From Web**
2. In the **URL** field, paste the [**Request URL** you copied from the **CMW Platform** API](#RequestURL).

   ![Initializing the Power Query in Excel](https://kb.cmwlab.com/assets/img_6442afcc8b705.png)

   Initializing the Power Query in Excel
3. In the **Access Web content** window:
   - Select **Basic**.
   - Enter the **user name** and **password** of the account with permission to view the selected record template.
   - Click **Connect**.

     _![     Configuring the credentials for API access](https://kb.cmwlab.com/assets/img_6446481f27823.png)_
4. The received data appears in the **Power Query Editor** window.

   ![Power Query Editor with the imported data](https://kb.cmwlab.com/assets/img_644649e72f2d0.png)

   Power Query Editor with the imported data
5. Click **To Table** in the ribbon. Click **OK**in the **To Table** window .

   ![Configuring the query table](https://kb.cmwlab.com/assets/img_64464c555a6b4.png)

   Configuring the query table
6. Expand the list of all record template attributes and select the attributes to load in the table.

   _![   Configuring the columns](https://kb.cmwlab.com/assets/img_64464c3c94675.png)_
7. Click **Close & Load** in the ribbon to import the data into the Excel spreadsheet.

   ![Loading the query table to the Excel spreadsheet](https://kb.cmwlab.com/assets/img_64464d4357314.png)

   *Loading the query table to the Excel spreadsheet*
8. The data will appear in the Excel spreadsheet as shown below.

   ![A query table imported to the Excel spreadsheet](https://kb.cmwlab.com/assets/img_64464d8ecaf5a.png)

   A query table imported to the Excel spreadsheet

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
