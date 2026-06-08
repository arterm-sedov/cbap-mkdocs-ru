---
kbTitle: Атрибут типа «Документ». Скачивание архива файлов из связанных записей и его прикрепление к атрибуту
title: Атрибут типа «Документ». Получение архива файлов из связанных записей
tags:
    - C#
    - C#-скрипт
    - скрипт
    - скачать документы
    - документ
    - атрибут типа «Документ»
    - атрибут типа «Запись»
    - скачать файлы
    - скачать архив
hide: tags
kbId: 5214
---

# Атрибут типа «Документ». Получение архива файлов из связанных записей {: #example_document_download_archive_related_records_csharp }

## Введение

**{{ productName }}** позволяет прикреплять файлы к атрибуту типа «**Документ**». При этом из каждой записи прикреплённые файлы приходится скачивать отдельно.

Атрибут типа «**Запись**» позволяет связать запись с реестром документов, к которым прикреплены файлы.

С помощью C#-скрипта можно настроить кнопку для скачивания из реестра документов в одном архиве всех файлов, связанных с записью.

Также при помощи C#-скрипта можно добавить сформированный архив файлов в атрибут типа «**Документ**».

Здесь представлен пример настройки кнопки, скачивающей все файлы, которые связаны с текущей записью, и добавляющей этот архив в атрибут типа «**Документ**».

См. также примеры работы с атрибутом типа «**Документ**»:

- _[Клонирование записи вместе с прикреплёнными файлами][example_document_clone_scenario_n3]_
- _[Скачивание файлов в папку на сервере][example_document_download_to_server_csharp]_
- _[Скачивание архива с файлами из выбранных строк таблицы или одной записи][example_document_download_archive_csharp]_

!!! question "Структура атрибута типа «Документ»"

    --8<-- "attribute_document_logic.md"

!!! tip "Извлечение файлов из атрибута типа «Документ» с помощью C#"

    --8<-- "attribute_document_get_file_csharp.md"

!!! tip "Добавление файлов в атрибут типа «Документ» с помощью C#"

    --8<-- "attribute_document_add_file_csharp.md"

## Прикладная задача

Имеется шаблон _«Заявки»_. К заявке можно прикрепить документы — записи из связанного шаблона _«Реестр документов»_. К каждому документу может быть прикреплено несколько файлов.

Необходимо создать кнопку для скачивания архива всех файлов из всех документов, прикреплённых к заявке. Скачанный архив необходимо прикрепить к заявке.

## Настройка кнопки для скачивания архива файлов

Чтобы скачать документы и прикрепить их к записи, настройте [кнопку][buttons] и C#-скрипт для неё.

1. Создайте **шаблон записи** _«Реестр документов»_ со следующим **атрибутом**:

    - **Название:** _Файлы_
    - **Системное имя:** _Files_
    - **Тип данных: документ**
    - **Использовать для поиска записей:** флажок установлен
    - **Хранить несколько значений:** флажок установлен

    --8<-- "csharp_file_download_warning.md"

2. Создайте **шаблон записи** _«Заявки»_ со следующими **атрибутами**:

    | Название    | Системное имя | Тип данных | Свойства                                                                                                         |
    | ----------- | ------------- | ---------- | --------------- |
    | _Документы_ | _Documents_   | **Запись** | <ul><li>**Связанный шаблон:** _Реестр документов_</li><li>**Хранить несколько значений:** флажок установлен</li> |
    | _Архив документов_ | _DocumentArchive_ | **Документ** ||

3. Создайте кнопку _«Скачать архив документов»_ со следующими свойствами:

    - **Контекст операции: запись**;
    - **Операция: С#-скрипт**;
    - **Результат выполнения: скачать документ**.

    --8<-- "csharp_script_context.md"

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

4. На вкладке «**Скрипт**» добавьте C#-скрипт по следующему образцу:

    ``` cs title="Скрипт для скачивания файлов из связанных записей"
    using System; 
    using System.Collections.Generic;
    using System.IO; 
    using Comindware.Data.Entity;
    using Comindware.TeamNetwork.Api.Data.UserCommands;
    using Comindware.TeamNetwork.Api.Data;
    using System.Collections.Generic;
    using System.Linq;

    class Script
    {
        // Определяем конструктор скрипта, выполняющегося в контексте кнопки
        public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
        { 
            // Получаем ID текущей записи шаблона «Заявки» из контекста операции кнопки.
            var reсordId = userCommandContext.ObjectIds[0];
            // Помещаем в массив documentIds идентификаторы записей шаблона «Реестр документов»
            // из атрибута «Документы» текущей записи.
            // Documents — системное имя атрибута «Документы» шаблона «Заявки».
            var documentIds = Api.TeamNetwork.ObjectService.GetPropertyValues(new string[] {reсordId}, new [] {"Documents"});
            // По идентификаторам получаем массив записей шаблона «Реестр документов», связанных с текущей записью.
            var DocumentRecords = documentIds[reсordId].TryGetValue("Documents", out object OutputRecordArray) && OutputRecordArray != null ? OutputRecordArray as object[] : null;
            // Инициализируем словарь файлов для архива в виде пар «имя:содержимое».
            var files = new Dictionary<string, byte[]>();
            // Добавляем файлы в поток для дальнейшего архивирования
            // из каждой записи шаблона «Реестр документов».
            foreach (var DocumentRecord in DocumentRecords)
            {
                // Получаем идентификатор записи шаблона «Реестр документов».
                var docId = DocumentRecord.ToString();
                // Помещаем в массив fileIds идентификаторы файлов, прикреплённых к атрибуту «Файлы».
                // Files — системное имя атрибута «Файлы» шаблона «Реестр документов».
                var fileIds = Api.TeamNetwork.ObjectService.GetPropertyValues(new []{docId}, new [] {"Files"});
                // По идентификаторам получаем массив объектов с прикреплёнными файлами.
                var attachedFileObjects = fileIds[docId].TryGetValue("Files", out object fileObject) 
                                          && fileObject != null ? fileObject as object[] : null;
                if(attachedFileObjects.Length > 0)
                {
                    // Добавляем в словарь все файлы, прикреплённые к атрибуту «Файлы».
                    foreach(var attachedFileObject in attachedFileObjects)
                    {
                    // Получаем прикреплённый файл.
                    var attachedFile = Api.TeamNetwork.DocumentService.GetContent(attachedFileObject.ToString());
                    // Помещаем содержимое файла в словарь файлов для архива по имени.
                    files[attachedFile.Name] = attachedFile.Data;
                    }
                }
            }
    {% if pdfOutput %}
    ```

    ``` cs title="Скрипт для скачивания файлов из связанных записей — продолжение"
    {% endif %}
            // Формируем архив файлов для скачивания из словаря files.
            var resultingArchive = Api.TeamNetwork.DocumentService.GetZippedStreams(files);
            // Инициализируем документ для файла архива,
            // чтобы прикрепить его к атрибуту «Архив документов».
            var archiveDocument = new Document 
            {
                Title = "Data.zip",
                Extension = ".zip"
            };
            // Помещаем архив файлов в массив байтов
            // для преобразования в документ и прикрепления к атрибуту.
            byte[] compressedBytes = resultingArchive.ToArray();
            // Создаём поток для прикрепления документа с архивом к атрибуту.
            var archiveFileStream = new MemoryStream();
            archiveFileStream.Write(compressedBytes, 0, compressedBytes.Length);
            archiveFileStream.Seek(0, SeekOrigin.Begin);
            // Преобразуем поток в объект документа с архивом для прикрепления к атрибуту.
            string documentObject = Api.TeamNetwork.DocumentService.CreateDocumentWithStream(archiveDocument, archiveFileStream, "");
            // Формируем словарь для прикрепления документа с архивом к атрибуту.
            var documentDict = new Dictionary<string,object>
            {
                // DocumentArchive — системное имя атрибута «Архив документов».
                { "DocumentArchive", documentObject }
            };
            // Прикрепляем архив к атрибуту «Архив документов».
            Api.TeamNetwork.ObjectService.EditWithAlias(reсordId, documentDict);
            // Возвращаем архив для скачивания в качестве результата нажатия кнопки.            
            return new UserCommandResult
            {
                Success = true,
                Commited = true,
                File = new UserCommandFileResult
                {
                    Content = resultingArchive,
                    // Укажите имя архива
                    Name = archiveDocument.Title
                }
            };
        }
    }
    ```

5. Поместите на форму шаблона _«Заявки»_ **атрибут** _«Архив документов»_ и **кнопку** _«Скачать архив документов»_.
6. Поместите на форму **атрибут** _«Документы»_ и настройте его **представление** в виде **таблицы**.
7. Поместите в таблицу _«Документы»_ на форме **атрибут** _«Файлы»_ шаблона записи _«Реестр документов»_.
8. В область кнопок таблицы _«Документы»_ поместите кнопки «**Создать**».

## Тестирование {: .pageBreakBefore }

1. Создайте новую запись в шаблоне _«Заявки»_.
2. Добавьте несколько строк в таблицу _«Документы»_.
3. К каждой строке в таблице _«Документы»_ прикрепите несколько файлов (в столбце «**Файлы**»).
4. Сохраните запись.
5. Нажмите кнопку _«Скачать архив документов»_.
6. Браузер скачает архив со всеми файлами из документов, прикреплённых к заявке.

    !!! note "Примечание"

        Если в браузере отобразится сообщение «**Незащищенное скачивание заблокировано**», нажмите кнопку «**Сохранить**», чтобы продолжить скачивание.

7. В поле _«Архив документов»_ должен появиться архив со всеми файлами из документов, прикреплённых к заявке.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Атрибут типа «Запись»][attribute_record]_
- _[Атрибут типа «Документ»][attribute_document]_
- _[Кнопки. Определение, настройка, удаление][buttons]_
- _[Написание скриптов на языке C#][csharp_guide]_
- _[Атрибут типа «Документ». Скачивание архива с файлами из выбранных строк таблицы и записи][example_document_download_archive_csharp]_
- _[Атрибут типа «Документ». Скачивание файлов в папку на сервере][example_document_download_to_server_csharp]_
- _[Атрибут типа «Документ». Клонирование записи вместе с прикреплёнными файлами][example_document_clone_scenario_n3]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
