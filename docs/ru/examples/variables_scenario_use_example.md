---
title:
kbId:
---

# Создание массива в переменной

## Введение

## Исходные данные

## Прикладная задача

## Настройка сценария

1. Создайте новый сценарий _«Сбор данных»_.
2. Откройте событие «**Нажатие кнопки**» и настройте его следующим образом:

    - Тип:
    - Контекстный шаблон:
    - Подключение:
    - Путь передачи данных:
    - Имя переменной: 

3. Добавьте действие «**Изменить значения переменных**» со следующими свойствами:

    - На вкладке «**Основные**»:
        - **Операция со значениями переменных: заменить**
        - **Набор переменных:** _Message_
    - На вкладке «**Дополнительно**»:
        - **Сбрасывать кэш значений:** флажок установлен

4. Добавьте действие «**Проверить результат выражения**» со следующими свойствами:

    - **Выражение: N3**

        ``` turtle
        @prefix variable: <http://comindware.com/ontology/session/variable#>.
        @prefix operator: <http://comindware.com/ontology/session/operator#>.
        @prefix object: <http://comindware.com/ontology/object#>.
        @prefix cmwui: <http://comindware.com/ontology/ui#>.
        @prefix session: <http://comindware.com/ontology/session#>.
        {
            ("Pozitsiikonkursa" "Pozitsiyazayavkinazakupku") object:findProperty ?Pozitsiyazayavkinazakupku.
            ("Pozitsiizayavkinazakupku" "appPosId") object:findProperty ?appPosId.
            ("Pozitsiikonkursa" "Vybrannoepredlozhenie" ) object:findProperty ?Vybrannoepredlozhenie.
            ("Pozitsiipredlozheniypokonkursam" "Predlagaemayatsena") object:findProperty ?Predlagaemayatsena.
            ("Pozitsiipredlozheniypokonkursam" "Predlozheniepokonkursu") object:findProperty ?Predlozheniepokonkursu.
            ("Predlozheniyapokonkursam" "Kompaniya") object:findProperty ?Kompaniya.
            ("Kompanii" "sapNo") object:findProperty ?sapNo.
            ("Kompanii" "Naimenovanieorganizatsii" ) object:findProperty ?Naimenovanieorganizatsii.
            #выстаскиваем данные
            ?item ?Pozitsiyazayavkinazakupku ?PozitsiyazayavkinazakupkuVal.
            ?PozitsiyazayavkinazakupkuVal ?appPosId ?appPosIdVal.
            ?item ?Vybrannoepredlozhenie ?VybrannoepredlozhenieVal.
            ?VybrannoepredlozhenieVal ?Predlagaemayatsena ?PredlagaemayatsenaVal.
            ?VybrannoepredlozhenieVal ?Predlozheniepokonkursu ?PredlozheniepokonkursuVal.
            ?PredlozheniepokonkursuVal ?Kompaniya ?KompaniyaVal.
            or {?KompaniyaVal ?sapNo ?sapNoVal.}
            or {"noSapNo" -> ?sapNoVal.}.
            or {?KompaniyaVal ?Naimenovanieorganizatsii ?NaimenovanieorganizatsiiVal.}
            or {"Без наименования" -> ?NaimenovanieorganizatsiiVal.}.
            
            variable:poss operator:add ?item. #добавляется элемент в массив
            # сетятся значения элемента массива
            (?item variable:appPosId) operator:replace ?appPosIdVal.
            (?item variable:price) operator:replace ?PredlagaemayatsenaVal.
            (?item variable:supplierName) operator:replace ?NaimenovanieorganizatsiiVal.
            (?item variable:sapNo) operator:replace ?sapNoVal.



            true -> ?value.
        }
        ```

## Тестирование

1. Создайте запись

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- 

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}