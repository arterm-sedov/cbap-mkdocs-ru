---
title: 'Написание выражений на языке N3'
kbId: 2401
url: 'https://kb.comindware.ru/article.php?id=2401'
updated: '2024-09-26 16:44:05'
---

# Написание выражений на языке N3

## Введение

Comindware Business Application позволяет составлять выражения на языке N3 (Notation3) для выполнения запросов данных и вычисления значений.

Преимущество языка N3 заключается в скорости вычислений, что позволяет эффективно использовать все возможности графовой базы данных. Язык выражений N3 позволяет осуществлять доступ к искомым данным и их связям поатрибутивно без необходимости загрузки данных потаблично, что присуще реляционным базам данных и языку запросов SQL.

Нотация N3 представляет собой набор записей типа: «субъект» «предикат» «объект». Данная конструкция может применяться в различных вариантах, от получения данных по заданным атрибутам, до математических операций.

## Синтаксис N3

Выражения N3 состоят из триплетов вида субъект-предикат-объект.

Например, `?group rdf:type account:Group` — триплет, позволяющий по любому из заданных аргументов обнаружить неизвестные. Если в триплете заданы объект и предикат, ПО будет осуществлять поиск субъекта, если заданы субъект и предикат — поиск объекта и т. д. Если в выражении задан один аргумент, ПО вернёт все значения для остальных двух.

Основы построения языка выражений N3 приведены в открытой документации, размещенной по адресу [*https://www.w3.org/TR/rdf11-concepts/*](https://www.w3.org/TR/rdf11-concepts/).

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
- Ризонер (Reasoner) — специальный механизм, выполняющий запросы.

```
in ?item.
{
#наш код
} => { ?item attribute:value ?value. }.
```

### Пять видов запросов

|  |  |  |  |
| --- | --- | --- | --- |
| `субъект` | `предикат` | объект не указан | Поиск объекта по заданному предикату и субъекту. |
| субъект не указан | `предикат` | `объект` | Поиск субъекта по заданному предикату и объекту. |
| `субъект` | `предикат` | `объект` | Проверка субъекта и объекта на полное совпадение. |
| субъект не указан | `предикат` | объект не указан | Поиск субъекта и объекта по заданному предикату. |
| *`субъект`* | *`предикат`* | *`?.`* | Проверка наличия значения. Здесь *`?.`*— обозначение функции проверки наличия непустого значения (факта) по субъекту и предикату. |

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

```
@prefix object: <http://comindware.com/ontology/object#>.
{
("currentTemplate" "Region") object:findProperty ?Region.
# Проверяем, что в текущей записи, атрибут Region содержит непустое значение
?item ?Region ?.
?item -> ?value.
}
```

**Функция once**

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
@prefix object: <http://comindware.com/ontology/object#>.
{
("Zayavitel" "Application") object:findProperty ?ApplicationProp.
?Zayavitel ?ApplicationProp ? .
}
```

**Задача:** выполнять действия с полем на форме при условии, что процент выполнения заявки больше 70, при этом действие не должно выполняться, если этап (атрибут Etap) выполнения равен 1.

```
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
```

**Задача:** при выполнении вышеописанного условия, выполнять для поля «Статус» заявки следующие действия: сменить тип доступа на «Только для чтения», установить значение «Завершена» и показать предупреждение с текстом «Заявка <Название заявки (атрибут Name)> завершена».

```
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

|  |  |
| --- | --- |
| `@prefix: <#>.` | `:John` — субъект определён в текущем документе |
| `a/ @a` | `Rdf:type` |
| `[]` | указываем, что существует объект с заданными свойствам без возможности ссылаться на него |
| `=` | эквивалентность (`owl:equivalentTo`) |
| `=>` | `Log:implies` |
| `объект.свойство` | переход к свойству |
| `(элемент1 элемент2)` | список |
| `_:variable` | `log:forSome` |
| `?variable` | `log:forAll` |

## Справочник встроенных функций N3

В следующей таблице приведен перечень функций, которые можно использовать в выражениях N3.

### Определения

- ***QName*** — qualified name (квалифицированное имя) идентификатор для элементов и атрибутов. QName используется для создания соответствия между URI и пространством имен.
- ***Escape-последовательности*** — сочетание символов, состоящих из косой черты (`\`), за которой следует буква или набор цифр. Escape-последовательность рассматривается как один символ и, следовательно, является допустимой символьной константой.
- ***StreamID*** — идентификатор файла изображения, расположенного в базе данных ПО.

| **Встроенные функции N3** | | | |
| --- | --- | --- | --- |
| **Функция** | **Описание** | **Использование** | **Возвра­щает** |
| Математические функции | | | |
| `@prefix w3math: <http://www.w3.org/2000/10/swap/math#>.` | | | |
| `w3math:quotient` | Берёт 2 аргумента в скобках, указанные в субъекте и результат деления первого на второе помещает в переменную объекта. | `(?WorkInSeconds ?WorkDaysInSeconds) w3math:quotient ?WorkSeconds.` | `number` |
| `w3math:integerQuotient` | Берёт 2 аргумента в скобках, указанные в субъекте и результат целочисленного деления первого на второе помещает в переменную объекта. | `(?WorkInSeconds ?WorkDaysInSeconds) w3math:integerQuotient ?WorkSeconds.` | `number` |
| `w3math:remainder` | Берёт 2 аргумента в скобках, указанные в субъекте и остаток от деления первого на второе помещает в переменную объекта. | `(?remainingWorkInSeconds ?remainingWorkDaysInSeconds) math:remainder ?remainingWorkSeconds.` | `number` |
| `w3math:product` | Берёт 2 аргумента в скобках, указанные в субъекте и результат их умножения помещает в переменную объекта. | `(?productingWorkInSeconds ?productingWorkDaysInSeconds w3math:product ?productingWorkSeconds.` | `number` |
| `w3math:lessThan` | Меньше чем | `?recordDate w3math:lessThan ?maxDate.` | `bool` |
| `w3math:notLessThan` | Не меньше чем | `?documentRecordsCount w3math:notLessThan 2.` | `bool` |
| `w3math:equalTo` | Равно (`dateTime` , `date` , `duration` , `string` , `number` ). | `?countWorkingDaysMounth w3math:equalTo ?countWorkingDays.` | `bool` |
| `w3math:notEqualTo` | Не равно (`dateTime` , `date` , `duration` , `string` , `number` ). | `?countWorkingDaysMounth w3math:notEqualTo ?countWorkingDays.` | `bool` |
| `w3math:greaterThan` | Больше чем (`dateTime` , `date` , `duration` , `string` , `number` ). | `?recordDate w3math:greaterThan ?minDate.` | `bool` |
| `w3math:notGreaterThan` | Не больше чем (`dateTime` , `date` , `duration` , `string` , `number` ). | `?documentRecordsCount w3math:notGreaterThan 2.` | `bool` |
| `w3math:negation` | Отрицание | `?firstNumber w3math:negation ?negationNumber.` | `number` |
| `@prefix cmwmath: <http://comindware.com/logics/math#>.` | | | |
| `cmwmath:sum` | Берёт сумму из субъекта типа List и записывает значение в объект. | `?durationsSeconds cmwmath:sum ?durationSumSeconds.` | `number` |
| `cmwmath:difference` | Берёт разность из субъекта типа List и записывает значение в объект. | `?list cmwmath:difference ?differenceTotal.` | `number` |
| `cmwmath:min` | Берёт минимальное значение из субъекта типа List и записывает значение в объект. | `?listQueue cmwmath:min ?queueMin.` | `number` `dateTime` `duration` |
| `cmwmath:max` | Берёт максимальное значение из субъекта типа List и записывает значение в объект. | `?listQueue cmwmath:max ?queueMax.` | `number` `dateTime` `duration` |
| `cmwmath:average` | Берёт 2 аргумента в скобках, указанные в субъекте и помещает их среднее арифметическое в переменную объекта. | `(?priceFirst ?priceSecond) cmwmath:average ?priceAverage.` | `number` |
| `cmwmath:round` | Округление к ближайшему целому. | `?quotientPrice cmwmath:round ?numberRound.` | `number` |
| `cmwmath:floor` | Округление в меньшую сторону. | `?quotientPrice cmwmath:floor ?numberFloor.` | `number` |
| `cmwmath:ceil` | Округление в большую сторону. | `?quotientPrice cmwmath:ceil ?numberCeil.` | `number` |
| Функции для работы с датами и временем | | | |
| `@prefix w3time: <http://www.w3.org/2000/10/swap/time#>.` | | | |
| `w3time:inSeconds` | Конвертирует значение типа `dateTime` или `duration` в количество секунд.  Конвертирует количество секунд в значение типа `dateTime` от начала времен. | `?durationWorkingDay w3time:inSeconds ?secondsWorkingDay.` | `number` |
| `@prefix cmwtime: <http://comindware.com/logics/time#>.` | | | |
| `cmwtime:toDuration` | Конвертирует количество секунд в значение типа `duration` . | `?secondsWorkingDay cmwtime:toDuration ?durationWorkingDay.` | `duration` |
| `cmwtime:getSpan` | Вычитает из первого значения субъекта типа `dateTime` второе значение субъекта типа `dateTime` . | `(?dateTime1 ?dateTime2) cmwtime:getSpan ?resultTimeSpan.` | `duration` |
| `cmwtime:addDuration` | Добавляет к значению субъекта типа `dateTime` значение типа `duration` . | `(?dateTime ?duration) cmwtime:addDuration ?value.` | `dateTime` |
| `cmwtime:subDuration` | Вычитает из значения субъекта типа `dateTime` значение типа `duration` . | `(?dateTime ?duration) cmwtime:subDuration ?value.` | `dateTime` |
| `cmwtime:endOfDay` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания дня, в пределах которого находится значение субъекта. | `?creationDateTime cmwtime:endOfDay ?endDateTime.` | `dateTime` |
| `cmwtime:startOfDay` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала дня, в пределах которого находится значение субъекта. | `?creationDateTime cmwtime:startOfDay ?startDateTime.` | `dateTime` |
| `cmwtime:startOfWeek` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала недели, в пределах которой находится значение субъекта. | `?creationDateTime cmwtime:startOfWeek ?startDateTime.` | `dateTime` |
| `cmwtime:startOfMonth` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала месяца, в пределах которого находится значение субъекта. | `?creationDateTime cmwtime:startOfMonth ?startDateTime.` | `dateTime` |
| `cmwtime:fromTzToTz` | Перевод значения типа `dateTime` в заданный часовой пояс. | `(?someDateTime "Etc/GMT" "Europe/Moscow") cmwtime:fromTzToTz ?tzDateTime.` | `dateTime` |
| `cmwtime:timeZoneHours` | Возвращает разницу во времени UTC и местным часовым поясом | `? cmwtime:timeZoneHours ?timeZoneDifferenceInHours.` | `integer` |
| `cmwtime:isToday` | Берёт значение из субъекта типа `dateTime` и проверяет на текущую дату. | `?creationDate cmwtime:isToday ?today.` | `bool` |
| `cmwtime:century` | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее веку указанной даты в местном часовом поясе. | `?creationDate cmwtime:century ?numberCentury.` | `number` |
| `cmwtime:isoFormat` | Конвертирует значение типа `dateTime` в формат ISO. | `?creationDate cmwtime:isoFormat ?isoFormatDate.` | `string` |
| `cmwtime:year` | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее году указанной даты в местном часовом поясе. | `?creationDate cmwtime:year ?numberYear.` | `number` |
| `cmwtime:month` | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее месяцу указанной даты в местном часовом поясе. | `?creationDate cmwtime:month ?numberMonth.` | `number` |
| `cmwtime:day` | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее дню месяца указанной даты в местном часовом поясе. | `?creationDate cmwtime:day ?numberDay.` | `number` |
| `cmwtime:hour` | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее часу указанной даты в местном часовом поясе. | `?creationDate cmwtime:hour ?numberHour.` | `number` |
| `cmwtime:minute` | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее минуте указанной даты в местном часовом поясе. | `?creationDate cmwtime:minute ?numberMinute.` | `number` |
| `cmwtime:second` | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее секундам указанной даты в местном часовом поясе. | `?creationDate cmwtime:second ?numberSecond.` | `number` |
| `cmwtime:makeDate` | Берёт значения субъекта типа число и возвращает объект типа `dateTime` . | `(?intervalBeginYear ?intervalBeginMonth ?intervalBeginDay 23 59 59) cmwtime:makeDate ?brokenIntervalEnd.`  `(?intervalEndYear ?intervalEndMonth ?intervalEndDay 0 0 0) cmwtime:makeDate ?brokenIntervalBegin.`  `(?startDateYear ?startDateMonth ?startDateDay) cmwtime:makeDate ?startDayDate.`  `(?startDateYear ?startDateMonth ?startDateDay ?startDateHour ?startDateMinute ?startDateSecond) cmwtime:makeDate ?intervalBegin.` | `dateTime` |
| `cmwtime:workhours` | Возвращает дату и время на основании количества рабочих часов с определенного момента времени, с поправкой на праздники и фактические выходные дни. | `(?startWorkDateTime ?qountWorkingHours ?startWorkingDay ?durationWorkingDay (?dateNotHoliday)) cmwtime:workhours ?newDateTime.` | `dateTime` |
| `cmwtime:workdays` | Возвращает дату на основании количества рабочих дней с определенной даты, с поправкой на праздники и фактические выходные дни. | `(?startWorkDateTime ?qountWorkingHours (?firstDateNotHoliday ?secondDateNotWorking)) cmwtime:workdays ?newDateTime.` | `dateTime` |
| `cmwtime:workhoursDuration` | Возвращает продолжительность работы между двумя датами при условии, что рабочий день начинается в заданное время и имеет определенную длительность. | `(?startWorkDateTime ?endWorkDateTime ?timeStartWorkingDay ?durationWorkingDay) cmwtime:workhoursDuration ?newDuration.` | `duration` |
| `cmwtime:workdaysDuration` | Возвращает продолжительность работы между двумя датами, на основании предположения, что рабочий день начинается в 00:00 и длится 24 часа. | `(?startWorkDateTime ?endWorkDateTime) cmwtime:workdaysDuration ?newDuration.` | `duration` |
| Функции для работы с интервалами времени | | | |
| `@prefix cmwduration: <http://comindware.com/logics/duration#>.` | | | |
| `cmwduration:days` | Берёт промежуток времени и возвращает количество дней. | `?durationHoliday cmwduration:days ?countDaysOfHoliday.` | `number` |
| `cmwduration:hours` | Берёт промежуток времени и возвращает количество часов. | `?durationHoliday cmwduration:hours ?countHoursOfHoliday.` | `number` |
| `cmwduration:minutes` | Берёт промежуток времени и возвращает количество минут. | `?durationHoliday cmwduration:minutes ?countMinutesOfHoliday.` | `number` |
| Функции для работы со строками | | | |
| `@prefix w3string: <http://www.w3.org/2000/10/swap/string#>.` | | | |
| `w3string:format` | Подставляет аргументы в нумерованные заместители вида `{0}`…`{n}` в исходной строке и возвращает результирующую строку. | `("{0}/{1} - {2}" ?value0 ?value1 ?value2) w3string:format ?outString.` | `string` |
| `w3string:matches` | Использует в качестве аргументов строку и регулярное выражение. Возвращает логическое значение Истина, если какая-либо часть строки или строка полностью соответствует условию, заданному регулярным выражением. В противном случае возвращает результат Ложь. | `?stringExample w3string:matches ?expression.` | `bool` |
| `w3string:notMatches` | Использует в качестве аргументов строку и регулярное выражение. Возвращает логическое значение Истина, если часть строки или строка полностью не соответствуют условию, заданному регулярным выражением. В противном случае возвращает результат Ложь. | `?stringExample w3string:notMatches ?expression.` | `bool` |
| `w3string:greaterThan` | Возвращает логическое значение Истина, если аргумент2 больше аргумента1, в противном случае возвращает результат Ложь. | `?creationDate w3string:greaterThan ?chooseDate.` | `bool` |
| `w3string:lessThan` | Возвращает логическое значение Истина, если аргумент2 меньше аргумента1, в противном случае возвращает результат Ложь. | `?creationDate w3string:lessThan ?chooseDate.` | `bool` |
| `w3string:notGreaterThan` | Возвращает логическое значение Истина, если аргумент2 НЕ больше аргумента1, в противном случае возвращает результат Ложь. | `?creationDate w3string:notGreaterThan ?chooseDate.` | `bool` |
| `w3string:notLessThan` | Возвращает логическое значение Истина, если аргумент2 НЕ меньше аргумента1, в противном случае возвращает результат Ложь. | `?creationDate w3string:notLessThan ?chooseDate.` | `bool` |
| `@prefix cmwstring: <http://comindware.com/logics/string#>.` | | | |
| `cmwstring:join` | Объединяет строки с использованием заданного разделителя. | `("," ?newDependencyLinks) cmwstring:join ?newDependencyLinksStr.` | `string` |
| `cmwstring:replace` | Заменяет все экземпляры заданной строки в исходной строке на новое значение. | `(?text "\n" "<br>") cmwstring:replace ?html.` | `string` |
| `cmwstring:cutString` | Обрезает строку на заданную длину и добавляет в конец заданные символы. | `(?taskTitleLong 50 "...") cmwstring:cutString ?taskTitle.` | `string` |
| `cmwstring:firstCapital` | Преобразует первый символ строки в прописной. | `?youStr cmwstring:firstCapital ?youStrCapital.` | `string` |
| `cmwstring:concatenation` | Конкатенация строк. | `(?firstString ?secondString) cmwstring:concatenation ?newString.` | `string` |
| `cmwstring:length` | Возвращает количество символов в строке. | `?stringName cmwstring:length ?countSymbols.` | `number` |
| `cmwstring:substring` | Обрезает строку от заданной позиции на заданное количестве символов (опционально). | `(?sourceString 2 4) cmwstring:substring ?resultString.`  `(?sourceString 2) cmwstring:substring ?resultString.` | `string` |
| `cmwstring:indexOf` | Возвращает номер (отсчитываемый от нуля) позиции, на которой располагается искомая строка в исходной строке. Номер позиции может отсчитываться от произвольного положения (опционально). | `(?sourceString ?subString) cmwstring:indexOf ?resultString.`  `(?sourceString ?subString 4) cmwstring:indexOf ?resultString.` | `number` |
| `cmwstring:toUri` | Преобразует escape-последовательности в URI. | `?sequence cmwstring:toUri ?reference.` | `string` |
| `cmwstring:fromUri` | Преобразует URI в escape-последовательности. | `?reference cmwstring:fromUri ?sequence.` | `string` |
| `cmwstring:toBase64` | Преобразует строку по стандарту кодирования Base64. | `?string cmwstring:toBase64 ?newStringBase.` | `string` |
| `cmwstring:fromBase64` | Декодирует строку по стандарту Base64. | `?stringBase cmwstring:fromBase64 ?newString.` | `string` |
| `cmwstring:split` | Находит заданный разделитель в строке и создает список. | `("_" ?string) cmwstring:split ?newString.` |  |
| `cmwstring:format` | Форматирует аргументы в соответствии с заданным шаблоном. Возвращает отформатированную строку. | `("{0}/{1} - {2}" ?v0 ?v1 ?v2) cmwstring:format ?outString.` | `string` |
| `@prefix cmwlogics: <http://comindware.com/logics#>.` | | | |
| `cmwlogics:value` | Присваивает значение субъекта объекту. | `?left cmwlogics:value ?right.`  `{time:now => ?left.`  `?left cmwlogics:value ?right`  `Result: ?right = dateTime.UtcNow.}` | `number` `dateTime` `string` `duration` `reference` `account` |
| `@prefix cmwentity: <http://comindware.com/ontology/entity#>.` | | | |
| `cmwentity:like` | Сравнивает шаблон и строку. | `?pattern cmwentity:like ?sourceString.` | `bool` |
| `cmwentity:startsWith` | Проверяет, что заданная строка начинается в соответствии с шаблоном и (опционально) в соответствии с заданной опцией сравнения (StringComparison). | `?sourceString entity:startsWith ?pattern.`  `(?sourceString “OrdinalIgnoreCase”) entity:startsWith ?pattern.` | `bool` |
| `cmwentity:endsWith` | Проверяет, что заданная строка заканчивается в соответствии с шаблоном и (опционально) в соответствии с заданной опцией сравнения (StringComparison). | `?sourceString entity:endsWith ?pattern.`  `(?sourceString “OrdinalIgnoreCase”) entity:endsWith ?pattern.` | `bool` |
| `cmwentity:indexOf` | Возвращает индекс первого вхождения подстроки в строку. Отсчет начинается с 1. | `(?sourceString ?substring) entity:indexOf ?index.` | `number` |
| `cmwentity:toLower` | Преобразует все символы строки в строчные. | `?string entity:toLower ?stringLow.` | `string` |
| `cmwentity:toUpper` | Преобразует все символы строки в прописные. | `?string entity:toUpper ?stringUpper.` | `string` |
| `cmwentity:contains` | Проверяет вхождение значения объекта типа `string` в значение субъекта типа `string` . | `?string entity:contains ?subString.` | `string` |
| `@prefix cmwbuiltin: <http://comindware.com/ontology/image/builtin#>.` | | | |
| `cmwbuiltin:toPlainText` | Конвертирует HTML-текст в обычный. | `?htmlText builtin:toPlainText ?plainText.` | `string` |
| Функции для работы со списками | | | |
| `@prefix w3list: <http://www.w3.org/2000/10/swap/list#>.` | | | |
| `w3list:append` | `((1 2) (3 4)) w3list:append (1 2 3 4)` |  |  |
| `w3list:in` |  |  | `bool` |
| `w3list:last` | Из представленной последовательности получает последний элемент. | `?listFlowers w3list:last ?lastFlower.` | `string` |
| `w3list:member` |  |  |  |
| `@prefix cmwlist: <http://comindware.com/logics/list#>.` | | | |
| `cmwlist:length` | Возвращает количество элементов последовательности. | `?listFlowers cmwlist:length ?countFlowers.` | `number` |
| `cmwlist:at` | Берёт список элементов и задает индекс. Возвращает значение элемента, соответствующее индексу.  `([23, 25, 12] 2)` возвращает `12`. | `(?list ?index) cmwlist:at ?valueOfIndex.` | `string` |
| Функции группировки и сортировки списков | | | |
| `@prefix cmwentity: <http://comindware.com/ontology/entity#>.` | | | |
| `cmwentity:groupby` | Группировка | `(?recordTemplate ?dataSet) entity:groupby ?attributeGroup` |  |
| `cmwentity:sortby` | Сортировка | `(?recordTemplate ?dataSet)  entity:sortby ?attributeGroup`  `(("key1_1" "key2_1" "value1_1") ("key1_2" "key2_2" "value1_2") ("key1_3" "key2_3" "value1_3"))`  `//  )`  `// right:`  `//  (("value1_2") ("value1_1") ("value1_3")) - sorted field-to-select data` |  |
| `@prefix cmwassert: <http://comindware.com/logics/assert#>.` | | | |
| `cmwassert:true` | `true` |  |  |
| `cmwassert:false` | `false` |  |  |
| `cmwassert:or` | Оператор `ИЛИ` | `or {} or {} … or {}.` |  |
| `cmwassert:if` | Условный оператор | `if {} then {} else {}.` |  |
| `cmwassert:count` | Выводит количество записей, удовлетворяющих условиям. | `{} assert:count ?c.` |  |
| `cmwassert:union` | Объединяет итераторы в один. | `({} … {}) assert:union true.` |  |
| `cmwassert:distinct` | Выбирает уникальные записи из связанных наборов данных. | `{`  `?item ?Positions ?PositionsVal.`  `?PositionsVal ?Items ?ItemsVal.`  `} assert:distinct ?ItemsVal.` |  |
| `cmwassert:range` |  |  |  |
| `cmwassert:sort` |  | `@in ?historyRecord1, ?historyRecord2.`  `@out ?result.`  `{`  `?historyRecord1 history:recordDate ?recordDate1.`  `?historyRecord2 history:recordDate ?recordDate2.`  `(?recordDate1 ?recordDate2) sort:timeComparer ?result.`  `} => { (?historyRecord1 ?historyRecord2) notification:sortHistoryRecords ?result }.`  `{`  `…`  `from {`  `?actualHistoryRecord history:recordOfSubjectHistory ?subject.`  `?actualHistoryRecord history:recordDate ?actualHistoryDate.`  `?actualHistoryDate math:notLessThan ?oldestHistoryDate.`  `?actualHistoryDate math:notGreaterThan ?newestHistoryDate.`  `} select ?actualHistoryRecord -> ?actualHistoryRecords.`  `(?actualHistoryRecords notification:sortHistoryRecords) assert:sort ?actualHistoryRecordsSorted.`  `…`  `}` |  |
| `cmwassert:once` | Выходит после первой успешной итерации. | `once {}.` |  |
| Функции для работы с идентификаторами ресурсов | | | |
| `@prefix cmwurl: <http://comindware.com/logics/url#>.` | | | |
| `cmwurl:encode` | Кодирует строку URL-адреса.  Аналог `System.Web.HttpUtility.UrlEncode(url)` | `?url cmwurl:encode ?encodedUrl.` | `string` |
| `cmwurl:combine` | Объединяет части предоставления списка строк пути в путь одной строкой. Аналог `System.IO.Path.Combine` | `(?path1 ?path2 ?path3 ...) cmwurl:combine ?combinedPath.` | `string` |
| `cmwurl:siteDir` | Получает текущую директорию нахождения проекта. | `?unused  cmwurl:siteDir ?siteDir.` | `string` |
| `@prefix cmwui: <http://comindware.com/ontology/ui#>.` | | | |
| `cmwui:toClientString` | Получает строковое представление ресурса (элемента или атрибута). | `?object cmwui:toClientString ?string.` | `string` |
| `cmwui:toQName` | Преобразует строковое представление ресурса в QName. | `?object cmwui:toQName ?qName.` | `string` |
| Функции поддерживающие и корректно обрабатывающие нулевые значения | | | |
| `@prefix cmwnullable <http://comindware.com/ontology/entity/nullable#>.` | | | |
| `cmwnullable:lessThan` | Меньше чем. (`dateTime` , `date` , `duration` , `string` , `number` )  Если в субъекте нулевое значение, возвращает нулевое значение. | `?recordDate cmwnullable:lessThan ?maxDate.` | `bool` |
| `cmwnullable:greaterThan` | Больше чем (`dateTime` , `date` , `duration` , `string` , `number` )  Если в субъекте нулевое значение, возвращает нулевое значение. | `?recordDate cmwnullable:greaterThan ?minDate.` | `bool` |
| `cmwnullable:notLessThan` | Не меньше (`dateTime` , `date` , `duration` , `string` , `number` )  Если в субъекте нулевое значение, возвращает нулевое значение. | `?documentRecordsCount cmwnullable:notLessThan 2.` | `bool` |
| `cmwnullable:notGreaterThan` | Не больше (`dateTime` , `date` , `duration` , `string` , `number` )  Если в субъекте нулевое значение, возвращает нулевое значение. | `?documentRecordsCount cmwnullable:notGreaterThan 2.` | `bool` |
| `cmwnullable:quotient` | Берёт 2 аргумента в скобках, указанные в субъекте и результат деления первого на второе помещает в переменную объекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `(?WorkInSeconds ?WorkDaysInSeconds) cmwnullable:quotient ?WorkSeconds.` | `number` |
| `cmwnullable:product` | Берёт 2 аргумента в скобках, указанные в субъекте и результат их умножения помещает в переменную объекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `(?productingWorkInSeconds ?productingWorkDaysInSeconds) cmwnullable:product ?productingWorkSeconds.` | `number` |
| `cmwnullable:integerQuotient` | Берёт 2 аргумента в скобках, указанные в субъекте и результат целочисленного деления первого на второе помещает в переменную объекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `(?WorkInSeconds ?WorkDaysInSeconds) cmwnullable:integerQuotient ?WorkSeconds.` | `number` |
| `cmwnullable:remainder` | Берёт 2 аргумента в скобках, указанные в субъекте и остаток от деления первого на второе помещает в переменную объекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `(?remainingWorkInSeconds ?remainingWorkDaysInSeconds) cmwnullable:remainder ?remainingWorkSeconds.` | `number` |
| `cmwnullable:sum` | Берёт сумму из субъекта типа `List` и записывает значение в объект.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?durationsSeconds cmwnullable:sum ?durationSumSeconds.` | `number` |
| `cmwnullable:difference` | Берёт разность из субъекта типа `List` и записывает значение в объект.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?list cmwnullable:difference ?differenceTotal.` | `number` |
| `cmwnullable:startOfDay` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала дня, в пределах которого находится значение субъекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?creationDateTime cmwnullable:startOfDay ?startDateTime.` | `dateTime` |
| `cmwnullable:startOfWeek` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала недели, в пределах которой находится значение субъекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?creationDateTime cmwnullable:startOfWeek ?startDateTime.` | `dateTime` |
| `cmwnullable:startOfMonth` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала месяца, в пределах которого находится значение субъекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?creationDateTime cmwnullable:startOfMonth ?startDateTime.` | `dateTime` |
| `cmwnullable:startOfQuarter` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала квартала, в пределах которого находится значение субъекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?creationDateTime cmwnullable:startOfQuarter ?startDateTime.` | `dateTime` |
| `cmwnullable:startOfYear` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала месяца, в пределах которого находится значение субъекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?creationDateTime cmwnullable:startOfYear ?startDateTime.` | `dateTime` |
| `cmwnullable:endOfDay` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания дня, в пределах которого находится значение субъекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?creationDateTime cmwnullable:endOfDay ?endDateTime.` | `dateTime` |
| `cmwnullable:endOfWeek` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания недели, в пределах которой находится значение субъекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?creationDateTime cmwnullable:endOfWeek ?endDateTime.` | `dateTime` |
| `cmwnullable:endOfMonth` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания месяца, в пределах которого находится значение субъекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?creationDateTime cmwnullable:endOfMonth ?endDateTime.` | `dateTime` |
| `cmwnullable:endOfQuarter` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания квартала, в пределах которого находится значение субъекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?creationDateTime cmwnullable:endOfQuarter ?endDateTime.` | `dateTime` |
| `cmwnullable:endOfYear` | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания года, в пределах которого находится значение субъекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?creationDateTime cmwnullable:endOfYear ?endDateTime.` | `dateTime` |
| `cmwnullable:inSeconds` | Конвертирует значение длительности в количество секунд.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?durationWorkingDay cmwnullable:inSeconds ?secondsWorkingDay.` | `number` |
| `cmwnullable:min` | Берёт минимальное значение из субъекта типа `List` и записывает значение в объект.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?listQueue cmwnullable:min ?queueMin.` | `number`  `dateTime   date`  `duration` |
| `cmwnullable:max` | Берёт максимальное значение из субъекта типа `List` и записывает значение в объект.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?listQueue cmwnullable:max ?queueMax.` | `number`  `dateTime   date`  `duration` |
| `cmwnullable:average` | Берёт 2 аргумента в скобках, указанные в субъекте и помещает их среднее арифметическое в переменную объекта.  Если в субъекте нулевое значение, возвращает нулевое значение. | `(?priceFirst ?priceSecond) cmwnullable:average ?priceAverage.` | `number` |
| `cmwnullable:toDuration` | Конвертирует количество секунд в значение типа `duration` .  Если в субъекте нулевое значение, возвращает нулевое значение. | `?secondsWorkingDay cmwnullable:toDuration ?durationWorkingDay.` | `duration` |
| `cmwnullable:round` | Округление к ближайшему целому.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?quotientPrice cmwnullable:round ?numberRound.` | `number` |
| `cmwnullable:floor` | Округление в меньшую сторону.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?quotientPrice cmwnullable:floor ?numberFloor.` | `number` |
| `cmwnullable:ceiling` | Округление в большую сторону.  Если в субъекте нулевое значение, возвращает нулевое значение. | `?quotientPrice cmwnullable:ceiling ?numberCeil.` | `number` |
| `cmwnullable:format` | Форматирует аргументы в соответствии с заданным шаблоном. Возвращает отформатированную строку.  Если в субъекте нулевое значение, возвращает нулевое значение. | `("{0}/{1} - {2}" ?v0 ?v1 ?v2) cmwnullable:format ?outString.` | `string` |
| Функции для работы с изображениями | | | |
| `@prefix cmwbuiltin: <http://comindware.com/ontology/image/builtin#>.` | | | |
| `cmwbuiltin:isSupportedImage` | Проверяет формат файла на соответствие одному из допустимых форматов: .`bmp, .gif, .exif, .jpg, .jpeg, .png, .tif` | `“bllalblablab.jpg” => ?fileName.`  `?fileName builtin:isSupportedImage ?right.` | `bool` |
| `cmwbuiltin:dimensions` | По `streamId` изображения получает разрешение в формате ширина × высота. | `?streamId builtin:dimensions ?dimensions.` | `string` |
| Специальные функции для работы с аккаунтами и группами | | | |
| `@prefix cmwlogics: <http://comindware.com/logics#>.` | | | |
| `cmwlogics:currentUser` | Предикат, получающий аккаунт текущего пользователя. | `cmwlogics:securityContext cmwlogics:currentUser ?userVal.` |  |
| `cmwlogics:securityContext` | Субъект, определяющий контекст персонального пространства. | `cmwlogics:securityContext cmwlogics:currentUser ?userVal.` |  |
| @prefix cmwaccount: <http://comindware.com/ontology/account#>. | | | |
| `cmwaccount:Group` | Определяет тип переменной Группа. | `?group rdf:type cmwaccount:Group.` |  |
| `cmwaccount:groupName` | Предикат для получения наименования группы. | `?group cmwaccount:groupName ?groupName.` | `string` |
| `cmwaccount:isSystemAdministrator` | Предикат для определения принадлежности аккаунта к системной роли «Системные администраторы» | `?user cmwaccount:isSystemAdministrator ?access.` | `bool` |
| `cmwaccount:displayName` | Предикат, для получения полного имени аккаунта | `?user cmwaccount:displayName ?userDisplayName.` | `string` |
| `cmwaccount:fullName` | Предикат для получения Ф. И. О. аккаунта. | `?user cmwaccount:fullName ?userNameSurname.` | `string` |
| `cmwaccount:manager` | Предикат для получения аккаунта руководителя, указанного для аккаунта. | `?user cmwaccount:manager ?userManager.` | `accountProperty` |
| `cmwaccount:mbox` | Предикат для получения адреса эл. почты аккаунта. | `?user cmwaccount:mbox ?userEmail.` | `string` |
| `cmwaccount:phone` | Предикат для получения номера телефона аккаунта. | `?user cmwaccount:phone ?userMobile.` | `string` |
| `cmwaccount:instantMessagingId` | Предикат для получения идентификатора аккаунта в мессенджере. | `account:instantMessagingId` | `string` |
| `cmwaccount:status` | Предикат для получения статуса аккаунта: `true` — включён. | `?user cmwaccount:status ? enabled` | `bool` |
| `cmwaccount:skype` | Предикат для получения идентификатора аккаунта в Skype. | `?user cmwaccount:skype ?loginSkype.` | `string` |
| `cmwaccount:username` | Предикат для получения имени пользователя  (логина) аккаунта. | `?user cmwaccount:username ?login.` | `string` |
| `cmwaccount:active` | Предикат для получения состояния аккаунта: `true` — включён. | `?user cmwaccount:active ? enabled` | `bool` |
| `cmwaccount:lastLoginDate` | Предикат для получения даты последней авторизации аккаунта. | `?user cmwaccount:lastLoginDate ?lastLoginDate.` | `dateTime` |
| `cmwaccount:language` | Предикат для получения кода языка отображения веб-сайта для аккаунта. | `?user cmwaccount:language ?userLanguage.` | `string` |
| `cmwaccount:sid` | Предикат для получения Active Directory Security ID аккаунта. | `?user account:sid ?sid.` | `string` |
| `cmwaccount:notificationSettings` | Предикат для получения параметров уведомлений аккаунта | `?user account:notificationSettings ?notificationConfig .` | `multiValue` |
| `cmwaccount:password` | Предикат для получения пароля к аккаунту. | `?user cmwaccount:password ?userPassword` | `string` |
| `cmwaccount:userpic` | Предикат для получения изображения профиля аккаунта. | `?user cmwaccount:userpic ?picture ..` | `string` |
| `cmwaccount:userpicLarge` | Предикат для получения увеличенного изображения профиля аккаунта. | `?user cmwaccount:userpicLarge ?picture.` | `string` |
| `cmwaccount:title` | Предикат для получения наименования должности аккаунта. | `?user cmwaccount:title  ?jobTitle.` | `string` |
| `cmwaccount:department` | Предикат для получения наименования отдела аккаунта. | `?user cmwaccount:department  ?departmentName.` | `string` |
| `cmwaccount:office` | Предикат для получения наименования офиса аккаунта. | `?user cmwaccount:office  ?officeName.` | `string` |
| `cmwaccount:userGroupMembership` | Предикат для получения списка групп, в которых состоит аккаунт. | `?user cmwaccount:userGroupMembership  ?goupList.` | `multiValue    groupProperty` |
| `cmwaccount:authenticationMethod` | Предикат для получения способа аутентификации аккаунта. | `?user cmwaccount:authenticationMethod ?authMethod.` | `string` |
| `cmwaccount:substitute` | Предикат для получения аккаунта заместителя, назначенного аккаунту. | `?user cmwaccount:substitute ?substituteAccount.` | `accountProperty` |
| `cmwaccount:substituteDateFrom` | Предикат для получения даты начала замещения аккаунта. | `?user cmwaccount:substituteDateFrom  ?subsitutionStart` | `dateTime` |
| `cmwaccount:substituteDateTo` | Предикат для получения даты окончания замещения аккаунта. | `?user cmwaccount:substituteDateTo  ?subsitutionEnd` | `dateTime` |
| `cmwaccount:birthday` | Предикат для получения дня рождения аккаунта. | `?user cmwaccount:birthday  ?birthday.` | `dateTime` |
| `cmwaccount:personalCalendarId` | Предикат для получения ID персонального календаря аккаунта. | `?user cmwaccount:personalCalendarId  ?calendarID.` | `string` |
| `cmwaccount:personalCalendarUri` | Предикат для получения URI персонального календаря аккаунта. | `?user cmwaccount:personalCalendarUri  ?calendarURI.` | `string` |
| `cmwaccount:presentedOnOrgchart` | Предикат для получения статуса включения аккаунта в организационную структуру: `true` — включён. | `?user cmwaccount:presentedOnOrgchart ?onOrgChart.` | `bool` |
| `cmwaccount:timeZone` | Предикат для получения серверного часового пояса аккаунта. | `?user cmwaccount:timeZone ?userTimeZone.` | `string` |
| Специальные функции | | | |
| `@prefix cmwobject: <http://comindware.com/ontology/object#>.` | | | |
| `cmwobject:findProperty` | Возвращает ID атрибута в переменную в объекте по заданным паре код шаблона записи и код атрибута в скобках субъекта. | `("ship_request" "client_code_SAP") cmwobject:findProperty ?cp.` |  |
| `@prefix cmwcontext: <http://comindware.com/logics/session/context#>.` | | | |
| `cmwcontext:time` | Возвращает текущее время сеанса. |  | `dateTime` |
| `cmwcontext:timeZoneOffset` | Возвращает смещение часового пояса сеанса. |  | `number` |
| `cmwcontext:origin` | Возвращает объект, по которому был запущен сценарий. |  |  |
| `cmwcontext:variable` | Возвращает переменную в контексте. |  |  |