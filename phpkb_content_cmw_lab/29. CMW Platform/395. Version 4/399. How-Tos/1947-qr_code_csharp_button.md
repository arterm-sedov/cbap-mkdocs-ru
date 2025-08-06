---
title: Generate a QR Code Using C# and a Third-Party Service on Button Click
kbId: 1947
---


# Generate a QR Code Using C# and a Third-Party Service on Button Click

## Use Case

Apart from using the built-in **QR code** attribute, you can generate a QR code using C# and a third-party service on a button click. You might want to do this to generate a special barcode or customize the QR code: change its size, color, image format or correction level, ad a logo overlay, etc.

In this article, we will configure a button to generate a 300x300px QR code pointing to [https://cmwlab.com](https://mycompany.com) via the `api.qrserver.com` service.

## Prerequisites

To proceed with the example, create the attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *QRCodes* | *QRinBase64* | **Text** | Select any **display format**.  .This attribute stores the generated QR code in the `base64` format. |
| *QRcodeImage* | **Text** | Select **HTML text** as the **display format**.  This attribute stores the QR code image and is placed on the form. |

## Instructions

1. In the *QRcodeImage* attribute properties, check the **Auto calculate** box and enter the following **Calculated value**:
   ```
   FORMAT("<img align='center' src='data:image/png;base64,{0}'</img>",LIST($QRinBase64))
   ```
2. In the *QRCodes* template, *c*reate a button with the following properties:
   - **Display name** — *Generate QR code*
   - **Operation** — **C# script**
   - **Operation context** — **Record**
   - **Operation result** — **Refresh data**

   On the **Script** tab, enter the following script:

   ```
   using System;
   using System.Collections.Generic;
   using System.Linq;
   using Comindware.Data.Entity;
   using Comindware.TeamNetwork.Api.Data.UserCommands;
   using Comindware.TeamNetwork.Api.Data;
   using RestSharp;

   class Script  
   {  
         public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)  
         {  
             ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;  
             byte[] AsBytes = new
             System.Net.WebClient().DownloadData
             ("https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://cmwlab.com" + userCommandContext.ObjectIds[0]);
   // 300x300 is desired QR code size
   // https://cmwlab.com is the URL to open upon scanning the QR-code
             string AsBase64String = Convert.ToBase64String(AsBytes);  
             var data = new Dictionary<string, object>
             {
                  { "QRinBase64", AsBase64String }
   // QRinBase64 is the system name of the attribute to store the QR code in base64 format  
              };  
              Api.TeamNetwork.ObjectService.EditWithAlias("QRCodes", userCommandContext.ObjectIds[0], data);
   // QRCodes is the system name of the record template where the button is located  
         var result = new UserCommandResult
         {  
           Success = true,  
           Commited = true,  
           Messages = new[]  
           {  
             new UserCommandMessage  
             {  
               Severity = SeverityLevel.Normal,  
               Text = "QR code was generated"
   // "QR code was generated" is the success message displayed upon generating the QR code  
             }  
            }  
         };  
     return result;  
       }
   }

   ```
3. In the *QRCodes* template, place the *QRcodeImage*attribute on a form.
4. Place the *Generate QR code* button on the form's toolbar.
5. Save the form.
6. Open or create a record in the *QRCodes* template.
7. Click the *Generate QR code* button: you should see the generated QR code on the form.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
