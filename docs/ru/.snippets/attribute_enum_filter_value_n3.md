С помощью **N3** для атрибута типа «**Список значений**» можно выполнять фильтрацию по системному имени его значения:

- Фильтрация (в таблице шаблона) записей с требуемым значением атрибута:

    ``` turtle
    @prefix convert: <http://comindware.com/logics/convertions#>.
    @prefix object: <http://comindware.com/ontology/object#>.
    {
        # Получаем атрибут типа «Список значений» из шаблона по системному имени.
        ("TemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
        # Получаем ID значения атрибута по системному имени.
        ("EnumAttributeSystemName" "enumValueSystemName") convert:enumValue ?enumValueId.
        # Возвращаем записи, у которых атрибут имеет значение "enumValueSystemName".
        ?item ?enumAttribute ?enumValueId.
    }
    ```

- Фильтрация добавляемых записей (в таблице на форме или раскрывающемся списке на форме) записей с требуемым значением атрибута:

    ``` turtle
    @prefix convert: <http://comindware.com/logics/convertions#>.
    @prefix object: <http://comindware.com/ontology/object#>.
    {
        # Получаем атрибут типа «Список значений» из шаблона по системному имени.
        ("TemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
        # Получаем ID значения атрибута по системному имени.
        ("EnumAttributeSystemName" "enumValueSystemName") convert:enumValue ?enumValueId.
        # Фильтруем и возвращаем записи, 
        # у которых атрибут имеет значение "enumValueSystemName".
        ?filteredRecordIds ?enumAttribute ?enumValueId.
        ?filteredRecordIds -> ?value.
    }
    ```
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

- Фильтрация отображаемых записей (в таблице на форме, раскрывающемся списке на форме, вычисляемом атрибуте или правиле для формы) записей с требуемым значением атрибута:

    ``` turtle
    @prefix convert: <http://comindware.com/logics/convertions#>.
    @prefix object: <http://comindware.com/ontology/object#>.
    {
        # Получаем атрибут типа «Запись» из шаблона с коллекцией записей.
        ("ParentTemplateSystemName" "RecordAttributeSystemName") object:findProperty ?RecordAttribute.
        # Получаем атрибут типа «Список значений» из связанного шаблона по системному имени.
        ("LinkedTemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
        # Получаем ID значения атрибута по системному имени.
        ("EnumAttributeSystemName" "enumValueSystemName") convert:enumValue ?enumValueId.
        # Получаем коллекцию записей из атрибута RecordAttribute.
        ?item ?RecordAttribute ?filteredRecordIds.
        # Фильтруем и возвращаем записи,
        # у которых атрибут имеет значение "enumValueSystemName".
        ?filteredRecordIds ?enumAttribute ?enumValueId.
        ?filteredRecordIds -> ?value.
    }
    ```
