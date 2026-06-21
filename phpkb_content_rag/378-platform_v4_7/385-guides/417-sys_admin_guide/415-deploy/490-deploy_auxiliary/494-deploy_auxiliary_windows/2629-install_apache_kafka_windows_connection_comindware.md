---
title: 'Установка Kafka в ОС Windows и подключение к Comindware Business Application Platform'
kbId: 2629
url: 'https://kb.comindware.ru/article.php?id=2629'
updated: '2024-08-15 14:30:44'
---

# Установка Kafka в ОС Windows и подключение к Comindware Business Application Platform

## Введение

Для обмена данными между **Comindware Business Application Platform** и внешними системами (а также для работы обсуждений) необходимо настроить подключение к брокеру сообщений Kafka.

Здесь представлена инструкция по установке Kafka в ОС Windows с использованием KRaft (без использования Zookeeper) и подключению Kafka к **Comindware Business Application Platform**.

## Предварительные условия

Должно быть установлено ПО Java и заданы следующие системные переменные:

- `JAVA_HOME` — путь к исполняемым файлам Open JDK, например `C:\Program Files\jdk\jdk-<version>`
- `JAVA_HOME_DLL` — путь к DLL-файлу Open JDK, например `C:\Program Files\jdk\jdk-<version>\bin\server\jvm.dll`
- `Path` — короткий путь к файлам Java: `%JAVA_HOME%\bin`

## Процесс установки

1. Скачайте последнюю версию Kafka с **[официального сайта](https://kafka.apache.org/downloads)**.

   Внимание!

   Для корректной работы Kafka рекомендуется скачивать архив с бинарными файлами.
2. Распакуйте файлы архива, например в папку `C:\kafka\kafka`

   Внимание!

   Рекомендуется использовать путь минимальной длины и названия папок без пробелов, иначе некоторые команды могут не сработать.
3. Создайте папку для журналов, например `X:\kafka\logs`.

   Внимание!

   Рекомендуется создавать папку для журналов на отдельном диске, а не на диске где установлено ПО Kafka.
4. Откройте файл конфигурации Kafka `C:\kafka\kafka\config\kraft\server.properties`.
5. Отредактируйте файл конфигурации, указав IP-адрес сервера Kafka и папку для журналов. При указании пути к папке журналов используйте косую черту `/`:

   ```
   process.roles=broker,controller
   node.id=1
   # Укажите IP-адрес сервера Kafka
   controller.quorum.voters=1@10.9.8.7:9093
   # Укажите IP-адрес сервера Kafka
   listeners=PLAINTEXT://10.9.8.7:9092,CONTROLLER://10.9.8.7:9093
   inter.broker.listener.name=PLAINTEXT
   # Укажите IP-адрес сервера Kafka
   advertised.listeners=PLAINTEXT://10.9.8.7:9092
   controller.listener.names=CONTROLLER
   listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL
   num.network.threads=3
   num.io.threads=8
   socket.send.buffer.bytes=102400
   socket.receive.buffer.bytes=102400
   socket.request.max.bytes=104857600
   # Укажите путь к папке журналов
   log.dirs=X:/kafka/logs
   num.partitions=1
   num.recovery.threads.per.data.dir=1
   offsets.topic.replication.factor=1
   transaction.state.log.replication.factor=1
   transaction.state.log.min.isr=1
   log.retention.hours=168
   log.segment.bytes=1073741824
   log.retention.check.interval.ms=300000
   ```
6. Откройте *PowerShell* от имени администратора и выполните команды:

   ```
   cd "C:\kafka\kafka\bin\windows\"
   .\kafka-storage.bat random-uuid
   ```
7. Kafka выдаст UID, например, `kNZtrWDsRvW0udJeaEahsg`
8. Используйте полученный UID в следующей команде:

   ```
   .\kafka-storage.bat format -t kNZtrWDsRvW0udJeaEahsg -c C:\kafka\kafka\config\kraft\server.properties
   ```
9. Загрузите с **[официального сайта](https://nssm.cc/download)** архив *NSSM* и распакуйте его.
10. В папке `\win64` найдите файл `nssm.exe` и скопируйте его в папку `C:\kafka\kafka\bin\windows\`.
11. В *PowerShell* от имени администратора выполните следующую команду:

    ```
    .\nssm install kafka
    ```
12. Запустится программа `NSSM service installer`.

_![Диалоговое окно NSSM service installer](https://kb.comindware.ru/assets/kafka_install_nssm_service_installer.png)_

13. Укажите следующие пути к файлам службы Kafka:

    - **Path**

    ```
    C:\kafka\kafka\bin\windows\kafka-server-start.bat
    ```

    - **Startup directory**

    ```
    C:\kafka\kafka\bin\windows\
    ```

    - **Arguments**

    ```
    C:\kafka\kafka\config\kraft\server.properties
    ```
14. Нажмите кнопку «**Install service**».
15. Произойдёт установка сервиса.
16. По завершении установки откройте программу *«Службы*» (*Services*) и найдите в списке `kafka`.

    ![Kafka в списке служб](https://kb.comindware.ru/assets/kafka_install_services.png)

    Kafka в списке служб
17. С помощью свойств службы включите и настройте автоматический перезапуск Kafka.

    ![Окно настройки службы Kafka](https://kb.comindware.ru/assets/kafka_install_kafka_service.png)

    Окно настройки службы Kafka
18. Протестируйте работу Kafka, выполнив в *PowerShell* следующие команды:

    ```
    cd "C:\kafka\kafka\bin\windows\"
    .\kafka-console-producer.bat --bootstrap-server 10.9.8.7:9092 --topic TEST
    # Отправьте любое сообщение, например:
    hello
    ```
19. При правильной работе Kafka выдаст предупреждение, что раннее такой ветки сообщений не было, и создаст её.

    ![Создание ветки сообщений Kafka в powershell.exe](https://kb.comindware.ru/assets/kafka_install_powershell.png)

    Создание ветки сообщений Kafka в powershell.exe

## Подключение Kafka к Comindware Business Application Platform

1. Откройте папку `C:\ProgramData\comindware\configs\instance`
2. Откройте файл с именем экземпляра ПО `.yml` и измените или добавьте следующую директиву:

   ```
   # Укажите IP-адрес сервера Kafka
   mq.server: 10.9.8.7:9092
   # Укажите имя экземпляра ПО
   mq.name: <instanceName>
   ```
3. Удалите следующую строку из файла `.yml`:

   ```
   kafkaBootstrapServer:
   ```
4. Перезапустите экземпляр ПО с помощью Утилиты администрирования.
5. Проверьте соединение с Kafka в браузере по ссылке:

   ```
   <instanceName>/async
   ```