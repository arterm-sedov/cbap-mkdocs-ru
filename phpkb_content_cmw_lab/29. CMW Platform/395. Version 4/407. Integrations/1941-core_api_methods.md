---
title: Web API Methods
kbId: 1941
---


# Web API Methods

## Introduction

The **CMW Platform** RESTful Web API provides generic REST API methods. These methods are the same for all **CMW Platform**versions.

This article contains the Web API methods overview. See complete API details in the Swagger UI.

## Accessing Web API

- Base URL for the Web API requests:
  `https://your-host/webapi/`
- Web API supports `GET`, `PUT`, `POST`  , and   `DELETE` queries.
- Web API supports JSON or XML content types.
- Web API supports basic authentication.

## Using Swagger

The Swagger UI provides detailed API method references, including request and response descriptions and data models with example values.

With the Swagger UI, you can execute the requests and view the responses.

Access the Swagger UI for Web API at:

`https://your-host/Docs/WebApi/`

Here `your-host` is the domain name of the **CMW Platform** instance.

_![Swagger UI for the method that creates an account template](https://kb.cmwlab.com/assets/img_661e5d5fbf8ed.png)_

### Definitions

The Web API methods and Swagger documentation use the following names for the CMW Platform entities:

- *activity*— process diagram element
- *alias*— system name
- *behaviour*— scenario, process diagram element
- *container*— template, application
- *dataset*— table in a template
- *global alias*— object path, consisting of its type, parent system name, and object system name
- *id*— object identifier
- *list*— array
- *property*— attribute
- *solution*— application
- *scheme*— process diagram
- *stream*— file stored in the system
- *transfer*— application version management
- *trigger*— scenario
- *user command*— button
- *worker*— system service
- ***object*** — a collection of property/value pairs
## Web API Method Descriptions

| Account — individual accounts | | | | |
| --- | --- | --- | --- | --- |
| Method | Query | Description | Input | Output |
| GET | /webapi/Account | Gets all accounts. |  | Array of objects with account properties |
| POST | /webapi/Account | Creates account. | Account properties object | Account ID |
| PUT | /webapi/Account | Edits account properties. | Account properties object | Status object |
| DELETE | /webapi/Account/{accountId} | Deletes account. | Account ID | Status object |
| GET | /webapi/Account/{accountId} | Gets account properties. | Account ID | Account properties object |
| AccountTemplate — account templates and accounts linked to them | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/AccountTemplate/{solutionAlias} | Creates account template. | Application system name, account template properties object | Object with account template system name |
| PUT | /webapi/AccountTemplate/{solutionAlias} | Edits account template properties. | Application system name, account template properties object | Status object |
| DELETE | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias} | Deletes account template. | Application system name, account template system name | Status object |
| GET | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias} | Gets account template properties. | Application system name, account template system name | Account template properties object |
| PUT | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias}/Disable | Archives account template. | Application system name, account template system name. | Status object |
| PUT | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias}/Enable | Unarchives account template. | Application system name, account template system name | Status object |
| PUT | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias}/Exclude | Unlinks accounts from the specified account template. | Application system name, account template system name, array of account IDs | Status object |
| PUT | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias}/Include | Links specified accounts to the specified account template. | Application system name, account template system name, array of account IDs | Status object |
| GET | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias}/ListIncluded | Gets accounts linked to the specified account template. | Application system name, account template system name | Array of objects with account properties |
| GET | /webapi/AccountTemplate/List/{solutionAlias} | Gets all account templates in the specified application. | Application system name | Array of objects with account template properties |
| Attribute — template attributes | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Attribute/{solutionAlias} | Creates attribute. | Application system name, attribute properties object | Object with attribute system name |
| PUT | /webapi/Attribute/{solutionAlias} | Edits attribute properties. | Application system name, attribute properties object | Status object |
| DELETE | /webapi/Attribute/{solutionAlias}/{attributeGlobalAlias} | Deletes attribute. | Application system name, attribute global alias: `Attribute@templateSystemName.attributeSystemName` | Status object |
| GET | /webapi/Attribute/{solutionAlias}/{attributeGlobalAlias} | Gets attribute properties. | Application system name, attribute global alias: `Attribute@templateSystemName.attributeSystemName` | Attribute properties object |
| PUT | /webapi/Attribute/{solutionAlias}/{attributeGlobalAlias}/Disable | Archives attribute. | Application system name, attribute global alias: `Attribute@templateSystemName.attributeSystemName` | Status object |
| PUT | /webapi/Attribute/{solutionAlias}/{attributeGlobalAlias}/Enable | Unarchives attribute. | Application system name, attribute global alias: `Attribute@templateSystemName.attributeSystemName` | Status object |
| GET | /webapi/Attribute/List/{templateGlobalAlias} | Gets all attributes for the specified template. | Template global alias: `Template@applicationSystemName.templateSystemName` | Array of objects with attribute properties |
| Backup — backup configurations and sessions | | | | |
| Method | Query | Description | Input | Output |
| DELETE | /webapi/Backup/Configuration | Deletes specified backup configurations. | Array of backup configuration IDs | Status object |
| GET | /webapi/Backup/Configuration | Gets all backup configurations. |  | Array of backup configuration objects |
| POST | /webapi/Backup/Configuration | Creates backup configuration. | Backup configuration object | Backup configuration ID |
| PUT | /webapi/Backup/Configuration | Edits backup configuration. | Backup configuration object | Status object |
| GET | /webapi/Backup/Configuration/{configurationId} | Gets backup configuration. | Backup configuration ID | Backup configuration object |
| DELETE | /webapi/Backup/Session | Deletes specified backup sessions. | Array of backup session IDs | Status object |
| POST | /webapi/Backup/Session | Returns backup sessions matching the specified filter. | Backup session filter object | Array of objects with backup session details |
| POST | /webapi/Backup/Session/{configurationId} | Initiates backup session using the specified configuration. | Backup configuration ID | Object with backup session details |
| GET | /webapi/Backup/Session/{sessionId} | Gets backup session. | Backup session ID | Object with backup session details |
| PUT | /webapi/Backup/Session/{sessionId} | Aborts backup session. | Backup session ID | Object with backup session details |
| POST | /webapi/Backup/SetElasticsearchRepository/{name} | Sets Elasticsearch snapshots repository. | Name of existing Elasticsearch snapshots repository | Status object |
| BehaviourState — scenarios and process elements | | | | |
| Method | Query | Description | Input | Output |
| GET | /webapi/BehaviourState/{solutionAlias} | Gets scenario and process element states in the specified application. | Application system name | Object with scenario and process element states |
| PUT | /webapi/BehaviourState/{solutionAlias} | Updates scenario and process element states in the specified application. | Object with scenario and process element states | Status object |
| CaseTemplate — case templates (legacy) | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/CaseTemplate/{solutionAlias} | Creates case template with/without related record template. | Application system name, case template properties object | Object with case template system name |
| PUT | /webapi/CaseTemplate/{solutionAlias} | Edits case template. | Application system name, case template properties object | Status object |
| DELETE | /webapi/CaseTemplate/{solutionAlias}/{caseTemplateAlias} | Deletes case template. | Application system name, case template system name | Status object |
| GET | /webapi/CaseTemplate/{solutionAlias}/{caseTemplateAlias} | Gets case template properties. | Application system name, case template system name | Case template properties object |
| PUT | /webapi/CaseTemplate/{solutionAlias}/{caseTemplateAlias}/Disable | Archives case template. | Application system name, case template system name | Status object |
| PUT | /webapi/CaseTemplate/{solutionAlias}/{caseTemplateAlias}/Enable | Unarchives case template. | Application system name, case template system name | Status object |
| GET | /webapi/CaseTemplate/List/{solutionAlias} | Gets all case templates in the specified application. | Application system name | Array of objects with case template properties |
| Dataset — tables | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Dataset/{solutionAlias} | Creates table. | Application system name, table configuration object | Table configuration object |
| PUT | /webapi/Dataset/{solutionAlias} | Edits table configuration. | Application system name, table configuration object | Status object |
| DELETE | /webapi/Dataset/{solutionAlias}/{datasetGlobalAlias} | Deletes table. | Application system name, table global alias: `Dataset@templateSystemName.tablesystemName` | Status object |
| GET | /webapi/Dataset/{solutionAlias}/{datasetGlobalAlias} | Gets table configuration. | Application system name, table global alias: `Dataset@templateSystemName.tablesystemName` | Table configuration object |
| GET | /webapi/Dataset/List/{templateGlobalAlias} | Gets all tables of the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Array of table configuration objects |
| Document — files attached to Document attributes | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Document | Creates document. | Document properties object | Object with document ID |
| PUT | /webapi/Document | Edits document properties. | Document properties object | Status object |
| DELETE | /webapi/Document/{documentId} | Deletes document. | Document ID | Status object |
| GET | /webapi/Document/{documentId} | Gets document properties. | Document ID | Document properties object |
| GET | /webapi/Document/{documentId}/Content | Gets document content. | Document ID | Document content (`application/octet-stream`) |
| POST | /webapi/Document/Content | Creates document by uploading a file. | Object with filename and content (`byte array`) | Object with document ID |
| POST | /webapi/Document/Revision/{documentId}/Content | Creates revision by uploading a file. | Document ID, object with filename and content (`byte array`) | Object with revision ID |
| GET | /webapi/Document/Revision/{revisionId} | Gets revision properties. | Revision ID | Revision properties object |
| GET | /webapi/Document/Revision/{revisionId}/Content | Gets revision content. | Revision ID | Revision content (`application/octet-stream`). |
| DocumentExportTemplate — export templates | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/DocumentExportTemplate/{solutionAlias} | Creates export template. | Application system name, object with export template properties | Export template system name |
| PUT | /webapi/DocumentExportTemplate/{solutionAlias} | Edits export template. | Application system name, object with export template properties | Status object |
| DELETE | /webapi/DocumentExportTemplate/{solutionAlias}/{exportTemplateGlobalAlias} | Deletes export template. | Application system name, export template global alias: `ExportTemplate@templateSystemName.exportTemplateSystemName` | Status object |
| GET | /webapi/DocumentExportTemplate/{solutionAlias}/{exportTemplateGlobalAlias} | Gets export template properties. | Application system name, export template global alias: `ExportTemplate@ templateSystemName.exportTemplateSystemName` | Object with export template properties |
| GET | /webapi/DocumentExportTemplate/List/{templateGlobalAlias} | Gets all export templates for the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Array of objects with export template properties |
| Form — forms and form rules (except process start forms and user task forms) | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Form/{solutionAlias} | Creates form. | Application system name, form configuration object | Form system name |
| PUT | /webapi/Form/{solutionAlias} | Edits form. | Application system name, form configuration object | Status object |
| DELETE | /webapi/Form/{solutionAlias}/{formGlobalAlias} | Deletes form. | Application system name, form global alias: `Form@templateSystemName.formSystemName` | Status object |
| GET | /webapi/Form/{solutionAlias}/{formGlobalAlias} | Gets form configuration. | Application system name, form global alias: `Form@templateSystemName.formSystemName` | Form configuration object |
| GET | /webapi/Form/FormRules/{solutionAlias}/{formGlobalAlias} | Gets form rules. | Application system name, form global alias: `Form@templateSystemName.formSystemName` | Form rules object |
| PUT | /webapi/Form/FormRules/{solutionAlias}/{formGlobalAlias} | Sets form rules. | Application system name, form global alias (`Form@templateSystemName.formSystemName`), form rules object. | Status object |
| GET | /webapi/Form/List/{templateGlobalAlias} | Gets all forms of the specified template. | Application system name, template global alias: `Template@solutionSystemName.templateSystemName` | Array of form configuration objects |
| SolutionGitIntegration — application version control via Git | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Git/AddRemoteBranch | Creates branch in the remote repository. | Repository and branch configuration object | Status object |
| POST | /webapi/Git/Connect | Initializes connection with the specified repository. | Repository configuration object | Status object |
| POST | /webapi/Git/GetRepositoryDetails | Gets repository commits. | Repository configuration object | Array of objects with commit properties |
| GET | /webapi/Git/GetUserConfiguration | Gets repository user credentials. |  | Object with repository user credentials |
| GET | /webapi/Git/GetUserSolutionConfig | Gets repository configuration and user details. |  | Object with repository configuration and user credentials |
| POST | /webapi/Git/ListBranches | Gets all repository branches. | Repository configuration object | Array of objects with branch properties |
| GET | /webapi/Git/ListRepositories | Gets all repositories of Git connections. |  | Array of repository configuration objects |
| POST | /webapi/Git/SaveUserCredentials | Saves user credentials. | Repository configuration and user credentials object | Status object |
| Heartbeat — server, process, scripts, and service status monitoring | | | | |
| Method | Query | Description | Input | Output |
| GET | /webapi/Heartbeat/Details | Gets service usage statistics. |  | Heartbeat details object |
| GET | /webapi/Heartbeat/IsAlive | Gets service availability status. |  | Status object |
| GET | /webapi/Heartbeat/ServerDetails | Gets server details. |  | Server information object |
| ProcessObjects — process diagram version migration | | | | |
| Method | **Query** | Description | Input | Output |
| POST | /webapi/ProcessObjects/Migrate | Changes process instances diagram version and moves tokens. | Process template global alias (`ProcessTemplate@applicationSystemName.templateSystemName`), target diagram ID, process instance IDs | Status object |
| ProcessTemplate — process templates | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/ProcessTemplate/{solutionAlias} | Creates process template. | Application system name, process template properties object | Process template system name |
| PUT | /webapi/ProcessTemplate/{solutionAlias} | Edits process template properties. | Application system name, process template properties object | Status object |
| DELETE | /webapi/ProcessTemplate/{solutionAlias}/{processTemplateAlias} | Deletes process template. | Application system name, process template system name | Status object |
| GET | /webapi/ProcessTemplate/{solutionAlias}/{processTemplateAlias} | Gets process template properties. | Application system name, process template system name | Process template properties object |
| PUT | /webapi/ProcessTemplate/{solutionAlias}/{processTemplateAlias}/Disable | Archives process template. | Application system name, process template system name | Status object |
| PUT | /webapi/ProcessTemplate/{solutionAlias}/{processTemplateAlias}/Enable | Unarchives process template. | Application system name, process template system name | Status object |
| GET | /webapi/ProcessTemplate/List/{solutionAlias} | Gets all process templates in the specified application. | Application system name | Array of objects with process template properties |
| Record — single record (except process templates) | | | | |
| Method | Query | Description | Input | Output |
| DELETE | /webapi/Record/{recordId} | Deletes record. | Record ID | Status object |
| GET | /webapi/Record/{recordId} | Gets record. | Record ID | Object with attribute values:  `{"attributeSystemName": "value"}` |
| PUT | /webapi/Record/{recordId} | Edits record. | Record ID, object with record attribute values:`[{"attributeSystemName": "value"}]` | Status object |
| POST | /webapi/Record/{recordId}/{deepClone} | Clones record. | Record ID, deep cloning flag (`true` — clone linked records) | Cloned record ID |
| PUT | /webapi/Record/{recordId}/Disable | Archives record. | Record ID | Status object |
| PUT | /webapi/Record/{recordId}/Enable | Unarchives record. | Record ID | Status object |
| POST | /webapi/Record/{templateGlobalAlias} | Creates record. | Application system name, template global alias (`Template@applicationSystemName.templateSystemName`), object with record attribute values: `[{"attributeSystemName": "value"}]` | Record ID |
| Records — multiple records and record export/import (except process templates) | | | | |
| Method | Query | Description | Input | Output |
| DELETE | /webapi/Records | Deletes specified records. | Array of record IDs | Status object |
| PUT | /webapi/Records | Edits specified records. | Array of record IDs and objects with record attribute values: `[{"attributeSystemName": "value"}]` | Status object |
| DELETE | /webapi/Records/{templateGlobalAlias} | Deletes all records from the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Status object |
| GET | /webapi/Records/{templateGlobalAlias} | Gets all records of the specified template. | Application system name, template global alias :`Template@applicationSystemName.templateSystemName` | Array of objects with record attribute values: `[{"attributeSystemName": "value"}]` |
| POST | /webapi/Records/{templateGlobalAlias} | Creates records. | Template global alias (`Template@applicationSystemName.templateSystemName`), array of objects with record attribute values: `[{"attributeSystemName": "value"}]` | Array of record IDs |
| GET | /webapi/Records/{templateGlobalAlias}/Export | Exports all records of the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Serialized records data |
| PUT | /webapi/Records/BulkEdit | Updates specified records with the same data. | Record properties and values to update | Status object |
| PUT | /webapi/Records/Disable | Archives specified records. | Array of record IDs | Status object |
| PUT | /webapi/Records/Enable | Unarchives specified records. | Array of record IDs | Status object |
| POST | /webapi/Records/Export | Exports specified records. | Record template global alias object, array of record IDs | Serialized records data |
| POST | /webapi/Records/Import | Imports records from a file. | ID of an uploaded file with serialized records data | The number of imported records |
| RecordTemplate — record templates | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/RecordTemplate/{solutionAlias} | Creates record template. | Application system name, record template properties object | Record template system name |
| PUT | /webapi/RecordTemplate/{solutionAlias} | Edits record template. | Application system name, record template properties object | Status object |
| DELETE | /webapi/RecordTemplate/{solutionAlias}/{recordTemplateAlias} | Deletes record template. | Application system name, record template system name | Status object |
| GET | /webapi/RecordTemplate/{solutionAlias}/{recordTemplateAlias} | Gets template by system name. | Application system name, record template system name | Record template properties object |
| PUT | /webapi/RecordTemplate/{solutionAlias}/{recordTemplateAlias}/Disable | Archives record template. | Application system name, record template system name | Status object |
| PUT | /webapi/RecordTemplate/{solutionAlias}/{recordTemplateAlias}/Enable | Unarchives record template. | Application system name, record template system name | Status object |
| GET | /webapi/RecordTemplate/List/{solutionAlias} | Gets all record templates in the specified application. | Application system name | Array of objects with record template properties |
| ReferenceData — records with specified attribute values | | | | |
| Method | Query | Description | Input | Output |
| DELETE | /webapi/ReferenceData/Delete | Deletes a record with specified key attribute values. | Template global alias object, object with key attribute system names and values | Deleted record ID. If several records are matched, returns null and no records are deleted |
| POST | /webapi/ReferenceData/Get | Gets attribute values of a record with specified key attribute values. | Template global alias object, object with key attribute system names and values, array of attribute system names to get | Object with record attribute values. If several records are matched, returns null and no records are returned |
| PUT | /webapi/ReferenceData/Put | Edits record with specified key attribute values. | Template global alias object, array of key attribute system names, object with key attribute system names and values, object with attribute system names and their new values | Edited record ID. If several records are matched, returns null and no records are edited |
| Solution — applications | | | | |
| Method | Query | Description | Input | Output |
| GET | /webapi/Solution | Gets all applications. |  | Array of objects with application properties |
| POST | /webapi/Solution | Creates application. | An object with application properties | Application system name |
| PUT | /webapi/Solution | Edits application properties. | An object with application properties | Status object |
| DELETE | /webapi/Solution/{solutionAlias} | Deletes application. | Application system name | Status object |
| GET | /webapi/Solution/{solutionAlias} | Gets application properties. | Application system name | Object with application properties |
| Toolbar — toolbars and buttons on them | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Toolbar/{solutionAlias} | Creates toolbar. | Application system name, toolbar configuration object | Toolbar system name |
| PUT | /webapi/Toolbar/{solutionAlias} | Edits toolbar. | Application system name, toolbar configuration object | Status object |
| DELETE | /webapi/Toolbar/{solutionAlias}/{toolbarGlobalAlias} | Deletes toolbar. | Application system name, toolbar global alias: `Toolbar@templateSystemName.toolbarAlias` | Status object |
| GET | /webapi/Toolbar/{solutionAlias}/{toolbarGlobalAlias} | Gets toolbar by system name. | Application system name, toolbar global alias: `Toolbar@templateSystemName.toolbarAlias` | Toolbar configuration object |
| GET | /webapi/Toolbar/List/{templateGlobalAlias} | Gets all toolbars for the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Array of toolbar configuration objects |
| Transfer — application model export/import | | | | |
| Method | Query | Description | Input | Output |
| GET | /webapi/Transfer/{fileId}/Validate | Validates application model. | Application model file ID | Validation summary object |
| GET | /webapi/Transfer/{solutionAlias} | Exports application model. | Application system name | An object with application model ZIP file in Base64 format and export summary |
| POST | /webapi/Transfer/{solutionAlias}/{fileId}/{publishAfterImport}/{policy} | Imports application model. | Application system name, application model ZIP/CTF file ID, imported process diagrams publishing flag (`true` — publish), behaviour state policy (`ApplyNew`, `ApplyOld`, `DisableAll`, or `EnableAll`). | Application import summary object |
| POST | /webapi/Transfer/Upload | Uploads application model file. | Application model ZIP file in Base64 format | An object with the uploaded file ID |
| UserCommand — buttons | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/UserCommand/{solutionAlias} | Creates button. | Application system name, button configuration object | Button system name |
| PUT | /webapi/UserCommand/{solutionAlias} | Edits button. | Application system name, button configuration object | Status object |
| DELETE | /webapi/UserCommand/{solutionAlias}/{userCommandGlobalAlias} | Deletes button. | Application system name, button global alias: `UserCommand@templateSystemName.userCommandAlias` | Status object |
| GET | /webapi/UserCommand/{solutionAlias}/{userCommandGlobalAlias} | Gets button configuration. | Application system name, button global alias: `UserCommand@templateSystemName.userCommandAlias` | Button configuration object |
| PUT | /webapi/UserCommand/{solutionAlias}/{userCommandGlobalAlias}/Disable | Archives button. | Application system name, button global alias: `UserCommand@templateSystemName.userCommandAlias` | Status object |
| PUT | /webapi/UserCommand/{solutionAlias}/{userCommandGlobalAlias}/Enable | Unarchives button. | Application system name, button global alias: `UserCommand@templateSystemName.userCommandAlias` | Status object |
| GET | /webapi/UserCommand/List/{templateGlobalAlias} | Gets all buttons of the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Array of button configuration objects |
| WorkerEngine — system services | | | | |
| Method | Query | Description | Input | Output |
| GET | /webapi/WorkerEngine/GetConfiguration | Gets system service statuses (`true` — enabled). |  | Object with system service statuses |
| PUT | /webapi/WorkerEngine/SetConfiguration | Sets system service statuses. | Object with system service statuses (`true` — enabled) | Status object |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
