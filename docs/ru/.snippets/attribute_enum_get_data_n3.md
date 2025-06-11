С помощью **N3** для атрибута типа «**Список значений**» можно получить:

- ID определённого значения:

    ``` turtle
    ("EnumAttributeSystemName" "enumValueSystemName") convert:enumValue ?enumValueId.
    ```

- объект с атрибутом:

    ``` turtle
    ("TemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
    ```

- из объекта с атрибутом — массив возможных значений атрибута в текущей записи:

    ``` turtle
    ?item ?enumAttribute ?enumAttributeValues.
    ```

    **Из этого массива можно получить:**

    - ID текущего значения атрибута:

        ``` turtle
        ?enumAttributeValues cmw:variantName ?enumValueId.
        ```

    - системное имя значения атрибута:

        ``` turtle
        ?enumAttributeValues cmw:variantAlias ?enumValueSystemName.
        ```

    - код значка значения атрибута:

        ``` turtle
        ?enumAttributeValues cmw:variantIcon ?enumValueIcon.
        ```

    - цвет значения атрибута в десятичном формате:

        ``` turtle
        ?enumAttributeValues cmw:color ?enumValueColor.
        ```
