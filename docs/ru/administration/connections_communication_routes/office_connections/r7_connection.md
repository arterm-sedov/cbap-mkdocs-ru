---
title: Р7 Офис
kbId: 2342
---

# Р7 Офис. Настройка сервера и подключения {: #r7_connection}

## Введение

**{{ productName }}** позволяет просматривать и редактировать прикреплённые к формам документы, электронные таблицы и презентации с помощью ПО «**Р7-Офис. Профессиональный. Сервер документов**» (далее «**Р7-Офис**»).

В данной статье представлены инструкции по настройке конфигурации сервера **Р7-Офис** и подключения к **Р7-Офис** в **{{ productName }}**.

См. также статью _«[Р7 Офис и Collabora Online. Использование для работы с документами]({{ kbArticleURLPrefix }}2343)»._

### Требования к серверу Р7-Офис

- Сервер **Р7-Офис** должен быть доступен серверу **{{ productName }}** и компьютерам конечных пользователей **{{ productName }}** посредством сетевого соединения.
- Конфигурацию сервера **Р7-Офис** необходимо модифицировать для поддержки работы с **{{ productName }}**.

!!! note "Примечание"

    Документы, создаваемые и редактируемые с помощью **Р7-Офис**, хранятся в папке загруженных файлов на сервере **{{ productName }}**. См. статью «[Просмотр фактических путей к папкам экземпляра продукта]({{ kbArticleURLPrefix }}2036)».

## Настройка конфигурации Р7-Офис

1. Откройте в текстовом редакторе файл конфигурации **Р-7 Офис**:  

    ```
    /etc/r7-office/documentserver/local.json
    ```

2. Установите следующие значения:  

    ```
    services.CoAuthoring.token.enable.request.inbox: **true**
    services.CoAuthoring.token.enable.browser: **true**
    ```

    _![Настройка конфигурации Р7-Офис](r7_connection_settings_configuration.png)_

3. Скопируйте в буфер обмена токен подключения из строки `services.CoAuthoring.secret.outbox.string`

_![Токен подключения в файле конфигурации Р7-Офис](r7_connection_token.png)_

## Настройка подключения к Р7-Офис

1. Перейдите в раздел [«**Администрирование**» — «**Подключения**»][administration].
2. Откройте двойным нажатием в списке или создайте подключение типа «**Подключения к офисным приложениям**» — «**Р7-Офис**».
3. Настройте подключение к Р7-Офис:

    - **Отключить** — установите этот флажок, чтобы временно прекратить использование данного подключения.
    - **Название подключения** — введите наглядное наименование подключения.
    - **Адрес сервера** — введите URL сервера включая порт.
    - **Ключ токена к серверу документов** — введите ключ, скопированный из файла конфигурации **Сервера документов**.

4. Нажмите кнопку «**Проверить соединение**». Должно отобразиться сообщение об успешном подключении к **Серверу документов**.
5. Сохраните подключение.

_![Настройка подключения к Р7-Офис](r7_connection_settings.png)_

--8<-- "related_topics_heading.md"

**[Р7 Офис и Collabora Online. Использование для работы с документами]({{ kbArticleURLPrefix }}2343)**

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}