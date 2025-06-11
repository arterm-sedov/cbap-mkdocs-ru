---
title: Apache Kafka. Установка в базовой конфигурации
kbId: 5074
---

# Apache Kafka. Установка в базовой конфигурации {: #kafka_deploy_linux}

## Введение

Для работы **{{ productName }}** требуется сервер Apache Kafka. См. [системные требования][system_requirements].

Здесь представлены инструкции по установке Kafka в простейшей базовой конфигурации с помощью дистрибутива **{{ productName }}** для ОС Linux.

Инструкции по установке Kafka в иных конфигурациях представлены на _[официальном сайте Apache Kafka](https://kafka.apache.org/quickstart)_.

С помощью дистрибутива **{{ productName }}** можно развернуть сервер Kafka вместе с экземпляром ПО или на отдельном сервере. Для этого укажите ключ `-k` при запуске скрипта `prerequisites_install.sh`. См. _«[Установка, запуск, инициализация и остановка ПО {{ productName }}][deploy_guide_linux]»_.

Здесь представлены требования к техническому обеспечению и инструкции по развёртыванию сервера Kafka в ОС Linux, а также приведён пример типового файла конфигурации. Инструкции представлены для версии Kafka 3.2.0, для других версий содержимое файлов конфигурации и порядок установки могут быть иными.

## Требования к серверу

Сервер Kafka создает значительную нагрузку на вычислительные ресурсы компьютера, поэтому рекомендуется:

- использовать отдельный SSD-диск для хранения журналов и данных сервера Kafka;
- использовать высокопроизводительный компьютер с достаточным объемом ОЗУ и количеством ядер ЦП.

## Установка Kafka

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

4. Установите Kafka из дистрибутива с помощью ключа `-k`:

    ``` sh
    sh prerequisites_install.sh -k
    ```

5. Отредактируйте файл `/usr/share/kafka/config/kraft/server.properties` по следующему образцу:

    --8<-- "kafka_deploy_config_start.md"
    # Путь к файлам журналов
    log.dirs=/var/log/comindware/.kafka
    --8<-- "kafka_deploy_config_end.md"

6. После установки удостоверьтесь, что служба Kafka запущена и имеет статус `Active (running)`:

    ``` sh
    systemctl status kafka
    ```

7. Если сервер Kafka не работает, запустите его:

    ``` sh
    systemctl start kafka
    ```

## Подключение экземпляра {{ productName }} к Kafka

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Задайте параметры подключения к Kafka в файле `/usr/share/comindware/configs/instance/<instanceName>.yml` (`<instanceName>` — имя экземпляра ПО {{ productName }}):

    ``` yaml
    # Адрес и порт сервера очереди сообщений (Kafka)
    mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
    # Идентификатор группы очереди сообщений
    mq.group: <instanceName>
    # Идентификатор узла очереди сообщений
    #mq.node: <instanceName>
    ```

    !!! warning "Внимание!"

        --8<-- "kafka_deploy_config_warning.md"

            - `/usr/share/comindware/configs/instance/<instanceName>.yml`
            - `/var/www/<instanceName>/apigateway.yml`
            - `/var/www/<instanceName>/adapterhost.yml`

3. Задайте параметры подключения к Kafka в файле `/var/www/<instanceName>apigateway.yml`:

    ``` yaml
    # Адрес и порт сервера очереди сообщений (Kafka)
    mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>
    # Идентификатор группы очереди сообщений
    mq.group: <instanceName>
    # Идентификатор узла очереди сообщений
    mq.node: <instanceName>
    ```

4. Задайте параметры подключения к Kafka в файле `/var/www/<instanceName>/adapterhost.yml`:

    ``` yaml
    # Адрес и порт сервера очереди сообщений (Kafka)
    mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>
    ```

5. Перезапустите экземпляр ПО:

    ``` sh
    systemctl restart comindware<instanceName>
    systemctl restart apigateway<instanceName>
    systemctl restart adapterhost<instanceName>
    ```

6. Проверьте соединение с Kafka в браузере по ссылке (`<instanceAddress>` — URL экземпляра ПО):

    ``` powershell
    <instanceAddress>/async
    ```

<!--additional-recommendations-start-->
## Дополнительные рекомендации

### Настройка безопасности

Для повышения безопасности рекомендуется настроить SSL/TLS для шифрования данных и аутентификацию с использованием SASL. Подробные инструкции см. в официальной документации Apache Kafka (на английском языке): <https://kafka.apache.org/documentation/#security>.

### Мониторинг и управление

Для мониторинга и управления сервером Kafka рекомендуется использовать инструменты, такие как Prometheus и Grafana. Подробные инструкции по настройке мониторинга см. в официальной документации Apache Kafka (на английском языке): <https://kafka.apache.org/documentation/#monitoring>.
<!--additional-recommendations-end-->

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Настройка конфигурации вспомогательного ПО для оптимизации работы {{ productName }}][auxiliary_software_optimize]_
- _[Конфигурация экземпляра, компонентов ПО и служб. Настройка][configuration_files_linux]_
- _[Пути и содержимое директорий экземпляра ПО][paths_windows]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
