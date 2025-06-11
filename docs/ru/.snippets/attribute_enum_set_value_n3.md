Чтобы c помощю **N3** задать значение атрибута типа «**Список значений**» (например, для вычисляемого атрибута или правила на форме), необходимо:

- получить ID требуемого значения атрибута:

    ``` turtle
    ("EnumAttributeSystemName" "ValueSystemName") convert:enumValue ?enumValueId.
    ```

- вернуть полученный ID:

    ``` turtle
    ?enumIdOverdue -> ?value.
    ```
