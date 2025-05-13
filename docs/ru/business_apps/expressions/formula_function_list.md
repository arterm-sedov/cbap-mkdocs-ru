---
title: Список функций языка формул
kbId: 4993
tags:
    - язык выражений
    - язык формул
    - выражения
    - формулы
    - enum
    - enumvalue
    - справочник функций
hide:
    - tags
---

# Список функций языка формул {{ companyName }} {: #formula_function_reference }

Здесь представлен синтаксис и примеры использования функций в формулах **{{ companyName }}**.

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADD()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Суммирует два значения. Конкатенация строк не поддерживается.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADD(value1, value2)
```

</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `value1`: число, `value2`: число.
- `value1`: длительность, `value2`: длительность.
- `value1`: дата и время, `value2`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">

- Число
- Длительность
- Дата и время

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADD(DATE('2024-01-01T01:01:01'), DURATION('P3Y6M4DT12H30M5S'))
```

Результат: `03.07.2027 13:31:06`

Здесь:

- `DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
- `DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDDAYS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное число дней к значению типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDDAYS(dateTime, numberOfDays)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfDays`: количество дней, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDDAYS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `04.01.2024 1:01:01`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDDAYSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество дней к значению типа «**Дата и время**» с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDDAYSUTC(dateTime, numberOfDays)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfDays`: количество дней, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDDAYSUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат: `04.01.2024 4:01:01`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDDUR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Суммирует два значения типа «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDDUR(duration1, duration2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`duration1`, `duration2`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDDUR(DURATION('P1DT12H30M5S'), DURATION('P1DT12H30M5S'))
```

Результат: `3 д 1 ч 10 с`

Здесь:

`DURATION()` — преобразует в длительность  строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDHOURS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество часов к значению типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDHOURS(dateTime, number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `number`: количество часов, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDHOURS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 4:01:01`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDHOURSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество часов к значению типа «**Дата и время**» с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDHOURSUTC(dateTime, number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `number`: количество часов, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDHOURSUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат: `01.01.2024 7:01:01` для часового пояса UTC+3.

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDLOC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет значение типа «**Длительность**» к значению типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDLOC(dateTime, duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `duration`: длительность, которую требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDLOC(DATE('2024-01-01T01:01:01'), DURATION('P1DT12H30M5S'))
```

Результат: `02.01.2024 13:31:06`

Здесь:

- `DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
- `DURATION()` — преобразует в длительность  строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDMINUTES()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество минут к значению типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDMINUTES(dateTime, numberOfMinutes)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfMinutes`: количество минут, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDMINUTES(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 1:04:01`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDMINUTESUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество минут к значению типа «**Дата и время**» с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDMINUTESUTC(dateTime, numberOfMinutes)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfMinutes`: количество минут, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDMINUTESUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат: `01.01.2024 4:04:01` для часового пояса UTC+3.

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDMONTHS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество месяцев к значению типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDMONTHS(dateTime, numberOfMonths)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfMonths`: количество месяцев, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDMONTHS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.04.2024 1:01:01`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDMONTHSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество месяцев к значению типа «**Дата и время**» с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDMONTHSUTC(dateTime, numberOfMonths)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfMonths`: количество месяцев, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDMONTHSUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат: `01.04.2024 4:01:01` для часового пояса UTC+3.

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDSECONDS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество секунд к значению типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDSECONDS(dateTime, number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `number`: количество секунд, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDSECONDS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 1:01:04`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDSECONDSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество секунд к значению типа «**Дата и время**» с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDSECONDSUTC(dateTime, number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `number`: количество секунд, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDSECONDSUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат: `01.01.2024 4:01:04` для часового пояса UTC+3.

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет значение типа «**Длительность**» к значению типа «**Дата и время**» с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDUTC(dateTime, duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `Duration`: длительность, которую требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDUTC(DATE('2024-01-01T01:01:01+00:00'), DURATION('P1DT12H30M5S'))
```

Результат: `02.01.2024 16:31:06` для часового пояса UTC+3.

Здесь:

- `DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
- `DURATION()` — преобразует в длительность  строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDYEARS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество лет к значению типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDYEARS(dateTime, number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `number`: количество лет, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDYEARS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2027 1:01:01`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDYEARSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Добавляет указанное количество лет к значению типа «**Дата и время**» с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDYEARSUTC(dateTime, number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `number`: количество лет, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDYEARSUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат: `01.01.2027 4:01:01` для часового пояса UTC+3.

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ALL()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Берёт список логических переменных и возвращает значение `true`, если все логические переменные принимают значение `true`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>

<td markdown="block">

``` cs
ALL(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list`: список логических значений или выражений, результатом которых являются логические значения.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ALL(LIST(BOOL("true"), BOOL("true"), BOOL("false")))
```

Результат: `False`

Здесь:

- [`BOOL()`](#bool) — преобразует строку в логическое значение.
- [`LIST()`](#list) — определяет список. Берёт перечисление значений, разделяет их запятыми и возвращает список.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `AND()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Берёт два логических значения или два выражения, результатом которых являются логические значения, и возвращает результат логического умножения этих значений.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
AND(bool1, bool2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`bool1`, `bool2`: логическое значение или выражение, возвращающее логическое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
AND(BOOL("true"), BOOL("true"))
```

Результат: `True`

Здесь:

- [`BOOL()`](#bool) — преобразует строку в логическое значение.
- [`LIST()`](#list) — определяет список. Берёт перечисление значений, разделяет их запятыми и возвращает список.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ANY()` {: #any_not_empty }

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Проверка на непустую последовательность.

Проверяет список на не пустоту.

По условию выборки формирует последовательность значений любого типа и проверяет её на не пустоту.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ANY(list), ANY((sequence))
```

Для задания последовательности используйте стандартный запрос `from where select`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `list`: список значений любого типа
- `sequence`: условие выборки

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ANY( from I in db->Tickets where i->product = 'Data Monsoon' select i->name)
```

Результат: `True`, если хотя бы один элемент имеет значение предиката `product` равным `Data Monsoon`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ANY()` {: #any_predicate }

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Проверка предиката.

Формирует выборку элементов и проверяет, что в ней есть хотя бы один элемент с истинным значением заданного предиката.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ANY([(query), queryVar, boolEval])
```

</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `query`: запрос типа `from where select`, который возвращает последовательность элементов.
- `queryVar`: локальная переменная, используемая в запросе.
- `boolEval`: логическое утверждение об элементе последовательности, результатом которого является логическое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ANY([(
    from i in db->Tickets where i->product=='Data Monsoon' select i),
    i,
    i->NeedsQAHelp
    ])
```

Результат: `True`, если поступил хотя бы один запрос по продукту `Data Monsoon`, для которого значение атрибута `NeedsQAHelp` равно `true`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ASCENDING()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Сортирует элементы последовательности в порядке возрастания.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ASCENDING(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`list`: список чисел или строк
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Отсортированный список значений
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ASCENDING('л', 'а', 'и')
```

Результат: `(SimpleString:а SimpleString:и SimpleString:л)`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `AVERAGE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает среднее арифметическое аргументов.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
AVERAGE(value1, value2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`value1`, `value2`: число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
AVERAGE(1, 3, 4, 7, 10)
```

Результат: `5`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `BETWEEN()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Проверяет факт вхождения даты или длительности в заданный диапазон. Значения типа «**Дата и время**» должны быть в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
BETWEEN(value, min, max)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `value` — дата и время или длительность для проверки.
- `min` — начальное значение диапазона.
- `max` — конечное значение диапазона.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
BETWEEN(DURATION("PT3H15M"), DURATION("PT3H1M"), DURATION("PT3H25M"))
```

Результат: `True`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `BETWEENUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Проверяет факт вхождения даты или длительности в заданный диапазон. Значения типа «**Дата и время**» должны быть с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
BETWEENUTC(value, min, max)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `value` — дата и время или длительность для проверки.
- `min` — начальное значение диапазона.
- `max` — конечное значение диапазона.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
BETWEENUTC(DATE("2023-01-15+00:00"), DATE("2024-02-15+01:00"), DATE("2024-08-15-01:00"))
```

Результат: `False`

Здесь:

- `DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `BOOL()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Преобразует строку в логический значение. Для правильной конвертации значение строки должно быть равно `true` или `false` без учёта регистра.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
BOOL(string)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string` — строка, которая преобразуется в логическое значение, со значением `true` или `false` (без учёта регистра). При неподходящих значениях атрибута (0, 1, истина, ложь и т. п.) функция возвращает пустое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
BOOL('TrUE')
```

Результат: `True`
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CEILING()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Округляет до ближайшего бо́льшего целого.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
CEILING(number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`number` — число, которое будет округлено.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CEILING(4.1)
```

Результат: `5`
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CENTURY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее веку указанной даты в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
CENTURY(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime` — дата, для которой требуется определить век.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CENTURY(DATE("2000-01-01T05:45:15"))
```

Результат: `21`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CENTURYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее веку указанной даты с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
CENTURYUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime` — дата, для которой требуется определить век.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CENTURYUTC(DATE("2000-01-01T05:45:15+10:00"))
```

Результат: `20`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `COMPARE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Сравнивает два значения длительности и возвращает целое число:

- `1`, если первая длительности больше второй;
- `0`, если длительности равны;
- `-1`, если первая длительность короче второй.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
COMPARE(duration1, duration2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`duration1`, `duration2`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
COMPARE(DURATION("PT3H15M"), DURATION("PT3H16M"))
```

Возвращает `-1`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CONCAT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Преобразует список строк в одну объединённую.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
CONCAT(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list` — список строк, которые требуется объединить.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CONCAT(LIST("Сумма доходов равна: ", "100000"))
```

Результат: `Сумма доходов равна: 100000`

Здесь:

[`LIST()`](#list) — функция, которая принимает значения, разделённые запятыми, и возвращает их список.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CONTAINS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает две строки между собой. Если первая строка содержит вторую, то возвращает логическое значение `true`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
CONTAINS(string, substring)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `string` — строка, в которой происходит поиск подстроки.
- `substring` — подстрока, которая ищется в строке.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CONTAINS("Это срочная заявка.", "срочн")
```

Результат: `True`
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CONVERTTIMEZONE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Переводит значение типа «**Дата и время**» из часового пояса, заданного на форме, в настройках аккаунта или глобальной конфигурации или указанного в значении аргумента, в заданный часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
CONVERTTIMEZONE(date, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `date` — дата и время.
- `timeZone` — целевой часовой пояс.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CONVERTTIMEZONE(DATE("2025-05-05T13:45:15+00:00"), "Europe/London")
```

Результат: `05.05.2025 14:45:15` для часового пояса UTC+3.

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CONVERTTIMEZONEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Переводит значение типа «**Дата и время**» с указанием часового пояса в формате UTC в заданный часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
CONVERTTIMEZONEUTC(date, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `date` — дата с указанием часового пояса с указанием часового пояса в формате UTC.
- `timeZone` — целевой часовой пояс.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CONVERTTIMEZONEUTC(DATE("2025-05-05T13:45:15+00:00"), "Europe/Moscow")
```

Результат: `05.05.2025 16:45:15`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `COUNT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает количество элементов в списке.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
COUNT(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list`: список элементов
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
COUNT(LIST("a", 2, "c", "d", 5))
```

Результат: `5`

Здесь:

[`LIST()`](#list) — функция, которая принимает значения, разделённые запятыми, и возвращает их список.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CREATEDATE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Преобразует числовые аргументы в значение типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
CREATEDATE(year, month, day)
```

**или**

``` cs
CREATEDATE(year, month, day, hour, minute, second)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`year, month, day, hour, minute, second`: число.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CREATEDATE(2025, 5, 5, 15, 45, 15)
```

Результат: `05.05.2025 15:45:15`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CREATEDATEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Преобразует числовые аргументы в значение типа «**Дата и время**» в часовом поясе с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
CREATEDATEUTC(year, month, day)
```

**или**

``` cs
CREATEDATEUTC(year, month, day, hour, minute, second)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`year, month, day, hour, minute, second`: число.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CREATEDATEUTC(2025, 5, 5, 15, 45, 15)
```

Результат: `05.05.2025 15:45:15`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее дню месяца указанной даты в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DAY(dateTime)
```

**или**

``` cs
DAY(dateTime, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `timeZone`: часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DAY(DATE("2025-05-05T23:45:15+00:00"), "Europe/Moscow")
```

Результат: `6`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAYOFWEEK()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает название дня недели указанной даты в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DAYOFWEEK(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DAYOFWEEK(DATE("2025-05-05T23:45:15"))
```

Результат: `понедельник`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAYOFWEEKUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает название дня недели указанной даты с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DAYOFWEEKUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DAYOFWEEKUTC(DATE("2025-05-05T23:45:15+00:00"))
```

Результат: `понедельник`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAYOFYEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает число, соответствующее дню года указанной даты в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DAYOFYEAR(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DAYOFYEAR(DATE("2025-05-05T23:45:15"))
```

Результат: `125`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAYOFYEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает число, соответствующее дню года указанной даты с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DAYOFYEARUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DAYOFYEARUTC(DATE("2025-05-05T23:45:15+00:00"))
```

Результат: `125`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAYS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает количество дней для аргумента типа «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DAYS(duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`duration`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DAYS(DURATION('P12DT64H75M1360S'))
```

Результат: `14,7344907407407`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAYSINMONTH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» или два аргумента типа «**Число**» и возвращает число, соответствующее количеству дней в месяце указанной даты в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DAYSINMONTH(dateTime)
```

**или**

``` cs
DAYSINMONTH(year, month)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `year, month`: число.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DAYSINMONTH(2024, 02)
```

Результат: `29`

``` cs
DAYSINMONTH(DATE("2025-02-05T23:45:15"))
```

Результат: `28`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAYSINMONTHUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» с указанием часового пояса в формате UTC или два аргумента типа «**Число**» и возвращает число, соответствующее количеству дней в месяце указанной даты.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DAYSINMONTHUTC(dateTime)
```

**или**

``` cs
DAYSINMONTHUTC(year, month)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `year, month`: число.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DAYSINMONTHUTC(2025, 02)
```

Результат: `28`

``` cs
DAYSINMONTHUTC(DATE("2025-02-28T23:45:15-02:00"))
```

Результат: `31`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» в формате и возвращает числовое значение, соответствующее дню месяца указанной даты.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DAYUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DAYUTC(DATE("2025-04-30T23:45:15-02:00"))
```

Результат: `1`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DECIMAL()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует строку в число типа `Decimal`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DECIMAL(string)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string` — строка с числовым значением (например, 10, 10,5, 10 000 для русского языка или 10, 10.5, 10,000 — для английского, т. е. значение интерпретируется в соответствии с языком текущего пользователя). При неподходящих значениях атрибута (1 р., $50 и т. п.) функция возвращает пустое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DECIMAL("10,5")
```

Результат: `10,5`
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DESCENDING()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Сортирует элементы последовательности в порядке убывания.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DESCENDING(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list`: список чисел или строк

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Отсортированный список значений
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DESCENDING('л', 'а', 'и')
```

Результат: `(SimpleString:л SimpleString:и SimpleString:а)`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DISTINCT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Сортирует элементы последовательности в порядке возрастания.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DISTINCT(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`list`: список чисел или строк
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Список уникальных значений
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DISTINCT(LIST('л', 'а', 'и', 'а', 'л'))
```

Результат: `л`, `а`, `и`

Здесь:

[`LIST`](#list) — определяет список. Берёт перечисление значений, разделяет их запятыми и возвращает список.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DIVIDE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Берёт в качестве аргументов два значения числового типа и возвращает результат деления одного на другое.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DIVIDE(dividend, divisor)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dividend`: число, делимое
- `divisor`: число, делитель

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DIVIDE (125, 25)
```

Результат: `5`
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `EMPTY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Проверяет, не является ли пустым значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
EMPTY(argument)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument`: атрибут или выражение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
EMPTY(DIVIDE(3, 3))
```

Результат: `False`

Здесь:

[`DIVIDE`](#divide) — берёт в качестве аргументов два значения числового типа и возвращает результат деления одного на другое.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFDAY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента, и возвращает дату и время окончания дня, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENDOFDAY(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ENDOFDAY(DATE('2025-05-05T01:01:01'))
```

Результат: `05.05.2025 23:59:59`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFDAYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» с указанием часового пояса в формате UTC и возвращает дату и время окончания дня, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENDOFDAYUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ENDOFDAYUTC(DATE('2025-05-05T01:01:01+03:00'))
```

Результат: `04.05.2025 23:59:59`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFMONTH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента, и возвращает дату и время окончания месяца, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENDOFMONTH(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ENDOFMONTH(DATE('2025-05-05T01:01:01'))
```

Результат: `31.05.2025 23:59:59`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFMONTHUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» с указанием часового пояса в формате UTC и возвращает дату и время окончания месяца, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENDOFMONTHUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ENDOFMONTHUTC(DATE('2025-05-01T01:01:01+03:00'))
```

Результат: `30.04.2025 23:59:59`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFQUARTER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента, и возвращает дату и время окончания квартала, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENDOFQUARTER(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ENDOFQUARTER(DATE('2025-04-01T01:01:01'))
```

Результат: `30.06.2025 23:59:59`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFQUARTERUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» с указанием часового пояса в формате UTC и возвращает дату и время окончания квартала, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENDOFQUARTERUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ENDOFQUARTERUTC(DATE('2025-04-01T01:01:01+03:00'))
```

Результат: `31.03.2025 23:59:59`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFWEEK()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента, и возвращает дату и время окончания недели, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENDOFWEEK(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ENDOFWEEK(DATE('2025-05-05T01:01:01'))
```

Результат: `11.05.2025 23:59:59`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFWEEKUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» с указанием часового пояса в формате UTC и возвращает дату и время окончания недели, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENDOFWEEKUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ENDOFWEEKUTC(DATE('2025-05-05T01:01:01+03:00'))
```

Результат: `04.05.2025 23:59:59`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFYEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента, и возвращает дату и время окончания года, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENDOFYEAR(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ENDOFYEAR(DATE('2025-01-01T01:01:01'))
```

Результат: `31.12.2025 23:59:59`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFYEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» с указанием часового пояса в формате UTC и возвращает дату и время окончания года, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENDOFYEARUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ENDOFYEARUTC(DATE('2025-01-01T01:01:01+03:00'))
```

Результат: `31.12.2024 23:59:59`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDSWITH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает две строки и возвращает значение `true`, если первая строка оканчивается на вторую строку, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENDSWITH(string, endString)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string`, `endString`: строка.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ENDSWITH("Строка", "ка")
```

Результат: `True`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENUMVALUE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Находит ID значения атрибута типа «**[Список значений][attribute_enum]**» по системным именам атрибута и значения.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ENUMVALUE("enumAttributeSystemName", "enumValueSystemName")
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `enumAttributeSystemName`: строка, системное имя атрибута типа «**Список значений**».
- `enumValueSystemName`: строка, системное имя одного из значений атрибута типа «**Список значений**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строку с ID искомого значения атрибута.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
EQUALS($Status, ID(ENUMVALUE("Status", "Resolved")))
```

Результат: `True`, если атрибут `Status` имеет значение`Resolved`.

Здесь:

- [`ID()`](#id) — приводит тип `string` к типу `id`, так как атрибут типа «**Список значений**» хранит ID своего текущего значения, а не его текстовое значение.
- [`EQUALS()`](#equals) — сравнивает значения двух аргументов.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `EQ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента типа «**Дата и время**» или «**Длительность**» и возвращает значение `true`, если они равны, в противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
EQ(value1, value2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `value1`, `value2`: дата и время.
- `value1`, `value2`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
EQ(DURATION('P2DT1H30M30S'), DURATION('P1DT25H30M30S'))
```

Результат: `True`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `EQUALS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает значения двух аргументов и возвращает `true`, если они равны, в противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
EQUALS(value1, value2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`value1`, `value2`: логическое значение, дата и время, число, строка или длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
EQUALS("string", 2)
```

Результат: `False`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `EQUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента типа «**Дата и время**» с указанием часового пояса в формате UTC и возвращает значение `true`, если они равны, в противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
EQUTC(dateTime1, dateTime2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime1`, `dateTime2`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
EQUTC(DATE('2025-01-01T01:01:01+03:00'), DATE('2025-01-01T00:01:01+02:00'))
```

Результат: `True`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `FIRST()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает первый элемент из списка. При отсутствии элементов в списке `FIRST()` возвращает пустое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
FIRST(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list`: список значений.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения совпадает с типом элементов списка.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
FIRST((from i in db->music where i->album == 'Whale Meditation' select i->song))
```

Результат: название первой песни из альбома `Whale Meditation`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `FIRSTCAPITAL()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует первую букву строки на заглавную.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
FIRSTCAPITAL(string)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string`: строка.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения совпадает с типом элементов списка.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
FIRSTCAPITAL("строка")
```

Результат: `Строка`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `FLOOR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Округляет число до ближайшего меньшего целого.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
FLOOR(number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`number`: число.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
FLOOR(5.9)
```

Результат: `5`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `FORMAT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Выполняет форматирование аргументов в соответствии с заданным шаблоном и возвращает отформатированную строку.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
FORMAT("stringToFormat {0} {1} ... {N}", LIST(value0, value1, ..., valueN))
```

Эта функция принимает строку с заполнителями вида `{0}`…`{N}` и список значений. Функция подставляет значения из списка в соответствующие заполнители и возвращает результирующую строку.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `"stringToFormat {0} {1} ... {N}"`: строка.
- `LIST(value0, value1, ..., valueN)`: список значений любых типов.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
FORMAT("Название: {0}, исполнитель: {1}", LIST("Yesterday","Beatles"))
```

Результат: `Название: Yesterday, исполнитель: Beatles`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `FORMATDUR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Выполняет форматирование значения типа «**Длительность**» в строку в формате ISO 8601.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
FORMATDUR(duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`duration`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
FORMATDUR($Duration)
```

Результат: `P<n>Y<n>M<n>DT<n>H<n>M<n>S`, где `<n>` — числовое значение, заданное в атрибуте `$Duration`.

Здесь:

`$Duration` — атрибут типа длительность.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `FORMATLOC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Выполняет форматирование значения типа «**Дата и время**» в строку заданного формата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
FORMATLOC(dateTime, formatString)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `formatString`: строка.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
FORMATLOC(DATE('2025-05-05T05:05:25'), "dd MMMM yyyy года hh:mm:ss")
```

Результат: `05 мая 2025 года 05:05:25`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `FORMATUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Выполняет форматирование значения типа «**Дата и время**» в формате UTC в строку заданного формата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
FORMATUTC(dateTime, formatString)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `formatString`: строка.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
FORMATUTC(DATE('2025-05-05T05:05:25+03:00'), "dd MMMM yyyy года hh:mm:ss")
```

Результат: `05 мая 2025 года 02:05:25`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `GE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Сравнивает значения двух аргументов типа «**Дата и время**» или «**Длительность**». Возвращает логическое значение `true`, если первый аргумент больше или равен второму, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
GE(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument1`, `argument2`: дата и время.
- `argument1`, `argument2`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
GE(DURATION('P1DT1H30M30S'), DURATION('P2DT1H30M30S'))
```

Результат: `False`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `GETSPAN()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Вычисляет длительность между значениями двух аргументов типа «**Дата и время**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
GETSPAN(dateTime1, dateTime2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime1`, `dateTime2`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
GETSPAN(DATE('2025-05-05T05:05:25'), DATE('2025-05-05T10:10:50'))
```

Результат: `-05:05:25`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `GETSPANUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Вычисляет длительность между значениями двух аргументов типа «**Дата и время**» с указанием часового пояса в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
GETSPANUTC(dateTime1, dateTime2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime1`, `dateTime2`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
GETSPANUTC(DATE('2025-05-05T05:05:25+00:00'), DATE('2025-05-05T05:05:25+05:00'))
```

Результат: `05:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `GEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает значения двух аргументов типа «**Дата и время**» с указанием часового пояса в формате UTC. Возвращает логическое значение `true`, если первый аргумент больше или равен второму, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
GEUTC(dateTime1, dateTime2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime1`, `dateTime2`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
GEUTC(DATE('2025-05-05T05:05:25+00:00'), DATE('2025-05-05T05:05:25+05:00'))
```

Результат: `True`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `GREATER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает логическое значение `true`, если значение первого аргумента больше второго, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
GREATER(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: число, строка, длительность или дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
GREATER(1, 0)
```

Результат: `True`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `GREATEREQ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает логическое значение `true`, если значение первого аргумента больше либо равно значению второго, в противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
GREATEREQ(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: число, строка, длительность или дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
GREATEREQ("Строка", "Сорока")
```

Результат: `True`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `GT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает логическое значение `true`, если значение первого аргумента типа «**Дата и время**» или «**Длительность**» больше значения второго, в противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
GT(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument1`, `argument2`: длительность
- `argument1`, `argument2`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
GT(DATE('2025-05-05T05:05:25'), DATE('2025-05-05T05:05:25'))
```

Результат: `False`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `GTUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает логическое значение `true`, если значение первого аргумента типа «**Дата и время**» с указанием часового пояса в формате UTC больше значения второго, в противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
GTUTC(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
GTUTC(DATE('2025-05-05T05:05:25+00:00'), DATE('2025-05-05T05:05:25+05:00'))
```

Результат: `True`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `HOUR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента и возвращает числовое значение, соответствующее часу указанной даты.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
HOUR(dateTime)
```

**или**

``` cs
HOUR(dateTime, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `timeZone`: строка, указание часового пояса в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
HOUR(DATE('2025-05-05T05:05:25+00:00'), "Europe/Moscow")
```

Результат: `8`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `HOURS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Длительность**» и возвращает числовое значение, соответствующее количеству часов.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
HOURS(duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`duration`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
HOURS(DURATION('P2DT1H0M0S'))
```

Результат: `49`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `HOURUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» с указанием часового пояса в формате UTC и возвращает числовое значение, соответствующее часу указанной даты.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
HOURUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
HOURUTC(DATE('2025-05-05T05:05:25+03:00'))
```

Результат: `2`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ID()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Преобразует строку с ID объекта в его идентификатор.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ID(objectID)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`objectID`: строка, системное имя объекта.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
ID объекта
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ID("oa.1")
```

Результат: идентификатор шаблона `oa.1`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `IF()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Использует в качестве аргументов значения или выражения, результатом которых является некоторое значение. Возвращает второй аргумент, если значение первого является логическим `true`, в противном случае возвращает третий аргумент.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
IF(argument1, argument2, argument3)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument1`: логическое значение или выражение, возвращающее логическое значение.
- `argument2`, `argument3`: значение любого типа или выражение, результатом которого является значение любого типа.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">

Тип возвращаемого значения тот же, что у аргументов `argument2` и `argument3`.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
IF(1==2, "Верно", "Не верно")
```

Результат: `Не верно`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `INDEXOF()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает номер позиции (отсчёт идёт от 0), на которой располагается искомая строка в исходной строке. Номер позиции также может отсчитываться от указанного значения.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
INDEXOF(sourceString, stringToFind, [startIndex])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `sourceString`: исходная строка.
- `stringToFind`: искомая строка.
- `startIndex`: номер позиции, от которой производится отсчёт.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
INDEXOF("У ёлки иголки колки.", "лки", 4")
```

Результат: `10`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `INSECONDS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует значение аргумента типа «**Дата и время**» или «**Длительность**» в число, равное количество секунд. Преобразует значение аргумента типа «**Число**» в длительность в секундах.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
INSECONDS(argument)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument`: дата и время, длительность или число.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">

- Число, если в качестве аргумента используется значение типа «**Дата и время**» или «**Длительность**».
- Длительность, если в качестве аргумента используется значение типа «**Число**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
INSECONDS(5)
```

Результат: `00:00:05`
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `INSECONDSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует значение аргумента типа «**Дата и время**» с указанием часового пояса в формате UTC или «**Длительность**» в число, равное количество секунд. Преобразует значение аргумента типа «**Число**» в длительность в секундах.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
INSECONDSUTC(argument)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument`: дата и время, длительность или число.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">

- Число, если в качестве аргумента используется значение типа «**Дата и время**» или «**Длительность**».
- Длительность, если в качестве аргумента используется значение типа «**Число**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
INSECONDSUTC(DATE('2025-05-05T05:05:25+00:00'))
```

Результат: `63882018325`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISLEAPYEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует значение аргумента типа «**Дата и время**». Возвращает логическое значение `true`, если год указанной даты является високосным, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISLEAPYEAR(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ISLEAPYEAR(DATE('2025-01-01T01:01:01'))
```

Результат: `False`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISLEAPYEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует значение аргумента типа «**Дата и время**» с указанием часового пояса в формате UTC. Возвращает логическое значение `true`, если год указанной даты является високосным, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISLEAPYEARUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ISLEAPYEARUTC(DATE('2025-01-01T01:01:01+03:00'))
```

Результат: `True`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISOFORMAT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует значение типа «**Дата и время**» в формат ISO.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISOFORMAT(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ISOFORMAT($_creationDate)
```

Результат: дата в формате ISO 8601.

Здесь:

`$_creationDate` — атрибут «**Дата создания**».
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISOFORMATUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует значение типа «**Дата и время**» с указанием часового пояса в формате UTC в формат ISO.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISOFORMATUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ISOFORMATUTC($_creationDate)
```

Результат: дата в формате ISO 8601 для часового пояса UTC-0.

Здесь:

`$_creationDate` — атрибут «**Дата создания**».
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISTODAY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает значение `true`, если значением аргумента является сегодняшняя дата. В противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISTODAY(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ISTODAY(NOW())
```

Результат: `True`

Здесь:

[`NOW()`](#now) — возвращает текущую дату и время.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISTODAYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает значение `true`, если значением аргумента является сегодняшняя дата для часового пояса UTC-0. В противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISTODAYUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ISTODAYUTC(NOW())
```

Результат: `True`, если в часовом поясе UTC-0 такая же дата.

Здесь:

[`NOW()`](#now) — возвращает текущую дату и время.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISWEEKEND()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает значение `true`, если заданная дата является выходным днём. В противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISWEEKEND(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ISWEEKEND(DATE('2025-05-05T01:01:01'))
```

Результат: `False`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISWEEKENDUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает значение `true`, если заданная дата с указанием часового пояса в формате UTC является выходным днём для часового пояса UTC-0. В противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISWEEKENDUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ISWEEKENDUTC(DATE('2025-05-05T01:01:01+03:00'))
```

Результат: `True`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISWORKDAY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает значение `true`, если заданная дата является рабочим днём. В противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISWORKDAY(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ISWORKDAY(DATE('2025-05-05T01:01:01'))
```

Результат: `True`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISWORKDAYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает значение `true`, если заданная дата с указанием часового пояса является рабочим днём для часового пояса UTC-0. В противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISWORKDAYUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ISWORKDAYUTC(DATE('2025-05-05T01:01:01+03:00'))
```

Результат: `False`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `JOIN()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Объединяет строки с использованием заданного разделителя.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
JOIN(separator, LIST(string1, ..., stringN))
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`separator`: строка, разделитель объединяемых строк.
`string1, ..., stringN`: объединяемые строки.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
JOIN(", ", LIST("Аналитик", "Архитектор", "Администратор"))
```

Результат: `False`

Здесь:

[`LIST()`](#list) — функция, которая принимает значения, разделённые запятыми, и возвращает их список.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LAST()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает первый элемент из списка. При отсутствии элементов в списке `FIRST()` возвращает пустое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
LAST(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list`: список значений.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения совпадает с типом элементов списка.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
LAST((from i in db->music where i->album == 'Whale Meditation' select i->song))
```

Результат: название последней песни из альбома `Whale Meditation`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает значения двух аргументов типа «**Дата и время**» или «**Длительность**». Если первый аргумент меньше или равен второму, возвращает логическое значение `true`. В противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
LE(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument1`, `argument2`: дата и время.
- `argument1`, `argument2`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
LE(DURATION('P2DT1H0M0S'), DURATION('P3DT1H0M0S'))
```

Результат: `True`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LENGTH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает количество символов в строке.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
LENGTH(string)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string`: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
LENGTH("В этой строке 26 символов.")
```

Результат: `26`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LESS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает логическое значение `true`, если значение первого аргумента меньше второго, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
LESS(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: длительность, число, строка или дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
LESS(1, 2)
```

Результат: `True`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LESSEQ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает логическое значение `true`, если значение первого аргумента меньше либо равно второму, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
LESSEQ(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: длительность, число, строка или дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
LESSEQ(1, 1)
```

Результат: `True`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LIST()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Определяет список. Берёт перечисление значений, разделяет их запятыми и возвращает список.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
LIST(argument1, …, argumentN)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, …, `argumentN`: список значений.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Cписок значений
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
LIST(1, 2, "a", "b")
```

Результат: список значений `1, 2, a, b`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LISTEQUALS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два списка значений. Если они равны, возвращает логическое значение `true`, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
LISTEQUALS(list1, list2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list1`, `list2`: список значений.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
LISTEQUALS(LIST(1, 2), LIST("a", "b"))
```

Результат: `False`

Здесь:

[`LIST()`](#list) — берёт перечисление значений, разделяет их запятыми и возвращает список.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает логическое значение `true`, если значение первого аргумента типа «**Дата и время**» или «**Длительность**» меньше второго, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
LT(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument1`, `argument2`: дата и время.
- `argument1`, `argument2`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
LT(DURATION('P2DT1H0M0S'), DURATION('P3DT1H0M0S'))
```

Результат: `True`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LTUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает логическое значение `true`, если значение первого аргумента типа «**Дата и время**» с указанием часового пояса в формате UTC меньше второго, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
LTUTC(dateTime1, dateTime2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime1`, `dateTime2`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
LTUTC(DATE('2025-05-05T01:01:01+03:00'), DATE('2025-05-05T01:01:01+04:00'))
```

Результат: `True`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MATCHES()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Использует в качестве аргументов строку и регулярное выражение. Возвращает логическое значение `true`, если какая-либо часть строки или строка полностью соответствует условию, заданному регулярным выражением. В противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
MATCHES(string, regex)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string`: строка.
`regex`: строка, регулярное выражение.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
MATCHES("Требуется решить проблему срочно!", "([Cс]рочн.+?)")
```

Результат: `True`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MAX()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Определяет максимальное значение среди всех элементов списка, заданного в качестве аргумента. Элементы списка могут быть значениями или выражениями, результатом которых является значение, типа «**Число**», «**Дата и время**» или «**Длительность**». Все элементы списка должны быть одного типа.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
MAX(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list`: список, состоящий из значений типа «**Число**», «**Дата и время**» или «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения тот же, что и у элементов списка, который является аргументом.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
MAX(DURATION('P2DT1H0M0S'), DURATION('P3DT1H0M0S'))
```

Результат: `3.01:00:00`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MIN()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Определяет минимальное значение среди всех элементов списка, заданного в качестве аргумента. Элементы списка могут быть значениями или выражениями, результатом которых является значение, типа «**Число**», «**Дата и время**» или «**Длительность**». Все элементы списка должны быть одного типа.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
MIN(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list`: список, состоящий из значений типа «**Число**», «**Дата и время**» или «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения тот же, что и у элементов списка, который является аргументом.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
MIN(DURATION('P2DT1H0M0S'), DURATION('P3DT1H0M0S'))
```

Результат: `2.01:00:00`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MINUTE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее минуте указанной даты в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
MINUTE(dateTime, [timeZone])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `timeZone`: строка, часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
MINUTE(DATE('2025-05-05T01:01:01'))
```

Результат: `1`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MINUTES()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Длительность**» и возвращает числовое значение, соответствующее количеству минут в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
MINUTES(duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`duration`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
MINUTES(DURATION('P1DT1H30M0S'))
```

Результат: `1530`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MINUTEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее минуте указанной даты для часового пояса UTC-0.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
MINUTEUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
MINUTEUTC(DATE('2025-05-05T01:01:01+03:30'))
```

Результат: `31`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MONTH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее месяцу указанной даты в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации или указанном в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
MONTH(dateTime, [timeZone])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `timeZone`: строка, часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
MONTH(DATE('2025-05-01T01:01:01+03:00'), "Europe/London")
```

Результат: `4`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MONTHS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Длительность**» и возвращает числовое значение, соответствующее количеству месяцев в значении аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
MONTHS(duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`duration`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
MONTHS(DURATION('P30D'))
```

Результат: `1`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MONTHUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее месяцу указанной даты для часового пояса UTC-0.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
MONTHUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
MONTHUTC(DATE('2025-05-01T01:01:01+03:00'))
```

Результат: `4`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `NE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента типа «**Дата и время**» или «**Длительность**». Если их значения не равны, возвращает логическое значение `true`, в противном случае возврашает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
NE(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument1`, `argument2`: дата и время.
- `argument1`, `argument2`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
NE(DURATION('P0DT25H30M0S'), DURATION('P1DT1H30M0S'))
```

Результат: `False`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `NEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента типа «**Дата и время**» с указанием часового пояса в формате UTC. Если их значения не равны, возвращает логическое значение `true`, в противном случае возврашает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
NEUTC(dateTime1, dateTime2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime1`, `dateTime2`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
NEUTC(DATE('2025-05-01T01:01:01+03:00'), DATE('2025-05-01T01:01:01+02:00'))
```

Результат: `True`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `NORMALIZE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Убирает лишние пробелы в строке, заданной в качестве аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
NORMALIZE(string)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string`: строка.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
NORMALIZE("В этой   строке  были    лишние  пробелы, но теперь   их    нет.")
```

Результат: `В этой строке были лишние пробелы, но теперь их нет.`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `NOT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Использует в качестве аргумента логическое значение или выражение, возвращающее логическое значение. Выполняет операцию логического отрицания над аргументом.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
NOT(boolean)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`boolean`: логическое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
NOT(EMPTY($_creationDate))
```

Результат: `True`

Здесь:

- [`EMPTY()`](#empty) — проверяет, не является ли пустым значение аргумента.
- `$_creationDate` — атрибут «**Дата создания**».

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `NOTEQUALS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента одного типа. Возвращает логическое значение `true`, если первый аргумент не равен второму, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
NOTEQUALS(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: строка, логическое значение, дата и время, число или длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
NOTEQUALS("Строка", "Сорока")
```

Результат: `True`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `NOTMATCHES()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Использует в качестве аргументов строку и регулярное выражение. Возвращает логическое значение `true`, если часть строки или строка полностью не соответствуют условию, заданному регулярным выражением. В противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
NOTMATCHES(string, regex)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `string`: строка.
- `regex`: строка,регулярное выражение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
NOTMATCHES("Требуется решить проблему срочно!", "([Cс]рочн.+?)")
```

Результат: `False`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `NOW()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает текущую дату и время в часовом поясе, заданном на форме, в настройках аккаунта или глобальной конфигурации.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
NOW()
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
Не требуются.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
NOW()
```

Результат: текущая дата и время.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `OBJECT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает список ID записей из указанного шаблона, в которых указанный **текстовый** атрибут имеет указанное значение.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
OBJECT("businessApp", "template", "attribute", "attributeValue")
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `businessApp`: строка, системное имя приложения.
- `template`: строка, системное имя шаблона.
- `attribute`: строка, системное имя атрибута.
- `attributeValue`: строка, значение атрибута.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Список
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
OBJECT("Fleetmanagement", "Requires", "Status", "Завершено")
```

Результат: список ID записей шаблона _«Заявки»_ (системное имя — `Requires`) приложения _«Управление автопарком»_ (системное имя — `Fleetmanagement`), у которых значение атрибута _«Статус»_ (системное имя — `Status`) равно статусу `Завершено`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `OR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Берёт два значения логического типа или два выражения, результатом которых являются значения логического типа, и возвращает результат логического сложения этих значений.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
OR(boolean1, boolean2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`booleant1`, `boolean2`: логическое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
OR(BOOL("true"), BOOL("false"))
```

Результат: `True`

Здесь:

[`BOOL()`](#bool) — преобразует строку в логическое значение.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `PARSEDATE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует данные строки в значение типа «**Дата и время**» согласно заданной маске.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
PARSEDATE(string, stringFormat)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `string`: строка.
- `stringFormat`: строка, формат данных.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
PARSEDATE("050525", "MMddyy")
```

Результат: `05.05.2025 0:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `PARSEDATEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует данные строки в значение типа «**Дата и время**» в часовом поясе UTC-0 согласно заданной маске.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
PARSEDATE(string, stringFormat)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `string`: строка.
- `stringFormat`: строка, формат данных.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
PARSEDATEUTC("0505250001", "MMddyyhhmm")
```

Результат: `05.05.2025 0:01:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `POW()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возводит первый аргумент в степень, указанную во втором аргументе, и возвращает результат.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
POW(base, degree)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `base`: число.
- `degree`: число.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
POW(2, 8)
```

Результат: `256`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `PRODUCT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Берёт в качестве аргументов два значения числового типа и возвращает результат умножения одного на другое.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
PRODUCT(number1, number2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `number1`: число.
- `number2`: число.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
PRODUCT(3, 4)
```

Результат: `12`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `QUARTERS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает количество кварталов для аргумента типа «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
QUARTERS(duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`duration`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
QUARTERS(DURATION('P200DT1H30M0S'))
```

Результат: `2,2`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `QUOTIENT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает целочисленный результат деления первого аргумента на второй.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
QUOTIENT(dividend, divisor)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dividend`: число.
- `divisor`: число.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
QUOTIENT(5, 2)
```

Результат: `2`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `REGEXREPLACE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block">
<span >Описание
</td>
<td markdown="block">
<span>Принимает исходную строку `sourceString`, находит в ней подстроки по регулярному выражению (шаблону) `regEx`, заменяет найденные подстроки замещающей строкой `replacementString` и возвращает результирующую строку. Инструмент отладки регулярных выражений со справкой:<a href="https://regex101.com/">https://regex101.com/</a>
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
REGEXREPLACE(sourceString, regEx, replacementString)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `sourceString`: исходная строка.
- `regEx`: строка с регулярным выражением.
- `replacementString`: замещающая строка.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

- `REGEXREPLACE($FIO,"(.+) (.+) (.+)","$2")` — принимает строку вида «`Фамилия Имя Отчество`» и возвращает Имя (второе слово из трёх).
- `REGEXREPLACE($Subject,".*\[#([0-9]+)\].*","$1")` — принимает строку вида «`Рассмотрите заявку [#12345]`» и возвращает код заявки (`12345`).
- `REGEXREPLACE($HTML,"&lt;p class=""title"">(.+)&lt;\/p>","&lt;h1>$1&lt;h1>")` — принимает HTML-код, заменяет параграфы класса `title` на заголовки уровня 1 и возвращает результирующий HTML-код.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `REMAINDER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает остаток от деления первого аргумента на второй.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
REMAINDER(dividend, divisor)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dividend`: число, делимое.
`divisor`: число, делитель.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
REMAINDER(5, 2)
```

Результат: `1`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `REPLACE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Заменяет все экземпляры заданной строки в исходной строке на новое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
REPLACE(string, subString1, subString2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string`, `subString1`, `subString2`: строка

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
REPLACE("НДС равен восемнадцати процентам.", "восемнадцати", "двадцати")
```

Результат: `НДС равен двадцати процентам.`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ROUND()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Округляет число к ближайшему целому числу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ROUND(number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`number`: число.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ROUND(3.5)
```

Результат: `4`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SECOND()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее секундам указанной даты.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SECOND(dateTime, [timeZone])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `timeZone`: строка, часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
SECOND(DATE('2025-05-05T01:01:01'), "Europe/London")
```

Результат: `1`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SECONDS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает количество секунд в значении аргумента типа «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SECONDS(duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`duration`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
SECONDS(DURATION('P1DT1H30M0S'))
```

Результат: `91800`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SECONDUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее секундам указанной даты в часовом поясе UTC-0.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SECONDUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
SECONDUTC(DATE('2025-05-05T01:01:01+01:00'))
```

Результат: `1`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SQRT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Вычисляет квадратный корень из значения аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SQRT(number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`number`: число.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
SQRT(25)
```

Результат: `5`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFDAY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала дня, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFDAY(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
STARTOFDAY(DATE('2025-05-05T01:01:01'))
```

Результат: `05.05.2025 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFDAYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала дня, в пределах которого находится значение аргумента для часового пояса UTC-0.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFDAYUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
STARTOFDAYUTC(DATE('2025-05-05T01:01:01+03:00'))
```

Результат: `04.05.2025 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFMONTH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала месяца, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFMONTH(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
STARTOFMONTH(DATE('2025-05-01T01:01:01'))
```

Результат: `01.05.2025 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFMONTHUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала месяца, в пределах которого находится значение аргумента для часового пояса UTC-0.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFMONTHUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
STARTOFMONTHUTC(DATE('2025-05-01T01:01:01+03:00'))
```

Результат: `01.04.2025 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFQUARTER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала квартала, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFQUARTER(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
STARTOFQUARTER(DATE('2025-04-01T01:01:01'))
```

Результат: `01.04.2025 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFQUARTERUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала квартала, в пределах которого находится значение аргумента для часового пояса UTC-0.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFQUARTERUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
STARTOFQUARTERUTC(DATE('2025-04-01T01:01:01+03:00'))
```

Результат: `01.01.2025 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFWEEK()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала недели, в пределах которой находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFWEEK(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
STARTOFWEEK(DATE('2025-05-05T01:01:01'))
```

Результат: `05.05.2025 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFWEEKUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала недели, в пределах которой находится значение аргумента для часового пояса UTC-0.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFWEEKUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
STARTOFWEEKUTC(DATE('2025-05-05T01:01:01+03:00'))
```

Результат: `28.04.2025 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFYEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала года, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFYEAR(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
STARTOFYEAR(DATE('2025-01-01T01:01:01'))
```

Результат: `01.01.2025 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFYEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала года, в пределах которого находится значение аргумента для часового пояса UTC-0.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFYEARUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
STARTOFYEARUTC(DATE('2025-01-01T01:01:01+03:00'))
```

Результат: `01.01.2024 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTSWITH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает две строки и возвращает значение `true`, если первая строка начинается на вторую строку, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTSWITH(string, startString)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string`, `startString`: строка.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
STARTSWITH("Строка", "Стр")
```

Результат: `True`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SUB()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Вычитает из значения аргумента типа «**Дата и время**» или «**Длительность**» значение типа «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SUB(dateTime, duration)
```

**или**

``` cs
SUB(duration, duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `duration`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
SUB(DATE('2025-01-01T01:01:01'), DURATION('P1DT1H30M0S'))
```

Результат: `30.12.2024 23:31:01`

Здесь:

- `DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
- `DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SUBSTRING()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Извлекает из строки подстроку, начиная с заданной позиции. При необходимости можно задать длину извлекаемой строки.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SUBSTRING(sourceString, startIndex, [numberOfChars])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `sourceString`: строка.
- `startIndex`: число, номер позиции начала подстроки, отсчитывается от 0.
- `numberOfChars`: число, количество символов в подстроке, необязательный аргумент.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
SUBSTRING("Раньше эта строка начиналась с другого слова.", 7, 31)
```

Результат: `эта строка начиналась с другого`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SUBTRACT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Вычитает значение второго аргумента из значения первого.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SUBTRACT(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument1`: число; `argument2`: число.
- `argument1`: длительность; `argument2`: длительность.
- `argument1`: дата и время; `argument2`: длительность.
- `argument1`: дата и время; `argument2`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число, длительность или дата и время.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
SUBTRACT(17, 10)
```

Результат: `7`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SUBUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Вычитает из значения аргумента типа «**Дата и время**» значение типа «**Длительность**». Возвращает значение типа «**Дата и время**» для часового пояса UTC-0.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SUBUTC(dateTime, duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `duration`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
SUBUTC(DATE('2025-01-01T01:01:01+00:00'), DURATION('P1DT1H30M0S'))
```

Результат: `31.12.2024 2:31:01` для часового пояса UTC+3.

Здесь:

- `DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
- `DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SUM()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Суммирует все значения аргументов типа «**Число**» или «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SUM(argument1, ..., argumentN)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1, ..., argumentN`: число или длительность.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения тот же, что и у элементов, являющихся аргументом.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
SUM(1, 2, 3, 4)
```

Результат: `10`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `TODURATION()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Конвертирует число в значение типа «**Длительность**» в секундах.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
TODURATION(number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`number`: число.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
TODURATION(12345)
```

Результат: `03:25:45`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `TOLOWER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Приводит все буквы в строке к нижнему регистру (прописным буквам).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
TOLOWER(string)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string`: строка.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
TOLOWER("Все Буквы В Этой Строке Стали Прописными.")
```

Результат: `все буквы в этой строке стали прописными.`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `TOUPPER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Приводит все буквы в строке к верхнему регистру (заглавным буквам).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
TOUPPER(string)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string`: строка.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
TOUPPER("Все Буквы В Этой Строке Стали Заглавными.")
```

Результат: `ВСЕ БУКВЫ В ЭТОЙ СТРОКЕ СТАЛИ ЗАГЛАВНЫМИ.`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `TRIM()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Удаляет пробелы в начале и конце строки.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
TRIM(string)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string`: строка.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
TRIM("   В этой строке были лишние пробелы.   ")
```

Результат: `В этой строке были лишние пробелы.`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `UNION()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Находит объединение двух множеств.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
UNION(object1, object2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`object1`, `object2`: запись.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Запись
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
UNION(object1, object2)
```

Результат: ``

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `USER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает идентификатор текущего аккаунта.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
USER()
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
Не требуются.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Идентификатор аккаунта
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
USER()
```

Результат: `account.XX` — ID аккаунта, который просматривает запись.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `VALUE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два аргумента: проверяемое выражение и значение по умолчанию. Возвращает значение первого аргумента, если оно не пустое и не равно `NULL`, в противном случае возвращает значение второго аргумента, если он есть.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
VALUE(argument, [defaultValue])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument`: проверяемое выражение.
- `defaultValue`: значение по умолчанию. Является необязательным аргументом.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения совпадает с типом проверяемого выражения.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
VALUE($Amount, "Не заполнено поле Amount")
```

Результат: значение атрибута _Amount_. В противном случае вернёт текст _«Не заполнено поле Amount»_.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WEEKOFYEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает номер недели года, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WEEKOFYEAR(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WEEKOFYEAR(DATE('2025-05-06T01:01:01'))
```

Результат: `18`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WEEKOFYEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает номер недели года, в пределах которого находится значение аргумента для часового пояса UTC-0.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WEEKOFYEARUTC(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WEEKOFYEARUTC(DATE('2025-05-06T01:01:01+03:00'))
```

Результат: `17`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKDAYS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет к указанной дате количество рабочих дней с учётом праздничных и выходных дней и возвращает получившуюся дату.

Если часовой пояс рабочего офиса отличается от часового пояса сервера **{{ productName }}**, используйте функцию [WORKDAYSTZ()](#workdaystz).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKDAYS(startDateTime, workingDays,
    [LIST(holidayDateTime1, …, holidayDateTimeN)]
    )
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время.
- `workingDays`: число, количество рабочих дней.
- `LIST(holidayDateTime1, …, holidayDateTimeN)`: праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WORKDAYS(DATE('2025-05-01'), 10, LIST(DATE('2025-05-01'), 
        DATE('2025-05-02'), DATE('2025-05-08'), DATE('2025-05-09')))
```

Результат: `21.05.2025 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKDAYSDURATION()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает продолжительность между двумя датами с учётом праздничных и выходных дней.

Если часовой пояс рабочего офиса отличается от часового пояса сервера **{{ productName }}**, используйте функцию [WORKDAYSDURATIONTZ()](#workdaysdurationtz).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKDAYSDURATION(startDateTime, endDateTime,
    [LIST(holidayDateTime1, …, holidayDateTimeN)]
    )
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время.
- `endDateTime`: дата и время.
- `LIST(holidayDateTime1, …, holidayDateTimeN)`: праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WORKDAYSDURATION(DATE('2025-05-01'), DATE('2025-05-12'), LIST(DATE('2025-05-01'), 
        DATE('2025-05-02'), DATE('2025-05-08'), DATE('2025-05-09')))
```

Результат: `3.00:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKDAYSDURATIONTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает продолжительность между двумя датами с учётом праздничных и выходных дней для указанного часового пояса.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKDAYSDURATIONTZ(startDateTime, endDateTime,
    LIST(holidayDateTime1, …, holidayDateTimeN),
    timeZone
    )
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время.
- `endDateTime`: дата и время.
- `LIST(holidayDateTime1, …, holidayDateTimeN)`: праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.
- `timeZone`: строка, часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WORKDAYSDURATIONTZ(DATE('2025-05-01'), DATE('2025-05-12'), LIST(DATE('2025-05-01'), 
        DATE('2025-05-02'), DATE('2025-05-08'), DATE('2025-05-09')), "Asia/Tokyo")
```

Результат: `3.06:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKDAYSDURATIONUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает продолжительность между двумя датами для часового пояса UTC-0 с учётом выходных дней.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKDAYSDURATIONUTC(startDateTime, endDateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`startDateTime`, `endDateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WORKDAYSDURATIONUTC(DATE('2025-05-01+03:00'), DATE('2025-05-12+00:00'))
```

Результат: `10`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKDAYSTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет к указанной дате количество рабочих дней с учётом праздничных и выходных дней для указанного часового пояса и возвращает получившуюся дату.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKDAYSTZ(startDay, workingDays,
    LIST(holidayDateTime1, …, holidayDateTimeN),
    timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время.
- `workingDays`: число, количество рабочих дней.
- `LIST(holidayDateTime1, …, holidayDateTimeN)`: праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.
- `timeZone`: строка, часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WORKDAYSTZ(DATE('2025-05-01+03:00'), 10, LIST(DATE('2025-05-01'), 
        DATE('2025-05-02'), DATE('2025-05-08'), DATE('2025-05-09')),
        "America/Anchorage")
```

Результат: `20.05.2025 0:00:00`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKDAYSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Прибавляет к указанной дате количество рабочих дней с учётом выходных дней для часового пояса UTC-0 и возвращает получившуюся дату.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKDAYSUTC(startDay, workingDays)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время.
- `workingDays`: число, количество рабочих дней.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WORKDAYSUTC()
```

Результат: ``

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKHOURS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает в качестве аргументов дату начала работы, количество часов, отведённых на работу, начала рабочего дня, продолжительность рабочего дня и список праздничных дней. Возвращает дату и время завершения работы.

Если часовой пояс рабочего офиса отличается от часового пояса сервера **{{ productName }}**, используйте функцию [`WORKHOURSTZ()`](#workhourstz).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKHOURS(startDateTime, workingHours, 
    workingDayStart, workingDayDuration,
    [LIST(holidayDateTime1, ..., holidayDateTimeN)])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время.
- `workingHours`: число, количество рабочих часов.
- `workingDayStart`: длительность, время начала рабочего дня от 00:00.
- `workingDayDuration`: длительность рабочего дня (должна быть меньше разницы между полуночью и временем начала рабочего дня).
- `LIST(holidayDateTime1, ..., holidayDateTimeN)`: праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WORKHOURS(DATE('2025-05-01'), 5, DURATION('PT9H'), DURATION('PT4H'), LIST(DATE('2025-05-01'), 
        DATE('2025-05-02'), DATE('2025-05-08'), DATE('2025-05-09')))
```

Результат: `06.05.2025 10:00:00`

Здесь:

- `DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
- `DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKHOURSDURATION()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает продолжительность рабочего времени между двумя датами при заданных начале рабочего дня и его продолжительности с учётом праздничных и выходных дней.

Если часовой пояс рабочего офиса отличается от часового пояса сервера **{{ companyName }}**, используйте функцию [`WORKHOURSDURATIONTZ()`](#workhoursdurationtz).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKHOURSDURATION(startDateTime, endDateTime, 
    workingDayStart, workingDayDuration,
    [LIST(holidayDateTime1, ..., holidayDateTimeN)])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время.
- `endDateTime`: дата и время.
- `workingDayStart`: длительность, время начала рабочего дня от 00:00.
- `workingDayEnd`: длительность рабочего дня (должна быть меньше разницы между полуночью и временем начала рабочего дня).
- `LIST(holidayDateTime1, ..., holidayDateTimeN)` (необязательно): праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WORKHOURSDURATION(DATE('2025-05-01'), DATE('2025-05-07'), DURATION('PT8H'), DURATION('PT15H'), LIST(DATE('2025-05-01'), 
        DATE('2025-05-02'), DATE('2025-05-08'), DATE('2025-05-09')))
```

Результат: `22:00:00`

Здесь:

- `DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
- `DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKHOURSDURATIONTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает продолжительность рабочего времени между двумя датами при заданных начале рабочего дня и его продолжительности с учётом праздничных и выходных дней для указанного часового пояса.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKHOURSDURATIONTZ(startDateTime, endDateTime, 
    workingDayStart, workingDayDuration,
    LIST(holiday1, ..., holidayN),
    timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время.
- `endDateTime`: дата и время.
- `workingDayStart`: длительность, время начала рабочего дня.
- `workingDayDuration`: длительность рабочего дня (должна быть меньше разницы между полуночью и временем начала рабочего дня).
- `LIST(holiday1, ..., holidayN)`: праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим
- `timeZone`: строка, часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WORKHOURSDURATIONTZ(DATE('2025-05-01'), DATE('2025-05-07'), DURATION('PT8H'), DURATION('PT15H'), LIST(DATE('2025-05-01'), 
        DATE('2025-05-02'), DATE('2025-05-08'), DATE('2025-05-09')),
        "Asia/Tokyo")
```

Результат: `1.04:00:00`

Здесь:

- `DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
- `DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKHOURSTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает в качестве аргументов дату начала работы, количество часов, отведённых на работу, начала рабочего дня, продолжительность рабочего дня, список праздничных дней и часовой пояс. Возвращает дату и время завершения работы для указанного часового пояса.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKHOURSTZ(startDateTime, workingHours, 
    workingDayStart, workingDayDuration,
    LIST(holidayDateTime1, ..., holidayDateTimeN),
    timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время.
- `workingHours`: число, количество рабочих часов.
- `workingDayStart`: длительность, время начала рабочего дня от 00:00.
- `workingDayDuration`: длительность рабочего дня (должна быть меньше разницы между полуночью и временем начала рабочего дня),
- `LIST(holidayDateTime1, ..., holidayDateTimeN)`: праздники и исключения из выходных дней, т. е. если всписке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим,
- `timeZone`: строка, часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
WORKHOURSTZ(DATE('2025-05-01'), 5, DURATION('PT9H'), DURATION('PT4H'), LIST(DATE('2025-05-01'), 
        DATE('2025-05-02'), DATE('2025-05-08'), DATE('2025-05-09')),
        "America/Anchorage")
```

Результат: `05.05.2025 10:00:00`

Здесь:

- `DATE()` — преобразует в дату строковый литерал в формате ISO 8601.
- `DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `YEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее году указанной даты.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
YEAR(dateTime, [timeZone])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `timeZone`: строка, часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
YEAR(DATE('2025-01-01+03:00'), "America/Anchorage")
```

Результат: `2024`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `YEARS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает количество лет для значения аргумента типа «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

```cs
YEARS(duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`duration`: длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
YEARS(DURATION('P183D'))
```

Результат: `0,5`

Здесь:

`DURATION()` — преобразует в длительность строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `YEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее году указанной даты для часового пояса UTC-0.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
YEAR(dateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dateTime`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
YEARUTC(DATE('2025-01-01+03:00'))
```

Результат: `2024`

Здесь:

`DATE()` — преобразует в дату строковый литерал в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
