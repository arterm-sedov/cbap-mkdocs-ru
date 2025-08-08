---
title: Конфигурация экземпляра, компонентов ПО и служб. Настройка
kbId: 5067
---

# Конфигурация экземпляра, компонентов ПО и служб. Настройка

## Введение

Здесь представлены инструкции по настройке файлов конфигурации после развёртывания и обновления ПО **{{ productName }}**, его компонентов и служб.

## Конфигурация экземпляра ПО

1. Откройте файл конфигурации экземпляра ПО (`<instanceName>` — имя экземпляра ПО) для редактирования:

   ```
   nano /usr/share/comindware/configs/instance/<instanceName>.yml

   ```
2. При необходимости измените параметры, например:

   - `journal.server` — адрес сервера OpenSearch (Elasticsearch).
   - `journal.name` — индекс сервера OpenSearch (Elasticsearch).
   - `db.workDir` — директория для хранения базы данных экземпляра ПО.
   - `db.name` — префикс кэшей в базе данных экземпляра ПО.
   - `userStorage.localDisk.path` — директория для хранения загруженных файлов.
   - `mq.server` — адрес сервера Apache Kafka.
   - `backup.defaultFolder` — директория для хранения резервных копий экземпляра ПО.
   - `backup.defaultFileName` — имя файла резервной копии экземпляра ПО.

   Внимание!

   Директивы `isFederationAuthEnabled` и `manageAdapterHost` требуется удалить, если они присутствуют.

   Директивы `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) и `cluster.name` / `clusterName` (имя экземпляра ПО) должны совпадать в трёх файлах конфигурации:

   - `/usr/share/comindware/configs/instance/<instanceName>.yml`
   - `/var/www/<instanceName>/adapterhost.yml`
   - `/var/www/<instanceName>/apigateway.yml`
3. Сохраните файл конфигурации.
4. Убедитесь, что директории, указанные в файле конфигурации, существуют. При необходимости создайте их и задайте права доступа:

   ```
   mkdir -p <path/to/Database>
   mkdir -p <path/to/Streams>
   mkdir -p <path/to/Backup>
   chown -R <User>:<Group> <path/to/Database> <path/to/Streams> <path/to/Backup>

   ```

   Здесь значения `<User>` и `<Group>` должны совпадать с такими же параметрами в файле `/usr/lib/systemd/system/comindware<instanceName>.service`
5. Перезапустите службу экземпляра ПО:

   ```
   systemctl restart comindware<instanceName>

   ```

### Пример YML-файла конфигурации экземпляра ПО

```
##### Настройка базовых параметров ПО #####
# Имя экземпляра ПО.
# Устаревшая директива: instanceName
clusterName: <instanceName>
# Имя узла экземпляра ПО.
#nodeName: <instanceName>
# Путь к экземпляру, по которому ПО находит свою конфигурацию.
configPath: <configPath>
# Адрес службы журналирования (OpenSearch (Elasticsearch)).
# Устаревшая директива: elasticsearchUri
journal.server: http://<searchHostIP>:<searchHostPort>
# Индекс службы журналирования.
# journal.name: <prefix>-<instanceName>
# Выключение службы журналирования.
#journal.enabled: false
# URI-адрес экземпляра ПО
fqdn: <hostName>
# Порт экземпляра ПО
port: <portNumber>
# Версия экземпляра ПО
version: <versionNumber>

##### Настройка базы данных #####
# Использование тонкого клиента.
#db.asThinClient: true
# Конечные точки для подключения тонкого клиента.
#db.asThinClientEndpoints: 127.0.0.1:10800
# Путь к базе данных.
# Устаревшая директива: databasePath
db.workDir: /var/lib/comindware/<instanceName>/Database
# Папка установки Apache Ignite.
#db.homeDir:
# Путь к файлу конфигурации Apache Ignite.
#db.configPath:
# Настройки JVM.
#db.jvmOpts:
# Настройки Java.
#db.javaOpts:
# Включение автоматической настройки узлов Apache Ignite.
#db.baselineAutoAdjustEnabledFlag: false
# Время ожидания фактического изменения настройки узлов Apache Ignite
# с момента последнего изменения.
#db.baselineAutoAdjustTimeout: 3000
# Согласованный глобальный уникальный идентификатор узла Apache Ignite.
#db.consistentId:
# Используемый префикс кэшей в базе данных
# Устаревшая директива: databaseName
db.name: <instanceName>
# Префикс кэшей в базе данных, используемый при обновлении.
#db.upgradeName:
# Путь к онтологии Comindware
#db.n3Dir:

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

##### Настройка очереди сообщений #####
# Адрес и порт сервера очереди сообщений Apache Kafka.
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
# Путь к файлу корневого сертификата сервера очереди сообщений.
#mq.ssl.caLocation:
# Выключение идентификации адреса сервера очереди сообщений.
#mq.ssl.endpointIdentificationEnabled: false

##### Настройка SASL-подключения очереди сообщений #####
# Имя пользователя, используемое для подключения посредством SASL.
#mq.sasl.username:
#Пароль для аутентификации, используемый для подключения посредством SASL.
#mq.sasl.password:
# Тип механизма SASL (None | Plain | ScramSha256 | ScramSha512).
#mq.sasl.mechanism:

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
#backup.default.<backupName>.repository.localDisk.path: /var/backups/<iname>
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
# Управление составом резервной копии — файлы истории (OpenSearch (Elasticsearch)).
#backup.default.<backupName>.withJournal: true

##### Настройка дополнительного хранилища для конфигурации резервного копирования по умолчанию #####
# Тип хранилища (LocalDisk | S3).
#backup.default.<backupName>.extraRepository.type: LocalDisk
# Путь к файлам резервных копий.
#backup.default.<backupName>.extraRepository.localDisk.path: /var/backups/<instanceName>ExtraRepository
# Имя корзины S3 для хранения файлов резервных копий.
#backup.default.<backupName>.extraRepository.s3.bucket:
# Имя подключения к S3.
#backup.default.<backupName>.extraRepository.s3.connection: <s3ConnectionName>

##### Настройка резервного копирования данных службы журналирования (OpenSearch (Elasticsearch)) #####
# Тип хранилища (LocalDisk | S3).
#backup.journalRepository.type: LocalDisk
# Путь к файлам резервных копий
#backup.journalRepository.localDisk.path: /var/backups/<instanceName>
# Имя корзины S3 для хранения файлов резервных копий.
#backup.journalRepository.s3.bucket:
# Имя подключения, настроенного в конфигурации службы журналирования.
#backup.journalRepository.s3.journalConnection: <s3ConnectionName>
# Имя подключения к S3, настроенного в этом файле конфигурации экземпляра ПО.
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
# Выключение функции проверки наличия и получения новых писем.
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

```

## Конфигурация службы apigateway

1. Откройте файл конфигурации `apigateway.yml` экземпляра ПО для редактирования:

   ```
   nano /var/www/<instanceName>/apigateway.yml

   ```
2. Измените необходимые параметры.
3. Удостоверьтесь, что значение параметра `cluster.name` (имя экземпляра ПО) совпадает с `clusterName` и значение параметров `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) — с аналогичными параметрами в [файле конфигурации экземпляра](#конфигурация-экземпляра-по).
4. Сохраните файл конфигурации.
5. Перезапустите службу `apigateway`:

   ```
   systemctl restart apigateway<instanceName>

   ```

### Пример конфигурации службы apigateway.yml

```
# Имя экземпляра ПО
cluster.name: <instanceName>
# Имя узла экземпляра
# nodeName:
# Включение/выключение конфигурации журналирования экземпляра (true | false)
log.enabled: true
# Путь к файлу конфигурации журналирования экземпляра
log.configurationFile: /var/www/<instanceName>/logs.config
kata.enabled: false
# Адрес сервера очереди сообщений Apache Kafka с портом.
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

## Конфигурация службы adapterhost

1. Откройте файл конфигурации `adapterhost.yml` экземпляра ПО для редактирования:

   ```
   nano /var/www/<instanceName>/adapterhost.yml

   ```
2. Измените необходимые параметры.
3. Удостоверьтесь, что значения параметров `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) и `clusterName` (имя экземпляра ПО) совпадают с аналогичными параметрами в [файле конфигурации экземпляра ПО](#пример-yml-файла-конфигурации-экземпляра-по).
4. Сохраните файл конфигурации.
5. После внесения изменений перезапустите службу `adapterhost`:

   ```
   systemctl restart adapterhost<instanceName>

   ```

### Пример файла конфигурации adapterhost.yml

```
# Имя экземпляра ПО
clusterName: <instanceName>
# Имя папки загрузчика экземпляра ПО
loaderFolder: <instanceName>
# Язык сервера (en-US | ru-RU )
serverLanguage: ru-RU
# Адрес и порт сервера очереди сообщений Apache Kafka
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

## Конфигурация Apache Ignite

1. Откройте файл конфигурации Apache Ignite для редактирования:

   ```
   nano /var/www/<instanceName>/Ignite.config

   ```
2. В блоке `<bean class="org.apache.ignite.configuration.DataRegionConfiguration">` задайте максимальный объём выделяемой памяти:

   - 3 ГБ:

     ```
     <property name="maxSize" value="#{3L * 1024 * 1024 * 1024}" />

     ```
   - 8 ГБ:

     ```
     <property name="maxSize" value="#{8L * 1024 * 1024 * 1024}" />

     ```
3. В случае изменения максимального объёма выделяемой памяти отредактируйте параметр `checkpointPageBufferSize`. Чтобы рассчитать размер значения, разделите размер `maxSize` на четыре, при этом значение должно быть в диапазоне 256 МБ — 2 ГБ.

   - 8 ГБ:

     ```
     <property name="checkpointPageBufferSize" value="#{2L * 1024 * 1024 * 1024}" />

     ```
4. Перезапустите службу экземпляра ПО:

   ```
   systemctl restart comindware<instanceName>

   ```

## Конфигурация кучи Java

В зависимости от объёма оперативной памяти на сервере следует отредактировать конфигурацию области памяти для кучи Java.

1. Откройте файл конфигурации среды экземпляра ПО для редактирования:

   ```
   nano /etc/sysconfig/comindware<instanceName>-env

   ```
2. Задайте объём памяти, который выделяется для кучи Java:

   ```
   JVM_OPTS=-Xms512m -Xmx16g -XX:MaxDirectMemorySize=1g ...

   ```

   Здесь:

   - `-Xms` — начальный размер кучи;
   - `-Xmx` — максимальный размер кучи.
3. Сохраните файл конфигурации.
4. Перезапустите службу экземпляра ПО:

   ```
   systemctl daemon-reload
   systemctl restart comindware<instanceName>

   ```

## Конфигурация NGINX

1. Откройте файл конфигурации NGINX для редактирования:

   - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

     ```
     nano /etc/nginx/sites-available/comindware<instanceName>

     ```
   - **РЕД ОС**, **Rocky** (RPM-based)

     ```
     nano /etc/nginx/conf.d/comindware<instanceName>

     ```
   - **Альт Сервер**

     ```
     nano /etc/nginx/sites-available.d/comindware<instanceName>

     ```
2. В директиве `server` задайте номер порта и адрес сервера, по которым будет доступен экземпляр ПО:

   ```
   server {
       # Адрес сервера для доступа к экземпляру ПО.
       server_name <hostName>
       # Номер порта для доступа к экземпляру ПО.
       listen <portNumber>
   }

   ```
3. Для записи событий в отдельные журналы укажите их:

   ```
       error_log /var/log/nginx/<instanceName>-error.log;
       access_log /var/log/nginx/<instanceName>-access.log;

   ```
4. Сохраните файл конфигурации.
5. Проверьте, что изменения работают корректно:

   ```
   nginx -t

   ```
6. При успешном вступлении изменений в силу перезагрузите NGINX:

   ```
   nginx -s reload

   ```

--8<-- "related_topics_heading.md"

- *[Пути и содержимое директорий экземпляра ПО][paths]*
- *[Настройка конфигурации вспомогательного ПО для оптимизации работы {{ productName }}][auxiliary_software_optimize]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
