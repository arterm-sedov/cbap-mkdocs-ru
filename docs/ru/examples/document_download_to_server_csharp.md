---
title: Атрибут типа «Документ». Скачивание файлов в папку на сервере
kbId: 5205
---

# Атрибут типа «Документ». Скачивание файлов в папку на сервере {: #example_document_download_to_server_csharp }

## Введение

Здесь представлен C#-скрипт для **[кнопки][buttons]**, который сохраняет все файлы, прикреплённые к атрибуту типа «**Документ**», из текущей записи в локальную папку **на сервере {{ productName }}**.

!!! question "Структура атрибута типа «Документ»"

    --8<-- "attribute_document_logic.md"

!!! tip "Извлечение файлов из атрибута типа «Документ» с помощью C#"

    --8<-- "attribute_document_get_file_csharp.md"

!!! tip "Добавление файлов в атрибут типа «Документ» с помощью C#"

    --8<-- "attribute_document_add_file_csharp.md"

## Образец скрипта {: .pageBreakBefore }

``` cs title="Скрипт для скачивания файлов на сервер"
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
{% if pdfOutput %}
```

``` cs title="Скрипт для скачивания файлов на сервер — продолжение"
{% endif %}
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

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Атрибут типа «Документ»][attribute_document]_
- _[Кнопки. Определение, настройка, удаление][buttons]_
- _[Написание скриптов на языке C#][csharp_guide]_
- _[Атрибут типа «Документ». Скачивание архива с файлами из всех строк таблицы с прикреплением архива к атрибуту][example_document_download_archive_related_records_csharp]_
- _[Атрибут типа «Документ». Скачивание архива с файлами из выбранных строк таблицы и записи][example_document_download_archive_csharp]_
- _[Атрибут типа «Документ». Клонирование записи вместе с прикреплёнными файлами][example_document_clone_scenario_n3]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
