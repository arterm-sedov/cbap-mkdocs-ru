---
title: 'Атрибут типа «Запись». Настройка фильтра записей для раскрывающегося списка на форме'
kbId: 4901
url: 'https://kb.comindware.ru/article.php?id=4901'
updated: '2026-06-17 14:09:51'
---

# Атрибут типа «Запись». Настройка фильтра записей для раскрывающегося списка на форме

В **{{ productName }}** для выбора значения из другого шаблона записи необходимо использовать атрибут типа «**Запись**». По умолчанию в раскрывающемся списке отображаются все записи, но в некоторых сценариях необходимо показывать только определённые записи.

Для ограничения отображения и выбора записей используйте функционал «**Фильтр**» в настройках конструктора формы, на которую вынесен данный атрибут.

## Сценарий

При создании заявки на командировку сотруднику нужно выбрать город, в который ему необходимо прибыть. Выбирать из всех городов не совсем удобно — желательно отфильтровать города по выбранной стране командировки.

## Исходные данные

Создайте следующие шаблоны записи и атрибуты:

| Шаблон записи | Атрибуты |
| --- | --- |
| *Страны* (`countries`) | `title` — текст; `Gorodastrany` — запись с несколькими значениями |
| *Города* (`cities`) | `title` — текст; `country` — запись из шаблона `countries` |
| *Заявки на командировки* (`Zayavkinakomandirovku`) | `title` — текст; `request_country` — запись из шаблона `countries`; `request_city` — запись из шаблона `cities` |

## Порядок настройки

1. В конструкторе формы шаблона *«Заявки на командировки»* для поля *«Город»* (`request_city`) в свойстве «**Фильтр**» выберите один из вариантов фильтрации:

   - **Атрибут** — выберите атрибут: *Страны* → *Города страны*;
   - **Формула** — введите выражение на языке Comindware Expression Language:

     ```
     from a in db->cities where a->country == $request_country select a->id
     ```
   - **N3** — введите выражение на языке N3:

     ```
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
   - **DMN** — выберите источник данных *Города* и настройте таблицу по образцу:

     ![Пример DMN-запроса](https://kb.comindware.ru/assets/dmn1.png)

     Пример DMN-запроса
2. Проверьте работу фильтра: выберите сначала страну, затем город. В раскрывающемся списке показываются записи с учётом прав доступа согласно роли пользователя. При отсутствии записей для выбора проверьте права доступа.

Примечание

С помощью [правил для формы][form_rules] можно настроить динамическое отображение полей для более удобного заполнения.

--8<-- "related_topics_heading.md"

- [Правила для формы][form_rules]
- [Атрибут типа «Запись»][attribute_record]
- [Динамические элементы формы. Раскрывающийся список][form_dynamic_elements]
- [Язык формул](https://kb.comindware.ru/category.php?id=880)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
