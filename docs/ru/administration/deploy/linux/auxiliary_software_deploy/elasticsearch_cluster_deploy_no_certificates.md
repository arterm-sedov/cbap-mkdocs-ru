---
title: Развёртывание Elasticsearch без сертификатов подлинности
kbId: 4612
---

# Развёртывание Elasticsearch без сертификатов подлинности {: #elasticsearch_cluster_deploy_no_certificates}

## Введение

Для работы ПО **{{ productName }}** требуется сервер Elasticsearch версии не ниже 8.10.2.

Здесь представлены требования к конфигурации компьютеров, инструкции по установке Elasticsearch, и настройке узлов кластера Elasticsearch без проверки сертификатов подлинности на виртуальных машинах с ОС Linux на базе Debian.

Только после запуска службы Elasticsearch можно приступать к развертыванию **{{ productName }}**, указав путь к серверу Elasticsearch.

## Подготовка физических и виртуальных машин, пакетов программ

Установка в минимальной конфигурации выполняется на 3 разделённых виртуальных машинах.

Для полнофункциональной отказоустойчивой системы требуется установка на 4 виртуальных машинах, расположенных на как минимум 3 физических машинах (IP-адреса приведены ниже исключительно для примера).

### Пример конфигурации серверов

- `masterdatanode1` c IP-адресом `1.1.1.1` и ролями `data`, `master`, `ingest`.
- ОЗУ не менее 8 ГБ, 4 ядра, SSD не менее 30 ГБ.
- `datanode2` c IP-адресом `1.1.1.2` и ролями `data`, `ingest`.
- ОЗУ не менее 8 ГБ, 4 ядра, SSD не менее 30 ГБ.
- `masternode3` c IP-адресом `1.1.1.3` и ролью `master`.
- ОЗУ не менее 4 ГБ, 4 ядра, SSD не менее 30 ГБ.
- `masternode4` c IP-адресом `1.1.1.4` и ролью master типа `voting_only`.
- ОЗУ не менее 4 ГБ, 4 ядра, SSD не менее 30 ГБ.

Серверы `masterdatanode1` и `datanode2` необходимо разместить на разных физических машинах.

На все машины в папку `/home/username` необходимо загрузить:

- `deb`-пакет `elasticsearch-8.5.1-amd64.deb`
- `yml`-файл конфигурации для Elasticsearch `customElasticConfig.yml`

## Установка Elasticsearch из deb-пакета

Повторите шаги, описанные в этом разделе, для каждого из узлов Elasticsearch.

1. Обновите ПО на сервере:

    ``` sh
    sudo apt update && sudo apt upgrade -y && sudo reboot
    ```

    В процессе обновления сервер перезагрузится.

2. Перейдите в папку пользователя:

    ``` sh
    cd /home/username/
    ```

3. Запустите процесс установки Elasticsearch:

    ``` sh
    sudo dpkg --install elasticsearch-8.5.1-amd64.deb
    ```

    По окончании установки машина выдаст отчёт:

    ``` sh
    Setting up elasticsearch (8.10.2) ...
    ---------------------------
    Security autoconfiguration information
    Authentication and authorization are enabled.
    TLS for the transport and HTTP layers is enabled and configured.
    The generated password for the elastic built-in superuser is : wfcEcSTqfyttNCNdpQgv
    If this node should join an existing cluster, you can reconfigure this with
    '/usr/share/elasticsearch/bin/elasticsearch-reconfigure-node --enrollment-token <token-here>'
    after creating an enrollment token on your existing cluster.
    You can complete the following actions at any time:
    Reset the password of the elastic built-in superuser with
    '/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic'.
    Generate an enrollment token for Kibana instances with
    '/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana'.
    Generate an enrollment token for Elasticsearch nodes with
    '/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node'.
    ---------------------------------------------------------------------
    ```

4. Обратите внимание на строку `The generated password for the elastic built-in superuser is` — напротив неё будет выведен автоматически сформированный пароль для встроенного суперпользователя elastic. **Сохраните этот пароль.**

## Конфигурация Elasticsearch {: .pageBreakBefore }

Повторите шаги, описанные в этом разделе, для каждого из узлов Elasticsearch.

Помните, что имя кластера `cluster.name` для каждого из узлов должно совпадать, а имя узла `node.name` должно быть уникальным.

1. Создайте папки, в которые Elasticsearch будет сохранять данные журналов, индексов и резервных копий:

    ``` sh
    sudo mkdir /var/elasticsearch
    sudo mkdir /var/elasticsearch/data
    sudo mkdir /var/elasticsearch/logs
    sudo mkdir /var/elasticsearch/backups
    ```

2. Измените владельца папки и права доступа к ней:

    ``` sh
    sudo chown elasticsearch:elasticsearch --recursive /var/elasticsearch/
    sudo chmod  764 --recursive /var/elasticsearch/
    ```

3. Создайте папку для хранения резервной копии `yml`-файла конфигурации Elasticsearch:

    ``` sh
    sudo mkdir /etc/elasticsearch/backupConfig
    ```

4. Переместите `yml`-файл конфигурации Elasticsearch в папку `/etc/elasticsearch/backupConfig`:

    ``` sh
    sudo mv /etc/elasticsearch/elasticsearch.yml /etc/elasticsearch/backupConfig
    ```

5. Создайте новый  `yml`-файл конфигурации Elasticsearch `elasticsearch.yml`:

    ``` sh
    sudo nano /etc/elasticsearch/elasticsearch.yml
    ```

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

6. Скопируйте в созданный файл конфигурации следующее содержимое:

    ``` yaml
    bootstrap.memory_lock: false
    cluster.name: elasticsearch.example.cbap
    cluster.max_shards_per_node: 10000
    http.port: 9200
    node.roles: [ master, data, ingest, remote_cluster_client ]
    node.name: elasticsearch1
    path.data: /var/elasticsearch/data
    path.logs: /var/elasticsearch/logs
    path.repo: /var/elasticsearch/backups
    xpack.security.enabled: false
    xpack.security.http.ssl:
      enabled: false
    #  keystore.path: certs/es1.p12    # [<-] specify path to signedNodeCert.p12 here
    xpack.security.transport.ssl:
      enabled: false
    #  key: certs/es1.key    # [<-] specify path to nodecert.key here
    #  certificate: certs/es1.crt    # [<-] specify path to nodeCert.crt here
    #  certificate_authorities: [ "certs/CMW-RootCA.crt" ]    # [<-] specify path to CACert.crt here
    network.host: 192.168.1.43
    discovery.seed_hosts : ["192.168.1.43", "192.168.1.42","1.1.1.3"]
    cluster.initial_master_nodes:
      - elasticsearch1
      - elasticsearch2
      - elasticsearch3
    #Этот флаг требуется для записи данных в индексы
    indices.id_field_data.enabled: true
    ```

6. Сохраните изменения `yml`-файла конфигурации закройте текстовый редактор Nano, нажав клавиши: ++ctrl+O++, ++enter++, ++ctrl+x++.
7. Измените для `yml`-файла конфигурации Elasticsearch владельца и права доступа:

    ``` sh
    sudo chown elasticsearch:elasticsearch --recursive /etc/elasticsearch/elasticsearch.yml
    sudo chmod 764 --recursive /etc/elasticsearch/elasticsearch.yml
    ```

8. Откройте в текстовом редакторе Nano `yml`-файл конфигурации Elasticsearch:

    ``` sh
    sudo nano /etc/elasticsearch/elasticsearch.yml
    ```

9. Задайте имя кластера с помощью директивы `cluster.name` в строке 2 `yml`-файла конфигурации: 

    ``` sh
    cluster.name: elasticsearch.example.cbap
    ```

    !!! note "Примечание"
        Имя кластера должно быть одинаковым для всех узлов кластера Elasticsearch.

10. Задайте имя узла с помощью директивы `node.name` в строке 11 `yml`-файла конфигурации. 

    !!! note "Примечание"
        Имя узла должно быть уникальным для каждого из узлов кластера Elasticsearch:

    ``` sh
    node.name: elasticsearch1
    ```

11. Укажите путь до директории, в которую настраиваемый узел Elasticsearch будет сохранять файлы данных шардов, отредактировав строку 13:

    ``` sh
    path.data: /var/elasticsearch/data
    ```

12. Укажите путь до директории, в которую настраиваемый узел Elasticsearch будет сохранять файлы логов, отредактировав строку 14:

    ``` sh
    path.logs: /var/elasticsearch/logs
    ```

13. Укажите путь до директории, в которую настраиваемый узел Elasticsearch будет сохранять файлы резервного копирования, отредактировав строку 15:

    ``` sh
    path.repo: /var/elasticsearch/backups
    ```

14. Укажите уникальный IP-адрес (как пример - 192.168.ХХХ.1) машины настраиваемого узла Elasticsearch, отредактировав строку 29:

    ``` sh
    network.host: 192.168.XXX.1
    ```

15. Задайте список IP-адресов машин (как пример - 192.168.XXX.1, 192.168.XXX.2, 192.168.XXX.3), на которых будут расположены узлы кластера Elasticsearch, отредактировав строку 31. Например, для кластера из трех узлов, директива будет вот такой:

    ``` sh
    discovery.seed_hosts : ["192.168.XXX.1", "192.168.XXX.2","192.168.XXX.3"]
    ```

16. Сохраните изменения `yml`-файла конфигурации и закройте текстовый редактор Nano, нажав клавиши: ++ctrl+O++, ++enter++, ++ctrl+x++.

## Запуск Elasticsearch {: .pageBreakBefore }

Повторите шаги, описанные в этом разделе, для каждого из узлов Elasticsearch.

1. Перезагрузите конфигурацию `systemd`:

    ``` sh
    sudo systemctl daemon-reload
    ```

2. Добавьте процесс `elasticsearch.service` в список автозагрузки при запуске ОС и запустите его:

    ``` sh
    sudo systemctl enable --now elasticsearch.service
    ```

3. Убедитесь, что процесс `elasticsearch.service` запустился:

    ``` sh
    sudo systemctl status elasticsearch.service
    ```

    ``` sh title="Пример результата проверки статуса процесса elasticsearch.service"
    elasticsearch.service - Elasticsearch
      Loaded: loaded (/lib/systemd/system/elasticsearch.service; enabled; vendor preset: enabled)
      Active: active (running) since Thu 2022-12-01 10:12:27 UTC; 6s ago
        Docs: <<https://www.elastic.co>>
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
        В случае возникновения ошибок при запуске процесса `elasticsearch.service` рекомендуется изучить файл журнала:

    ``` sh
    sudo less /var/elasticsearch/logs/yourClusterName.log
    ```

4. С помощью curl убедитесь, что REST API узла Elasticsearch доступен:

    ``` sh
    sudo curl <http://192.168.XXX.XX>Х:9200
    ```

    Пример ответа на запрос:
    {: .pageBreakBefore }

    ``` json
    {
    "name" : "elasticsearch1",
    "cluster_name" : "yourClusterName",
    "cluster_uuid" : "Xfj14lWBRf2c6GAuwtV5lg",
    "version" : {
        "number" : "8.5.1",
        "build_flavor" : "default",
        "build_type" : "deb",
        "build_hash" : "c1310c45fc534583afe2c1c03046491efba2bba2",
        "build_date" : "2022-11-09T21:02:20.169855900Z",
        "build_snapshot" : false,
        "lucene_version" : "9.4.1",
        "minimum_wire_compatibility_version" : "7.17.0",
        "minimum_index_compatibility_version" : "7.0.0"
        },
    "tagline" : "You Know, for Search"
    }
    ```
    {% include-markdown ".snippets/pdfEndOfBlockHack.md" %}

## Проверка состояния кластера

1. Выполнив для каждого из узлов кластера Elasticsearch шаги, описанные в предыдущих разделах, от любого из узлов выполните GET-запрос проверки состояния кластера:

    ``` sh
    sudo curl <http://192.168.XXX.XX1:9200/_cluster/health?pretty>>
    ```

2. Убедитесь, что в ответе на запрос значение параметра `number_of_nodes` равно количеству узлов кластера:

    ``` json
    {
    "cluster_name" : "yourClusterName",
    "status" : "green",
    "timed_out" : false,
    "number_of_nodes" : 2,
    "number_of_data_nodes" : 2,
    "active_primary_shards" : 1,
    "active_shards" : 2,
    "relocating_shards" : 0,
    "initializing_shards" : 0,
    "unassigned_shards" : 0,
    "delayed_unassigned_shards" : 0,
    "number_of_pending_tasks" : 0,
    "number_of_in_flight_fetch" : 0,
    "task_max_waiting_in_queue_millis" : 0,
    "active_shards_percent_as_number" : 100.0
    }
    ```

## Пример yml-файла конфигурации узла Elasticsearch {: .pageBreakBefore }

``` yaml
bootstrap.memory_lock: false
cluster.name: elasticsearch.example.cbap
cluster.max_shards_per_node: 10000
http.port: 9200
node.roles: [ master, data, ingest, remote_cluster_client ]
node.name: elasticsearch1
path.data: /var/elasticsearch/data
path.logs: /var/elasticsearch/logs
path.repo: /var/elasticsearch/backups
xpack.security.enabled: false
xpack.security.http.ssl:
  enabled: false
#  keystore.path: certs/es1.p12    # [<-] specify path to signedNodeCert.p12 here
xpack.security.transport.ssl:
  enabled: false
#  key: certs/es1.key    # [<-] specify path to nodecert.key here
#  certificate: certs/es1.crt    # [<-] specify path to nodeCert.crt here
#  certificate_authorities: [ "certs/CMW-RootCA.crt" ]    # [<-] specify path to CACert.crt here
network.host: 192.168.1.43
discovery.seed_hosts : ["192.168.1.43", "192.168.1.42","1.1.1.3"]
cluster.initial_master_nodes:
  - elasticsearch1
  - elasticsearch2
  - elasticsearch3
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
