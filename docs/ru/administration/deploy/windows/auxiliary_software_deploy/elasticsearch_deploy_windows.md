---
title: Elasticsearch. Установка в базовой конфигурации для Windows
kbId: 4617
---

# Elasticsearch. Установка в базовой конфигурации для Windows {: #elasticsearch_deploy_windows}

## Введение

Для работы **{{ productName }}** требуется сервер Elasticsearch. См. [системные требования][system_requirements].

В случае установки **{{ productName }}** версии {{ productVersion }} в Windows [Утилита администрирования][admin_utility_install_launch] устанавливает службу Elasticsearch в папку `C:\Program Files\Elasticsearch\elasticsearch-8.1.0\`.

Установленная таким образом служба Elasticsearch имеет базовую конфигурацию: без аутентификации и с одним узлом. Она доступна по адресу `localhost:9200`.

Вы можете использовать имеющуюся службу Elasticsearch или развернуть её на отдельном сервере.

Здесь представлены требования к техническому обеспечению и инструкции по развёртыванию службы Elasticsearch в ОС Windows, а также приведён пример типового файла конфигурации. Инструкции представлены для версии Elasticsearch 8.10.2, для других версий содержимое файлов конфигурации и порядок установки могут быть иными.

{%
include-markdown ".snippets/elasticsearch_opensearch_configure.md"
rewrite-relative-urls=false
%}

## Требования к компьютеру

Сервер Elasticsearch создает значительную нагрузку на вычислительные ресурсы компьютера, поэтому рекомендуется:

- использовать отдельный SSD-диск для хранения журналов и данных сервера Elasticsearch;
- осуществлять мониторинг свободного места на диске, так как сервер перестает записывать данные, если на диске мало свободного места;
- использовать высокопроизводительный компьютер с достаточным объемом ОЗУ и количеством ядер ЦП, так как для обработки каждого индекса создается отдельный поток, а индексов может быть много.

## Установка Elasticsearch

Для установки Elasticsearch необходимо распаковать исполняемые файлы из ZIP-архива, а затем настроить переменные среды, службу Elasticsearch и конфигурацию сервера.

В процессе установки и настройки Elasticsearch все команды следует выполнять от имени администратора.

1. Скачайте файл `elasticsearch-<8.XX.X>-windows-x86_64.zip` c дистрибутивом Elasticsearch. Здесь `<8.XX.X>` — номер версии Elasticsearch.
2. Распакуйте архив в целевую папку, например: `C:\Program Files\Elastic\Elasticsearch\elasticsearch-<8.XX.X>`

    Последующие инструкции подразумевают, что сервер Elasticsearch установлен в эту папку.

3. Настройте переменные среды, как указано ниже:

    - Путь к исполняемым файлам Elasticsearch: `ES_HOME: C:\Program Files\Elasticsearch\elasticsearch\elasticsearch-<8.XX.X>`
    - Путь к JDK (требуется версия, совместимая с текущей версией Elasticsearch): `ES_JAVA_HOME: C:\Program Files\Elasticsearch\elasticsearch-<8.XX.X>\jdk`
    - Папка с файлами конфигурации: `ES_PATH_CONF: C:\Program Files\Elasticsearch\elasticsearch-<8.XX.X>\config`
    - Папка с файлами журналов: `SERVICE_LOG_DIR: C:\ProgramData\Elasticsearch\elasticsearch-<8.XX.X>\logs`
    - Директива для автоматического запуска службы: `ES_START_TYPE: auto`

4. Настройте службу Elasticsearch с помощью файла конфигурации `elasticsearch.yml`

    Можно скопировать его содержимое из раздела «[Пример типового файла конфигурации Elasticsearch](#пример-типового-файла-конфигурации-elasticsearch)».

5. Зарегистрируйте службу Elasticsearch, выполнив следующую команду:

    ``` sh
    "C:\Program Files\Elasticsearch\elasticsearch-<8.XX.X>\bin\elasticsearch-service.bat" install
    ```

6. Запустите службу Elasticsearch, выполнив следующую команду:

    ``` sh
    "C:\Program Files\Elasticsearch\elasticsearch-<8.XX.X>\bin\elasticsearch-service.bat" start
    ```

7. Сформируйте пароль для пользователя Elasticsearch с помощью следующей команды:

    ``` sh
    "C:\Program Files\Elasticsearch\elasticsearch-<8.XX.X>\bin\elasticsearch-reset-password.bat" –u elastic
    ```

8. Сохраните пароль, который отобразится на экране.

    !!! note "Примечание"

        Если пароль не отобразился, но отобразилось сообщение с предложением нажать клавишу ++y++ для просмотра пароля, нажмите клавишу ++y++.

9. Убедитесь, что служба Elasticsearch успешно зарегистрирована и работает с помощью приложения «Службы» (`services.msc`):

    _![Сведения о службе Elasticsearch в приложении «Службы»](https://kb.comindware.ru/assets/Picture5.png)_

10. Если служба Elasticsearch не запустилась:

    - проверьте ошибки конфигурации в журнале Elasticsearch по пути `C:\ProgramData\Elasticsearch\elasticsearch-<8.XX.X>\logs` (указанном в переменной окружения среды `SERVICE_LOG_DIR`).
    - устраните ошибки, запустите службу и проверьте работоспособность службы, как указано в пункте 8.

## Подключение к Elasticsearch при развертывании экземпляра продукта

1. Перед созданием экземпляра продукта укажите адрес сервера Elasticsearch, который будет использоваться по умолчанию для новых экземпляров продукта, в конфигурации Утилиты администрирования Comindware. См. _«[Утилита администрирования {{ companyName }}. Установка и использование][admin_utility_install_launch]»_.

    _![Настройка стандартного адреса сервера Elasticsearch](https://kb.comindware.ru/assets/Picture6.png)_

2. Если не был указан адрес сервера Elasticsearch в конфигурации Утилиты администрирования, то его потребуется указать при развертывании экземпляра продукта.
3. Укажите адрес сервера и префикс индекса Elasticsearch для данного экземпляра **{{ productName }}**.

    _![Настройка адреса сервера Elasticsearch для экземпляра продукта](https://kb.comindware.ru/assets/Picture7.png)_

4. После развертывания экземпляра продукта в разделе «**Администрирование системы**» — «**Подключения**» будет отображаться настроенное подключение к Elasticsearch.

    _![Подключение к Elasticsearch в новом экземпляре продукта](https://kb.comindware.ru/assets/Picture8.png)_

5. Чтобы изменить свойства подключения к Elasticsearch, дважды нажмите его строку в списке подключений.
6. Отобразится окно «**Свойства подключения: Elasticsearch**».
7. При необходимости измените свойства подключения, **проверьте соединение** и нажмите кнопку «**Сохранить**».

    _![Настройка свойств подключения к Elasticsearch](https://kb.comindware.ru/assets/Picture9.png)_

8. После изменения свойств сервера Elasticsearch перезапустите экземпляр продукта с помощью Утилиты администрирования {{ companyName }}. См.  _«[Утилита администрирования {{ companyName }}. Установка и использование][admin_utility_install_launch]»_.

## Пример типового файла конфигурации Elasticsearch

Ниже приведен пример файла `elasticsearch.yml` для следующей конфигурации сервера:

- сервер Elasticsearch состоит из единственного узла;
- сервер работает в локальной сети;
- включена аутентификация;
- сервер доступен через порт `9201`;
- адрес сервера `http://testhost:9201`;
- путь к файлу конфигурации: `C:\Program Files\Elastic\Elasticsearch\<8.XX.X>\config\elasticsearch.yml`

``` sh
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
path.data: d:\ProgramData\Elasticsearch\elasticsearch-<8.XX.X>\data

# Путь к папке с журналами
path.logs: d:\ProgramData\Elasticsearch\elasticsearch-<8.XX.X>\logs

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

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
