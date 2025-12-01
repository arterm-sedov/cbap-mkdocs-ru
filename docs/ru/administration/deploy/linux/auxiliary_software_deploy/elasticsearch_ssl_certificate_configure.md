---
title: Настройка SSL-сертификатов на кластере Elasticsearch
kbId: 4606
---

# Настройка SSL-сертификатов для Elasticsearch {: #elasticsearch_ssl_certificate_configure}

## Введение

Для работы ПО **{{ productName }}** требуется сервер Elasticsearch версии не ниже 8.1.0.

Здесь представлены инструкции по формированию SSL-сертификатов подлинности узлов и настройке Elasticsearch с проверкой сертификатов подлинности для Elasticsearch.

Перед выполнением нижеприведённых инструкций необходимо развернуть Elasticsearch без сертификатов подлинности.

Дальнейшие инструкции предполагают, что кластер и служба Elasticsearch развёрнуты согласно инструкциям в статье «**[Установка Elasticsearch и настройка кластера Elasticsearch без сертификатов подлинности][elasticsearch_cluster_deploy_no_certificates]**» на виртуальных машинах с Linux.

## Формирование SSL-сертификатов

### Установка Open SSL

1. Убедитесь, что пакет `openssl` установлен в операционной системе:

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

### Формирование сертификата СА {: .pageBreakBefore }

1. В домашней папке пользователя `username` создайте папку, в которой предстоит работать:

    ``` sh
    mkdir certsGen
    ```

2. Перейдите в папку `certsGen`:

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
    - файл `ca.pem` — сертификат центра сертификации (CA Certificate).

### Формирование ключей и сертификатов для узлов кластера Elasticsearch {: .pageBreakBefore }

Для примера далее используется один узел Elasticsearch. Для дополнительных узлов повторите шаги, подставив фактические IP‑адреса.

1. <a id="P1_3_1"></a>Создайте закрытый ключ узла `elastic-key.pem`:

    ``` sh
    openssl genpkey -out elastic-key.pem -algorithm RSA -pkeyopt rsa_keygen_bits:2048
    ```

2. Создайте файл описания узла `openssl.cnf` со следующим содержимым (подставьте фактический IP‑адрес узла Elasticsearch вместо `<XXX.XXX.XXX.XXX>`):

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

4. <a id="P1_3_4"></a>Используя CSR, сертификат CA и закрытый ключ CA, создайте подписанный CA сертификат узла Elasticsearch `elastic-cert.pem`:

    ``` sh
    openssl x509 -req -in elastic.csr -CA ca.pem -CAkey ca-key.pem -CAcreateserial -out elastic-cert.pem -days 365 -sha256 -extfile openssl.cnf -extensions req_ext
    ```

5. Аналогично [шагу 1.3.1](#P1_3_1)–[шагу 1.3.4](#P1_3_4) создайте ключи и сертификаты для остальных узлов Elasticsearch, указывая их IP‑адреса в `openssl.cnf`.

### Отправка созданных сертификатов на узлы кластера {: .pageBreakBefore }

1. Отправьте созданные сертификаты с помощью `SSH` (подставьте свои имена файлов, имя пользователя и IP‑адрес):

    ``` sh
    sudo scp ca.pem username@<XXX.XXX.XXX.XXX>:/home/username/
    sudo scp elastic-cert.pem username@<XXX.XXX.XXX.XXX>:/home/username/
    sudo scp elastic-key.pem username@<XXX.XXX.XXX.XXX>:/home/username/
    ```

2. В каждом из узлов перенесите сгенерированные файлы в папку, из которой Elasticsearch будет считывать сертификаты (например, `/etc/elasticsearch/`):

    ``` sh
    sudo mv /home/username/ca.pem /etc/elasticsearch/
    sudo mv /home/username/elastic-cert.pem /etc/elasticsearch/
    sudo mv /home/username/elastic-key.pem /etc/elasticsearch/
    ```

3. Измените пользователя для директории и настройте права доступа:

    ``` sh
    sudo chown elasticsearch:elasticsearch --recursive /etc/elasticsearch/
    sudo chmod 764 --recursive /etc/elasticsearch/
    ```

## Настройка кластера Elasticsearch {: .pageBreakBefore }

### Добавление сертификата CA в хранилище сертификатов ОС и Mono

1. Добавьте сертификат CA в хранилище сертификатов операционной системы (пример для дистрибутивов на базе Debian):

    ``` sh
    sudo cp /etc/elasticsearch/ca.pem /usr/local/share/ca-certificates/ca.crt
    sudo update-ca-certificates
    ```

2. Добавьте сертификат CA в хранилище сертификатов платформы Mono Framework:

    ``` sh
    sudo mono /usr/lib/mono/4.5/cert-sync.exe /etc/elasticsearch/ca.pem
    ```

### Настройка узла кластера для работы с SSL-сертификатами {: .pageBreakBefore }

1. Для каждого узла кластера Elasticsearch отредактируйте `yml`-файл конфигурации Elasticsearch, как показано в примерах ниже. Внимательно следите за сохранением отступов. Воспользуйтесь текстовым редактором Nano:

    ``` sh
    sudo nano /etc/elasticsearch/elasticsearch.yml
    ```

2. Добавьте настройки SSL для узла Elasticsearch, указав фактические пути к созданным файлам `elastic-key.pem`, `elastic-cert.pem` и `ca.pem`:

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

3. Ниже приведён пример файла `elasticsearch.yml` для одиночного узла (single-node). При необходимости адаптируйте параметры `cluster.name`, `node.name`, `http.host` и другие настройки под вашу инфраструктуру:

    ``` yaml
    #======================== Elasticsearch Configuration =========================

    cluster.name: my-application

    # ------------------------------------ Node ------------------------------------

    node.name: node-1

    # ----------------------------------- Paths ------------------------------------

    path.data: /var/lib/elasticsearch # database path Elasticsearch
    path.logs: /var/log/elasticsearch # путь к файлам журнала Elasticsearch
    #path.repo: /var/backups/elasticsearch # путь к репозиторию резервных копий Elasticsearch

    # ----------------------------------- Memory -----------------------------------

    bootstrap.memory_lock: false

    # ---------------------------------- Network -----------------------------------

    # ниже указать IP сервера Elasticsearch или 127.0.0.1, если Elasticsearch и 
    # Comindware Business Application Platform развёрнуты на одной машине
    #network.host: 127.0.0.1  
    http.host: <XXX.XXX.XXX.XXX> # IP - слушать внешний интерфейс, 127.0.0.1 - localhost, 0.0.0.0 - все
    http.port: 9200 # порт по умолчанию

    # --------------------------------- Discovery ----------------------------------

    discovery.type: single-node # директива для работы в режиме одного узла
    #discovery.seed_hosts: ["192.168.12.1"] # директива для работы кластера
    #cluster.initial_master_nodes: ["192.168.12.1"] # директива для работы кластера

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
5. Повторите шаги 1–4 для каждого из узлов Elasticsearch.

### Настройка параметров JVM для Elasticsearch

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

### Обновление хранилища сертификатов Linux и Mono для сертификатов Elasticsearch

1. Добавьте сертификат CA и сертификат узла в хранилище сертификатов Mono (команды выполняются после копирования файлов в `/etc/elasticsearch/`):

    ``` sh
    sudo mono /usr/lib/mono/4.5/cert-sync.exe /etc/elasticsearch/ca.pem
    sudo mono /usr/lib/mono/4.5/cert-sync.exe /etc/elasticsearch/elastic-cert.pem
    ```

## Запуск Elasticsearch {: .pageBreakBefore }

Выполните нижеприведённые шаги для каждого узла Elasticsearch.

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
    elasticsearch.service - Elasticsearch

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
    Dec 01 10:11:12 penguin-02 systemd[1]: Starting Elasticsearch...
    Dec 01 10:12:27 penguin-02 systemd[1]: Started Elasticsearch.
    ```

    !!! note "Примечание"
        В случае ошибок с запуском процесса `elasticsearch.service` рекомендуется изучить файл журнала:

        ``` sh
        sudo less /var/elasticsearch/logs/yourClusterName.log
        ```

4. Повторите шаги, описанные в этом разделе, для каждого из узлов Elasticsearch.

### Сброс пароля пользователя `elastic`

1. При необходимости сбросьте пароль для встроенного пользователя `elastic`:

    ``` sh
    sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password -i -u elastic
    ```

2. Следуйте интерактивным подсказкам утилиты и сохраните новый пароль.

## Присвоение сертификату статуса доверенного {: .pageBreakBefore }

Перед проверкой состояния кластера необходимо присвоить новому источнику сертификата статус доверенного. Инструкции в данном разделе приведены для среды Windows 10.

1. Откройте в файловом менеджере папку с сертификатом.
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

## Проверка состояния кластера {: .pageBreakBefore }

1. После того как для каждого из узлов кластера Elasticsearch были выполнены шаги, описанные в предыдущих разделах, с любого из узлов выполните `GET`-запрос в веб-браузере:

    ``` sh
    https://192.168.XXX.XX1:9200/_cluster/health?pretty
    ```

2. Браузер отобразит форму для ввода учётных данных.
3. Введите имя встроенного суперпользователя `elastic` и один из автоматически сгенерированных паролей, которые были созданы при развёртывании Elasticsearch.

    _![Ввод учётных данных для доступа к кластеру Elasticsearch](https://kb.comindware.ru/assets/image2.png)_

4. Браузер отобразит данные `REST API` кластера Elasticsearch.
5. Убедитесь, что значение параметра `number_of_nodes` равно количеству узлов кластера.

    _![Данные REST API кластера Elasticsearch](https://kb.comindware.ru/assets/image1.png)_

## Права доступа и диагностика неполадок {: .pageBreakBefore }

1. Убедитесь, что на необходимые каталоги выданы корректные права:

    - Назначьте владельца:

        ``` sh
        sudo chown -R elasticsearch:elasticsearch /var/lib/comindware/
        ```

    - Назначьте права доступа:

        ``` sh
        sudo chmod -R 766 /var/lib/comindware/
        ```

2. В случае проблем с библиотекой `jna-5.10.0.jar` или других ошибок работы Elasticsearch изучите журналы:

    ``` sh
    journalctl -xe
    tail -f /var/log/comindware/instanceName/Logs/audit_0000-00-00.log
    nano /var/log/comindware/instanceName/Logs/audit_0000-00-00.log
    cat /var/elasticsearch/logs/elasticsearch.example.cbap.log
    ```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
