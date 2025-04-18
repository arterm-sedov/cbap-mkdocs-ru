---
kbTitle: Атрибут типа «Документ». Клонирование записи вместе с прикреплёнными файлами с помощью сценария по нажатию кнопки
title: Атрибут типа «Документ». Клонирование записи с прикреплёнными файлами
kbId: 4883
---

# Атрибут типа «Документ». Клонирование записи с прикреплёнными файлами {: #example_document_clone_scenario_n3 }

## Введение

Здесь представлены инструкции по настройке сценария для клонирования записи вместе с файлами, прикреплёнными к [атрибуту типа «**Документ**»][attribute_document].

Сценарий для копирования файлов, прикреплённых к атрибуту типа «**Изображение**», можно настроить аналогичным образом.

См. также примеры работы с атрибутом типа «**Документ**»:

- _[Скачивание архива с файлами из всех строк таблицы с прикреплением архива к атрибуту][example_document_download_archive_related_records_csharp]_
- _[Скачивание архива с файлами из выбранных строк таблицы или одной записи][example_document_download_archive_csharp]_
- _[Скачивание файлов в папку на сервере][example_document_download_to_server_csharp]_

!!! question "Структура атрибута типа «Документ»"

    --8<-- "attribute_document_logic.md"

!!! tip "Извлечение файлов из атрибута типа «Документ» с помощью N3"

    --8<-- "attribute_document_get_file_n3.md"

!!! tip "Добавление файлов в атрибут типа «Документ» с помощью N3"

    --8<-- "attribute_document_add_file_n3.md"
    {% include-markdown ".snippets/pdfEndOfBlockHack.md" %}

## Прикладная задача

Необходимо настроить кнопку, которая будет создавать дубликат текущей записи и прикреплять к ней дубликаты всех файлов, прикреплённых к исходной записи. Если к исходной записи не прикреплен ни один файл, то создавать её дубликат не требуется.

## Исходные данные

1. Создайте приложение _«Документооборот»_.
2. В приложении _«Документооборот»_ создайте шаблон записи _«Пакеты документов»_ с системным именем `DocumentPacks` и следующими атрибутами:

    | Название атрибута                | Системное имя      | Свойства              |
    | -------------------------------- | ------------------ | --------------------- |
    | _Наименование пакета документов_ | `DocumentPackName` | **Тип данных: текст** |
    | _Файлы документов_               | `AttachedFiles`    | <ul><li>**Тип данных: документ**</li><li> **Хранить несколько значений:** флажок установлен</li></ul> |

3. Поместите атрибуты _«Наименование пакета документов»_ и _«Файлы документов»_ на основную форму шаблона _«Пакеты документов»_.

## Настройка кнопки «Копировать пакет документов»

1. Отройте шаблон записи _«Пакеты документов»._
2. Перейдите на вкладку «**Кнопки**».
3. Создайте кнопку «**Копировать пакет документов**»:

    - **Контекст операции: запись**
    - **Операция: вызвать событие «Нажата кнопка»**
    - **Результат выполнения: навигация**
    - **Переход к: предыдущая страница**

4. Поместите кнопку _«Копировать документ»_ на основную форму шаблона _«Пакеты документов»._

## Настройка сценария «Копирование пакета документов»

1. На странице [администрирования приложения][apps] выберите пункт «**Сценарии**».
2. Создайте сценарий:

    - **Название**: _Копирование документа_
    - **Системное имя**: заполняется автоматически.
    - **Контекст выполнения**: **от имени системы**

3. Отобразится конструктор сценария.
4. Нажмите заголовок события «**Нажатие кнопки**».
5. Настройте свойства события:

    - **Тип: Нажатие кнопки**
    - **Контекстный шаблон:** _Пакеты документов_
    - **Кнопка:** _Копировать пакет документов_

6. После действия «**Нажата кнопка**» создайте и настройте действие «**Изменить значения переменных**»:

    - **Операция со значениями переменных: заменить**
    - **Переменная:** _originalRecord_
    - Настройте таблицу дочерних переменных.

    | Имя переменной {: width=50% } | Значение        |
    | -------------- | --------------- |
    | _id_           | **Атрибут: ID** |

    !!! warning "Бизнес-логика"

        Это действие будет сохранять в переменную `originalRecord.id` идентификатор исходной записи в шаблоне _«Пакеты документов»_ для использования в последующих действиях.

7. После события «**Изменить значения переменных**» создайте и настройте действие «**Выполнить по условиям**» следующим образом:

    - Название условия: _Файл прикреплён_
    - **Выражение: N3**

    ``` turtle
    # Импортируем функции для работы
    # с данными текущего сеанса, переменными и записями 
    @prefix variable: <http://comindware.com/ontology/session/variable#>.
    @prefix session: <http://comindware.com/ontology/session#>.
    @prefix object: <http://comindware.com/ontology/object#>.
    {
        #Находим атрибут AttachedFiles (Файлы документов)
        # в шаблоне DocumentPacks (Пакеты документов) и помещаем ID атрибута
        # в локальную переменную ?AttachedFilesAttribute
        ("DocumentPacks" "AttachedFiles") object:findProperty ?AttachedFilesAttribute.
        #Находим переменную originalRecord из предыдущего действия
        #и помещаем её в локальную переменную ?originalRecordVariable
        session:context variable:originalRecord ?originalRecordVariable.
        #Находим переменную originalRecord.id с ID исходной записи
        # в шаблоне «Пакеты документов» и помещаем ID записи
        # в локальную переменную ?docPackRecordId
        ?originalRecordVariable variable:id ?docPackRecordId.
        # Считываем значение атрибута «Файлы документов» в исходной записи
        ?docPackRecordId ?AttachedFilesAttribute ?.
        # Возвращаем true, если к атрибуту «Файлы документов»
        # прикреплён хотя бы один файл
        true -> ?value.
    }
    ```

    !!! warning "Бизнес-логика"

        Это действие будет инициировать вложенные в него действия, если в текущей записи _«Пакеты документов»_ к атрибуту _«Файлы документов»_ (с системным именем `AttachedFiles`) прикреплён хотя бы один файл.

8. Внутри действия «**Выполнить по условиям**» создайте действие «**Создать запись**» с **целевым шаблоном** _«Пакеты документов»_.

    !!! warning "Бизнес-логика"

        Это действие создаёт пустую запись в шаблоне _«Пакеты документов»_, в которую последующие действия скопируют значения атрибутов _«Наименование пакета документов»_ и _«Файлы документов»_.

9. Внутри действия «**Создать запись**» создайте и настройте действие «**Изменить значение атрибутов**» следующим образом:

    - **Атрибут:** _Наименование пакета документов_
    - **Операция со значениями: заменить**
    - **Значение:****N3**

    ``` turtle
    # Импортируем функции для работы
    # с данными текущего сеанса, переменными и записями 
    @prefix variable: <http://comindware.com/ontology/session/variable#>.
    @prefix session: <http://comindware.com/ontology/session#>.
    @prefix object: <http://comindware.com/ontology/object#>.
    {
        # Находим атрибут DocumentPackName (Наименование пакета документов)
        # в шаблоне DocumentPacks (Пакеты документов)
        # и помещаем ID атрибута в локальную переменную ?PackNameAttribute
        ("DocumentPacks" "DocumentPackName") object:findProperty ?PackNameAttribute.
        # Помещаем переменную originalRecord
        # в локальную переменную ?originalRecordVariable
        session:context variable:originalRecord ?originalRecordVariable.
        # Помещаем ID исходной записи в шаблоне «Пакеты документов»
        # в локальную переменную docPackRecordId
        ?originalRecordVariable variable:id ?docPackRecordId.
        # Возвращаем значение атрибута «Наименование пакета документов» из исходной записи
        ?docPackRecordId ?PackNameAttribute ?value.
    }
    ```

    !!! warning "Бизнес-логика"

        Это действие копирует значение атрибута _«Наименование пакета документов»_ из исходной записи в новую.

10. После действия «**Изменить значение атрибутов**» внутри действия «**Создать запись**» создайте и настройте действие «**Повторять по количеству объектов**» следующим образом:

    - **Переменная:** _document_
    - **Атрибут или выражение для поиска объектов: формула**

    ``` turtle
    # Импортируем функции для работы
    # с данными текущего сеанса, переменными и записями 
    @prefix variable: <http://comindware.com/ontology/session/variable#>.
    @prefix session: <http://comindware.com/ontology/session#>.
    @prefix object: <http://comindware.com/ontology/object#>.
    {
        #Находим атрибут AttachedFiles (Файлы документов)
        # в шаблоне DocumentPacks (Пакеты документов)
        # и помещаем ID атрибута в локальную переменную ?AttachedFilesAttribute  
        ("DocumentPacks" "AttachedFiles") object:findProperty ?AttachedFilesAttribute.
        # Помещаем переменную originalRecord
        # в локальную переменную originalRecordVariable
        session:context variable:originalRecord ?originalRecordVariable.
        # Помещаем ID исходной записи в шаблоне «Пакеты документов»
        # в локальную переменную docPackRecordId
        ?originalRecordVariable variable:id ?docPackRecordId.
        # Возвращаем значение атрибута «Файлы документов» из исходной записи
        ?docPackRecordId ?AttachedFilesAttribute ?value.
    }
    ```

    !!! warning "Бизнес-логика"

        На каждой итерации цикла в переменную `document` будет помещаться ссылка на запись в _системном_ **шаблоне документа** с файлом, прикреплённым к атрибуту _«Файлы документов»_ из исходной записи.

11.  Внутри действия «**Повторять по количеству объектов**» создайте и настройте действие «**Изменить значение атрибутов**» следующим образом:

    - **Атрибут:** _Файлы документов_
    - **Операция со значениями: добавить**
    - **Значение: N3**
    
    ``` turtle
    # Импортируем функции для работы
    # с документами и данными текущего сеанса
    @prefix document: <http://comindware.com/ontology/document#>.
    @prefix variable: <http://comindware.com/ontology/session/variable#>.
    @prefix session: <http://comindware.com/ontology/session#>.
    {
        # Помещаем переменную document 
        # из действия «Повторять по количеству объектов»
        # в локальную переменную ?doc
        session:context variable:document ?doc.
        # Помещаем ссылку на прикреплённый файл
        # в локальную переменную ?revision
        ?doc document:currentRevision ?revision.
        # Помещаем содержимое файла в формате Base64
        # в локальную переменную ?content
        ?revision document:content ?content.
        # Помещаем имя файла в локальную переменную ?filename
        ?doc document:title ?filename.
        #Собирем новый файл из имени и содержимого,
        # сохраняем его в папку Streams,
        #и возвращаем ID нового документа с прикреплённым файлом
        (?content ?filename) document:attach ?value.
    }
    ```

    !!! warning "Бизнес-логика"

        Это действие будет прикреплять к атрибуту _«Файлы документов»_ в новой записи дубликат файла, прикреплённого к  атрибуту _«Файлы документов»_ из исходной записи.

_![Настроенный сценарий для дублирования записи вместе с прикреплёнными к ней файлами](img/document_clone_scenario_n3_scenario.png)_

## Тестирование работы сценария

1. Откройте шаблон _«Пакеты документов»_ и нажмите кнопку «**Перейти к экземплярам**».
2. Отобразится список записей в шаблоне _«Пакеты документов»._
3. Создайте запись и заполните форму:

    - Введите _«Наименование пакета документов»_.
    - Прикрепите к полю _«Файлы документов»_ несколько файлов.

4. Сохраните запись.
5. Нажмите кнопку _«Копировать пакет документов»._
6. Должен снова отобразиться список записей в шаблоне _«Пакеты документов»._
7. В списке записей должна появиться новая запись — дубликат исходной.
8. Откройте новую запись и убедитесь, что содержимое полей _«Наименование пакета документов»_ и _«Файлы документов»_ совпадает с содержимым исходной записи.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Пути и содержимое папок экземпляра ПО][paths]_
- _[Атрибут типа «Документ»][attribute_document]_
- _[Кнопки. Определение, настройка, удаление][buttons]_
- _[Событие и действия сценария. Определения, типы, свойства, настройка][scenario_elements]_
- _[Атрибут типа «Документ». Скачивание архива с файлами из всех строк таблицы с прикреплением архива к атрибуту][example_document_download_archive_related_records_csharp]_
- _[Атрибут типа «Документ». Скачивание файлов в папку на сервере][example_document_download_to_server_csharp]_
- _[Атрибут типа «Документ». Скачивание архива с файлами из выбранных строк таблицы и записи][example_document_download_archive_csharp]_
- _[Атрибут типа «Документ». Клонирование записи вместе с прикреплёнными файлами][example_document_clone_scenario_n3]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
