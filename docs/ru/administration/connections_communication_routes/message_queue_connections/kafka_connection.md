---
title: Получение сообщений через Kafka
kbTitle: Получение сообщений через Kafka. Настройка подключения, пути передачи данных и сценария
kbId: 4704
---

# Получение сообщений через {{ apacheKafkaVariants }} {: #kafka_connection}

{% include-markdown ".snippets/experimental_feature.md" %}

## Введение

Здесь представлены инструкции по настройке подключения, пути передачи данных и сценария для обмена данными с внешней системой посредством шины сообщений {{ apacheKafkaVariants }}.

{% if not gostech %}
Настройка обмена данными для шин MSMQ и RabbitMQ осуществляется аналогичным образом.
{% endif %}

!!! question "Определения"

    - **Подключения** **к шинам сообщений** {{ apacheKafkaVariants }}{% if not gostech %}, MSMQ и RabbitMQ{% endif %} используются для обмена данными между  и с внешними системами. 
    - Для обмена данными требуется настроить **подключение** и **путь передачи данных**, который обеспечивает преобразование данных между системами.
    - **{{ apacheKafkaVariants }}** — это распределённая система обмена сообщениями с высокой пропускной способностью.
    - **Продюсер** — это сервис, который записывает сообщения в топик {{ apacheKafkaVariants }} для передачи потребителям.
    - **Брокер** — это сервис, который хранит и обрабатывает сообщения в топиках {{ apacheKafkaVariants }}. Брокеры объединены в кластер.
    - **Потребитель**, **консюмер** — это сервис, который получает сообщения из топиков {{ apacheKafkaVariants }}.
    - **Топик** {{ apacheKafkaVariants }} — это хранилище сообщений, объединённых общей бизнес-логикой. Например, в одном топике можно объединить сообщения о заказах, а в другом сообщения о бухгалтерских проводках. К одному топику могут обращаться несколько продюсеров и потребителей. Топик может быть разбит на **разделы**.
{% if pdfOutput %}

!!! question "Определения — продолжение"
{% endif %}
    - **Раздел**, **партиция** — составная часть **топика**. Раздел состоит из **сегментов** — файловых журналов сообщений. Сообщения нумеруются последовательно, записываются в конец сегмента и хранятся неизменными. Разделы могут находиться в разных **брокерах**.
    - При получении сообщений через шину {{ apacheKafkaVariants }} **{{ productName }}** является **потребителем**, а при отправке — **продюсером**.

## Прикладная задача

Необходимо настроить интеграцию с шиной {{ apacheKafkaVariants }}, которая будет опрашивать топик `CLIENT_ORDERS`, извлекать из него данные о заказах клиентов и создавать для каждого полученного заказа запись в шаблоне _«Заказы»_ с заполненными кодом и суммой заказа.

## Исходные данные

- Имеется приложение _«Обработка заказов»__._
- В приложении имеется шаблон записи _«Заказы»_ со следующими атрибутами:

    | Название атрибута | Тип данных |
    | ----------------- | ---------- |
    | _Код заказа_      | **Текст**  |
    | _Сумма заказа_    | **Число**  |

- Имеется сервер {{ apacheKafkaVariants }}, доступный по адресу `12.34.56.78:9092`

## Настройка подключения к {{ apacheKafkaVariants }} {: #kafka_connection_configure .pageBreakBefore }

1. Откройте страницу [«**Администрирование**» — «**Подключения**»][administration].
2. Создайте или настройте **подключение к шине сообщений** типа «**Получение сообщений через Kafka**»:

    - **Системное имя** — введите уникальное имя из латинских букв и цифр, например `kafka_receive_messages_connection`
    - **Отключить** — установите этот флажок, если требуется деактивировать подключение.
    - **Описание** — введите наглядное описание подключения.
    - **Запись в файловые журналы** — выберите способ записи сведений о работе подключения:

        - **Полные сведения об обработке сообщения**
        - **Только ошибки**
        - **Отключить**

    - **Список пар хост/порт (разделённых запятой), используемых для подключения к кластеру Kafka** — введите адреса одного или нескольких узлов кластера {{ apacheKafkaVariants }}, например `123.45.67.89:9092`.
    - **Максимальный объем данных (в байтах), который брокеры должны возвращать по запросу сообщений** — введите лимит для ответа каждого брокера, при превышении которого ответ будет содержать только первые сообщения, поместившиеся в лимит, а остальные сообщения будут отброшены.
    - **Количество байтов, которые необходимо попытаться получить для каждого топика-партиции в каждом запросе сообщений** — введите объём данных для получения от {{ apacheKafkaVariants }}, не меньше максимального размера сообщения, допустимого сервером {{ apacheKafkaVariants }}. При превышении лимита сообщения не будут переданы.
    - **Тайм-аут (в миллисекундах) для запросов на стороне сервера Kafka** — введите лимит времени обработки запроса сервером {{ apacheKafkaVariants }}. При превышении лимита обмен данными будет прерван.
    - **Тайм-аут на стороне клиента (в миллисекундах)** — введите лимит времени ожидания ответа от сервера {{ apacheKafkaVariants }}. При превышении лимита сообщения не будут переданы.
    - **Временной интервал (в миллисекундах) для пакетной обработки сообщений, используемых при запросах сообщений** — введите интервал опроса {{ apacheKafkaVariants }}.
    - **Имя пользователя** и **пароль** — введите логин и пароль для подключения к серверу {{ apacheKafkaVariants }}.

## Настройка пути передачи данных через {{ apacheKafkaVariants }} {: #kafka_connection_communication_route_configure}

1. Откройте страницу [«**Администрирование**» — «**Пути передачи данных**»][administration].
2. Создайте или настройте путь передачи данных для **подключения к шине сообщений** типа «**Получение сообщений через Kafka**».
3. Настройте параметры на вкладке «**Основные свойства**»:

    - **Подключение** — выберите ранее настроенное [подключение к шине {{ apacheKafkaVariants }}](#kafka_connection_configure): `kafka_receive_messages_connection`
    - **Системное имя** — введите уникальное имя из латинских букв и цифр, например `kafka_receive_messages_route`
    - **Отключить** — установите этот флажок, если требуется деактивировать путь передачи данных.
    - **Описание** — введите наглядное описание пути передачи данных.
    - **Номер шины данных** — выберите номер потока обработки сообщений, например **0**. Если одновременно используется много путей передачи данных через {{ apacheKafkaVariants }}, для распределения нагрузки может потребоваться выбрать для них разные номера шины данных.

4. Настройте параметры на вкладке «**Атрибуты сообщений**»:

    - **Тип сообщения** — выберите тип «**Получение сообщений через Kafka**» (в соответствии с типом пути передачи данных).
    - **Запрос** — с помощью кнопки «**Добавить**» сформируйте структуру атрибутов, соответствующую структуре сообщения в формате XML/JSON. Значения этих атрибутов будут помещены в переменную и обработаны с помощью [сценария](#настройка-сценария), срабатывающего при наступлении события «**Получение сообщения**»:

        - **Системное имя** — введите имя, совпадающее с именем поля в XML/JSON с точностью до строчных и прописных букв.
        - **Тип** — выберите тип атрибута, соответствующий типу поля в XML/JSON.
        - **Описание** — введите наглядное описание атрибута.
        - **Обязательный** — установите этот флажок, если атрибут должен присутствовать в сообщении.
        - **Не пустой** — установите этот флажок, если атрибут должен иметь значение.
        - **Массив** — установите этот флажок, если атрибут может содержать список значений.

        !!! note "Примечание"

            Чтобы добавить дочерний атрибут, установите флажок в первом столбце таблицы у родительского атрибута и нажмите кнопку «**Добавить**».

        !!! example "Пример передачи массива объектов"

            - Сообщение содержит массив объектов `orders` в формате JSON:

                ```
                {
                    "orders": [
                        {
                        "code": "12-A",
                        "amount": 123
                        },
                        {
                        "code": "34-B"
                        "amount": 345
                        },
                        {
                        "code": "56-C",
                        "amount": 678
                        }
                    ]
                }
                ```

            - Для получения данных из приведённого выше сообщения создайте следующие атрибуты:

                | Родительский атрибут | Системное имя | Тип данных | Массив            |
                | -------------------- | ------------- | ---------- | ----------------- |
                |                      | _orders_      | **Объект** | Флажок установлен |
                | _orders_             | _code_        | **Строка** |                   |
                | _orders_             | _amount_      | **Число**  |                   |

    - **Ответ** и **Ответ с ошибкой** — аналогично запросу, сформируйте структуру атрибутов для отправки серверу {{ apacheKafkaVariants }} ответа на полученный запрос. Значения этим атрибутам можно присвоить с помощью [сценария](#настройка-сценария), срабатывающего при наступлении события «**Получение сообщения**».
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

5. Настройте параметры на вкладке «**Интеграция**»:

    - **Очередь** — введите название топика {{ apacheKafkaVariants }}, который необходимо прослушивать, например `CLIENT_ORDERS`.
    - **Тип содержимого** — выберите формат передачи данных:
        - **XML**
        - **JSON**
    - **Уникальная текстовая строка** — укажите название группы потребителей. Например, введите имя экземпляра ПО **{{ productName }}**. Название группы потребителей служит для отслеживания новых сообщений в топике. Не назначайте это название группы другим потребителям, в противном случае будет утрачен прогресс считывания сообщений из топика.

## Настройка сценария {. pageBreakBefore }

Для получения сообщений через шину {{ apacheKafkaVariants }} и передачи данных в шаблон записи требуется настроить [сценарий][scenarios], срабатывающий при поступлении сообщения из {{ apacheKafkaVariants }}.

1. На странице **администрирования приложения** выберите пункт «**Сценарии**».
2. Создайте сценарий:

    - **Название**: _Получение данных из {{ apacheKafkaVariants }}_
    - **Системное имя**: заполняется автоматически.
    - **Контекст выполнения**: **От инициатора**
    - **Статус**: на время настройки триггера можно выбрать «**Приостановлен**», чтобы сценарий не срабатывал без необходимости. После настройки сценария, установите статус «**Активен**», чтобы сценарий обрабатывал сообщения, появляющиеся в топике {{ apacheKafkaVariants }}.

3. Отобразится конструктор сценария.
4. Нажмите заголовок события «**Нажатие кнопки**».
5. Настройте свойства события:

    - **Тип: Получение сообщения**
    - **Контекстный шаблон:** _Заказы_
    - **Подключение:** _kafka_receive_messages_connection_
    - **Путь передачи данных:** _kafka_receive_messages_connection_
    - **Имя переменной:** _kafka_message —_ в этой переменной будет храниться полученное сообщение.

6. После события «**Получение сообщения**» создайте и настройте действие «**Повторять по количеству объектов**»:

    - **Переменная:** _order_
    - **Атрибут или выражение для поиска объектов: формула**

        ```
        $$kafka_message->orders
        ```

        На каждой итерации цикла в переменную `order` будет помещаться объект из полученного в сообщении от {{ apacheKafkaVariants }} массива `orders`.

7. Внутри действия «**Повторять по количеству объектов**» создайте действие «**Создать запись**» с целевым шаблоном _«Заказы»_.
8. Внутри действия «**Создать запись**» создайте действие «**Изменить значение атрибутов**».
9. В действии «**Изменить значения атрибутов**» на вкладке «**Дополнительно**» установите флажок «**Сбрасывать кэш значений**».
10. На вкладке «**Основные**» настройте следующие атрибуты:

    | Атрибут        | Операция со значениями | Значение                       |
    | -------------- | ---------------------- | ------------------------------ |
    | _Код заказа_   | **Заменить**           | **Формула:** `$$order->code`   |
    | _Сумма заказа_ | **Заменить**           | **Формула: `$$order->amount`** |

_![Настроенный сценарий для получения данных через шину {{ apacheKafkaVariants }}](kafka_connection_scenarios.png)_

## Создание топика и тестирование работы интеграции {: .pageBreakBefore }

1. С помощью скрипта продюсера {{ apacheKafkaVariants }} инициализируйте топик, например `CLIENT_ORDERS`:

    ```
    sudo -i
    cd /usr/share/kafka/bin
    bash kafka-console-producer.sh --bootstrap-server 12.34.56.78:9092 --topic CLIENT_ORDER
    ```

    Здесь `12.34.56/78:9092` — IP-адрес сервера {{ apacheKafkaVariants }}.

2. В терминале отобразится запрос сообщения.
3. Каждая введённая строка будет отправлена при нажатии клавиши ++enter++.
4. Отправьте в топик сообщение с данными заказов, например, в формате JSON:

    ```
    { "orders": [ { "code": "12-A", "amount": 123 }, { "code": "34-B" "amount": 345 }, { "code": "56-C", "amount": 678 } ] }
    ```

5. Продюсер отправит введённое сообщение в топик {{ apacheKafkaVariants }}.
6. Чтобы завершить работу продюсера нажмите в терминале клавиши ++ctrl+c++.
7. Откройте шаблон записи _«Заказы»_ и нажмите кнопку «**Перейти к экземплярам**».
8. В шаблоне должны быть созданы записи, заполненные данными заказов из сообщения {{ apacheKafkaVariants }}.

## Просмотр журнала работы сценария

1. Откройте страницу «**Журналы событий**».
2. Выберите вкладку «**Трассировка событий**».
3. Дважды нажмите событие сценария _«Получение данных из {{ apacheKafkaVariants }}»_.
4. Отобразится цепочка событий со сведениями обо всех шагах сценария.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Подключения. Типы, создание, настройка, удаление][connections]_
- _[Пути передачи данных. Типы, создание, настройка, удаление][communication_routes]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
