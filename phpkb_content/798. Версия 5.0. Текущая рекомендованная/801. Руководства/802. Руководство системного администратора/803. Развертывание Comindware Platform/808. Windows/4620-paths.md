---
title: Пути и содержимое директорий экземпляра ПО
kbId: 4620
---

# Пути и содержимое директорий экземпляра ПО

## Введение

Здесь представлена информация о расположении файлов и директорий экземпляра ПО **{{ productName }}**.

Ознакомьтесь также с [рекомендациями по настройке путей](#paths_recommendations).

## Содержимое директорий — Linux

По умолчанию файлы экземпляра ПО находятся в директории `/var/lib/comindware/<instanceName>`

Здесь и далее `<instanceName>` — имя экземпляра ПО.

Фактические пути к директориям экземпляра ПО указаны в файле конфигурации:

```
/usr/share/comindware/configs/instance/<instanceName>.yml

```

**Пути по умолчанию**

- `/usr/share/comindware/configs/instance/<instanceName>.yml` — файл конфигурации. В этом файле задаются все остальные пути, перечисленные ниже.
- `/var/www/<instanceName>` — исполняемые и конфигурационные файлы экземпляра ПО:

  - `logs.config` — конфигурация журналов, см. *«[Подсистема журналирования][logging_engine]»*;
  - `adapterhost.yml` — конфигурация службы Adapterhost;
  - `apigateway.yml` — конфигурация службы Apigateway;
  - `Ignite.config` — конфигурация Apache Ignite.
- `/var/lib/comindware/<instanceName>/Database/db` — файлы базы данных.
- `/var/lib/comindware/<instanceName>/Database/log` — файлы журналов Apache Ignite.
- `/var/log/comindware/<instanceName>/Logs/` — файлы журналов.
- `/var/lib/comindware/<instanceName>/Database/Scripts` — скомпилированные библиотеки для скриптов на языке С#.
- `/var/lib/comindware/<instanceName>/Streams` — загруженные пользователями и сформированные системой файлы, которые прикреплены к соответствующим атрибутам.
- Вспомогательные файлы:
  - `/var/lib/comindware/<instanceName>/Database/git` — файлы локального репозитория Git для управления версиями приложений.
  - `/var/lib/comindware/<instanceName>/Database/FullTextSearch` — индексы полнотекстового поиска.
  - `/var/lib/comindware/<instanceName>/Database/snapshots` — снимки данных Apache Ignite.
  - `/var/lib/comindware/<instanceName>/Database/wal` — файлы журнала предварительной записи.
- Временные файлы:
  - `/var/lib/comindware/<instanceName>/Temp`
  - `/var/lib/comindware/<instanceName>/LocalTemp`

## Содержимое директорий — Windows

По умолчанию файлы экземпляра ПО находятся в директории с экземпляром ПО: `C:\\ProgramData\\Comindware\\Instances\\<instanceName>`.

Здесь и далее `<instanceName>` — имя экземпляра ПО.

Фактические пути к директориям экземпляра ПО указаны в файле конфигурации:

```
C:\\ProgramData\\сomindware\\configs\\instance\\<instanceName>.yml

```

**Пути по умолчанию**

- `C:\\Program Files\\Comindware\\CBAP` — исполняемые файлы ПО разных версий.
- `C:\\ProgramData\\сomindware\\configs` — общие файлы конфигурации ПО.
- `C:\\ProgramData\\сomindware\\configs\\instance\\<instanceName>.yml` — файл конфигурации. В этом файле задаются все остальные пути, перечисленные ниже.
- `C:\\ProgramData\\сomindware\\Instances` — папка с экземплярами ПО.
- `C:\\ProgramData\\сomindware\\Instances\\<instanceName>` — экземпляр ПО.
- `C:\\ProgramData\\сomindware\\Instances\\<instanceName>\\config` — исполняемые и конфигурационные файлы экземпляра ПО.:
  - `logs.config` — конфигурация журналов, см. *«[Подсистема журналирования][logging_engine]»*;
  - `adapterhost.yml` — конфигурация службы Adapterhost;
  - `apigateway.yml` — конфигурация службы Apigateway;
  - `Ignite.config` — конфигурация Apache Ignite.
- `C:\\ProgramData\\сomindware\\Instances\\<instanceName>\\Database` — файлы базы данных.
- `C:\\ProgramData\\сomindware\\Instances\\<instanceName>\\Database\\Scripts` — DLL-файлы, скомпилированные из скриптов на языке C#.
- `C:\\ProgramData\\сomindware\\Instances\\<instanceName>\\Streams` — файлы, загруженные пользователями и сформированные ПО.
- `C:\\ProgramData\\сomindware\\Instances\\<instanceName>\\Logs` — журналы экземпляра ПО.
- Вспомогательные файлы:
  - `C:\\ProgramData\\сomindware\\Instances\\<instanceName>\\Database\\git` — файлы локального репозитория Git для управления версиями приложений.
  - `C:\\ProgramData\\сomindware\\Instances\\<instanceName>\\Database\\FullTextSearch` — индексы полнотекстового поиска.
  - `C:\\ProgramData\\сomindware\\Instances\\<instanceName>\\Database\\snapshots` — снимки данных Apache Ignite.
  - `C:\\ProgramData\\сomindware\\Instances\\<instanceName>\\Database\\wal` — файлы журнала предварительной записи.
- Временные файлы:
  - `C:\\ProgramData\\сomindware\\Instances\\<instanceName>\\Temp`
  - `C:\\ProgramData\\сomindware\\Instances\\<instanceName>\\LocalTemp`

## Рекомендации по настройке путей

Для более стабильной и надёжной работы платформы, рекомендуем разделить данные по нескольких хранилищам, например, как указано ниже.

- **Хранилище исполняемых и конфигурационных файлов**
  - ПО **{{ productName }}** и конфигурационные файлы экземпляра ПО.
  - `<instanceName>.yml`: файл конфигурации экземпляра ПО.
- **Хранилище базы данных**
  - `Database`: файлы базы данных.
  - `Database/Scripts`: скомпилированные C#-скрипты.
- **Хранилище журналов**
  - `Logs`: журналы экземпляра ПО.
- **Хранилище резервных копий**
  - `Backups`: файлы резервных копий.
- **Хранилище загружаемых и временных файлов**

  - `LocalTemp`: временные файлы резервных копий.
  - `Temp`: временные копии загруженных файлов и скомпилированных C#-скриптов.
  - `Streams`: файлы, загружаемые пользователями и сформированные ПО.

  Внимание!

  Для директорий в этм хранилище с настроить проверку с помощью антивирусного ПО.

  См. *«[Антивирусное ПО. Настройка сканирования и исключений][antivirus_exceptions_configure]»*.

Технические требования к хранилищам данных описаны в статье *[«Архитектура, ландшафт, программное и техническое обеспечение»][architecture_landscape]*.

--8<-- "related_topics_heading.md"

- [Конфигурация экземпляра, компонентов ПО и служб. Настройка в Linux][configuration_files_linux]
- [Развёртывание {{ productName }}. Архитектура, ландшафт, программное и техническое обеспечение][architecture_landscape]
- [Антивирусное ПО. Настройка сканирования и исключений][antivirus_exceptions_configure]
- [Подсистема журналирования][logging_engine]

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
