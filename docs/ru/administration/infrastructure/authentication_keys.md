---
title: Ключи аутентификации API
kbId: 4674
---

# Ключи аутентификации API. Определения, настройка, удаление {: #authentication_keys}

<div class="admonition question" markdown="block">

## Определения {: .admonition-title #definitions}

- **Ключи аутентификации** используются для доступа к API **{{ productName }}** из внешних систем с использованием HMAC-аутентификации.
- Ключ аутентификации следует назначать аккаунту, у которого есть разрешение «**Вызовы API**» в [системной роли][system_roles], либо пользователю входящему в системную роль «**Системные администраторы**». Только такие аккаунты могут использовать API **{{ productName }}**.
- При HMAC-аутентификации внешняя система должна передать токен и секретный ключ.

</div>

## Просмотр списка и настройка ключа аутентификации

1. На странице «[**Администрирование**][administration]» в разделе «**Инфраструктура**» выберите пункт «**Ключи аутентификации**» <i class="fa-light fa-lock-keyhole">‌</i>.
2. Отобразится список ключей.

    _![Список ключей аутентификации](authentication_key_list.png)_

3. Нажмите кнопку «**Создать**» или дважды нажмите строку имеющегося ключа.
{: .pageBreakAfter}
4. При создании ключа выберите аккаунт **пользователя** и **срок действия ключа**. При настройке имеющегося ключа можно только изменить его **срок действия**.

    _![Настройка нового ключа аутентификации](authentication_key_settings.png)_

5. Нажмите кнопку «**Сохранить**».
6. Отобразятся свойства сформированного ключа.
7. Используйте сформированные **секретный ключ** и **токен для аутентификации** внешних систем при доступе к API **{{ productName }}**.

    _![Свойства сформированного ключа аутентификации](authentication_key_properties.png)_

## Удаление ключей аутентификации {: .pageBreakBefore }

!!! warning "Внимание!"

    После удаления ключей аутентификации аккаунты, которым они назначены, потеряют возможность использовать API **{{ productName }}** с HMAC-аутентификацией.

1. Откройте список ключей аутентификации.
2. Установите флажки в первом столбце для адаптеров, подлежащих удалению.
3. Нажмите кнопку «**Удалить**».
4. Подтвердите удаление ключей.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Введение в API][api_intro]_
- _[Системные роли. Определения, настройка, объединение, удаление][system_roles]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
