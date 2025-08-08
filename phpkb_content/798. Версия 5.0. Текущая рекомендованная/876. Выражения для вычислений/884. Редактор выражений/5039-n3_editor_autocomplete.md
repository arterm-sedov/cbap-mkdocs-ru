---
title: Предиктивный ввод в выражениях на языке N3
kbId: 5039
---

# Предиктивный ввод в выражениях на языке N3

## Введение

Для ввода выражений на языке N3 в редакторе выражений предусмотрены предиктивный ввод и подсказки:

- При вводе символов `@`, `?`, `:`, `^^`, префиксов, предикатов, имён объектов, функций и аргументов, а также при нажатии клавиш `Ctrl`+`Пробел` отображается список подходящих по контексту конструкций и сущностей.
- При вводе имён функций и объектов отображаются подсказки с их описанием.

Примечание

Примеры выражений на языке N3 в данном разделе составлены для вычисления значений атрибутов. См. *«[Вычисляемые атрибуты][attribute_calculated]»*.

Обычно (например, в выражениях, по которым вычисляются значения атрибутов), в системной переменной `item` содержится **ID** текущей записи (входные данные), а в переменную `value` помещаются выходные данные.

В выражениях, задающих фильтры (например, фильтр для таблиц), доступна только переменная `item`, в которую помещается результат вычисления выражения.

## Объявление префикса

1. Введите символ `@`.
2. Отобразится список доступных префиксов.
3. Выберите префикс в списке, чтобы просмотреть его описание и URI.

_![Список доступных префиксов N3 с описанием](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_prefix_autocomplete.png)_

4. Дважды нажмите префикс, например `math`, чтобы вставить его в выражение.

Пример: префикс math для математических функций```
@prefix math: <http://www.w3.org/2000/10/swap/math#>.

```

## Ввод заготовки конструкции на языке N3

1. Введите фигурные скобки `{ }` в пустое выражение (после [префиксов](#n3_editor_autocomplete_prefix)).
2. Внутри фигурных скобок нажмите клавиши `Ctrl`+`Пробел`.
3. Отобразится список доступных конструкций.
4. Выберите конструкцию в списке, чтобы просмотреть её описание.

   ![Список доступных конструкций N3](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_block_autocomplete.png)

   Список доступных конструкций N3
5. Дважды нажмите конструкцию в списке, чтобы вставить её заготовку в выражение.

Пример: заготовка конструкции if-then-else```
{
if { }
  then { }
  else { }.
}

```

## Ввод предиката

1. В позиции предиката нажмите клавиши `Ctrl`+`Пробел`.
2. Отобразится список [объявленных префиксов](#n3_editor_autocomplete_prefix).

   ![Список доступных префиксов](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_predicate_prefix_autocomplete.png)

   Список доступных префиксов
3. Выберите префикс в списке, чтобы просмотреть его описание.
4. Дважды нажмите префикс, например `task`, чтобы вставить его в выражение.
5. В позиции после префикса введите двоеточие `:`.
6. Отобразится список функций для префикса.

   ![Список функций для префикса](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_predicate_prefix_function_autocomplete.png)

   Список функций для префикса
7. Дважды нажмите имя функции, например `objectId`, чтобы вставить его в выражение.

Пример: выражение, возвращающее ID исполнителей активных задач для текущей записи```
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

## Ввод имени переменной

1. Введите фигурные скобки `{ }` в пустое выражение (после [префиксов](#n3_editor_autocomplete_prefix)).
2. Внутри фигурных скобок введите символ `?`. Этот список также можно вызвать, нажав клавиши `Ctrl`+`Пробел` в позиции после символа `?`.
3. Отобразится список доступных переменных.

   ![Список доступных переменных](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_variable_autocomplete.png)

   Список доступных переменных
4. Дважды нажмите имя переменной, например `value`, чтобы вставить его в выражение.

Пример: выражение, возвращающее список всех записей из шаблона аккаунта```
@prefix account: <http://comindware.com/ontology/account#>.
@prefix container: <http://comindware.com/ontology/container#>.
{
  # Получаем ID шаблона аккаунта Zakazchiki
  ?user container:alias "Zakazchiki".
  # Получаем список аккаунтов из шаблона Zakazchiki
  ?value account:extendedBy ?user.
}

```

## Ввод запроса ID атрибута с помощью функции object:findProperty

Функция `object:findProperty` возвращает ID атрибута шаблона по заданным системным именам шаблона и атрибута. По ID атрибута можно получить его значение.
При предиктивном вводе для неё формируется заготовка и для ввода аргументов отображаются списки подходящих шаблонов и атрибутов.

1. Внутри фигурных скобок нажмите клавиши `Ctrl`+`Пробел`.
2. В отобразившемся списке конструкций дважды нажмите функцию `FindProperty`.

   ![Список конструкций на языке N3](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_findproperty_autocomplete.png)

   Список конструкций на языке N3
3. В выражение будет вставлена заготовка функции:

   `( ) object:findProperty ?foundProperty`
4. В позиции первого аргумента (после открывающей скобки) нажмите клавиши `Ctrl`+`Пробел`.
5. Отобразится список подходящих шаблонов в приложении.

   ![Список шаблонов в приложении](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_findproperty_argument1_autocomplete.png)

   Список шаблонов в приложении
6. Дважды нажмите системное имя шаблона, например `Zayavkanaotpusk`, чтобы вставить его в выражение.
7. В позиции второго аргумента (через пробел после первого) нажмите клавиши `Ctrl`+`Пробел`.
8. Отобразится список атрибутов шаблона, выбранного на шаге 4.

   ![Список атрибутов шаблона](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_findproperty_argument2_autocomplete.png)

   Список атрибутов шаблона
9. Дважды нажмите системное имя атрибута, например `_creationDate`, чтобы вставить его в выражение.

Пример: выражение, возвращающее месяц по значению атрибута типа «Дата и время»```
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

## Ввод запроса списка записей шаблона по его системному имени с помощью функции object:alias

Функция `object:alias` возвращает записи шаблона с заданным системным именем. При предиктивном вводе для неё формируется заготовка, отображается список подходящих шаблонов и формируется компактный запрос записей выбранного шаблона с использованием квадратных скобок.

1. Внутри фигурных скобок нажмите клавиши `Ctrl`+`Пробел`.
2. В отобразившемся списке конструкций дважды нажмите функцию `ObjectAlias`.

   ![Список конструкций на языке N3](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_square_brackets_autocomplete.png)

   Список конструкций на языке N3
3. В выражение будет вставлена заготовка функции:

   ```
   a [object:alias ].

   ```
4. В позиции перед закрывающей квадратной скобкой нажмите клавиши `Ctrl`+`Пробел`.
5. Отобразится список шаблонов в приложении.

   ![Список шаблонов в приложении](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_square_brackets_templates_autocomplete.png)

   Список шаблонов в приложении
6. Дважды нажмите системное имя шаблона, например `Zayavkanaotpusk`.
7. В выражение будет вставлен запрос записей выбранного шаблона:

   ```
   ?objectZayavkanaotpusk a [object:alias "Zayavkanaotpusk"].

   ```
8. Чтобы присвоить результат выражения значению вычисляемого атрибута, замените имя переменной `objectZayavkanaotpusk` на `value`.

Пример: компактное выражение, возвращающее все записи шаблона по его системному имени```
@prefix object: <http://comindware.com/ontology/object#>.
{
  # Получаем список записей шаблона Zayavkanaotpusk
  ?value a [object:alias "Zayavkanaotpusk"].
}

```

Эквивалентное выражение без квадратных скобок```
@prefix object: <http://comindware.com/ontology/object#>.
{
  # Получаем ID шаблона Zayavkanaotpusk
  ?zayavkiTemplate object:alias "Zayavkanaotpusk".
  # Получаем список записей шаблона Zayavkanaotpusk
  ?value a ?zayavkiTemplate.
}

```

## Ввод запроса списка записей шаблона с заданным значением атрибута с помощью функции object:findObject

Функция `object:findObject` возвращает список записей шаблона по заданным системным именам приложения, шаблона и атрибута и значению атрибута.
При предиктивном вводе для неё формируется заготовка и для ввода аргументов отображаются списки подходящих приложений, шаблонов и атрибутов.

1. Внутри фигурных скобок нажмите клавиши `Ctrl`+`Пробел`.
2. В отобразившемся списке конструкций дважды нажмите функцию `FindObject`.

   ![Список конструкций на языке N3](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_findobject_autocomplete.png)

   Список конструкций на языке N3
3. В выражение будет вставлена заготовка функции:

   ```
   ( ) object:findObject ?foundObject

   ```
4. Чтобы присвоить результат выражения значению вычисляемого атрибута, замените имя переменной `foundObject` на `value`.
5. В позиции первого аргумента (после открывающей скобки) нажмите клавиши `Ctrl`+`Пробел`.
6. Отобразится список подходящих шаблонов в приложении.

   ![Список приложений](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_findobject_argument1_autocomplete.png)

   Список приложений
7. Дважды нажмите системное имя приложения, например `Upravlenieavtoparkom`, чтобы вставить его в выражение.
8. В позиции второго аргумента (через пробел после первого) нажмите клавиши `Ctrl`+`Пробел`.
9. Отобразится список шаблонов в приложении, выбранном на шаге 6.

   ![Список шаблонов в приложении](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_findobject_argument2_autocomplete.png)

   Список шаблонов в приложении
10. Дважды нажмите системное имя шаблона, например `Avtomobil`, чтобы вставить его в выражение.
11. В позиции третьего аргумента (через пробел после второго) нажмите клавиши `Ctrl`+`Пробел`.
12. Отобразится список атрибутов шаблона, выбранного на шаге 10.

    ![Список атрибутов шаблона](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_findobject_argument3_autocomplete.png)

    Список атрибутов шаблона
13. Дважды нажмите системное имя атрибута, например `Marka`, чтобы вставить его в выражение.
14. В позиции четвёртого аргумента (через пробела после третьего) введите в искомое значение выбранного атрибута, например `"Лада"`.

Пример: выражение, возвращающее список записей шаблона с заданным значением атрибута```
@prefix object: <http://comindware.com/ontology/object#>.
{
  # Получаем список записей шаблона Avtomobil из приложения Upravlenieavtoparkom,
  # в которых атрибут Marka имеет значение «Лада»
  ("Upravlenieavtoparkom""Avtomobil""Marka""Лада") object:findObject ?value.
}

```

## Ввод значений из атрибута типа «Список значений»

Если предикат определяет [атрибут типа «Список значений»][attribute_enum], предиктивный ввод подсказывает значения из этого списка.

1. Введите предикат, например `cmw:taskStatus`, который определяет системный [атрибут типа «Список значений»][attribute_enum], содержащий статус задачи.
2. В позиции через пробел после предиката нажмите клавиши `Ctrl`+`Пробел`.
3. В отобразившемся списке значений нажмите требуемое значение, например `taskStatus:inProgress` (активная задача), чтобы вставить его в выражение.

_![Список значений атрибута taskStatus](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_enum_autocomplete.png)_

Пример: выражение, возвращающее список задач со статусом «Выполняется»```
@prefix cmw: <http://comindware.com/logics#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
{
  ?value cmw:taskStatus taskStatus:inProgress.
}

```

## Ввод типа литерала

1. Введите литерал в кавычках, например `"P1D"` (1 день в формате ISO).
2. После кавычек введите символы `^^`.
3. Нажмите клавиши `Ctrl`+`Пробел`.
4. Отобразится список доступных типов литералов.
5. Дважды нажмите тип литерала, например `duration`, чтобы вставить его в выражение.

_![Список доступных типов литералов](/platform/v5.0/business_apps/expressions/expression_editor/n3_editor/img/n3_editor_literal_autocomplete.png)_

Пример: выражение, возвращающее конец текущего дня```
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

--8<-- "related_topics_heading.md"

- [Редактор выражений][expression_editor]
- [Примеры использования языка N3](https://kb.comindware.ru/category.php?id=879)
- [Атрибут типа «Список значений»][attribute_enum]

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
