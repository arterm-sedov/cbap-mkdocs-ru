---
title: Формирование SSL-сертификатов и настройка Elasticsearch для их использования
kbId: 4606
---

# Формирование SSL-сертификатов и настройка Elasticsearch для их использования

## Введение

Для работы ПО **{{ productName }}** требуется сервер Elasticsearch версии не ниже 8.1.0.

В этой статье представлены инструкции по формированию SSL-сертификатов подлинности узлов и настройке Elasticsearch с проверкой сертификатов подлинности для Elasticsearch.

Перед выполнением нижеприведённых инструкций необходимо развернуть Elasticsearch без сертификатов подлинности.

Дальнейшие инструкции предполагают, что служба Elasticsearch развёрнута согласно инструкциям в статье «**[Установка и настройка Elasticsearch без сертификатов подлинности][elasticsearch_cluster_deploy_no_certificates]**» на виртуальных машинах с ОС Ubuntu 22.04.4 LTS.

## 1. Формирование SSL-сертификатов

### 1.1 Установка Open SSL

1.1.1 Перед установкой OpenSSL обновите ПО:

```
sudo apt update
sudo apt upgrade
```

1.1.2. Установите OpenSSL:

```
 sudo apt install openssl
```

### 1.2. Формирование сертификата СА

1.2.1. В домашней папке пользователя `username` создайте папку, в которой предстоит работать:

```
mkdir certsGen
```

1.2.2. Перейдите в папку `certsGen`:

```
cd certsGen/
```

1.2.3. Создайте ключи для СА:

```
sudo openssl genrsa -aes256 -out ExampleRootCA.key 4096
```

1.2.4. Придумайте, запишите и введите пароль для формирования ключа.

1.2.5. В результате вы получите ключ `ExampleRootCA.key` для CA.

1.2.6. Создайте сертификат СА:

```
sudo openssl req -x509 -new -nodes -key ExampleRootCA.key -sha256 -days 10000 -out ExampleRootCA.crt -subj '/CN=Xmpl Root CA/C=RU/ST=Moscow/O=Xmpl'
```

1.2.6. В результате вы получите файл `ExampleRootCA.crt` — сертификат СА.

### 1.3. Формирование ключей и сертификатов для узлов кластера Elasticsearch

Для примера используется следующая схема именования сертификатов  узлов: `es1`, `es2`, `es3` и т. д.

1.3.1. Создайте ключ и сертификат для узла `es1`:

```
sudo openssl req -new -nodes -out es1.csr -newkey rsa:4096 -keyout es1.key -subj '/CN=Elasticsearch 1/C=RU/ST=Moscow/O=Xmpl/OU=Xmpl Cloud'
```

1.3.2. Аналогично [шагу 1.3.1](#P1_3_1) создайте сертификат для каждого узла, подставляя вместо `es1.csr` и `es1.key` соответствующие значения.

1.3.3. Для каждого из узлов создайте `ext`-файл, описывающий узел. Подставьте свои значения напротив `DNS.1`, `DNS.2` и `IP.1`.

```
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

1.3.4. Для узла `es1` создайте подписанный СА сертификат и сохраните его в файл `es1.crt`:

```
sudo openssl x509 -req -in es1.csr -CA ExampleRootCA.crt -CAkey ExampleRootCA.key -CAcreateserial -out es1.crt -days 10000 -sha256 -extfile es1.ext
Enter pass phrase for ExampleRootCA.key: ВВЕДИТЕ ПАРОЛЬ
```

1.3.5. Используйте придуманный на [шаге 1.2.3](#P1_2_3) пароль.

1.3.6. Аналогично [шагу 1.3.4](#P1_3_4) создайте подписанные сертификаты для остальных узлов.

1.3.7. Для узла `es1` создайте p12-пакет с ключом, сертификатом и сертификатом СА:

```
sudo openssl pkcs12 -export -certfile ExampleRootCA.crt -in es1.crt -inkey es1.key -out es1.p12
Enter Export Password: ВВЕДИТЕ ПАРОЛЬ
Verifying - Enter Export Password: ВВЕДИТЕ ПАРОЛЬ


```

1.3.8. Используйте придуманный на [шаге 1.2.3](#P1_2_3) пароль.

1.3.9. Аналогично [шагу 1.3.7](#P1_3_7) создайте `p12`-пакеты для остальных узлов.

### 1.4. Отправка созданных сертификатов на узлы кластера.

1.4.1. Отправьте созданные сертификаты с помощью `SSH` (подставьте свои имена файлов, имя пользователя и IP-адрес):

```
sudo scp es2.crt username@192.168.0.1:/home/username/
sudo scp es2.key username@192.168.0.1:/home/username/
sudo scp es2.p12 username@192.168.0.1:/home/username/

```

1.4.2. В каждом из узлов перенесите сгенерированные файлы (подставьте фактическое имя файла вместо `esX`)  в папку `/etc/elasticsearch/certs`:

```
sudo mv /home/username/esX.* /etc/elasticsearch/certs
```

1.4.3. Измените пользователя для директории и настройте права доступа:

```
sudo chown elasticsearch:elasticsearch --recursive /etc/elasticsearch/certs/
sudo chmod 764 --recursive /etc/elasticsearch/certs/

```

## 2. Настройка кластера Elasticsearch

### 2.1. Добавление пароля SSL-сертификата в хранилище ключей Elasticsearch

2.1.1. Вызовите инструмент `elasticsearch-keystore` и добавьте в него пароль от сформированных сертификатов (см. [параграф 1.2.3](#P1_2_3)):

```
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

### 2.2. Настройка узла кластера для работы с SSL-сертификатами

2.2.1. Для каждого узла кластера Elasticsearch отредактируйте `yml`-файл конфигурации Elasticsearch, как показано в примерах ниже. Внимательно следите за сохранением отступов. Воспользуйтесь редактором текстовым редактором Nano:

```
sudo nano /etc/elasticsearch/elasticsearch.yml
```

Исходный файл конфигурации Elasticsearch:

```
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

```
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

```
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

2.2.2. Сохраните изменения и закройте текстовый редактор Nano, нажав клавиши: `Ctrl O, Ввод, Ctrl X`.

2.2.3. Повторите шаги 2.2.1–2.2.2 для каждого из узлов Elasticsearch.

## 3. Запуск Elasticsearch

Выполните нижеприведённые шаги для каждого узла Elasticsearch.

3.1. Перезагрузите конфигурацию `systemd`:

```
sudo systemctl daemon-reload
```

3.2. Перезапустите процесс `elasticsearch.service`:

```
sudo systemctl restart elasticsearch.service
```

3.3. Убедитесь, что процесс `elasticsearch.service` запустился:

```
sudo systemctl status elasticsearch.service
```

```
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

**Примечание**

В случае ошибок с запуском процесса `elasticsearch.service` рекомендуется изучить файл журнала:

```
sudo less /var/elasticsearch/logs/yourClusterName.log
```

3.4. Повторите шаги, описанные в этом разделе, для каждого из узлов Elasticsearch.

## 4. Присвоение сертификату статуса доверенного

Перед проверкой состояния кластера необходимо присвоить новому источнику сертификата статус доверенного. Инструкции в данном разделе приведены для среды Windows 10.

4.1. Откройте в файловом менеджере папку с сертификатом.

4.2. Откройте файл сертификата `CA.crt`.

4.3. В отобразившемся окне нажмите кнопку «**Установить сертификат**».

4.4. Выберите, следует ли хранить сертификат на уровне пользователя или на уровне машины.

4.5. Нажмите кнопку «**Далее**».

4.6. Выберите пункт «**Разместить все сертификаты в следующем хранилище**».

4.7. Нажмите кнопку «**Обзор**».

4.8. Выберите «**Доверенные корневые источники сертификатов**».

4.9. Нажмите кнопку «**ОК**».

4.10. Нажмите кнопку «**Далее**».

4.11 Нажмите кнопку «**Завершить**».

4.12 Если отобразится запрос, нажмите кнопку «**Да**».

## 5. Проверка состояния кластера

5.1. После того как для каждого из узлов кластера Elasticsearch были выполнены шаги, описанные в предыдущих разделах, с любого из узлов выполните `GET`-запрос в веб-браузере:

```
https://192.168.XXX.XX1:9200/_cluster/health?pretty
```

5.2. Браузер отобразит форму для ввода учётных данных.

5.3. Введите имя встроенного суперпользователя `elastic` и один из автоматически сгенерированных паролей, которые были созданы при развёртывании Elasticsearch.

_![Ввод учётных данных для доступа к кластеру Elasticsearch](https://kb.comindware.ru/assets/image2.png)_

5.4. Браузер отобразит данные `REST API` кластера Elasticsearch.

5.5. Убедитесь, что значение параметра `number_of_nodes` равно количеству узлов кластера.

_![Данные REST API кластера Elasticsearch](https://kb.comindware.ru/assets/image1.png)_

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
