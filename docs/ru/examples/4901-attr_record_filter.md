---
title: Атрибут типа «Запись». Настройка фильтра записей для раскрывающегося списка на форме
kbId: 4901
tags:
    - N3
    - атрибуты
    - выражение на N3
    - пример
    - формулы
hide: tags
---

# Атрибут типа «Запись». Настройка фильтра записей для раскрывающегося списка на форме {: #attr_record_filter }

В **{{ productName }}** для выбора значения из другого шаблона записи необходимо использовать атрибут типа «**Запись**». По умолчанию в раскрывающемся списке отображаются все записи, но в некоторых сценариях необходимо показывать только определённые записи.

Для ограничения отображения и выбора записей используйте функционал «**Фильтр**» в настройках конструктора формы, на которую вынесен данный атрибут.

## Сценарий {: #attr_record_filter_scenariy }

При создании заявки на командировку сотруднику нужно выбрать город, в который ему необходимо прибыть. Выбирать из всех городов не совсем удобно — желательно отфильтровать города по выбранной стране командировки.

## Исходные данные {: #attr_record_filter_data_model }

Создайте следующие шаблоны записи и атрибуты:

| Шаблон записи | Атрибуты |
| --- | --- |
| _Страны_ (`countries`) | `title` — текст; `Gorodastrany` — запись с несколькими значениями |
| _Города_ (`cities`) | `title` — текст; `country` — запись из шаблона `countries` |
| _Заявки на командировки_ (`Zayavkinakomandirovku`) | `title` — текст; `request_country` — запись из шаблона `countries`; `request_city` — запись из шаблона `cities` |

## Порядок настройки {: #attr_record_filter_setup }

1. В конструкторе формы шаблона _«Заявки на командировки»_ для поля _«Город»_ (`request_city`) в свойстве «**Фильтр**» выберите один из вариантов фильтрации:

    - **Атрибут** — выберите атрибут: _Страны_ → _Города страны_;
    - **Формула** — введите выражение на языке Comindware Expression Language:

        ```sql
        from a in db->cities where a->country == $request_country select a->id
        ```

    - **N3** — введите выражение на языке N3:

        ```turtle
        @prefix container: <http://comindware.com/ontology/container#>.
        @prefix object: <http://comindware.com/ontology/object#>.
        @prefix math: <http://www.w3.org/2000/10/swap/math#>.
        {
           ("cities" "country") object:findProperty ?citiescountryProp.
           ("Zayavkinakomandirovku" "request_country") object:findProperty ?Zayavkinakomandirovkurequest_countryProp.

           ?item ?Zayavkinakomandirovkurequest_countryProp ?Zayavkinakomandirovkurequest_countryProperty.
           ?value a [object:alias "cities"].
           ?value ?citiescountryProp ?Zayavkinakomandirovkurequest_countryProperty.
        }
        ```

    - **DMN** — выберите источник данных _Города_ и настройте таблицу по образцу:

        _![Пример DMN-запроса](https://kb.comindware.ru/assets/dmn1.png)_

2. Проверьте работу фильтра: выберите сначала страну, затем город. В раскрывающемся списке показываются записи с учётом прав доступа согласно роли пользователя. При отсутствии записей для выбора проверьте права доступа.

!!! note "Примечание"

    С помощью [правил для формы][form_rules] можно настроить динамическое отображение полей для более удобного заполнения.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Правила для формы][form_rules]
- [Атрибут типа «Запись»][attribute_record]
- [Динамические элементы формы. Раскрывающийся список][form_dynamic_elements_dropdown]
- [Язык формул][formula_guide]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
