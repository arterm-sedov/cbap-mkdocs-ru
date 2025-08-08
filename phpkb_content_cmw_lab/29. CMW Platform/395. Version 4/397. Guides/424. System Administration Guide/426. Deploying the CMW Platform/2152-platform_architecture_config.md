---
title: CMW Platform Architecture, Landscape, and Software &amp; Hardware Configuration
kbId: 2152
---


# CMW Platform Architecture, Landscape, and Software &amp; Hardware Configuration

Version: 1.0

Published: 07.04.2023

## Introduction

The CMW Platform is a low-code business process management software powered by a modern technology stack.

This article contains:

- Brief description of the CMW Platform architecture
- Recommended deployment landscape options
- Recommended software and hardware configurations

## Definitions

**Product** — CMW Platform software.

**Instance** — deployed CMW Platform website.

**System** — complete hardware and software environment powered by the CMW Platform.

**Application server** — deployed instance of the CMW Platform.

**Application** — standalone business solution running on the application server.

**Active users** — users who regularly generate data on the application server.

**DAS** — storage device directly connected to the application server.

**SAN** — storage area network.

**IOPS** — throughput expressed as a number of input/output operations per second.

## System Architecture

The System architecture is client-server, component-multilayer, and service-oriented. It supports extension via plugins and adapters.

The System comprises the following subsystems:

- *Web application*: single page application (SPA) based on Marionette, Backbone, React, and Redux.
- *Mobile app*: React Native powered by Expo.
- *Backend*: service components based on .NET 6.0, .NET Framework 4.8 (Windows), Mono 6.12 (Linux), and JDK 17.
- *Database management system (DBMS)*: CMW Elastic Data (proprietary) that stores the data in the file system or the Apache Ignite (depending on the load requirements and deployment configuration).
- *Full-text search engine*: Lucene.NET.
- *Transaction logging and analysis, and System**data monitoring*: Elasticsearch, Kibana.
- *File logging*: NLog.
- *Integration modules*: see [Integration with External Systems](#mcetoc_1g7eann3f2).

![CMW Platform architecture diagram](https://kb.cmwlab.com/assets/CMW_Platform_Architecture_EN_v1.6.svg)

*CMW Platform architecture diagram*

### System Security and Resilience

The System supports the following security and fault tolerance mechanisms.

- *External security*:
  - Kerberos and OpenID user authentication,
  - firewall,
  - reverse proxy.
- *Internal security*: role-based security model.
- *Fault tolerance:*redundant servers, data storage, and processing nodes.
- *Scalability*: additional request-processing servers.

### Integration with External Systems

The System supports the following external integration types.

- *Git* — version control for applications created in the System.
- *OData* — communication with external systems via the REST API.
- *OpenLDAP (Active Directory)* — authentication, account management, and single sign-on.
- *SMTP/IMAP/Exchange* — receiving and sending e-mail.
- *ESB ( RabbitMQ/MSMQ)* — communication with external systems in distributed and federated environments.

## System deployment landscape

To ensure uninterrupted operation, deploy the System in an environment with adequate performance and fault tolerance.

You can deploy the System for internet or intranet access:

- *Minimum configuration* — deploy on one virtual or physical machine.
- *Production configuration —* deploy on the customer's premises in a fault-tolerant landscape per the customer's requirements.

### Recommended System Deployment Options

#### Minimum Configuration

A minimal System configuration suitable for demonstrations and pilot projects comprises the following components:

1. CMW Platform instance.
2. CMW Elastic Data DBMS.
3. Elasticsearch server in a single-node configuration to log transactions and data changes.

![Minimal System configuration](https://kb.cmwlab.com/assets/CMW_Platform_Minimal_Configuration_EN.svg)

Minimum System configuration

#### Production Configuration

A production System configuration with resource duplication, redundancy, and fault tolerance includes the following components.

1. CMW Platform instance.
2. CMW Elastic Data DBMS.
3. Elasticsearch server to log transactions and data changes.
4. NGINX reverse proxy to filter out unwanted requests and relay valid requests to the internal network.
5. Zabbix server to monitor service availability and free disk space.
6. Mail server (SMTP/IMAP) (optional) to send notifications.
7. LDAP server (optional) for centralized management of the network infrastructure.
8. Git server (optional) for version control of the applications built with the CMW Platform.

_![Production System configuration](https://kb.cmwlab.com/assets/CMW_Platform_Production_Configuration_EN.svg)_

Production use scenarios impose the following System requirements.

- *Security* — implemented by setting up a firewall and a reverse proxy server.
- *Fault tolerance* — implemented by setting up the redundant servers and additional data server nodes.
- *Scalability* — implemented by adding more request-processing servers.

_![Typical landscape of the System services](https://kb.cmwlab.com/assets/CMW_Typical_Service_Landscape_EN.svg)_

### Recommended Set of Application Servers

To improve application development and testing efficiency, as well as application fault tolerance and security, deploy several application servers.

When defining the technical requirements, determine the need for each of these servers:

1. *Development server* to develop the applications.
2. *Testing server (pre-production)* to test the applications.
3. *Primary server (production)* to run the applications.
4. *Standby server* to use in case of primary server overload or failure.

## The System Hardware Configuration

See below the recommended hardware specifications to deploy the System at the customer's premises under Windows or Linux.

### Application Server Configuration

The application server provides user and third-party system interaction, data input, processing, and storage (database, configuration, uploaded files, logs, and backups).

Host the application server on a physical or virtual machine.

The following guidelines will help you configure the application server hardware.

In a minimum configuration, you can deploy a single application server to develop, test, and run the applications.

The following recommended specifications provide a comfortable experience for the end users, citizen developers, and testers of the CMW Platform applications.

Actual hardware requirements may vary significantly and depend on the following factors:

- number of active users,
- number of applications,
- number of running processes,
- number of configured calculations, rules, conditions, and data dependencies,
- size of stored data and documents.

We recommend deploying the subsystems (Apache Ignite, Elasticsearch, NGINX, Zabbix) and the Product instance virtual machines on different physical machines.

Communication channels between the System nodes must provide at least 10 Gbps bandwidth.

#### An Example Hardware Resource Calculation for a Fault-Tolerant System

The table below shows an example of hardware allocation for the following number of users:

- 500 registered
- 200 active
- 25 online

| **Server name** | **Description** | **Logical CPU cores, 3.0 GHz and above** | **RAM, GB** | **Data storage, GB** | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Software partition** **SSD** | **Database** **Highly reliablehigh speed** **SSD** | **Uploads** **HDD** | **Logs** **HDD** | **Backups** **HDD** |
| **Infrastructure services** | | | | | | | | |
| NGINX-reverse-proxy1 | Reverse proxy (VPS) | 2 | 2 | 24 |  |  |  |  |
| NGINX-reverse-proxy2 | Reverse proxy (VPS) | 2 | 2 | 24 |  |  |  |  |
| Zabbix1 | Monitoring and tracking system (VPS) | 2 | 4 | 24 | 128 |  |  |  |
| Zabbix2 | Monitoring and tracking system (VPS) | 2 | 4 | 24 | 128 |  |  |  |
|  |  |  |  |  |  |  |  |  |
| **Production environment** | | | | | | | | |
| CMWP-node1\* | CMW Platform application server (VPS) | 8 | 32 | 64 | 128 | 1024 | 16 | 512 |
| CMWP-node2\* | CMW Platform application server (VPS) | 8 | 32 | 64 | 128 | 16 |
| CMWP-node3\* | CMW Platform application server (VPS) | 8 | 32 | 64 | 128 | 16 |
| Elasticsearch-node1\* | Elasticsearch logging server (VPS) | 4 | 16 | 24 | 128 |  | 16 | 512 |
| Elasticsearch-node2\* | Elasticsearch logging server (VPS) | 4 | 16 | 24 | 128 |  | 16 |
| Elasticsearch-node3\* | Elasticsearch logging server (VPS) | 4 | 16 | 24 | 128 |  | 16 |
| \* Virtual servers of the same service must be hosted on different physical machines. | | | | | | | | |
| The connection speed between the servers must be at least 10 Gbps. | | | | | | | | |
|  | | | | | | | | |
| **Test and development environment** | | | | | | | | |
| Git-server | GitLab | 2 | 4 | 24 | 128 |  |  |  |
| CMWP-test | CMW Platform application server (VPS) | 8 | 24 | 64 | 128 | 32 | 16 | 128 |
| CMWP-dev | CMW Platform application server (VPS) | 8 | 24 | 64 | 128 | 32 | 16 | 128 |
| Elasticsearch | Elasticsearch logging server (VPS) | 4 | 16 | 24 | 128 |  | 16 | 128 |
|  |  |  |  |  |  |  |  |  |
| **Total by resource type** | | **66** | **224** | **536** | **1536** | **1088** | **144** | **1408** |

#### Minimum Primary and Backup Application Server Configuration

| **Number of users** | **CPU cores** 3.7 GHz and above (Add 1 core per 100 active users per application) | **RAM, GB(Add 4GB** per 100 active users per application) | **HDD, GB** | **SSD, GB** |
| --- | --- | --- | --- | --- |
| **Primary Application Server** | | | | |
| 1–200 active | 4 + (1 × app qty) | 16 + (4 × app qty) | 16 | 16 |
| 200 active | 4 + (2 × app qty) | 16 + (8 × app qty) | 16 × app qty | 16 × app qty |
| 300 active | 4 + (3 × app qty) | 16 + (12 × app qty) | 16 × app qty | 16 × app qty |
| 400 active | 4 + (4 × app qty) | 16 + (16 × app qty) | 16 × app qty | 16 × app qty |
| **Standby Application Server** | | | | |
| 1­–200 | 4 + (1 × app qty) | 16 + (4 × app qty) | 16 × app qty | 8 × app qty |
| 200 | 4 + (2 × app qty) | 16 + (8 × app qty) | 16 × app qty | 8 × app qty |
| 300 | 4 + (3 × app qty) | 16 + (12 × app qty) | 16 × app qty | 8 × app qty |
| 400 | 4 + (4 × app qty) | 16 + (16 × app qty) | 16 × app qty | 8 × app qty |

#### Minimum Development and Test Server Configuration

| **Number of users** | **CPU cores** 3.7 GHz and above | **RAM,GB** | **HDD,GB** | **SSD,GB** |
| --- | --- | --- | --- | --- |
| **Development server** | | | | |
| 1–100 | 4 | 16 | 16 | 16 |
| **Test server** | | | | |
| 1–100 | 4 | 16 | 16 | 16 |

### Storage Configuration

In a minimum configuration, all application server data folders can be stored on a single partition on a high-performance SSD.

High-performance storage systems (SSD DAS/SAN) must provide a throughput of at least 100,000 IOPS per application server.

When defining the System specifications, determine the amount of space allocated on the high-performance (SSD DAS/SAN) and low-performance storage systems (HDD DAS/SAN).

To optimize data processing, storage, and backup, configure separate storage for the application server data folders:

- *Database and configuration files* — SSD DAS/SAN. The application server constantly processes this data online, which creates a high load on the storage subsystem.
- *Files uploaded by users* — HDD DAS/SAN. Uploaded files are stored for a long time and outside of the database. They are fetched via links. Hence, a high-performance storage subsystem is optional for them.
- *System logs* — HDD DAS/SAN. Log file writing operations create a minimal load on the storage subsystem.
- *Backups* — HDD DAS/SAN. Backups are created periodically and rarely used. For their storage, the volume is more important than the performance. However, the backup speed may decrease if there are many small uploaded files. In this case, place the backup folder on a high-performance drive.
- *Temporary folder* — SSD DAS/SAN. The temporary file storage and processing load may increase due to various factors, such as many active users and transactions, users uploading many files, etc.

## Change Log

| Date | Version | Changes |
| --- | --- | --- |
| 07.04.2023 | 1.0 | Original version. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
