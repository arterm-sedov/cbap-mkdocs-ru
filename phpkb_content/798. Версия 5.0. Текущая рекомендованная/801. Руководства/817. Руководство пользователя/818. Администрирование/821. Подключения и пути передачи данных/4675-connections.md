---
title: Подключения. Определения, типы, создание, настройка, удаление
kbId: 4675
---

# Подключения. Определения, типы, создание, настройка, удаление

## Определения

- **Подключения** используются для интеграции и обмена данными между **{{ productName }}** и внешними системами.
- **Подключение** обеспечивает физическую передачу данных между системами.
- Для обмена данными требуется настроить **подключение** и **путь передачи данных**, который обеспечивает преобразование данных между системами. См. *«[Пути передачи данных. Определения, типы, создание, настройка, удаление][communication_routes]».*
- Одно **подключение** можно использовать для нескольких **путей передачи данных**, чтобы не настраивать общие параметры, такие как URL-адрес, учетные данные, ключ API и т. п.

См. также *[Примеры интеграций](https://kb.comindware.ru/category.php?id=875)*.

## Типы подключений

### Системные подключения

- [Управление версиями через Git][git_connection]
- [Elasticsearch][elasticsearch_connection]
- Абстрактное подключение
- [Карты][map_configure]
- [Хранилище S3][s3_connection]

### Аутентификация

- [Аутентификация через WS-Federation][wsfederation_connection]
- [Аутентификация через OpenID Connect][openid_connection]
- [Active Directory][ad_connection]

### Подключения к офисным приложениям

- [Р7 Офис][r7_connection]
- [Collabora Online][collabora_connection]

### Подключения к электронной почте

- [Получение эл. почты в процессе][process_receiving_connection]
- [Отправка эл. почты из процесса][process_sending_connection]
- [Получение эл. почты через Exchange][scenario_receive_email]
- [Отправка эл. почты через Exchange][scenario_send_email]
- [Получение эл. почты через IMAP][scenario_receive_email]
- [Отправка почты через SMTP][scenario_send_email]

### Подключения REST и OData

- [Получение веб-запросов][get_connection]
- [Отправка веб-запросов][http_send_request_connection]
- [Синхронизация с веб-сервисом][odata_connection]
- [Отправка HTTP-запросов][http_send_connection]
- [Получение HTTP-запросов][http_receive_example]

### Подключения к шине сообщений

- Отправка сообщений через Kafka
- [Получение сообщений через Kafka][kafka_connection]
- Отправка сообщений через MSMQ
- Получение сообщений через MSMQ
- Отправка сообщений через RabbitMQ
- Получение сообщений через RabbitMQ

### SQL-подключения

- [Отправка запросов в СУБД][sql_send_connection]
- [Получение данных из СУБД][sql_receive_connection]

### Пользовательские подключения

- [Отправка сообщений в «СФЕРА Курьер»][esphere_send_configure]
- [Получение сообщений из «СФЕРА Курьер»][esphere_receive_configure]

Примечание

В разделе «**Пользовательские подключения**» также отображаются подключения для [адаптеров][adapters].

## Просмотр списка подключений и настройка подключения

1. На странице [«**Администрирование**» – «**Инфраструктура**»][administration] выберите пункт «**Подключения**» *‌*.
2. Отобразится [список подключений][connections] со следующими сведениями:

   - **ID** — уникальный идентификатор подключения, формируется автоматически.
   - **Системное имя** — уникальное имя подключения.
   - **Тип** — назначение подключения, см. [типы подключений](#типы-подключений).
   - **Включено** — активное подключение обозначается флажком.
3. Нажмите кнопку «**Создать**» и выберите [тип подключения](#типы-подключений) или дважды нажмите подключение в списке.
4. Настройте свойства подключения.
5. Нажмите кнопку «**Проверить соединение**». В случае успешного соединения с сервером отобразится сообщение «**Соединение установлено**». Если соединение установить не удастся, отобразится сообщение об ошибке.
6. Сохраните подключение.

_![Список подключений](/platform/v5.0/administration/connections_communication_routes/img/connection_list.png)_

## Удаление подключения

1. Выберите подключение, установив для него флажок в первом столбце списка.
2. Нажмите кнопку «**Удалить**».
3. Подтвердите удаление.

--8<-- "related_topics_heading.md"

- *[Пути передачи данных. Определения, типы, создание, настройка, удаление][communication_routes]*
- *[Примеры интеграций](https://kb.comindware.ru/category.php?id=875)*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
