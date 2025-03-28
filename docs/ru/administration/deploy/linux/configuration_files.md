---
title: Конфигурация экземпляра, компонентов ПО и служб. Настройка
kbId: 5067
---

# Конфигурация экземпляра, компонентов ПО и служб. Настройка {: #configuration_files_linux }

## Введение

Здесь представлены инструкции по настройке файлов конфигурации после развёртывания и обновления ПО **{{ productName }}**, его компонентов и служб.

## Конфигурация экземпляра ПО

1. Откройте файл конфигурации экземпляра ПО (`<instanceName>` — имя экземпляра ПО) для редактирования:

    ``` sh
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

2. При необходимости измените параметры, например:

    - `journal.server` — адрес сервера {{ openSearchVariants }}.
    - `journal.name` — индекс сервера {{ openSearchVariants }}.
    - `db.workDir` — директория для хранения базы данных экземпляра ПО.
    - `db.name` — префикс кэшей в базе данных экземпляра ПО.
    - `userStorage.localDisk.path` — директория для хранения пользовательских файлов.
    - `mq.server` — адрес сервера {{ apacheKafkaVariants }}.
    - `backup.defaultFolder` — директория для хранения резервных копий экземпляра ПО.
    - `backup.defaultFileName` — имя файла резервной копии экземпляра ПО.

    --8<-- "instance_config_warning.md"

3. Сохраните файл конфигурации.
4. Убедитесь, что директории, указанные в файле конфигурации, существуют. При необходимости создайте их и задайте права доступа:

    ``` sh
    mkdir -p <path/to/Database>
    mkdir -p <path/to/Streams>
    mkdir -p <path/to/Backup>
    chmod -R 766 <path/to/Database> <path/to/Streams> <path/to/Backup>
    chown -R <User>:<Group> <path/to/Database> <path/to/Streams> <path/to/Backup>
    ```

    Здесь значения `<User>` и `<Group>` должны совпадать с такими же параметрами в файле `/usr/lib/systemd/system/comindware<instanceName>.service`

5. Перезапустите службу экземпляра ПО:

    ``` sh
    systemctl restart comindware<instanceName>
    ```

### Пример YML-файла конфигурации экземпляра ПО {: .pageBreakBefore }

<!--instanceYML-start-->
``` yml
#################### Настройка базовых параметров ПО ####################
# Имя экземпляра ПО
# Устаревшая директива: instanceName
clusterName: <instanceName>
# Имя узла экземпляра ПО
#nodeName: <instanceName>
# Путь к экземпляру, по которому ПО находит свою конфигурацию
configPath: <configPath>
# Адрес службы журналирования ({{ openSearchVariants }}, OpenSearch)
# Устаревшая директива: elasticsearchUri
journal.server: http://<searchHostIP>:<searchHostPort>
# Индекс службы журналирования ({{ openSearchVariants }}, OpenSearch)
# journal.name: <instanceName>
# URI-адрес экземпляра ПО
fqdn: <hostName>
# Порт экземпляра ПО
port: <portNumber>
# Версия экземпляра ПО
version: <versionNumber>
#################### Настройка базы данных ####################
# Использование тонкого клиента
#db.asThinClient: true
# Конечные точки для подключения тонкого клиента
#db.asThinClientEndpoints: 127.0.0.1:10800
# Путь к базе данных
# Устаревшая директива: databasePath
db.workDir: /var/lib/comindware/<instanceName>/Database
# Папка установки Ignite.
#db.homeDir:
# Путь к файлу конфигурации
#db.configPath:
# Настройки JVM
#db.jvmOpts:
# Настройки Java
#db.javaOpts:
# Включение автоматической настройки узлов Ignite
#db.baselineAutoAdjustEnabledFlag: false
# Значение времени ожидания фактического изменения настройки узлов Ignite с момента последнего изменения
#db.baselineAutoAdjustTimeout: 3000
# Cогласованный глобальный уникальный идентификатор узла
#db.consistentId: 
# Используемый префикс кэшей в базе данных
# Устаревшая директива: databaseName
db.name: <instanceName>
# Используемый префикс кэшей в базе данных при обновлении
#db.upgradeName:
# Путь к онтологии {{ companyName }}
#db.n3Dir:
#################### Настройка хранения пользовательских файлов ####################
# Тип хранилища (LocalDisk | S3)
userStorage.type: LocalDisk
# Путь к пользовательским файлам экземпляра
userStorage.localDisk.path: /var/lib/comindware/<instanceName>/Streams
# Имя корзины для хранения пользовательских файлов
#userStorage.s3.bucket:
# Имя конфигурации S3
#userStorage.s3.connection: <s3ConnectionName>
#################### Настройка хранения временных файлов ####################
# Тип хранилища (LocalDisk | S3)
tempStorage.type: LocalDisk
# Путь к временным файлам экземпляра
tempStorage.localDisk.path: /var/lib/comindware/<instanceName>/Temp
# Имя корзины для хранения временных файлов
#tempStorage.s3.bucket:
# Имя конфигурации S3
#tempStorage.s3.connection: <s3ConnectionName>
# Временная папка
tempWorkingDir: /var/lib/comindware/fooo/LocalTemp
#################### Настройки очереди сообщений ####################
# Адрес и порт сервера очереди сообщений {{ apacheKafkaVariants }}
mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
# Идентификатор группы очереди сообщений
mq.group: <instanceName>
# Префикс имени очередей сообщений
mq.name: <instanceName>
# Идентификатор узла очереди сообщений
mq.node: <instanceName>
# Выключение функции очереди сообщений
#mq.enabled: false
# Протокол безопасности очереди сообщений. (Plaintext | Ssl | SaslPlaintext | SaslSsl)
#mq.securityProtocol: Plaintext
#################### Настройки SSL-подключения очереди сообщений ####################
# Путь к файлу корневого сертификата сервера очереди сообщений
#mq.ssl.caLocation:
# Выключение идентификации адреса сервера очереди сообщений
#mq.ssl.endpointIdentificationEnabled: false 
#################### Настройки SASL-подключения очереди сообщений ####################
# Имя пользователя, используемое для подключения при помощи SASL
#mq.sasl.username:
#Пароль для аутентификации, используемый для подключения при помощи SASL
#mq.sasl.password:
# Тип механизма SASL (None | Plain | ScramSha256 | ScramSha512)
#mq.sasl.mechanism:
#################### Настройки очереди сообщений для коммуникации с адаптерами ####################
# Выключение функции коммуникации брокера сообщений с адаптером 0
#mq.adapter.0.enabled: false
# Настройки отправителя сообщений
#mq.adapter.0.producer.enabled: false
# Настройки получателя сообщений
#mq.adapter.0.consumer.enabled: false
# Выключение функции коммуникации брокера сообщений с адаптером 1
#mq.adapter.1.enabled: false
# Настройки отправителя сообщений
#mq.adapter.1.producer.enabled: false
# Настройки получателя сообщений
#mq.adapter.1.consumer.enabled: false
# Выключение функции коммуникации брокера сообщений с адаптером 2
#mq.adapter.2.enabled: false
# Настройки отправителя сообщений
#mq.adapter.2.producer.enabled: false
# Настройки получателя сообщений
#mq.adapter.2.consumer.enabled: false
# Выключение функции коммуникации брокера сообщений с адаптером 3
#mq.adapter.3.enabled: false
# Настройки отправителя сообщений
#mq.adapter.3.producer.enabled: false
# Настройки получателя сообщений
#mq.adapter.3.consumer.enabled: false
#################### Настройки OpenID-аутентификации ####################
# Имя OpenID-сервиса использующегося для входа
#auth.openId.displayName:
# Включение функции OpenID
#auth.openId.enabled: true
# Адрес сервера OpenID Connect
#auth.openId.server:
# Пространство имен или контекст, в котором происходит аутентификация пользователей. Используется для управления идентификацией и доступом в системе OpenID Connect
#auth.openId.realm:
# Уникальный идентификатор клиентского приложения, используемый для аутентификации и авторизации запросов в рамках протокола OpenID Connect
#auth.openId.clientId:
# Секретный ключ OpenId Connect
#auth.openId.clientSecret:
# Список идентификаторов целевой аудитории, для которой предназначены токены, используемые в процессе аутентификации и авторизации в OpenID Connect.
#auth.openId.audience:
#################### Конфигурация резервного копирования ####################
# Папка для резервного копирования по умолчанию
# Устаревшая директива: backup.config.default.repository.localDisk.path
backup.defaultFolder: /var/backups/<instanceName>
# Имя файла для резервного копирования по умолчанию
backup.defaultFileName: <instanceName>
# Выключение функции резервного копирования
#backup.enabled: false
# Выключение сеансов резервного копирования. Выключает выполнение резервного копирования, но не создание сеансов резервного копирования.
#backup.sessionsEnabled: false
# Выключение создания сеансов резервного копирования по расписанию
#backup.schedulesEnabled: false
# Максимальное количество сеансов резервного копирования
#backup.maxSessions: 5
#################### Конфигурация резервного копирования по умолчанию ####################
# Имя файла для резервного копирования по умолчанию
#backup.default.<backupName>.name: Backup
# Тип хранилища: LocalDisk или S3
#backup.default.<backupName>.repository.type: LocalDisk
# Путь к файлам резервных копий
#backup.default.<backupName>.repository.localDisk.path: /var/backups/<iname>
# Имя корзины для хранения файлов резервных копий
#backup.default.<backupName>.repository.s3.bucket:
# Имя конфигурации S3
#backup.default.<backupName>.repository.s3.connection: <s3ConnectionName>
# Описание конфигурации
#backup.default.<backupName>.description:
# Период создания сессий резервного копирования
#backup.default.<backupName>.period: 23:00
# Дни создания сессий резервного копирования
#backup.default.<backupName>.days: [Sunday,  Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]
# Время начала создания сессий резервного копирования
#backup.default.<backupName>.timeFrom: 00:01
# Время окончания создания сессий резервного копирования
#backup.default.<backupName>.timeUpTo: 23:59
# Количество резервных копий одновременно хранящихся в системе. Старые будут удалены автоматически.
#backup.default.<backupName>.keepRecent: 10
# Управление составом резервной копии - загруженные файлы
#backup.default.<backupName>.withStreams: true
# Управление составом резервной копии -  файлы скриптов
#backup.default.<backupName>.withScripts: true
# Управление составом резервной копии - файлы истории
#backup.default.<backupName>.withJournal: true
#################### Настройки дополнительного хранилища резервного копирования по умолчанию ####################
# Тип хранилища: LocalDisk или S3
#backup.default.<backupName>.extraRepository.type: LocalDisk
# Путь к файлам резервных копий
#backup.default.<backupName>.extraRepository.localDisk.path: /var/backups/<instanceName>ExtraRepository
# Имя корзины для хранения файлов резервных копий
#backup.default.<backupName>.extraRepository.s3.bucket:
# Имя конфигурации S3
#backup.default.<backupName>.extraRepository.s3.connection: <s3ConnectionName>
#################### Настройки резервного копирования журналирования ####################
# Тип хранилища: LocalDisk или S3
#backup.journalRepository.type: LocalDisk
# Путь к файлам резервных копий
#backup.journalRepository.localDisk.path: /var/backups/<instanceName>
# Имя корзины для хранения файлов резервных копий
#backup.journalRepository.s3.bucket:
# Имя соединения, описанного в конфигурации сервиса журналирования
#backup.journalRepository.s3.journalConnection: <s3ConnectionName>
# Имя конфигурации S3
#backup.journalRepository.s3.platformConnection: <s3ConnectionName>
#################### Настройки подключения к хранилищу S3 ####################
# Описание конфигурации
#s3.<s3ConnectionName>.description:
# Адрес подключения к S3
#s3.<s3ConnectionName>.endpointURL:
# Информация учетной записи. Ключ подключения к хранилищу S3
#s3.<s3ConnectionName>.accessKey:
# Информация учетной записи. Секретный ключ подключения к хранилищу S3
#s3.<s3ConnectionName>.secretKey:
# Идентификатор указывающий что запросы будут использовать адресацию в стиле системных путей
#s3.<s3ConnectionName>.pathStyleAccess: true
#################### Настройка полнотекстового поиска ####################
# Выключение функции полнотекстового поиска
#search.enabled: false
# Выключение обновления индексов полнотекстового поиска
#search.rebuildingEnabled: false
# Выключение индексирования для полнотекстового поиска
#search.indexingEnabled: false
#################### Настройки сенсоров мониторинга ####################
# Выключение функции сенсоров мониторинга
#sensors.enabled: false
#################### Настройки LDAP-синхронизации ####################
# Выключение функции LDAP-синхронизации
#sync.ldap.enabled: true
# Выключение сеансов LDAP-синхронизации. Выключает выполнение сеансов, но не их создание.
#sync.ldap.sessionsEnabled: true
# Выключение создания сеансов LDAP-синхронизации по расписанию
#sync.ldap.schedulesEnabled: true
# Выключение интеграции OData
#sync.oData.enabled: false
# Выключение сеансов интеграции OData. Выключает выполнение сеансов, но не их создание.
#sync.oData.sessionsEnabled: false
# Выключение создания сеансов OData интеграции по расписанию
#sync.oData.schedulesEnabled: false
# Интервал экспорта OData интеграции 
#sync.oData.exportTimeInterval: 60
#################### Настройки трассировки производительности ####################
# Выключение функции трассировки производительности
#tracing.enabled: false
#################### Настройки электронной почты ####################
# Выключение функции проверки получения электронной почты
#email.listenerEnabled: false
# Выключение отправки электронной почты
#email.senderEnabled: false
#################### Настройки уведомлений ####################
# Выключение функции отправки уведомлений
#notifications.enabled: false
# Выключение отправки уведомлений по пользовательским задачам
#notifications.onUserTaskEnabled: false
# Выключение отправки уведомлений из обсуждений
#notifications.pushEnabled: false
# Выключение отправки уведомлений на страницах обслуживания
#notifications.onMaintenanceEnabled: false
#################### Настройка бизнес-процессов ####################
# Выключение функции бизнес-процессов
#bpms.enabled: false
# Количество потоков выполнения бизнес-процессов
#bpms.threadsCount: 4
# Выключение процессных таймеров
#bpms.timersEnabled: false
#################### Использование контейнера Docker ####################
# Включение контейнера Docker
#isContainerEnvironment: true
#################### Настройка обработчика сервис-запросов ####################
# Включение функции обработчика сервис-запросов
#requestProcessor.enabled: true
# Список обработчиков сервис-запросов. Если не указан, включает все доступные на узле (conversation, useractivity, notification, architect)
#requestProcessor.services:
#  - apiPrefix: conversation
#    enabled: true
# Конфигурация отображения количества строк таблицы на одной странице
#queryPageResultRange: [ 50, 500, 5000, 1000000000 ]
```
<!--instanceYML-end-->

## Конфигурация службы apigateway {: .pageBreakBefore }

1. Откройте файл конфигурации `apigateway.yml` экземпляра ПО для редактирования:

    ``` sh
    nano /var/www/<instanceName>/apigateway.yml
    ```

2. Измените необходимые параметры.
3. Удостоверьтесь, что значение параметра `cluster.name` (имя экземпляра ПО) совпадает с `clusterName` и значение параметров `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) — с аналогичными параметрами в [файле конфигурации экземпляра](#конфигурация-экземпляра-по).
4. Сохраните файл конфигурации.
5. Перезапустите службу `apigateway`:

    ``` sh
    systemctl restart apigateway<instanceName>
    ```

### Пример конфигурации службы apigateway.yml {: .pageBreakBefore }

<!--apigatewayYML-start-->
``` yml
# Имя экземпляра ПО
cluster.name: <instanceName>
# Имя узла экземпляра
# nodeName:
# Включение/выключение конфигурации журналирования экземпляра (true | false)
log.enabled: true
# Путь к файлу конфигурации журналирования экземпляра
log.configurationFile: /var/www/<instanceName>/logs.config
kata.enabled: false
# Адрес сервера очереди сообщений {{ apacheKafkaVariants }} с портом.
mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>
# Идентификатор группы очереди сообщений
mq.group: <instanceName>
# Идентификатор узла очереди сообщений
mq.node: <instanceName>
# Тип механизма SASL. (None | Plain | ScramSha256 | ScramSha512)
mq.sasl.mechanism: None
# Протокол безопасности очереди сообщений. (Plaintext | Ssl | SaslPlaintext | SaslSsl)
mq.securityProtocol: Plaintext
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
# Префиксы служб API
services:
- apiPrefix: conversation
- apiPrefix: useractivity
- apiPrefix: notification
- apiPrefix: architect
```
<!--apigatewayYML-end-->

## Конфигурация службы adapterhost {: .pageBreakBefore }

1. Откройте файл конфигурации `adapterhost.yml` экземпляра ПО для редактирования:

    ``` sh
    nano /var/www/<instanceName>/adapterhost.yml
    ```

2. Измените необходимые параметры.
3. Удостоверьтесь, что значения параметров `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) и `clusterName` (имя экземпляра ПО) совпадают с аналогичными параметрами в [файле конфигурации экземпляра ПО](#пример-yml-файла-конфигурации-экземпляра-по).
4. Сохраните файл конфигурации.
5. После внесения изменений перезапустите службу `adapterhost`:

    ``` sh
    kill -9 $(ps -eo pid,args | grep $<instanceName> | grep Agent | awk {'print $1'}) && systemctl restart comindware<instanceName>
    ```

### Пример файла конфигурации adapterhost.yml

<!--adapterhostYML-start-->
``` yml
# Имя экземпляра ПО
clusterName: <instanceName>
# Имя папки загрузчика экземпляра ПО
loaderFolder: <instanceName>
# Язык сервера (en-US | ru-RU )
serverLanguage: ru-RU
# Адрес и порт сервера очереди сообщений {{ apacheKafkaVariants }}
mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>
# Протокол безопасности очереди сообщений. (Plaintext | Ssl | SaslPlaintext | SaslSsl)
mq.securityProtocol: Plaintext
# Тип механизма SASL (None | Plain | ScramSha256 | ScramSha512)
mq.sasl.mechanism: None
# Путь к файлам журналирования экземпляра ПО
log.folder: /var/log/comindware/<instanceName>/Logs/
# Максимальное кол-во файлов журналов
log.maxArchiveFiles: 100
# Максимальный размер файлов журналов (байты)
log.archiveAboveSize: 1048576000
# Путь к архивам журналов
log.archiveFolder: /var/log/comindware/<instanceName>/Logs/Archive/
```
<!--adapterhostYML-end-->

## Конфигурация {{ apacheIgniteVariants }} {: .pageBreakBefore }

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

## Конфигурация кучи Java {: .pageBreakBefore }

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

## Конфигурация {{ nginxVariants }} {: .pageBreakBefore }

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

- _[Пути и содержимое директорий экземпляра ПО][paths]_
- _[Настройка конфигурации вспомогательного ПО для оптимизации работы {{ productName }}][auxiliary_software_optimize]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
