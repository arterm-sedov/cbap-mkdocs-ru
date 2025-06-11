---
title: Написание выражений на языке N3
kbId: 4852
---

# Написание выражений на языке N3 {: #n3_guide }

## Введение

**{{ productName }}** позволяет составлять выражения на языке N3 (Notation3) для выполнения запросов данных и вычисления значений.

Преимущество языка N3 заключается в скорости вычислений, что позволяет эффективно использовать все возможности графовой базы данных. Язык выражений N3 позволяет осуществлять доступ к искомым данным и их связям поатрибутивно без необходимости загрузки данных потаблично, что присуще реляционным базам данных и языку запросов SQL.

Нотация N3 представляет собой набор записей типа: «субъект» «предикат» «объект». Данная конструкция может применяться в различных вариантах, от получения данных по заданным атрибутам, до математических операций.

## Синтаксис N3

Выражения N3 состоят из триплетов вида субъект-предикат-объект.

Например, `?group rdf:type account:Group` — триплет, позволяющий по любому из заданных аргументов обнаружить неизвестные. Если в триплете заданы объект и предикат, ПО будет осуществлять поиск субъекта, если заданы субъект и предикат — поиск объекта и т. д. Если в выражении задан один аргумент, ПО вернёт все значения для остальных двух.

Основы построения языка выражений N3 приведены в открытой документации, размещенной по адресу <https://www.w3.org/TR/rdf11-concepts/>.

Синтаксические элементы

- `@prefix property: <http://comindware.com/ontology/user/op#>.` — объявление префикса встроенного пакета, т.е. синонима, используемого в выражении..
- `rdf:type` — использование префикса для удобочитаемости и сокращения размеров кода.
- `{}` — объявление тела выражения.
- `?` — объявление переменных.
- `?item`  — входной параметр.
- `?item` — значения ссылки (экземпляры шаблона записи, с которым связан текущий шаблон записи).
- `?value` — выходной параметр.
- `a` — принадлежность субъекта к объекту.
- `.` — терминатор триплета.
- `#` — комментарий.
- `->` — присваивание значения.
- `()` — объявление списка.
- `[]` — неявное использование субъекта.

Полезные конструкции и встроенные функции

- `("templateSystemName" "attributeSystemName") object:findProperty ?p.` — возвращает в переменную `?p` атрибут по заданным системным именам шаблона и атрибута.
- `once {}.` — выходит после первой успешной итерации.
- `or {} or {} … or {}.` — логический оператор `ИЛИ`.
- `if {} then {} else {}.` — условный оператор.
- `from {} select ?v -> ?vList.` — возвращает список в переменную `?vList`.
- `?list math:sum ?sum.` — вычисляет сумму.
- `{} assert:count ?c.` — вычисляет количество записей.
- `({} … {}) assert:union true.` — объединяет итераторы в один.

## Запросы N3

- Запросы пишутся в виде набора триплетов.
- У запроса есть входные (в некоторых случаях) и выходные данные.
- Запрос выполняется последовательно сверху вниз по каждому триплету.
- Если запрос ничего не вернул, то это считается пустым результатом.
- Ризонёр (Reasoner) — специальный механизм, выполняющий запросы.

``` turtle
in ?item.
{
#наш код
} => { ?item attribute:value ?value. }.
```

### Пять видов запросов

| `субъект`         | `предикат`   | объект не указан | Поиск объекта по заданному предикату и субъекту. |
| ----------------- | ------------ | ---------------- | ------ |
| субъект не указан | `предикат`   | `объект`         | Поиск субъекта по заданному предикату и объекту.             |
| `субъект`         | `предикат`   | `объект`         | Проверка субъекта и объекта на полное совпадение.            |
| субъект не указан | `предикат`   | объект не указан | Поиск субъекта и объекта по заданному предикату.             |
| *`субъект`*       | *`предикат`* | *`?.`*           | Проверка наличия значения. Здесь *`?.`*— обозначение функции проверки наличия непустого значения (факта) по субъекту и предикату. |

 
### Порядок обработки запросов

_![Рисунок 1. Порядок обработки запроса для поиска ID аккаунта по имени пользователя](https://kb.comindware.ru/assets/img_64d245cbdcd08.png)_

_![Рисунок 2. Порядок обработки запроса для поиска ID задач по имени пользователя](https://kb.comindware.ru/assets/img_64d245f3c243e.png)_

## Возможности использования выражений N3

ПО позволяет использовать выражения N3 при настройке следующих сущностей и функций:

- Атрибут → Вычисление значения
- Форма → Фильтр на поле
- Правила для формы → Условие применения правила
- Правила для формы → Условие выполнения действия
- Правила для формы → Вычисление значения для действия
- Кнопка → Условие отображения
- Таблица → Системный фильтр
- Роль → Разрешения → Шаблон записи, аккаунта, процесса → Фильтр аккаунтов (Переназначение)
- Роль → Разрешения → Шаблон записи, аккаунта, процесса → Условие применения
- Сценарий → Изменение значений переменных → Вычисление значения
- Сценарий → Изменение значений атрибутов → Вычисление значения
- Сценарий → Смена контекста → Вычисление набора объектов
- Сценарий → Дублирование записи → Вычисление набора объектов
- Сценарий → Проверка результата выражения → Выражение для проверки
- Сценарий → Выполнение по условиям → Условие выполнения действий
- Сценарий → Повтор по числовому счётчику → Количество итераций
- Сценарий → Повтор по количеству объектов → Вычисление набора объектов

## Входные и выходные данные выражений в зависимости от контекста

| **Сущность** | **Входные данные (контекст)** | **Выходные данные** |
| --- | --- | --- |
| Атрибут → Вычисляемое значение | `?item` — текущая запись или экземпляр процесса | `?value` — вычисленное значение атрибута |
| Форма → Фильтр на поле | `?item` — текущая запись или экземпляр процесса | `?value` — список искомых записей |
| Правила для формы → Правило → Условие выполнения | `?item` — текущая запись или экземпляр процесса | `?value` — `true` (правило сработает) или `false` или пусто (не сработает) |
| Правила для формы → Действие  → Условие выполнения | `?item` — текущая запись или экземпляр процесса | `?value` — `true` (действие сработает) или `false` или пусто (не сработает) |
| Правила для формы → Вычисляемое значение для действия | `?item` — текущая запись или экземпляр процесса | `?value` — целевое значение атрибута |
| Кнопка → Условия отображения | `?item` — текущая запись или экземпляр процесса | `?value` — `true` или false |
| Таблица → Системный фильтр |  | `?value` — список записей для вывода в таблице |
| Роль → Разрешения → Шаблон записи, аккаунта, процесса → Фильтр аккаунтов | `?item` — текущая запись или экземпляр процесса | `?value` — список групп или аккаунтов, которые имеют соответствующие разрешения на запись или экземпляр процесса |
| Роль → Разрешения → Шаблон записи, аккаунта, процесса → Условие применения | `?item` — текущая запись или экземпляр процесса | `?value` — `true` или `false` |
| Сценарий → Изменение значений переменных → Вычисление значения | `?item` — текущая запись или экземпляр процесса | `?value` — вычисленное значение переменной |
| Сценарий → Изменение значений атрибутов → Вычисление значения | `?item` — текущая запись или экземпляр процесса | `?value` — вычисленное значение атрибута |
| Сценарий → Смена контекста → Вычисление набора объектов | `?item` — текущая запись или экземпляр процесса | `?value` — список объектов для перехода |
| Сценарий → Дублирование записи → Вычисление набора объектов | `?item` — текущая запись или экземпляр процесса | `?value` — список объектов для дублирования |
| Сценарий → Проверка результата выражения → Выражение для проверки | `?item` — текущая запись или экземпляр процесса | `?value` — `true` (проверка пройдена) или `false` |
| Сценарий → Выполнение по условиям → Условие выполнения действий | `?item` — текущая запись или экземпляр процесса | `?value` — `true` (выполнять действия) или `false` |
| Сценарий → Повтор по числовому счётчику → Количество итераций | `?item` — текущая запись или экземпляр процесса | `?value` — количество итераций |
| Сценарий → Повтор по количеству объектов → Вычисление набора объектов | `?item` — текущая запись или экземпляр процесса | `?value` — список объектов |

## Примеры использования встроенных функций и операторов N3

**Функция .?**

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
("currentTemplate" "Region") object:findProperty ?Region.
# Проверяем, что в текущей записи, атрибут Region содержит непустое значение
?item ?Region ?.
?item -> ?value.
}
```

**Функция once**

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
("currentTemplate" "Region") object:findProperty ?Region.
("Biznesstruktura" "Region") object:findProperty ?Region2.

once {
?item ?Region ?RegionVal.
?check ?Region2 ?RegionVal.
}.
true -> ?value.
}
```

**Оператор if**

``` turtle
@prefix cmw: <http://comindware.com/logics#>.
@prefix session: <http://comindware.com/ontology/session#>.
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
{
session:context session:requestTime ?now. #получим текущую дату
?tasks a cmw:UserTask.
if {?tasks cmw:dueDate ?.}
then {
?tasks cmw:dueDate ?dueDateVal.
?dueDateVal math:greaterThan ?now.
?tasks -> ?value.
}
else {?tasks -> ?value.}.
}

```

**Оператор from и функция sum**

``` turtle
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
@prefix object: <http://comindware.com/ontology/object#>.
{
("Nakladnaya" "PoziciiNakladnoy") object:findProperty ?Positions.
("PoziciiNakladnoy" "Summa") object:findProperty ?Summa.

from  {
  ?item ?Positions ?PositionsVal.
  ?PositionsVal ?Summa ?SummaVal.
} select ?SummaVal -> ?SummaList.

?SummaList math:sum ?value.
}
```

**Функция count**

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix assert: <http://comindware.com/logics/assert#>.
{
("Nakladnaya" "PoziciiNakladnoy") object:findProperty ?Positions.

{
?item ?Positions ?PositionsVal.
} assert:count ?value.
}
```

**Функция distinct**

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix assert: <http://comindware.com/logics/assert#>.
{
("Nakladnaya" "PoziciiNakladnoy") object:findProperty ?Positions.
("PoziciiNakladnoy" "Nomenklatura") object:findProperty ?Items.
{
{
?item ?Positions ?PositionsVal.
?PositionsVal ?Items ?ItemsVal.
} assert:distinct ?ItemsVal.
} assert:count ?value.
}
```

**Оператор union**

``` turtle
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix object: <http://comindware.com/ontology/object#>.
{
("Nakladnaya" "Gruzootpravitel") object:findProperty ?ShippedBy.
("Nakladnaya" "Poluchatel") object:findProperty ?Receiver.

(
{?item ?ShippedBy ?Contractor.}
{?item ?Receiver ?Contractor.}
) assert:union true.
?Contractor -> ?value.
}
```

## Примеры использования расширений Comindware для языка N3

**Задача**: вывести заявки, у которых значение атрибута Status не равно «Завершен» и дата начала уже прошла относительно текущей даты.

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix session: <http://comindware.com/ontology/session#>.
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
{
("Proekt" "Status") object:findProperty ?StatusProp.
?Proekty ?StatusProp ?Status.
("Proekt" "Datanachala") object:findProperty ?DatanachalaProp.
?Proekty ?DatanachalaProp ?Datanachala.
session:context session:requestTime ?now.
?now math:greaterThan ?Datanachala.
?Status != "Завершен".
?value == ?Proekty.
}
```

**Задача**: при добавлении существующих записей в коллекцию отображать в списке только те проекты, у которых прошла проверка (атрибут Proverka имеет значение `true`) или у которых атрибут Status имеет значение «Создан».

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
("Proekt" "Status") object:findProperty ?StatusProp.
?Proekty ?StatusProp ?Status.
("Proekt" "Proverka") object:findProperty ?ProverkaProp.
?Proekty ?ProverkaProp ?Proverka.
or {
?Proverka == true.
}
or {
?Status == "Создан".
}.
?value == ?Proekty.
}
```

**Задача**: выводить в списке на добавление только руководителей текущего пользователя (атрибут manager типа «Аккаунт») или пользователей с должностью «Менеджер» (атрибут title типа «Текст»)

``` turtle
@prefix cmw: <http://comindware.com/logics#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
{
cmw:securityContext cmw:currentUser ?currUser.
?users a account:Account.
or {
?currUser account:manager ?users. #users - руководители
}
or {
?users account:title ?title.
?title string:matches "Менеджер".
}.
?value == ?users.
}
```

**Задача:** выводить только тех заявителей, которые прикреплены к заявкам.

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
("Zayavitel" "Application") object:findProperty ?ApplicationProp.
?Zayavitel ?ApplicationProp ? .
}
```

**Задача:** выполнять действия с полем на форме при условии, что процент выполнения заявки больше 70, при этом действие не должно выполняться, если этап (атрибут Etap) выполнения равен 1.

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
{
  ("Application" "Etap") object:findProperty ?EtapProp.
  ?item ?EtapProp ?Etap.
  ("Application" "percent") object:findProperty ?percentProp.
  ?item ?percentProp ?percent.
  or {
    ?Etap == 1.
    ?value == false.
  }
  or {
    ?percent math:greaterThan 70.
    ?value == true.
  }.
}
```

**Задача:** при выполнении вышеописанного условия, выполнять для поля «Статус» заявки следующие действия: сменить тип доступа на «Только для чтения», установить значение «Завершена» и показать предупреждение с текстом «Заявка <Название заявки (атрибут Name)> завершена».

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix output: <http://comindware.com/ontology/tableOutput#>.
{
output:result a output:Result.
("Application" "Etap") object:findProperty ?EtapProp.
?item ?EtapProp ?Etap.
("Application" "percent") object:findProperty ?percentProp.
?item ?percentProp ?percent.
?Etap != 1.
?percent math:greaterThan 70.
output:result output:typeOfAccess "Только чтения".
output:result output:value "Завершена".
("Application" "Name") object:findProperty ?NameProp.
?item ?NameProp ?Name.
("Заявка" ?Name "завершена") string:format ?warning.
output:result output:warning "Завершена".
}
```

## Упрощения

Ниже представлены некоторые упрощения N3, упрощающие и ускоряющие работу.

| `@prefix: <#>.`       | `:John` — субъект определён в текущем документе                                          |
| --------------------- | ---------------------------------------------------------------------------------------- |
| `a/ @a`               | `Rdf:type`          |
| `[]`                  | указываем, что существует объект с заданными свойствам без возможности ссылаться на него |
| `=`                   | эквивалентность (`owl:equivalentTo`)                                                     |
| `=>`                  | `Log:implies`       |
| `объект.свойство`     | переход к свойству  |
| `(элемент1 элемент2)` | список              |
| `_:variable`          | `log:forSome`       |
| `?variable`           | `log:forAll`        |

## Справочник встроенных функций N3

В следующей таблице приведен перечень функций, которые можно использовать в выражениях N3.

!!! question "Определения"

    - ***QName*** — qualified name (квалифицированное имя) идентификатор для элементов и атрибутов. QName используется для создания соответствия между URI и пространством имен.
    - ***Escape-последовательности*** — сочетание символов, состоящих из косой черты (`\`), за которой следует буква или набор цифр. Escape-последовательность рассматривается как один символ и, следовательно, является допустимой символьной константой.
    - ***StreamID*** — идентификатор файла изображения, расположенного в базе данных ПО.

### Математические функции `w3math`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix w3math: <http://www.w3.org/2000/10/swap/math#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`w3math:quotient`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт 2 аргумента в скобках, указанные в субъекте и результат деления первого на второе помещает в переменную объекта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?WorkInSeconds ?WorkDaysInSeconds) w3math:quotient ?WorkSeconds.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3math:integerQuotient`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт 2 аргумента в скобках, указанные в субъекте и результат целочисленного деления первого на второе помещает в переменную объекта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?WorkInSeconds ?WorkDaysInSeconds) w3math:integerQuotient ?WorkSeconds.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3math:remainder`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт 2 аргумента в скобках, указанные в субъекте и остаток от деления первого на второе помещает в переменную объекта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?remainingWorkInSeconds ?remainingWorkDaysInSeconds) math:remainder ?remainingWorkSeconds.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3math:product`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт 2 аргумента в скобках, указанные в субъекте и результат их умножения помещает в переменную объекта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?productingWorkInSeconds ?productingWorkDaysInSeconds) w3math:product ?productingWorkSeconds.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3math:lessThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Меньше чем</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?recordDate w3math:lessThan ?maxDate.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3math:notLessThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Не меньше чем</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?documentRecordsCount w3math:notLessThan 2.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3math:equalTo`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Равно (`dateTime` , `date` , `duration` , `string` , `number` ).</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?countWorkingDaysMounth w3math:equalTo ?countWorkingDays.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3math:notEqualTo`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Не равно (`dateTime` , `date` , `duration` , `string` , `number` ).</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?countWorkingDaysMounth w3math:notEqualTo ?countWorkingDays.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3math:greaterThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Больше чем (`dateTime` , `date` , `duration` , `string` , `number` ).</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?recordDate w3math:greaterThan ?minDate.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3math:notGreaterThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Не больше чем (`dateTime` , `date` , `duration` , `string` , `number` ).</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?documentRecordsCount w3math:notGreaterThan 2.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3math:negation`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Отрицание</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?firstNumber w3math:negation ?negationNumber.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
</tbody>
</table>

### Математические функции `cmwmath`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwmath: <http://comindware.com/logics/math#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwmath:sum`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт сумму из субъекта типа List и записывает значение в объект.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?durationsSeconds cmwmath:sum ?durationSumSeconds.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwmath:difference`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт разность из субъекта типа List и записывает значение в объект.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?list cmwmath:difference ?differenceTotal.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwmath:min`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт минимальное значение из субъекта типа List и записывает значение в объект.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?listQueue cmwmath:min ?queueMin.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number` `dateTime` `duration`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwmath:max`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт максимальное значение из субъекта типа List и записывает значение в объект.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?listQueue cmwmath:max ?queueMax.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number` `dateTime` `duration`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwmath:average`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт 2 аргумента в скобках, указанные в субъекте и помещает их среднее арифметическое в переменную объекта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?priceFirst ?priceSecond) cmwmath:average ?priceAverage.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwmath:round`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Округление к ближайшему целому.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?quotientPrice cmwmath:round ?numberRound.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwmath:floor`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Округление в меньшую сторону.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?quotientPrice cmwmath:floor ?numberFloor.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwmath:ceil`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Округление в большую сторону.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?quotientPrice cmwmath:ceil ?numberCeil.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
</tbody>
</table>

### Функции для работы с датами и временем `w3time`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix w3time: <http://www.w3.org/2000/10/swap/time#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`w3time:inSeconds`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Конвертирует значение типа `dateTime` или `duration` в количество секунд. Конвертирует количество секунд в значение типа `dateTime` от начала времен.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?durationWorkingDay w3time:inSeconds ?secondsWorkingDay.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
</tbody>
</table>

### Функции для работы с датами и временем `cmwtime`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwtime: <http://comindware.com/logics/time#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwtime:toDuration`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Конвертирует количество секунд в значение типа `duration`.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?secondsWorkingDay cmwtime:toDuration ?durationWorkingDay.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`duration`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:getSpan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Вычитает из первого значения субъекта типа `dateTime` второе значение субъекта типа `dateTime`.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?dateTime1 ?dateTime2) cmwtime:getSpan ?resultTimeSpan.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`duration`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:addDuration`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Добавляет к значению субъекта типа `dateTime` значение типа `duration`.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?dateTime ?duration) cmwtime:addDuration ?value.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:subDuration`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Вычитает из значения субъекта типа `dateTime` значение типа `duration`.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?dateTime ?duration) cmwtime:subDuration ?value.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:endOfDay`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания дня, в пределах которого находится значение субъекта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwtime:endOfDay ?endDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:startOfDay`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала дня, в пределах которого находится значение субъекта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwtime:startOfDay ?startDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:startOfWeek`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала недели, в пределах которой находится значение субъекта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwtime:startOfWeek ?startDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:startOfMonth`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала месяца, в пределах которого находится значение субъекта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwtime:startOfMonth ?startDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:fromTzToTz`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Перевод значения типа `dateTime` в заданный часовой пояс.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?someDateTime "Etc/GMT" "Europe/Moscow") cmwtime:fromTzToTz ?tzDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:timeZoneHours`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает разницу во времени UTC и местным часовым поясом.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`? cmwtime:timeZoneHours ?timeZoneDifferenceInHours.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`integer`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:isToday`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и проверяет на текущую дату.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate cmwtime:isToday ?today.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:century`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее веку указанной даты в местном часовом поясе.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate cmwtime:century ?numberCentury.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:isoFormat`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Конвертирует значение типа `dateTime` в формат ISO.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate cmwtime:isoFormat ?isoFormatDate.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:year`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее году указанной даты в местном часовом поясе.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate cmwtime:year ?numberYear.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:month`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее месяцу указанной даты в местном часовом поясе.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate cmwtime:month ?numberMonth.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:day`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее дню месяца указанной даты в местном часовом поясе.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate cmwtime:day ?numberDay.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:hour`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее часу указанной даты в местном часовом поясе.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate cmwtime:hour ?numberHour.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:minute`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее минуте указанной даты в местном часовом поясе.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate cmwtime:minute ?numberMinute.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:second`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее секундам указанной даты в местном часовом поясе.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate cmwtime:second ?numberSecond.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:makeDate`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значения субъекта типа число и возвращает объект типа `dateTime`.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?intervalBeginYear ?intervalBeginMonth ?intervalBeginDay 23 59 59) cmwtime:makeDate ?brokenIntervalEnd.` `(?intervalEndYear ?intervalEndMonth ?intervalEndDay 0 0 0) cmwtime:makeDate ?brokenIntervalBegin.` `(?startDateYear ?startDateMonth ?startDateDay) cmwtime:makeDate ?startDayDate.` `(?startDateYear ?startDateMonth ?startDateDay ?startDateHour ?startDateMinute ?startDateSecond) cmwtime:makeDate ?intervalBegin.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:workhours`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает дату и время на основании количества рабочих часов с определенного момента времени, с поправкой на праздники и фактические выходные дни.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?startWorkDateTime ?qountWorkingHours ?startWorkingDay ?durationWorkingDay (?dateNotHoliday)) cmwtime:workhours ?newDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:workdays`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает дату на основании количества рабочих дней с определенной даты, с поправкой на праздники и фактические выходные дни.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?startWorkDateTime ?qountWorkingHours (?firstDateNotHoliday ?secondDateNotWorking)) cmwtime:workdays ?newDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:workhoursDuration`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает продолжительность работы между двумя датами при условии, что рабочий день начинается в заданное время и имеет определенную длительность.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?startWorkDateTime ?endWorkDateTime ?timeStartWorkingDay ?durationWorkingDay) cmwtime:workhoursDuration ?newDuration.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`duration`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwtime:workdaysDuration`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает продолжительность работы между двумя датами, на основании предположения, что рабочий день начинается в 00:00 и длится 24 часа.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?startWorkDateTime ?endWorkDateTime) cmwtime:workdaysDuration ?newDuration.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`duration`</td>
</tr>
</tbody>
</table>

### Функции для работы с интервалами времени `cmwduration`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwduration: <http://comindware.com/logics/duration#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwduration:days`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт промежуток времени и возвращает количество дней.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?durationHoliday cmwduration:days ?countDaysOfHoliday.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwduration:hours`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт промежуток времени и возвращает количество часов.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?durationHoliday cmwduration:hours ?countHoursOfHoliday.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwduration:minutes`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт промежуток времени и возвращает количество минут.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?durationHoliday cmwduration:minutes ?countMinutesOfHoliday.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
</tbody>
</table>

### Функции для работы со строками `w3string`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix w3string: <http://www.w3.org/2000/10/swap/string#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`w3string:format`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Подставляет аргументы в нумерованные заместители вида `{0}`…`{n}` в исходной строке и возвращает результирующую строку.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`("{0}/{1} - {2}" ?value0 ?value1 ?value2) w3string:format ?outString.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3string:matches`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Использует в качестве аргументов строку и регулярное выражение. Возвращает логическое значение Истина, если какая-либо часть строки или строка полностью соответствует условию, заданному регулярным выражением. В противном случае возвращает результат Ложь.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?stringExample w3string:matches ?expression.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3string:notMatches`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Использует в качестве аргументов строку и регулярное выражение. Возвращает логическое значение Истина, если часть строки или строка полностью не соответствуют условию, заданному регулярным выражением. В противном случае возвращает результат Ложь.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?stringExample w3string:notMatches ?expression.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3string:greaterThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает логическое значение Истина, если аргумент2 больше аргумента1, в противном случае возвращает результат Ложь.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate w3string:greaterThan ?chooseDate.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3string:lessThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает логическое значение Истина, если аргумент2 меньше аргумента1, в противном случае возвращает результат Ложь.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate w3string:lessThan ?chooseDate.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3string:notGreaterThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает логическое значение Истина, если аргумент2 НЕ больше аргумента1, в противном случае возвращает результат Ложь.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate w3string:notGreaterThan ?chooseDate.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3string:notLessThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает логическое значение Истина, если аргумент2 НЕ меньше аргумента1, в противном случае возвращает результат Ложь.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDate w3string:notLessThan ?chooseDate.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
</tbody>
</table>

### Функции для работы со строками `cmwstring`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwstring: <http://comindware.com/logics/string#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwstring:join`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Объединяет строки с использованием заданного разделителя.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`("," ?newDependencyLinks) cmwstring:join ?newDependencyLinksStr.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:replace`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Заменяет все экземпляры заданной строки в исходной строке на новое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?text "\n" "<br>") cmwstring:replace ?html.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:cutString`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Обрезает строку на заданную длину и добавляет в конец заданные символы.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?taskTitleLong 50 "...") cmwstring:cutString ?taskTitle.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:firstCapital`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Преобразует первый символ строки в прописной.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?youStr cmwstring:firstCapital ?youStrCapital.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:concatenation`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Конкатенация строк.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?firstString ?secondString) cmwstring:concatenation ?newString.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:length`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает количество символов в строке.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?stringName cmwstring:length ?countSymbols.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:substring`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Обрезает строку от заданной позиции на заданное количество символов (опционально).</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?sourceString 2 4) cmwstring:substring ?resultString.` `(?sourceString 2) cmwstring:substring ?resultString.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:indexOf`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает номер (отсчитываемый от нуля) позиции, на которой располагается искомая строка в исходной строке. Номер позиции может отсчитываться от произвольного положения (опционально).</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?sourceString ?subString) cmwstring:indexOf ?resultString.` `(?sourceString ?subString 4) cmwstring:indexOf ?resultString.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:toUri`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Преобразует escape-последовательности в URI.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?sequence cmwstring:toUri ?reference.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:fromUri`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Преобразует URI в escape-последовательности.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?reference cmwstring:fromUri ?sequence.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:toBase64`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Преобразует строку по стандарту кодирования Base64.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?string cmwstring:toBase64 ?newStringBase.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:fromBase64`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Декодирует строку по стандарту Base64.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?stringBase cmwstring:fromBase64 ?newString.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:split`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Находит заданный разделитель в строке и создает список.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`("_" ?string) cmwstring:split ?newString.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown></td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwstring:format`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Форматирует аргументы в соответствии с заданным шаблоном. Возвращает отформатированную строку.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`("{0}/{1} - {2}" ?v0 ?v1 ?v2) cmwstring:format ?outString.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
</tbody>
</table>

### Функции для работы со строками `cmwlogics`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwlogics: <http://comindware.com/logics#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwlogics:value`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Присваивает значение субъекта объекту.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?left cmwlogics:value ?right.` `{time:now => ?left.` `?left cmwlogics:value ?right` `Result: ?right = dateTime.UtcNow.}`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number` `dateTime` `string` `duration` `reference` `account`</td>
</tr>
</tbody>
</table>

### Функции для работы со строками `cmwentity`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwentity: <http://comindware.com/ontology/entity#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwentity:like`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Сравнивает шаблон и строку.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?pattern cmwentity:like ?sourceString.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwentity:startsWith`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Проверяет, что заданная строка начинается в соответствии с шаблоном и (опционально) в соответствии с заданной опцией сравнения (StringComparison).</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?sourceString entity:startsWith ?pattern.` `(?sourceString “OrdinalIgnoreCase”) entity:startsWith ?pattern.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwentity:endsWith`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Проверяет, что заданная строка заканчивается в соответствии с шаблоном и (опционально) в соответствии с заданной опцией сравнения (StringComparison).</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?sourceString entity:endsWith ?pattern.` `(?sourceString “OrdinalIgnoreCase”) entity:endsWith ?pattern.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwentity:indexOf`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает индекс первого вхождения подстроки в строку. Отсчет начинается с 1.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?sourceString ?substring) entity:indexOf ?index.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwentity:toLower`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Преобразует все символы строки в строчные.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?string entity:toLower ?stringLow.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwentity:toUpper`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Преобразует все символы строки в прописные.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?string entity:toUpper ?stringUpper.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwentity:contains`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Проверяет вхождение значения объекта типа `string` в значение субъекта типа `string`.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?string entity:contains ?subString.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
</tbody>
</table>

### Функции для работы со строками `cmwbuiltin`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwbuiltin: <http://comindware.com/ontology/image/builtin#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwbuiltin:toPlainText`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Конвертирует HTML-текст в обычный.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?htmlText builtin:toPlainText ?plainText.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
</tbody>
</table>

### Функции для работы со списками `w3list`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix w3list: <http://www.w3.org/2000/10/swap/list#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`w3list:append`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Добавляет элементы к списку</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`((1 2) (3 4)) w3list:append (1 2 3 4)`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>Список</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3list:in`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Если объект — список, и в нём есть субъект, возвращает `true`</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?subjectToFind w3list:append ?list`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3list:last`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Из представленной последовательности получает последний элемент.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?listFlowers w3list:last ?lastFlower.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`w3list:member`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Если субъект — список, и в нём есть объект, возвращает `true`</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?list w3list:append ?objectToFind`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
</tbody>
</table>

### Функции для работы со списками `cmwlist`

<table markdown="block">
<thead markdown="block">
<th markdown colspan="2">`@prefix cmwlist: <http://comindware.com/logics/list#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwlist:length`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает количество элементов последовательности.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?listFlowers cmwlist:length ?countFlowers.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwlist:at`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт список элементов и задает индекс. Возвращает значение элемента, соответствующее индексу. `([23, 25, 12] 2)` возвращает `12`.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?list ?index) cmwlist:at ?valueOfIndex.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
</tbody>
</table>

### Функции группировки и сортировки списков `cmwentity`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwentity: <http://comindware.com/ontology/entity#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwentity:groupby`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Группировка</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?recordTemplate ?dataSet) entity:groupby ?attributeGroup`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown></td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwentity:sortby`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Сортировка</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?recordTemplate ?dataSet) entity:sortby ?attributeGroup` `(("key1_1" "key2_1" "value1_1") ("key1_2" "key2_2" "value1_2") ("key1_3" "key2_3" "value1_3"))` `//` `// right:` `// (("value1_2") ("value1_1") ("value1_3")) - sorted field-to-select data`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown></td>
</tr>
</tbody>
</table>

### Функции для работы с идентификаторами ресурсов `cmwurl`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwurl: <http://comindware.com/logics/url#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwurl:encode`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Кодирует строку URL-адреса. Аналог `System.Web.HttpUtility.UrlEncode(url)`</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?url cmwurl:encode ?encodedUrl.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwurl:combine`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Объединяет части предоставления списка строк пути в путь одной строкой. Аналог `System.IO.Path.Combine`</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?path1 ?path2 ?path3 ...) cmwurl:combine ?combinedPath.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwurl:siteDir`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Получает текущую директорию нахождения проекта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?unused cmwurl:siteDir ?siteDir.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
</tbody>
</table>

### Функции для работы с идентификаторами ресурсов `cmwui`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwui: <http://comindware.com/ontology/ui#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwui:toClientString`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Получает строковое представление ресурса (элемента или атрибута).</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?object cmwui:toClientString ?string.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwui:toQName`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Преобразует строковое представление ресурса в QName.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?object cmwui:toQName ?qName.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
</tbody>
</table>

### Функции поддерживающие и корректно обрабатывающие нулевые значения `cmwnullable`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwnullable <http://comindware.com/ontology/entity/nullable#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:lessThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Меньше чем. (`dateTime` , `date` , `duration` , `string` , `number` ) Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?recordDate cmwnullable:lessThan ?maxDate.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:greaterThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Больше чем (`dateTime` , `date` , `duration` , `string` , `number` ) Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?recordDate cmwnullable:greaterThan ?minDate.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:notLessThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Не меньше (`dateTime` , `date` , `duration` , `string` , `number` ) Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?documentRecordsCount cmwnullable:notLessThan 2.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:notGreaterThan`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Не больше (`dateTime` , `date` , `duration` , `string` , `number` ) Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?documentRecordsCount cmwnullable:notGreaterThan 2.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:quotient`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт 2 аргумента в скобках, указанные в субъекте и результат деления первого на второе помещает в переменную объекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?WorkInSeconds ?WorkDaysInSeconds) cmwnullable:quotient ?WorkSeconds.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:product`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт 2 аргумента в скобках, указанные в субъекте и результат их умножения помещает в переменную объекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?productingWorkInSeconds ?productingWorkDaysInSeconds) cmwnullable:product ?productingWorkSeconds.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:integerQuotient`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт 2 аргумента в скобках, указанные в субъекте и результат целочисленного деления первого на второе помещает в переменную объекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?WorkInSeconds ?WorkDaysInSeconds) cmwnullable:integerQuotient ?WorkSeconds.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:remainder`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт 2 аргумента в скобках, указанные в субъекте и остаток от деления первого на второе помещает в переменную объекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?remainingWorkInSeconds ?remainingWorkDaysInSeconds) cmwnullable:remainder ?remainingWorkSeconds.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:sum`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт сумму из субъекта типа `List` и записывает значение в объект. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?durationsSeconds cmwnullable:sum ?durationSumSeconds.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:difference`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт разность из субъекта типа `List` и записывает значение в объект. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?list cmwnullable:difference ?differenceTotal.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:startOfDay`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала дня, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwnullable:startOfDay ?startDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:startOfWeek`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала недели, в пределах которой находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwnullable:startOfWeek ?startDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:startOfMonth`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала месяца, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwnullable:startOfMonth ?startDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:startOfQuarter`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала квартала, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwnullable:startOfQuarter ?startDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:startOfYear`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала месяца, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwnullable:startOfYear ?startDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:endOfDay`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания дня, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwnullable:endOfDay ?endDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:endOfWeek`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания недели, в пределах которой находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwnullable:endOfWeek ?endDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:endOfMonth`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания месяца, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwnullable:endOfMonth ?endDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:endOfQuarter`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания квартала, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwnullable:endOfQuarter ?endDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:endOfYear`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания года, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?creationDateTime cmwnullable:endOfYear ?endDateTime.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:inSeconds`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Конвертирует значение длительности в количество секунд. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?durationWorkingDay cmwnullable:inSeconds ?secondsWorkingDay.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:min`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт минимальное значение из субъекта типа `List` и записывает значение в объект. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?listQueue cmwnullable:min ?queueMin.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`  `dateTime`  `date`  `duration`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:max`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт максимальное значение из субъекта типа `List` и записывает значение в объект. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?listQueue cmwnullable:max ?queueMax.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`  `dateTime`  `date`  `duration`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:average`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Берёт 2 аргумента в скобках, указанные в субъекте и помещает их среднее арифметическое в переменную объекта. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`(?priceFirst ?priceSecond) cmwnullable:average ?priceAverage.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:toDuration`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Конвертирует количество секунд в значение типа `duration`. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?secondsWorkingDay cmwnullable:toDuration ?durationWorkingDay.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`duration`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:round`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Округление к ближайшему целому. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?quotientPrice cmwnullable:round ?numberRound.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:floor`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Округление в меньшую сторону. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?quotientPrice cmwnullable:floor ?numberFloor.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:ceiling`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Округление в большую сторону. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?quotientPrice cmwnullable:ceiling ?numberCeil.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwnullable:format`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Форматирует аргументы в соответствии с заданным шаблоном. Возвращает отформатированную строку. Если в субъекте нулевое значение, возвращает нулевое значение.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`("{0}/{1} - {2}" ?v0 ?v1 ?v2) cmwnullable:format ?outString.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
</tbody>
</table>

### Функции для работы с изображениями `cmwbuiltin`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwbuiltin: <http://comindware.com/ontology/image/builtin#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwbuiltin:isSupportedImage`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Проверяет формат файла на соответствие одному из допустимых форматов: `.bmp, .gif, .exif, .jpg, .jpeg, .png, .tif`</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`“bllalblablab.jpg” => ?fileName.` `?fileName builtin:isSupportedImage ?right.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwbuiltin:dimensions`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>По `streamId` изображения получает разрешение в формате ширина × высота.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?streamId builtin:dimensions ?dimensions.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
</tbody>
</table>

### Специальные функции для работы с аккаунтами и группами `cmwlogics`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwlogics: <http://comindware.com/logics#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwlogics:currentUser`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат, получающий аккаунт текущего пользователя.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`cmwlogics:securityContext cmwlogics:currentUser ?userVal.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown></td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwlogics:securityContext`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Субъект, определяющий контекст персонального пространства.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`cmwlogics:securityContext cmwlogics:currentUser ?userVal.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown></td>
</tr>
</tbody>
</table>

### Специальные функции для работы с аккаунтами и группами `cmwaccount`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwaccount: <http://comindware.com/ontology/account#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:Group`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Определяет тип переменной Группа.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?group rdf:type cmwaccount:Group.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown></td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:groupName`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения наименования группы.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?group cmwaccount:groupName ?groupName.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:isSystemAdministrator`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для определения принадлежности аккаунта к системной роли «Системные администраторы»</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:isSystemAdministrator ?access.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:displayName`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат, для получения полного имени аккаунта</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:displayName ?userDisplayName.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:fullName`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения Ф. И. О. аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:fullName ?userNameSurname.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:manager`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения аккаунта руководителя, указанного для аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:manager ?userManager.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`accountProperty`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:mbox`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения адреса эл.&nbsp;почты аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:mbox ?userEmail.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:phone`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения номера телефона аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:phone ?userMobile.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:instantMessagingId`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения идентификатора аккаунта в мессенджере.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`account:instantMessagingId`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:status`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения статуса аккаунта: `true` — включён.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:status ? enabled`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:skype`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения идентификатора аккаунта в Skype.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:skype ?loginSkype.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:username`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения имени пользователя (логина) аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:username ?login.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:active`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения состояния аккаунта: `true` — включён.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:active ? enabled`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:lastLoginDate`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения даты последней авторизации аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:lastLoginDate ?lastLoginDate.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:language`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения кода языка отображения веб-сайта для аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:language ?userLanguage.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:sid`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения Active Directory Security ID аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user account:sid ?sid.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:notificationSettings`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения параметров уведомлений аккаунта</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user account:notificationSettings ?notificationConfig .`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`multiValue`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:password`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения пароля к аккаунту.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:password ?userPassword`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:userpic`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения изображения профиля аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:userpic ?picture ..`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:userpicLarge`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения увеличенного изображения профиля аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:userpicLarge ?picture.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:title`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения наименования должности аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:title  ?jobTitle.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:department`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения наименования отдела аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:department  ?departmentName.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:office`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения наименования офиса аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:office  ?officeName.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:userGroupMembership`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения списка групп, в которых состоит аккаунт.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:userGroupMembership  ?groupList.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`multiValue   groupProperty`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:authenticationMethod`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения способа аутентификации аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:authenticationMethod ?authMethod.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:substitute`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения аккаунта заместителя, назначенного аккаунту.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:substitute ?substituteAccount.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`accountProperty`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:substituteDateFrom`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения даты начала замещения аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:substituteDateFrom  ?subsitutionStart`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:substituteDateTo`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения даты окончания замещения аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:substituteDateTo  ?subsitutionEnd`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:birthday`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения дня рождения аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:birthday  ?birthday.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:personalCalendarId`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения ID персонального календаря аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:personalCalendarId  ?calendarID.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:personalCalendarUri`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения URI персонального календаря аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:personalCalendarUri  ?calendarURI.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:presentedOnOrgchart`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения статуса включения аккаунта в организационную структуру: `true` — включён.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:presentedOnOrgchart ?onOrgChart.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`bool`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwaccount:timeZone`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Предикат для получения серверного часового пояса аккаунта.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`?user cmwaccount:timeZone ?userTimeZone.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
</tbody>
</table>

### Специальные функции `cmwobject`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwobject: <http://comindware.com/ontology/object#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwobject:findProperty`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает в объект ID атрибута по заданной в субъекте паре системных имён шаблона записи и атрибута.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
`("templateClients" "attibuteClientCode") cmwobject:findProperty ?attibute.`
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`string`</td>
</tr>
</tbody>
</table>

### Специальные функции `cmwcontext`

<table markdown="block">
<thead markdown="block">
<tr markdown="block">
<th markdown colspan="2">`@prefix cmwcontext: <http://comindware.com/logics/session/context#>.`</th>
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<th markdown colspan="2">`cmwcontext:time`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает текущее время сеанса.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`dateTime`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwcontext:timeZoneOffset`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает смещение часового пояса сеанса.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown>`number`</td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwcontext:origin`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает объект, по которому был запущен сценарий.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown></td>
</tr>
<tr markdown="block">
<th markdown colspan="2">`cmwcontext:variable`</th>
</tr>
<tr markdown="block">
<td markdown>**Описание**</td>
<td markdown>Возвращает переменную в контексте.</td>
</tr>
<tr markdown="block">
<td markdown>**Синтаксис**</td>
<td markdown="block">
</td>
</tr>
<tr markdown="block">
<td markdown>**Возвращает**</td>
<td markdown></td>
</tr>
</tbody>
</table>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
