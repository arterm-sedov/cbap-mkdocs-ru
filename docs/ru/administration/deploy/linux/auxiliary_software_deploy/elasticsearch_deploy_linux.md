---
title: Elasticsearch. Установка в базовой конфигурации
kbId: 4601
---

# Elasticsearch. Установка в базовой конфигурации {: #elasticsearch_deploy_Linux}

## Введение

Для работы **{{ productName }}** требуется сервер Elasticsearch. См. [системные требования][system_requirements].

Здесь представлены инструкции по установке Elasticsearch с помощью дистрибутива **{{ productName }}** в простейшей базовой конфигурации.

Инструкции по установке Elasticsearch в иных конфигурациях:

- _[Официальный сайт Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/targz.html)_ (английский язык)
- _[Установка и настройка Elasticsearch без сертификатов подлинности][elasticsearch_cluster_deploy_no_certificates]_

С помощью дистрибутива **{{ productName }}** можно развернуть сервер Elasticsearch вместе с экземпляром ПО или на отдельном сервере. Для этого укажите ключ `-e` при запуске скрипта `prerequisites_install.sh`. См. _«[Установка, запуск, инициализация и остановка ПО {{ productName }}][deploy_guide_linux]»_.

Установленная таким образом сервер Elasticsearch имеет базовую конфигурацию: без аутентификации и с одним узлом. Он доступна по адресу `localhost:9200`.

Здесь представлены требования к техническому обеспечению и инструкции по развёртыванию сервера Elasticsearch в ОС Linux, а также приведён пример типового файла конфигурации. Инструкции представлены для версии Elasticsearch 8.10.2, для других версий содержимое файлов конфигурации и порядок установки могут быть иными.

{%
include-markdown ".snippets/elasticsearch_opensearch_configure.md"
rewrite-relative-urls=false
%}

## Требования к серверу {: .pageBreakBefore }

Elasticsearch создает значительную нагрузку на вычислительные ресурсы компьютера, поэтому рекомендуется:

- использовать отдельный SSD-диск для хранения журналов и данных сервера Elasticsearch;
- осуществлять мониторинг свободного места на диске, так как сервер перестает записывать данные, если на диске мало свободного места;
- использовать высокопроизводительный компьютер с достаточным объемом ОЗУ и количеством ядер ЦП, так как для обработки каждого индекса создается отдельный поток, а индексов может быть много.

## Установка Elasticsearch {: .pageBreakBefore }

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Скачайте и распакуйте дистрибутив с вспомогательным ПО **{{ productName }}**, полученный по ссылке от компании **{{ companyName }}** (`X.X`, `<versionNumber>` — номер версии ПО, `<osname>` — название операционной системы):

    ``` sh
    tar -xf X.X-release-ru-<versionNumber>.prerequisites.<osname>.tar.gz
    ```

    !!! tip "Совет"

        После распаковки архив можно удалить для экономии места:

        ``` sh
        rm -f X.X-release-ru-<versionNumber>.prerequisites.<osname>.tar.gz
        ```

3. Перейдите в директорию со скриптами для развёртывания вспомогательного ПО:

    ``` sh
    cd <prerequisitesDistPath>/CMW_<osname>/scripts
    ```

    Здесь:  `<prerequisitesDistPath>/CMW_<osname>/` — путь к распакованному дистрибутиву со вспомогательным ПО.

4. Установите Elasticsearch из дистрибутива с помощью ключа `-e`:

    ``` sh
    sh prerequisites_install.sh -e
    ```

5. После установки удостоверьтесь, что сервер Elasticsearch запущен и имеет статус `Active (running)`:

    ``` sh
    systemctl status elasticsearch
    ```

6. Если сервер Elasticsearch не работает, запустите его:

    ``` sh
    systemctl start elasticsearch
    ```

## Пример типового файла конфигурации Elasticsearch {: .pageBreakBefore }

Ниже приведен пример файла `elasticsearch.yml` для следующей конфигурации сервера:

- сервер Elasticsearch состоит из единственного узла;
- сервер работает в локальной сети;
- отключена аутентификация;
- сервер доступна через порт `9200`;
- адрес сервера `http://<opesearchIP>:9200`;
- путь к файлу конфигурации: `/etc/elasticsearch/elasticsearch.yml`

``` {: .sh .pageBreakAfter title="Пример типового файла конфигурации Elasticsearch" }
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
# {{ productName }} развёрнуты на одной машине
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
{% if pdfOutput %}
```

``` sh title="Пример типового файла конфигурации Elasticsearch — продолжение"
{% endif %}
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

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Официальный сайт Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/targz.html)_ (английский язык)
- _[Установка и настройка Elasticsearch без сертификатов подлинности][elasticsearch_cluster_deploy_no_certificates]_
- _[Установка, запуск, инициализация и остановка ПО {{ productName }}][deploy_guide_linux]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
