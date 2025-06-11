Чтобы считать файл из атрибута типа «**Документ**» с помощью выражения N3, необходимо:

- получить объект с атрибутом:

    ``` turtle
    ("TemplateSystemName" "DocumentAttributeSystemName") object:findProperty ?DocumentAttribute.
    ```

- из объекта с атрибутом получить значение атрибута в текущей записи:

    ``` turtle
    ?item documentAttribute ?documentAttributeValue.
    ```

- из значения атрибута получить текущую версию документа:

    ``` turtle
    ?documentAttributeValue document:revision ?revision.
    ```

- из версии получить содержимое файла в формате `base64`:

    ``` turtle
    ?revision document:content ?content.
    ```

- из версии получить имя файла:

    ``` turtle
    ?revision document:title ?title.
    ```
