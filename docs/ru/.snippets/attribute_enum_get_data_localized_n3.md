С помощью **N3** для атрибута типа «**Список значений**» можно получить названия значения атрибута на английском, русском и немецком языках:

``` turtle
# Находим атрибут EnumAttributeSystemName в шаблоне TemplateSystemName.
("TemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
# Присваиваем переменной ?enumAttributeValues
# объект со списком значений атрибута.
?item ?enumAttribute ?enumAttributeValues.
# Присваиваем переменной ?enumValueId
# объект с выбранным значением атрибута.
?enumAttributeValues cmw:variantName ?enumValueId.
# Присваиваем переменной ?enumAttributeValues массив объектов
# с заполненными названиями значения атрибута на всех языках.
?enumValueId l10n:text ?enumValueLanguageVersions.
# Начинаем цикл по ?enumValueLanguageVersions
    # Присваиваем переменной ?langCodeStr код языка
    # названия значения атрибута на текущей итерации цикла.
    ?enumValueLanguageVersions l10n:lang ?langCode.
    ("{0}" ?langCode) string:format ?langCodeStr.
    # Сравниваем код языка для значения атрибута с желаемым.
    # "ru" — код русского языка, "en" — английского, "de" — немецкого.
    ?langCodeStr cmwentity:contains "ru".
        # Если предыдущее предложение возвращает true,
        # записываем значение на русском языке в вычисляемый атрибут.
        ?names l10n:data ?value.
# переходим к следующей итерации по ?enumValueLanguageVersions.
```
