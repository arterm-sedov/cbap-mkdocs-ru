---
title: 'OpenSearch. Настройка подключения'
kbId: 4678
url: 'https://kb.comindware.ru/article.php?id=4678'
updated: '2026-06-20 18:04:46'
---

# OpenSearch. Настройка подключения

## Введение

**{{ productName }}** использует службу OpenSearch (Elasticsearch) для записи истории всех транзакций, таких как журнал изменений записей и [экземпляров процессов][process_diagram_view_instance], [цепочка событий][logs_event_chain_view] и т. п.

Подключение к OpenSearch (Elasticsearch) автоматически создаётся при [развёртывании][deploy_guide_linux] **{{ productName }}**.

Здесь представлены инструкции по настройке подключения к серверу OpenSearch (Elasticsearch).

## Настройка подключения

1. Перейдите в [список подключений][connections].
2. Дважды нажмите в списке подключение *«ElasticsearchChannel»* или создайте подключение типа «**Системные подключения**» — «**Elasticsearch**».
3. Настройте свойства подключения:

   - **Отключить** — установите этот флажок, чтобы временно деактивировать подключение;
   - **Префикс индекса** — введите *уникальный* префикс записей в БД OpenSearch (Elasticsearch) для данного экземпляра **{{ productName }}**;

     Примечание

     Префикс индекса служит для идентификации записей в БД OpenSearch (Elasticsearch). Если к одному серверу OpenSearch (Elasticsearch) подключается несколько экземпляров {{ productName }}, их префиксы индексов должны отличаться. В противном случае будет нарушена целостность данных в БД OpenSearch (Elasticsearch).

     Допустимый префикс индекса

     В префиксе индекса допускается использовать только строчные латинские буквы и цифры.

     Если в имени префикса будут прописные буквы или спецсимволы (например, дефис), служба журналирования автоматически преобразует их в строчные буквы и символы подчёркивания.
   - **Название** — введите наглядное наименование подключения;
   - **URL подключения для журналирования** — введите адрес сервера OpenSearch (Elasticsearch);
   - **Имя пользователя** — введите логин для входа в OpenSearch (Elasticsearch);
   - **Пароль** — введите пароль для входа в OpenSearch (Elasticsearch).
4. Нажмите кнопку «**Проверить соединение**». Должно отобразиться сообщение «**Соединение установлено**».
5. Сохраните подключение.

_![Настройка подключения к OpenSearch (Elasticsearch)](/platform/v5.0/administration/connections_communication_routes/system_connections/img/elasticsearch_connection_settings.png)_

--8<-- "related_topics_heading.md"

- *[OpenSearch (Elasticsearch). Настройка разрешений][opensearch_permissions]*
- *[Инициализация {{ productName }}][deploy_guide_linux]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
