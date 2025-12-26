---
title: 'Атрибут типа «Документ». Формирование ссылки на файл'
kbId: 5151
tags:
    - N3
    - HTML
    - атрибут
    - выражения
    - вычисления
    - документ
    - загрузка
    - пример
    - ссылки
    - скачивание
    - файлы
    - формулы
hide: tags
---

# Атрибут типа «Документ». Формирование ссылки на файл {: #example_document_get_uri }

## Введение {: #example_document_get_uri_intro }

**{{ productName }}** позволяет прикрепить любые файлы к атрибуту типа «**Документ**».

Атрибут типа «**Документ**» хранит не сами файлы, а ссылки на них.

Эти файлы доступны для скачивания по прямой ссылке без предоставления доступа к атрибуту типа «**Документ**».

Здесь представлен пример настройки текстового атрибута в **формате HTML**, в который помещаются ссылки на файлы, загруженные в атрибут типа «**Документ**», с помощью выражения N3.

!!! question "Структура атрибута типа «Документ»"

    --8<-- "attribute_document_logic.md"
    --8<-- "attribute_document_get_file_n3.md"
    --8<-- "attribute_document_get_file_formula.md"

## Прикладная задача {: #example_document_get_uri_task }

Имеется шаблон с атрибутом типа «**Документ**», к которому прикрепляются различные файлы.

Требуется настроить поле, в котором будут перечислены имена прикреплённых файлов со ссылками для их скачивания.

## Исходные данные {: #example_document_get_uri_source_data }

В шаблоне _«Заявки»_ (системное имя `Заявки`) имеется атрибут _«Вложения»_ со следующими свойствами:

- **Тип: документ**
- **Системное имя:** _Вложения_
- **Хранить несколько значений: флажок установлен**

## Настройка шаблона {: #example_document_get_uri_template_setup }

1. Создайте текстовый атрибут со следующими свойствами:

    - **Название:** _Ссылки для скачивания_
    - **Формат отображения: HTML-текст**

        !!! warning "Важно!"

            Если задать для атрибута другой формат отображения, HTML-теги будут отображаться как обычный текст.

    - **Вычислять автоматически: флажок установлен**
    - **Вычисляемое значение:**
        - **Формула:**

        ``` cs
        # Из атрибута «Вложения» (Вложения) собираем URI и имена всех прикреплённых файлов
        # и соединяем в HTML с разделителем <br/>
        # 'https://host-name' — имя хоста {{ productName }}
        FORMAT(
            "<ul>{0}</u>",
            LIST(
                JOIN(" ", from a in $Вложения select
                    FORMAT("<a href='https://host-name{0}'>{1}</a>", 
                    LIST(a->currentRevision->httpUri, a->currentRevision->revisionFilename)
                    )
                )
            )
        )
        ```

        **или**

        - **N3**

        ``` turtle
        # Импортируем функции для работы
        # с документами и строками
        @prefix object: <http://comindware.com/ontology/object#>.
        @prefix document: <http://comindware.com/ontology/document#>.
        @prefix cmwstring: <http://comindware.com/logics/string#>.
        @prefix string: <http://www.w3.org/2000/10/swap/string#>.
        {
            # Находим атрибут «Вложения» и помещаем в ?filesAttribute
            ("Заявки" "Вложения") object:findProperty ?filesAttribute.
            # Запускаем цикл
            from {
                # Находим содержимое ?filesAttribute в текущей
                # записи и помещаем в ?file
                ?item ?filesAttribute ?file.
                # Получаем текущую ревизию документа и
                # помещаем в ?fileRevision
                ?file document:currentRevision ?fileRevision.
                # Получаем ссылку на файл без имени хоста
                # и помещаем в ?fileUri
                ?fileRevision document:httpUri ?fileUri.
                # Помещаем имя файла в ?fileName
                ?fileRevision document:name ?fileName.
                # Формируем строки с именами файлов и ссылками на них
                # и помещаем в ?formatUri
                # 'https://host-name' — имя хоста {{ productName }}
                ("<li><a href='https://host-name{0}'>{1}</a></li>" ?fileUri ?fileName) string:format ?formatUri.
                }
            # Формируем ?uriList из ?formatUri.
            select ?formatUri -> ?uriList.
            # Формируем из ?uriList маркированный список 
            # и возвращаем его в значение атрибута
            (" " ?uriList) cmwstring:join ?listItems.
            ("<ul>{0}</u>" ?listItems) cmwstring:format ?value.
        }
        ```

2. Поместите на форму атрибут _«Ссылки для скачивания»_.

## Тестирование {: #example_document_get_uri_testing }

1. Создайте запись в шаблоне _«Заявки»_.
2. Прикрепите несколько файлов к атрибуту _«Вложения»_.
3. Сохраните запись.
4. В поле атрибута _«Ссылки для скачивания»_ должен отобразиться маркированный список со ссылками для скачивания прикреплённых файлов.
5. Проверьте, скачиваются ли файлы.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Атрибут типа «Документ»][attribute_document]
- [Атрибут типа «Документ». Скачивание архива с файлами из выбранных строк таблицы и записи][example_document_download_archive_csharp]
- [Атрибут типа «Документ». Скачивание архива с файлами из всех строк таблицы с прикреплением архива к атрибуту][example_document_download_archive_related_records_csharp]
- [Атрибут типа «Документ». Скачивание файлов в папку на сервере][example_document_download_to_server_csharp]
- [Атрибут типа «Документ». Клонирование записи вместе с прикреплёнными файлами][example_document_clone_scenario_n3]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
