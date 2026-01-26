---
title: OpenSearch. Настройка подключения
kbId: 4678
---

<!-- статья скрыта, она неактуальна для версии 5.0 от 10.10.2025 -->

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

            {% include-markdown ".snippets/opensearch_prefix_requirements.md" %}

        !!! warning "Допустимый префикс индекса"

            {% include-markdown ".snippets/opensearch_index_naming_requirements.md" %}

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

- _[{{ openSearchVariants }}. Настройка разрешений][opensearch_permissions]_
- _[Инициализация {{ productName }}][deploy_guide_linux_initialize]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
