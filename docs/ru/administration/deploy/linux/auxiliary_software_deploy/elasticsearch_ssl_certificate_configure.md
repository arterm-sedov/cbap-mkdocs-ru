---
title: Настройка SSL-сертификатов на кластере OpenSearch (Elasticsearch)
kbId: 4606
tags:
tags:
    - Elasticsearch
    - OpenSearch
    - Linux
    - сертификаты
    - администрирование
    - безопасность
    - кластер
    - настройка
    - развёртывание
    - сервер
    - установка
hide: tags
---

# Настройка SSL-сертификатов для {{ openSearchVariants }} {: #elasticsearch_ssl_certificate_configure }

## Введение {: #elasticsearch_ssl_certificate_configure_introduction }

Для работы ПО **{{ productName }}** требуется сервер {{ openSearchVariants }}.

Здесь представлены инструкции по формированию SSL-сертификатов подлинности узлов и настройке {{ openSearchVariants }} с проверкой сертификатов подлинности для {{ openSearchVariants }}.

Перед выполнением нижеприведённых инструкций необходимо развернуть {{ openSearchVariants }} без сертификатов подлинности.

Дальнейшие инструкции предполагают, что кластер и служба {{ openSearchVariants }} развёрнуты согласно инструкциям в статье «**[Установка {{ openSearchVariants }} и настройка кластера {{ openSearchVariants }} без сертификатов подлинности][elasticsearch_cluster_deploy_no_certificates]**» на виртуальных машинах с Linux.

## Формирование SSL-сертификатов {: #elasticsearch_ssl_certificate_configure_ssl_certificates .pageBreakBefore }

### Установка Open SSL {: #elasticsearch_ssl_certificate_configure_openssl_install }

1. Проверьте, установлен ли пакет `openssl` в операционной системе:

    - Для дистрибутивов на базе Debian:

        ``` sh
        dpkg --list | grep openssl
        ```

    - Для дистрибутивов на базе RHEL:

        ``` sh
        dnf list installed | grep openssl
        ```

2. При необходимости перед установкой OpenSSL обновите ПО:

    ``` sh
    sudo apt update
    sudo apt upgrade
    ```

3. Установите OpenSSL (для дистрибутивов на базе Debian; для других дистрибутивов используйте соответствующий менеджер пакетов):

    ``` sh
    sudo apt install openssl
    ```

### Формирование сертификата СА {: #elasticsearch_ssl_certificate_configure_ca_certificate .pageBreakBefore }

1. В домашней директории пользователя `<username>` создайте директорию для выполнения дальнейших операций (например, `certsGen`):

    ``` sh
    mkdir certsGen
    ```

2. Перейдите в директорию `certsGen`:

    ``` sh
    cd certsGen/
    ```

3. <a id="P1_2_3"></a>Создайте закрытый ключ `ca-key.pem` для центра сертификации (CA):

    ``` sh
    openssl genpkey -out ca-key.pem -algorithm RSA -pkeyopt rsa_keygen_bits:2048
    ```

4. Создайте сертификат СА `ca.pem`:

    ``` sh
    openssl req -new -x509 -sha256 -key ca-key.pem -out ca.pem -days 3650 -subj "/CN=ElasticSearchCA"
    ```

5. В результате вы получите:

    - файл `ca-key.pem` — закрытый ключ центра сертификации;
    - файл `ca.pem` — сертификат центра сертификации.

### Формирование ключей и сертификатов для узлов кластера {{ openSearchVariants }} {: #elasticsearch_ssl_certificate_configure_node_certificates .pageBreakBefore }

Для примера далее используется один узел {{ openSearchVariants }}. Для дополнительных узлов повторите шаги, подставив фактические IP‑адреса вместо `<XXX.XXX.XXX.XXX>`.

1. <a id="P1_3_1"></a>Создайте закрытый ключ узла `elastic-key.pem`:

    ``` sh
    openssl genpkey -out elastic-key.pem -algorithm RSA -pkeyopt rsa_keygen_bits:2048
    ```

2. Создайте файл описания узла `openssl.cnf` со следующим содержимым (подставьте фактический IP‑адрес узла {{ openSearchVariants }} вместо `<XXX.XXX.XXX.XXX>`):

    ``` ini
    [ req ]
    distinguished_name = req_distinguished_name
    req_extensions = req_ext
    prompt = no

    [ req_distinguished_name ]
    CN = <XXX.XXX.XXX.XXX>

    [ req_ext ]
    subjectAltName = @alt_names

    [ alt_names ]
    IP.1 = <XXX.XXX.XXX.XXX>
    ```

3. Используя файл описания `openssl.cnf` и ключ узла `elastic-key.pem`, создайте запрос на сертификат (CSR) `elastic.csr`:

    ``` sh
    openssl req -new -key elastic-key.pem -out elastic.csr -config openssl.cnf
    ```

4. <a id="P1_3_4"></a>Используя CSR, сертификат CA и закрытый ключ CA, создайте подписанный CA сертификат узла {{ openSearchVariants }} `elastic-cert.pem`:

    ``` sh
    openssl x509 -req -in elastic.csr -CA ca.pem -CAkey ca-key.pem -CAcreateserial -out elastic-cert.pem -days 365 -sha256 -extfile openssl.cnf -extensions req_ext
    ```

5. Аналогично [шагам 1–4](#P1_3_1) создайте ключи и сертификаты для остальных узлов {{ openSearchVariants }}, указывая их IP‑адреса в `openssl.cnf`.

### Отправка созданных сертификатов на узлы кластера {: #elasticsearch_ssl_certificate_configure_send_certs_to_nodes .pageBreakBefore }

1. Отправьте созданные сертификаты с помощью `SSH` (подставьте свои имена файлов, имя пользователя вместо `<username>` и IP‑адрес вместо `<XXX.XXX.XXX.XXX>`):

    ``` sh
    sudo scp ca.pem <username>@<XXX.XXX.XXX.XXX>:/home/<username>/
    sudo scp elastic-cert.pem <username>@<XXX.XXX.XXX.XXX>:/home/<username>/
    sudo scp elastic-key.pem <username>@<XXX.XXX.XXX.XXX>:/home/<username>/
    ```

2. На каждом из узлов перенесите сгенерированные файлы в директорию, из которой {{ openSearchVariants }} будет считывать сертификаты (например, `/etc/elasticsearch/`):

    ``` sh
    sudo mv /home/<username>/ca.pem /etc/elasticsearch/
    sudo mv /home/<username>/elastic-cert.pem /etc/elasticsearch/
    sudo mv /home/<username>/elastic-key.pem /etc/elasticsearch/
    ```

3. Задайте владельца и права доступа к директории:

    ``` sh
    sudo chown elasticsearch:elasticsearch --recursive /etc/elasticsearch/
    sudo chmod 764 --recursive /etc/elasticsearch/
    ```

## Настройка кластера {{ openSearchVariants }} {: #elasticsearch_ssl_certificate_configure_cluster_configuration .pageBreakBefore }

### Добавление сертификата CA в хранилище сертификатов ОС и Mono Framework {: #elasticsearch_ssl_certificate_configure_add_ca_to_stores}

1. Добавьте сертификат CA в хранилище сертификатов операционной системы (пример для дистрибутивов на базе Debian):

    ``` sh
    sudo cp /etc/elasticsearch/ca.pem /usr/local/share/ca-certificates/ca.crt
    sudo update-ca-certificates
    ```

2. Добавьте сертификат CA в хранилище сертификатов Mono Framework:

    ``` sh
    sudo mono /usr/lib/mono/4.5/cert-sync.exe /etc/elasticsearch/ca.pem
    ```

### Настройка узла кластера для работы с SSL-сертификатами {: #elasticsearch_ssl_certificate_configure_node_ssl_settings .pageBreakBefore }

1. Для каждого узла кластера {{ openSearchVariants }} отредактируйте `yml`-файл конфигурации {{ openSearchVariants }}, как показано в примерах ниже. Внимательно следите за сохранением отступов:

    ``` sh
    sudo nano /etc/elasticsearch/elasticsearch.yml
    ```

2. Добавьте настройки SSL для узла {{ openSearchVariants }}, указав фактические пути к созданным файлам `elastic-key.pem`, `elastic-cert.pem` и `ca.pem`:

    ``` yaml
    xpack.security.enabled: true

    xpack.security.transport.ssl.enabled: true
    xpack.security.transport.ssl.verification_mode: certificate
    xpack.security.transport.ssl.key: /etc/elasticsearch/elastic-key.pem
    xpack.security.transport.ssl.certificate: /etc/elasticsearch/elastic-cert.pem
    xpack.security.transport.ssl.certificate_authorities: [ "/etc/elasticsearch/ca.pem" ]

    xpack.security.http.ssl.enabled: true
    xpack.security.http.ssl.key: /etc/elasticsearch/elastic-key.pem
    xpack.security.http.ssl.certificate: /etc/elasticsearch/elastic-cert.pem
    xpack.security.http.ssl.certificate_authorities: [ "/etc/elasticsearch/ca.pem" ]
    ```

3. Ниже приведён пример файла `elasticsearch.yml` для конфигурации с одним узлом. При необходимости адаптируйте параметры `cluster.name`, `node.name`, `http.host` и другие настройки в соответствии с вашей конфигурацией:

    ``` yaml
    #======================== {{ openSearchVariants }} Configuration =========================

    cluster.name: my-application

    # ------------------------------------ Node ------------------------------------

    node.name: node-1

    # ----------------------------------- Paths ------------------------------------

    path.data: /var/lib/elasticsearch # database path {{ openSearchVariants }}
    path.logs: /var/log/elasticsearch # путь к файлам журнала {{ openSearchVariants }}
    #path.repo: /var/backups/elasticsearch # путь к репозиторию резервных копий {{ openSearchVariants }}

    # ----------------------------------- Memory -----------------------------------

    bootstrap.memory_lock: false

    # ---------------------------------- Network -----------------------------------

    # ниже указать IP сервера {{ openSearchVariants }} или 127.0.0.1, если {{ openSearchVariants }} и 
    # Comindware Business Application Platform развёрнуты на одной машине
    #network.host: 127.0.0.1  
    http.host: <XXX.XXX.XXX.XXX> # IP - слушать внешний интерфейс, 127.0.0.1 - localhost, 0.0.0.0 - все
    http.port: 9200 # порт по умолчанию

    # --------------------------------- Discovery ----------------------------------

    discovery.type: single-node # директива для работы в режиме одного узла
    #discovery.seed_hosts: ["<XXX.XXX.XX.XXX>"] # директива для работы кластера
    #cluster.initial_master_nodes: ["<XXX.XXX.XX.XXX>"] # директива для работы кластера

    # ---------------------------------- Various -----------------------------------

    search.allow_expensive_queries: true
    action.destructive_requires_name: true
    indices.id_field_data.enabled: true

    # ---------------------------------- Security ----------------------------------

    xpack.security.enabled: true

    xpack.security.transport.ssl.enabled: true
    xpack.security.transport.ssl.verification_mode: certificate
    xpack.security.transport.ssl.key: /etc/elasticsearch/elastic-key.pem
    xpack.security.transport.ssl.certificate: /etc/elasticsearch/elastic-cert.pem
    xpack.security.transport.ssl.certificate_authorities: [ "/etc/elasticsearch/ca.pem" ]

    xpack.security.http.ssl.enabled: true
    xpack.security.http.ssl.key: /etc/elasticsearch/elastic-key.pem
    xpack.security.http.ssl.certificate: /etc/elasticsearch/elastic-cert.pem
    xpack.security.http.ssl.certificate_authorities: [ "/etc/elasticsearch/ca.pem" ]
    ```

4. Сохраните изменения и закройте текстовый редактор Nano, нажав клавиши: ++ctrl+O++, ++enter++, ++ctrl+x++.
5. Повторите шаги 1–4 для каждого из узлов {{ openSearchVariants }}.

### Настройка параметров JVM для {{ openSearchVariants }} {: #elasticsearch_ssl_certificate_configure_jvm_settings .pageBreakBefore }

1. Откройте файл настроек JVM:

    ``` sh
    sudo nano /etc/elasticsearch/jvm.options
    ```

2. Убедитесь, что параметры начального и максимального размера кучи заданы и не закомментированы (значения подберите в соответствии с объёмом доступной памяти сервера):

    ``` text
    -Xms4g
    -Xmx4g
    ```

3. Сохраните изменения и закройте файл.

### Обновление хранилища сертификатов Linux и Mono Framework для сертификатов {{ openSearchVariants }} {: #elasticsearch_ssl_certificate_configure_update_linux_mono_stores}

1. Добавьте сертификат CA и сертификат узла в хранилище сертификатов Mono Framework (команды выполняются после копирования файлов в `/etc/elasticsearch/`):

    ``` sh
    sudo mono /usr/lib/mono/4.5/cert-sync.exe /etc/elasticsearch/ca.pem
    sudo mono /usr/lib/mono/4.5/cert-sync.exe /etc/elasticsearch/elastic-cert.pem
    ```

## Запуск {{ openSearchVariants }} {: #elasticsearch_ssl_certificate_configure_start_elasticsearch .pageBreakBefore .pageBreakBefore }

Выполните следующие шаги для каждого узла {{ openSearchVariants }}.

1. Перезагрузите конфигурацию `systemd`:

    ``` sh
    sudo systemctl daemon-reload
    ```

2. Перезапустите процесс `elasticsearch.service`:

    ``` sh
    sudo systemctl restart elasticsearch.service
    ```

3. Убедитесь, что процесс `elasticsearch.service` запустился:

    ``` sh
    sudo systemctl status elasticsearch.service
    ```

    ``` sh title="Пример результата проверки статуса процесса elasticsearch.service"
    elasticsearch.service - {{ openSearchVariants }}

        Loaded: loaded (/lib/systemd/system/elasticsearch.service; enabled; vendor preset: enabled)

        Active: active (running) since Thu 2022-12-01 10:12:27 UTC; 6s ago
            Docs: <https://www.elastic.co>
        Main PID: 3597 (java)
            Tasks: 63 (limit: 4575)
            Memory: 629.9M
            CPU: 44.422s
            CGroup: /system.slice/elasticsearch.service
                ├─3597 /usr/share/elasticsearch/jdk/bin/java -Xms4m -Xmx64m -XX:+UseSerialGC -Dcli.name=server -Dcli.scri>
                ├─3656 /usr/share/elasticsearch/jdk/bin/java -Des.networkaddress.cache.ttl=60 -Des.networkaddress.cache.n>
                └─3676 /usr/share/elasticsearch/modules/x-pack-ml/platform/linux-x86_64/bin/controller
    Dec 01 10:11:12 penguin-02 systemd[1]: Starting {{ openSearchVariants }}...
    Dec 01 10:12:27 penguin-02 systemd[1]: Started {{ openSearchVariants }}.
    ```

    !!! note "Примечание"
        В случае ошибок с запуском процесса `elasticsearch.service` рекомендуется изучить файл журнала:

        ``` sh
        sudo less /var/elasticsearch/logs/yourClusterName.log
        ```

4. Повторите шаги 1–3 для каждого из узлов {{ openSearchVariants }}.

### Сброс пароля пользователя `elastic` {: #elasticsearch_ssl_certificate_configure_reset_elastic_password .pageBreakBefore }

1. При необходимости сбросьте пароль для встроенного пользователя `elastic`:

    ``` sh
    sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password -i -u elastic
    ```

2. Следуйте интерактивным подсказкам утилиты и сохраните новый пароль.

## Присвоение сертификату статуса доверенного {: #elasticsearch_ssl_certificate_configure_trust_certificate .pageBreakBefore }

Перед проверкой состояния кластера необходимо присвоить новому источнику сертификата статус доверенного. Инструкции в данном разделе приведены для среды Windows 10.

1. Откройте в файловом менеджере директорию с сертификатом.
2. Откройте файл сертификата (например, `ca.pem` или предварительно переименованный в `CA.crt`).
3. В отобразившемся окне нажмите кнопку «**Установить сертификат**».
4. Выберите, следует ли хранить сертификат на уровне пользователя или на уровне машины.
5. Нажмите кнопку «**Далее**».
6. Выберите пункт «**Разместить все сертификаты в следующем хранилище**».
7. Нажмите кнопку «**Обзор**».
8. Выберите «**Доверенные корневые источники сертификатов**».
9. Нажмите кнопку «**ОК**».
10. Нажмите кнопку «**Далее**».
11. Нажмите кнопку «**Завершить**».
12. Если отобразится запрос, нажмите кнопку «**Да**».

## Проверка состояния кластера {: #elasticsearch_ssl_certificate_configure_cluster_health_check .pageBreakBefore }

1. После того как для каждого из узлов кластера {{ openSearchVariants }} были выполнены шаги, описанные в предыдущих разделах, с любого из узлов выполните `GET`-запрос в веб-браузере:

    ``` sh
    https://192.168.XXX.XX1:9200/_cluster/health?pretty
    ```

2. Браузер отобразит форму для ввода учётных данных.
3. Введите имя встроенного суперпользователя `elastic` и один из автоматически сгенерированных паролей, которые были созданы при развёртывании {{ openSearchVariants }}.

    _![Ввод учётных данных для доступа к кластеру {{ openSearchVariants }}](https://kb.comindware.ru/assets/image2.png)_

4. Браузер отобразит данные `REST API` кластера {{ openSearchVariants }}.
5. Убедитесь, что значение параметра `number_of_nodes` равно количеству узлов кластера.

    _![Данные REST API кластера {{ openSearchVariants }}](https://kb.comindware.ru/assets/image1.png)_

## Настройка прав доступа и диагностика неполадок {: #elasticsearch_ssl_certificate_configure_permissions_troubleshooting .pageBreakBefore }

1. Убедитесь, что на необходимые каталоги выданы корректные права:

    - Назначьте владельца:

        ``` sh
        sudo chown -R elasticsearch:elasticsearch /var/lib/comindware/
        ```

    - Назначьте права доступа:

        ``` sh
        sudo chmod -R 766 /var/lib/comindware/
        ```

2. В случае возникновения проблем с библиотекой `jna-5.10.0.jar` или других ошибок в работе {{ openSearchVariants }} изучите журналы:

    ``` sh
    journalctl -xe
    tail -f /var/log/comindware/instanceName/Logs/audit_0000-00-00.log
    nano /var/log/comindware/instanceName/Logs/audit_0000-00-00.log
    cat /var/elasticsearch/logs/elasticsearch.example.cbap.log
    ```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Официальная документация Elasticsearch (английский язык)](https://www.elastic.co/docs/deploy-manage)
- [Официальная документация OpenSearch (английский язык)](https://docs.opensearch.org/latest/)
- [Установка и настройка Elasticsearch без сертификатов подлинности][elasticsearch_cluster_deploy_no_certificates]
- [Elasticsearch. Установка в базовой конфигурации][elasticsearch_deploy_Linux]
- [Установка, запуск, инициализация и остановка ПО {{ productName }}][deploy_guide_linux]
- [Конфигурация экземпляра, компонентов ПО и служб. Настройка][configuration_files_linux]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
