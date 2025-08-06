---
title: Apache Kafka. Установка в базовой конфигурации
kbId: 5074
---

# Apache Kafka. Установка в базовой конфигурации

## Введение

Для работы **{{ productName }}** требуется сервер Apache Kafka. См. [системные требования][system_requirements].

Здесь представлены инструкции по установке Kafka в простейшей базовой конфигурации с помощью дистрибутива **{{ productName }}** для ОС Linux.

Инструкции по установке Kafka в иных конфигурациях представлены на *[официальном сайте Apache Kafka](https://kafka.apache.org/quickstart)*.

С помощью дистрибутива **{{ productName }}** можно развернуть сервер Kafka вместе с экземпляром ПО или на отдельном сервере. Для этого укажите ключ `-k` при запуске скрипта `prerequisites_install.sh`. См. *«[Установка, запуск, инициализация и остановка ПО {{ productName }}][deploy_guide_linux]»*.

Здесь представлены требования к техническому обеспечению и инструкции по развёртыванию сервера Kafka в ОС Linux, а также приведён пример типового файла конфигурации. Инструкции представлены для версии Kafka 3.2.0, для других версий содержимое файлов конфигурации и порядок установки могут быть иными.

## Требования к серверу

Сервер Kafka создает значительную нагрузку на вычислительные ресурсы компьютера, поэтому рекомендуется:

- использовать отдельный SSD-диск для хранения журналов и данных сервера Kafka;
- использовать высокопроизводительный компьютер с достаточным объемом ОЗУ и количеством ядер ЦП.

## Установка Kafka

1. Перейдите в режим суперпользователя:

   ```
   sudo -s

   ```

   или

   ```
   su -

   ```
2. Скачайте и распакуйте дистрибутив с вспомогательным ПО **{{ productName }}**, полученный по ссылке от компании **Comindware** (`X.X`, `<versionNumber>` — номер версии ПО, `<osname>` — название операционной системы):

   ```
   tar -xf X.X-release-ru-<versionNumber>.prerequisites.<osname>.tar.gz

   ```

   Совет

   После распаковки архив можно удалить для экономии места:

   ```
   rm -f X.X-release-ru-<versionNumber>.prerequisites.<osname>.tar.gz

   ```
3. Перейдите в директорию со скриптами для развёртывания вспомогательного ПО:

   ```
   cd <prerequisitesDistPath>/CMW_<osname>/scripts

   ```

   Здесь: `<prerequisitesDistPath>/CMW_<osname>/` — путь к распакованному дистрибутиву со вспомогательным ПО.
4. Установите Kafka из дистрибутива с помощью ключа `-k`:

   ```
   sh prerequisites_install.sh -k

   ```
5. Отредактируйте файл `/usr/share/kafka/config/kraft/server.properties` по следующему образцу:

   ```
   # Роли, в которых должен выступать сервер Kafka
   process.roles=broker,controller
   # Идентификатор узла
   node.id=1
   # IP-адрес сервера Kafka
   controller.quorum.voters=1@<KafkaIP>:9093
   # IP-адрес сервера Kafka
   listeners=PLAINTEXT://<KafkaIP>:9092,CONTROLLER://<KafkaIP>:9093
   # Имя слушателя для связи между брокерами
   inter.broker.listener.name=PLAINTEXT
   # Имена слушателей контроллера
   controller.listener.names=CONTROLLER
   # Карта протоколов безопасности для слушателей
   listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL
   # Количество сетевых потоков
   num.network.threads=3
   # Количество потоков ввода-вывода
   num.io.threads=8
   # Размер буфера отправки сокета
   socket.send.buffer.bytes=102400
   # Размер буфера приёма сокета
   socket.receive.buffer.bytes=102400
   # Максимальный размер запроса
   socket.request.max.bytes=104857600
   # Путь к файлам журналов
   log.dirs=/var/log/comindware/.kafka
   # Количество разделов (партиций) по умолчанию
   num.partitions=4
   # Количество потоков восстановления на каталог данных
   num.recovery.threads.per.data.dir=1
   # Фактор репликации темы смещений
   offsets.topic.replication.factor=1
   # Фактор репликации журнала состояния транзакций
   transaction.state.log.replication.factor=1
   # Минимальное количество ISR для журнала состояния транзакций
   transaction.state.log.min.isr=1
   # Время хранения журналов (в часах)
   log.retention.hours=168
   # Размер сегмента журнала
   log.segment.bytes=1073741824
   # Интервал проверки хранения журналов (в миллисекундах)
   log.retention.check.interval.ms=300000
   # Максимальный размер запроса
   max.request.size=104857600
   # Максимальный размер сообщения
   max.message.bytes=104857600
   # Максимальный размер сообщения
   message.max.bytes=104857600
   # Максимальный размер сообщения для выборки
   fetch.message.max.bytes=104857600
   # Максимальный размер сообщения для выборки реплики
   replica.fetch.max.bytes=104857600

   ```
6. После установки удостоверьтесь, что служба Kafka запущена и имеет статус `Active (running)`:

   ```
   systemctl status kafka

   ```
7. Если сервер Kafka не работает, запустите его:

   ```
   systemctl start kafka

   ```

## Подключение экземпляра {{ productName }} к Kafka

1. Перейдите в режим суперпользователя:

   ```
   sudo -s

   ```

   или

   ```
   su -

   ```
2. Задайте параметры подключения к Kafka в файле `/usr/share/comindware/configs/instance/<instanceName>.yml` (`<instanceName>` — имя экземпляра ПО {{ productName }}):

   ```
   # Адрес и порт сервера очереди сообщений (Kafka)
   mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
   # Идентификатор группы очереди сообщений
   mq.group: <instanceName>
   # Идентификатор узла очереди сообщений
   #mq.node: <instanceName>

   ```

   Внимание!

   Для корректной работы экземпляра ПО необходимо соблюсти следующие условия:

   - IP-адрес и порт {{ apacheKafkaVariants }} должны быть обязательно прописаны цифрами в формате `XXX.XXX.XXX.XXX:XXXXX`. То есть недопустимо указывать имя хоста вместо IP-адреса и опускать номер порта.
   - Установите соответствующие вашей конфигурации значения параметров `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений). Они должны совпадать во всех файлах конфигурации:

     - `/usr/share/comindware/configs/instance/<instanceName>.yml`
     - `/var/www/<instanceName>/apigateway.yml`
     - `/var/www/<instanceName>/adapterhost.yml`
3. Задайте параметры подключения к Kafka в файле `/var/www/<instanceName>apigateway.yml`:

   ```
   # Адрес и порт сервера очереди сообщений (Kafka)
   mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>
   # Идентификатор группы очереди сообщений
   mq.group: <instanceName>
   # Идентификатор узла очереди сообщений
   mq.node: <instanceName>

   ```
4. Задайте параметры подключения к Kafka в файле `/var/www/<instanceName>/adapterhost.yml`:

   ```
   # Адрес и порт сервера очереди сообщений (Kafka)
   mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>

   ```
5. Перезапустите экземпляр ПО:

   ```
   systemctl restart comindware<instanceName>
   systemctl restart apigateway<instanceName>
   systemctl restart adapterhost<instanceName>

   ```
6. Проверьте соединение с Kafka в браузере по ссылке (`<instanceAddress>` — URL экземпляра ПО):

   ```
   <instanceAddress>/async

   ```

## Дополнительные рекомендации

### Настройка безопасности

Для повышения безопасности рекомендуется настроить SSL/TLS для шифрования данных и аутентификацию с использованием SASL. Подробные инструкции см. в официальной документации Apache Kafka (на английском языке): <https://kafka.apache.org/documentation/#security>.

### Мониторинг и управление

Для мониторинга и управления сервером Kafka рекомендуется использовать инструменты, такие как Prometheus и Grafana. Подробные инструкции по настройке мониторинга см. в официальной документации Apache Kafka (на английском языке): <https://kafka.apache.org/documentation/#monitoring>.

--8<-- "related_topics_heading.md"

- [Настройка конфигурации вспомогательного ПО для оптимизации работы {{ productName }}][auxiliary_software_optimize]
- [Конфигурация экземпляра, компонентов ПО и служб. Настройка][configuration_files_linux]
- [Пути и содержимое директорий экземпляра ПО][paths_windows]

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
