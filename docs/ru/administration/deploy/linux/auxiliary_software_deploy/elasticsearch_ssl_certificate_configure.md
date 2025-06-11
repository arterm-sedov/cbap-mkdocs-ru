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

1. Перед установкой OpenSSL обновите ПО:

    ``` sh
    sudo apt update
    sudo apt upgrade
    ```

2. Установите OpenSSL:

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

3. <a id="P1_2_3"></a>Создайте ключи для СА:

    ``` sh
    sudo openssl genrsa -aes256 -out ExampleRootCA.key 4096
    ```

4. Придумайте, запишите и введите пароль для формирования ключа.
5. В результате вы получите ключ `ExampleRootCA.key` для CA.
6. Создайте сертификат СА:

    ``` sh
    sudo openssl req -x509 -new -nodes -key ExampleRootCA.key -sha256 -days 10000 -out ExampleRootCA.crt -subj '/CN=Xmpl Root CA/C=RU/ST=Moscow/O=Xmpl'
    ```

6. В результате вы получите файл `ExampleRootCA.crt` — сертификат СА.

### Формирование ключей и сертификатов для узлов кластера Elasticsearch {: .pageBreakBefore }

Для примера используется следующая схема именования сертификатов  узлов: `es1`, `es2`, `es3` и т. д.

1. <a id="P1_3_1"></a>Создайте ключ и сертификат для узла `es1`:

    ``` sh
    sudo openssl req -new -nodes -out es1.csr -newkey rsa:4096 -keyout es1.key -subj '/CN=Elasticsearch 1/C=RU/ST=Moscow/O=Xmpl/OU=Xmpl Cloud'
    ```

2. Аналогично [шагу 1.3.1](#P1_3_1) создайте сертификат для каждого узла, подставляя вместо `es1.csr` и `es1.key` соответствующие значения.
3. Для каждого из узлов создайте `ext`-файл, описывающий узел. Подставьте свои значения напротив `DNS.1`, `DNS.2` и `IP.1`.

    ``` ini
    sudo cat > es1.ext << EOF

    authorityKeyIdentifier=keyid
    basicConstraints=CA:FALSE
    keyUsage = critical, digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
    extendedKeyUsage = critical, serverAuth, clientAuth
    subjectAltName = @alt_names
    [alt_names]
    DNS.1 = yourClusterName
    DNS.2 = elasticsearch1
    IP.1 = 192.168.XXX.1
    EOF
    ```

4. <a id="P1_3_4"></a>Для узла `es1` создайте подписанный СА сертификат и сохраните его в файл `es1.crt`:

    ``` sh
    sudo openssl x509 -req -in es1.csr -CA ExampleRootCA.crt -CAkey ExampleRootCA.key -CAcreateserial -out es1.crt -days 10000 -sha256 -extfile es1.ext

    Enter pass phrase for ExampleRootCA.key: ВВЕДИТЕ ПАРОЛЬ
    ```

5. Используйте придуманный на [шаге 1.2.3](#P1_2_3) пароль.
6. Аналогично [шагу 1.3.4](#P1_3_4) создайте подписанные сертификаты для остальных узлов.
7. <a id="P1_3_7"></a>Для узла `es1` создайте p12-пакет с ключом, сертификатом и сертификатом СА:

    ``` sh
    sudo openssl pkcs12 -export -certfile ExampleRootCA.crt -in es1.crt -inkey es1.key -out es1.p12

    Enter Export Password: ВВЕДИТЕ ПАРОЛЬ

    Verifying - Enter Export Password: ВВЕДИТЕ ПАРОЛЬ
    ```

8. Используйте придуманный на [шаге 1.2.3](#P1_2_3) пароль.
9. Аналогично [шагу 1.3.7](#P1_3_7) создайте `p12`-пакеты для остальных узлов.

### Отправка созданных сертификатов на узлы кластера {: .pageBreakBefore }

1. Отправьте созданные сертификаты с помощью `SSH` (подставьте свои имена файлов, имя пользователя и IP-адрес):

    ``` sh
    sudo scp es2.crt username@192.168.0.1:/home/username/
    sudo scp es2.key username@192.168.0.1:/home/username/
    sudo scp es2.p12 username@192.168.0.1:/home/username/
    ```

2. В каждом из узлов перенесите сгенерированные файлы (подставьте фактическое имя файла вместо `esX`)  в папку `/etc/elasticsearch/certs`:

    ``` sh
    sudo mv /home/username/esX.* /etc/elasticsearch/certs
    ```

3. Измените пользователя для директории и настройте права доступа:

    ``` sh
    sudo chown elasticsearch:elasticsearch --recursive /etc/elasticsearch/certs/
    sudo chmod 764 --recursive /etc/elasticsearch/certs/
    ```

## Настройка кластера Elasticsearch {: .pageBreakBefore }

### Добавление пароля SSL-сертификата в хранилище ключей Elasticsearch

1. Вызовите инструмент `elasticsearch-keystore` и добавьте в него пароль от сформированных сертификатов (см. [параграф 1.2.3](#P1_2_3)):

    ``` sh
    sudo /usr/share/elasticsearch/bin/elasticsearch-keystore add xpack.security.http.ssl.keystore.secure_password

    Setting xpack.security.http.ssl.keystore.secure_password already exists. Overwrite? [y/N]y

    Enter value for xpack.security.http.ssl.keystore.secure_password: ВВЕДИТЕ ПАРОЛЬ

    sudo /usr/share/elasticsearch/bin/elasticsearch-keystore add xpack.security.http.ssl.truststore.secure_password

    Enter value for xpack.security.http.ssl.truststore.secure_password: ВВЕДИТЕ ПАРОЛЬ

    sudo /usr/share/elasticsearch/bin/elasticsearch-keystore add xpack.security.transport.ssl.keystore.secure_password

    Setting xpack.security.transport.ssl.keystore.secure_password already exists. Overwrite? [y/N]y

    Enter value for xpack.security.transport.ssl.keystore.secure_password: ВВЕДИТЕ ПАРОЛЬ

    sudo /usr/share/elasticsearch/bin/elasticsearch-keystore add xpack.security.transport.ssl.truststore.secure_password

    Setting xpack.security.transport.ssl.truststore.secure_password already exists. Overwrite? [y/N]y

    Enter value for xpack.security.transport.ssl.truststore.secure_password: ВВЕДИТЕ ПАРОЛЬ
    ```

### Настройка узла кластера для работы с SSL-сертификатами {: .pageBreakBefore }

1. Для каждого узла кластера Elasticsearch отредактируйте `yml`-файл конфигурации Elasticsearch, как показано в примерах ниже. Внимательно следите за сохранением отступов. Воспользуйтесь редактором текстовым редактором Nano:

    ``` sh
    sudo nano /etc/elasticsearch/elasticsearch.yml
    ```

    Исходный файл конфигурации Elasticsearch:

    ``` yaml
    xpack.security.enabled: false
    xpack.security.http.ssl:
        enabled: false
    #   keystore.path: certs/es1.p12    # [<-] specify path to signedNodeCert.p12 here
    xpack.security.transport.ssl:
        enabled: false
    #   key: certs/es1.key    # [<-] specify path to nodecert.key here
    #   certificate: certs/es1.crt    # [<-] specify path to nodeCert.crt here
    #   certificate_authorities: [ "certs/ExampleRootCA.crt" ]    # [<-] specify path to CACert.crt here
    ```

    Пример изменённого файла конфигурации, где сертификат узла — `es1.crt`, ключ — `es1.key`, `pem`-пакет с сертификатом и ключом — `es1.p12`:

    ``` yaml
    xpack.security.enabled: true
    xpack.security.http.ssl:
        enabled: true
        keystore.path: certs/es1.p12    # [<-] specify path to signedNodeCert.p12 here
    xpack.security.transport.ssl:
        enabled: true
        key: certs/es1.key    # [<-] specify path to nodecert.key here
        certificate: certs/es1.crt    # [<-] specify path to nodeCert.crt here
        certificate_authorities: [ "certs/ExampleRootCA.crt" ]    # [<-] specify path to CACert.crt here
    ```

    Пример изменённого файла конфигурации, где сертификат узла — `es2.crt`, ключ — `es2.key`, `pem`-пакет с сертификатом и ключом — `es2.p12`:

    ``` sh
    xpack.security.enabled: true
    xpack.security.http.ssl:
        enabled: true
        keystore.path: certs/es2.p12    # [<-] specify path to signedNodeCert.p12 here
    xpack.security.transport.ssl:
        enabled: true
        key: certs/es2.key    # [<-] specify path to nodecert.key here
        certificate: certs/es2.crt    # [<-] specify path to nodeCert.crt here
        certificate_authorities: [ "certs/ExampleRootCA.crt" ]    # [<-] specify path to CACert.crt here
    ```

2. Сохраните изменения и закройте текстовый редактор Nano, нажав клавиши: ++ctrl+O++, ++enter++, ++ctrl+x++.
3. Повторите шаги 1–2 для каждого из узлов Elasticsearch.

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

## Присвоение сертификату статуса доверенного {: .pageBreakBefore }

Перед проверкой состояния кластера необходимо присвоить новому источнику сертификата статус доверенного. Инструкции в данном разделе приведены для среды Windows 10.

1. Откройте в файловом менеджере папку с сертификатом.
2. Откройте файл сертификата `CA.crt`.
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

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
