---
title: 'OpenSearch. Настройка разрешений'
kbId: 5152
tags:
  - OpenSearch
  - разрешения
  - права доступа
  - роли
  - журнал транзакций
  - журналирование
  - журналирование
  - безопасность
hide:
  - tags
---

# {{ openSearchVariants }}. Настройка разрешений {: #opensearch_permissions }

## Введение {: #opensearch_permissions_intro }

**{{ productName }}** использует службу {{ openSearchVariants }} для журналирования транзакций (истории изменений записей и [экземпляров процессов][process_diagram_view_instance], [цепочки событий][logs_event_chain_view] и т.&nbsp;п.).

Для корректной работы журнала транзакций пользователь **{{ productName }}** в {{ openSearchVariants }} должен иметь необходимые разрешения на создание индексов, запись и чтение данных.

Здесь представлены инструкции по настройке разрешений для пользователя **{{ productName }}** в {{ openSearchVariants }}.

!!! note "Служебный пользователь в {{ openSearchVariants }}"

    - В конфигурации экземпляра ПО необходимо указать адрес сервера и уникальный префикс индексов {{ openSearchVariants }}. Индекс префикса служит для идентификации данных экземпляра ПО на сервере журналирования транзакций. Поэтому во избежание конфликтов данных для каждого экземпляра ПО следует указывать собственный префикс индекса.
    - В конфигурации сервера {{ openSearchVariants }} необходимо создать одного пользователя для **{{ productName }}**.
    - При инициализации экземпляра ПО или в конфигурации экземпляра необходимо указать пользователя **{{ productName }}**, используемого сервером {{ openSearchVariants }}.
    - Экземпляр ПО будет взаимодействовать с {{ openSearchVariants }} под указанным пользователем и создавать, наполнять и читать индексы с заданным префиксом.

См. также _«[{{ openSearchVariants }}. Настройка подключения][elasticsearch_connection]»_.

## Обзор необходимых разрешений {: #opensearch_permissions_overview }

Для корректной работы журнала транзакций пользователь **{{ productName }}** в {{ openSearchVariants }} должен иметь перечисленные ниже разрешения.

### Разрешения на управление индексами {: #opensearch_permissions_index_management }

Обеспечивают управление структурой хранилища журналов: создание индексов и обновление сопоставления полей.

| Разрешение | Описание | Применение в {{ productName }} |
| :-- | :-- | :-- |
| `indices:admin/create` | Создание новых индексов | Создание индексов при первом запуске |
| `indices:admin/data_stream/create` | Создание потоков данных | Автоматизированное конвейерное журналирование транзакций |
| `indices:admin/mapping/put` | Обновление сопоставлений индекса | Изменение структуры данных (например, при обновлении версии {{ productName }}) |

### Разрешения на чтение данных {: #opensearch_permissions_read }

Обеспечивают доступ для чтения и поиска записей в журнале транзакций.

| Разрешение | Описание | Применение в {{ productName }} |
| :-- | :-- | :-- |
| `indices:data/read/get` | Получение данных | Просмотр конкретной записи о транзакции |
| `indices:data/read/search` | Поиск в индексах | Базовый поиск |
| `indices:data/read/search*` | Все варианты поиска | Агрегации, сложные запросы для фильтрации и анализа |
| `indices:data/read/search/template` | Использование сохранённых шаблонов | Повторные поисковые запросы |

### Разрешения Point-in-Time {: #opensearch_permissions_pit }

Обеспечивают создание консистентных снимков при обработке больших объёмов данных.

| Разрешение | Описание | Применение в {{ productName }} |
| :-- | :-- | :-- |
| `indices:data/read/point_in_time/create` | Создание сеанса PIT | Для консистентной работы с большими наборами данных |
| `indices:data/read/point_in_time/readall` | Чтение всех сеансов PIT | Управление активными сеансами Point-in-Time |

### Разрешения на запись данных {: #opensearch_permissions_write }

Обеспечивают запись и обновление записей о транзакциях в журнале.

| Разрешение | Описание | Применение в {{ productName }} |
| :-- | :-- | :-- |
| `indices:data/write/index` | Индексирование транзакций | Основная операция записи транзакций в журнал |
| `indices:data/write/update` | Обновление существующих транзакций | Коррекция ошибочных записей |
| `indices:data/write/update/byquery` | Массовое обновление по условию | Батч-операции для исправления данных |
| `indices:data/write*` | Все операции записи | Удаление, переиндексация и прочие операции |

### Глобальные разрешения кластера {: #opensearch_permissions_cluster }

Обеспечивают базовые возможности работы с индексами на уровне кластера.

| Разрешение | Описание | Применение в {{ productName }} |
| :-- | :-- | :-- |
| `read` | Глобальное чтение на уровне кластера | Базовый доступ ко всем операциям чтения |
| `write` | Глобальная запись на уровне кластера | Базовый доступ ко всем операциям записи |

## Настройка роли для {{ productName }} {: #opensearch_permissions_role_config }

Для пользователя **{{ productName }}** рекомендуется создать отдельную роль с необходимыми разрешениями. Роль должна предоставлять доступ только к индексам с префиксом, указанным в параметре `journal.name` конфигурации экземпляра ПО.

### Создание роли через REST API {: #opensearch_permissions_role_config_api }

1. Создайте роль с необходимыми разрешениями:

    ``` bash
    curl -X PUT \
      --user <cmwJournalUserName>:<safePassword> \
      --cacert /path/to/root.crt \
      -H "Content-Type: application/json" \
      https://<openSearchHost>:<port>/_plugins/_security/api/roles/<cmwJournalRole> \
      -d '{
        "index_permissions": [{
          "index_patterns": ["<prefix>*"],
          "dls": "",
          "fls": [],
          "masked_fields": [],
          "allowed_actions": [
            "indices:admin/create",
            "indices:admin/data_stream/create",
            "indices:admin/mapping/put",
            "indices:data/read/get",
            "indices:data/read/search",
            "indices:data/read/search*",
            "indices:data/read/search/template",
            "indices:data/read/point_in_time/create",
            "indices:data/read/point_in_time/readall",
            "indices:data/write/index",
            "indices:data/write/update",
            "indices:data/write/update/byquery",
            "indices:data/write*"
          ]
        }],
        "cluster_permissions": [
          "read",
          "write"
        ]
      }'
    ```

    Здесь:
    - `<prefix>` — значение параметра `journal.name` из конфигурации экземпляра ПО (по умолчанию `cmw<instanceName>`, где `<instanceName>` — имя экземпляра ПО);
    - `<host>:<port>` — адрес сервера {{ openSearchVariants }};
    - `/path/to/root.crt` — путь к сертификату корневого центра сертификации (если используется TLS).

    !!! note "Примечание"

        Если используется несколько экземпляров **{{ productName }}** с разными префиксами индексов, создайте отдельную роль для каждого префикса или используйте шаблон индекса, охватывающий все необходимые префиксы.

2. Создайте пользователя и назначьте ему роль:

    ``` bash
    curl -X PUT \
      --user <cmwJournalUserName>:<safePassword> \
      --cacert /path/to/root.crt \
      -H "Content-Type: application/json" \
      https://<openSearchHost>:<port>/_plugins/_security/api/internalusers/<cmwJournalUserName> \
      -d '{
        "password": "<safePassword>",
        "opendistro_security_roles": ["<cmwJournalRole>"],
        "backend_roles": [],
        "attributes": {}
      }'
    ```

3. Укажите созданного пользователя в конфигурации экземпляра ПО:

    ``` yaml title="Пример конфигурации подключения к {{ openSearchVariants }}"
    # Адрес службы журналирования {{ openSearchVariants }}.
    journal.server: https://<openSearchHost>:<port>
    # Префикс индекса службы журналирования {{ openSearchVariants }}.
    journal.name: <prefix>
    # Имя пользователя службы журналирования
    journal.username: <cmwJournalUserName>
    # Пароль службы журналирования
    journal.password: <safePassword>
    ```

### Создание роли через OpenSearch Dashboards {: #opensearch_permissions_role_config_dashboards }

1. Откройте OpenSearch Dashboards и перейдите в раздел **Security** → **Roles**.
2. Нажмите **Create role**.
3. Укажите имя роли, например `cmwJournalRole`.
4. В разделе **Index permissions**:

    - В поле **Index** укажите шаблон индекса: `<prefix>*` (например, `cmw<instanceName>*`).
    - В разделе **Index permissions** добавьте следующие разрешения:
        - `indices:admin/create`
        - `indices:admin/data_stream/create`
        - `indices:admin/mapping/put`
        - `indices:data/read/get`
        - `indices:data/read/search`
        - `indices:data/read/search*`
        - `indices:data/read/search/template`
        - `indices:data/read/point_in_time/create`
        - `indices:data/read/point_in_time/readall`
        - `indices:data/write/index`
        - `indices:data/write/update`
        - `indices:data/write/update/byquery`
        - `indices:data/write*`

5. В разделе **Cluster permissions** добавьте:
    - `read`
    - `write`

6. Нажмите **Create**.

7. Перейдите в раздел **Security** → **Internal Users** и создайте пользователя или отредактируйте существующего.

8. В разделе **Mapped users** назначьте созданную роль пользователю.

## Проверка конфигурации {: #opensearch_permissions_verification }

После настройки разрешений проверьте, что пользователь **{{ productName }}** может выполнять необходимые операции для работы журнала транзакций:

1. Проверьте доступ к поиску в индексах:

    ``` bash
    curl -X GET \
      --user <cmwJournalUserName>:<safePassword> \
      --cacert /path/to/root.crt \
      https://<openSearchHost>:<port>/<prefix>*/_search?size=10
    ```

2. Проверьте возможность создания индекса:

    ``` bash
    curl -X PUT \
      --user <userName>:<safePassword> \
      --cacert /path/to/root.crt \
      https://<openSearchHost>:<port>/<prefix_test_index>
    ```

    !!! note "Очистка тестового индекса"

        Тестовый индекс `<prefix_test_index>` останется после проверки, так как удаление индексов требует разрешения `indices:admin/delete`, которое не входит в список необходимых разрешений для работы журнала транзакций.

        Для удаления тестового индекса выполните команду **от имени администратора {{ openSearchVariants }}**:

        ``` bash
        curl -X DELETE \
          --user <adminUser>:<safePassword> \
          --cacert /path/to/root.crt \
          https://<openSearchHost>:<port>/<prefix_test_index>
        ```

3. Проверьте подключение из **{{ productName }}**:

    - Перейдите в [список подключений][connections].
    - Откройте подключение к {{ openSearchVariants }}.
    - Нажмите **Проверить соединение**.

    Должно отобразиться сообщение «**Соединение установлено**».

!!! warning "Ошибки доступа"

    Если при проверке возникают ошибки доступа (например, `security_exception` или `403 Forbidden`), убедитесь, что:

    - Роль назначена пользователю корректно.
    - Шаблон индекса в роли соответствует префиксу, указанному в `journal.name`.
    - Все необходимые разрешения добавлены в роль.
    - Пользователь имеет доступ к кластеру (разрешения `read` и `write` на уровне кластера).

## Рекомендации по безопасности {: #opensearch_permissions_security }

### Принцип наименьших привилегий {: #opensearch_permissions_security_least_privilege }

Назначайте пользователю **{{ productName }}** только те разрешения, которые необходимы для журналирования транзакций:

- Ограничьте доступ только индексами с префиксом экземпляра ПО.
- Не предоставляйте разрешения на удаление индексов (`indices:admin/delete`), если это не требуется.
- Не используйте роль с полным доступом (`all_access`) для пользователя **{{ productName }}**.

### Ограничение шаблона индексов {: #opensearch_permissions_security_index_pattern }

Используйте конкретный префикс индекса в шаблоне роли вместо широкого шаблона (например, `*`):

- Правильно: `cmw<instanceName>*` — доступ только к индексам экземпляра `<instanceName>`.
- Неправильно: `*` — доступ ко всем индексам кластера.

### Использование TLS {: #opensearch_permissions_security_tls }

Используйте HTTPS/TLS для подключения к {{ openSearchVariants }}:

- Настройте сертификаты в конфигурации экземпляра ПО.
- Для проверки сертификатов временно установите параметр `journal.certificateSkipValidation: false`.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[{{ openSearchVariants }}. Настройка подключения][elasticsearch_connection]_
- _[Конфигурация экземпляра ПО][configuration_files]_
- _[Журнал изменений не записывается. Диагностика и исправление][troubleshooting_history_not_written]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
