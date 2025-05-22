---
title: 'Пути и содержимое директорий экземпляра ПО'
kbId: 4620
---

# Пути и содержимое директорий экземпляра ПО {: #paths }

## Введение {: #paths_intro }

Здесь представлена информация о расположении файлов и директорий экземпляра ПО **{{ productName }}**.

Ознакомьтесь также с [рекомендациями по настройке путей](#paths_recommendations).

{% if adminGuideLinux or kbExport %}

## Содержимое директорий {% if userGuide or kbExport %}— Linux{% endif %} {: #paths_linux }

По умолчанию файлы экземпляра ПО находятся {% if gostech %}в файловой системе контейнера{% endif %} в директории `/var/lib/comindware/<instanceName>`

Здесь и далее `<instanceName>` — имя экземпляра ПО.

Фактические пути к директориям экземпляра ПО указаны в файле конфигурации:

``` sh
/usr/share/comindware/configs/instance/<instanceName>.yml
```

**Пути по умолчанию**

- `/usr/share/comindware/configs/instance/<instanceName>.yml` — файл конфигурации. В этом файле задаются все остальные пути, перечисленные ниже.
{% if gostech %}
- `/usr/share/comindware/<instanceName>` — исполняемые и конфигурационные файлы экземпляра ПО.
{% else %}
- `/var/www/<instanceName>` — исполняемые и конфигурационные файлы экземпляра ПО:
    - `logs.config` — конфигурация журналов, см. *«[Подсистема журналирования][logging_engine]»*;
    - `adapterhost.yml` — конфигурация службы Adapterhost;
    - `apigateway.yml` — конфигурация службы Apigateway;
    - `Ignite.config` — конфигурация {{ apacheIgniteVariants }}.
{% endif %}
- `/var/lib/comindware/<instanceName>/Database/db` — файлы базы данных.
{% if not gostech %}
- `/var/lib/comindware/<instanceName>/Database/log` — файлы журналов {{ apacheIgniteVariants }}.
- `/var/log/comindware/<instanceName>/Logs/` — файлы журналов.
{% endif %}
- `/var/lib/comindware/<instanceName>/Database/Scripts` — скомпилированные библиотеки для скриптов на языке С#.
- `/var/lib/comindware/<instanceName>/Streams` — загруженные пользователями и сформированные системой файлы, которые прикреплены к соответствующим атрибутам.
- Вспомогательные файлы:
    - `/var/lib/comindware/<instanceName>/Database/git` — файлы локального репозитория Git для управления версиями приложений.
    - `/var/lib/comindware/<instanceName>/Database/FullTextSearch` — индексы полнотекстового поиска.
    - `/var/lib/comindware/<instanceName>/Database/snapshots` — снимки данных {{ apacheIgniteVariants }}.
    - `/var/lib/comindware/<instanceName>/Database/wal` — файлы журнала предварительной записи.
- Временные файлы:
    - `/var/lib/comindware/<instanceName>/Temp`
    - `/var/lib/comindware/<instanceName>/LocalTemp`

{% endif %}

{% if adminGuideWindows or kbExport %}

## Содержимое директорий {% if userGuide or kbExport %}— Windows{% endif %} {: #paths_windows }

По умолчанию файлы экземпляра ПО находятся в директории с экземпляром ПО: `C:\ProgramData\Comindware\Instances\<instanceName>`.

 Здесь и далее `<instanceName>` — имя экземпляра ПО.

Фактические пути к директориям экземпляра ПО указаны в файле конфигурации:

``` powershell
C:\ProgramData\сomindware\configs\instance\<instanceName>.yml
```

**Пути по умолчанию**

- `C:\Program Files\Comindware\CBAP` — исполняемые файлы ПО разных версий.
- `C:\ProgramData\сomindware\configs` — общие файлы конфигурации ПО.
- `C:\ProgramData\сomindware\configs\instance\<instanceName>.yml` — файл конфигурации. В этом файле задаются все остальные пути, перечисленные ниже.
- `C:\ProgramData\сomindware\Instances` — папка с экземплярами ПО.
- `C:\ProgramData\сomindware\Instances\<instanceName>` — экземпляр ПО.
- `C:\ProgramData\сomindware\Instances\<instanceName>\config` — исполняемые и конфигурационные файлы экземпляра ПО.:
    - `logs.config` — конфигурация журналов, см. *«[Подсистема журналирования][logging_engine]»*;
    - `adapterhost.yml` — конфигурация службы Adapterhost;
    - `apigateway.yml` — конфигурация службы Apigateway;
    - `Ignite.config` — конфигурация Apache Ignite.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Database` — файлы базы данных.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Database\Scripts` — DLL-файлы, скомпилированные из скриптов на языке C#.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Streams` — файлы, загруженные пользователями и сформированные ПО.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Logs` — журналы экземпляра ПО.
- Вспомогательные файлы:
    - `C:\ProgramData\сomindware\Instances\<instanceName>\Database\git` — файлы локального репозитория Git для управления версиями приложений.
    - `C:\ProgramData\сomindware\Instances\<instanceName>\Database\FullTextSearch` — индексы полнотекстового поиска.
    - `C:\ProgramData\сomindware\Instances\<instanceName>\Database\snapshots` — снимки данных Apache Ignite.
    - `C:\ProgramData\сomindware\Instances\<instanceName>\Database\wal` — файлы журнала предварительной записи.
- Временные файлы:
    - `C:\ProgramData\сomindware\Instances\<instanceName>\Temp`
    - `C:\ProgramData\сomindware\Instances\<instanceName>\LocalTemp`

{% endif %}

## Рекомендации по настройке путей {: #paths_recommendations }

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

    !!! warning "Внимание!"

        Для директорий в этм хранилище с настроить проверку с помощью антивирусного ПО.

        См. _«[Антивирусное ПО. Настройка сканирования и исключений][antivirus_exceptions_configure]»_.

Технические требования к хранилищам данных описаны в статье _[«Архитектура, ландшафт, программное и техническое обеспечение»][architecture_landscape]_.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

{% if adminGuideLinux or kbExport %}
- [Конфигурация экземпляра, компонентов ПО и служб. Настройка в Linux][configuration_files_linux]
- [Развёртывание Comindware Platform. Архитектура, ландшафт, программное и техническое обеспечение][architecture_landscape]
{% endif %}
{% if not gostech %}
- [Антивирусное ПО. Настройка сканирования и исключений][antivirus_exceptions_configure]
{% endif %}
- [Подсистема журналирования][logging_engine]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
