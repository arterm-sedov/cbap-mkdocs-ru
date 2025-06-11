---
title: Adapters
tags:
    - adapters
    - adapter creation
    - connections
    - connection creation
hide:
    - tags
kbId: 4672
---

# Adapters. Definitions, Setup, Deletion {: #adapters }

<div class="admonition question" markdown="block">

## Definitions {: .admonition-title }

- An **Adapter** is a custom module for connecting **{{ productName }}** to external systems.
- An adapter includes a data model and methods for sending or receiving requests.
- To use an adapter, you need to upload and compile its source code on the **{{ productName }}** side.
- After compiling the adapter, you need to configure the appropriate connection, data transfer path, and scenario for interacting with the external system. See [Adapter Setup Procedure](#adapter-setup-procedure).

</div>

## Benefits of Using Adapters

Custom adapters provide the following benefits:

- speed and flexibility in implementing business-required data exchange methods;
- ability to process and transform data at specialized protocol level;
- processing of various data models using a single adapter;
- increased fault tolerance through data exchange with **{{ productName }}** via message broker.

## Adapter Setup Procedure

!!! warning "Attention"

    For successful adapter compilation, .NET libraries version 6.0 or higher must be installed on the **{{ productName }}** server.

1. [Define the data model](#building-data-model) to be transmitted through the adapter.
2. [Define the adapter logic](#adapter-structure) for sending and receiving data.
3. [Prepare a Visual Studio solution](#adapter-source-code-structure) with adapter source code in C#.
4. [Configure the server](#server-setup-for-adapter-operation) for adapter operation.
5. [Upload and compile the adapter](#viewing-adapter-list-and-adapter-setup) on the **{{ productName }}** server.
6. Configure the connection according to the protocol for connecting to the external system.
7. Configure the data transfer path according to the data model and logic for interacting with the external system.
8. Configure templates and scenario for processing requests using the adapter.

## Building Data Model

To develop an adapter, form a data model:

1. Prepare a description of the data structure in a standardized format (e.g., XML, JSON) or in the form of a table.
2. Convert the data structure description into C# adapter class models, for example using the autogenerator at <https://json2csharp.com/code-converters/xml-to-csharp>.
3. Modify the obtained model according to the required business logic.

## Adapter Structure

The adapter should consist of the following blocks:

- data serialization or deserialization block;
- data model description and conversion block for internal adapter models;
- adapter endpoint block that distributes requests between methods according to the adapter data model;
- service block responsible for Kestrel operation, message sending, timeouts, data validation, etc.

## Adapter Source Code Structure

Request a solution template from a **{{ companyName }}** representative. You can develop an adapter for your needs based on it.

The adapter is a Visual Studio solution consisting of the following components:

- project with adapter source code, including one solution file (`.sln`) in the root folder;
- subprojects containing interfaces for adapter development and subsequent compilation;
- subproject containing the main adapter functionality;
- additional subprojects, for example for localization;
- folder with pluggable libraries.

Package the finished solution in a ZIP archive for compilation in **{{ productName }}**.

_![Example of archive contents with adapter source code](img/adapter_archive_content.png)_
{% include-markdown ".snippets/pdfEndOfBlockHack.md" %}

The following designations are used below:

- `{AdapterName}` — adapter name used in the Visual Studio solution name and in the system adapter name in **{{ productName }}**. For example:
    - `IncomingAdapter` — adapter for receiving data;
    - `OutgoingAdapter` — adapter for sending data.
- `{communicationRouteName}` — name of the data transfer path implemented in the adapter.
- `{communicationRoutePath}` — relative path to the data transfer path.

### Projects in the Adapter

The Visual Studio solution should include the projects listed below.

These projects should be copied from the solution template.

In general, only the `{AdapterName}`, `CustomLocalization`, and `ExternalServiceContracts` projects should be modified.

- `{AdapterName}` — project with main adapter business logic for [receiving](#adapter-classes-and-methods-for-receiving-messages) and [sending](#adapter-classes-and-methods-for-sending-messages) messages.
- `IncomingService` or `OutgoingService` — project for processing incoming or outgoing messages in **{{ productName }}**.
- `Adapter` — basic adapter logic.
- `ConnectionManager` — dispatcher for connections to external services.
- `Heartbeat` — adapter state monitoring.
- `Localization.Adapter` — standard localized messages and adapter graphical interface.
- `MessageBroker.Api` — interfaces for interaction with the message broker service.
- `Platform.FormDefinition` — adapter graphical interface.
- Optional libraries:
    - `CustomLocalization` — message field localization and other text constants.
    - `ExternalServiceContracts` — external service message models.

### Adapter Classes and Methods for Receiving Messages

The `{AdapterName}` project must implement the `IIncomingConnectionService` interface using the following classes and methods for interacting with **{{ productName }}**:

- `Adapter` class

    | Method | Description |
    |---|---|
    | `GetName()` | Adapter name |
    | `GetDescription()` | Adapter description |
    | `GetVersion()` | Adapter version |
    | `GetSignatures()` | Description of all implemented data transfer paths |

- `Behaviour` folder
    - `{communicationRouteName}` folder
        - `{communicationRouteName}Performer` class

            | Method | Description |
            |---|---|
            | `{communicationRouteName}Performer()` | Formation of incoming message and response to it |
            | `RecognizeRawRequest()` | Definition of correspondences in the incoming message to internal data (mapping) |
            | `SendRawResponse()` | Call of `IIncomingConnectionService.OnReplyReceive(object message)` interface for successful response or `IIncomingConnectionService.OnErrorReceive(object message)` for sending error message (required method if waiting for synchronous response from **{{ productName }}** is enabled) |

        - `{communicationRouteName}IncomingService` class (inherits from `GenericIncomingConnectionService`)

            | Property | Description |
            |---|---|
            | `IsWaitResponse` | Definition of waiting for synchronous response from **{{ productName }}** |
            | `Integration` | Integration type |

    - `Service` class

        | Method / Property | Description |
        |---|---|
        | `CreatePerformer()` | Initialization of incoming message reception |
        | `OnStart()` | Call of `IIncomingConnectionService.Subscribe` interface when creating or enabling data transfer path on **{{ productName }}** server |
        | `OnStop()` | Call of `IIncomingConnectionService.Unsubscribe` interface when deleting or disabling data transfer path on **{{ productName }}** server |
        | `PerformTest()` | Service operability check using `IIncomingConnectionService.PerformTest` interface |
        | `GetEndpointConfigs()` | Getting list of connections with `{сommunicationRoutePath}` specified in `Route` property |
        | `KestrelConfig` | Initialization of list of connections to `Kestrel`, including `EndpointConfig` |
        | `GetIncomingService()` | Initialization of data transfer path |

- `Configuration` folder
    - `Endpoint` class

        | Property | Description |
        |---|---|
        | `Endpoint` | Creation of connection to external service |
        | `EndpointForm` | Form for connection setup |

    - `Procedure` class

        | Property | Description |
        |---|---|
        | `Procedure` | Data transfer path configuration |
        | `SignatureForm` | Form for data transfer path setup |

- `Signature` folder
    - `{communicationRouteName}ExternalMessage` class

        | Property | Description |
        |---|---|
        | `{communicationRouteName}ExternalMessage` | External service message model |

    - `{communicationRouteName}IncomingMessage` class

        | Property | Description |
        |---|---|
        | `{communicationRouteName}IncomingMessage` | Incoming message model, necessarily inherited from `Comindware.Adapter.Message` with required `Display` property for localization of each attribute via `CustomLocalization` |

    - `ErrorMessage` class

        | Property | Description |
        |---|---|
        | `ErrorMessage` | Error message model inherited from `Comindware.Adapter.Message` |

    - `ResponseMessage` class

        | Property | Description |
        |---|---|
        | `ResponseMessage` | Response message model inherited from `Comindware.Adapter.Message` |

    - `{communicationRouteName}Signature` class

        | Method | Description |
        |---|---|
        | `GetIncomingMessageType()` | Definition of incoming message type after its conversion to internal data |
        | `GetOutgoingMessageType()` | Definition of successful response message type |
        | `GetErrorMessageType()` | Definition of error message type |

### Adapter Classes and Methods for Sending Messages

The `{adapterName}` project must implement the `IOutgoingConnectionService` interface using the following classes and methods for interacting with **{{ productName }}**:

- `Adapter` class

    | Method | Description |
    |---|---|
    | `GetName()` | Adapter name |
    | `GetDescription()` | Adapter description |
    | `GetVersion()` | Adapter version |
    | `GetSignatures()` | Description of all implemented data transfer paths |

- `Behaviour` folder
    - `{communicationRouteName}` folder
        - `{communicationRouteName}Performer` class

            | Method | Description |
            |---|---|
            | `TranslateIncomingMessage()` | Definition of correspondences in internal message to external data (mapping) |
            | `SendRawRequest()` | Sending message to external service |
            | `RecognizeRawResponse()` | Processing of external service response |

        - `{communicationRouteName}OutgoingService` class (inherits from `GenericOutgoingConnectionService`)

            | Method / Property | Description |
            |---|---|
            | `Execute()` | Implementation of outgoing requests |
            | `ConnectionConfigData` | Connection configuration to external server |

    - `Service` class

        | Method / Property | Description |
        |---|---|
        | `CreatePerformer()` | Initialization of outgoing message sending |
        | `PerformTest()` | Connection check with external service |
        | `GetEndpointConfigs()` | Getting list of connections with `{сommunicationRoutePath}` specified in `Route` property |

- `Configuration` folder
    - `Endpoint` class

        | Property | Description |
        |---|---|
        | `Endpoint` | Properties for creating connection to external service |
        | `EndpointForm` | Form for connection setup |

    - `Procedure` class

        | Property | Description |
        |---|---|
        | `Procedure` | Data transfer path configuration |

- `Signature` folder
    - `{communicationRouteName}ExternalMessage` class

        | Property | Description |
        |---|---|
        | `{communicationRouteName}ExternalMessage` | External service message model |

    - `{communicationRouteName}Request` class

        | Property | Description |
        |---|---|
        | `{communicationRouteName}Request` | Request message model inherited from `Comindware.Adapter.Message` |

    - `ErrorMessage` class

        | Property | Description |
        |---|---|
        | `ErrorMessage` | Error message model inherited from `Comindware.Adapter.Message` |

    - `ResponseMessage` class

        | Property | Description |
        |---|---|
        | `ResponseMessage` | Response message model inherited from `Comindware.Adapter.Message` |

    - `{communicationRouteName}Signature` class

        | Method | Description |
        |---|---|
        | `GetIncomingMessageType()` | Definition of incoming message type after its conversion to internal data |
        | `GetOutgoingMessageType()` | Definition of successful response message type |
        | `GetErrorMessageType()` | Definition of error message type |

## Server Setup for Adapter Operation

1. Switch to superuser mode:

    --8<-- "linux_sudo.md"

2. Open the NGINX configuration file for editing (`instanceName` — software instance name):

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        nano /etc/nginx/sites-available/comindware<instanceName>
        ```

    - **RED OS**, **Rocky** (RPM-based)

        ``` sh
        nano /etc/nginx/conf.d/comindware<instanceName>
        ```

    - **Alt Server**

        ``` sh
        nano /etc/nginx/sites-available.d/comindware<instanceName>
        ```

3. Add the following directives for each data transfer path (`communicationRoutePath` — relative path to data transfer path, `hostName` — **{{ productName }}** server address, `portNumber` — port on which the adapter is available):

    !!! warning "NGINX Setup Features for Adapters"

        The port on which the adapter is available must be different from the **{{ productName }}** server port number.

    ``` cs
    location <communicationRoutePath> {
                proxy_pass https://<hostName>:<portNumber>;
        }
    ```

## Viewing Adapter List and Adapter Setup

1. On the [**Administration** — **Infrastructure**][administration] page, select **Adapters** <i class="fa-light fa-puzzle-piece-simple">‌</i>.
2. The list of adapters will be displayed.

    _![Adapter list](adapter_list.png)_

3. Click the **Create** button or double-click the row of an existing adapter.
4. The adapter properties page will be displayed.

    _![Adapter properties page](adapter_properties.png)_

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

5. In the **Adapter Source Code** field, upload a ZIP archive with adapter source code. The archive must contain a prepared Visual Studio solution. See [Adapter Structure](#visual-studio-solution-structure).
6. Click the **Save** button.
7. Click the **Publish** button to compile the adapter.
8. If the adapter compilation is successful, its name will be displayed in the adapter list and adapter properties. The name is taken from the Visual Studio solution files.
9. After compilation, view the **compilation log**.

    _![Example of compilation log](adapter_compilation_log.png)_

10. If necessary, download the archive with adapter operation logs (of the form `_CBAP.adapters.20221026.logs.zip_`) by clicking the **Download Operation Log** button.

    _![Example of adapter operation log](adapter_execution_log.png)_

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

11. An item with the connection name for the compiled adapter will appear in the **Create** — **Custom Connections** menu on the **[Connections][connections]** and **[Data Transfer Paths][communication_routes]** pages. In this case, a corresponding **message type** will be provided for each data model in the data transfer path.

_![Creating connection using adapter](adapter_custom_connection_create_menu.png)_

_![Creating data transfer path using adapter](adapters_custom_communication_route_create_menu.png)_

## Monitoring Adapter Operation

You can use built-in monitoring tools to check adapter operation.

- On the adapter properties page, download the archive with its operation logs by clicking the **Download Operation Log** button. This log contains the following information about adapter operation:
    - status of adapter services;
    - status of adapter connection;
    - method availability;
    - allocated memory volume;
    - information about created data transfer paths;
    - adapter interaction with the Kafka service.

    See also _“[Adapter Logs][logging_engine_adapter_logs]”_ and _“[Event in Adapter][log_files_event_examples_adapter_event]”_.

- In the **[Connections][connections]** adapter properties, click the **Download Log** button. This log contains the following events:
    - connection status;
    - receiving or sending messages;
    - starting message processing scenario;
    - using adapter methods.

    See also _“[Connection Status][log_files_event_examples_connection_status]”_

- View events of receiving or sending requests and associated event chains:
    - Open the **Administration** — **[Event Logs][logs]** page.
    - Go to the **Event Trace** tab.
    - View events of type **Request Received** and **Request Sent** related to adapter operation by double-clicking the event row.

    See also _“[Viewing Event Chain][logs_event_chain_view]”_.

## Deleting Adapter {: .pageBreakBefore }

!!! warning "Attention!"

    Data transfer paths and connections generated for the deleted adapter will become inactive and stop working.

1. Open the [adapter list](#viewing-adapter-list-and-adapter-setup).
2. Set the checkbox in the first column for the adapter to be deleted.
3. Click the **Delete** button.
4. Confirm adapter deletion.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Connections. Definitions, Types, Creation, Setup, Deletion][connections]_
- _[Event Logs. Types, Viewing, Event Chains][logs]_
- _[Examples of Events in File Logs][log_files_event_examples]_
- _[Logging Subsystem][logging_engine]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
