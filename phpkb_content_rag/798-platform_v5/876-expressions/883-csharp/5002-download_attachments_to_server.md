---
title: 'Атрибут типа «Документ». Скачивание файлов в папку на сервере'
kbId: 5002
url: 'https://kb.comindware.ru/article.php?id=5002'
updated: '2025-04-01 13:40:16'
---

# Атрибут типа «Документ». Скачивание файлов в папку на сервере

## Введение

Здесь представлен C#-скрипт для **[кнопки](https://kb.comindware.ru/article.php?id=4790)**, который сохраняет все файлы, прикреплённые к атрибуту типа «**Документ**», из текущей записи в локальную папку **на сервере Comindware Platform**.

Структура атрибута типа «Документ»

- Атрибут типа «**Документ**» хранит одну или несколько ссылок на записи (**документы**) в системном шаблоне документа, к которым прикрепляются файлы (например, загруженные пользователями).
- В шаблоне документа имеется атрибут `currentRevision` (текущая **версия**), который хранит ссылку на запись в системном шаблоне версии.
- В шаблоне версии имеются атрибуты `title` (имя) и `content` (содержимое), которые хранят имя файла и ссылку на файл, физически хранящийся в папке `Streams` на сервере.

Извлечение файлов из атрибута типа «Документ» с помощью C#

Чтобы считать файл из атрибута типа «**Документ**» с помощью C#-скрипта, необходимо:

- из текущей записи получить массив идентификаторов файлов, прикреплённых к атрибуту:

  ```
  var fileIds = Api.TeamNetwork.ObjectService.GetPropertyValues(recordId, new [] {"documentAttributeSystemName"})`;
  ```
- получить массив объектов с прикреплёнными файлами:

  ```
  var attachedFileObjects = fileIds[docId].TryGetValue("Files", out object fileObject)
                              && fileObject != null ? fileObject as object[] : null;
  ```
- получить объект файла (`attachedFile`):

  ```
  var attachedFile = Api.TeamNetwork.DocumentService.GetContent(attachedFileObject[0].ToString());
  ```
- получить имя файла с расширением (`attachedFile.Name`);
- получить содержимое файла (`attachedFile.Data`);
- при необходимости получить объект с метаданными документа:

  ```
  var attachedFile = Api.TeamNetwork.DocumentService.GetDocument(attachedFileObject[0].ToString());
  ```

  - `attachedFile.Title` — имя файла с расширением;
  - `attachedFile.Extension` — расширение файла.

Добавление файлов в атрибут типа «Документ» с помощью C#

Чтобы прикрепить к атрибуту типа «**Документ**» файл с помощью C#-скрипта, необходимо:

- сформировать объект типа `Document`:

  ```
  var document = new Document
      {
          Title = "имя файла.расширение",
          Extension = ".расширение"
      };
  ```
- сформировать массив байтов `byte[] fileBytes` с содержимым файла;
- из массива байтов создать поток `MemoryStream()` для прикрепления документа к атрибуту:

  ```
      var fileStream = new MemoryStream();
      fileStream.Write(fileBytes, 0, fileBytes.Length);
      fileStream.Seek(0, SeekOrigin.Begin);
  ```
- преобразовать поток в объект документа для прикрепления к атрибуту:

  ```
  string documentObject = Api.TeamNetwork.DocumentService.CreateDocumentWithStream(document, fileStream, "");
  ```
- сформировать словарь из системного имени атрибута и объекта документа:

  ```
  var documentDict = new Dictionary<string,object>
      {
          { "DocumentAttributeSystemName", documentObject }
      };
  ```
- прикрепить результирующий документ к атрибуту записи `reсordId`:

  ```
      Api.TeamNetwork.ObjectService.EditWithAlias(reсordId, documentDict)
  ```

## Образец скрипта

Скрипт для скачивания файлов на сервер```
using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;
using System.IO;
class Script {
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities) {
        try {
            //<ServerDownloadPath> — путь для скачивания файлов на сервере
            var path = @ "<ServerDownloadPath>";
            //DocumentAttributeSystemName — системное имя атрибута типа «Документ»
            var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new string[] {
                userCommandContext.ObjectIds[0]
            }, new string[] {
                "DocumentAttributeSystemName"
            });
            var documentIdsObj = data[userCommandContext.ObjectIds[0]]["DocumentAttributeSystemName"];
            var documentIds = documentIdsObj as IEnumerable < object > ;
            if (documentIds == null) {
                documentIds = new string[] {
                    documentIdsObj as string
                };
            }
            foreach(var documentIdObj in documentIds) {
                var documentId = documentIdObj as string;
                var documentData = Api.TeamNetwork.DocumentService.GetContent(documentId);
                var documentInfo = Api.TeamNetwork.DocumentService.GetDocument(documentId);
                var docData = new Document {
                    Title = documentData.Name,
                        Extension = documentInfo.Extension
                };
                var stream = new MemoryStream();
                stream.Write(documentData.Data, 0, documentData.Data.Length);
                stream.Seek(0, SeekOrigin.Begin);
                var filepath = path + documentData.Name;
                using(FileStream outstr = new FileStream(filepath, FileMode.Create)) {
                    stream.CopyTo(outstr);
                }
            }
        } catch {
            var badresult = new UserCommandResult {
                Success = true,
                    Commited = true,
                    ResultType = UserCommandResultType.DataChange,
                    Messages = new [] {
                        new UserCommandMessage {
                            Severity = SeverityLevel.Normal,
                                Text = "Неудачно"
                        }
                    }
            };
            return badresult;
        }

        var result = new UserCommandResult {
            Success = true,
                Commited = true,
                ResultType = UserCommandResultType.DataChange,
                Messages = new [] {
                    new UserCommandMessage {
                        Severity = SeverityLevel.Normal,
                            Text = "Удачно"
                    }
                }
        };
        return result;
    }
}
```

## Связанные статьи

- *[Атрибут типа «Документ»](https://kb.comindware.ru/article.php?id=4782)*
- *[Кнопки. Определение, настройка, удаление](https://kb.comindware.ru/article.php?id=4790)*
- *[Написание скриптов на языке C#](https://kb.comindware.ru/article.php?id=4864)*
- *[Атрибут типа «Документ». Скачивание архива с файлами из всех строк таблицы с прикреплением архива к атрибуту](https://kb.comindware.ru/article.php?id=5081)*
- *[Атрибут типа «Документ». Скачивание архива с файлами из выбранных строк таблицы и записи](https://kb.comindware.ru/article.php?id=4921)*
- *[Атрибут типа «Документ». Клонирование записи вместе с прикреплёнными файлами](https://kb.comindware.ru/article.php?id=4883)*