---
title: 'Elasticsearch. Установка в базовой конфигурации'
kbId: 2650
url: 'https://kb.comindware.ru/article.php?id=2650'
updated: '2024-11-07 19:06:51'
---

# Elasticsearch. Установка в базовой конфигурации

## Введение

Для работы **Comindware Business Application Platform** требуется сервер Elasticsearch. См. [системные требования](https://kb.comindware.ru/article.php?id=1271).

Здесь представлены инструкции по установке Elasticsearch с помощью дистрибутива **Comindware Business Application Platform** в простейшей базовой конфигурации.

Инструкции по установке Elasticsearch в иных конфигурациях:

- *[Официальный сайт Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/targz.html)* (английский язык)
- *[Установка Elasticsearch и настройка кластера Elasticsearch без сертификатов подлинности](https://kb.comindware.ru/article.php?id=2095)*

С помощью дистрибутива **Comindware Business Application Platform** можно развернуть сервер Elasticsearch вместе с экземпляром ПО или на отдельном сервере. Для этого укажите ключ `-e` при запуске скрипта `install.sh`. См. *«[Установка, запуск, инициализация и остановка ПО Comindware Business Application Platform](https://kb.comindware.ru/article.php?id=2344)»*.

Установленная таким образом сервер Elasticsearch имеет базовую конфигурацию: без аутентификации и с одним узлом. Он доступна по адресу `localhost:9200`.

Здесь представлены требования к техническому обеспечению и инструкции по развёртыванию сервера Elasticsearch в ОС Linux, а также приведён пример типового файла конфигурации. Инструкции представлены для версии Elasticsearch 8.10.2, для других версий содержимое файлов конфигурации и порядок установки могут быть иными.

## Требования к серверу

Elasticsearch создает значительную нагрузку на вычислительные ресурсы компьютера, поэтому рекомендуется:

- использовать отдельный SSD-диск для хранения журналов и данных сервера Elasticsearch;
- осуществлять мониторинг свободного места на диске, так как сервер перестает записывать данные, если на диске мало свободного места;
- использовать высокопроизводительный компьютер с достаточным объемом ОЗУ и количеством ядер ЦП, так как для обработки каждого индекса создается отдельный поток, а индексов может быть много.

## Установка Elasticsearch

1. Перейдите в режим суперпользователя:

   ```
   sudo -i
   ```

   или

   ```
   su -
   ```
2. Скачайте и распакуйте дистрибутив **Comindware Business Application Platform** по ссылке, предоставленной компанией **Comindware** (`X.X.XXXX.X` — номер версии ПО, `<osname>` — название операционной системы):

   ```
   tar -xf X.X-release-ru-X.X.XXXX.X.<osname>.tar.gz
   ```
3. Перейдите в распакованную директорию:

   ```
   cd CMW_<osname>/
   ```
4. Установите Elasticsearch из дистрибутива с помощью ключа `-e`:

   ```
   sh install.sh -e
   ```
5. После установки удостоверьтесь, что сервер Elasticsearch запущен и имеет статус `Active (running)`:

   ```
   systemctl status elasticsearch
   ```
6. Если сервер Elasticsearch не работает, запустите его:

   ```
   systemctl start elasticsearch
   ```

## Пример типового файла конфигурации Elasticsearch

Ниже приведен пример файла `elasticsearch.yml` для следующей конфигурации сервера:

- сервер Elasticsearch состоит из единственного узла;
- сервер работает в локальной сети;
- отключена аутентификация;
- сервер доступна через порт `9200`;
- адрес сервера `http://localhost:9200`;
- путь к файлу конфигурации: `/etc/elasticsearch/elasticsearch.yml`

```
#======================== Elasticsearch Configuration =========================
# Имя кластера
cluster.name: my-application
# ------------------------------------ Node ------------------------------------
# Имя узла
node.name: node-1
# ----------------------------------- Paths ------------------------------------
# Путь к директории с данными
path.data: /var/lib/elasticsearch
# Путь к файлам журнала Elasticsearch
path.logs: /var/log/elasticsearch
# path.repo: /var/backups/elasticsearch # путь к репозиторию резервных копий Elasticsearch
# ----------------------------------- Memory -----------------------------------
# Разрешите свопинг памяти
bootstrap.memory_lock: false
# ---------------------------------- Network -----------------------------------
# Укажите IP сервера Elasticsearch или 127.0.0.1, если Elasticsearch и
# Comindware Business Application Platform развёрнуты на одной машине
network.host: 127.0.0.1
http.port: 9200 # порт по умолчанию
# --------------------------------- Discovery ----------------------------------
# Директива для работы в режиме одного узла
discovery.type: single-node
# discovery.seed_hosts: ["192.168.12.1"] # Директива для режима кластера
# cluster.initial_master_nodes: ["192.168.12.1"] # Директива для режима кластера
# ---------------------------------- Various -----------------------------------
# Нечёткий поиск включён
search.allow_expensive_queries: true
# Удаление всех индексов запрещено
action.destructive_requires_name: true
# Запись данных в индексы включена
indices.id_field_data.enabled: true
# ---------------------------------- Security ----------------------------------
# Аутентификация отключена
xpack.security.enabled: false
xpack.security.enrollment.enabled: false
# Поддержка HTTPS отключена
xpack.security.http.ssl:
  enabled: false
  #  keystore.path: certs/http.p12
# TLS/SSL отключено
xpack.security.transport.ssl:
  enabled: false
  #  verification_mode: certificate
  #  keystore.path: certs/transport.p12
  #  truststore.path: certs/transport.p12
# IP - слушать внешний интерфейс, 127.0.0.1 - localhost, 0.0.0.0 - все
http.host: 0.0.0.0
```

## Связанные статьи

**[Официальный сайт Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/targz.html)** (английский язык)

**[Установка Elasticsearch и настройка кластера Elasticsearch без сертификатов подлинности](https://kb.comindware.ru/article.php?id=2095)**

**[Установка, запуск, инициализация и остановка ПО Comindware Business Application Platform](https://kb.comindware.ru/article.php?id=2344)**