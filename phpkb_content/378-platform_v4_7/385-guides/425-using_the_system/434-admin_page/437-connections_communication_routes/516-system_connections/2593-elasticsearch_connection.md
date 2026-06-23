---
title: 'Elasticsearch. Настройка подключения'
kbId: 2593
url: 'https://kb.comindware.ru/article.php?id=2593'
updated: '2024-10-31 13:45:07'
---

# Elasticsearch. Настройка подключения

## Введение

**{{ productName }}** использует службу Elasticsearch для записи истории всех транзакций, таких как журнал изменений записей и [экземпляров процессов](https://kb.comindware.ru/article.php?id=2355), [цепочка событий](https://kb.comindware.ru/article.php?id=2180#logs_event_chain_view) и т. п.

Подключение к Elasticsearch автоматически создаётся при [развёртывании](https://kb.comindware.ru/article.php?id=2344#deploy_guide_linux_initialize) **{{ productName }}**.

В данной статье представлены инструкции по настройке подключения к серверу Elasticsearch.

## Настройка подключения

1. Перейдите в [список подключений](https://kb.comindware.ru/article.php?id=2205).
2. Дважды нажмите в списке подключение *«ElasticsearchChannel»* или создайте подключение типа «**Системные подключения**» — «**Elasticsearch**».
3. Настройте свойства подключения:

   - **Отключить** — установите этот флажок, чтобы временно деактивировать подключение;
   - **Префикс индекса** — введите *уникальный* префикс записей в БД Elasticsearch для данного экземпляра **{{ productName }}**;

     Примечание

     Префикс индекса служит для идентификации записей в БД Elasticsearch. Если к одному серверу Elasticsearch подключается несколько экземпляров **{{ productName }}**, их префиксы индексов должны отличаться. В противном случае будет нарушена целостность данных в БД Elasticsearch.
   - **Название** — введите наглядное наименование подключения;
   - **URL подключения для журналирования** — введите адрес сервера Elasticsearch;
   - **Имя пользователя** — введите логин для входа на сервер Elasticsearch;
   - **Пароль** — введите пароль для входа на сервер Elasticsearch.
4. Нажмите кнопку «**Проверить соединение**». Должно отобразиться сообщение «**Соединение установлено**».
5. Сохраните подключение.

_![Настройка подключения к Elasticsearch](https://kb.comindware.ru/assets/elasticsearch_connection_settings.png)_

--8<-- "related_topics_heading.md"

**[Инициализация {{ productName }}](https://kb.comindware.ru/article.php?id=2344#deploy_guide_linux_initialize)**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
