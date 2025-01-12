---
title: Синхронизация с веб-сервисом
tags:
  - приложение
  - интеграции
  - интеграция по OData
  - OData
  - подключения
  - подключение
  - синхронизация
hide:
  - tags
kbId: 4702
---

# Синхронизация с веб-сервисом. Настройка подключения {: #odata_connection}

## Настройка подключения к OData-сервису

1. Откройте раздел «**Администрирование**» — «**Подключения**».
2. Создайте подключение типа «**Синхронизация с веб-сервисом**».

    _![Создание подключения для синхронизации с веб-сервисом](odata_integration_connection_create.png)_

3. Настройте свойства подключения.

    - **Название** — наглядное название подключения к OData-сервису.
    - **Адрес веб-сервиса** — URL для подключения к серверу OData.

        !!! tip "Совет"

            Для экспериментов с синхронизацией по OData можно использовать общедоступные серверы, предоставляемые OData.org.

            Например, для тестирования импорта данных в качестве **адреса веб-сервиса** можно указать: 

            [https://services.odata.org/V3/OData/OData.svc/](https://services.odata.org/V3/OData/OData.svc/)

            Адреса остальных тестовых серверов OData.org представлены на следующих сайтах:

            [https://services.odata.org/](https://services.odata.org/) 

            [https://www.odata.org/odata-services/](https://www.odata.org/odata-services/) 

        {% include-markdown ".snippets/pdfPageBreakHard.md" %}

    - **Тип аутентификации**:
    {: .pageBreakBefore }
        - **Без аутентификации**
        - **Обычная**
        - **Windows**
    - **Имя пользователя** — укажите в случае выбора **типа аутентификации** «**Обычная**» или «**Windows**».
    - **Пароль** — укажите в случае выбора **типа аутентификации** «**Обычная**» или «**Windows**».
    - **Тайм-аут запроса** — время ожидания выполнения запроса, по истечении которого запрос отменяется.
    - **Версия OData**
        - **V2**
        - **V3**
        - **V4**
    - **Заголовки** — при необходимости укажите особые заголовки запроса:
        - **Заголовок** — имя заголовка;
        - **Значение заголовка** — содержимое заголовка.
    - **Отключить** — установите этот флажок, если требуется деактивировать данное подключение.

4. Сохраните подключение.
5. Нажмите кнопку «**Проверить соединение**». В области «**Результаты**» отобразятся полученные с сервера сущности.

_![Настройка свойств подключения для синхронизации с веб-сервисом](odata_integration_connection_properties.png)_

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Синхронизация с веб-сервисом. Интеграция по OData][odata_integration]_
- _[Интеграция с 1С по OData. Настройка для импорта данных][1c_integrations]_

</div>

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}
