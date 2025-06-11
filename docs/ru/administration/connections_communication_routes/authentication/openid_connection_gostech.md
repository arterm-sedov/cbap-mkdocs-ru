---
title: Аутентификация через OpenID Connect
kbId: 4685
---

# Аутентификация через OpenID Connect. Настройка подключения и служб {: #openid_connection}

## Настройка конфигурации перед развёртыванием {{ productName }}

1. Перед тем как развёртывать **{{ productName }}** измените в конфигурационном файле `values.yaml` Helm-чарта следующие директивы:

    ``` yaml
    ...
    platform:
        config:
        # Укажите данные данные интеграции с {{ authServiceVariants }}
        auth_openId_enabled: "true"
        auth_openId_server: <plarformViAMServerAddress>
        auth_openId_realm: <plarformViAMServerRealm>
        auth_openId_clientId: <plarformViAMServerClientId>
        auth_openId_clientSecret: <plarformViAMClientSecret>
    ...
    ```

2. Сохраните файл конфигурации.
3. Разверните экземпляр ПО. См. _«[Установка и инициализация ПО][deploy_guide_linux]»_.

## Проверка адреса сервера {{ productName }}

1. Откройте раздел [«**Администрирование**» — «**Глобальная конфигурация**»][administration].
2. Удостоверьтесь, что **URL-адрес сервера** начинается с `https://`.

    _![Проверка адреса сервера](openid_connection_check.png)_

## Вход в {{ productName }} {: .pageBreakBefore }

1. Откройте веб-сайт экземпляра {{ productName }}, например [https://mycompany.ru](https://mycompany.ru/)
2. Нажмите кнопку «**Войти как администратор**».

    _![Переход к странице входа администратора](openid_connection_administrator_entry.png)_

3. Введите свои учётные данные и нажмите кнопку «**Войти**».

    _![Вход с аккаунтом администратора](openid_connection_administrator.png)_

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

4. Выйдите из системы.
5. Отобразится страница входа с кнопкой «**Войти с помощью Google**».

    _![Кнопка «Войти с помощью Google»](openid_connection_google_entry.png)_

6. На этом настройка входа через OpenID Connect завершена. Теперь пользователи смогут входить в **{{ productName }}** с помощью своих аккаунтов Google.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Установка и инициализация ПО][deploy_guide_linux]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
