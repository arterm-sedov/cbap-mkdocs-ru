---
title: 'Функции и литералы в формулах'
kbTitle: 'Литералы и функции в формулах. Справочник, описания, примеры'
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

[](){: #formula_function_list }
# Литералы и функции в формулах. Справочник, описания, примеры {: #formula_reference }

## Введение {: #formula_reference }

Здесь представлены синтаксис и примеры использования функций в формулах **{{ companyName }}**.

## Функции для объявления литералов {: #formula_reference_literals }

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `BOOL()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует строку в логическое значение `True` или `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` sql
BOOL(string)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string` — строка `True` или `False` (без учёта регистра).

При некорректном значении аргумента (`0`, `1`, `истина`, `ложь` и т. п.) функция возвращает пустое значение.

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

``` sql
BOOL('TRUE')
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

### `CREATEDATE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует числовые аргументы (год, месяц, день, часы, минуты, секунды) в значение типа «**Дата и время**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
CREATEDATE(year, month, day)
```

**или**

``` sql
CREATEDATE(year, month, day, hour, minute, second)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`year, month, day, hour, minute, second`: числа.

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

``` sql
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

### `CREATEDATEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует числовые аргументы (год, месяц, день, часы, минуты, секунды) в значение типа «**Дата и время**» в часовом поясе `UTC+00:00`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
CREATEDATEUTC(year, month, day)
```

**или**

``` sql
CREATEDATEUTC(year, month, day, hour, minute, second)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`year, month, day, hour, minute, second`: числа.

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

``` sql
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

### `DATE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует в строку в формате ISO&nbsp;8601 в значение даты и времени.

Функция возвращает значение в часовом поясе, заданном на сервере **{{ productName }}**.

См. также _«[Форматирование значений в шаблонах экспорта и формулах][export_template_file_formula_format_values]»_.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
DATE(string)
```

</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `string`: строка в формате `YYYY-MM-DDThh:mm:ss±hh:mm`
    - `YYYY-MM-DD` — год, месяц, число;
    - `T` — разделитель даты и времени;
    - `hh:mm:ss` — часы, минуты, секунды;
    - `±hh:mm` — часовой пояс.

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
**Примеры**
</td>
<td markdown="block">

- `DATE("2025-08-15")` — 15 августа 2025 г.
- `DATE("13:45:15")` — 13 часов 45 минут 15 секунд текущего дня.
- `DATE("2025-08-15T13:45:15")` — 13 часов 45 минут 15 секунд 15 августа 2025 г. в часовом поясе, заданном на сервере.
- `DATE("2025-08-15T13:45:15+08:00")` — 08 часов 45 минут 15 секунд 15 августа 2025 г., если на сервере задан часовой пояс `UTC+03` (`13-8+3=8`).

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DECIMAL()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует строку в десятичное число.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
DECIMAL(string)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string` — строка с числовым значением.

Значение интерпретируется в соответствии с языком текущего аккаунта текущего пользователя, например:

- `10000`, `10,5` для русского языка;
- `10000`, `10.5` для английского языка.

При неподходящих значениях аргумента (`1 р.`, `$50`, `10 000` и т. п.) функция возвращает пустое значение.

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

``` sql
IF (USER()->language=='ru',
    DECIMAL(REPLACE("10000.5", ".", ",")),
    DECIMAL(REPLACE("10000,5", ",", ".")))
```

Результат: `10000,5` для пользователей с любым языком аккаунта.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DURATION()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует строку в формате ISO&nbsp;8601 в значение длительности.

См. также _«[Форматирование значений в шаблонах экспорта и формулах][export_template_file_formula_format_values]»_.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
DURATION(string)
```

</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `string`: строка в формате `P<n>Y<n>M<n>DT<n>H<n>M<n>S`
    - `<n>` — число;
    - `P` — префикс периода, обязательный;
    - `Y` — годы;
    - `M` — месяцы;
    - `W` — недели;
    - `D` — дни;
    - `T` — префикс времени, используется только для указания времени;
    - `H` — часы;
    - `M` — минуты;
    - `S` — секунды.

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
**Примеры**
</td>
<td markdown="block">

- `DURATION("P3Y6M4DT12H30M5S")` — 3 года 6 месяцев 4 дня 12 часов 30 минут 5 секунд.
- `DURATION("PT3H15M")` — 3 часа 15 минут.
- `DURATION("P3D")` — 3 дня.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ID()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Преобразует строку в идентификатор объекта.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
ID(string)
```

</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `string`: строка с идентификатором объекта.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Идентификатор объекта
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Примеры**
</td>
<td markdown="block">

- `ID("136")` — идентификатор записи `136`.
- `ID("account.2")` — идентификатор аккаунта `account.2`.

</td>
</tr>
</tbody>
</table>

[](){: #formula_reference_functions }
## Математические функции {: #formula_reference_functions_math }

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADD()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Суммирует два значения типа «**Число**», «**Дата и время**» или «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
ADD(argument1, argument2)
```

</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument1`: число, `argument2`: число.
- `argument1`: длительность, `argument2`: длительность.
- `argument1`: дата и время, `argument2`: длительность.

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

``` sql
ADD(DATE('2024-01-01T01:01:01'), DURATION('P3Y6M4DT12H30M5S'))
```

Результат: `03.07.2027 13:31:06`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `CEILING()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Округляет аргумент до ближайшего бо́льшего целого.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` sql
CEILING(number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`number` — число, которое требуется округлить.

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

``` sql
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

### `DIVIDE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает результат деления двух числовых аргументов.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
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

### `FLOOR()`

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

``` sql
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

``` sql
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

### `POW()`

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

``` sql
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

``` sql
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

### `PRODUCT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Перемножает два числовых аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
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

### `QUOTIENT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает целую часть результата деления первого аргумента на второй.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
QUOTIENT(dividend, divisor)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dividend`: число, делимое.
- `divisor`: число, делитель.

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

``` sql
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

### `REMAINDER()`

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

``` sql
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

``` sql
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

### `ROUND()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Округляет число до ближайшего целого.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ROUND(3.5)
```

Результат: `4`

``` sql
ROUND(3.4)
```

Результат: `3`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `SQRT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Вычисляет квадратный корень аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
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

### `SUBTRACT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Вычисляет разность двух аргументов типа «**Число**», «**Длительность**» или «**Дата и время**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
SUBTRACT(17, 10)
```

Результат: `7`

</td>
</tr>
</tbody>
</table>

## Функции для сравнения {: #formula_reference_functions_compare }

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `EQUALS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента и возвращает `True`, если они равны, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
EQUALS(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: логическия значения, дата и время, длительность, числа, или строки.

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

``` sql
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

### `GREATER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает логическое значение `True`, если первый аргумент больше второго, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
GREATER(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: числа, строки, длительность или дата и время.

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

``` sql
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

### `GREATEREQ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает логическое значение `True`, если первый аргумент больше или равен второму, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
GREATEREQ(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: числа, строки, длительность или дата и время.

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

``` sql
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

### `LESS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента, возвращает логическое значение `True`, если первый аргумент меньше второго, в противном случае возвращает `False`.

Строки сравниваются лексикографически — по алфавиту.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
LESS(argument1, argument2)
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

``` sql
LESS(0.1, 1)
```

Результат: `True`

``` sql
LESS("0,1", "0.1")
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

### `LESSEQ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента, возвращает логическое значение `True`, если первый аргумент меньше или равено второму, в противном случае возвращает `False`.

Строки сравниваются лексикографически — по алфавиту.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
LESSEQ(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: число, строка, длительность  или дата и время.

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

``` sql
LESSEQ(1.0, 1)
```

Результат: `True`

``` sql
LESSEQ("1.0", "1")
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

### `NOTEQUALS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента одинакового типа и возвращает логическое значение `True`, если первый аргумент не равен второму, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
NOTEQUALS("Строка", "Сорока")
```

Результат: `True`

</td>
</tr>
</tbody>
</table>

## Логические функции {: #formula_reference_functions_boolean }

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ALL()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает список логических значений и возвращает `True`, если все они имеют значение `True`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>

<td markdown="block">

``` sql
ALL(listBool)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`listBool`: список логических значений или выражений, возвращающих логические значения.

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

``` sql
ALL(LIST(BOOL("True"), BOOL("True"), BOOL("False")))
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

### `AND()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два логических аргумента и возвращает результат их логического умножения (конъюнкции).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
AND(bool1, bool2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`bool1`, `bool2`: логические значения или выражения, возвращающие логическое значение.

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

``` sql
AND(BOOL("True"), BOOL("True"))
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

### `ANY()` {: #any_not_empty }

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Проверка на непустую последовательность.

Проверяет список или набор данных на наличие значений. Возвращает `True`, если аргумент содержит хотя бы одно значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
ANY(dataset)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`dataset`: список значений или набор данных (например сформированный с помощью запроса вида `from ... where ... select`).

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

``` sql
ANY(from in db->Tickets where i->product == "Data Monsoon" select i->name)
```

Результат: `True`, если запрос вернёт хотя бы один элемент.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ANY()` {: #any_predicate }

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Проверка предиката.

Формирует набор данных и возвращает `True`, если в наборе данных есть хотя бы один элемент с истинным значением заданного предиката.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
ANY([(query), queryVar, boolEval])
```

</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `query`: запрос, возвращающий набор данных, вида `from ... where ... select`.
- `queryVar`: локальная переменная, используемая в запросе.
- `boolEval`: выражение с элементом набора данных, возвращающее логическое значение.

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

``` sql
ANY([
    (from i in db->Tickets where i->product=='Data Monsoon' select i),
    i,
    i->NeedsQAHelp
    ])
```

Результат: `True`, если запрос вернёт хотя бы одну запись, в которой значение атрибута `NeedsQAHelp` равно `True`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `IF()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Выполняет тренарную операцию.

Принимает три аргумента. Если первый аргумент равен `True`,  возвращает второй аргумент в противном случае возвращает третий аргумент.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
IF(condition, resultTrue, resultFalse)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `condition`: логическое значение или выражение, возвращающее логическое значение.
- `resultTrue`: значение любого типа, возвращаемое, когда `condition` равно `True`.
- `resultFalse`: значение любого типа, возвращаемое, когда `condition` не равно `True`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">

Тип возвращаемого значения совпадает с типом аргамента `resultTrue` или `resultFalse`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` sql
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

### `NOT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает логический аргумент и выполняет над ним операцию отрицания: возвращает логическое значение `True`, если аргумент имеет значение `False` и наоборот.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
NOT(EMPTY(NOW()))
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

### `OR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два логических аргумента и возвращает результат их логического сложения (дизъюнкции).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
OR(boolean1, boolean2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`boolean1`, `boolean2`: логическоие значения.

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

``` sql
OR(BOOL("True"), BOOL("False"))
```

Результат: `True`

</td>
</tr>
</tbody>
</table>

## Агрегатные функции {: #formula_reference_functions_aggregate }

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ASCENDING()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сортирует элементы списка в порядке возрастания.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
Список
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` sql
ASCENDING('в', 'а', 'б')
```

Результат: `а`, `б`, `в`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `AVERAGE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает среднее арифметическое значение аргументов.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
AVERAGE(argument1, ... argumentN)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argumentN`: числа

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

``` sql
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

### `COUNT()`

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

``` sql
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

``` sql
COUNT(LIST("a", 2, "c", "d", 5))
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

### `DESCENDING()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сортирует элементы списка в порядке возрастания.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
DESCENDING('а', 'б', 'в')
```

Результат: `в`, `б`, `а`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DISTINCT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Удаляет дубликаты элементов из списка.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
DISTINCT(LIST('а', 'а', 'в', 'б', 'Б', 'в'))
```

Результат: `а`, `б`, `Б`, `в`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `FIRST()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает первый элемент списка. При отсутствии элементов возвращает пустое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
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

### `LAST()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает последний элемент списка. При отсутствии элементов возвращает пустое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
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

### `LIST()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает любое количество аргументов любых типов, разделённых запятыми, и возвращает список.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
LIST(argument1, …, argumentN)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, …, `argumentN`: значения любых типов.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Cписок значений таких же типов, как аргументы
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` sql
LIST(1, 2, "a", "b")
```

Результат: `[1, 2, "a", "b"]`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `LISTEQUALS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два списка значений. Если они совпадают, возвращает логическое значение `True`, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
LISTEQUALS(list1, list2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list1`, `list2`: списки значений.
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

``` sql
LISTEQUALS(LIST(1, 2), LIST("1", "2"))
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

### `MAX()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает список значений и возвращает максимальное из значений его элементов.

Все элементы списка должны быть одинакового типа: «**Число**», «**Дата и время**» или «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
MAX(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list`: список значений типа «**Число**», «**Дата и время**» или «**Длительность**»

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">

Тип возвращаемого значения совпадает с типом элементов списка

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` sql
MAX(DURATION('P2DT1H0M0S'), DURATION('P3DT1H0M0S'))
```

Результат: `3.01:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `MIN()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает список значений и возвращает минимальное из значений его элементов.

Все элементы списка должны быть одинакового типа: «**Число**», «**Дата и время**» или «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
MIN(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list`: список значений типа «**Число**», «**Дата и время**» или «**Длительность**»

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">

Тип возвращаемого значения совпадает с типом элементов списка

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` sql
MIN(DURATION('P2DT1H0M0S'), DURATION('P3DT1H0M0S'))
```

Результат: `2.01:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `SUM()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает любое количество аргументов типа «**Число**» или «**Длительность**», перечисленных через запятую, и возвращает их сумму.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
SUM(argument1, ..., argumentN)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1, ..., argumentN`: числа или длительность.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения совпадает с типом аргументов
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` sql
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

### `UNION()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Объединяет в один список два объекта или два списка объектов (ID записей или экземпляров процесса).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
UNION(object1, object2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`object1`, `object2`: объекты или списки объектов.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Список записей
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` sql
UNION(
    from i in db->music where i->album == 'Whale Meditation' select i->id, 
    from i in db->music where i->album == 'Bird Song' select i->id)
```

Результат: список ID песен из альбомов `Whale Meditation` и `Bird Song`.

</td>
</tr>
</tbody>
</table>

## Системные функции {: #formula_reference_functions_system }

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `EMPTY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Проверяет, является ли пустым значение аргумента. Возвращает логическое значение `True`, если значение пустое, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
EMPTY(DIVIDE(3, 3))
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

### `ENUMVALUE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает системное имя атрибута атрибута типа «**Список значений**» и системное имя его значения и вовзрращает ID этого значения.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
EQUALS($Status, ID(ENUMVALUE("Status", "Resolved")))
```

Результат: `True`, если атрибут `Status` имеет значение `Resolved`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `OBJECT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает четыре строковых аргумента: системные имена приложения, шаблона и атрибута, а также значение атрибута типа «**Текст**». Возвращает список ID записей из указанного шаблона, в которых указанный атрибут имеет заданное значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `attributeValue`: строка, искомое значение атрибута.

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

``` sql
OBJECT("Fleetmanagement", "Requests", "Status", "Завершено")
```

Результат: список ID записей шаблона _«Заявки»_ (системное имя — `Requests`) приложения _«Управление автопарком»_ (системное имя — `Fleetmanagement`), у которых значение атрибута _«Статус»_ (системное имя — `Status`) равно `Завершено`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `USER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает идентификатор аккаунта текущего пользователя.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
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

### `VALUE()`

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

``` sql
VALUE(argument, defaultValue)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument`: проверяемое выражение, возвращающее значение любого типа.
- `defaultValue`: значение по умолчанию любого типа (необязательный аргумент).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения совпадает с типом первого или второго аргумента.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` sql
VALUE($Amount, "Не заполнено поле Amount")
```

Результат: значение атрибута _Amount_, если оно не пустое. В противном случае — текст _«Не заполнено поле Amount»_.

</td>
</tr>
</tbody>
</table>

## Функции для обработки строк {: #formula_reference_functions_date_string }

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `CONCAT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Объединяет строки из списка в одну строку.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
CONCAT(LIST("Сумма доходов равна: ", "100000"))
```

Результат: `Сумма доходов равна: 100000`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `CONTAINS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Ищет подстроку в строке. Если первая строка содержит вторую, возвращает логическое значение `True`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `substring` — подстрока, которую требуется найти.

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

``` sql
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

### `ENDSWITH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает две строки и возвращает значение `True`, если первая строка оканчивается на вторую, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
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

### `FIRSTCAPITAL()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует первую букву строки в прописную (заглавную).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
Строка.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` sql
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

### `FORMAT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает строку с заполнителями вида `{0}`…`{N}` и список значений. Подставляет значения из списка в соответствующие заполнители, форматирует их по заданному шаблону и возвращает результирующую строку.

См. также _«[Форматирование значений в шаблонах экспорта и формулах][export_template_file_formula_format_values]»_.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
FORMAT("stringToFormat {0} {1} ... {N}", LIST(argument0, argument1, ..., valueN))
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `"stringToFormat {0} {1} ... {N}"`: строка с заменителями.
- `LIST(argument0, argument1, ..., argumentN)`: список значений любых типов.

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

``` sql
FORMAT(
    "Название: {0}, исполнитель: {1}, дата релиза: {2:dd MMMM yyyy 'г.'}",
    LIST("Yesterday","Beatles", DATE("1965-06-14"))
    )
```

Результат: `Название: Yesterday, исполнитель: Beatles, дата релиза: 14 июня 1965 г.`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `INDEXOF()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Ищет подстроку в строке. Возвращает номер позиции (по умолчанию поиск отсчёт идёт от `0`) искомой строки в исходной строке. Также можно указать номер начальной позиции для поиска.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
INDEXOF(sourceString, stringToFind, startIndex)
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
- `startIndex`: номер начальной позиции для поиска (необязательный аргумент).

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

``` sql
INDEXOF("У ёлки иголки колки.", "лки", 4)
```

Результат: `10`

``` sql
INDEXOF("У ёлки иголки колки.", "лки")
```

Результат: `3`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `JOIN()`

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

``` sql
JOIN(separator, stringList)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`separator`: строка, разделитель объединяемых строк.
`stringList`: список строк, которые требуется объединить.
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

``` sql
JOIN(", ", LIST("Аналитик", "Архитектор", "Администратор"))
```

Результат: `Аналитик, Архитектор, Администратор`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `LENGTH()`

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

``` sql
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

``` sql
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

### `MATCHES()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает строку и регулярное выражение. Возвращает логическое значение `True`, если часть строки или вся строка соответствует регулярному выражению. В противном случае возвращает `False`.

Для изучения и отладки регулярных выражений можно воспользоваться следующим инструментом: <https://regex101.com>

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
`regex`: строка с регулярным выражением.

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

``` sql
MATCHES("Требуется решить проблему срочно!", "[Cс]рочн.+?")
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

### `NORMALIZE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Убирает лишние пробелы из строкового аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
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

### `NOTMATCHES()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает строку и регулярное выражение. Возвращает логическое значение `True`, если часть строки или вся строка не соответствует регулярному выражению. В противном случае возвращает `False`.

Для изучения и отладки регулярных выражений можно воспользоваться следующим инструментом: <https://regex101.com>

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `regex`: строка, задающая регулярное выражение.

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

``` sql
NOTMATCHES("Требуется решить проблему срочно!", "[Cс]рочн.+?")
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

### `REGEXREPLACE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block">
<span >Описание
</td>
<td markdown="block">

Принимает три строковых аргумента: исходную строку, регулярное выражение, замещающую строку. Находит в исходной строке подстроки по регулярному выражению, заменяет найденные подстроки замещающей строкой и возвращает результирующую строку.

Для изучения и отладки регулярных выражений можно воспользоваться следующим инструментом: <https://regex101.com>

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
REGEXREPLACE("Фамилия Имя Отчество","(.+) (.+) (.+)","$2")
```

Результат: `Имя`

``` sql
REGEXREPLACE("Рассмотрите заявку [#12345]",".*\[#([0-9]+)\].*","$1")
```

 Результат: `12345`

``` sql
REGEXREPLACE($HTML,"&lt;p class=""title"">(.+)&lt;\/p>","&lt;h1>$1&lt;h1>")
```

Результат: заменяет в HTML-коде параграфы класса `title` на заголовки уровня 1.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `REPLACE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает три строки: исходную, искомую и замещающую. Заменяет все вхождения искомой строки в исходной строке на замещающую строку.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
REPLACE(string, subString, replacementString)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`string`, `subString`, `replacementString`: строки

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

``` sql
REPLACE("Заявка утверждена.", "утверждена", "одобрена")
```

Результат: `Заявка одобрена.`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `TOLOWER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Приводит все буквы в строке к нижнему регистру (строчным буквам).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
TOLOWER("Все Буквы В ЭТОЙ Строке Стали Строчными.")
```

Результат: `все буквы в этой строке стали строчными.`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `TOUPPER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Приводит все буквы в строке к верхнему регистру (прописным буквам).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
TOUPPER("Все Буквы В Этой Строке Стали прописными.")
```

Результат: `ВСЕ БУКВЫ В ЭТОЙ СТРОКЕ СТАЛИ ПРОПИСНЫМИ.`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `TRIM()`

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

``` sql
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

``` sql
TRIM("   В этой строке были лишние пробелы.   ")
```

Результат: `В этой строке были лишние пробелы.`

</td>
</tr>
</tbody>
</table>


<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `STARTSWITH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает две строки и возвращает значение `True`, если первая строка начинается на вторую, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
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

### `SUBSTRING()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает три аргумента: строку и два числа. Извлекает из исходной строки подстроку начиная с заданной позиции до конца исходной строки либо до указанной длины подстроки.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
SUBSTRING(sourceString, startIndex, numberOfChars)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `sourceString`: строка.
- `startIndex`: номер позиции начала подстроки, отсчитывается от `0`.
- `numberOfChars`: количество символов в подстроке (необязательный аргумент).

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

``` sql
SUBSTRING("Раньше эта строка начиналась с другого слова.", 7, 31)
```

Результат: `эта строка начиналась с другого`

</td>
</tr>
</tbody>
</table>

## Функции для обработки дат, времени и длительности {: #formula_reference_functions_date_time_duration }

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDDAYS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество дней к значению типа «**Дата и время**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `numberOfDays`: количество дней, которое требуется прибавить.

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

``` sql
ADDDAYS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `04.01.2024 1:01:01`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDDAYSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество дней к значению типа «**Дата и время**» и переводит результат в часовой пояс `UTC+00:00`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `numberOfDays`: количество дней, которое требуется прибавить.

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

``` sql
ADDDAYSUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат при `UTC+03:00` на сервере: `04.01.2024 04:01:01`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDDUR()`

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

``` sql
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

``` sql
ADDDUR(DURATION('P1DT12H30M5S'), DURATION('P1DT12H30M5S'))
```

Результат: `3 д 1 ч 10 с`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDHOURS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество часов к значению типа «**Дата и время**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
ADDHOURS(dateTime, numberOfHours)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfHours`: количество часов, которое требуется прибавить.

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

``` sql
ADDHOURS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 4:01:01`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDHOURSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество часов к значению типа «**Дата и время**» и переводит результат в часовой пояс `UTC+00:00`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
ADDHOURSUTC(dateTime, numberOfHours)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfHours`: количество часов, которое требуется прибавить.

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

``` sql
ADDHOURSUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат при `UTC+03:00` на сервере: `01.01.2024 07:01:01`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDLOC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет значение типа «**Длительность**» к значению типа «**Дата и время**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `duration`: длительность, которую требуется прибавить.

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

``` sql
ADDLOC(DATE('2024-01-01T01:01:01'), DURATION('P1DT12H30M5S'))
```

Результат: `02.01.2024 13:31:06`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDMINUTES()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество минут к значению типа «**Дата и время**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `numberOfMinutes`: количество минут, которое требуется прибавить.

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

``` sql
ADDMINUTES(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 01:04:01`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDMINUTESUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество минут к значению типа «**Дата и время**» и переводит результат в часовой пояс `UTC+00:00`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `numberOfMinutes`: количество минут, которое требуется прибавить.

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

``` sql
ADDMINUTESUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат при `UTC+03:00` на сервере: `01.01.2024 04:04:01`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDMONTHS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество месяцев к значению типа «**Дата и время**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `numberOfMonths`: количество месяцев, которое требуется прибавить.

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

``` sql
ADDMONTHS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.04.2024 1:01:01`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDMONTHSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество месяцев к значению типа «**Дата и время**» и переводит результат в часовой пояс `UTC+00:00`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `numberOfMonths`: количество месяцев, которое требуется прибавить.

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

``` sql
ADDMONTHSUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат при `UTC+03:00` на сервере: `01.04.2024 04:01:01`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDSECONDS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество секунд к значению типа «**Дата и время**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
ADDSECONDS(dateTime, numberOfSeconds)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfSeconds`: количество секунд, которое требуется прибавить.

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

``` sql
ADDSECONDS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 1:01:04`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDSECONDSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество секунд к значению типа «**Дата и время**» и переводит результат в часовой пояс `UTC+00:00`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
ADDSECONDSUTC(dateTime, numberOfSeconds)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfSeconds`: количество секунд, которое требуется прибавить.

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

``` sql
ADDSECONDSUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат при `UTC+03:00` на сервере: `01.01.2024 4:01:04`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет значение типа «**Длительность**» к значению типа «**Дата и время**» и переводит результат в часовой пояс `UTC+00:00`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `duration`: длительность, которую требуется прибавить.

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

``` sql
ADDUTC(DATE('2024-01-01T01:01:01+00:00'), DURATION('P1DT12H30M5S'))
```

Результат при `UTC+03:00` на сервере: `02.01.2024 16:31:06`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDYEARS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество лет к значению типа «**Дата и время**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
ADDYEARS(dateTime, numberOfYears)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfYears`: количество лет, которое требуется прибавить.

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

``` sql
ADDYEARS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2027 1:01:01`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ADDYEARSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Прибавляет указанное количество лет к значению типа «**Дата и время**» и переводит результат в часовой пояс `UTC+00:00`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
ADDYEARSUTC(dateTime, numberOfYears)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `numberOfYears`: количество лет, которое требуется прибавить.

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

``` sql
ADDYEARSUTC(DATE('2024-01-01T01:01:01+00:00'), 3)
```

Результат при `UTC+03:00` на сервере: `01.01.2027 4:01:01`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `BETWEEN()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает `True`, если значение типа «**Дата и время**» или «**Длительность**» входит в заданный диапазон.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
BETWEEN(DURATION("PT3H15M"), DURATION("PT3H1M"), DURATION("PT3H25M"))
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

### `BETWEENUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Возвращает `True`, если значение типа «**Дата и время**» или «**Длительность**» входит в заданный диапазон. Приводит значения типа «**Дата и время**» к часовому поясу `UTC+00:00`.

</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
BETWEENUTC(
    DATE("2025-01-15+00:00"),
    DATE("2024-02-15+01:00"),
    DATE("2024-08-15-01:00")
)
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

### `CENTURY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает число, соответствующее веку аргумента.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
CENTURY(DATE("2000-01-01T05:45:15"))
```

Результат: `21`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `CENTURYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает номер века, на который приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
CENTURYUTC(DATE("2000-01-01T05:45:15+10:00"))
```

Результат: `20`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `COMPARE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два значения типа «**Длительность**» и возвращает целое число:

- `1`, если первый аргумент больше второго;
- `0`, если аргументы равны;
- `-1`, если первый аргумент меньше второго.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
COMPARE(DURATION("PT3H15M"), DURATION("PT3H16M"))
```

Возвращает `-1`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `CONVERTTIMEZONE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Переводит значение типа «**Дата и время**» в заданный часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
CONVERTTIMEZONE(dateTime, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime` — дата и время.
- `timeZone` — строка, задающая часовой пояс в формате IANA.

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
CONVERTTIMEZONE(DATE("2025-05-05T13:45:15+00:00"), "Europe/London")
```

Результат при `UTC+03:00` на сервере: `05.05.2025 14:45:15`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `CONVERTTIMEZONEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Переводит значение типа «**Дата и время**» в часовой пояс `UTC+00:00`, а затем в заданный часовой пояс в формате IANA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
CONVERTTIMEZONEUTC(dateTime, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime` — дата и время.
- `timeZone` — строка, задающая часовой пояс в формате IANA.

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

``` sql
CONVERTTIMEZONEUTC(DATE("2025-05-05T13:45:15+00:00"), "Europe/Moscow")
```

Результат: `05.05.2025 16:45:15`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DAY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает значение типа «**Дата и время**» и строку с часовым поясом в формате IANA. Возвращает число месяца, на которое приходится указанная дата с учётом часового пояса.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `timeZone`: строка, задающая часовой пояс в формате IANA (необязательный аргумент).

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

``` sql
DAY(DATE("2025-05-05T23:45:15+00:00"), "Europe/Moscow")
```

Результат: `6`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DAYOFWEEK()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает название соответствующего дня недели.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
DAYOFWEEK(DATE("2025-05-05T23:45:15"))
```

Результат: `понедельник`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DAYOFWEEKUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» переводит его в часовой пояс `UTC+00:00` и возвращает название дня недели, на который приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
DAYOFWEEKUTC(DATE("2025-05-05T20:45:15-01:00"))
```

Результат: `понедельник`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DAYOFYEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает номер дня соответствующего года.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
DAYOFYEAR(DATE("2025-05-05T23:45:15"))
```

Результат: `125`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DAYOFYEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает номер дня года, на который приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
DAYOFYEARUTC(DATE("2025-05-05T23:45:15+00:00"))
```

Результат: `125`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DAYS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует значение типа «**Длительность**» в десятичное число, представляющее количество дней.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
DAYS(DURATION('P12DT64H75M1360S'))
```

Результат: `14,7344907407407`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DAYSINMONTH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» или два аргумента типа «**Число**» — год и месяц. Возвращает количество дней в соответствующем месяце.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
DAYSINMONTH(dateTime)
```

**или**

``` sql
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
- `year, month`: числа.

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

``` sql
DAYSINMONTH(2024, 02)
```

Результат: `29`

``` sql
DAYSINMONTH(DATE("2025-02-05T23:45:15"))
```

Результат: `28`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DAYSINMONTHUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» или два аргумента типа «**Число**» — год и месяц. Преобразует дату и время в часовой пояс `UTC+00:00`. Возвращает количество дней в результирующем месяце.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
DAYSINMONTHUTC(dateTime)
```

**или**

``` sql
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
- `year, month`: числа.

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

``` sql
DAYSINMONTHUTC(2025, 02)
```

Результат: `28`

``` sql
DAYSINMONTHUTC(DATE("2025-02-28T23:45:15-02:00"))
```

Результат: `31`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `DAYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает число месяца, на который приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
DAYUTC(DATE("2025-04-30T23:45:15-02:00"))
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

### `ENDOFDAY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время окончания соответствующего дня.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ENDOFDAY(DATE('2025-05-05T01:01:01'))
```

Результат: `05.05.2025 23:59:59`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ENDOFDAYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает дату и время окончания результирующего дня.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ENDOFDAYUTC(DATE('2025-05-05T01:01:01+03:00'))
```

Результат при `UTC+03:00` на сервере: `05.05.2025 02:59:59`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ENDOFMONTH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время окончания соответствующего месяца.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ENDOFMONTH(DATE('2025-05-05T01:01:01'))
```

Результат: `31.05.2025 23:59:59`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ENDOFMONTHUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает дату и время окончания месяца, на который приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ENDOFMONTHUTC(DATE('2025-05-01T01:01:01+03:00'))
```

Результат для `UTC+03:00` на сервере: `01.05.2025 02:59:59`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ENDOFQUARTER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время окончания соответствующего квартала.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ENDOFQUARTER(DATE('2025-04-01T01:01:01'))
```

Результат: `30.06.2025 23:59:59`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ENDOFQUARTERUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает дату и время окончания квартала, на который приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ENDOFQUARTERUTC(DATE('2025-04-01T01:01:01+03:00'))
```

Результат для `UTC+03:00` на сервере: `01.04.2025 02:59:59`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ENDOFWEEK()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», и возвращает дату и время окончания соответствующей недели.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ENDOFWEEK(DATE('2025-05-05T01:01:01'))
```

Результат: `11.05.2025 23:59:59`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ENDOFWEEKUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает дату и время окончания недели, на которую приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ENDOFWEEKUTC(DATE('2025-05-05T01:01:01+03:00'))
```

Результат для `UTC+03:00` на сервере: `05.05.2025 02:59:59`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ENDOFYEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время окончания соответствующего года.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ENDOFYEAR(DATE('2025-01-01T01:01:01'))
```

Результат: `31.12.2025 23:59:59`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ENDOFYEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает дату и время окончания года, на который приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ENDOFYEARUTC(DATE('2025-01-01T01:01:01+03:00'))
```

Результат при `UTC+03:00` на сервере: `31.12.2024 23:59:59`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `EQ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента типа «**Дата и время**» или «**Длительность**» и возвращает значение `True`, если они равны, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
EQ(argument1, argument2)
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

``` sql
EQ(DURATION('P2DT1H30M30S'), DURATION('P1DT25H30M30S'))
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

### `EQUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два аргумента типа «**Дата и время**», преобразует их в часовой пояс `UTC+00:00`. Сравнивает результирующие значения и возвращает значение `True`, если они равны, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
EQUTC(DATE('2025-01-01T01:01:01+03:00'), DATE('2025-01-01T00:01:01+02:00'))
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

### `FORMATDUR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует значение типа «**Длительность**» в строку формата ISO&nbsp;8601.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
FORMATDUR(INSECONDS(5000000))
```

Результат: `P57DT20H53M20S`, где:

- `P` — префикс периода;
- `Y` — годы;
- `M` — месяцы;
- `W` — недели;
- `D` — дни;
- `T` — префикс времени;
- `H` — часы;
- `M` — минуты;
- `S` — секунды.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `FORMATLOC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует значение типа «**Дата и время**» в строку формата ISO&nbsp;8601.

См. также _«[Форматирование значений в шаблонах экспорта и формулах][export_template_file_formula_format_values]»_.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `formatString`: строка, задающая формат ISO&nbsp;8601.

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

``` sql
FORMATLOC(DATE('2025-05-05T05:05:25'), "dd MMMM yyyy г. hh:mm:ss")
```

Результат: `05 мая 2025 г. 05:05:25`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `FORMATUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует значение типа «**Дата и время**» в строку формата ISO&nbsp;8601 в часовом поясе `UTC+00:00`.

См. также _«[Форматирование значений в шаблонах экспорта и формулах][export_template_file_formula_format_values]»_.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
FORMATUTC(DATE('2025-05-05T05:05:25+03:00'), "dd MMMM yyyy года hh:mm:ss")
```

Результат: `05 мая 2025 г. 02:05:25`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `GE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента типа «**Дата и время**» или «**Длительность**». Возвращает логическое значение `True`, если первый аргумент больше или равен второму, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
GE(DURATION('P1DT1H30M30S'), DURATION('P2DT1H30M30S'))
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

### `GETSPAN()`

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

``` sql
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

``` sql
GETSPAN(DATE('2025-05-05T05:05:25'), DATE('2025-05-05T10:10:50'))
```

Результат: `-05:05:25`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `GETSPANUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два аргумента типа «**Дата и время**», переводит их значения в часовой пояс `UTC+00:00` и вычисляет длительность между результирующими значениями.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
GETSPANUTC(DATE('2025-05-05T05:05:25+00:00'), DATE('2025-05-05T05:05:25+05:00'))
```

Результат: `05:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `GEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два аргумента типа «**Дата и время**», переводит их значения в часовой пояс `UTC+00:00`. Сравнивает результирующие значения и возвращает логическое значение `True`, если первое значение больше или равно второму, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
GEUTC(DATE('2025-05-05T05:05:25+00:00'), DATE('2025-05-05T05:05:25+05:00'))
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

### `GT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два аргумента типа «**Дата и время**» или «**Длительность**». Возвращает логическое значение `True`, если первый аргумент больше второго, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
GT(DATE('2025-05-05T05:05:25'), DATE('2025-05-05T05:05:25'))
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

### `GTUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два аргумента типа «**Дата и время**» и переводит их значения в часовой пояс `UTC+00:00`. Возвращает логическое значение `True`, если первое значение больше второго, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
GTUTC(DATE('2025-05-05T05:05:25+00:00'), DATE('2025-05-05T05:05:25+05:00'))
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

### `HOUR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает значение типа «**Дата и время**» и строку с часовым поясом в формате IANA. Возвращает час результирующего времени с учётом часового пояса.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `timeZone`: строка, задающая часовой пояс в формате IANA (необязательный аргумент).

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

``` sql
HOUR(DATE('2025-05-05T05:05:25+00:00'), "Europe/Moscow")
```

Результат: `8`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `HOURS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует аргумент типа «**Длительность**» в количество часов в десятичном формате.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
HOURS(DURATION('P2DT1H30M0S'))
```

Результат: `49,5`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `HOURUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает число, соответствующее часу результирующего времени.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
HOURUTC(dateTime)
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

``` sql
HOURUTC(DATE('2025-05-05T05:05:25+03:00'))
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

### `INSECONDS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

- Преобразует аргумент типа «**Дата и время**» или «**Длительность**» в количество секунд.
- Преобразует количество секунд в аргументе типа «**Число**» в значение типа «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

- Количество секунд для аргумента типа «**Дата и время**» или «**Длительность**».
- Длительность для аргумента типа «**Число**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` sql
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

### `INSECONDSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

- Переводит аргумент типа «**Дата и время**» в часовой пояс `UTC+00:00` и возвращает количество секунд в результирующем значении.
- Преобразует аргумент типа «**Длительность**» в количество секунд.
- Преобразует количество секунд в аргументе типа «**Число**» в значение типа «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

- Количество секунд для аргумента типа «**Дата и время**» или «**Длительность**».
- Длительность для аргумента типа «**Число**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` sql
INSECONDSUTC(DATE('2025-05-05T05:05:25'))
```

Результат: `63882018325`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ISLEAPYEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает логическое значение `True`, если год указанной даты является високосным, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ISLEAPYEAR(DATE('2025-01-01T01:01:01'))
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

### `ISLEAPYEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает логическое значение `True`, если год результирующей даты является високосным, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ISLEAPYEARUTC(DATE('2025-01-01T01:01:01+03:00'))
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

### `ISOFORMAT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует значение типа «**Дата и время**» в строку формата ISO&nbsp;8601.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ISOFORMAT(NOW())
```

Результат: `2025-05-28T09:07:52.362149+03:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ISOFORMATUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает значение типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и преобразует в строку формата ISO&nbsp;8601.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ISOFORMATUTC(NOW())
```

Результат: `2025-05-28T06:10:39.357235Z`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ISTODAY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает логическое значение `True`, если значение аргумента приходится на текущую дату, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ISTODAY(NOW())
```

Результат: `True`, так как `NOW()` возвращает текущую дату.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ISTODAYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00`и возвращает логическое значение `True`, если результирующее значение приходится на текущую дату, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ISTODAYUTC(NOW())
```

Результат: `True`, если дата в часовом поясе `UTC+00:00` совпадает с текущей датой.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `ISWEEKEND()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает логическое значение `True`, если значение аргумента приходится на выходной день, в противном случае возвращает результат `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ISWEEKEND(DATE('2025-05-05T01:01:01'))
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

### `ISWEEKENDUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает логическое значение `True`, если результирующее значение приходится на выходной день, в противном случае возвращает результат `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ISWEEKENDUTC(DATE('2025-05-05T01:01:01+03:00'))
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

### `ISWORKDAY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает логическое значение `True`, если значение аргумента приходится на рабочий день, в противном случае возвращает результат `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ISWORKDAY(DATE('2025-05-05T01:01:01'))
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

### `ISWORKDAYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает логическое значение `True`, если результирующее значение приходится на рабочий день, в противном случае возвращает результат `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
ISWORKDAYUTC(DATE('2025-05-05T01:01:01+03:00'))
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

### `LE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента типа «**Дата и время**» или «**Длительность**». Если первый аргумент меньше или равен второму, возвращает логическое значение `True`, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
LE(DURATION('P2DT1H0M0S'), DURATION('P3DT1H0M0S'))
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

### `LT()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента типа «**Дата и время**» или «**Длительность**» и возвращает логическое значение `True`, если первый аргумент меньше второго, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
LT(DURATION('P2DT1H0M0S'), DURATION('P3DT1H0M0S'))
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

### `LTUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два аргумента типа «**Дата и время**», переводит их значения в часовой пояс `UTC+00:00` и возвращает логическое значение `True`, если первое значение меньше второго, в противном случае возвращает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
LTUTC(DATE('2025-05-05T01:01:01+03:00'), DATE('2025-05-05T01:01:01+04:00'))
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

### `MINUTE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и строку с часовым поясом в формате IANA.

Приводит аргумент к заданному часовому поясу и возвращает минуты результирующего времени.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
MINUTE(dateTime, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `timeZone`: строка, задающая часовой пояс в формате IANA (необязательный аргумент).

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

``` sql
MINUTE(DATE('2025-05-05T01:01:01'))
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

### `MINUTES()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует аргумент типа «**Длительность**» в количество минут в десятичном формате.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
MINUTES(DURATION('P1DT1H30M30S'))
```

Результат: `1530,5`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `MINUTEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его значение в часовой пояс `UTC+00:00` и возвращает число, соответствующее минутам результирующего времени.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
MINUTEUTC(DATE('2025-05-05T01:01:01+03:30'))
```

Результат: `31`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `MONTH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и строку с часовым поясом в формате IANA.

Приводит аргумент к заданному часовому поясу и возвращает месяц результирующей даты.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
MONTH(dateTime, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `timeZone`: строка, задающая часовой пояс в формате IANA (необязательный аргумент).

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

``` sql
MONTH(DATE('2025-05-01T01:01:01+03:00'), "Europe/London")
```

Результат: `4`

``` sql
MONTH(DATE('2025-05-01T01:01:01+03:00'), "Europe/Moscow")
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

### `MONTHS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует аргумент типа «**Длительность**» в количество месяцев в десятичном формате.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
MONTHS(DURATION('P45D'))
```

Результат: `1,5`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `MONTHUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает число, соответствующее месяцу указанной даты для часового пояса `UTC+00:00`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
MONTHUTC(DATE('2025-05-01T01:01:01+03:00'))
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

### `NE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Сравнивает два аргумента типа «**Дата и время**» или «**Длительность**» и возвращает логическое значение `True`, если они не равны, в противном случае возврашает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
NE(DURATION('P0DT25H30M0S'), DURATION('P1DT1H30M0S'))
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

### `NEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два аргумента типа «**Дата и время**», переводит их значения в часовой пояс `UTC+00:00` и возвращает логическое значение `True`, если результирующие значения не равны, в противном случае возврашает `False`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
NEUTC(DATE('2025-05-01T01:01:01+03:00'), DATE('2025-05-01T01:01:01+02:00'))
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

### `NOW()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">
Возвращает текущие дату и время.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
NOW()
```

Результат: `28.05.2025 12:01:53`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `PARSEDATE()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует строку в значение типа «**Дата и время**» согласно заданной маске в формате ISO&nbsp;8601.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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
- `stringFormat`: строка, задающая формат даты по стандарту ISO&nbsp;8601.

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

``` sql
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

### `PARSEDATEUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует строку в значение типа «**Дата и время**» в часовом поясе `UTC+00:00` согласно заданной маске в формате ISO&nbsp;8601.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
PARSEDATEUTC(string, stringFormat)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `string`: строка.
- `stringFormat`: строка, задающая формат даты по стандарту ISO&nbsp;8601.

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

``` sql
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

### `QUARTERS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует аргумент типа «**Длительность**» в количество кварталов в десятичном формате.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
QUARTERS(DURATION('P229D'))
```

Результат: `2,5`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `SECOND()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и строку с часовым поясом в формате IANA.

Приводит аргумент к заданному часовому поясу и возвращает секунды результирующего времени.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
SECOND(dateTime, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `timeZone`: строка, задающая часовой пояс в формате IANA (необязательный аргумент).

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

``` sql
SECOND(DATE('2025-05-05T01:01:01'), "Europe/London")
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

### `SECONDS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует аргумент типа «**Длительность**» в количество секунд.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
SECONDS(DURATION('P1DT1H30M0S'))
```

Результат: `91800`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `SECONDUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает число, соответствующее секундам резуьтирующего времени.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
SECONDUTC(DATE('2025-05-05T01:01:01+01:00'))
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

### `STARTOFDAY()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала соответствующего дня.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
STARTOFDAY(DATE('2025-05-05T01:01:01'))
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

### `STARTOFDAYUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает дату и время начала результирующего дня.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
STARTOFDAYUTC(DATE('2025-05-05T01:01:01+03:00'))
```

Результат при `UTC+03:00` на сервере: `04.05.2025 03:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `STARTOFMONTH()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала соответствующего месяца.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
STARTOFMONTH(DATE('2025-05-01T01:01:01'))
```

Результат: `01.05.2025 0:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `STARTOFMONTHUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает дату и время начала месяца, на который приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
STARTOFMONTHUTC(DATE('2025-05-01T01:01:01+03:00'))
```

Результат при `UTC+03:00` на сервере: `01.04.2025 03:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `STARTOFQUARTER()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала соответствующего квартала.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
STARTOFQUARTER(DATE('2025-04-01T01:01:01'))
```

Результат: `01.04.2025 0:00:00`


</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `STARTOFQUARTERUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает дату и время начала квартала, на который приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
STARTOFQUARTERUTC(DATE('2025-04-01T01:01:01+03:00'))
```

Результат при `UTC+03:00` на сервере: `01.01.2025 03:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `STARTOFWEEK()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала соответствующей недели.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
STARTOFWEEK(DATE('2025-05-05T01:01:01'))
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

### `STARTOFWEEKUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает дату и время начала недели, на которую приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
STARTOFWEEKUTC(DATE('2025-05-05T01:01:01+03:00'))
```

Результат при `UTC+03:00` на сервере: `28.04.2025 03:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `STARTOFYEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала соответствующего года.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
STARTOFYEAR(DATE('2025-01-01T01:01:01'))
```

Результат: `01.01.2025 0:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `STARTOFYEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает дату и время начала года, на который приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
STARTOFYEARUTC(DATE('2025-01-01T01:01:01+03:00'))
```

Результат для `UTC+03:00`: `01.01.2024 03:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `SUB()`

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

``` sql
SUB(dateTime, duration)
```

**или**

``` sql
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

``` sql
SUB(DATE('2025-01-01T01:01:01'), DURATION('P1DT1H30M0S'))
```

Результат: `30.12.2024 23:31:01`

</td>
</tr>
</tbody>
</table>



<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `SUBUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Вычитает из значения типа «**Дата и время**» значение типа «**Длительность**». Возвращает значение типа «**Дата и время**» для часового пояса `UTC+00:00`.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
SUBUTC(DATE('2025-01-01T01:01:01+00:00'), DURATION('P1DT1H30M0S'))
```

Результат при `UTC+03:00` на сервере: `31.12.2024 02:31:01`.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `TODURATION()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует количество секунд в значение типа «**Длительность**».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
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

### `WEEKOFYEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает номер недели соответствующего года.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
WEEKOFYEAR(DATE('2025-05-06T01:01:01'))
```

Результат: `18`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `WEEKOFYEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает номер недели года, на которую приходится результирующая дата.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
WEEKOFYEARUTC(DATE('2025-05-06T01:01:01+03:00'))
```

Результат при `UTC+03:00` на сервере: `17`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `WORKDAYS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает три аргумента: дату, количество рабочих дней и список исключаемых дат.

Прибавляет к исходной дате количество рабочих дней с учётом выходных дней и списка исключений и возвращает результирующую дату.

Если в списке исключений указан рабочий день, он считается выходным, а если если указан выходной день, он считается рабочим.

Если рабочий часовой пояс отличается от часового пояса сервера **{{ productName }}**, используйте функцию [WORKDAYSTZ()](#workdaystz).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
WORKDAYS(
    startDateTime, workingDays,
    LIST(excludedDate1, …, excludedDateN)
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
- `workingDays`: количество рабочих дней.
- `LIST(excludedDate1, …, excludedDateN)` (необязательный аргумент): список исключаемых дат.

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

``` sql
WORKDAYS(
    DATE('2025-05-01'), 10,
    LIST(
        DATE('2025-05-01'), 
        DATE('2025-05-02'),
        DATE('2025-05-08'),
        DATE('2025-05-09')
    )
)
```

Результат: `21.05.2025 0:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `WORKDAYSDURATION()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает три аргумента: начальные дату и время, конечные дату и время и список исключаемых дат.

Возвращает длительность между начальной и конечной датой с учётом выходных дней и списка исключений.

Если в списке исключений указан рабочий день, он считается выходным, а если если указан выходной день, он считается рабочим.

Если рабочий часовой пояс отличается от часового пояса сервера **{{ productName }}**, используйте функцию [WORKDAYSDURATIONTZ()](#workdaysdurationtz).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
WORKDAYSDURATION(
    startDateTime, endDateTime,
    LIST(excludedDate1, …, excludedDateN)
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
- `LIST(excludedDate1, …, excludedDateN)`: (необязательный аргумент): список исключаемых дат.

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

``` sql
WORKDAYSDURATION(
    DATE('2025-05-01'), DATE('2025-05-12'),
    LIST(
        DATE('2025-05-01'),
        DATE('2025-05-02'),
        DATE('2025-05-08'),
        DATE('2025-05-09')
    )
)
```

Результат: `3.00:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `WORKDAYSDURATIONTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает три аргумента: начальные дату и время, конечные дату и время, список исключаемых дат и часовой пояс.

Возвращает длительность между начальной и конечной датой с учётом выходных дней, списка исключений и часового пояса.

Если в списке исключений указан рабочий день, он считается выходным, а если если указан выходной день, он считается рабочим.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
WORKDAYSDURATIONTZ(
    startDateTime, endDateTime,
    LIST(excludedDate1, …, excludedDateN),
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
- `LIST(excludedDate1, …, excludedDateN)`: (необязательный аргумент): список исключаемых дат.
- `timeZone`: строка, задающая часовой пояс в формате IANA.

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

``` sql
WORKDAYSDURATIONTZ(
    DATE('2025-05-01'), DATE('2025-05-12'), 
    LIST(
        DATE('2025-05-01'),
        DATE('2025-05-02'),
        DATE('2025-05-08'),
        DATE('2025-05-09')
    ),
    "Asia/Tokyo"
)
```

Результат: `3.06:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `WORKDAYSDURATIONUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два аргумента: начальные и конечные дату и время.

Переводит даты и время в часовой пояс `UTC+00:00` и возвращает длительность между ними за вычетом выходных дней.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
WORKDAYSDURATIONUTC(
    DATE('2025-05-01+03:00'), DATE('2025-05-12+00:00')
)
```

Результат: `9`

``` sql
WORKDAYSDURATIONUTC(
    DATE('2025-05-01-12:00'), DATE('2025-05-12+00:00')
)
```

Результат: `8`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `WORKDAYSTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает три аргумента: дату, количество рабочих дней, список исключаемых дат и часовой пояс.

Прибавляет к исходной дате количество рабочих дней с учётом выходных дней, списка исключений и часового пояса и возвращает результирующую дату.

Если в списке исключений указан рабочий день, он считается выходным, а если если указан выходной день, он считается рабочим.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
WORKDAYSTZ(
    startDay, workingDays,
    LIST(excludedDate1, …, excludedDateN),
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
- `workingDays`: число, количество рабочих дней.
- `LIST(excludedDate1, …, excludedDateN)`: (необязательный аргумент): список исключаемых дат.
- `timeZone`: строка, задающая часовой пояс в формате IANA.

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

``` sql
WORKDAYSTZ(
    DATE('2025-05-01+03:00'), 10, 
    LIST(
        DATE('2025-05-01'), 
        DATE('2025-05-02'), 
        DATE('2025-05-08'), 
        DATE('2025-05-09')
    ),
    "America/Anchorage"
)
```

Результат: `20.05.2025 0:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `WORKDAYSUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает два аргумента: дату и количество рабочих дней.

Приводит дату к часовому поясу `UTC+00:00`, прибавляет количество рабочих дней за вычетом выходных дней и возвращает результирующую дату.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
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

``` sql
WORKDAYSUTC(DATE('2025-05-01+03:00'), 3)
```

Результат: `06.05.2025 0:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `WORKHOURS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает пять аргументов: дату начала работы, количество рабочих часов, отведённых на работу, время начала рабочего дня, продолжительность рабочего дня и список исключаемых дат.

Прибавляет к начальной дате количество рабочих часов с учётом времени начала и продолжительности рабочего дня, выходных дней и списка исключений и возвращает дату и время завершения работы.

Если в списке исключений указан рабочий день, он считается выходным, а если если указан выходной день, он считается рабочим.

Если рабочий часовой пояс  отличается от часового пояса сервера **{{ productName }}**, используйте функцию [`WORKHOURSTZ()`](#workhourstz).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
WORKHOURS(
    startDateTime, workingHours, 
    workingDayStart, workingDayDuration,
    LIST(excludedDate1, ..., excludedDateN)
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
- `workingHours`: число, количество рабочих часов.
- `workingDayStart`: длительность, время начала рабочего дня от 00:00.
- `workingDayDuration`: длительность рабочего дня (должна быть меньше разницы между полуночью и временем начала рабочего дня).
- `LIST(excludedDate1, ..., excludedDateN)`: (необязательный аргумент): список исключаемых дат.

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

``` sql
WORKHOURS(
    DATE('2025-05-01'), 5,
    DURATION('PT9H'), DURATION('PT4H'),
    LIST(
        DATE('2025-05-01'),
        DATE('2025-05-02'),
        DATE('2025-05-08'),
        DATE('2025-05-09')
    )
)
```

Результат: `06.05.2025 10:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `WORKHOURSDURATION()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает пять аргументов: начальные дату и время, конечные дату и время, время начала рабочего дня, продолжительность рабочего дня и список исключаемых дат.

Возвращает длительность рабочего времени между начальной и конечной датами с учётом времени начала и продолжительности рабочего дня, выходных дней и списка исключений.

Если в списке исключений указан рабочий день, он считается выходным, а если если указан выходной день, он считается рабочим.

Если рабочий часовой пояс  отличается от часового пояса сервера **{{ companyName }}**, используйте функцию [`WORKHOURSDURATIONTZ()`](#workhoursdurationtz).

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
WORKHOURSDURATION(
    startDateTime, endDateTime, 
    workingDayStart, workingDayDuration,
    LIST(excludedDate1, ..., excludedDateN)
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
- `workingDayStart`: длительность, время начала рабочего дня от 00:00.
- `workingDayEnd`: длительность рабочего дня (должна быть меньше разницы между полуночью и временем начала рабочего дня).
- `LIST(excludedDate1, ..., excludedDateN)` (необязательный аргумент): список исключаемых дат.

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

``` sql
WORKHOURSDURATION(
    DATE('2025-05-01'), DATE('2025-05-07'), 
    DURATION('PT8H'), DURATION('PT15H'),
    LIST(
        DATE('2025-05-01'), 
        DATE('2025-05-02'), 
        DATE('2025-05-08'), 
        DATE('2025-05-09')
    )
)
```

Результат: `22:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `WORKHOURSDURATIONTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает шесть аргументов: начальные дату и время, конечные дату и время, время начала рабочего дня, продолжительность рабочего дня, список исключаемых дат и часовой пояс.

Возвращает длительность рабочего времени между начальной и конечной датами с учётом времени начала и продолжительности рабочего дня, выходных дней, списка исключений и часового пояса.

Если в списке исключений указан рабочий день, он считается выходным, а если если указан выходной день, он считается рабочим.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
WORKHOURSDURATIONTZ(
    startDateTime, endDateTime, 
    workingDayStart, workingDayDuration,
    LIST(holiday1, ..., holidayN),
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
- `workingDayStart`: длительность, время начала рабочего дня.
- `workingDayDuration`: длительность рабочего дня (должна быть меньше разницы между полуночью и временем начала рабочего дня).
- `LIST(holiday1, ..., holidayN)` (необязательный аргумент): список исключаемых дат.
- `timeZone`: строка, задающая часовой пояс в формате IANA.

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

``` sql
WORKHOURSDURATIONTZ(
    DATE('2025-05-01'), DATE('2025-05-07'),
    DURATION('PT8H'), DURATION('PT15H'),
    LIST(
        DATE('2025-05-01'), 
        DATE('2025-05-02'), 
        DATE('2025-05-08'),
        DATE ('2025-05-09')
    ),
    "Asia/Tokyo"
)
```

Результат: `1.04:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `WORKHOURSTZ()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает пять аргументов: дату начала работы, количество часов, отведённых на работу, время начала рабочего дня, продолжительность рабочего дня, список исключаемых дат и часовой пояс.

Прибавляет к начальной дате количество рабочих часов с учётом времени начала и продолжительности рабочего дня, выходных дней, списка исключений и часового пояса и возвращает дату и время завершения работы.

Если в списке исключений указан рабочий день, он считается выходным, а если если указан выходной день, он считается рабочим.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
WORKHOURSTZ(
    startDateTime, workingHours, 
    workingDayStart, workingDayDuration,
    LIST(excludedDate1, ..., excludedDateN),
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
- `workingHours`: число, количество рабочих часов.
- `workingDayStart`: длительность, время начала рабочего дня от 00:00.
- `workingDayDuration`: длительность рабочего дня (должна быть меньше разницы между полуночью и временем начала рабочего дня),
- `LIST(excludedDate1, ..., excludedDateN)` (необязательный аргумент):  список исключаемых дат.
- `timeZone`: строка, задающая часовой пояс в формате IANA.

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

``` sql
WORKHOURSTZ(
    DATE('2025-05-01'), 5, 
    DURATION('PT9H'), DURATION('PT4H'), 
    LIST(
        DATE('2025-05-01'), 
        DATE('2025-05-02'), 
        DATE('2025-05-08'), 
        DATE('2025-05-09')
    ),
    "America/Anchorage"
)
```

Результат: `05.05.2025 10:00:00`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `YEAR()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и строку с часовым поясом в формате IANA.

Приводит аргумент к заданному часовому поясу и возвращает год результирующей даты.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
YEAR(dateTime, timeZone)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `dateTime`: дата и время.
- `timeZone`: строка, задающая часовой пояс в формате IANA (необязательный аргумент).

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

``` sql
YEAR(DATE('2025-01-01'), "America/Anchorage")
```

Результат: `2024`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `YEARS()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Преобразует аргумента типа «**Длительность**» в количество лет.

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

``` sql
YEARS(DURATION('P183D'))
```

Результат: `0,5`

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

### `YEARUTC()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" class="functionDescriptionColumn">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**», переводит его в часовой пояс `UTC+00:00` и возвращает год результирующей даты.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` sql
YEARUTC(dateTime)
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

``` sql
YEARUTC(DATE('2025-01-01+03:00'))
```

Результат: `2024`

</td>
</tr>
</tbody>
</table>

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Редактор выражений][expression_editor]
- [Введение в язык формул Comindware][formula_guide]
- [Форматирование значений в шаблонах экспорта и формулах][export_template_file_formula_format_values]
- [Глобальная конфигурация][global_configuration]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
