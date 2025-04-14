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

Добавляет к значению типа «Дата и время» в местном часовом поясе указанное число дней.

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

Добавляет указанное количество дней к значению типа «Дата и время» в формате UTC.

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
ADDDAYSUTC(DATE('2024-01-01T01:01:01'), 3)
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

## `ADDDUR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Суммирует два значения типа «Длительность».

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

Добавляет указанное количество часов к значению типа «Дата и время».

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

Добавляет указанное количество часов к значению типа «Дата и время» в формате UTC.

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
ADDHOURSUTC(DATE('2024-01-01T01:01:01'), 3)
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

## `ADDLOC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет значение типа «Длительность» к значению типа «Дата и время» в местном часовом поясе.

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

Добавляет указанное количество минут к значению типа «Дата и время» в местном часовом поясе.

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

Добавляет указанное количество минут к значению типа «Дата и время» в формате UTC.

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
ADDMINUTESUTC(DATE('2024-01-01T01:01:01'), 3)
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

## `ADDMONTHS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество месяцев к значению типа «Дата и время» в местном часовом поясе.

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

Добавляет указанное количество месяцев к значению типа «Дата и время» в формате UTC.

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
ADDMONTHSUTC(DATE('2024-01-01T01:01:01'), 3)
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

## `ADDSECONDS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество секунд к значению типа «Дата и время» в местном часовом поясе.

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

Добавляет указанное количество секунд к значению типа «Дата и время» в формате UTC.

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
ADDSECONDSUTC(DATE('2024-01-01T01:01:01'), 3)
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

## `ADDUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет значение типа «Длительность» к значению типа «Дата и время» в формате UTC.

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
ADDUTC(DATE('2024-01-01T01:01:01'), DURATION('P1DT12H30M5S'))
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

## `ADDYEARS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество лет к значению типа «Дата и время» в местном часовом поясе.

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
Добавляет указанное количество лет к значению типа «Дата и время» в формате UTC.

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
ADDYEARSUTC(DATE('2024-01-01T01:01:01'), 3)
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

## `ALL()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Берет список логических переменных и возвращает значение `true`, если все логические переменные принимают значение `true`.

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
Берет два логических значения или два выражения, результатом которых являются логические значения, и возвращает результат логического умножения этих значений.

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

```
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

```
ANY( from I in db->Tickets where i->product = 'Data Monsoon' select i->name)
```

Возвращает значение `true`, если хотя бы один элемент имеет значение предиката `product` равным «`Data Monsoon`».

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

`ANY([(query), queryVar, boolEval])`
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

Возвращает значение `true`, если поступил хотя бы один запрос по продукту Data Monsoon, при обработке которого потребуется участие отдела QA.

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

```
ASCENDING(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`list`: список значений типа «Число» или строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
сортированный список значений
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

```
ASCENDING('л', 'а', 'и')
```

Возвращает `(string:а string:и string:л)`

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
AVERAGE(value1, value2)
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

Проверяет факт вхождения даты или длительности в заданный диапазон. Значения типа «Дата и время» должны быть в местном часовом поясе.

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
логическое значение
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

Результат: `true`

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

Проверяет факт вхождения даты или длительности в заданный диапазон. Значения типа «Дата и время» должны быть в формате UTC.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
BETWEENUTC(вate, ыtartDate, уndDate)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `вate` — дата для проверки.
- `ыtartDate` — начальное значение диапазона.
- `уndDate` — конечное значение диапазона.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
BETWEENUTC(DATE("2023-01-15"), DATE("2024-08-15"), DATE("2024-08-15"))
```

Результат: `false`

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
Преобразует строку в логический тип. Для правильной конвертации, значение строки должно быть равно `true` или `false` без учёта регистра.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
BOOL(String)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`String` — строка, которая преобразуется в логическое значение,  со значением `true` или `false` (без учёта регистра). При неподходящих значениях атрибута (0, 1, истина, ложь и т. п.) функция возвращает пустое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
логическое значение
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

Возвращает `True`
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
Округляет до ближайшего большего целого.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
CEILING(Number)
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

Возвращает `5`
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

Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее веку указанной даты в местном часовом поясе.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
CENTURY(DateTime)
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
CENTURY(DATE("2024-08-15T13:45:15"))
```

Возвращает `21`

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
строку
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

Возвращает `Сумма доходов равна: 100000`

Здесь:

`LIST()` — функция, которая принимает значения одного типа, разделённые запятыми, и возвращает их список.

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
логическое значение
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

Возвращает `True`
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
Переводит значение типа «Дата и время» из локального часового пояса в заданный часовой пояс в формате IANA.

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

- `date` — дата в местном часовом поясе.
- `TimeZone` — целевой часовой пояс.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
логическое значение
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
Возвращает `True`
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
COUNT(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: список строк
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
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DATETIMEFROMSECONDS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Преобразует заданное количество секунд в дату.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
DATETIMEFROMSECONDS(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: число
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
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DATETIMEINSECONDS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Преобразует заданную в качестве аргумента дату в количество секунд, прошедшее с 00:00:00 1 января 1970 года (Unix-время).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
DATETIMEINSECONDS(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
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
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее дню месяца указанной даты в местном часовом поясе.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DAY(dayTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dayTime`: дата и время

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
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAYTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее дню месяца указанной даты в заданном часовом поясе. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DAYTZ(dayTime, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dayTime`: дата и время
- `timeZone`: строка, часовой пояс

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

Преобразует строку в число.

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

Возвращает `10,5`
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
Берет в качестве аргументов два значения числового типа и возвращает результат деления одного на другое.

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
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DURATIONFROMSECONDS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Преобразует заданное количество секунд в длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DURATIONFROMSECONDS(seconds)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`seconds`: число, секунды

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
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DURATIONINSECONDS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Преобразует заданную длительность в количество секунд.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DURATIONINSECONDS(duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`duration`: длительность

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
Берет в качестве аргумента выражение, результатом которого является некоторое значение, и проверяет данное значение на пустоту.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
EMPTY(argument1)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: значение, являющееся результатом выражения, заданного в качестве аргумента, и имеющее один с ним тип.

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
Принимает аргумент типа «Дата и время» и возвращает дату и время окончания дня, в пределах которого находится значение аргумента.

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
Принимает аргумент типа «Дата и время» и возвращает дату и время окончания месяца, в пределах которого находится значение аргумента.

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
Принимает аргумент типа «Дата и время» и возвращает дату и время окончания квартала, в пределах которого находится значение аргумента.

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
Принимает аргумент типа «Дата и время» и возвращает дату и время окончания недели, в пределах которого находится значение аргумента.

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
Принимает аргумент типа «Дата и время» и возвращает дату и время окончания года, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
ENDOFYEAR(dateTime)
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
ENDSWITH(string1, string2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string1`, `string2`: строка
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

Возвращает `true`, если атрибут `Status` имеет значение`Resolved`.

Атрибут типа «**Список значений**» хранит ID своего текущего значения. Поэтому в формуле функция`ID()`приводит тип `string` к типу `id`, чтобы функция `EQUALS()` сравнивала значения одного типа.

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

Сравнивает два аргумента и возвращает значение `true`, если они равны, в противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
EQUALS(value1, value2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`value1`, `value2`: значение любого типа

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

- `list` — список значений.

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
FIRST((from i in db->music where i>album == 'Whale Meditation' select i->song))
```

Возвращает название первой песни из альбома Whale Meditation.

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
Округляет число в меньшую сторону.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
FLOOR(number)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`number`: число
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
FORMAT("stringToFormat {0} {1} ... {N}", LIST(value0, value1, .., valueN))
```

Эта функция принимает строку с заполнителями вида `{0}`…`{N}` и список значений. Функция подставляет значения из списка в соответствующие заполнители и возвращает результирующую строку.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
Строка задания формата: строка
`LIST(value0, value1, .., valueN)`: список значений любых типов.

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

Возвращает строку:

```
Название: Yesterday, исполнитель: Beatles
```

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
Возвращает логическое значение `true`, если аргумент1 больше аргумента2, в противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
GREATER(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: логическое значение, число, строка или дата и время.

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
Возвращает логическое значение `true`, если аргумент1 больше либо равен аргументу2, в противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
GREATEREQ(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: логическое значение, число, строка или дата и время.

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
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее часу указанной даты в местном часовом поясе.

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
Число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `HOURTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее часу указанной даты в заданном часовом поясе. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
HOURTZ(dateTime, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время
- `timeZone`: строка, часовой пояс
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
ID("objectID")
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

`ID("oa.21")` — возвращает идентификатор шаблона `oa.21`.

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
Использует в качестве аргументов значения или выражения, результатом которых является некоторое значение. Возвращает аргумент2, если аргумент1 является Истиной, в противном случае возвращает аргумент3.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
IF(argument1, argumen2, argument3)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: логическое значение или выражение, возвращающее логическое значение.
`argument2`, `argument3`: значение любого типа или выражение, результатом которого является значение любого типа.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения тот же, что у аргументов `argument2` и `argument3`
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
Возвращает номер (отсчитываемый от нуля) позиции, на которой располагается искомая строка в исходной строке. Номер позиции может отсчитываться от произвольного положения (необязательно).

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

- `sourceString`: исходная строка,
- `stringToFind`: искомая строка,
- `startIndex` (необязательно): номер позиции, от которой производится отсчет

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
Преобразует значение длительности в секунды и наоборот.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
INSECONDS(argument)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument`: длительность или число

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">

Число, если в качестве аргумента используется значение длительности.

Длительность, если в качестве аргумента используется число.

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
Преобразует значение типа «Дата и время» в формат ISO.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISOFORMAT(argument1)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
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
Возвращает значение `true`, если задана сегодняшняя дата. В противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ISTODAY(argument1)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
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
JOIN(argument1, LIST(argument2, argument3,.. argumentN))
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: разделитель объединяемых строк,
`argument2`, `argument3`, .., `argumentN` (в функции `LIST()`): объединяемые строки
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
LENGTH(argument1)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: строка
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
Возвращает логическое значение `true`, если аргумент1 меньше аргумента2, в противном случае возвращает результат `false`.

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

`argument1`, `argument2`: логическое значение, число, строка или дата и время.

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
Возвращает логическое значение `true`, если аргумент1 меньше либо равен аргументу2, в противном случае возвращает результат `false`.

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

`argument1`, `argument2`: логическое значение, число, строка или дата и время.

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
Определяет список. Берет перечисление значений одного типа, разделяет их запятыми и возвращает список.

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

`argument1`, …, `argumentN`: значения одного типа
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
список
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MAKEDATETIME()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает дату и время в местном часовом поясе, соответствующие указанным значениям года, месяца, дня, часа, минут и секунд.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
MAKEDATETIME(year, month, day, hour, minutes, seconds)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `year`: число, соответствующее году.
- `month`: число, соответствующее месяцу.
- `day`: число, соответствующее дню.
- `hour`: число, соответствующее часу.
- `minutes`: число, соответствующее минутам.
- `seconds`: число, соответствующее секундам.

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
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MAKEDATETIMETZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает дату и время в заданном часовом поясе, соответствующие указанным значениям года, месяца, дня, часа, минут и секунд. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MAKEDATETIMETZ(year, month, day, hour, minutes, seconds, timeZone)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `year`: число, соответствующее году.
- `month`: число, соответствующее месяцу.
- `day`: число, соответствующее дню.
- `hour`: число, соответствующее часу.
- `minutes`: число, соответствующее минутам.
- `seconds`: число, соответствующее секундам.
- `timeZone`: строковый идентификатор часового пояса.

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
Использует в качестве аргументов строку и регулярное выражение. Возвращает логическое значение `true`, если какая-либо часть строки или строка полностью соответствуетусловию, заданному регулярным выражением. В противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MATCHES(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: строка
`argument2`: строка (регулярное выражение)
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
Определяет максимальное значение при помощи функции GREATER среди всех элементов списка, заданного в качестве аргумента. Элементы списка могут быть значениями или выражениями, результатом которых является значение. Все элементы списка должны быть одного типа.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MAX(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: список, состоящий из значений типа «Число», длительность или дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения тот же, что и у элементов списка. Являющегося аргументом.

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
Определяет минимальное значение при помощи функции LESS среди всех элементов списка, заданного в качестве аргумента. Элементы списка могут быть значениями или выражениями, результатом которых является значение. Все элементы списка должны быть одного типа.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MIN(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: список, состоящий из значений типа «Число», длительность или дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения тот же, что и у элементов списка, являющегося аргументом.

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
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее минуте указанной даты в местном часовом поясе.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MINUTE(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
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
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MINUTETZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее минуте указанной даты в заданном часовом поясе. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MINUTETZ(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
`argument2`: строка
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
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее месяцу указанной даты в местном часовом поясе.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MONTH(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
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
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MONTHTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее месяцу указанной даты в заданном часовом поясе. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MONTHTZ(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
`argument2`: строка
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
NOT(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: логический
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
Сравнивает два аргумента и возвращает логическое значение `true`, если аргумент1 не равен аргументу2, в противном случае возвращает результат `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
NOTEQUALS(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: значение любого типа
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
NOTMATCHES(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: строка
`argument2`: строка (регулярное выражение)
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
Возвращает текущую дату и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
NOW()
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
аргументы не требуются
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
текущую дату и время
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
Поиск записи шаблона, в которой атрибут имеет указанное значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
OBJECT(`argument1`, `argument2`, `argument3`, `argument4`)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: системное имя бизнес-приложения
`argument2`: системное имя шаблона записи
`argument3`: системное имя атрибута
`argument4`: значение атрибута
Строковые литералы в аргументах следует заключать в кавычки.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
ID записи
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
Берет два значения логического типа или два выражения, результатом которых являются значения логического типа, и возвращает результат логического сложения этих значений.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
OR(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: логическое значение или выражение, возвращающее логическое значение.

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
Берет в качестве аргументов два значения числового типа и возвращает результат умножения одного на другое.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
PRODUCT(number1, number2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`number1`: число
`number2`: число
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
Использует в качестве аргументов два значения числового типа и возвращает целочисленный результат деления одного на другое.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
QUOTIENT(dividend, divisor)
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
целое число
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
<span >Принимает исходную строку `sourceString`, находит в ней подстроки по регулярному выражению (шаблону) `regEx`, заменяет найденные подстроки замещающей строкой `replacementString` и возвращает результирующую строку. Инструмент отладки регулярных выражений со справкой:<a href="https://regex101.com/">https://regex101.com/</a>
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
<span >REGEXREPLACE(sourceString, regEx, replacementString)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `sourceString`: исходная строка
- `regEx`: строка с регулярным выражением
- `replacementString`: замещающая строка

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
строку
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
Использует в качестве аргументов два значения числового типа и возвращает остаток от деления одного значения на другое.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
REMAINDER(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`(делимое): число
`argument2`(делитель): число
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
REPLACE(argument1, argument2, argument3)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: исходная строка
`argument2`: заменяемая строка
`argument3`: новая строка
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
ROUND(argument1)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: число
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
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее секундам указанной даты в местном часовом поясе.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SECOND(argument1)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
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
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SECONDTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее секундам указанной даты в заданном часовом поясе. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SECONDTZ(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
`argument2`: строка
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
Принимает аргумент типа «Дата и время» и возвращает дату и время начала дня, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOF`DAY(argument1)`
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
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
Принимает аргумент типа «Дата и время» и возвращает дату и время начала месяца, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
STARTOFMONTH(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
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
Принимает аргумент типа «Дата и время» и возвращает дату и время начала квартала, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
STARTOFQUARTER(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
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
Принимает аргумент типа «Дата и время» и возвращает дату и время начала недели, в пределах которой находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFWEEK(argument1)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
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
Принимает аргумент типа «Дата и время» и возвращает дату и время начала года, в пределах которого находится значение аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTOFYEAR(argument1)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: дата и время
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
Сравнивает два аргумента и возвращает значение `true`, если значение аргумента1 начинается с значения аргумента2, в противном случае возвращает `false`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
STARTSWITH(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: строка
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
Извлекает из строки подстроку определенной длины начиная с заданной позиции (задание длины опционально).

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

`sourceString`: строка
`startIndex`: номер позиции подстроки (отсчитываемый от нуля)
`numberOfChars`(необязательно): количество символов в подстроке

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
Вычитает значение аргумента2 из значения аргумента1.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SUBTRACT(value1, value2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`value1`: число; `value2`: число.
`value1`: длительность; `value2`: длительность.
`value1`: дата и время; `value2`: длительность.
`value1`: дата и время; `value2`: дата и время.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
длительность
дата и время
длительность
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
Суммирует все значения списка, используемого в качестве аргумента. Конкатенация строк не поддерживается.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
SUM(valueList)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`valueList`: список, состоящий из значений типа «Число» или «Длительность»
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
тип возвращаемого значения тот же, что и у элементов списка, являющегося аргументом
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
Переводит строку в нижний регистр (к прописным буквам).

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
`string`: строка
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
Переводит строку в верхний регистр (к заглавным буквам).

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
`string`: строка
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
Возвращает текущего пользователя или идентификатор текущего пользователя, в зависимости от того, к какому типу данных относится поле. Если вычисляемый атрибут принадлежит типу данных Пользователь, функция возвращает текущего пользователя. Если вычисляемый атрибут текстового типа, функция возвращает идентификатор текущего пользователя.

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
аргументы не требуются
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
пользователь или строка
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

- `argument` — проверяемое выражение.
- `defaultValue` — значение по умолчанию. Является необязательным аргументом.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
тип возвращаемого значения совпадает с типом проверяемого выражения
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

Возвращает значение атрибута _Amount_. В противном случае вернёт текст _«Не заполнено поле Amount»_.

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
Возвращает дату на основании количества рабочих дней с определенной даты, с поправкой на праздники и фактические выходные дни.
Если часовой пояс рабочего офиса отличается от часового пояса сервера **{{ companyName }}**, используйте функцию WORKDAYSTZ().

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKDAYS(startDateTime, workingDays,
    [LIST(holiday1, holiday2, …, holidayN)]
    )
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время начала работы,
- `workingDays`: количество рабочих дней,
- `LIST(holiday1, holiday2, …, holidayN)`: праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.

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
Возвращает дату на основании количества рабочих дней с определенной даты, с поправкой на праздники и фактические выходные дни, а также на временную зону рабочего офиса.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKDAYSTZ(startDay, workingDays,
    LIST(holiday1, holiday2, …, holidayN),
    timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время начала работы
- `workingDays`: количество рабочих дней
- `LIST(holiday1, holiday2, …, holidayN)`: праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим
- `timeZone`: часовой пояс рабочего офиса в формате `Olson DB`
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
Возвращает продолжительность работы между двумя датами, на основании предположения, что рабочий день начинается в 00:00 и длится 24 часа.
Если часовой пояс рабочего офиса отличается от часового пояса сервера **{{ companyName }}**, используйте функцию WORKDAYSDURATIONTZ ().

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKDAYSDURATION(startDateTime, endDateTime,
    [LIST(holiday1, holiday2, …, holidayN)])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время начала работы,
- `endDateTime`: дата и время окончания работы,
- `LIST(holiday1, holiday2, …, holidayN)` (необязательно): праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.

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
Возвращает продолжительность работы между двумя датами с поправкой на временную зону рабочего офиса, на основании предположения, что рабочий день начинается в 00:00 и длится 24 часа.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
WORKDAYSDURATIONTZ(startDateTime, endDateTime,
    LIST(holiday1, holiday2, .., holidayN),
    timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время начала работы,
- `endDateTime`: дата и время окончания работы,
- `LIST(holiday1, holiday2, .., holidayN)`: праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим,
- `timeZone`: часовой пояс рабочего офиса в формате `Olson DB`.

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
Возвращает дату и время на основании количества рабочих часов с определенного момента времени, с поправкой на праздники и фактические выходные дни.

Если часовой пояс рабочего офиса отличается от часового пояса сервера **{{ companyName }}**, используйте функцию `WORKHOURSTZ ()`.

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
    [LIST(holiday1, holiday2, .., holidayN)])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время начала работы,
- `workingHours`: количество рабочих часов,
- `workingDayStart`: время начала рабочего дня,
- `workingDayDuration`: длительность рабочего дня (должна быть меньше разницы между 24 ч и временем начала рабочего дня),
- `LIST(holiday1, holiday2, .., holidayN)` (необязательно): праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.

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
Возвращает продолжительность работы между двумя датами при условии, что рабочий день начинается в заданное время и имеет определенную длительность.

Если часовой пояс рабочего офиса отличается от часового пояса сервера **{{ companyName }}**, используйте функцию `WORKHOURSDURATIONTZ()`.

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
    [LIST(holiday1, holiday2, .., holidayN)])
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время начала работы
- `endDateTime`: дата и время окончания работы
- `workingDayStart`: время начала рабочего дня
- `workingDayDuration`: длительность рабочего дня (должна быть меньше разницы между 24 ч и временем начала рабочего дня)
- `LIST(holiday1, holiday2, .., holidayN)` (необязательно): праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.

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
Возвращает продолжительность работы между двумя датами с поправкой на временную зону рабочего офиса, при условии, что рабочий день начинается в заданное время и имеет определенную длительность.

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
    LIST(holiday1, holiday2, .., holidayN),
    timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время начала работы
- `endDateTime`: дата и время окончания работы
- `workingDayStart`: время начала рабочего дня
- `workingDayDuration`: длительность рабочего дня (должна быть меньше разницы между 24 ч и временем начала рабочего дня)
- `LIST(holiday1, holiday2, .., holidayN)`: праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим
- `timeZone`: часовой пояс рабочего офиса в формате `Olson DB`.

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
Возвращает дату и время на основании количества рабочих часов с определенного момента времени, с поправкой на праздники и фактические выходные дни, а также на временную зону рабочего офиса.

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
    LIST(holiday1, holiday2, .., holidayN),
    timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `startDateTime`: дата и время начала работы,
- `workingHours`: количество рабочих часов,
- `workingDayStart`: время начала рабочего дня,
- `workingDayDuration`: длительность рабочего дня (должна быть меньше разницы между 24 ч и временем начала рабочего дня),
- `LIST(holiday1, holiday2, .., holidayN), timeZone)`: праздники и исключения из выходных дней, т. е. если всписке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим,
- `timeZone`: часовой пояс рабочего офиса в формате `Olson DB`.

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
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее году указанной даты в местном часовом поясе.

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
`dateTime`: дата и время
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
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `YEARTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «Дата и время» и возвращает числовое значение, соответствующее году указанной даты в заданном часовом поясе.

Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

```cs
YEARTZ(dateTime, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время
- `timeZone`: строка
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
</tbody>
</table>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
