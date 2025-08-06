---
title: Написание выражений на языке N3
kbId: 4852
---

# Написание выражений на языке N3

## Введение

**{{ productName }}** позволяет составлять выражения на языке N3 (Notation3) для выполнения запросов данных и вычисления значений.

Преимущество языка N3 заключается в скорости вычислений, что позволяет эффективно использовать все возможности графовой базы данных. Язык выражений N3 позволяет осуществлять доступ к искомым данным и их связям поатрибутивно без необходимости загрузки данных потаблично, что присуще реляционным базам данных и языку запросов SQL.

Нотация N3 представляет собой набор записей типа: «субъект» «предикат» «объект». Данная конструкция может применяться в различных вариантах, от получения данных по заданным атрибутам, до математических операций.

## Синтаксис N3

Выражения N3 состоят из триплетов вида субъект-предикат-объект.

Например, `?group rdf:type account:Group` — триплет, позволяющий по любому из заданных аргументов обнаружить неизвестные. Если в триплете заданы объект и предикат, ПО будет осуществлять поиск субъекта, если заданы субъект и предикат — поиск объекта и т.д. Если в выражении задан один аргумент, ПО вернёт все значения для остальных двух.

Основы построения языка выражений N3 приведены в открытой документации, размещенной по адресу <https://www.w3.org/TR/rdf11-concepts/>.

### Синтаксические элементы

- `@prefix property: <http://comindware.com/ontology/user/op#>.` — объявление префикса встроенного пакета, т. е. синонима, используемого в выражении.
- `rdf:type` — использование префикса для удобочитаемости и сокращения размеров кода.
- `{}` — объявление тела выражения.
- `?` — объявление переменных.
- `?item` — входной параметр.
- `?item` — значения ссылки (экземпляры шаблона записи, с которым связан текущий шаблон записи).
- `?value` — выходной параметр.
- `a` — принадлежность субъекта к объекту.
- `.` — терминатор триплета.
- `#` — комментарий.
- `->` — присваивание значения.
- `()` — объявление списка.
- `[]` — неявное использование субъекта.

### Полезные конструкции и встроенные функции

- `("templateSystemName" "attributeSystemName") object:findProperty ?p.` — возвращает в переменную `?p` атрибут по заданным системным именам шаблона и атрибута.
- `once {}.` — выходит после первой успешной итерации.
- `or {} or {} … or {}.` — логический оператор `ИЛИ`.
- `if {} then {} else {}.` — условный оператор.
- `from {} select ?v -> ?vList.` — возвращает список в переменную `?vList`.
- `?list math:sum ?sum.` — вычисляет сумму.
- `{} assert:count ?c.` — вычисляет количество записей.
- `({} … {}) assert:union true.` — объединяет итераторы в один.

### Упрощения

Ниже представлены некоторые упрощения N3, упрощающие и ускоряющие работу.

- `@prefix: <#>.` — `:John` означает, что субъект определён в текущем документе.
- `a/ @a` — `Rdf:type`.
- `[]` — указываем, что существует объект с заданными свойствам без возможности ссылаться на него.
- `=` — эквивалентность (`owl:equivalentTo`).
- `=>` — `Log:implies`.
- `объект.свойство` — переход к свойству.
- `(элемент1 элемент2)` — список.
- `_:variable` — `log:forSome`.
- `?variable` — `log:forAll`.

## Запросы в N3

- Запросы пишутся в виде набора триплетов.
- У запроса есть входные (в некоторых случаях) и выходные данные.
- Запрос выполняется последовательно сверху вниз по каждому триплету.
- Если запрос ничего не вернул, то это считается пустым результатом.
- Ризонёр (Reasoner) — специальный механизм, выполняющий запросы.

```
in ?item.
{
  #наш код
} => { ?item attribute:value ?value. }.

```

### Пять видов запросов

| Структура запроса | | | Описание |
| --- | --- | --- | --- |
| `субъект` | `предикат` | `объект не указан` | Поиск объекта по заданному предикату и субъекту. |
| `субъект не указан` | `предикат` | `объект` | Поиск субъекта по заданному предикату и объекту. |
| `субъект` | `предикат` | `объект` | Проверка субъекта и объекта на полное совпадение. |
| `субъект не указан` | `предикат` | `объект не указан` | Поиск субъекта и объекта по заданному предикату. |
| `субъект` | `предикат` | `?.` | Проверка наличия значения. Здесь `?.` — обозначение функции проверки наличия непустого значения (факта) по субъекту и предикату. |

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

| Сущность | Входные данные (контекст) | Выходные данные |
| --- | --- | --- |
| Атрибут → Вычисляемое значение | `?item` — текущая запись или экземпляр процесса | `?value` — вычисленное значение атрибута |
| Форма → Фильтр на поле | `?item` — текущая запись или экземпляр процесса | `?value` — список искомых записей |
| Правила для формы → Правило → Условие выполнения | `?item` — текущая запись или экземпляр процесса | `?value` — `true` (правило сработает) или `false` или пусто (не сработает) |
| Правила для формы → Действие → Условие выполнения | `?item` — текущая запись или экземпляр процесса | `?value` — `true` (действие сработает) или `false` или пусто (не сработает) |
| Правила для формы → Вычисляемое значение для действия | `?item` — текущая запись или экземпляр процесса | `?value` — целевое значение атрибута |
| Кнопка → Условия отображения | `?item` — текущая запись или экземпляр процесса | `?value` — `true` или false |
| Таблица → Системный фильтр |  | `?item` — список записей для вывода в таблице |
| Роль → Разрешения → Шаблон записи, аккаунта, процесса → Фильтр аккаунтов | `?item` — текущая запись или экземпляр процесса | `?value` — список групп или аккаунтов, которые имеют соответствующие разрешения на запись или экземпляр процесса |
| Роль → Разрешения → Шаблон записи, аккаунта, процесса → Условие применения | `?item` — текущая запись или экземпляр процесса | `?value` — `true` или `false` |
| Сценарий → Изменение значений переменных → Вычисление значения | `?item` — текущая запись или экземпляр процесса | `?value` — вычисленное значение переменной |
| Сценарий → Изменение значений атрибутов → Вычисление значения | `?item` — текущая запись или экземпляр процесса | `?value` — вычисленное значение атрибута |
| Сценарий → Смена контекста → Вычисление набора объектов | `?item` — текущая запись или экземпляр процесса | `?value` — список объектов для перехода |
| Сценарий → Дублирование записи → Вычисление набора объектов | `?item` — текущая запись или экземпляр процесса | `?value` — список объектов для дублирования |
| Сценарий → Проверка результата выражения → Выражение для проверки | `?item` — текущая запись или экземпляр процесса | `?value` — `true` (проверка пройдена) или `false` |
| Сценарий → Выполнение по условиям → Условие выполнения действий | `?item` — текущая запись или экземпляр процесса | `?value` — `true` (выполнять действия) или `false` |
| Сценарий → Повтор по числовому счётчику → Количество итераций | `?item` — текущая запись или экземпляр процесса | `?value` — количество итераций |
| Сценарий → Повтор по количеству объектов → Вычисление набора объектов | `?item` — текущая запись или экземпляр процесса | `?value` — список объектов |

## Примеры использования встроенных функций и операторов N3

### Функция `.?`

```
@prefix object: <http://comindware.com/ontology/object#>.
{
  ("currentTemplate" "Region") object:findProperty ?Region.
  # Проверяем, что в текущей записи, атрибут Region содержит непустое значение
  ?item ?Region ?.
  ?item -> ?value.
}

```

### Функция `once`

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

### Оператор `if`

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

### Оператор `from` и функция `sum`

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

### Функция `count`

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

### Функция `distinct`

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

### Оператор `union`

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

### Пример 1

Вывести заявки, у которых значение атрибута Status не равно «Завершен» и дата начала уже прошла относительно текущей даты.

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

### Пример 2

При добавлении существующих записей в коллекцию отображать в списке только те проекты, у которых прошла проверка (атрибут Proverka имеет значение `true`) или у которых атрибут Status имеет значение «Создан».

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

### Пример 3

Выводить в списке на добавление только руководителей текущего пользователя (атрибут manager типа «Аккаунт») или пользователей с должностью «Менеджер» (атрибут title типа «Текст»)

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

### Пример 4

Выводить только тех заявителей, которые прикреплены к заявкам.

```
@prefix object: <http://comindware.com/ontology/object#>.
{
  ("Zayavitel" "Application") object:findProperty ?ApplicationProp.
  ?Zayavitel ?ApplicationProp ? .
}

```

### Пример 5

Выполнять действия с полем на форме при условии, что процент выполнения заявки больше 70, при этом действие не должно выполняться, если этап (атрибут Etap) выполнения равен 1.

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
}

```

### Пример 6

При выполнении вышеописанного условия, выполнять для поля «Статус» заявки следующие действия: сменить тип доступа на «Только для чтения», установить значение «Завершена» и показать предупреждение с текстом «Заявка <Название заявки (атрибут Name)> завершена».

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

## Справочник встроенных функций N3

В следующей таблице приведен перечень функций, которые можно использовать в выражениях N3.

Определения

- ***QName*** — qualified name (квалифицированное имя) идентификатор для элементов и атрибутов. QName используется для создания соответствия между URI и пространством имен.
- ***Escape-последовательности*** — сочетание символов, состоящих из косой черты (`\\`), за которой следует буква или набор цифр. Escape-последовательность рассматривается как один символ и, следовательно, является допустимой символьной константой.
- ***StreamID*** — идентификатор файла изображения, расположенного в базе данных ПО.

### Математические функции `w3math`

| `@prefix w3math: <http://www.w3.org/2000/10/swap/math#>.` | |
| --- | --- |
| `w3math:quotient` | |
| --- | --- |
| **Описание** | Берёт 2 аргумента в скобках, указанные в субъекте и результат деления первого на второе помещает в переменную объекта. |
| **Синтаксис** | ``` (?WorkInSeconds ?WorkDaysInSeconds) w3math:quotient ?WorkSeconds.   ``` |
| **Возвращает** | `number` |
| `w3math:integerQuotient` | |
| **Описание** | Берёт 2 аргумента в скобках, указанные в субъекте и результат целочисленного деления первого на второе помещает в переменную объекта. |
| **Синтаксис** | ``` (?WorkInSeconds ?WorkDaysInSeconds) w3math:integerQuotient ?WorkSeconds.   ``` |
| **Возвращает** | `number` |
| `w3math:remainder` | |
| **Описание** | Берёт 2 аргумента в скобках, указанные в субъекте и остаток от деления первого на второе помещает в переменную объекта. |
| **Синтаксис** | ``` (?remainingWorkInSeconds ?remainingWorkDaysInSeconds) math:remainder ?remainingWorkSeconds.   ``` |
| **Возвращает** | `number` |
| `w3math:product` | |
| **Описание** | Берёт 2 аргумента в скобках, указанные в субъекте и результат их умножения помещает в переменную объекта. |
| **Синтаксис** | ``` (?productingWorkInSeconds ?productingWorkDaysInSeconds) w3math:product ?productingWorkSeconds.   ``` |
| **Возвращает** | `number` |
| `w3math:lessThan` | |
| **Описание** | Меньше чем |
| **Синтаксис** | ``` ?recordDate w3math:lessThan ?maxDate.   ``` |
| **Возвращает** | `bool` |
| `w3math:notLessThan` | |
| **Описание** | Не меньше чем |
| **Синтаксис** | ``` ?documentRecordsCount w3math:notLessThan 2.   ``` |
| **Возвращает** | `bool` |
| `w3math:equalTo` | |
| **Описание** | Равно (`dateTime` , `date` , `duration` , `string` , `number`). |
| **Синтаксис** | ``` ?countWorkingDaysMounth w3math:equalTo ?countWorkingDays.   ``` |
| **Возвращает** | `bool` |
| `w3math:notEqualTo` | |
| **Описание** | Не равно (`dateTime` , `date` , `duration` , `string` , `number`). |
| **Синтаксис** | ``` ?countWorkingDaysMounth w3math:notEqualTo ?countWorkingDays.   ``` |
| **Возвращает** | `bool` |
| `w3math:greaterThan` | |
| **Описание** | Больше чем (`dateTime` , `date` , `duration` , `string` , `number`). |
| **Синтаксис** | ``` ?recordDate w3math:greaterThan ?minDate.   ``` |
| **Возвращает** | `bool` |
| `w3math:notGreaterThan` | |
| **Описание** | Не больше чем (`dateTime` , `date` , `duration` , `string` , `number`). |
| **Синтаксис** | ``` ?documentRecordsCount w3math:notGreaterThan 2.   ``` |
| **Возвращает** | `bool` |
| `w3math:negation` | |
| **Описание** | Отрицание |
| **Синтаксис** | ``` ?firstNumber w3math:negation ?negationNumber.   ``` |
| **Возвращает** | `number` |

### Математические функции `cmwmath`

| `@prefix cmwmath: <http://comindware.com/logics/math#>.` | |
| --- | --- |
| `cmwmath:sum` | |
| --- | --- |
| **Описание** | Берёт сумму из субъекта типа List и записывает значение в объект. |
| **Синтаксис** | ``` ?durationsSeconds cmwmath:sum ?durationSumSeconds.   ``` |
| **Возвращает** | `number` |
| `cmwmath:difference` | |
| **Описание** | Берёт разность из субъекта типа List и записывает значение в объект. |
| **Синтаксис** | ``` ?list cmwmath:difference ?differenceTotal.   ``` |
| **Возвращает** | `number` |
| `cmwmath:min` | |
| **Описание** | Берёт минимальное значение из субъекта типа List и записывает значение в объект. |
| **Синтаксис** | ``` ?listQueue cmwmath:min ?queueMin.   ``` |
| **Возвращает** | `number` `dateTime` `duration` |
| `cmwmath:max` | |
| **Описание** | Берёт максимальное значение из субъекта типа List и записывает значение в объект. |
| **Синтаксис** | ``` ?listQueue cmwmath:max ?queueMax.   ``` |
| **Возвращает** | `number` `dateTime` `duration` |
| `cmwmath:average` | |
| **Описание** | Берёт 2 аргумента в скобках, указанные в субъекте и помещает их среднее арифметическое в переменную объекта. |
| **Синтаксис** | ``` (?priceFirst ?priceSecond) cmwmath:average ?priceAverage.   ``` |
| **Возвращает** | `number` |
| `cmwmath:round` | |
| **Описание** | Округление к ближайшему целому. |
| **Синтаксис** | ``` ?quotientPrice cmwmath:round ?numberRound.   ``` |
| **Возвращает** | `number` |
| `cmwmath:floor` | |
| **Описание** | Округление в меньшую сторону. |
| **Синтаксис** | ``` ?quotientPrice cmwmath:floor ?numberFloor.   ``` |
| **Возвращает** | `number` |
| `cmwmath:ceil` | |
| **Описание** | Округление в большую сторону. |
| **Синтаксис** | ``` ?quotientPrice cmwmath:ceil ?numberCeil.   ``` |
| **Возвращает** | `number` |

### Функции для работы с датами и временем `w3time`

| `@prefix w3time: <http://www.w3.org/2000/10/swap/time#>.` | |
| --- | --- |
| `w3time:inSeconds` | |
| --- | --- |
| **Описание** | Конвертирует значение типа `dateTime` или `duration` в количество секунд. Конвертирует количество секунд в значение типа `dateTime` от начала времен. |
| **Синтаксис** | ``` ?durationWorkingDay w3time:inSeconds ?secondsWorkingDay.   ``` |
| **Возвращает** | `number` |

### Функции для работы с датами и временем `cmwtime`

| `@prefix cmwtime: <http://comindware.com/logics/time#>.` | |
| --- | --- |
| `cmwtime:toDuration` | |
| --- | --- |
| **Описание** | Конвертирует количество секунд в значение типа `duration`. |
| **Синтаксис** | ``` ?secondsWorkingDay cmwtime:toDuration ?durationWorkingDay.   ``` |
| **Возвращает** | `duration` |
| `cmwtime:getSpan` | |
| **Описание** | Вычитает из первого значения субъекта типа `dateTime` второе значение субъекта типа `dateTime`. |
| **Синтаксис** | ``` (?dateTime1 ?dateTime2) cmwtime:getSpan ?resultTimeSpan.   ``` |
| **Возвращает** | `duration` |
| `cmwtime:addDuration` | |
| **Описание** | Добавляет к значению субъекта типа `dateTime` значение типа `duration`. |
| **Синтаксис** | ``` (?dateTime ?duration) cmwtime:addDuration ?value.   ``` |
| **Возвращает** | `dateTime` |
| `cmwtime:subDuration` | |
| **Описание** | Вычитает из значения субъекта типа `dateTime` значение типа `duration`. |
| **Синтаксис** | ``` (?dateTime ?duration) cmwtime:subDuration ?value.   ``` |
| **Возвращает** | `dateTime` |
| `cmwtime:endOfDay` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания дня, в пределах которого находится значение субъекта. |
| **Синтаксис** | ``` ?creationDateTime cmwtime:endOfDay ?endDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwtime:startOfDay` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала дня, в пределах которого находится значение субъекта. |
| **Синтаксис** | ``` ?creationDateTime cmwtime:startOfDay ?startDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwtime:startOfWeek` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала недели, в пределах которой находится значение субъекта. |
| **Синтаксис** | ``` ?creationDateTime cmwtime:startOfWeek ?startDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwtime:startOfMonth` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала месяца, в пределах которого находится значение субъекта. |
| **Синтаксис** | ``` ?creationDateTime cmwtime:startOfMonth ?startDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwtime:fromTzToTz` | |
| **Описание** | Перевод значения типа `dateTime` в заданный часовой пояс. |
| **Синтаксис** | ``` (?someDateTime "Etc/GMT" "Europe/Moscow") cmwtime:fromTzToTz ?tzDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwtime:timeZoneHours` | |
| **Описание** | Возвращает разницу во времени UTC и местным часовым поясом. |
| **Синтаксис** | ``` ? cmwtime:timeZoneHours ?timeZoneDifferenceInHours.   ``` |
| **Возвращает** | `integer` |
| `cmwtime:isToday` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и проверяет на текущую дату. |
| **Синтаксис** | ``` ?creationDate cmwtime:isToday ?today.   ``` |
| **Возвращает** | `bool` |
| `cmwtime:century` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее веку указанной даты в местном часовом поясе. |
| **Синтаксис** | ``` ?creationDate cmwtime:century ?numberCentury.   ``` |
| **Возвращает** | `number` |
| `cmwtime:isoFormat` | |
| **Описание** | Конвертирует значение типа `dateTime` в формат ISO. |
| **Синтаксис** | ``` ?creationDate cmwtime:isoFormat ?isoFormatDate.   ``` |
| **Возвращает** | `string` |
| `cmwtime:year` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее году указанной даты в местном часовом поясе. |
| **Синтаксис** | ``` ?creationDate cmwtime:year ?numberYear.   ``` |
| **Возвращает** | `number` |
| `cmwtime:month` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее месяцу указанной даты в местном часовом поясе. |
| **Синтаксис** | ``` ?creationDate cmwtime:month ?numberMonth.   ``` |
| **Возвращает** | `number` |
| `cmwtime:day` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее дню месяца указанной даты в местном часовом поясе. |
| **Синтаксис** | ``` ?creationDate cmwtime:day ?numberDay.   ``` |
| **Возвращает** | `number` |
| `cmwtime:hour` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее часу указанной даты в местном часовом поясе. |
| **Синтаксис** | ``` ?creationDate cmwtime:hour ?numberHour.   ``` |
| **Возвращает** | `number` |
| `cmwtime:minute` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее минуте указанной даты в местном часовом поясе. |
| **Синтаксис** | ``` ?creationDate cmwtime:minute ?numberMinute.   ``` |
| **Возвращает** | `number` |
| `cmwtime:second` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает числовое значение, соответствующее секундам указанной даты в местном часовом поясе. |
| **Синтаксис** | ``` ?creationDate cmwtime:second ?numberSecond.   ``` |
| **Возвращает** | `number` |
| `cmwtime:makeDate` | |
| **Описание** | Берёт значения субъекта типа число и возвращает объект типа `dateTime`. |
| **Синтаксис** | ``` (?intervalBeginYear ?intervalBeginMonth ?intervalBeginDay 23 59 59) cmwtime:makeDate ?brokenIntervalEnd.   ```  ``` (?intervalEndYear ?intervalEndMonth ?intervalEndDay 0 0 0) cmwtime:makeDate ?brokenIntervalBegin.   ```  ``` (?startDateYear ?startDateMonth ?startDateDay) cmwtime:makeDate ?startDayDate.   ```  ``` (?startDateYear ?startDateMonth ?startDateDay ?startDateHour ?startDateMinute ?startDateSecond) cmwtime:makeDate ?intervalBegin.   ``` |
| **Возвращает** | `dateTime` |
| `cmwtime:workhours` | |
| **Описание** | Возвращает дату и время на основании количества рабочих часов с определенного момента времени, с поправкой на праздники и фактические выходные дни. |
| **Синтаксис** | ``` (?startWorkDateTime ?qountWorkingHours ?startWorkingDay ?durationWorkingDay (?dateNotHoliday)) cmwtime:workhours ?newDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwtime:workdays` | |
| **Описание** | Возвращает дату на основании количества рабочих дней с определенной даты, с поправкой на праздники и фактические выходные дни. |
| **Синтаксис** | ``` (?startWorkDateTime ?qountWorkingHours (?firstDateNotHoliday ?secondDateNotWorking)) cmwtime:workdays ?newDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwtime:workhoursDuration` | |
| **Описание** | Возвращает продолжительность работы между двумя датами при условии, что рабочий день начинается в заданное время и имеет определенную длительность. |
| **Синтаксис** | ``` (?startWorkDateTime ?endWorkDateTime ?timeStartWorkingDay ?durationWorkingDay) cmwtime:workhoursDuration ?newDuration.   ``` |
| **Возвращает** | `duration` |
| `cmwtime:workdaysDuration` | |
| **Описание** | Возвращает продолжительность работы между двумя датами, на основании предположения, что рабочий день начинается в 00:00 и длится 24 часа. |
| **Синтаксис** | ``` (?startWorkDateTime ?endWorkDateTime) cmwtime:workdaysDuration ?newDuration.   ``` |
| **Возвращает** | `duration` |

### Функции для работы с интервалами времени `cmwduration`

| `@prefix cmwduration: <http://comindware.com/logics/duration#>.` | |
| --- | --- |
| `cmwduration:days` | |
| --- | --- |
| **Описание** | Берёт промежуток времени и возвращает количество дней. |
| **Синтаксис** | ``` ?durationHoliday cmwduration:days ?countDaysOfHoliday.   ``` |
| **Возвращает** | `number` |
| `cmwduration:hours` | |
| **Описание** | Берёт промежуток времени и возвращает количество часов. |
| **Синтаксис** | ``` ?durationHoliday cmwduration:hours ?countHoursOfHoliday.   ``` |
| **Возвращает** | `number` |
| `cmwduration:minutes` | |
| **Описание** | Берёт промежуток времени и возвращает количество минут. |
| **Синтаксис** | ``` ?durationHoliday cmwduration:minutes ?countMinutesOfHoliday.   ``` |
| **Возвращает** | `number` |

### Функции для работы со строками `w3string`

| `@prefix w3string: <http://www.w3.org/2000/10/swap/string#>.` | |
| --- | --- |
| `w3string:format` | |
| --- | --- |
| **Описание** | Подставляет аргументы в нумерованные заместители вида `{0}`…`{n}` в исходной строке и возвращает результирующую строку. |
| **Синтаксис** | ``` ("{0}/{1} - {2}" ?value0 ?value1 ?value2) w3string:format ?outString.   ``` |
| **Возвращает** | `string` |
| `w3string:matches` | |
| **Описание** | Использует в качестве аргументов строку и регулярное выражение. Возвращает логическое значение Истина, если какая-либо часть строки или строка полностью соответствует условию, заданному регулярным выражением. В противном случае возвращает результат Ложь. |
| **Синтаксис** | ``` ?stringExample w3string:matches ?expression.   ``` |
| **Возвращает** | `bool` |
| `w3string:notMatches` | |
| **Описание** | Использует в качестве аргументов строку и регулярное выражение. Возвращает логическое значение Истина, если часть строки или строка полностью не соответствуют условию, заданному регулярным выражением. В противном случае возвращает результат Ложь. |
| **Синтаксис** | ``` ?stringExample w3string:notMatches ?expression.   ``` |
| **Возвращает** | `bool` |
| `w3string:greaterThan` | |
| **Описание** | Возвращает логическое значение Истина, если аргумент2 больше аргумента1, в противном случае возвращает результат Ложь. |
| **Синтаксис** | ``` ?creationDate w3string:greaterThan ?chooseDate.   ``` |
| **Возвращает** | `bool` |
| `w3string:lessThan` | |
| **Описание** | Возвращает логическое значение Истина, если аргумент2 меньше аргумента1, в противном случае возвращает результат Ложь. |
| **Синтаксис** | ``` ?creationDate w3string:lessThan ?chooseDate.   ``` |
| **Возвращает** | `bool` |
| `w3string:notGreaterThan` | |
| **Описание** | Возвращает логическое значение Истина, если аргумент2 НЕ больше аргумента1, в противном случае возвращает результат Ложь. |
| **Синтаксис** | ``` ?creationDate w3string:notGreaterThan ?chooseDate.   ``` |
| **Возвращает** | `bool` |
| `w3string:notLessThan` | |
| **Описание** | Возвращает логическое значение Истина, если аргумент2 НЕ меньше аргумента1, в противном случае возвращает результат Ложь. |
| **Синтаксис** | ``` ?creationDate w3string:notLessThan ?chooseDate.   ``` |
| **Возвращает** | `bool` |

### Функции для работы со строками `cmwstring`

| `@prefix cmwstring: <http://comindware.com/logics/string#>.` | |
| --- | --- |
| `cmwstring:join` | |
| --- | --- |
| **Описание** | Объединяет строки с использованием заданного разделителя. |
| **Синтаксис** | ``` ("," ?newDependencyLinks) cmwstring:join ?newDependencyLinksStr.   ``` |
| **Возвращает** | `string` |
| `cmwstring:replace` | |
| **Описание** | Заменяет все экземпляры заданной строки в исходной строке на новое значение. |
| **Синтаксис** | ``` (?text "\\n" "<br>") cmwstring:replace ?html.   ``` |
| **Возвращает** | `string` |
| `cmwstring:cutString` | |
| **Описание** | Обрезает строку на заданную длину и добавляет в конец заданные символы. |
| **Синтаксис** | ``` (?taskTitleLong 50 "...") cmwstring:cutString ?taskTitle.   ``` |
| **Возвращает** | `string` |
| `cmwstring:firstCapital` | |
| **Описание** | Преобразует первый символ строки в прописной. |
| **Синтаксис** | ``` ?youStr cmwstring:firstCapital ?youStrCapital.   ``` |
| **Возвращает** | `string` |
| `cmwstring:concatenation` | |
| **Описание** | Конкатенация строк. |
| **Синтаксис** | ``` (?firstString ?secondString) cmwstring:concatenation ?newString.   ``` |
| **Возвращает** | `string` |
| `cmwstring:length` | |
| **Описание** | Возвращает количество символов в строке. |
| **Синтаксис** | ``` ?stringName cmwstring:length ?countSymbols.   ``` |
| **Возвращает** | `number` |
| `cmwstring:substring` | |
| **Описание** | Обрезает строку от заданной позиции на заданное количество символов (опционально). |
| **Синтаксис** | ``` (?sourceString 2 4) cmwstring:substring ?resultString.  (?sourceString 2) cmwstring:substring ?resultString.   ``` |
| **Возвращает** | `string` |
| `cmwstring:indexOf` | |
| **Описание** | Возвращает номер (отсчитываемый от нуля) позиции, на которой располагается искомая строка в исходной строке. Номер позиции может отсчитываться от произвольного положения (опционально). |
| **Синтаксис** | ``` (?sourceString ?subString) cmwstring:indexOf ?resultString.   ```  ``` (?sourceString ?subString 4) cmwstring:indexOf ?resultString.   ``` |
| **Возвращает** | `number` |
| `cmwstring:toUri` | |
| **Описание** | Преобразует escape-последовательности в URI. |
| **Синтаксис** | ``` ?sequence cmwstring:toUri ?reference.   ``` |
| **Возвращает** | `string` |
| `cmwstring:fromUri` | |
| **Описание** | Преобразует URI в escape-последовательности. |
| **Синтаксис** | ``` ?reference cmwstring:fromUri ?sequence.   ``` |
| **Возвращает** | `string` |
| `cmwstring:toBase64` | |
| **Описание** | Преобразует строку по стандарту кодирования Base64. |
| **Синтаксис** | ``` ?string cmwstring:toBase64 ?newStringBase.   ``` |
| **Возвращает** | `string` |
| `cmwstring:fromBase64` | |
| **Описание** | Декодирует строку по стандарту Base64. |
| **Синтаксис** | ``` ?stringBase cmwstring:fromBase64 ?newString.   ``` |
| **Возвращает** | `string` |
| `cmwstring:split` | |
| **Описание** | Находит заданный разделитель в строке и создает список. |
| **Синтаксис** | ``` ("_" ?string) cmwstring:split ?newString.   ``` |
| **Возвращает** | — |
| `cmwstring:format` | |
| **Описание** | Форматирует аргументы в соответствии с заданным шаблоном. Возвращает отформатированную строку. |
| **Синтаксис** | ``` ("{0}/{1} - {2}" ?v0 ?v1 ?v2) cmwstring:format ?outString.   ``` |
| **Возвращает** | `string` |

### Функции для работы со строками `cmwlogics`

| `@prefix cmwlogics: <http://comindware.com/logics#>.` | |
| --- | --- |
| `cmwlogics:value` | |
| --- | --- |
| **Описание** | Присваивает значение субъекта объекту. |
| **Синтаксис** | ``` ?left cmwlogics:value ?right.   ```  ``` {    time:now => ?left.    ?left cmwlogics:value ?right.    Result: ?right = dateTime.UtcNow.  }   ``` |
| **Возвращает** | `number` `dateTime` `string` `duration` `reference` `account` |

### Функции для работы со строками `cmwentity`

| `@prefix cmwentity: <http://comindware.com/ontology/entity#>.` | |
| --- | --- |
| `cmwentity:like` | |
| --- | --- |
| **Описание** | Сравнивает шаблон и строку. |
| **Синтаксис** | ``` ?pattern cmwentity:like ?sourceString.   ``` |
| **Возвращает** | `bool` |
| `cmwentity:startsWith` | |
| **Описание** | Проверяет, что заданная строка начинается в соответствии с шаблоном и (опционально) в соответствии с заданной опцией сравнения (StringComparison). |
| **Синтаксис** | ``` ?sourceString entity:startsWith ?pattern.   ```  ``` (?sourceString "OrdinalIgnoreCase") entity:startsWith ?pattern.   ``` |
| **Возвращает** | `bool` |
| `cmwentity:endsWith` | |
| **Описание** | Проверяет, что заданная строка заканчивается в соответствии с шаблоном и (опционально) в соответствии с заданной опцией сравнения (StringComparison). |
| **Синтаксис** | ``` ?sourceString entity:endsWith ?pattern.   ```  ``` (?sourceString "OrdinalIgnoreCase") entity:endsWith ?pattern.   ``` |
| **Возвращает** | `bool` |
| `cmwentity:indexOf` | |
| **Описание** | Возвращает индекс первого вхождения подстроки в строку. Отсчет начинается с 1. |
| **Синтаксис** | ``` (?sourceString ?substring) entity:indexOf ?index.   ``` |
| **Возвращает** | `number` |
| `cmwentity:toLower` | |
| **Описание** | Преобразует все символы строки в строчные. |
| **Синтаксис** | ``` ?string entity:toLower ?stringLow.   ``` |
| **Возвращает** | `string` |
| `cmwentity:toUpper` | |
| **Описание** | Преобразует все символы строки в прописные. |
| **Синтаксис** | ``` ?string entity:toUpper ?stringUpper.   ``` |
| **Возвращает** | `string` |
| `cmwentity:contains` | |
| **Описание** | Проверяет вхождение значения объекта типа `string` в значение субъекта типа `string`. |
| **Синтаксис** | ``` ?string entity:contains ?subString.   ``` |
| **Возвращает** | `string` |

### Функции для работы со строками `cmwbuiltin`

| `@prefix cmwbuiltin: <http://comindware.com/ontology/image/builtin#>.` | |
| --- | --- |
| `cmwbuiltin:toPlainText` | |
| --- | --- |
| **Описание** | Конвертирует HTML-текст в обычный. |
| **Синтаксис** | ``` ?htmlText builtin:toPlainText ?plainText.   ``` |
| **Возвращает** | `string` |

### Функции для работы со списками `w3list`

| `@prefix w3list: <http://www.w3.org/2000/10/swap/list#>.` | |
| --- | --- |
| `w3list:append` | |
| --- | --- |
| **Описание** | Добавляет элементы к списку |
| **Синтаксис** | ``` ((1 2) (3 4)) w3list:append ?resultingList1234.   ``` |
| **Возвращает** | `list` |
| `w3list:in` | |
| **Описание** | Если объект — список, и в нём есть субъект, возвращает `true` |
| **Синтаксис** | ``` ?subjectToFind w3list:in ?list.   ``` |
| **Возвращает** | `bool` |
| `w3list:last` | |
| **Описание** | Из представленной последовательности получает последний элемент. |
| **Синтаксис** | ``` ?listFlowers w3list:last ?lastFlower.   ``` |
| **Возвращает** | `string` |
| `w3list:member` | |
| **Описание** | - Если субъект — список, и в нём есть объект, возвращает `true`. - Если субъект — список, а объект не задан, возвращает итератор по элементам списка. |
| **Синтаксис** | ``` ?list w3list:member ?objectToFind.   ```  ``` ?list w3list:member ?listElements.   ``` |
| **Возвращает** | `bool`, `iterator` |
|

### Функции для работы со списками `cmwlist`

`@prefix cmwlist: <http://comindware.com/logics/list#>.` | || `cmwlist:length` | |
| --- | --- |
| **Описание** | Возвращает количество элементов последовательности. |
| **Синтаксис** | ``` ?listFlowers cmwlist:length ?countFlowers.   ``` |
| **Возвращает** | `number` |
| `cmwlist:at` | |
| **Описание** | Берёт список элементов и задает индекс. Возвращает значение элемента, соответствующее индексу. `([23, 25, 12] 2)` возвращает `12`. |
| **Синтаксис** | ``` (?list ?index) cmwlist:at ?valueOfIndex.   ``` |
| **Возвращает** | `string` |

### Функции группировки и сортировки списков `cmwentity`

| `@prefix cmwentity: <http://comindware.com/ontology/entity#>.` | |
| --- | --- |
| `cmwentity:groupby` | |
| --- | --- |
| **Описание** | Группировка |
| **Синтаксис** | ``` (?recordTemplate ?dataSet) entity:groupby ?attributeGroup.   ```  Входные данные:  ``` (("key1_1" "key2_1" "value1_1") ("key1_2" "key2_2" "value1_2") ("key1_3" "key2_3" "value1_3"))   ```  Результат: ```  (("value1_2") ("value1_1") ("value1_3"))   ``` |
| **Возвращает** | `list` |
| `cmwentity:sortby` | |
| **Описание** | Сортировка |
| **Синтаксис** | ``` (?recordTemplate ?dataSet) entity:sortby ?attributeGroup.   ```  Входные данные:  ``` (("key1_1" "key2_1" "value1_1") ("key1_2" "key2_2" "value1_2") ("key1_3" "key2_3" "value1_3"))   ```  Результат: ```  (("value1_2") ("value1_1") ("value1_3"))   ``` |
| **Возвращает** | `list` |

### Функции логических выражений и логики `cmwassert`

| `@prefix cmwassert: <http://comindware.com/logics/assert#>.` | |
| --- | --- |
| `cmwassert:true` | |
| --- | --- |
| **Описание** | Объявляет логическое значение `true` |
| **Синтаксис** | ``` true   ``` |
| **Возвращает** | `boolean` |
| `cmwassert:false` | |
| **Описание** | Объявляет логическое значение `false` |
| **Синтаксис** | ``` false   ``` |
| **Возвращает** | `boolean` |
| `cmwassert:or` | |
| **Описание** | Оператор `ИЛИ` |
| **Синтаксис** | ``` or {} or {} … or {}.   ``` |
| **Возвращает** | `boolean` |
| `cmwassert:if` | |
| **Описание** | Условный оператор |
| **Синтаксис** | ``` if {} then {} else {}.   ``` |
| **Возвращает** | `boolean` |
| `cmwassert:count` | |
| **Описание** | Выводит количество записей, удовлетворяющих условиям. |
| **Синтаксис** | ``` {} assert:count ?c.   ``` |
| **Возвращает** | `number` |
| `cmwassert:union` | |
| **Описание** | Объединяет итераторы в один. |
| **Синтаксис** | ``` ({} … {}) assert:union true.   ``` |
| **Возвращает** | `list` |
| `cmwassert:distinct` | |
| **Описание** | Выбирает уникальные записи из связанных наборов данных. |
| **Синтаксис** | ``` {  ?item ?Positions ?PositionsVal.  ?PositionsVal ?Items ?ItemsVal.  } assert:distinct ?ItemsVal.   ``` |
| **Возвращает** | `list` |
| `cmwassert:sort` | |
| **Описание** | Сортирует элементы по заданному критерию. |
| **Синтаксис** | ``` @in ?historyRecord1, ?historyRecord2.  @out ?result.  {    ?historyRecord1 history:recordDate ?recordDate1.    ?historyRecord2 history:recordDate ?recordDate2.    (?recordDate1 ?recordDate2) sort:timeComparer ?result.  } => { (?historyRecord1 ?historyRecord2) notification:sortHistoryRecords ?result }.    {    from {      ?actualHistoryRecord history:recordOfSubjectHistory ?subject.      ?actualHistoryRecord history:recordDate ?actualHistoryDate.      ?actualHistoryDate math:notLessThan ?oldestHistoryDate.      ?actualHistoryDate math:notGreaterThan ?newestHistoryDate.    } select ?actualHistoryRecord -> ?actualHistoryRecords.    (?actualHistoryRecords notification:sortHistoryRecords) assert:sort ?actualHistoryRecordsSorted.  }   ``` |
| **Возвращает** | `list` |
| `cmwassert:once` | |
| **Описание** | Выходит после первой успешной итерации |
| **Синтаксис** | ``` once {}.   ``` |
| **Возвращает** | — |

### Функции для работы с идентификаторами ресурсов `cmwurl`

| `@prefix cmwurl: <http://comindware.com/logics/url#>.` | |
| --- | --- |
| `cmwurl:encode` | |
| --- | --- |
| **Описание** | Кодирует строку URL-адреса. Аналог `System.Web.HttpUtility.UrlEncode(url)` |
| **Синтаксис** | ``` ?url cmwurl:encode ?encodedUrl.   ``` |
| **Возвращает** | `string` |
| `cmwurl:combine` | |
| **Описание** | Объединяет части предоставления списка строк пути в путь одной строкой. Аналог `System.IO.Path.Combine` |
| **Синтаксис** | ``` (?path1 ?path2 ?path3 ...) cmwurl:combine ?combinedPath.   ``` |
| **Возвращает** | `string` |
| `cmwurl:siteDir` | |
| **Описание** | Получает текущую директорию нахождения проекта. |
| **Синтаксис** | ``` ?unused cmwurl:siteDir ?siteDir.   ``` |
| **Возвращает** | `string` |

### Функции для работы с идентификаторами ресурсов `cmwui`

| `@prefix cmwui: <http://comindware.com/ontology/ui#>.` | |
| --- | --- |
| `cmwui:toClientString` | |
| --- | --- |
| **Описание** | Получает строковое представление ресурса (элемента или атрибута). |
| **Синтаксис** | ``` ?object cmwui:toClientString ?string.   ``` |
| **Возвращает** | `string` |
| `cmwui:toQName` | |
| **Описание** | Преобразует строковое представление ресурса в QName. |
| **Синтаксис** | ``` ?object cmwui:toQName ?qName.   ``` |
| **Возвращает** | `string` |

### Функции поддерживающие и корректно обрабатывающие нулевые значения `cmwnullable`

| `@prefix cmwnullable <http://comindware.com/ontology/entity/nullable#>.` | |
| --- | --- |
| `cmwnullable:lessThan` | |
| --- | --- |
| **Описание** | Меньше чем. (`dateTime` , `date` , `duration` , `string` , `number`). Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?recordDate cmwnullable:lessThan ?maxDate.   ``` |
| **Возвращает** | `bool` |
| `cmwnullable:greaterThan` | |
| **Описание** | Больше чем (`dateTime` , `date` , `duration` , `string` , `number`). Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?recordDate cmwnullable:greaterThan ?minDate.   ``` |
| **Возвращает** | `bool` |
| `cmwnullable:notLessThan` | |
| **Описание** | Не меньше (`dateTime` , `date` , `duration` , `string` , `number`). Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?documentRecordsCount cmwnullable:notLessThan 2.   ``` |
| **Возвращает** | `bool` |
| `cmwnullable:notGreaterThan` | |
| **Описание** | Не больше (`dateTime` , `date` , `duration` , `string` , `number`). Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?documentRecordsCount cmwnullable:notGreaterThan 2.   ``` |
| **Возвращает** | `bool` |
| `cmwnullable:quotient` | |
| **Описание** | Берёт 2 аргумента в скобках, указанные в субъекте и результат деления первого на второе помещает в переменную объекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` (?WorkInSeconds ?WorkDaysInSeconds) cmwnullable:quotient ?WorkSeconds.   ``` |
| **Возвращает** | `number` |
| `cmwnullable:product` | |
| **Описание** | Берёт 2 аргумента в скобках, указанные в субъекте и результат их умножения помещает в переменную объекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` (?productingWorkInSeconds ?productingWorkDaysInSeconds) cmwnullable:product ?productingWorkSeconds.   ``` |
| **Возвращает** | `number` |
| `cmwnullable:integerQuotient` | |
| **Описание** | Берёт 2 аргумента в скобках, указанные в субъекте и результат целочисленного деления первого на второе помещает в переменную объекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` (?WorkInSeconds ?WorkDaysInSeconds) cmwnullable:integerQuotient ?WorkSeconds.   ``` |
| **Возвращает** | `number` |
| `cmwnullable:remainder` | |
| **Описание** | Берёт 2 аргумента в скобках, указанные в субъекте и остаток от деления первого на второе помещает в переменную объекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` (?remainingWorkInSeconds ?remainingWorkDaysInSeconds) cmwnullable:remainder ?remainingWorkSeconds.   ``` |
| **Возвращает** | `number` |
| `cmwnullable:sum` | |
| **Описание** | Берёт сумму из субъекта типа `List` и записывает значение в объект. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?durationsSeconds cmwnullable:sum ?durationSumSeconds.   ``` |
| **Возвращает** | `number` |
| `cmwnullable:difference` | |
| **Описание** | Берёт разность из субъекта типа `List` и записывает значение в объект. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?list cmwnullable:difference ?differenceTotal.   ``` |
| **Возвращает** | `number` |
| `cmwnullable:startOfDay` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала дня, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?creationDateTime cmwnullable:startOfDay ?startDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwnullable:startOfWeek` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала недели, в пределах которой находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?creationDateTime cmwnullable:startOfWeek ?startDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwnullable:startOfMonth` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала месяца, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?creationDateTime cmwnullable:startOfMonth ?startDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwnullable:startOfQuarter` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала квартала, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?creationDateTime cmwnullable:startOfQuarter ?startDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwnullable:startOfYear` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время начала месяца, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?creationDateTime cmwnullable:startOfYear ?startDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwnullable:endOfDay` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания дня, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?creationDateTime cmwnullable:endOfDay ?endDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwnullable:endOfWeek` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания недели, в пределах которой находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?creationDateTime cmwnullable:endOfWeek ?endDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwnullable:endOfMonth` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания месяца, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?creationDateTime cmwnullable:endOfMonth ?endDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwnullable:endOfQuarter` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания квартала, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?creationDateTime cmwnullable:endOfQuarter ?endDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwnullable:endOfYear` | |
| **Описание** | Берёт значение из субъекта типа `dateTime` и возвращает дату и время окончания года, в пределах которого находится значение субъекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?creationDateTime cmwnullable:endOfYear ?endDateTime.   ``` |
| **Возвращает** | `dateTime` |
| `cmwnullable:inSeconds` | |
| **Описание** | Конвертирует значение длительности в количество секунд. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?durationWorkingDay cmwnullable:inSeconds ?secondsWorkingDay.   ``` |
| **Возвращает** | `number` |
| `cmwnullable:min` | |
| **Описание** | Берёт минимальное значение из субъекта типа `List` и записывает значение в объект. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?listQueue cmwnullable:min ?queueMin.   ``` |
| **Возвращает** | `number` `dateTime` `date` `duration` |
| `cmwnullable:max` | |
| **Описание** | Берёт максимальное значение из субъекта типа `List` и записывает значение в объект. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?listQueue cmwnullable:max ?queueMax.   ``` |
| **Возвращает** | `number` `dateTime` `date` `duration` |
| `cmwnullable:average` | |
| **Описание** | Берёт 2 аргумента в скобках, указанные в субъекте и помещает их среднее арифметическое в переменную объекта. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` (?priceFirst ?priceSecond) cmwnullable:average ?priceAverage.   ``` |
| **Возвращает** | `number` |
| `cmwnullable:toDuration` | |
| **Описание** | Конвертирует количество секунд в значение типа `duration`. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?secondsWorkingDay cmwnullable:toDuration ?durationWorkingDay.   ``` |
| **Возвращает** | `duration` |
| `cmwnullable:round` | |
| **Описание** | Округление к ближайшему целому. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?quotientPrice cmwnullable:round ?numberRound.   ``` |
| **Возвращает** | `number` |
| `cmwnullable:floor` | |
| **Описание** | Округление в меньшую сторону. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?quotientPrice cmwnullable:floor ?numberFloor.   ``` |
| **Возвращает** | `number` |
| `cmwnullable:ceiling` | |
| **Описание** | Округление в большую сторону. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ?quotientPrice cmwnullable:ceiling ?numberCeil.   ``` |
| **Возвращает** | `number` |
| `cmwnullable:format` | |
| **Описание** | Форматирует аргументы в соответствии с заданным шаблоном. Возвращает отформатированную строку. Если в субъекте нулевое значение, возвращает нулевое значение. |
| **Синтаксис** | ``` ("{0}/{1} - {2}" ?v0 ?v1 ?v2) cmwnullable:format ?outString.   ``` |
| **Возвращает** | `string` |

### Функции для работы с изображениями `cmwbuiltin`

| `@prefix cmwbuiltin: <http://comindware.com/ontology/image/builtin#>.` | |
| --- | --- |
| `cmwbuiltin:isSupportedImage` | |
| --- | --- |
| **Описание** | Проверяет формат файла на соответствие одному из допустимых форматов: `.bmp, .gif, .exif, .jpg, .jpeg, .png, .tif` |
| **Синтаксис** | ``` "bllalblablab.jpg" => ?fileName.  ?fileName builtin:isSupportedImage ?right.   ``` |
| **Возвращает** | `bool` |
| `cmwbuiltin:dimensions` | |
| **Описание** | По `streamId` изображения получает разрешение в формате ширина × высота. |
| **Синтаксис** | ``` ?streamId builtin:dimensions ?dimensions.   ``` |
| **Возвращает** | `string` |

### Специальные функции для работы с аккаунтами и группами `cmwlogics`

| `@prefix cmwlogics: <http://comindware.com/logics#>.` | |
| --- | --- |
| `cmwlogics:currentUser` | |
| --- | --- |
| **Описание** | Предикат, получающий аккаунт текущего пользователя. |
| **Синтаксис** | ``` cmwlogics:securityContext cmwlogics:currentUser ?userVal.   ``` |
| **Возвращает** | — |
| `cmwlogics:securityContext` | |
| **Описание** | Субъект, определяющий контекст персонального пространства. |
| **Синтаксис** | ``` cmwlogics:securityContext cmwlogics:currentUser ?userVal.   ``` |
| **Возвращает** | — |

### Специальные функции для работы с аккаунтами и группами `cmwaccount`

| `@prefix cmwaccount: <http://comindware.com/ontology/account#>.` | |
| --- | --- |
| `cmwaccount:Group` | |
| --- | --- |
| **Описание** | Определяет тип переменной Группа. |
| **Синтаксис** | ``` ?group rdf:type cmwaccount:Group.   ``` |
| **Возвращает** | — |
| `cmwaccount:groupName` | |
| **Описание** | Предикат для получения наименования группы. |
| **Синтаксис** | ``` ?group cmwaccount:groupName ?groupName.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:isSystemAdministrator` | |
| **Описание** | Предикат для определения принадлежности аккаунта к системной роли «Системные администраторы» |
| **Синтаксис** | ``` ?user cmwaccount:isSystemAdministrator ?access.   ``` |
| **Возвращает** | `bool` |
| `cmwaccount:displayName` | |
| **Описание** | Предикат, для получения полного имени аккаунта |
| **Синтаксис** | ``` ?user cmwaccount:displayName ?userDisplayName.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:fullName` | |
| **Описание** | Предикат для получения Ф. И. О. аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:fullName ?userNameSurname.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:manager` | |
| **Описание** | Предикат для получения аккаунта руководителя, указанного для аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:manager ?userManager.   ``` |
| **Возвращает** | `accountProperty` |
| `cmwaccount:mbox` | |
| **Описание** | Предикат для получения адреса эл. почты аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:mbox ?userEmail.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:phone` | |
| **Описание** | Предикат для получения номера телефона аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:phone ?userMobile.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:instantMessagingId` | |
| **Описание** | Предикат для получения идентификатора аккаунта в мессенджере. |
| **Синтаксис** | ``` account:instantMessagingId   ``` |
| **Возвращает** | `string` |
| `cmwaccount:status` | |
| **Описание** | Предикат для получения статуса аккаунта: `true` — включён. |
| **Синтаксис** | ``` ?user cmwaccount:status ? enabled.   ``` |
| **Возвращает** | `bool` |
| `cmwaccount:skype` | |
| **Описание** | Предикат для получения идентификатора аккаунта в Skype. |
| **Синтаксис** | ``` ?user cmwaccount:skype ?loginSkype.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:username` | |
| **Описание** | Предикат для получения имени пользователя (логина) аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:username ?login.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:active` | |
| **Описание** | Предикат для получения состояния аккаунта: `true` — включён. |
| **Синтаксис** | ``` ?user cmwaccount:active ? enabled.   ``` |
| **Возвращает** | `bool` |
| `cmwaccount:lastLoginDate` | |
| **Описание** | Предикат для получения даты последней авторизации аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:lastLoginDate ?lastLoginDate.   ``` |
| **Возвращает** | `dateTime` |
| `cmwaccount:language` | |
| **Описание** | Предикат для получения кода языка отображения веб-сайта для аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:language ?userLanguage.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:sid` | |
| **Описание** | Предикат для получения Active Directory Security ID аккаунта. |
| **Синтаксис** | ``` ?user account:sid ?sid.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:notificationSettings` | |
| **Описание** | Предикат для получения параметров уведомлений аккаунта |
| **Синтаксис** | ``` ?user account:notificationSettings ?notificationConfig .   ``` |
| **Возвращает** | `multiValue` |
| `cmwaccount:password` | |
| **Описание** | Предикат для получения пароля к аккаунту. |
| **Синтаксис** | ``` ?user cmwaccount:password ?userPassword   ``` |
| **Возвращает** | `string` |
| `cmwaccount:userpic` | |
| **Описание** | Предикат для получения изображения профиля аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:userpic ?picture ..   ``` |
| **Возвращает** | `string` |
| `cmwaccount:userpicLarge` | |
| **Описание** | Предикат для получения увеличенного изображения профиля аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:userpicLarge ?picture.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:title` | |
| **Описание** | Предикат для получения наименования должности аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:title  ?jobTitle.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:department` | |
| **Описание** | Предикат для получения наименования отдела аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:department  ?departmentName.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:office` | |
| **Описание** | Предикат для получения наименования офиса аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:office  ?officeName.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:userGroupMembership` | |
| **Описание** | Предикат для получения списка групп, в которых состоит аккаунт. |
| **Синтаксис** | ``` ?user cmwaccount:userGroupMembership  ?groupList.   ``` |
| **Возвращает** | `multiValue groupProperty` |
| `cmwaccount:authenticationMethod` | |
| **Описание** | Предикат для получения способа аутентификации аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:authenticationMethod ?authMethod.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:substitute` | |
| **Описание** | Предикат для получения аккаунта заместителя, назначенного аккаунту. |
| **Синтаксис** | ``` ?user cmwaccount:substitute ?substituteAccount.   ``` |
| **Возвращает** | `accountProperty` |
| `cmwaccount:substituteDateFrom` | |
| **Описание** | Предикат для получения даты начала замещения аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:substituteDateFrom  ?subsitutionStart   ``` |
| **Возвращает** | `dateTime` |
| `cmwaccount:substituteDateTo` | |
| **Описание** | Предикат для получения даты окончания замещения аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:substituteDateTo  ?subsitutionEnd   ``` |
| **Возвращает** | `dateTime` |
| `cmwaccount:birthday` | |
| **Описание** | Предикат для получения дня рождения аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:birthday  ?birthday.   ``` |
| **Возвращает** | `dateTime` |
| `cmwaccount:personalCalendarId` | |
| **Описание** | Предикат для получения ID персонального календаря аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:personalCalendarId  ?calendarID.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:personalCalendarUri` | |
| **Описание** | Предикат для получения URI персонального календаря аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:personalCalendarUri  ?calendarURI.   ``` |
| **Возвращает** | `string` |
| `cmwaccount:presentedOnOrgchart` | |
| **Описание** | Предикат для получения статуса включения аккаунта в организационную структуру: `true` — включён. |
| **Синтаксис** | ``` ?user cmwaccount:presentedOnOrgchart ?onOrgChart.   ``` |
| **Возвращает** | `bool` |
| `cmwaccount:timeZone` | |
| **Описание** | Предикат для получения серверного часового пояса аккаунта. |
| **Синтаксис** | ``` ?user cmwaccount:timeZone ?userTimeZone.   ``` |
| **Возвращает** | `string` |

### Специальные функции `cmwobject`

| `@prefix cmwobject: <http://comindware.com/ontology/object#>.` | |
| --- | --- |
| `cmwobject:findProperty` | |
| --- | --- |
| **Описание** | Возвращает в объект ID атрибута по заданной в субъекте паре системных имён шаблона записи и атрибута. |
| **Синтаксис** | ``` ("templateClients" "attibuteClientCode") cmwobject:findProperty ?attibute.   ``` |
| **Возвращает** | `string` |

### Специальные функции `cmwcontext`

| `@prefix cmwcontext: <http://comindware.com/logics/session/context#>.` | |
| --- | --- |
| `cmwcontext:time` | |
| --- | --- |
| **Описание** | Возвращает текущее время сеанса. |
| **Синтаксис** | ``` cmwcontext:time   ``` |
| **Возвращает** | `dateTime` |
| `cmwcontext:timeZoneOffset` | |
| **Описание** | Возвращает смещение часового пояса сеанса. |
| **Синтаксис** | ``` cmwcontext:timeZoneOffset   ``` |
| **Возвращает** | `number` |
| `cmwcontext:origin` | |
| **Описание** | Возвращает объект, по которому был запущен сценарий. |
| **Синтаксис** | ``` cmwcontext:origin   ``` |
| **Возвращает** | — |
| `cmwcontext:variable` | |
| **Описание** | Возвращает переменную в контексте. |
| **Синтаксис** | ``` cmwcontext:variable   ``` |
| **Возвращает** | — |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
