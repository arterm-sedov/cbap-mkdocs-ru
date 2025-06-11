---
title: OpenSearch. Настройка подключения
kbId: 4678
---

# {{ openSearchVariantsUnquotedNominative }}. Настройка подключения {: #elasticsearch_connection}

## Введение

**{{ productName }}** использует службу {{ openSearchVariants }} для записи истории всех транзакций, таких как журнал изменений записей и [экземпляров процессов][process_diagram_view_instance], [цепочка событий][logs_event_chain_view] и т.&nbsp;п.

Подключение к {{ openSearchVariantsUnquotedDative }} автоматически создаётся при [развёртывании][deploy_guide_linux_initialize] **{{ productName }}**.

Здесь представлены инструкции по настройке подключения к {% if not gostech %}серверу{% endif %} {{ openSearchVariantsUnquotedDative }}.

## Настройка подключения

1. Перейдите в [список подключений][connections].
2. Дважды нажмите в списке подключение {% if not gostech %}_«ElasticsearchChannel»_ или создайте подключение типа «**Системные подключения**» — «**Elasticsearch**»{% else %}к {{ openSearchVariantsUnquotedDative }}{% endif %}.
3. Настройте свойства подключения:

    - **Отключить** — установите этот флажок, чтобы временно деактивировать подключение;
    - **Префикс индекса** — введите _уникальный_ префикс записей в БД {{ openSearchVariantsUnquotedGenitive }} для данного экземпляра **{{ productName }}**;

        !!! note "Примечание"

            Префикс индекса служит для идентификации записей в БД {{ openSearchVariantsUnquotedGenitive }}. Если к {% if not gostech %}одному серверу{% endif %} {{ openSearchVariantsUnquotedDative }} подключается несколько экземпляров **{{ productName }}**, их префиксы индексов должны отличаться. В противном случае будет нарушена целостность данных в БД {{ openSearchVariantsUnquotedGenitive }}.

    - **Название** — введите наглядное наименование подключения;
    - **URL подключения для журналирования** — введите адрес {% if not gostech %}сервера{% endif %} {{ openSearchVariantsUnquotedGenitive }};
    - **Имя пользователя** — введите логин для входа в {{ openSearchVariantsUnquotedAccusative }};
    - **Пароль** — введите пароль для входа в {{ openSearchVariantsUnquotedAccusative }}.

4. Нажмите кнопку «**Проверить соединение**». Должно отобразиться сообщение «**Соединение установлено**».
5. Сохраните подключение.

{% if not gostech %}
_![Настройка подключения к {{ openSearchVariants }}](elasticsearch_connection_settings.png)_
{% endif %}

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Инициализация {{ productName }}][deploy_guide_linux_initialize]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
