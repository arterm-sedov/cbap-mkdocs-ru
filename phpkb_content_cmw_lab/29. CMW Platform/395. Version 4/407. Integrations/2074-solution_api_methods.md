---
title: Solution API Methods
kbId: 2074
---


# Solution API Methods

## Introduction

Solution API provides RESTful methods that are automatically generated for all record, account, organizational unit, and role templates (but not for process templates) in the current **CMW Platform** instance.

There are five methods for each template:

- Delete a record
- Get data of a record
- Edit data of a record
- Get data of all records
- Create a record

This article provides an overview of the Solution API methods. See complete API details in the Swagger UI.

## Access to Solution API

- Base URL for the Solution API requests:
  `https://your-host/api/public/solution/`
- Solution API supports `GET`, `PUT`, `POST`, and   `DELETE` queries.
- Solution API methods support JSON content type.
- Solution API supports basic authentication.

## Using Swagger

The Swagger UI provides detailed API method references, including request and response descriptions and data models with example values.

With the Swagger UI, you can execute the requests and view the responses.

Access the Swagger UI for Solution API at:

`http://your-host/Docs/SolutionApi`

Here `your-host` is the domain name of the **CMW Platform** instance.

_![Swagger UI for the method that creates a template record](https://kb.cmwlab.com/assets/img_64d4a6580acd8.png)_

## Solution API Method Descriptions

| TemplateSystemName — records in a template by its system name | | | | |
| --- | --- | --- | --- | --- |
| Method | Query | Description | Input | Output |
| DELETE | /TemplateSystemName/{id} | Deletes a record from the TemplateSystemName template | Record ID | Status object |
| GET | /TemplateSystemName/{id} | Gets data of a record in the TemplateSystemName template | Record ID | Object with record attribute values:`{"attributeSystemName": "value"}` |
| PUT | /TemplateSystemName/{id} | Edits data of a record in the TemplateSystemName template | Record ID, object with record attribute values: `{"attributeSystemName": "value"}` | Status object |
| GET | /TemplateSystemName | Gets data of all records in the TemplateSystemName template |  | Array of objects with record attribute values:`[{"attributeSystemName": "value"}]` |
| POST | /TemplateSystemName | Creates a record in the TemplateSystemName template | Object with record attribute values: `{"attributeSystemName": "value"}` | Record ID |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
