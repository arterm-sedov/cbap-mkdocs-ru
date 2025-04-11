---
title: Атрибут типа «Документ». Скачивание архива файлов из связанных записей и его прикрепление к атрибуту
kbId: 5081
---

# Атрибут типа «Документ». Скачивание архива файлов из связанных записей и его прикрепление к атрибуту

## Введение

**{{ productName }}** позволяет прикреплять файлы к атрибуту типа «**Документ**». При этом из каждой записи прикреплённые файлы приходится скачивать отдельно.

Атрибут типа «**Запись**» позволяет связать запись с реестром документов, к которым прикреплены файлы.

С помощью C#-скрипта можно настроить кнопку для скачивания из реестра документов в одном архиве всех файлов, связанных с записью.

Также при помощи C#-скрипта можно добавить сформированный архив файлов в атрибут типа «**Документ**».

Здесь представлен пример настройки кнопки, скачивающей все файлы, которые связаны с текущей записью, и добавляющей этот архив в атрибут типа «**Документ**».

См. также примеры работы с атрибутом типа «**Документ**»:

- *[Клонирование записи вместе с прикреплёнными файлами][example_document_clone_scenario_n3]*
- *[Скачивание файлов в папку на сервере][example_document_download_to_server_csharp]*
- *[Скачивание архива с файлами из выбранных строк таблицы или одной записи][example_document_download_archive_csharp]*

Структура атрибута типа «Документ»

- Атрибут типа «**Документ**» хранит одну или несколько ссылок на записи (**документы**) в системном шаблоне документа, к которым прикрепляются файлы.
- В шаблоне документа имеется атрибут `currentRevision` (текущая **ревизия**), который хранит ссылку на запись в системном шаблоне ревизии.
- В шаблоне ревизии имеются атрибуты `title` (имя) и `content` (содержимое), которые хранят имя файла и ссылку на файл, физически хранящийся в папке `Streams` на сервере.
- Чтобы считать файл из атрибута типа «**Документ**» с помощью C#-скрипта, необходимо:
    - из текущей записи получить массив идентификаторов файлов, прикреплённых к атрибуту:
     ````
    var fileIds = Api.TeamNetwork.ObjectService.GetPropertyValues(recordId, new [] {"documentAttributeSystemName"})`;
    
    ````
    - получить массив объектов с прикреплёнными файлами:
     ````
    var attachedFileObjects = fileIds[docId].TryGetValue("Files", out object fileObject)
                              && fileObject != null ? fileObject as object[] : null;
    
    ````
    - получить объект файла (`attachedFile`):
     ````
    var attachedFile = Api.TeamNetwork.DocumentService.GetContent(attachedFileObject[0].ToString());
    
    ````
    - получить имя файла с расширением (`attachedFile.Name`);
    - получить содержимое файла (`attachedFile.Data`);
    - при необходимости получить объект с метаданными документа:
     ````
    var attachedFile = Api.TeamNetwork.DocumentService.GetDocument(attachedFileObject[0].ToString());
    
    ````
        - `attachedFile.Title` — имя файла с расширением;
        - `attachedFile.Extension` — расширение файла.
- Чтобы прикрепить к атрибуту типа «**Документ**» файл с помощью C#-скрипта, необходимо:
    - сформировать объект типа `Document`:
     ````
    var document = new Document
        {
            Title = "имя файла.расширение",
            Extension = ".расширение"
        };
    
    ````
    - сформировать массив байтов `byte[] fileBytes` с содержимым файла;
    - из массива байтов создать поток `MemoryStream()` для прикрепления документа к атрибуту:
     ````
        var fileStream = new MemoryStream();
        fileStream.Write(fileBytes, 0, fileBytes.Length);
        fileStream.Seek(0, SeekOrigin.Begin);
    
    ````
    - преобразовать поток в объект документа для прикрепления к атрибуту:
     ````
    string documentObject = Api.TeamNetwork.DocumentService.CreateDocumentWithStream(document, fileStream, "");
    
    ````
    - сформировать словарь из системного имени атрибута и объекта документа;
     ````
    var documentDict = new Dictionary<string,object>
        {
            { "DocumentAttributeSystemName", documentObject }
        };
    
    ````
    - прикрепить результирующий документ к атрибуту записи `reсordId`:
     ````
     Api.TeamNetwork.ObjectService.EditWithAlias(reсordId, documentDict)
    
    ````

## Прикладная задача

Имеется шаблон *«Заявки»*. К заявке можно прикрепить документы — записи из связанного шаблона *«Реестр документов»*. К каждому документу может быть прикреплено несколько файлов.

Необходимо создать кнопку для скачивания архива всех файлов из всех документов, прикреплённых к заявке. Скачанный архив необходимо прикрепить к заявке.

## Настройка кнопки для скачивания архива файлов

Чтобы скачать документы и прикрепить их к записи, настройте [кнопку][buttons] и C#-скрипт для неё.

1. Создайте **шаблон записи** *«Реестр документов»* со следующим **атрибутом**:

    - **Название:** *Файлы*
    - **Системное имя:** *Files*
    - **Тип данных: документ**
    - **Использовать для поиска записей:** флажок установлен
    - **Хранить несколько значений:** флажок установлен
Внимание!

Для корректного скачивания файлов с помощью C#-скрипта у атрибута типа «**Документ**» рекомендуется установить флажок «**Использовать для поиска записей**». В противном случае скрипт может не сработать.
2. Создайте **шаблон записи** *«Заявки»* со следующими **атрибутами**:

| Название | Системное имя | Тип данных | Свойства |
| --- | --- | --- | --- |
| *Документы* | *Documents* | **Запись** | - **Связанный шаблон:** *Реестр документов*     - **Хранить несколько значений:** флажок установлен |
| *Архив документов* | *DocumentArchive* | **Документ** |  |
3. Создайте кнопку *«Скачать архив документов»* со следующими свойствами:

    - **Контекст операции: запись**;
    - **Операция: С#-скрипт**;
    - **Результат выполнения: скачать документ**.
4. На вкладке «**Скрипт**» добавьте C#-скрипт по следующему образцу:

Контекст C#-скрипта

C#-скрипты можно использовать в следующих контекстах:

    - на кнопках;
    - в задачах-выполнении сценария;
    - в сценариях.
В зависимости от контекста в C#-скрипте будут отличаться метод `Main()` и возвращаемое значение.

Чтобы применить описанный выше C#-скрипт в других контекстах, также понадобится изменить значение переменной `reсordId`, содержащей ID текущей записи:

    - `var reсordId = context.BusinessObjectId;` — для задачи-выполнения сценария;
    - `var reсordId = userCommandContext.ObjectIds[0];` — для кнопки;
    - `var reсordId = ObjectId.ToString().Replace("user.", "");` — для действия сценария «**Проверить результат скрипта**».
См. *«[Написание скриптов на языке C#][csharp_guide]»*.

````
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

````
5. Поместите на форму шаблона *«Заявки»* **атрибут** *«Архив документов»* и **кнопку** *«Скачать архив документов»*.
6. Поместите на форму **атрибут** *«Документы»* и настройте его **представление** в виде **таблицы**.
7. Поместите в таблицу *«Документы»* на форме **атрибут** *«Файлы»* шаблона записи *«Реестр документов»*.
8. В область кнопок таблицы *«Документы»* поместите кнопки «**Создать**».

## Тестирование

1. Создайте новую запись в шаблоне *«Заявки»*.
2. Добавьте несколько строк в таблицу *«Документы»*.
3. К каждой строке в таблице *«Документы»* прикрепите несколько файлов (в столбце «**Файлы**»).
4. Сохраните запись.
5. Нажмите кнопку *«Скачать архив документов»*.
6. Браузер скачает архив со всеми файлами из документов, прикреплённых к заявке.

Примечание

Если в браузере отобразится сообщение «**Незащищенное скачивание заблокировано**», нажмите кнопку «**Сохранить**», чтобы продолжить скачивание.
7. В поле *«Архив документов»* должен появиться архив со всеми файлами из документов, прикреплённых к заявке.

--8<-- "related_topics_heading.md"

- *[Атрибут типа «Запись»][attribute_record]*
- *[Атрибут типа «Документ»][attribute_document]*
- *[Кнопки. Определение, настройка, удаление][buttons]*
- *[Написание скриптов на языке C#][csharp_guide]*
- *[Атрибут типа «Документ». Скачивание архива с файлами из выбранных строк таблицы и записи][example_document_download_archive_csharp]*
- *[Атрибут типа «Документ». Скачивание файлов в папку на сервере][example_document_download_to_server_csharp]*
- *[Атрибут типа «Документ». Клонирование записи вместе с прикреплёнными файлами][example_document_clone_scenario_n3]*

[*‌*
 К началу](#)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
