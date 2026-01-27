---
title: Конфигурация экземпляра, компонентов ПО и служб. Настройка
kbId: 5067
tags:
    - Linux
    - администрирование
    - компоненты
    - конфигурация
    - настройка
    - развёртывание
    - службы
    - системные службы
    - установка
    - файлы конфигурации
    - экземпляр
hide: tags
---

# Конфигурация экземпляра, компонентов ПО и служб. Настройка {: #configuration_files_linux }

## Введение {: #configuration_files_linux_intro }

Здесь представлены инструкции по настройке файлов конфигурации после развёртывания и обновления ПО **{{ productName }}**, его компонентов и служб.

## Управление системными службами {: #configuration_files_linux_system_services }

В **{{ productName }} {{ productVersion }}** системные службы настраиваются с помощью [файла конфигурации экземпляра ПО](#configuration_files_linux_instance).

!!! warning "Важно!"

    - Для применения изменений параметров системных служб необходимо перезапустить экземпляр ПО.
    - По умолчанию все системные службы включены.

!!! note "Обновление конфигурации системных служб с версии 4.7"

    Инструкции по обновлению конфигурации с версий 4.7.x на версию {{ productVersion }} см. в статье _«[Обновление версии экземпляра ПО с его остановкой][upgrade_version_linux]»_.

Ниже перечислены системные службы и соответствующие параметры конфигурации. См. _[Пример файла конфигурации экземпляра ПО](#configuration_files_linux_instance_example)_.

| Системная служба | Назначение | Параметр, значение по умолчанию {: width=320px}|
| ------------------ | ------------ | ---------------------- |
| **Резервное копирование** | Управление созданием резервных копий экземпляра ПО | `backup.enabled`<br>`backup.sessionsEnabled: true`<br>`backup.schedulesEnabled: true` |
| **Получение эл. почты** | Получение новых электронных писем | `email.listenerEnabled: true` |
| **Отправка эл. почты** | Отправка электронных писем | `email.senderEnabled: true` |
| **Полнотекстовый поиск** | Индексирование значений атрибутов и обновление поисковых индексов | `search.enabled: true`<br>`search.rebuildingEnabled: true`<br>`search.indexingEnabled: true` |
| **Уведомления** | Формирование и отправка системных уведомлений | `notifications.enabled: true`<br>`notifications.onUserTaskEnabled: true`<br>`notifications.pushEnabled: true`<br>`notifications.onMaintenanceEnabled: true` |
| **Бизнес-процессы** | Выполнение бизнес-процессов; обработка таймеров (включая запуск по расписанию и таймерам резервного копирования, интеграция, процессов, синхронизации с сервером каталогов) | `bpms.enabled: true`<br>`bpms.timersEnabled: true` |
| **Синхронизация с OData** | Синхронизация данных с внешними системами по протоколу OData | `sync.oData.enabled: true`<br>`sync.oData.sessionsEnabled`<br>`sync.oData.schedulesEnabled: true` |
| **Синхронизация с LDAP** | Синхронизация пользователей и групп с LDAP-сервером | `sync.ldap.enabled: true`<br>`sync.ldap.sessionsEnabled: true`<br>`sync.ldap.schedulesEnabled: true` |
| **Монитор производительности** | Сбор показателей производительности системы | `sensors.enabled: true` |
| **Трассировка производительности** | Сбор данных трассировки для анализа производительности | `tracing.enabled: true` |

## Конфигурация экземпляра ПО {{ productName }} {: #configuration_files_linux_instance }

1. Откройте файл конфигурации экземпляра ПО (`<instanceName>` — имя экземпляра ПО) для редактирования:

    ``` sh
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

2. При необходимости измените параметры, например:

    - `journal.server` — адрес сервера {{ openSearchVariants }}.
    - `journal.name` — префикс индекса сервера {{ openSearchVariants }} (необязательно, по умолчанию назначается префикс `cmw<instanceName>`).
    - `journal.username` — имя пользователя сервера {{ openSearchVariants }} (необязательно).
    - `journal.password` — пароль сервера {{ openSearchVariants }} (необязательно).
    - `db.workDir` — директория для хранения базы данных экземпляра ПО.
    - `db.name` — префикс кэшей в базе данных экземпляра ПО.
    - `userStorage.localDisk.path` — директория для хранения загруженных файлов.
    - `mq.server` — адрес и порт брокера сообщений {{ apacheKafkaVariants }}.
    - `mq.group` — идентификатор группы очереди сообщений.
    - `mq.name` — префикс имени очередей сообщений.
    - `mq.node` — идентификатор узла очереди сообщений.
    - `backup.defaultFolder` — директория для хранения резервных копий экземпляра ПО.
    - `backup.defaultFileName` — имя файла резервной копии экземпляра ПО.

    --8<-- "instance_config_warning.md"

3. Сохраните файл конфигурации.
4. Убедитесь, что директории, указанные в файле конфигурации, существуют. При необходимости создайте их и задайте права доступа:

    ``` sh
    mkdir -p <path/to/Database>
    mkdir -p <path/to/Streams>
    mkdir -p <path/to/Backup>
    chown -R <User>:<Group> <path/to/Database> <path/to/Streams> <path/to/Backup>
    ```

    Здесь значения `<User>` и `<Group>` должны совпадать с такими же параметрами в файле `/usr/lib/systemd/system/comindware<instanceName>.service`

5. Перезапустите службу экземпляра ПО:{% if pdfOutput %} `systemctl restart comindware<instanceName>`{% else %}

    ``` sh
    systemctl restart comindware<instanceName>
    ```
{% endif %}
### Пример YML-файла конфигурации экземпляра ПО {: #configuration_files_linux_instance_example .pageBreakBefore }

<!--instanceYML-start-->
``` yaml
##### Настройка базовых параметров {{ productName }} #####
# Имя экземпляра {{ productName }}.
# Устаревшая директива: instanceName
clusterName: <instanceName>
# Имя узла экземпляра {{ productName }}.
#nodeName: <instanceName>
# Путь к экземпляру, по которому {{ productName }} находит свою конфигурацию.
configPath: <configPath>
# Адрес службы журналирования {{ openSearchVariants }}.
# Устаревшая директива: elasticsearchUri
journal.server: http://<searchHostIP>:<searchHostPort>
# Индекс службы журналирования {{ openSearchVariants }}.
# Допускается использовать только строчные буквы и цифры.
# Если в имени индекса будут прописные буквы или спецсимволы (например, дефис),
# служба журналирования автоматически преобразует их в строчные буквы и символы подчёркивания.
# journal.name: <prefix><instanceName>
# Имя пользователя службы журналирования
# journal.username: xxxx
# Пароль службы журналирования
# journal.password: xxxx
# Выключение службы журналирования.
#journal.enabled: false
# Выключение проверки валидации сертификатов
#journal.certificateSkipValidation: false
# URI-адрес экземпляра {{ productName }}.
fqdn: <hostName>
# Порт экземпляра {{ productName }}.
port: <portNumber>
# Версия экземпляра {{ productName }}.
version: <versionNumber>

{% if pdfOutput %}
```
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
``` yaml title="Пример YML-файла конфигурации экземпляра ПО — продолжение"
{% endif %}
##### Настройка базы данных #####
# Использование тонкого клиента.
#db.asThinClient: true
# Конечные точки для подключения тонкого клиента.
#db.asThinClientEndpoints: 127.0.0.1:10800
# Путь к базе данных.
# Устаревшая директива: databasePath
db.workDir: /var/lib/comindware/<instanceName>/Database
# Папка установки {{ apacheIgniteVariants }}.
#db.homeDir:
# Путь к файлу конфигурации {{ apacheIgniteVariants }}.
#db.configPath:
# Настройки JVM.
#db.jvmOpts:
# Настройки Java.
#db.javaOpts:
# Включение автоматической активации кластера {{ apacheIgniteVariants }} при запуске.
# При использовании нескольких узлов рекомендуется отключить на всех узлах.
#db.baselineAutoActivationEnabledFlag: false
# Включение автоматической настройки узлов {{ apacheIgniteVariants }}.
# На всех узлах должно быть одинаковое значение.
#db.baselineAutoAdjustEnabledFlag: false
# Время ожидания фактического изменения настройки узлов {{ apacheIgniteVariants }}
# с момента последнего изменения.
#db.baselineAutoAdjustTimeout: 3000
# Согласованный глобальный уникальный идентификатор узла {{ apacheIgniteVariants }}.
#db.consistentId: 
# Используемый префикс кэшей в базе данных
# Устаревшая директива: databaseName
db.name: <instanceName>
# Вес узла (целочисленное значение) с точки зрения кластера {{ apacheIgniteVariants }}.
# Суммарный вес всех узлов не должен превышать 100.
# Значение по умолчанию: 100/кол-во узлов.
#db.weight:
# Префикс кэшей в базе данных, используемый при обновлении.
#db.upgradeName:
# Путь к онтологии {{ companyName }}
#db.n3Dir:
# Директива применяется во время апгрейда кэшей. Если флаг не установлен, старые кэши необходимо удалять вручную.
#db.autoRemoveCachesOnUpgrade: false
# Директива применяется во время запуска системы. Если флаг установлен, на существующие кэши будет применена новая конфигурация (если она отличается).
#db.applyCachesConfigsOnStart: false
# Количество резервных копий для каждого кэша. При db.systemCacheConfig.cacheMode = Replicated не оказывает влияния.
#db.cacheConfig.backups: 2
# Тип кэша. Доступные значения: Partitioned | Replicated
#db.cacheConfig.cacheMode: Replicated
# Задержка ребалансировки (в секундах) при изменении топологии кластера {{ apacheIgniteVariants }}.
#db.cacheConfig.rebalanceDelay: 0
# Тип ребалансировки. Доступные значения: Sync | Async | None
#db.cacheConfig.rebalanceMode: Async
# Тип синхронизации данных кэша. Доступные значения: FullSync | FullAsync | PrimarySync
db.cacheConfig.writeSynchronizationMode: FullSync

{% if pdfOutput %}
```
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
``` yaml title="Пример YML-файла конфигурации экземпляра ПО — продолжение"
{% endif %}
##### Настройка хранения загруженных файлов #####
# Тип хранилища (LocalDisk | S3).
userStorage.type: LocalDisk
# Путь к пользовательским файлам экземпляра.
userStorage.localDisk.path: /var/lib/comindware/<instanceName>/Streams
# Имя корзины S3 для хранения загруженных файлов.
#userStorage.s3.bucket:
# Имя подключения к S3.
#userStorage.s3.connection: <s3ConnectionName>

##### Настройка хранения временных файлов #####
# Тип хранилища (LocalDisk | S3).
tempStorage.type: LocalDisk
# Путь к временным файлам экземпляра.
tempStorage.localDisk.path: /var/lib/comindware/<instanceName>/Temp
# Имя корзины S3 для хранения временных файлов.
#tempStorage.s3.bucket:
# Имя подключения к S3.
#tempStorage.s3.connection: <s3ConnectionName>
# Временная папка
tempWorkingDir: /var/lib/comindware/<instanceName>/LocalTemp

{% if pdfOutput %}
```
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
``` yaml title="Пример YML-файла конфигурации экземпляра ПО — продолжение"
{% endif %}
##### Настройка очереди сообщений #####
# Адрес и порт брокера сообщений {{ apacheKafkaVariants }}.
mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
# Идентификатор группы очереди сообщений.
mq.group: <prefix>-<instanceName>
# Префикс имени очередей сообщений.
mq.name: <instanceName>
# Идентификатор узла очереди сообщений.
mq.node: <instanceName>
# Выключение функции очереди сообщений.
#mq.enabled: false
# Протокол безопасности очереди сообщений.
# (Plaintext | Ssl | SaslPlaintext | SaslSsl)
#mq.securityProtocol: Plaintext

##### Настройка SSL-подключения очереди сообщений #####
# Путь к файлу корневого сертификата брокера сообщений.
#mq.ssl.caLocation:
# Выключение идентификации адреса брокера сообщений.
#mq.ssl.endpointIdentificationEnabled: false 

##### Настройка SASL-подключения очереди сообщений #####
# Имя пользователя, используемое для подключения посредством SASL.
#mq.sasl.username:
#Пароль для аутентификации, используемый для подключения посредством SASL.
#mq.sasl.password:
# Тип механизма SASL (None | Plain | ScramSha256 | ScramSha512).
#mq.sasl.mechanism:

##### Создание топиков #####
# Коэффициент репликации для создаваемого топика.
#mq.replicationFactor: 3
# Количество партиций для создаваемого топика.
#mq.numPartitions: 16
# Таймаут для запроса метаданных (миллисекунды).
#mq.metadataTimeoutMsec: 3000

{% if pdfOutput %}
```
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
``` yaml title="Пример YML-файла конфигурации экземпляра ПО — продолжение"
{% endif %}
##### Настройка очереди сообщений для коммуникации с адаптерами #####
# Выключение функции коммуникации брокера сообщений с адаптером 0.
#mq.adapter.0.enabled: false
# Выключение отправителя сообщений.
#mq.adapter.0.producer.enabled: false
# Выключение получателя сообщений.
#mq.adapter.0.consumer.enabled: false
# Выключение функции коммуникации брокера сообщений с адаптером 1.
#mq.adapter.1.enabled: false
# Выключение отправителя сообщений.
#mq.adapter.1.producer.enabled: false
# Выключение получателя сообщений.
#mq.adapter.1.consumer.enabled: false
# Выключение функции коммуникации брокера сообщений с адаптером 2.
#mq.adapter.2.enabled: false
# Выключение отправителя сообщений.
#mq.adapter.2.producer.enabled: false
# Выключение получателя сообщений.
#mq.adapter.2.consumer.enabled: false
# Выключение функции коммуникации брокера сообщений с адаптером 3.
#mq.adapter.3.enabled: false
# Выключение отправителя сообщений.
#mq.adapter.3.producer.enabled: false
# Выключение получателя сообщений.
#mq.adapter.3.consumer.enabled: false

##### Настройка OpenID-аутентификации #####
# Имя OpenID-сервиса, использующегося для входа.
#auth.openId.displayName:
# Включение функции OpenID.
#auth.openId.enabled: true
# Адрес сервера OpenID Connect.
#auth.openId.server:
# Пространство имен или контекст, в котором происходит аутентификация пользователей.
# Используется для управления идентификацией и доступом в системе OpenID Connect.
#auth.openId.realm:
# Уникальный идентификатор клиентского приложения, используемый
# для аутентификации и авторизации запросов по протоколу OpenID Connect.
#auth.openId.clientId:
# Секретный ключ OpenId Connect
#auth.openId.clientSecret:
# Список идентификаторов целевой аудитории, для которой предназначены токены, 
# используемые в процессе аутентификации и авторизации в OpenID Connect.
#auth.openId.audience:

##### Настройки аутентификации #####
# Минимальная длина пароля пользователя
#auth.minimalPasswordLength: 14
# Время истечения сессии пользователя в формате дд.чч:мм:сс  
#auth.sessionExpirationTime: 00.12:00:00

{% if pdfOutput %}
```
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
``` yaml title="Пример YML-файла конфигурации экземпляра ПО — продолжение"
{% endif %}
##### Настройка резервного копирования #####
# Папка для резервного копирования по умолчанию.
# Будет использоваться во вновь создаваемых конфигурациях резервного копирования.
# Устаревшая директива: backup.config.default.repository.localDisk.path
backup.defaultFolder: /var/backups/<instanceName>
# Имя файла резервных копий по умолчанию.
# Будет использоваться во вновь создаваемых конфигурациях резервного копирования.
backup.defaultFileName: <instanceName>
# Выключение функции резервного копирования.
#backup.enabled: false
# Выключение сеансов резервного копирования.
# Выключает выполнение резервного копирования, но не его настройку.
#backup.sessionsEnabled: false
# Выключение запуска сеансов резервного копирования по расписанию.
#backup.schedulesEnabled: false
# Максимальное количество сеансов резервного копирования.
#backup.maxSessions: 5

##### Конфигурация резервного копирования по умолчанию #####
# <backupName> — имя конфигурации резервного копирования, без пробелов
# Имя файлов резервных копий.
# К нему будут добавляться метка времени и расширение cdbbz, например:
# Backup.202202161625.cdbbz
#backup.default.<backupName>.name: Backup
# Тип хранилища (LocalDisk | S3).
#backup.default.<backupName>.repository.type: LocalDisk
# Путь к файлам резервных копий.
#backup.default.<backupName>.repository.localDisk.path: /var/backups/<instanceName>
# Имя корзины S3 для хранения файлов резервных копий.
#backup.default.<backupName>.repository.s3.bucket:
# Имя подключения к S3.
#backup.default.<backupName>.repository.s3.connection: <s3ConnectionName>
# Описание конфигурации
#backup.default.<backupName>.description:
# Периодичность запуска резервного копирования.
#backup.default.<backupName>.period: 23:00
# Дни запуска резервного копирования.
#backup.default.<backupName>.days: [Sunday,  Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]
# Время начала запуска резервного копирования.
#backup.default.<backupName>.timeFrom: 00:01
# Время окончания запуска резервного копирования.
#backup.default.<backupName>.timeUpTo: 23:59
# Количество резервных копий одновременно хранящихся в системе.
# Старые будут удалены автоматически.
#backup.default.<backupName>.keepRecent: 10
# Управление составом резервной копии — загруженные файлы
#backup.default.<backupName>.withStreams: true
# Управление составом резервной копии —  файлы скриптов.
#backup.default.<backupName>.withScripts: true
# Управление составом резервной копии — файлы истории ({{ openSearchVariants }}).
#backup.default.<backupName>.withJournal: true

{% if pdfOutput %}
```
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
``` yaml title="Пример YML-файла конфигурации экземпляра ПО — продолжение"
{% endif %}
##### Настройка дополнительного хранилища для конфигурации резервного копирования по умолчанию #####
# Тип хранилища (LocalDisk | S3).
#backup.default.<backupName>.extraRepository.type: LocalDisk
# Путь к файлам резервных копий.
#backup.default.<backupName>.extraRepository.localDisk.path: /var/backups/<instanceName>ExtraRepository
# Имя корзины S3 для хранения файлов резервных копий.
#backup.default.<backupName>.extraRepository.s3.bucket:
# Имя подключения к S3.
#backup.default.<backupName>.extraRepository.s3.connection: <s3ConnectionName>

##### Настройка резервного копирования данных службы журналирования ({{ openSearchVariants }}) #####
# Тип хранилища (LocalDisk | S3).
#backup.journalRepository.type: LocalDisk
# Путь к файлам резервных копий
#backup.journalRepository.localDisk.path: /var/backups/<instanceName>
# Имя корзины S3 для хранения файлов резервных копий.
#backup.journalRepository.s3.bucket:
# Имя подключения, настроенного в конфигурации службы журналирования.
#backup.journalRepository.s3.journalConnection: <s3ConnectionName>
# Имя подключения к S3, настроенного в этом файле конфигурации экземпляра {{ productName }}.
#backup.journalRepository.s3.platformConnection: <s3ConnectionName>

##### Конфигурация подключения к хранилищу S3 #####
# Описание конфигурации.
#s3.<s3ConnectionName>.description:
# Адрес подключения к S3.
#s3.<s3ConnectionName>.endpointURL:
# Информация учётной записи. Ключ подключения к хранилищу S3
#s3.<s3ConnectionName>.accessKey:
# Информация учётной записи. Секретный ключ подключения к хранилищу S3.
#s3.<s3ConnectionName>.secretKey:
# Установите значение true, если сервер принимает только запросы path-style вида:
# https://<s3hostname>/bucket-name/key-name
#s3.<s3ConnectionName>.pathStyleAccess: true

{% if pdfOutput %}
```
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
``` yaml title="Пример YML-файла конфигурации экземпляра ПО — продолжение"
{% endif %}
##### Настройка полнотекстового поиска #####
# Выключение функции полнотекстового поиска.
#search.enabled: false
# Выключение обновления индексов полнотекстового поиска.
#search.rebuildingEnabled: false
# Выключение индексирования для полнотекстового поиска.
#search.indexingEnabled: false

##### Настройка сенсоров мониторинга #####
# Выключение функции сенсоров мониторинга.
#sensors.enabled: false
##### Настройка синхронизации аккаунтов с LDAP-сервисом #####
# Выключение функции синхронизации.
#sync.ldap.enabled: true
# Выключение запуска сеансов синхронизации.
# Выключает выполнение сеансов, но не их настройку.
#sync.ldap.sessionsEnabled: true
# Выключение запуска сеансов синхронизации по расписанию.
#sync.ldap.schedulesEnabled: true

##### Настройка синхронизации данных с OData-сервисом #####
# Выключение интеграции по OData.
#sync.oData.enabled: false
# Выключение запуска сеансов синхронизации данных по OData.
# Выключает выполнение сеансов, но не их настройку.
#sync.oData.sessionsEnabled: false
# Выключение запуска сеансов синхронизации данных по OData по расписанию.
#sync.oData.schedulesEnabled: false
# Интервал экспорта данных по OData (минуты).
#sync.oData.exportTimeInterval: 60

##### Настройки трассировки производительности #####
# Выключение функции трассировки производительности.
#tracing.enabled: false

##### Настройки электронной почты #####
# Выключение функции проверки наличия и получения новых писем.
#email.listenerEnabled: false
# Выключение функции отправки эл. почты
#email.senderEnabled: false

##### Настройки уведомлений #####
# Выключение функции отправки уведомлений.
#notifications.enabled: false
# Выключение отправки уведомлений по пользовательским задачам.
#notifications.onUserTaskEnabled: false
# Выключение отправки уведомлений об обсуждениях.
#notifications.pushEnabled: false
# Выключение отправки уведомлений на страницах обслуживания.
#notifications.onMaintenanceEnabled: false

{% if pdfOutput %}
```
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
``` yaml title="Пример YML-файла конфигурации экземпляра ПО — продолжение"
{% endif %}
##### Настройка бизнес-процессов #####
# Выключение функции бизнес-процессов
#bpms.enabled: false
# Количество потоков выполнения бизнес-процессов
#bpms.threadsCount: 4
# Выключение процессных таймеров
#bpms.timersEnabled: false

##### Настройка использования Docker #####
# Включение использования в среде Docker
#isContainerEnvironment: true

##### Настройка обработчика сервис-запросов #####
# Включение функции обработчика сервис-запросов
#requestProcessor.enabled: true
# Список обработчиков сервис-запросов. 
# Если не указан, включает все доступные на узле  запросы
# (conversation, useractivity, notification, architect)
#requestProcessor.services:
#  - apiPrefix: conversation
#  - enabled: true

##### Настройка отображения количества строк таблицы на одной странице #####
# Задайте варианты, которые будут отображаться
# в меню выбора количества строк таблицы.
#queryPageResultRange: [ 50, 500, 5000, 1000000000 ]

#################### Настройка аккаунтов ####################
# Вкл./выкл. для всех пользователей возможность добавления замещений для собственного аккаунта 
#account.selfSubstitutionsEnabled: true
```
<!--instanceYML-end-->

## Конфигурация службы apigateway {: #configuration_files_linux_apigateway .pageBreakBefore }

1. Откройте файл конфигурации `apigateway.yml` экземпляра ПО для редактирования:

    ``` sh
    nano /var/www/<instanceName>/apigateway.yml
    ```

2. Измените необходимые параметры.
3. Удостоверьтесь, что значение параметра `cluster.name` (имя экземпляра ПО) совпадает с `clusterName` и значение параметров `mq.server` (адрес и порт брокера сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) — с аналогичными параметрами в [файле конфигурации экземпляра](#configuration_files_linux_instance).
4. Сохраните файл конфигурации.
5. Перезапустите службу `apigateway`:

    ``` sh
    systemctl restart apigateway<instanceName>
    ```

### Пример конфигурации службы apigateway.yml {: #configuration_files_linux_apigateway_example .pageBreakBefore }

<!--apigatewayYML-start-->
``` yaml
# Имя экземпляра ПО
cluster.name: <instanceName>
# Имя узла экземпляра
# nodeName:
# Включение/выключение конфигурации журналирования экземпляра (true | false)
log.enabled: true
# Путь к файлу конфигурации журналирования экземпляра
log.configurationFile: /var/www/<instanceName>/logs.config
# Адрес и порт брокера сообщений {{ apacheKafkaVariants }}.
mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>
# Идентификатор группы очереди сообщений
mq.group: <instanceName>
# Префикс имени очередей сообщений
mq.name: <instanceName>
# Идентификатор узла очереди сообщений
mq.node: <instanceName>
# Тип механизма SASL. (None | Plain | ScramSha256 | ScramSha512)
mq.sasl.mechanism: None
# Имя пользователя, используемое для подключения посредством SASL
#mq.sasl.username:
# Пароль для аутентификации, используемый для подключения посредством SASL
#mq.sasl.password:
# Протокол безопасности очереди сообщений. (Plaintext | Ssl | SaslPlaintext | SaslSsl)
mq.securityProtocol: Plaintext
# Путь к файлу корневого сертификата брокера сообщений
#mq.ssl.caLocation:
# Выключение идентификации адреса брокера сообщений
#mq.ssl.endpointIdentificationEnabled: false
# Порт для входящих соединений
#listen.port:
# Протокол входящих соединений (None, Http1, Http2, Http1AndHttp2)
listen.protocol: Http1AndHttp2
# Путь к сокету apigateway
listen.socketPath: /var/www/<instanceName>/App_Data/apigateway.socket
# Включение/выключение файлового хранилища  (true | false)
fileStorage.enabled: true
# Тип файлового хранилища (Platform — встроенное | Custom — особая DLL-библиотека )
fileStorage.type: Platform
# IP-адрес сервера для загрузки файлов
fileStorage.attachmentServerUri: http://local.host.ip.address/
# Путь к загружаемым файлам
fileStorage.uploadAttachment.path: /api/Attachment/Upload
# Путь к скачанным файлам
fileStorage.downloadAttachment.path: /api/Attachment/GetReferenceContent/{0}
# Путь к удалённым файлам
fileStorage.removeAttachment.path: /api/Attachment/Remove/{0}
# HTTP-метод отправки файлов в хранилище. (GET | POST | PUT | DELETE)
#fileStorage.uploadAttachment.method: POST
# HTTP-метод загрузки файлов из хранилища. (GET | POST | PUT | DELETE)
#fileStorage.downloadAttachment.method: GET
# HTTP-метод удаления файлов из хранилища. (GET | POST | PUT | DELETE)
#fileStorage.removeAttachment.method: DELETE
# Вкл./выкл. страницы для мониторинга подключений (true | false)
statusPage.enabled: true
# Префиксы служб API
services:
- apiPrefix: conversation
- apiPrefix: useractivity
- apiPrefix: notification
- apiPrefix: architect
```
<!--apigatewayYML-end-->

## Конфигурация службы adapterhost {: #configuration_files_linux_adapterhost .pageBreakBefore }

1. Откройте файл конфигурации `adapterhost.yml` экземпляра ПО для редактирования:

    ``` sh
    nano /var/www/<instanceName>/adapterhost.yml
    ```

2. Измените необходимые параметры.
3. Удостоверьтесь, что значения параметров `mq.server` (адрес и порт брокера сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) и `clusterName` (имя экземпляра ПО) совпадают с аналогичными параметрами в [файле конфигурации экземпляра ПО](#configuration_files_linux_instance_example).
4. Сохраните файл конфигурации.
5. После внесения изменений перезапустите службу `adapterhost`:

    ``` sh
    systemctl restart adapterhost<instanceName>
    ```

### Пример файла конфигурации adapterhost.yml {: #configuration_files_linux_adapterhost_example }

<!--adapterhostYML-start-->
``` yaml
# Имя экземпляра ПО
clusterName: <instanceName>
# Имя папки загрузчика экземпляра ПО
loaderFolder: <instanceName>
# Язык сервера (en-US | ru-RU )
serverLanguage: ru-RU
# Адрес и порт брокера сообщений {{ apacheKafkaVariants }}
mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>
# Префикс имени очередей сообщений
mq.name: <instanceName>
# Идентификатор группы очереди сообщений
mq.group: <instanceName>
# Идентификатор узла очереди сообщений
mq.node: <instanceName>
# Имя пользователя, используемое для подключения посредством SASL
mq.sasl.username:
# Пароль для аутентификации, используемый для подключения посредством SASL
mq.sasl.password:
# Тип механизма SASL (None | Plain | ScramSha256 | ScramSha512)
mq.sasl.mechanism: None
# Путь к файлу корневого сертификата брокера сообщений
mq.ssl.caLocation:
# Выключение/включение идентификации адреса брокера сообщений
mq.ssl.endpointIdentificationEnabled: true
# Протокол безопасности очереди сообщений. (Plaintext | Ssl | SaslPlaintext | SaslSsl)
mq.securityProtocol: Plaintext
# Путь к файлам журналирования экземпляра ПО
log.folder: /var/log/comindware/<instanceName>/Logs/
```
<!--adapterhostYML-end-->

## Конфигурация {{ apacheIgniteVariants }} {: #configuration_files_linux_ignite .pageBreakBefore }

1. Откройте файл конфигурации {{ apacheIgniteVariants }} для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Ignite.config
    ```

2. В блоке `<bean class="org.apache.ignite.configuration.DataRegionConfiguration">` задайте максимальный объём выделяемой памяти:

    - 3 ГБ:

        ``` xml
        <property name="maxSize" value="#{3L * 1024 * 1024 * 1024}" />
        ```

    - 8 ГБ:

        ``` xml
        <property name="maxSize" value="#{8L * 1024 * 1024 * 1024}" />
        ```

3. В случае изменения максимального объёма выделяемой памяти отредактируйте параметр `checkpointPageBufferSize`. Чтобы рассчитать размер значения, разделите размер `maxSize` на четыре, при этом значение должно быть в диапазоне 256 МБ — 2 ГБ.

    - 8 ГБ:

        ``` xml
        <property name="checkpointPageBufferSize" value="#{2L * 1024 * 1024 * 1024}" />
        ```

4. Перезапустите службу экземпляра ПО:

    ``` sh
    systemctl restart comindware<instanceName>
    ```

## Конфигурация кучи Java {: #configuration_files_linux_jvm .pageBreakBefore }

В зависимости от объёма оперативной памяти на сервере следует отредактировать конфигурацию области памяти для кучи Java.

1. Откройте файл конфигурации среды экземпляра ПО для редактирования:

    ``` sh
    nano /etc/sysconfig/comindware<instanceName>-env
    ```

2. Задайте объём памяти, который выделяется для кучи Java:

    ``` ini
    JVM_OPTS=-Xms512m -Xmx16g -XX:MaxDirectMemorySize=1g ...
    ```

    Здесь:

    - `-Xms` — начальный размер кучи;
    - `-Xmx` — максимальный размер кучи.

3. Сохраните файл конфигурации.
4. Перезапустите службу экземпляра ПО:

    ``` sh
    systemctl daemon-reload
    systemctl restart comindware<instanceName>
    ```

## Конфигурация {{ nginxVariants }} {: #configuration_files_linux_nginx .pageBreakBefore }

1. Откройте файл конфигурации {{ nginxVariants }} для редактирования:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        nano /etc/nginx/sites-available/comindware<instanceName>
        ```

    - **РЕД ОС**, **Rocky** (RPM-based)

        ``` sh
        nano /etc/nginx/conf.d/comindware<instanceName>
        ```

    - **Альт Сервер**

        ``` sh
        nano /etc/nginx/sites-available.d/comindware<instanceName>
        ```

2. В директиве `server` задайте номер порта и адрес сервера, по которым будет доступен экземпляр ПО:

    ``` sh
    server {
        # Адрес сервера для доступа к экземпляру ПО.
        server_name <hostName>
        # Номер порта для доступа к экземпляру ПО.
        listen <portNumber>
    }
    ```

3. Для записи событий в отдельные журналы укажите их:

    ``` sh
        error_log /var/log/nginx/<instanceName>-error.log;
        access_log /var/log/nginx/<instanceName>-access.log;
    ```

4. Сохраните файл конфигурации.
5. Проверьте, что изменения работают корректно:

    ``` sh
    nginx -t
    ```

6. При успешном вступлении изменений в силу перезагрузите {{ nginxVariants }}:

    ``` sh
    nginx -s reload
    ```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Пути и содержимое директорий экземпляра ПО][paths]
- [Настройка конфигурации вспомогательного ПО для оптимизации работы {{ productName }}][auxiliary_software_optimize]
- [{{ openSearchVariants }}. Настройка разрешений][opensearch_permissions]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
