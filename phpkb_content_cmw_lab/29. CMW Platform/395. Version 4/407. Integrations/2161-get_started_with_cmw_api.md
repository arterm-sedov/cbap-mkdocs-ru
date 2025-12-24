---
title: Get Started With CMW API
kbId: 2161
---


# Get Started With CMW API

## Introduction

The **CMW Platform** can communicate with external system APIs via **connections**and   **communication routes** and can also process requests from external systems via the three **REST APIs**:

- [**Solution API**](https://kb.comindware.ru/article.php?id=2074)
- **System Core API**
- [**Web API**](https://kb.comindware.ru/article.php?id=1941)

### Definitions

- **API** (Application Programming Interface) is a set of methods, classes, libraries, and functions that enable communication between different systems.
- **REST API** is an API that conforms to the Representational State Transfer architecture. The REST API allows you to efficiently utilize HTTP, scale services, and develop applications using almost any programming language in compliance with the REST design principles:
  - Stateless — the server does not store the request state. Each incoming request contains all the data necessary to process it and is processed independently of other requests.
  - Uniform interface — the server transmits data in a well-defined format.
  - Client and server independence — the client can interact with the server only through the resource URI. The server can only transfer the requested data to the client via HTTP.
  - Resource cacheability — responses indicate their cacheability. Resources can be cached at the server or client.
  - Layered architecture — the client can connect to authorized intermediaries between the client and the server to receive responses from the server, and the server can forward requests to other servers.
  - Code on demand (optional) — the server can extend the client capabilities by transferring executable logic, for example, to validate user-entered data.
- **RESTful** is a web service that implements the **REST** architecture.
- **Resource** is an object or information in an application, such as a template, account, or document, that an API provides access to.
- **Resource URI** is a Uniform Resource Identifier in an API.
- **Client** is a person or system that accesses resources via an API.
## Access the API

In its simplest case, **RESTful** services send and receive HTTP requests in a URL string to retrieve or send data, execute a command, or perform another action.

To configure integrations using **REST API**, you can follow this general principle:

- Develop an integration scenario — which system initiates the API call, how often, what methods it uses to transfer what data, what happens next, etc.
- Use the API documentation to test requests, configure connections, and generate final production requests.

### API Methods

The **CMW Platform** supports the following API methods:

- `GET` — get a list of all records.
- `GET {id}` — get a record with identifier   `{id}`.
- `DELETE {id}` — delete a record with identifier   `{id}`.
- `POST` — create a new record.
- `PUT {id}` — change a record with identifier   `{id}`.

### Initiate a Request From an External System

The **CMW Platform** can receive HTTP API requests in two ways:

- `GET` or   `DELETE` request as a URL string containing all request parameters.
  - The external system sends the request in a URL string. You can generate a query template for an external system using [Swagger](#mcetoc_1h7csahj80).
  - You can test this request in a browser: copy the received   **Request URL** into the address bar and press `Enter`. If you are logged in to the **CMW Platform**, no authentication is needed.
- `POST` or   `PUT` request with a body containing all the parameters (e.g., username and password, data to send or receive, etc.).
  - The external system sends a request in JSON or XML format. You can generate a query template for an external system using [Swagger](#mcetoc_1h7csahj80).
  - This option is more flexible, allowing you to transfer more data in a structured form. But you can't test this type of request in a browser. You can test it using the built-in Swagger or external services like Postman, SoapUI, Insomnia, etc.
- **CMW Platform** returns a response in JSON or XML format.

### Authenticate External System to Access CMW API

The   **CMW Platform** API supports two methods to authenticate external systems:

- Basic authentication — specify the username and password of the account used to execute the request.
- HMAC — specify the token and secret key generated for the account on the **Administration** –   **Authentication Keys** page.

Notes

- To use API and [Swagger](#mcetoc_1h7csahj80), you should create a special account and grant it the **API calls** permission in a system role. Also, the API and Swagger are available to users in the   **System Administrators** system role.
- When calling API methods in the   [Swagger](#mcetoc_1h7csahj80) using the `https://your-host/docs` page, you're logged in to the **CMW Platform**, and no authentication is required.
- When calling API methods from an external system, you must add request headers to authenticate using the account with API access.
- Most external systems provide means to configure the authentication method. Otherwise, add the `Authorization` parameter to the request `Header` containing the username and password encrypted in `Base64` format.
### Initiate External API Request

The **REST API** is adopted widely, and you can often find **API** documentation for a specific system by googling: *<system name> REST API*.

The   **CMW Platform**can access external APIs using the following methods:

- A C# script (triggered by a button or a process script task) establishes a connection to an external system, generates a request, sends it, and receives a response.
- A scenario generates and sends the request through a configured external system connection. The script generates the request body, analyze the response, and place the response data into post attributes.
- A send message intermediate or end event in a process generates and sends the request.

Note

To send requests using scripts or process events, you need to configure an external service connection and communication route.

### Authenticate CMW Platform to Access External API

When accessing an external API, use the authentication method supported by the external system. Refer to the external API documentation and see if you must include the username and password in the request URL or body or generate and use a security token instead of sending the password in plain text.

## Use Swagger

The **CMW Platform** provides a built-in API sandbox powered by Swagger.

- Swagger provides a detailed reference on API methods, including request and response descriptions, and data models with example values.
- Swagger allows you to execute requests and view responses.
- When executing a request, Swagger generates an API resource URI to use in external systems, including the request body syntax template.

1. To open the Swagger page, enter   `https://your-host/docs`, where   `your-host` is the domain name of your server, in your browser address bar.
2. The **CMW Platform API** page appears with the following sections:
   - **RESTful Web API** —immutable methods common for all software versions (see [Web API Methods](https://kb.comindware.ru/article.php?id=1941));
   - **System Core API** — system methods that may differ for different software versions;
   - **Solution API** — methods for business application templates (see [Solution API Methods](https://kb.comindware.ru/article.php?id=2074)).
3. Go to the required API page.
4. Expand an API method in the list.
5. Select the request and response format in the **Response Content Type** field.
6. Run a method by clicking **Try it out**.
7. The request template will be generated: 
   - **Request URL** — copy this string to an external system as the request URI. For `GET` and   `DELETE` requests, it contains the entire request.
   - **Example Value** — copy this string to an external system as the request body.

_![Swagger page with the CMW Platform API sections](https://kb.cmwlab.com/assets/img_661e5cf63fc5a.png)_

## Example: Call a System Core API Method

To create a record template using the System Core API, send the following `POST` request to the **Request URL**obtained in Swagger:

```
http://your-host/api/public/system/TeamNetwork/ObjectAppService/Create
```

- `Substitute your-host` with your **CMW Platform** instance URL.
- In the request `body`, specify the system name of the record template (for example,   `"Car"`).
- In the response, the **CMW Platform**will return the ID of the created record template (for example,   `"oa.1"`).

## Related Articles

**[Solution API Methods](https://kb.comindware.ru/article.php?id=2074)**

**[Web API Methods](https://kb.comindware.ru/article.php?id=1941)**

 [*‌*Back to top](#)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
