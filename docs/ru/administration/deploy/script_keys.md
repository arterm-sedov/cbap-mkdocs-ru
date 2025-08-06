---
title: 'Установочные скрипты. Назначение и ключи'
kbTitle: 'Установочные скрипты. Назначение и ключи'
kbId: 5122
tags:
  - Linux
  - Windows
  - bash
  - deploy
  - deployment
  - powershell
  - sh
  - скрипты
  - скрипты установки
  - установка
  - обновление
  - удаление
  - инсталляция
  - ключи
  - экземпляр
  - администрирование
hide: tags
---

# Установочные скрипты. Назначение и ключи {: #script_keys }

## Введение {: #script_keys_intro }

Для быстрого развёртывания, обновления, запуска, остановки и удаления **{{ productName }}** компания **{{ companyName }}** предоставляет дистрибутив со скриптами, настраивающими необходимое программное обеспечение.

Здесь представлены сведения о скриптах настройки конфигурации ПО и их ключах.

!!! warning "Пути к файлам и директориям"

    Используемые по умолчанию пути к файлам  **{{ productName }}** см. в статье _«[Пути и содержимое директорий экземпляра ПО][paths]»_.

    В вашей конфигурации могут использоваться другие пути, поэтому внимательно подставляйте фактические пути в команды при выполнении инструкций.

!!! note "Скрипты для Linux и Windows"

    Для большинства операций в Linux и Windows предусмотрены одинаковые скрипты с соответствующим расширением: `.sh` или `.ps1`.

    Если скрипты или синтаксис ключей для Linux и Windows отличаются, здесь представлены соответствующие ключи и примеры.

    В зависимости от версии ПО, некоторые скрипты могут отсутствовать для той или иной операционной системы, если они для неё не требуются.

!!! tip "Обязательные ключи для скриптов"

    Если не указать обязательный ключ для любого скрипта, он запросит его после запуска.

    Для некоторых скриптов не требуется указывать ключи и примеры их запуска здесь не представлены, так как для запуска достаточно указать имя скрипта в терминале.

## Вызов справки для скриптов {: #script_keys_help_call }

Для ознакомления с ключами (если таковые имеются) и назначением большинства скриптов можно использовать ключ `-h` (Linux и Windows), `--help` (Linux) или `-help` (Windows) без указания каких-либо других ключей, например:

``` bash
sh prerequisites_install.sh -h
```

``` powershell
.\instance_upgrade.ps1 -h
```

Далее ключ `-h` повторно не упоминается, так как он действует одинаково для всех скриптов.

!!! warning "Справка имеется не у всех скриптов"

    Для некоторых служебных, не предназначенных для вызова пользователем и не требующих объяснения скриптов ключ `-h` не предусмотрен.

## Условные обозначения {: #script_keys_conditional_legend }

Здесь используются следующие обозначения:

- `<instanceName>` — имя экземпляра ПО.
- `<versionNumber>` — номер версии ПО.
- `<portNumber>` — номер порта.
- `<osname>` — название ОС.
- `<versionPath>` — путь к директории с версией ПО.
- `<hostName>` — имя хоста экземпляра ПО.
- `<value>` — значение, подставляемое пользователем.
- `<path/to>` — путь к файлу или директории, подставляемый пользователем.

## Скрипты для установки вспомогательного ПО {: #script_keys_prerequisites }

Скрипты для установки вспомогательного ПО расположены в следующей директории распакованного дистрибутива вспомогательного ПО:

- **Linux:** `X.X-release-ru-<versionNumber>.prerequisites.<osname>/CMW_<osname>/scripts`
- **Windows:** `X.X-release-ru-<versionNumber>.prerequisites.Windows\CMW_Windows<versionNumber>\scripts`

### Скрипты для Linux и Windows {: #script_keys_linux_windows }

#### `prerequisites_install` {: #scripts_keys_prerequisites_install }

**Назначение:** установка и настройка вспомогательного ПО и зависимостей **{{ productName }}**.

**Ключи:**

- **Linux**
    - `-u=<user>`, `--user=<user>` — указать пользователя для установки компонентов.
    - `-g=<group>`, `--group=<group>` — указать группу для установки компонентов.
    - `-k`, `--kafka` — установить Kafka.
    - `-kc`, `--kafkaClient` — установить клиентские библиотеки Kafka.
    - `-d`, `--dotnet` — установить .NET.
    - `-o`, `--opensearch` — установить OpenSearch.
    <!-- НЕ ИСПОЛЬЗОВАТЬ ПОКА НЕ РЕАЛИЗОВАН КЛАСТЕР
    - `-i`, `--ignite` — установить Apache Ignite.
    -->
    - `-p`, `--platform` — установить компоненты **{{ productName }}**.

    **Пример:**

        ``` bash
        sh prerequisites_install.sh -p -d -k
        ```

- **Windows**
    - Используйте скрипт без ключей:

        ``` powershell
        .\prerequisites_install.ps1
        ```
    <!-- НЕ ИСПОЛЬЗОВАТЬ ПОКА НЕ БУДЕТ РЕАЛИЗОВАН КЛАСТЕР
    - `-ignite` — установить Apache Ignite.

    **Пример:**

        ``` powershell
        .\prerequisites_install.ps1 -ignite
        ```
    -->

#### `prerequisites_list` {: #script_keys_prerequisites_list }

**Назначение:** вывод списка установленных компонентов вспомогательного ПО.

#### `version_check` {: #script_keys_version_check }

**Назначение:** проверка состояния среды и компонентов вспомогательного ПО.

#### `version_check_environment` {: #script_keys_version_check_environment }

**Назначение:** проверка состояния среды — выводит статус и версию установленных компонентов, необходимых для работы вспомогательного ПО и **{{ productName }}**.

#### `version_list` {: #script_keys_version_list }

**Назначение:** вывод списка установленных версий **{{ productName }}**.

#### `version_upgrade_onetime` {: #script_keys_version_upgrade_onetime }

**Назначение:** обновление установленной версии ПО **{{ productName }}** до новой с переносом файлов, остановкой и удалением старых сервисов, обновлением конфигураций и запуском новой версии.

### Скрипты только для Windows

#### `files_unblock` {: #scripts_keys_files_unblock }

**Назначение:** разблокировка установочных файлов, скачанных из Интернета (снятие метки безопасности `Zone.Identifier`).

**Ключ:**

- `-path <path/to/distribution>` — путь к распакованной директории с установочными файлами, которые требуется разблокировать. Если не указать этот ключ, скрипт разблокирует файлы в текущей директории.

**Пример:**

``` powershell
.\files_unblock.ps1 -path С:\Downloads\prerequisites
```

### Скрипты только для Linux

#### `prerequisites_uninstall` {: #script_keys_prerequisites_uninstall }

**Назначение:** удаление выбранных компонентов вспомогательного ПО.

**Ключи:**

- `-d`, `--dotnet` — удалить .NET.
- `-j`, `--java` — удалить Java.
- `-k`, `--kafka` — удалить Kafka.
- `-m`, `--mono` — удалить Mono.
- `-n`, `--nginx` — удалить Nginx.

**Пример:**

``` bash
sh prerequisites_uninstall.sh -d -j
```

## Скрипты для установки {{ productName }} {: #script_keys_platform_scripts }

Скрипты для установки ПО **{{ productName }}** расположены в следующей директории с распакованным дистрибутивом **{{ productName }}**:

- **Linux:** `X.X-release-ru-<versionNumber>.<osname>/CMW_<osname>_<versionNumber>/scripts`
- **Windows:** `X.X-release-ru-<versionNumber>.Windows\CMW_Windows<versionNumber>\scripts`

### Кросс-платформенные скрипты

#### `instance_check` {: #script_keys_instance_check }

**Назначение:** проверка состояния экземпляра ПО.

**Ключ:**

- `<instanceName>` — имя экземпляра ПО (**обязательный**).

**Пример:**

``` sh
bash instance_check.sh my_company_instance
```

#### `instance_create` {: #script_keys_instance_create }

**Назначение:** создание нового экземпляра **{{ productName }}**, генерация конфигурационных файлов, а также развёртывание демонстрационной базы данных.

**Ключи:**

- **Linux**
    - `-n=<instanceName>`, `--name=<instanceName>` — указать имя экземпляра ПО (обязательный).
    - `-p=<portNumber>`, `--port=<portNumber>` — назначить порт экземпляру ПО (обязательный). По умолчанию: `80`.
    - `-v=<versionNumber>`, `--version=<versionNumber>` — развернуть ПО указанной версии (обязательный).
    - `-fqdn=<hostName>`, `--instance-fqdn=<hostName>` — указать имя хоста для экземпляра ПО. По умолчанию: `localhost`.
    - `-el=<value>`, `--elasticsearch-url=<value>` — указать ссылку или IP-адрес службы Elasticsearch.
    - `-kf=<value>`, `--kafka-url=<value>` — указать ссылку или IP-адрес службы Kafka.
    - `-d`, `--demoDB` — создать экземпляр ПО c демонстрационной базой данных.

    **Пример:**

        ``` bash
        bash instance_create.sh -n=my_company_instance -p=8080 -v=5.0.1234.0
            ```

- **Windows**
    - `-name <instanceName>` — указать имя экземпляра ПО (обязательный).
    - `-port <portNumber>` — назначить порт экземпляру ПО. По умолчанию: 80.
    - `-version <versionNumber>` — развернуть ПО указанной версии вида `X.X.XXXX.X`.
    - `-versionPath <versionPath>` — развернуть ПО из указанной папки `<versionPath>` с версией ПО.
    - `-fqdn <hostName>` — имя хоста для экземпляра ПО (опционально, по умолчанию: localhost).
    - `-demoDB` — создать экземпляр ПО c демонстрационной базой данных.

    **Пример:**

        ``` powershell
        .\instance_create.ps1 -name my_company_instance -port 8080 -version 5.0.1234.0
        ```

#### `instance_delete` {: #script_keys_instance_delete }

**Назначение:** удаление экземпляра **{{ productName }}**, его конфигурационных файлов, а также пользовательских данных и всех связанных файлов.

**Ключи:**

- **Linux**
    - `-n=<instanceName>`, `--name=<instanceName>` — указать имя экземпляра ПО (обязательный).
    - `--deleteData` — удалить базу данных и пользовательские файлы экземпляра ПО.
    - `--deleteLogs` — удалить журналы экземпляра ПО.
    - `--deleteBackups` — удалить резервные копии экземпляра ПО.

    **Пример:**

        ``` bash
        bash instance_delete.sh -n=my_company_instance
        ```

- **Windows**
    - `-name <instanceName>` — указать имя экземпляра ПО (обязательный). Если не указать другие ключи, будет удалена только служба `comindware<instanceName>`.
    - `-deleteData` — удалить базу данных из папки вида и пользовательские файлы экземпляра ПО. Без указания этого ключа или ключа `-clear` база данных экземпляра ПО не будет удалена.
    - `-clear` — удалить все файлы, папки, базу данных и пользовательские файлы, а также службы экземпляра ПО, сайт и пул из IIS.

    **Пример:**

        ``` powershell
        .\instance_delete.ps1 -name my_company_instance -clear
        ```

#### `instance_list` {: #script_keys_instance_list }

**Назначение:** вывод списка установленных экземпляров ПО.

**Ключи не требуются**

#### `instance_upgrade` {: #script_keys_instance_upgrade }

**Назначение:** обновление экземпляра ПО.

**Ключи:**

- **Linux**
    - `-n=<instanceName>`, `--name=<instanceName>` — указать имя экземпляра ПО (обязательный).
    - `-vp=<path/to>`, `--versionPath=<path/to>` — путь к папке с новой версией ПО (обязательный).

    **Пример:**

        ``` sh
        bash instance_upgrade.sh -n=my_company_instance -vp=/comindware/5.0.1234.0
        ```

- **Windows**
    - `-name <instanceName>` — указать имя экземпляра ПО (обязательный).
    - `-version <versionNumber>` — указать номер версии, до которой необходимо обновить экземпляр ПО (обязательный).
    - `-versionPath <path/to>` — обновить экземпляр ПО до версии из указанной папки.

    **Пример:**

        ``` powershell
        .\instance_upgrade.ps1 -name my_company_instance -version 5.0.1234.0
        ```

#### `version_check` {: #script_keys_version_check_platform }

**Назначение:** проверка состояния среды и компонентов **{{ productName }}**.

**Ключи не требуются**

#### `version_check_environment` {: #script_keys_version_check_environment_platform }

**Назначение:** проверка состояния среды и компонентов **{{ productName }}** — выводит статус и версию установленных компонентов, необходимых для работы **{{ productName }}**.

#### `version_delete` {: #script_keys_version_delete }

**Назначение:** удаление указанной версии ПО.

**Ключи:**

- **Linux**
    - `-v=<versionNumber>`, `--version=<versionNumber>` — указать номер версии ПО (**обязательный**).

    **Пример:**

        ``` bash
        sh version_delete.sh -v=5.0.1234.0
        ```

- **Windows**
    - `-version <versionNumber>` — указать номер версии ПО (обязательный).

    **Пример:**

        ``` powershell
        .\version_delete.ps1 -version 5.0.1234.0
        ```

#### `version_install` {: #script_keys_version_install }

**Назначение:** установка версии ПО из текущей директории с дистрибутивом.

**Ключи не требуются**

#### `version_list` {: #script_keys_version_list_platform }

**Назначение:** вывод списка установленных версий ПО.

**Ключи не требуются**

#### `version_upgrade_onetime` {: #script_keys_version_upgrade_onetime_platform }

**Назначение:** обновление установленной версии **{{ productName }}** до новой с переносом файлов, остановкой и удалением старых сервисов, обновлением конфигураций и запуском новой версии.

**Ключи не требуются**

### Скрипты только для Windows

#### `files_unblock` {: #script_keys_files_unblock_platform }

**Назначение:** разблокировка установочных файлов, скачанных из Интернета (снятие метки безопасности `Zone.Identifier`).

**Ключ:**

- `-path <path/to/distribution>` — путь к распакованной директории с установочными файлами, которые требуется разблокировать. Если не указать этот ключ, скрипт разблокирует файлы в текущей директории.

**Пример:**

``` powershell
.\files_unblock.ps1 -path С:\Downloads\CMW
```

#### `instance_restore_from_backup` {: #script_keys_instance_restore_from_backup }

**Назначение:** восстановление данных экземпляра ПО из архивной резервной копии (файл `.cdbbz`) в указанные каталоги `Database` и `Streams`.

**Ключи:**

- `-zipPath <path/to>` — указать путь к архиву резервной копии `.cdbbz` (обязательный).
- `-dataPath <path/to>` — указать путь к каталогу `Database` для восстановления (обязательный).
- `-streamsPath <path/to>` — указать путь к каталогу `Streams` для восстановления (обязательный).
- `-tempDir <path/to>` — указать временный каталог для распаковки архива.
- `-deleteOldData` — удалить старые данные перед восстановлением.

**Пример:**

``` powershell
.\instance_restore_from_backup.ps1 -zipPath C:\Documents\CMW_backup -dataPath C:\Documents\CMW\Database -streamsPath C:\Documents\CMW\Streams
```

#### `instance_start` {: #script_keys_instance_start }

**Назначение:** запуск экземпляра ПО.

**Ключ:**

- `-name <instanceName>` — указать имя экземпляра ПО (обязательный).

**Пример:**

``` powershell
.\instance_start.ps1 -name my_company_instance
```

#### `instance_stop` {: #script_keys_instance_stop }

**Назначение:** остановка экземпляра ПО.

**Ключи:**

- `-name <instanceName>` — указать имя экземпляра ПО (обязательный).

**Пример:**

``` powershell
.\instance_stop.ps1 -name my_company_instance
```

## Служебные скрипты

Служебные скрипты являются вспомогательными и служат для вызова другими скриптами. Они не предназначены для самостоятельного запуска пользователем.

Список служебных скриптов (**может измениться в зависимости от версии ПО**):

### Для Windows {: #service_scripts_windows }

| Имя скрипта            | Назначение                                                          |
| ---------------------- | ------------------------------------------------------------------- |
| adapterhost_config     | Генерация конфигурационного файла `adapterhost.yml` для экземпляра. |
| adapterhost_register   | Регистрация Adapterhost как службы.                                 |
| adapterhost_start      | Запуск службы Adapterhost.                                          |
| adapterhost_stop       | Остановка службы Adapterhost.                                       |
| adapterhost_unregister | Удаление службы Adapterhost.                                        |
| apigateway_register    | Регистрация Apigateway как службы.                                  |
| apigateway_start       | Запуск службы Apigateway.                                           |
| apigateway_stop        | Остановка службы Apigateway.                                        |
| apigateway_unregister  | Удаление службы Apigateway.                                         |
| upgrade_config_file    | Обновление конфигурационных файлов при обновлении версии ПО.        |

### Для Linux {: #service_scripts_linux }

Служебные скрипты для Linux организованы по директориям для работы с соответствующими службами.

| Директория                  | Назначение                          |
| --------------------------- | ----------------------------------- |
| `components/adapterhost/`   | Управление службой AdapterHost      |
| `components/apigateway/`    | Управление службой ApiGateway       |
| `components/kafka/`         | Установка и настройки Kafka         |
| `components/nginx/`         | Установка и настройки Nginx         |
| `components/opensearch/`    | Установка и настройки OpenSearch    |
| `components/elasticsearch/` | Установка и настройки Elasticsearch |

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Пути и содержимое директорий экземпляра ПО][paths]
- [Развёртывание ПО в ОС Linux][deploy_guide_linux]
- [Резервное копирование и восстановление в ОС Linux][backup_restore_cdbbz]
- [Развёртывание ПО в ОС Windows][deploy_guide_windows]
- [Резервное копирование и восстановление в ОС Windows][backup_restore_windows]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
