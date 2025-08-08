---
title: Установка Apache Kafka в ОС Windows и подключение к Comindware Platform
kbId: 4614
---

# Установка Apache Kafka в ОС Windows и подключение к {{ productName }}

## Введение

Для обмена данными между **{{ productName }}** и внешними системами (а также для работы обсуждений) необходимо настроить подключение к брокеру сообщений Kafka.

Здесь представлена инструкция по установке Kafka в ОС Windows с использованием KRaft (без использования Zookeeper) и подключению Kafka к **{{ productName }}**.

## Предварительные условия

Должно быть установлено ПО Java и заданы следующие системные переменные:

- `JAVA_HOME` — путь к исполняемым файлам Open JDK, например `C:\\Program Files\\jdk\\jdk-<version>\\bin`
- `JAVA_HOME_DLL` — путь к DLL-файлу Open JDK, например `C:\\Program Files\\jdk\\jdk-<version>\\bin\\server\\jvm.dll`
- `Path` — короткий путь к файлам Java: `%JAVA_HOME%\\bin`

Внимание!

- При указании путей используйте фактические имена дисков вместо используемых здесь дисков `C` и `X`.
- Для корректной работы Kafka рекомендуется скачивать архив с бинарными файлами.
- Рекомендуется использовать путь минимальной длины и названия папок без пробелов, иначе некоторые команды могут не сработать.
- Рекомендуется создавать папку для журналов на отдельном диске, а не на диске где установлено ПО Kafka.

## Процесс установки

1. Скачайте последнюю версию Kafka с **[официального сайта](https://kafka.apache.org/downloads)**.
2. Распакуйте файлы архива, например в папку `C:\\kafka`
3. Создайте папку для журналов, например `X:\\kafka\\logs`.
4. Откройте файл конфигурации Kafka `C:\\kafka\\config\\kraft\\server.properties`.
5. Отредактируйте файл конфигурации, указав IP-адрес сервера Apache Kafka, папку для журналов и размеры сообщений.

   Внимание!

   В директиве `log.dirs` для указания пути к папке журналов используйте прямую косую черту `/`, а не обратную `\\`:

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
   # Bспользуйте прямую косую черту `/`, а не обратную `\\`
   log.dirs=X:/kafka/logs
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
6. Откройте *PowerShell* от имени администратора и выполните команды:

   ```
   cd "C:\\kafka\\bin\\windows\\"
   .\\kafka-storage.bat random-uuid

   ```
7. Kafka выдаст UID, например, `kNZtrWDsRvW0udJeaEahsg`
8. Используйте полученный UID в следующей команде:

   ```
   .\\kafka-storage.bat format -t kNZtrWDsRvW0udJeaEahsg -c C:\\kafka\\config\\kraft\\server.properties

   ```
9. Загрузите с **[официального сайта](https://nssm.cc/download)** архив *NSSM* и распакуйте его.
10. В папке `\\win64` найдите файл `nssm.exe` и скопируйте его в папку `C:\\kafka\\bin\\windows\\`.
11. В *PowerShell* от имени администратора выполните следующую команду:

    ```
    .\\nssm install kafka

    ```
12. Запустится программа `NSSM service installer`.

    ![Диалоговое окно NSSM service installer](/platform/v5.0/administration/deploy/windows/auxiliary_software_deploy/img/kafka_install_nssm_service_installer.png)

    Диалоговое окно NSSM service installer
13. Укажите следующие пути к файлам службы Kafka:

    - **Path**

    ```
    C:\\kafka\\bin\\windows\\kafka-server-start.bat

    ```

    - **Startup directory**

    ```
    C:\\kafka\\bin\\windows\\

    ```

    - **Arguments**

    ```
    C:\\kafka\\config\\kraft\\server.properties

    ```
14. Нажмите кнопку «**Install service**».
15. Произойдёт установка сервиса.
16. По завершении установки откройте программу *«Службы*» (*Services*) и найдите в списке `kafka`.

    ![Kafka в списке служб](/platform/v5.0/administration/deploy/windows/auxiliary_software_deploy/img/kafka_install_services.png)

    Kafka в списке служб
17. В окне свойств службы на вкладке «**Восстановление**» включите и настройте перезапуск Kafka в случае сбоев.

    ![Окно настройки службы Kafka](/platform/v5.0/administration/deploy/windows/auxiliary_software_deploy/img/kafka_install_kafka_service.png)

    Окно настройки службы Kafka
18. Протестируйте работу Kafka, выполнив в *PowerShell* следующие команды:

    ```
    cd "C:\\kafka\\bin\\windows\\"
    .\\kafka-console-producer.bat --bootstrap-server <KafkaIP>:9092 --topic TEST
    # Отправьте любое сообщение, например:
    hello

    ```
19. При правильной работе Kafka выдаст предупреждение, что раннее такой ветки сообщений не было, и создаст её.

    ![Создание ветки сообщений Kafka в powershell.exe](/platform/v5.0/administration/deploy/windows/auxiliary_software_deploy/img/kafka_install_powershell.png)

    Создание ветки сообщений Kafka в powershell.exe

## Подключение экземпляра {{ productName }} к Kafka

1. Откройте папку `C:\\ProgramData\\comindware\\configs\\instance`
2. Задайте параметры подключения к Kafka в файле `<instanceName>.yml` (`<instanceName>` — имя экземпляра ПО):

   ```
   # IP-адрес сервера Kafka
   mq.server: <KafkaIP>:9092
   # Имя экземпляра ПО
   mq.group: <instanceName>
   # Идентификатор узла очереди сообщений
   mq.node: <instanceName>

   ```
3. Удалите следующую строку из файла `<instanceName>.yml`:

   ```
   kafkaBootstrapServer:

   ```

   Внимание!

   Для корректной работы экземпляра ПО необходимо соблюсти следующие условия:

   - IP-адрес и порт {{ apacheKafkaVariants }} должны быть обязательно прописаны цифрами в формате `XXX.XXX.XXX.XXX:XXXXX`. То есть недопустимо указывать имя хоста вместо IP-адреса и опускать номер порта.
   - Установите соответствующие вашей конфигурации значения параметров `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений). Они должны совпадать во всех файлах конфигурации:

     ```
     C:\\ProgramData\\comindware\\configs\\instance\\<instanceName>.yml
     C:\\ProgramData\\comindware\\Instances\\<InstanceName>\\config\\apigateway.yml
     C:\\ProgramData\\comindware\\Instances\\<InstanceName>\\config\\adapterhost.yml

     ```
   - Удостоверьтесь, что в `YML`-файлах конфигурации все пути указаны с обратной косой чертой `\\` в стиле Windows, а не в стиле Linux `/`.
4. Задайте параметры подключения к Kafka в файле `apigateway.yml`:

   ```
   # Укажите IP-адрес сервера Kafka
   # без префикса http/https
   mq.server: <KafkaIP>:9092
   # Укажите имя экземпляра ПО
   mq.group: <instanceName>
   # Идентификатор узла очереди сообщений
   mq.node: <instanceName>

   ```
5. Задайте параметры подключения к Kafka в файле `adapterhost.yml`:

   ```
   # Укажите IP-адрес сервера Kafka
   mq.server: <KafkaIP>:9092

   ```
6. Перезапустите экземпляр ПО.
7. Проверьте соединение с Kafka в браузере по ссылке (`<instanceAddress>` — URL экземпляра ПО):

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
- [Пути и содержимое директорий экземпляра ПО][paths_windows]

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
