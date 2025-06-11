Чтобы прикрепить к атрибуту типа «**Документ**» файл с помощью C#-скрипта, необходимо:

- сформировать объект типа `Document`:

    ``` cs
    var document = new Document 
        {
            Title = "имя файла.расширение",
            Extension = ".расширение"
        };
    ```

- сформировать массив байтов `byte[] fileBytes` с содержимым файла;
- из массива байтов создать поток `MemoryStream()` для прикрепления документа к атрибуту:

    ``` cs
        var fileStream = new MemoryStream();
        fileStream.Write(fileBytes, 0, fileBytes.Length);
        fileStream.Seek(0, SeekOrigin.Begin);
    ```

- преобразовать поток в объект документа для прикрепления к атрибуту:

    ``` cs
    string documentObject = Api.TeamNetwork.DocumentService.CreateDocumentWithStream(document, fileStream, "");
    ```

- сформировать словарь из системного имени атрибута и объекта документа:

    ``` cs
    var documentDict = new Dictionary<string,object>
        {
            { "DocumentAttributeSystemName", documentObject }
        };
    ```

- прикрепить результирующий документ к атрибуту записи `reсordId`:

    ``` cs
        Api.TeamNetwork.ObjectService.EditWithAlias(reсordId, documentDict)
    ```
