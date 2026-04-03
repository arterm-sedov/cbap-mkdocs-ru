---
title: 'OpenSearch. Настройка разрешений'
kbId: 5152
url: 'https://kb.comindware.ru/article.php?id=5152'
updated: '2026-01-27 18:41:10'
---

# OpenSearch. Настройка разрешений

## Введение

**Comindware Platform** использует службу OpenSearch (Elasticsearch) для журналирования транзакций (истории изменений записей и [экземпляров процессов](https://kb.comindware.ru/article.php?id=4723), [цепочки событий](https://kb.comindware.ru/article.php?id=4673#logs_event_chain_view) и т. п.).

Для корректной работы журнала транзакций пользователь **Comindware Platform** в OpenSearch (Elasticsearch) должен иметь необходимые разрешения на создание индексов, запись и чтение данных.

Здесь представлены инструкции по настройке разрешений для пользователя **Comindware Platform** в OpenSearch (Elasticsearch).

Служебный пользователь в OpenSearch (Elasticsearch)

- В конфигурации экземпляра ПО необходимо указать адрес сервера и уникальный префикс индексов OpenSearch (Elasticsearch). Индекс префикса служит для идентификации данных экземпляра ПО на сервере журналирования транзакций. Поэтому во избежание конфликтов данных для каждого экземпляра ПО следует указывать собственный префикс индекса.
- В конфигурации сервера OpenSearch (Elasticsearch) необходимо создать одного пользователя для **Comindware Platform**.
- При инициализации экземпляра ПО или в конфигурации экземпляра необходимо указать пользователя **Comindware Platform**, используемого сервером OpenSearch (Elasticsearch).
- Экземпляр ПО будет взаимодействовать с OpenSearch (Elasticsearch) под указанным пользователем и создавать, наполнять и читать индексы с заданным префиксом.

## Обзор необходимых разрешений

Для корректной работы журнала транзакций пользователь **Comindware Platform** в OpenSearch (Elasticsearch) должен иметь перечисленные ниже разрешения.

### Разрешения на управление индексами

Обеспечивают управление структурой хранилища журналов: создание индексов и обновление сопоставления полей.

| Разрешение | Описание | Применение в Comindware Platform |
| --- | --- | --- |
| `indices:admin/create` | Создание новых индексов | Создание индексов при первом запуске |
| `indices:admin/data_stream/create` | Создание потоков данных | Автоматизированное конвейерное журналирование транзакций |
| `indices:admin/mapping/put` | Обновление сопоставлений индекса | Изменение структуры данных (например, при обновлении версии Comindware Platform) |

### Разрешения на чтение данных

Обеспечивают доступ для чтения и поиска записей в журнале транзакций.

| Разрешение | Описание | Применение в Comindware Platform |
| --- | --- | --- |
| `indices:data/read/get` | Получение данных | Просмотр конкретной записи о транзакции |
| `indices:data/read/search` | Поиск в индексах | Базовый поиск |
| `indices:data/read/search*` | Все варианты поиска | Агрегации, сложные запросы для фильтрации и анализа |
| `indices:data/read/search/template` | Использование сохранённых шаблонов | Повторные поисковые запросы |

### Разрешения Point-in-Time

Обеспечивают создание консистентных снимков при обработке больших объёмов данных.

| Разрешение | Описание | Применение в Comindware Platform |
| --- | --- | --- |
| `indices:data/read/point_in_time/create` | Создание сеанса PIT | Для консистентной работы с большими наборами данных |
| `indices:data/read/point_in_time/readall` | Чтение всех сеансов PIT | Управление активными сеансами Point-in-Time |

### Разрешения на запись данных

Обеспечивают запись и обновление записей о транзакциях в журнале.

| Разрешение | Описание | Применение в Comindware Platform |
| --- | --- | --- |
| `indices:data/write/index` | Индексирование транзакций | Основная операция записи транзакций в журнал |
| `indices:data/write/update` | Обновление существующих транзакций | Коррекция ошибочных записей |
| `indices:data/write/update/byquery` | Массовое обновление по условию | Батч-операции для исправления данных |

### Глобальные разрешения кластера

Обеспечивают базовые возможности работы с индексами на уровне кластера.

| Разрешение | Описание | Применение в Comindware Platform |
| --- | --- | --- |
| `read` | Глобальное чтение на уровне кластера | Базовый доступ ко всем операциям чтения |
| `write` | Глобальная запись на уровне кластера | Базовый доступ ко всем операциям записи |

## Настройка роли для Comindware Platform

Для пользователя **Comindware Platform** рекомендуется создать отдельную роль с необходимыми разрешениями. Роль должна предоставлять доступ только к индексам с префиксом, указанным в параметре `journal.name` конфигурации экземпляра ПО.

### Создание роли через REST API

1. Создайте роль с необходимыми разрешениями:

   ```
   curl -X PUT \\
     --user <cmwJournalUserName>:<safePassword> \\
     --cacert /path/to/root.crt \\
     -H "Content-Type: application/json" \\
     https://<openSearchHost>:<port>/_plugins/_security/api/roles/<cmwJournalRole> \\
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
   - `<openSearchHost>:<port>` — адрес сервера OpenSearch (Elasticsearch);
   - `/path/to/root.crt` — путь к сертификату корневого центра сертификации (если используется TLS).

   Примечание

   Если используется несколько экземпляров **Comindware Platform** с разными префиксами индексов, создайте отдельную роль для каждого префикса или используйте шаблон индекса, охватывающий все необходимые префиксы.
2. Создайте пользователя и назначьте ему роль:

   ```
   curl -X PUT \\
     --user <cmwJournalUserName>:<safePassword> \\
     --cacert /path/to/root.crt \\
     -H "Content-Type: application/json" \\
     https://<openSearchHost>:<port>/_plugins/_security/api/internalusers/<cmwJournalUserName> \\
     -d '{
       "password": "<safePassword>",
       "opendistro_security_roles": ["<cmwJournalRole>"],
       "backend_roles": [],
       "attributes": {}
     }'
   ```
3. Укажите созданного пользователя в конфигурации экземпляра ПО:

   Пример конфигурации подключения к OpenSearch (Elasticsearch)```
   # Адрес службы журналирования OpenSearch (Elasticsearch).
   journal.server: https://<openSearchHost>:<port>
   # Префикс индекса службы журналирования OpenSearch (Elasticsearch).
   # Индекс службы журналирования OpenSearch (Elasticsearch).
   journal.name: <prefix>
   # Имя пользователя службы журналирования
   journal.username: <cmwJournalUserName>
   # Пароль службы журналирования
   journal.password: <safePassword>
   ```

   Примечание

   Префикс индекса служит для идентификации записей в БД OpenSearch (Elasticsearch). Если к одному серверу OpenSearch (Elasticsearch) подключается несколько экземпляров Comindware Platform, их префиксы индексов должны отличаться. В противном случае будет нарушена целостность данных в БД OpenSearch (Elasticsearch).

   Допустимый префикс индекса

   В префиксе индекса допускается использовать только строчные латинские буквы и цифры.

   Если в имени префикса будут прописные буквы или спецсимволы (например, дефис), служба журналирования автоматически преобразует их в строчные буквы и символы подчёркивания.

### Создание роли через OpenSearch Dashboards

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

## Проверка конфигурации

После настройки разрешений проверьте, что пользователь **Comindware Platform** может выполнять необходимые операции для работы журнала транзакций:

1. Проверьте доступ к поиску в индексах:

   ```
   curl -X GET \\
     --user <cmwJournalUserName>:<safePassword> \\
     --cacert /path/to/root.crt \\
     https://<openSearchHost>:<port>/<prefix>*/_search?size=10
   ```
2. Проверьте возможность создания индекса:

   ```
   curl -X PUT \\
     --user <userName>:<safePassword> \\
     --cacert /path/to/root.crt \\
     https://<openSearchHost>:<port>/<prefix_test_index>
   ```

   Очистка тестового индекса

   Тестовый индекс `<prefix_test_index>` останется после проверки, так как удаление индексов требует разрешения `indices:admin/delete`, которое не входит в список необходимых разрешений для работы журнала транзакций.

   Для удаления тестового индекса выполните команду **от имени администратора OpenSearch (Elasticsearch)**:

   ```
   curl -X DELETE \\
     --user <adminUser>:<safePassword> \\
     --cacert /path/to/root.crt \\
     https://<openSearchHost>:<port>/<prefix_test_index>
   ```

Ошибки доступа

Если при проверке возникают ошибки доступа (например, `security_exception` или `403 Forbidden`), убедитесь, что:

- Роль назначена пользователю корректно.
- Шаблон индекса в роли соответствует префиксу, указанному в `journal.name`.
- Все необходимые разрешения добавлены в роль.
- Пользователь имеет доступ к кластеру (разрешения `read` и `write` на уровне кластера).

## Рекомендации по безопасности

### Принцип наименьших привилегий

Назначайте пользователю **Comindware Platform** только те разрешения, которые необходимы для журналирования транзакций:

- Ограничьте доступ только индексами с префиксом экземпляра ПО.
- Не предоставляйте разрешения на удаление индексов (`indices:admin/delete`), если это не требуется.
- Не используйте роль с полным доступом (`all_access`) для пользователя **Comindware Platform**, если это не требуется.

### Ограничение шаблона индексов

Используйте конкретный префикс индекса в шаблоне роли вместо широкого шаблона (например, `*`):

- Правильно: `cmw<instanceName>*` — доступ только к индексам экземпляра `<instanceName>`.
- Неправильно: `*` — доступ ко всем индексам.

### Использование TLS

Используйте HTTPS/TLS для подключения к OpenSearch (Elasticsearch):

- Настройте сертификаты в конфигурации экземпляра ПО.
- Для проверки сертификатов временно установите параметр `journal.certificateSkipValidation: false`.

## Связанные статьи

- [OpenSearch (Elasticsearch). Настройка подключения](https://kb.comindware.ru/article.php?id=4678)
- [Конфигурация экземпляра ПО](https://kb.comindware.ru/article.php?id=5067)
- [Журнал изменений не записывается. Диагностика и исправление](../../../../troubleshooting/history_not_logged.html#troubleshooting_history_not_written)