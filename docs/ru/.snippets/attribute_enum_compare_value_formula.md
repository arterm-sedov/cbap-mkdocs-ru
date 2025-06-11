С помощью **формулы** сравнить значение атрибута типа «**Список значений**» с требуемым можно по системному имени значения следующими способами:

- равенство

    ``` cs
    $EnumAttributeSystemName == EnumValueSystemName
    ```

    или

    ``` cs
    EQUALS($EnumAttributeSystemName->cmw.variantAlias, "EnumValueSystemName")
    ```

    или

    ``` cs
    EQUALS($EnumAttributeSystemName, ENUMVALUE("EnumAttributeSystemName", "EnumValueSystemName"))
    ```

- неравенство

    ``` cs
    $EnumAttributeSystemName !== EnumValueSystemName
    ```

    или

    ``` cs
    NOT(EQUALS($EnumAttributeSystemName->cmw.variantAlias, "EnumValueSystemName"))
    ```

    или

    ``` cs
    NOT(EQUALS($EnumAttributeSystemName, ENUMVALUE("EnumAttributeSystemName", "EnumValueSystemName")))
    ```
