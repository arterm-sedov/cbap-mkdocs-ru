---
title: 'Атрибуты типа «Изображение» и «Документ». Вывод изображения на форму записи'
kbTitle: 'Атрибуты типа «Изображение» и «Документ». Вывод изображения на форме'
kbId: 4975
tags:
    - N3
    - HTML-текст
    - атрибут типа «Документ»
    - атрибут типа «Изображение»
    - галерея
    - документ
    - изображение
    - изображения
    - отображение
    - пример
    - тройки
    - триплеты
    - формулы
    - фотографии
hide: tags
---

# Атрибуты типа «Изображение» и «Документ». Вывод изображения на форме {: #example_image_gallery_on_form }

## Введение {: #example_image_gallery_on_form_intro }

В **{{ productName }}** можно загрузить изображения, прикрепив их к атрибуту типа «**Изображение**» или «**Документ**».

При этом изображения, прикреплённые к этим атрибутам отображаются на формах только в режиме предпросмотра и не растягиваются на весь размер формы.

Чтобы вывести одно или несколько изображений на форму, задав произвольное HTML-форматирование, можно воспользоваться текстовым атрибутом, задав для него формат отображения «**HTML-текст**».

Здесь представлены настройки по формированию галереи изображений на форме из атрибута типа «**Изображение**» или «**Документ**».

!!! question "Структура атрибута типа «Изображение»"

    --8<-- "attribute_image_logic.md"
    --8<-- "attribute_image_get_file_n3.md"

!!! question "Структура атрибута типа «Документ»"

    --8<-- "attribute_document_logic.md"
    --8<-- "attribute_document_get_file_n3.md"
    --8<-- "attribute_document_get_file_formula.md"

## Прикладная задача {: #example_image_gallery_on_form_use_case .pageBreakBefore }

Требуется вывести на форму галерею изображений, которые хранятся в атрибуте типа «**Изображение**» или «**Документ**».

## Исходные данные {: #example_image_gallery_on_form_initial_data }

В шаблоне _«Карточки товаров»_ (системное имя `ProductCards`) имеются две формы:

- **основная**, на которой данные заполняют сотрудники;
- _Клиентская форма_, которая отображается для клиентов.

## Порядок настройки для атрибута типа «Изображение» {: #example_image_gallery_on_form_image_setup .pageBreakBefore }

1. В шаблоне _«Карточки товаров»_ создайте атрибут _«Изображения»_ со следующими свойствами:

    - **Системное имя:** _Изображения_
    - **Тип данных: изображение**
    - **Хранить несколько значений: флажок установлен**

2. Создайте атрибут _«Галерея»_ со следующими свойствами:

    - **Системное имя:** _Галерея_
    - **Тип данных: текст**
    - **Формат отображения: HTML-текст**
  
        !!! warning "Важно!"

            Если задать для атрибута другой формат отображения, HTML-теги будут отображаться как обычный текст.

    - **Вычислять автоматически:** флажок установлен
    - **Выражение для вычислений:**
        - **Формула**

            ``` sql
            # Из атрибута «Изображения» собираем изображения
            # и соединяем в HTML с разделителем <br/>
            # 'https://host-name' — имя хоста {{ productName }}
            JOIN("<br/>", from a in $Изображения select
                FORMAT("<img src='https://your-host{0}'>", 
                LIST(a->uri)
                )
            )
            ```

        **или**

        - **N3**

            ``` turtle
            # Импортируем функции для работы
            # с изображениями и строками
            @prefix object: <http://comindware.com/ontology/object#>.
            @prefix image: <http://comindware.com/ontology/image#>.
            @prefix cmwstring: <http://comindware.com/logics/string#>.
            @prefix string: <http://www.w3.org/2000/10/swap/string#>.
            {
                # Находим атрибут «Изображения» и помещаем в ?imagesAttribute
                ("ProductCards" "Изображения") object:findProperty ?imagesAttribute.
                # Запускаем цикл
                from {
                    # Находим содержимое ?imagesAttribute в текущей
                    # записи и помещаем в ?image
                    ?item ?imagesAttribute ?image.
                    # Получаем ссылку на файл без имени хоста
                    # и помещаем в ?imageUri
                    ?image image:uri ?imageUri.
                    # Формируем HTML-строки c изображениями и помещаем в ?formatUri
                    # 'https://host-name' — имя хоста {{ productName }}
                    ("<img src='https://host-name{0}'>" ?imageUri) string:format ?formatUri.
                    }
                # Формируем лист HTML-строк ?uriList из ?formatUri.
                select ?formatUri -> ?uriList.
                # Формируем из ?uriList одну большую строку
                # с разделителем <br/> (перенос строки)
                # и возвращаем её в значение атрибута
                ("<br/>" ?uriList) cmwstring:join ?value.
            }
            ```

3. Поместите атрибут _«Изображения»_ на **основную форму**.
4. Поместите атрибут _«Галерея»_ на форму _«Клиентская форма»_.

### Тестирование для атрибута типа «Изображение» {: #example_image_gallery_on_form_image_testing }

1. Создайте запись в шаблоне _«Карточки товаров»_.
2. Сохраните запись.
3. Прикрепите изображения к атрибуту _«Изображения»_.
4. С помощью селектора <i class="fa-light fa-angle-down"></i> перейдите к форме _«Клиентская форма»_.
5. На форме должны отобразиться прикреплённые изображения в виде галереи.

## Порядок настройки для атрибута типа «Документ» {: #example_image_gallery_on_form_document_setup .pageBreakBefore }

1. В шаблоне _«Карточки товаров»_ добавьте атрибут _«Фотографии»_ со следующими свойствами:

    - **Системное имя:** _Фотографии_
    - **Тип данных: документ**
    - **Хранить несколько значений:** флажок установлен

2. Создайте атрибут _«Отображение фотографий на форме»_ со следующими свойствами:

    - **Системное имя:** _Фотогалерея_
    - **Тип данных: текст**
    - **Формат отображения: HTML-текст**

        !!! warning "Важно!"

            Если задать для атрибута другой формат отображения, HTML-теги будут отображаться как обычный текст.

    - **Вычислять автоматически:** флажок установлен
    - **Выражение для вычислений:**
        - **Формула**

            ``` sql
            # Из атрибута «Фотографии» собираем изображения
            # и соединяем в HTML с разделителем <br/>
            # 'https://host-name' — имя хоста {{ productName }}
            JOIN("<br/>", from a in $Фотографии select
                FORMAT("<img src='https://your-host{0}'/>", 
                LIST(a->currentRevision->httpUri)
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
                # Находим атрибут «Изображения» (Фотографии) и помещаем в ?photosAttribute
                ("ProductCards" "Фотографии") object:findProperty ?photosAttribute.
                # Запускаем цикл
                from {
                    # Находим содержимое ?photosAttribute в текущей
                    # записи и помещаем в ?photos
                    ?item ?photosAttribute ?photos.
                    # Получаем текущую ревизию документа и
                    # помещаем в ?fileRevision
                    ?photos document:currentRevision ?fileRevision.
                    # Получаем ссылку на файл без имени хоста
                    # и помещаем в ?fileUri
                    ?fileRevision document:httpUri ?fileUri.
                    # Формируем HTML-строки c изображениями и помещаем в ?formatUri
                    # 'https://host-name' — имя хоста {{ productName }}
                    ("<img src='https://host-name{0}'>" ?fileUri) string:format ?formatUri.
                    }
                # Формируем лист HTML-строк ?uriList из ?formatUri.
                select ?formatUri -> ?uriList.
                # Формируем из ?uriList одну большую строку
                # с разделителем <br/> (перенос строки)
                # и возвращаем её в значение атрибута
                ("<br/>" ?uriList) cmwstring:join ?value.
            }
            ```

3. Поместите атрибут _«Фотографии»_ на **основную форму**.
4. Поместите атрибут _«Отображение фотографий на форме»_ на форму _«Клиентская форма»_.

### Тестирование для атрибута типа «Документ» {: #example_image_gallery_on_form_document_testing }

1. Создайте запись в шаблоне _«Карточки товаров»_.
2. Прикрепите изображения к атрибуту _«Фотографии»_.
3. Сохраните запись.
4. С помощью селектора <i class="fa-light fa-angle-down"></i> перейдите к форме _«Клиентская форма»_.
5. На форме должны отобразиться прикреплённые изображения в виде галереи.

## Примеры стилизации изображений {: .pageBreakBefore }

!!! tip "Форматирование с помощью CSS"

    Для форматирования изображения можно использовать следующие свойства CSS:
    
    - `max-width` и `max-height` для ограничения размера;
    - `border-radius` для скругления углов;
    - `border` для рамки;
    - `margin` для отступов вокруг изображения.

- Ограничение размера до 300x300 пикселей

    ``` sql
    # 
    JOIN("<br/>", from a in $Фотографии select
        FORMAT("<img src='https://host-name{0}' style='max-width: 300px; max-height: 300px;' alt='Описание изображения'/>",
        LIST(a->currentRevision->httpUri)
        )
    )
    ```

- Обрезка по размеру 200x200&nbsp;пикселей с обрезкой и скруглением углов радиусом 8&nbsp;пикселей:

    ``` sql
    # Отображение изображений 
    JOIN("<br/>", from a in $Фотографии select
        FORMAT("<div style='display: inline-block; margin: 5px;'><img src='https://host-name{0}' width='200' height='200' style='object-fit: cover; border-radius: 8px;' alt='Описание изображения'/></div>",
        LIST(a->currentRevision->httpUri)
        )
    )
    ```

- Автоматическое масштабирование и рамка со скругленными углами радиусом 4&nbsp;пикселя:

    ``` sql
    # Адаптивное отображение 
    JOIN("<br/>", from a in $Фотографии select
        FORMAT("<div style='text-align: center; margin: 10px;'><img src='https://host-name{0}' style='max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px;' alt='Описание изображения'/></div>",
        LIST(a->currentRevision->httpUri)
        )
    )
    ```

- Проверка наличия файлов изображений:

    ``` sql
    IF(ISBLANK($Фотографии), "<p style='color: #999; font-style: italic;'>Изображения не загружены</p>",
        JOIN("<br/>", from a in $Фотографии select
            FORMAT("<img src='https://host-name{0}' style='max-width: 250px; max-height: 250px; margin: 5px;' alt='Описание изображения'/>",
            LIST(a->currentRevision->httpUri)
            )
        )
    )
    ```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Атрибут типа «Документ»][attribute_document]_
- _[Атрибут типа «Изображение»][attribute_image]_
- _[Атрибут «Документ». Формирование ссылки на файл][document_uri]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
