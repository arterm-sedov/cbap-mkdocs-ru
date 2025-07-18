---
title: Elasticsearch. Установка в базовой конфигурации для Windows
kbId: 4617
---

# Elasticsearch. Установка в базовой конфигурации для Windows

## Введение

Для работы **{{ productName }}** требуется сервер Elasticsearch. См. [системные требования][system_requirements].

Установщик **{{ productName }}** в Windows можно установить службу Elasticsearch в базовой конфигурацию: без аутентификации и с одним узлом. Она доступна по адресу `localhost:9200`.

См. *«[Установка, запуск, инициализация и остановка ПО в Windows][deploy_guide_windows]»*.

Вы можете использовать имеющуюся службу Elasticsearch или развернуть её на отдельном сервере.

Здесь представлены требования к техническому обеспечению и инструкции по развёртыванию службы Elasticsearch в ОС Windows, а также приведён пример типового файла конфигурации. Инструкции представлены для версии Elasticsearch 8.10.2, для других версий содержимое файлов конфигурации и порядок установки могут быть иными.

Служебный пользователь сервера журналирования транзакций OpenSearch (Elasticsearch)

- В конфигурации экземпляра ПО необходимо указать адрес сервера и уникальный префикс индексов OpenSearch (Elasticsearch). Индекс префикса служит для идентификации данных экземпляра ПО на сервере журналирования транзакций. Поэтому во избежание конфликтов данных для каждого экземпляра ПО следует указывать собственный префикс индекса.
- В конфигурации сервера журналирования транзакций необходимо создать одного пользователя для **{{ productName }}**.
- При инициализации экземпляра ПО или в конфигурации экземпляра необходимо указать пользователя **{{ productName }}**, используемого сервером журналирования транзакций.
- Экземпляр ПО будет взаимодействовать с сервером журналирования транзакций под указанным пользователем и создавать, наполнять и читать индексы с заданным префиксом.

## Требования к компьютеру

Сервер Elasticsearch создает значительную нагрузку на вычислительные ресурсы компьютера, поэтому рекомендуется:

- использовать отдельный SSD-диск для хранения журналов и данных сервера Elasticsearch;
- осуществлять мониторинг свободного места на диске, так как сервер перестает записывать данные, если на диске мало свободного места;
- использовать высокопроизводительный компьютер с достаточным объемом ОЗУ и количеством ядер ЦП, так как для обработки каждого индекса создается отдельный поток, а индексов может быть много.

## Установка Elasticsearch

Для установки Elasticsearch необходимо распаковать исполняемые файлы из ZIP-архива, а затем настроить переменные среды, службу Elasticsearch и конфигурацию сервера.

В процессе установки и настройки Elasticsearch все команды следует выполнять от имени администратора.

1. Скачайте файл `elasticsearch-<8.XX.X>-windows-x86_64.zip` c дистрибутивом Elasticsearch. Здесь `<8.XX.X>` — номер версии Elasticsearch.
2. Распакуйте архив в целевую папку, например: `C:\\Program Files\\Elastic\\Elasticsearch\\elasticsearch-<8.XX.X>`

   Последующие инструкции подразумевают, что сервер Elasticsearch установлен в эту папку.
3. Настройте переменные среды, как указано ниже:

   - Путь к исполняемым файлам Elasticsearch: `ES_HOME: C:\\Program Files\\Elasticsearch\\elasticsearch\\elasticsearch-<8.XX.X>`
   - Путь к JDK (требуется версия, совместимая с текущей версией Elasticsearch): `ES_JAVA_HOME: C:\\Program Files\\Elasticsearch\\elasticsearch-<8.XX.X>\\jdk`
   - Папка с файлами конфигурации: `ES_PATH_CONF: C:\\Program Files\\Elasticsearch\\elasticsearch-<8.XX.X>\\config`
   - Папка с файлами журналов: `SERVICE_LOG_DIR: C:\\ProgramData\\Elasticsearch\\elasticsearch-<8.XX.X>\\logs`
   - Директива для автоматического запуска службы: `ES_START_TYPE: auto`
4. Настройте службу Elasticsearch с помощью файла конфигурации `elasticsearch.yml`

   Можно скопировать его содержимое из раздела «[Пример типового файла конфигурации Elasticsearch](#elasticsearch_deploy_windows_config_example)».
5. Зарегистрируйте службу Elasticsearch, выполнив следующую команду:

   ```
   "C:\\Program Files\\Elasticsearch\\elasticsearch-<8.XX.X>\\bin\\elasticsearch-service.bat" install

   ```
6. Запустите службу Elasticsearch, выполнив следующую команду:

   ```
   "C:\\Program Files\\Elasticsearch\\elasticsearch-<8.XX.X>\\bin\\elasticsearch-service.bat" start

   ```
7. Сформируйте пароль для пользователя Elasticsearch с помощью следующей команды:

   ```
   "C:\\Program Files\\Elasticsearch\\elasticsearch-<8.XX.X>\\bin\\elasticsearch-reset-password.bat" –u elastic

   ```
8. Сохраните пароль, который отобразится на экране.

   Примечание

   Если пароль не отобразился, но отобразилось сообщение с предложением нажать клавишу `Y` для просмотра пароля, нажмите клавишу `Y`.
9. Убедитесь, что служба Elasticsearch успешно зарегистрирована и работает с помощью приложения «Службы» (`services.msc`):

   ![Сведения о службе Elasticsearch в приложении «Службы»](https://kb.comindware.ru/assets/Picture5.png)

   Сведения о службе Elasticsearch в приложении «Службы»
10. Если служба Elasticsearch не запустилась:

    - проверьте ошибки конфигурации в журнале Elasticsearch по пути `C:\\ProgramData\\Elasticsearch\\elasticsearch-<8.XX.X>\\logs` (указанном в переменной окружения среды `SERVICE_LOG_DIR`).
    - устраните ошибки, запустите службу и проверьте работоспособность службы, как указано в пункте 8.

## Подключение к Elasticsearch при развертывании экземпляра ПО

1. При необходимости при запуске экземпляра ПО **{{ productName }}** укажите адрес сервера и префикс индекса Elasticsearch для данного экземпляра.

   ![Настройка адреса сервера Elasticsearch для экземпляра ПО](https://kb.comindware.ru/assets/Picture7.png)

   Настройка адреса сервера Elasticsearch для экземпляра ПО
2. После развертывания экземпляра ПО в разделе «**Администрирование системы**» — «**Подключения**» будет отображаться настроенное подключение к Elasticsearch.

   ![Подключение к Elasticsearch в новом экземпляре ПО](/platform/v5.0/administration/deploy/windows/auxiliary_software_deploy/img/elasticsearch_deploy_windows_connection.png)

   Подключение к Elasticsearch в новом экземпляре ПО
3. Чтобы изменить свойства подключения к Elasticsearch, дважды нажмите его строку в списке подключений.
4. Отобразится окно «**Свойства подключения: Elasticsearch**».
5. При необходимости измените свойства подключения, **проверьте соединение** и нажмите кнопку «**Сохранить**».

   ![Настройка свойств подключения к Elasticsearch](/platform/v5.0/administration/deploy/windows/auxiliary_software_deploy/img/elasticsearch_deploy_windows_connection_configure.png)

   Настройка свойств подключения к Elasticsearch
6. После изменения свойств сервера Elasticsearch перезапустите экземпляр ПО.

## Пример типового файла конфигурации Elasticsearch

Ниже приведен пример файла `elasticsearch.yml` для следующей конфигурации сервера:

- сервер Elasticsearch состоит из единственного узла;
- сервер работает в локальной сети;
- включена аутентификация;
- сервер доступен через порт `9201`;
- адрес сервера `http://testhost:9201`;
- путь к файлу конфигурации: `C:\\Program Files\\Elastic\\Elasticsearch\\<8.XX.X>\\config\\elasticsearch.yml`

```
# Начало файла конфигурации
#Разрешить свопинг памяти
bootstrap.memory_lock: false

# Название кластера
cluster.name: cmw

# Максимальное возможное количество шардов в кластере
# Система создает отдельный индекс для каждого объекта мониторинга, поэтому
# рекомендуется увеличить количество шардов до 3000
cluster.max_shards_per_node: 3000

# Стандартный номер порта 9200 изменен по соображениям безопасности
http.port: 9201

# Сетевые параметры
# Если доступ по сети не требуется,
# то уберите строки #network.host и discovery.seed_hosts
# Замените имя компьютера `testhost` на реальное имя
network.host: testhost
discovery.seed_hosts:
  - testhost

# Простейшая конфигурация с одним узлом
discovery.type: single-node

# Название узла
node.name: cmw

# Путь к папке с данными
path.data: d:\\ProgramData\\Elasticsearch\\elasticsearch-<8.XX.X>\\data

# Путь к папке с журналами
path.logs: d:\\ProgramData\\Elasticsearch\\elasticsearch-<8.XX.X>\\logs

# Путь к папке с резервными копиями
# Путь должен указывать на существующий диск
# Резервные копии должны храниться на отдельном диске отдельно от основных данных
# Включите в конфигурацию директиву path.repo, если требуется создавать резервные копии
# path.repo: d:elastic_backup

# Обычная лицензия
xpack.license.self_generated.type: basic

# Аутентификация включена
xpack.security.enabled: true

# Запись данных в индексы включена
indices.id_field_data.enabled: true

# Геолокация отключена
ingest.geoip.downloader.enabled: false

```

--8<-- "related_topics_heading.md"

- [Установка, запуск, инициализация и остановка ПО в Windows][deploy_guide_windows]
- [Пути и содержимое директорий экземпляра ПО][paths_windows]

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
