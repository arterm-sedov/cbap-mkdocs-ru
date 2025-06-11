Чтобы прикрепить к атрибуту типа «**Документ**» файл с помощью выражения N3, необходимо:

- сформировать содержимое файла в формате `base64`:

    ``` turtle
    ?documentContentSource document:content ?content.
    ```

- сформировать имя файла:

    ``` turtle
    ?documentTitleSource document:title ?title.
    ```

- прикрепить полученный файл к атрибуту типа «**Документ**», т. е. поместить на него ссылку в версию:

    ``` turtle
    (?content ?title) document:attach ?documentAttributeValue.
    ```
