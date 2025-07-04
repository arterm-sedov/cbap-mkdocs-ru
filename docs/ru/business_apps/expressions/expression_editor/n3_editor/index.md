---
title: Предиктивный ввод в выражениях на языке N3
kbId: 5039
tags:
  - N3
  - ObjectAlias
  - аргументы
  - атрибут типа «Список значений»
  - атрибуты
  - выражения
  - вычисляемые атрибуты
  - задача
  - квадратные скобки
  - литерал
  - object:alias
  - операторы
  - переменные
  - подсказки
  - предиктивный ввод
  - предикаты
  - префиксы
  - приложения
  - проверка значения
  - редактор выражений
  - сценарии
  - системное имя
  - список значений
  - статус задачи
  - тип литерала
  - тройки
  - функции
  - шаблоны
  - enum
  - findObject
  - findProperty
  - taskStatus
  - xsd
hide:
  - tags
---

# Предиктивный ввод в выражениях на языке N3 {: #n3_editor_autocomplete }

## Введение

Для ввода выражений на языке N3 в редакторе выражений предусмотрены предиктивный ввод и подсказки:

* При вводе символов `@`, `?`, `:`, `^^`, префиксов, предикатов, имён объектов, функций и аргументов, а также при нажатии клавиш ++ctrl+space++ отображается список подходящих по контексту конструкций и сущностей.
* При вводе имён функций и объектов отображаются подсказки с их описанием.
<!-- * При наличии ошибки в выражении после нажатия клавиш ++ctrl+space++ отображается сообщение об ошибке с указанием её позиции в коде. -->

<!-- _![Сообщение об ошибке при предиктивном вводе](n3_autocomplete_error_message.png)_ -->

!!! Note "Примечание"
    Примеры выражений на языке N3 в данном разделе составлены для вычисления значений атрибутов. См. _«[Вычисляемые атрибуты][attribute_calculated]»_.

    Обычно (например, в выражениях, по которым вычисляются значения атрибутов), в системной переменной `item` содержится **ID** текущей записи (входные данные), а в переменную `value` помещаются выходные данные.

    В выражениях, задающих фильтры (например, фильтр для таблиц), доступна только переменная `item`, в которую помещается результат вычисления выражения.

## Объявление префикса {: #n3_editor_autocomplete_prefix .pageBreakBefore }

1. Введите символ `@`.
2. Отобразится список доступных префиксов.
3. Выберите префикс в списке, чтобы просмотреть его описание и URI.
_![Список доступных префиксов N3 с описанием](n3_editor_prefix_autocomplete.png)_
4. Дважды нажмите префикс, например `math`, чтобы вставить его в выражение.

``` turtle title="Пример: префикс math для математических функций"
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
```

## Ввод заготовки конструкции на языке N3 {: #n3_editor_autocomplete_block .pageBreakBefore }

1. Введите фигурные скобки `{  }` в пустое выражение (после [префиксов](#n3_editor_autocomplete_prefix)).
2. Внутри фигурных скобок нажмите клавиши ++ctrl+space++.
3. Отобразится список доступных конструкций.
4. Выберите конструкцию в списке, чтобы просмотреть её описание.

    _![Список доступных конструкций N3](n3_editor_block_autocomplete.png)_

5. Дважды нажмите конструкцию в списке, чтобы вставить её заготовку в выражение.

``` turtle title="Пример: заготовка конструкции if-then-else"
{
if { }
  then { }
  else { }.
}
```

## Ввод предиката {: #n3_editor_autocomplete_predicate .pageBreakBefore  }

1. В позиции предиката нажмите клавиши ++ctrl+space++.
2. Отобразится список [объявленных префиксов](#n3_editor_autocomplete_prefix).

    _![Список доступных префиксов](n3_editor_predicate_prefix_autocomplete.png)_

3. Выберите префикс в списке, чтобы просмотреть его описание.
4. Дважды нажмите префикс, например `task`, чтобы вставить его в выражение.
5. В позиции после префикса введите двоеточие `:`.
6. Отобразится список функций для префикса.

    _![Список функций для префикса](n3_editor_predicate_prefix_function_autocomplete.png)_

7. Дважды нажмите имя функции, например `objectId`, чтобы вставить его в выражение.

``` turtle title="Пример: выражение, возвращающее ID исполнителей активных задач для текущей записи"
# Это выражение подходит для использования в вычисляемом атрибуте
# Импортируем функции для работы с логикой, задачами,
# статусами задач, аккаунтами и ролями.
@prefix cmw: <http://comindware.com/logics#>.
@prefix task: <http://comindware.com/ontology/task#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix role: <http://comindware.com/ontology/role#>.
{
    # Получаем задачи, связанные с текущей записью.
    # Если выражение используется в таблице задач процесса, 
    # то эта строка не требуется, т. к. контекст уже будет задачами.
    ?tasks task:objectId ?item.
    # Получаем активные задачи.
    ?tasks cmw:taskStatus taskStatus:inProgress.
    # Получаем фактических и возможных исполнителей задач.
    # Проверяем различные варианты назначения задач.
    or{
        # Возвращаем фактического исполнителя,
        # если он назначен через группы и роли.
        ?tasks cmw:assignee ?assigneeRoles.
        ?assigneeRoles role:roleMembers ?groupMembers.
        ?groupMembers account:groupUsers ?value.
    }
    or {

        # Возвращаем фактического исполнителя,
        # если он назначен через роли.
        ?tasks cmw:assignee ?assigneeRoles.
        ?assigneeRoles role:roleMembers ?value.
    }
    or {
        # Возвращаем фактического исполнителя,
        # если он назначен через аккаунт.
        ?tasks cmw:assignee ?value.
    }
    or{
        # Возвращаем список возможных исполнителей,
        # если они назначены через группы и роли.
        ?tasks cmw:possibleAssignee ?possibleRoles.
        ?assigneeRoles role:roleMembers ?groupMembers.
        ?groupMembers account:groupUsers ?value.
    }
    or {

        # Возвращаем список возможных исполнителей,
        # если они назначены через роли.
        ?tasks cmw:possibleAssignee ?possibleRoles.
        ?assigneeRoles role:roleMembers ?value.
    }
    or {
        # Возвращаем список возможных исполнителей,
        # если они назначены через аккаунты.
        ?tasks cmw:possibleAssignee ?value.
    }.
    # Оставляем только активные аккаунты.
    ?value account:active true.
    # Исключаем отключенные аккаунты
    not {?value cmw:isDisabled true.}.
}
```

## Ввод имени переменной {: .pageBreakBefore }

1. Введите фигурные скобки `{  }` в пустое выражение (после [префиксов](#n3_editor_autocomplete_prefix)).
2. Внутри фигурных скобок введите символ `?`. Этот список также можно вызвать, нажав клавиши ++ctrl+space++ в позиции после символа `?`.
3. Отобразится список доступных переменных.

    _![Список доступных переменных](n3_editor_variable_autocomplete.png)_

4. Дважды нажмите имя переменной, например `value`, чтобы вставить его в выражение.

``` turtle title="Пример: выражение, возвращающее список всех записей из шаблона аккаунта"
@prefix account: <http://comindware.com/ontology/account#>.
@prefix container: <http://comindware.com/ontology/container#>.
{
  # Получаем ID шаблона аккаунта Zakazchiki
  ?user container:alias "Zakazchiki".
  # Получаем список аккаунтов из шаблона Zakazchiki
  ?value account:extendedBy ?user.
}
```

## Ввод запроса ID атрибута с помощью функции object:findProperty {: .pageBreakBefore }

Функция `#!turtle object:findProperty` возвращает ID атрибута шаблона по заданным системным именам шаблона и атрибута. По ID атрибута можно получить его значение.
При предиктивном вводе для неё формируется заготовка и для ввода аргументов отображаются списки подходящих шаблонов и атрибутов.

1. Внутри фигурных скобок нажмите клавиши ++ctrl+space++.
2. В отобразившемся списке конструкций дважды нажмите функцию `FindProperty`.

    _![Список конструкций на языке N3](n3_editor_findproperty_autocomplete.png)_

3. В выражение будет вставлена заготовка функции:

    ```#!turtle
    ( ) object:findProperty ?foundProperty
    ```

4. В позиции первого аргумента (после открывающей скобки) нажмите клавиши ++ctrl+space++.
5. Отобразится список подходящих шаблонов в приложении.

    _![Список шаблонов в приложении](n3_editor_findproperty_argument1_autocomplete.png)_

6. Дважды нажмите системное имя шаблона, например `Zayavkanaotpusk`, чтобы вставить его в выражение.
7. В позиции второго аргумента (через пробел после первого) нажмите клавиши ++ctrl+space++.
8. Отобразится список атрибутов шаблона, выбранного на шаге 4.

    _![Список атрибутов шаблона](n3_editor_findproperty_argument2_autocomplete.png)_

9. Дважды нажмите системное имя атрибута, например `_creationDate`, чтобы вставить его в выражение.

{% include-markdown ".snippets/pdfPageBreakHard.md" %}

``` turtle title="Пример: выражение, возвращающее месяц по значению атрибута типа «Дата и время»"
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwtime: <http://comindware.com/logics/time#>.
{
    # Находим атрибут _creationDate шаблона Zayavkanaotpusk
    ("Zayavkanaotpusk" "_creationDate") object:findProperty ?dtProperty.

    # Определяем значение атрибута _creationDate
    # в текущей записи шаблона Zayavkanaotpusk
    ?item ?dtProperty ?dmonth.
    # Извлекаем номер месяца из значения атрибута _creationDate
    ?dmonth cmwutc:month ?value.
}
```

## Ввод запроса списка записей шаблона по его системному имени с помощью функции object:alias {: .pageBreakBefore }

Функция `#!turtle object:alias` возвращает записи шаблона с заданным системным именем. При предиктивном вводе для неё формируется заготовка, отображается список подходящих шаблонов и формируется компактный запрос записей выбранного шаблона с использованием квадратных скобок.

1. Внутри фигурных скобок нажмите клавиши ++ctrl+space++.
2. В отобразившемся списке конструкций дважды нажмите функцию `ObjectAlias`.

    _![Список конструкций на языке N3](n3_editor_square_brackets_autocomplete.png)_

3. В выражение будет вставлена заготовка функции:

    ``` turtle
    a [object:alias ].
    ```

4. В позиции перед закрывающей квадратной скобкой нажмите клавиши ++ctrl+space++.
5. Отобразится список шаблонов в приложении.

    _![Список шаблонов в приложении](n3_editor_square_brackets_templates_autocomplete.png)_

6. Дважды нажмите системное имя шаблона, например `Zayavkanaotpusk`.
7. В выражение будет вставлен запрос записей выбранного шаблона:

    ``` turtle
    ?objectZayavkanaotpusk a [object:alias "Zayavkanaotpusk"].
    ```

8. Чтобы присвоить результат выражения значению вычисляемого атрибута, замените имя переменной `objectZayavkanaotpusk` на `value`.

{% include-markdown ".snippets/pdfPageBreakHard.md" %}

``` turtle title="Пример: компактное выражение, возвращающее все записи шаблона по его системному имени"
@prefix object: <http://comindware.com/ontology/object#>.
{
  # Получаем список записей шаблона Zayavkanaotpusk
  ?value a [object:alias "Zayavkanaotpusk"].
}
```

``` turtle title="Эквивалентное выражение без квадратных скобок"
@prefix object: <http://comindware.com/ontology/object#>.
{
  # Получаем ID шаблона Zayavkanaotpusk
  ?zayavkiTemplate object:alias "Zayavkanaotpusk".
  # Получаем список записей шаблона Zayavkanaotpusk
  ?value a ?zayavkiTemplate.
}
```

## Ввод запроса списка записей шаблона с заданным значением атрибута с помощью функции object:findObject {: .pageBreakBefore }

Функция `#!turtle object:findObject` возвращает список записей шаблона по заданным системным именам приложения, шаблона и атрибута и значению атрибута.
При предиктивном вводе для неё формируется заготовка и для ввода аргументов отображаются списки подходящих приложений, шаблонов и атрибутов.

1. Внутри фигурных скобок нажмите клавиши ++ctrl+space++.
2. В отобразившемся списке конструкций дважды нажмите функцию `FindObject`.

    _![Список конструкций на языке N3](n3_editor_findobject_autocomplete.png)_

3. В выражение будет вставлена заготовка функции:

    ``` turtle
    ( ) object:findObject ?foundObject
    ```

4. Чтобы присвоить результат выражения значению вычисляемого атрибута, замените имя переменной `foundObject` на `value`.
5. В позиции первого аргумента (после открывающей скобки) нажмите клавиши ++ctrl+space++.
6. Отобразится список подходящих шаблонов в приложении.

    _![Список приложений](n3_editor_findobject_argument1_autocomplete.png)_

7. Дважды нажмите системное имя приложения, например `Upravlenieavtoparkom`, чтобы вставить его в выражение.
8. В позиции второго аргумента (через пробел после первого) нажмите клавиши ++ctrl+space++.
9. Отобразится список шаблонов в приложении, выбранном на шаге 6.

    _![Список шаблонов в приложении](n3_editor_findobject_argument2_autocomplete.png)_

10. Дважды нажмите системное имя шаблона, например `Avtomobil`, чтобы вставить его в выражение.
11. В позиции третьего аргумента (через пробел после второго) нажмите клавиши ++ctrl+space++.
12. Отобразится список атрибутов шаблона, выбранного на шаге 10.

    _![Список атрибутов шаблона](n3_editor_findobject_argument3_autocomplete.png)_

13. Дважды нажмите системное имя атрибута, например `Marka`, чтобы вставить его в выражение.
14. В позиции четвёртого аргумента (через пробела после третьего) введите в искомое значение выбранного атрибута, например `"Лада"`.

``` turtle title="Пример: выражение, возвращающее список записей шаблона с заданным значением атрибута"
@prefix object: <http://comindware.com/ontology/object#>.
{
  # Получаем список записей шаблона Avtomobil из приложения Upravlenieavtoparkom,
  # в которых атрибут Marka имеет значение «Лада»
  ("Upravlenieavtoparkom""Avtomobil""Marka""Лада") object:findObject ?value.
}
```

## Ввод значений из атрибута типа «Список значений» {: .pageBreakBefore }

Если предикат определяет [атрибут типа «Список значений»][attribute_enum], предиктивный ввод подсказывает значения из этого списка.

1. Введите предикат, например `#!turtle cmw:taskStatus`, который определяет системный [атрибут типа «Список значений»][attribute_enum], содержащий статус задачи.
2. В позиции через пробел после предиката нажмите клавиши ++ctrl+space++.
3. В отобразившемся списке значений нажмите требуемое значение, например `#!turtle taskStatus:inProgress` (активная задача), чтобы вставить его в выражение.

_![Список значений атрибута taskStatus](n3_editor_enum_autocomplete.png)_

``` turtle title="Пример: выражение, возвращающее список задач со статусом «Выполняется»"
@prefix cmw: <http://comindware.com/logics#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
{
  ?value cmw:taskStatus taskStatus:inProgress.
}
```

## Ввод типа литерала

1. Введите литерал в кавычках, например `"P1D"` (1 день в формате ISO).
2. После кавычек введите символы `^^`.
3. Нажмите клавиши ++ctrl+space++.
4. Отобразится список доступных типов литералов.
5. Дважды нажмите тип литерала, например `duration`, чтобы вставить его в выражение.

_![Список доступных типов литералов](n3_editor_literal_autocomplete.png)_

``` turtle title="Пример: выражение, возвращающее конец текущего дня"
@prefix session: <http://comindware.com/ontology/session#>.
@prefix cmwutc: <http://comindware.com/logics/time/utc#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix cmwdur: <http://comindware.com/logics/time/duration#>.
{
  # Текущее время в UTC
  session:context session:requestTime ?nowUTC.
  # Время начала текущего дня
  ?nowUTC cmwutc:startOfDay ?startOfTodayUTC.
  # Начало следующих суток = время начала текущего дня + 1 сутки
  (?startOfTodayUTC "P1D"^^xsd:duration) cmwdur:add ?value.
}
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Редактор выражений][expression_editor]
- [Примеры использования языка N3][n3_use_examples]
- [Атрибут типа «Список значений»][attribute_enum]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
