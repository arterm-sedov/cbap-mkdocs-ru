С помощью **N3** для атрибута типа «**Список значений**» можно выполнять сравнение по системному имени его значения:

- Сравнение значения атрибута с требуемым:

    ``` turtle
    @prefix object: <http://comindware.com/ontology/object#>.
    @prefix cmw: <http://comindware.com/logics#>.
    {
        # Получаем атрибут типа «Список значений» из шаблона по системному имени.
        ("TemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
        # Получаем коллекцию возможных значений атрибута.
        ?item ?enumAttribute ?enumAttributeValues.
        # Получаем системное имя значения атрибута в текущей записи.
        ?enumAttributeValues cmw:variantAlias ?enumValueSystemName.
        # Сравниваем системное имя значения атрибута с требуемым
        # и возвращаем результат.
        if
        {
            ?enumValueSystemName == "targetValueSystemName".
        }
        then
        {
            true -> ?value.
        }
        else
        {
            false -> ?value.
        }
    }
    ```