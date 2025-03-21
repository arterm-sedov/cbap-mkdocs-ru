---
title: Атрибут типа «Документ». Копирование записи вместе с прикреплённым документом с помощью сценария по нажатию кнопки
kbId: 2608
---

# Атрибут типа «Документ». Копирование записи вместе с прикреплённым документом с помощью сценария по нажатию кнопки

## Введение

В этой статье представлены инструкции по настройке сценария для копирования записи, в которой имеется [атрибут типа «**Документ**»][attribute_document], вместе с файлами, прикреплёнными к этому атрибуту.

Сценарий для копирования файлов, прикреплённых к атрибуту типа «**Изображение**», настраивается аналогичным образом.

### Определения

- Атрибут типа «**Документ**» хранит одну или несколько ссылок на записи (**документы**) в *системном* **шаблоне документа**, к которым прикрепляются файлы.
- В **шаблоне документа** имеется атрибут **currentRevision**, который хранит ссылку на запись (**ревизию**) в *системном* **шаблоне ревизии**.
- В **шаблоне ревизии** имеются атрибуты **title** и **content**, которые хранят имя файла и ссылку на файл, физически хранящийся в папке `Streams` на сервере **{{ productName }}**.
- Для того чтобы прикрепить к атрибуту типа «**Документ**» дубликат файла (а не ссылку на имеющийся файл), необходимо:
    - считать из атрибута типа «**Документ**» ссылку на **документ**, хранящийся в **шаблоне документа**;
    - считать из **документа** ссылку на **ревизию**, хранящуюся в **шаблоне ревизии** (из атрибута **currentRevision**);
    - считать из **ревизии**содержимое и имя файла (из атрибутов **content** и **title)**;
    - прикрепить полученный файл к атрибуту типа «**Документ**», т. е. поместить на него ссылку в **ревизию**.

## Прикладная задача

Необходимо настроить сценарий по нажатию кнопки на форме записи, который будет создавать дубликат текущей записи и прикреплять к ней дубликаты всех файлов, прикреплённых к исходной записи. Если к исходной записи не прикреплен ни один файл, то создавать её дубликат не требуется.

## Исходные данные

1. Создайте приложение *«Документооборот»**.*
2. В приложении *«Документооборот»*создайте шаблон записи *«**Пакеты д**окументов**»* с системным именем `DocumentPacks` и следующими атрибутами:
3. | Название атрибута | Системное имя | Свойства |
| --- | --- | --- |
| *Наименование пакета документов* | `DocumentPackName` | **Тип данных: текст** |
| *Файлы документов* | `AttachedFiles` | **Тип данных: документ** **Хранить несколько значений:**флажок установлен |
4. Вынесите на атрибуты *«Наименование пакета документов»* и *«Файлы документов»* вынесены на основную форму шаблона *«**Пакеты д**окументов**».*

## Настройка кнопки «Копировать пакет документов»

1. Отройте шаблон записи *«Пакеты документов».*
2. Перейдите на вкладку «**Кнопки**».
3. Создайте кнопку «****Копировать пакет документов****  »:
    - **Контекст операции: запись**
    - **Операция: вызвать событие «Нажата кнопка»**
    - **Результат выполнения: навигация**
    - **Переход к: предыдущая страница**
4. Поместите кнопку «**Копировать документ**» на основную форму шаблона *«Пакеты документов».*

## Настройка сценария «Копирование пакета документов»

1. На странице [администрирования приложения][apps] выберите пункт «**Сценарии**».
2. Создайте сценарий:
    - **Название**: *Копирование документа*
    - **Системное имя**: заполняется автоматически.
    - **Контекст выполнения**: **от имени системы**
3. Отобразится конструктор сценария.
4. Нажмите заголовок события «**Нажатие кнопки**».
5. Настройте свойства события:
    - **Тип: Нажатие кнопки**
    - **Контекстный шаблон:** *Пакеты д**окументов*
    - **Кнопка:***Копировать пакет документов*
6. После действия «**Нажата кнопка**» создайте и настройте действие «**Изменить значения переменных**»:
    - **Операция со значениями переменных: заменить**
    - **Переменная:** originalRecord
    - Настройте таблицу дочерних переменных.
    
    | Имя переменной | Значение |
    | --- | --- |
    | *id* | **Атрибут: ID** |
Бизнес-логика

Это действие будет сохранять в переменную `originalRecord.id` идентификатор исходной записи в шаблоне *«Пакеты документов»* для использования в последующих действиях.
7. После события «**Изменить значения переменных**» создайте и настройте действие «**Выполнить по условиям**» следующим образом:

    - Название условия: *Файл прикреплён*
    - **Выражение:** **N3**
    
    ```
    # Импортируем функции для работы с данными текущего сеанса, переменными и записями 
    @prefix variable: <http://comindware.com/ontology/session/variable#>.
    @prefix session: <http://comindware.com/ontology/session#>.
    @prefix object: <http://comindware.com/ontology/object#>.
    {
        #Находим атрибут «Файлы документов» в шаблоне «Пакеты документов»
        #и помещаем ID атрибута в локальную переменную AttachedFilesAttribute
        ("DocumentPacks" "AttachedFiles") object:findProperty ?AttachedFilesAttribute.
        #Находим переменную originalRecord из предыдущего действия
        #и помещаем её в локальную переменную originalRecordVariable
        session:context variable:originalRecord ?originalRecordVariable.
        #Находим переменную originalRecord.id с ID исходной записи в шаблоне «Пакеты документов»
        #и помещаем ID записи в локальную переменную docPackRecordId
        ?originalRecordVariable variable:id ?docPackRecordId.
        #Считываем значение атрибута «Файлы документов» в исходной записи
        ?docPackRecordId ?AttachedFilesAttribute ?.
        #Возвращаем true, если к атрибуту «Файлы документов» прикреплён хотя бы один файл
        true -> ?value.
    }
    ```
Бизнес-логика

Это действие будет инициировать вложенные в него действия, если в текущей записи *«Пакеты документов»* к атрибуту *«Файлы документов» (*с системным именем `AttachedFiles`) прикреплён хотя бы один файл.
8. Внутри действия «**Выполнить по условиям**» создайте действие «**Создать запись**» с **целевым шаблоном** *«Пакеты документов»*.

Бизнес-логика

Это действие создаёт пустую запись в шаблоне *«Пакеты документов»*, в которую последующие действия скопируют значения атрибутов *«Наименование пакета документов»* и *«Файлы документов»*.
9. Внутри действия «**Создать запись**» создайте и настройте действие «**Изменить значение атрибутов**» следующим образом:

    - **Атрибут:***Наименование пакета документов*
    - **Операция со значениями: заменить**
    - **Значение:****N3**
    
    ```
    # Импортируем функции для работы с данными текущего сеанса, переменными и записями 
    @prefix variable: <http://comindware.com/ontology/session/variable#>.
    @prefix session: <http://comindware.com/ontology/session#>.
    @prefix object: <http://comindware.com/ontology/object#>.
    {
        #Находим атрибут «Наименование пакета документов» в шаблоне «Пакеты документов»
        #и помещаем ID атрибута в локальную переменную PackNameAttribute
        ("DocumentPacks" "DocumentPackName") object:findProperty ?PackNameAttribute.
        #Помещаем переменную originalRecord в локальную переменную originalRecordVariable
        session:context variable:originalRecord ?originalRecordVariable.
        #Помещаем ID исходной записи в шаблоне «Пакеты документов»
        #в локальную переменную docPackRecordId
        ?originalRecordVariable variable:id ?docPackRecordId.
        #Возвращшаем значение атрибута «Наименование пакета документов» из исходной записи
        ?docPackRecordId ?PackNameAttribute ?value.
    }
    ```
Бизнес-логика

Это действие копирует значение атрибута *«Наименование пакета документов»* из исходной записи в новую.
10. После действия «**Изменить значение атрибутов**» внутри действия «**Создать запись**» создайте и настройте действие «**Повторять по количеству объектов**» следующим образом:
    - **Переменная:** *document*
    - **Атрибут или выражение для поиска объектов:** ******формула******
    
    ```
    # Импортируем функции для работы с данными текущего сеанса, переменными и записями 
    @prefix variable: <http://comindware.com/ontology/session/variable#>.
    @prefix session: <http://comindware.com/ontology/session#>.
    @prefix object: <http://comindware.com/ontology/object#>.
    {
        #Находим атрибут «Файлы документов» в шаблоне «Пакеты документов»
        #и помещаем ID атрибута в локальную переменную AttachedFilesAttribute  
        ("DocumentPacks" "AttachedFiles") object:findProperty ?AttachedFilesAttribute.
        #Помещаем переменную originalRecord в локальную переменную originalRecordVariable
        session:context variable:originalRecord ?originalRecordVariable.
        #Помещаем ID исходной записи в шаблоне «Пакеты документов»
        #в локальную переменную docPackRecordId
        ?originalRecordVariable variable:id ?docPackRecordId.
        #Возвращшаем значение атрибута «Файлы документов» из исходной записи
        ?docPackRecordId ?AttachedFilesAttribute ?value.
    }
    ```
Бизнес-логика

На каждой итерации цикла в переменную `document` будет помещаться ссылка на запись в *системном* **шаблоне документа** с файлом, прикреплённым к атрибуту *«Файлы документов»* из исходной записи.
11. Внутри действия «**Повторять по количеству объектов**» создайте и настройте действие «**Изменить значение атрибутов**» следующим образом:

    - **Атрибут:** *Файлы документов*
    - **Операция со значениями: добавить**
    - ****Значение:****  **N3**
    
    ```
    # Импортируем функции для работы с документами и данными текущего сеанса
    @prefix document: <http://comindware.com/ontology/document#>.
    @prefix variable: <http://comindware.com/ontology/session/variable#>.
    @prefix session: <http://comindware.com/ontology/session#>.
    {
        #Помещаем переменную document из действия «Повторять по количеству объектов»
        #в локальную переменную doc
        session:context variable:document ?doc.
        #Помещаем ссылку на прикреплённый файл в локальную переменную revision
        ?doc document:currentRevision ?revision.
        #Помещаем содержимое файла в формате Base64 в локальную переменную content
        ?revision document:content ?content.
        #Помещаем имя файла в локальную переменную filename
        ?doc document:title ?filename.
        #Собирем новый файл из имени и содержимого, сохраняем его в папку Streams,
        #и возвращаем ID нового документа с прикреплённым файлом
        (?content ?filename) document:attach ?value.
    }
    ```
Бизнес-логика

Это действие будет прикреплять к атрибуту *«Файлы документов»* в новой записи дубликат файла, прикреплённого к  атрибуту *«Файлы документов»*из исходной записи.

_![Настроенный сценарий для дублирования записи вместе с прикреплёнными к ней файлами](https://kb.comindware.ru/assets/img_66476d15e078c.png)_

## Тестирование работы сценария

1. Откройте шаблон *«Пакеты документов»* и нажмите кнопку «**Перейти к экземплярам**».
2. Отобразится список записей в шаблоне *«Пакеты документов».*
3. Создайте запись и заполните форму:
    - Введите *«Наименование пакета документов»*.
    - Прикрепите к полю *«Файлы документов»* несколько файлов.
4. Сохраните запись.
5. Нажмите кнопку *«Копировать пакет документов».*
6. Должен снова отобразиться список записей в шаблоне *«Пакеты документов».*
7. В списке записей должна появиться новая запись — дубликат исходной.
8. Откройте новую запись и убедитесь, что содержимое полей *«Наименование пакета документов»* и *«Файлы документов»* совпадает с содержимым исходной записи*.*

--8<-- "related_topics_heading.md"

**[Пути и содержимое папок экземпляра ПО][paths]**

**[Атрибут типа «Документ»][attribute_document]**

**[Кнопки. Определение, настройка, удаление][buttons]**

**`![](https://kb.comindware.ru/images/marker.png)Настройка действий сценария {Article-ID:2149}`**



{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
