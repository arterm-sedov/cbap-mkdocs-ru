# N-Triples

### Обзорный курс


## Содержание

##### Урок 1. Онтологии в реальном мире

##### Урок 2. Введение в графы

##### Урок 3. N-Triples —что это такое?

##### Урок 4. Comindware Elastic Data

##### Урок 5. Запросы N-Triples и как они работают

##### Урок 6. Использование N-Triples в платформе


## Онтологии в реальном мире

```
Владеет
```
```
❖ Окружающий мир состоит из объектов
❖ Объекты имеют различные характеристики
❖ Объекты связаны между собой и/или взаимодействуют
```

## Онтологии в реальном мире

```
Объект - это
```
```
Класс Яблоко Класс Человек
```
```
+ Цвет
+ Вкус
```
```
Яблоко 1
Яблоко 2
```
```
❖ Объекты представляются классами
❖ Классы имеют свойства
❖ Классы взаимодействуют между собой
❖ Классы имеют экземпляры
```

## Онтологии в реальном мире

##### ЗАДАНИЕ 1

##### Разложите на классы и их свойства предметы реального мира:

##### карандаши в пенале


## Введение в графы

##### Граф —это абстрактная фигура, состоящая из вершин и ребер, связывающих

##### вершины


## Введение в графы

```
Владеет
```
```
Человек Автомобиль
Владеет
```
```
Иван Иваныч
```
```
Является
```
```
Вольво
```
```
Владеет
```
```
Является
```

## Введение в графы

##### ЗАДАНИЕ 2

##### Создайте граф по предметам реального мира из предыдущего задания:

##### карандаши в пенале


## N-Triples

##### ❖ N-Triples является упрощенным текстовым представлением графов в

##### модели RDF (resource definition framework), рекомендованной

##### консорциумом всемирной паутины для описания данных и метаданных

##### ❖ Является частью концепции семантической паутины (предназначенной

##### для обработки машинами)

##### ❖ Является упрощенным подмножеством нотацийTurtle и Notation3,

##### представляющих модели RDF в компактном и удобном для чтения виде

```
Субъект Объект
```
```
Предикат
```

## N-Triples

```
<http:/uri/#Человек> <http:/uri/#владеет> <http:/uri/#Автомобиль>
<Иван Иваныч> <http:/uri/#является> <http:/uri/#Человек>
<Вольво> <http:/uri/#является> <http:/uri/#Автомобиль>
<Иван Иваныч> <http:/uri/#владеет> <Вольво>
```
```
Владеет
```
```
Человек Автомобиль
Владеет
```
```
Иван Иваныч
```
```
Является
```
```
Вольво
```
```
Владеет
```
```
Является
```

## N-Triples

##### ЗАДАНИЕ 3

##### Преобразуйте граф из предыдущего задания в набор триплетов:

##### карандаши в пенале


## Comindware Elastic Data

##### ❖ База данных представляет собой RDF граф в нотации N-Triple

##### ❖ Данные Comindware Elastic Data хранятся в виде набора триплетов

##### ❖ Системные метаданные хранятся в виде набора файлов с расширением

##### *.n

##### ❖ Прикладные метаданные и данные хранятся в единой базе данных в виде

##### набора файлов

##### ❖ Все ссылочные данные проиндексированы для выполнения быстрого

##### поиска


## Comindware Elastic Data

# User:Task class.
#
cmw:UserTask a cmw:Class, container:ItemClass, object:App;
cmw:parentClass s:Serializable;
cmw:isSystem true;
cmw:counterId true;
cmw:counterPrefix "";
container:alias "_UserTask";
cmw:classSystemType cmw:UserTask;
object:property
cmw:title,
cmw:assignee,
cmw:taskStatus,
cmw:endDate,
cmw:dueDate,
task:objectId,
cmw:possibleAssignee,
cmw:isReassignProhibited,
cmw:startDate;
cmw:property
cmw:estimatedWork,
cmw:percentComplete,
cmw:isFollowed,
cmw:isRecurrent,
cmw:completionDate,
cmw:completedBy.

```
cmw:assignee a object:Property.
cmw:assignee cmw:propertyName
<http://comindware.com/text/cmw/platform/task#assignee>.
cmw:assignee cmw:propertyDescription
<http://comindware.com/text/cmw/platform/task/assignee#description>.
cmw:assignee cmw:propertyType cmw:accountProperty.
cmw:assignee s:serializer s:asQName.
cmw:assignee object:alias "assignee".
@in ?task.
{
@from
{
?task cmw:allChildren ?child.
not {? cmw:parent ?child }.
not { ?child cmw:taskStatus taskStatus:completed }.
if-not { ?child cmw:remainingWork ?work }
then { "P0D"^^xsd:duration -> ?work. }.
}
@select ?work -> ?works.
?works cmwmath:sum ?estimatedWork.
if { ?estimatedWork == null }
then { "P0D"^^xsd:duration -> ?result. }
else { ?estimatedWork -> ?result. }.
} => { ?task cmw:estimatedWork ?result }.
```

## Comindware Elastic Data

#
# account:Account class.
#
account:Account a cmw:Class, cmw:Prototype, object:App;
cmw:isSystem true;
cmw:className "Account";
container:alias "_Account";
cmw:counterId true;
cmw:counterPrefix "account";
cmw:prototypeName
<http://comindware.com/text/cmw/platform/account#prototypeName>;
cmw:prototypeClass account:Account;
cmw:classSystemType account:Account;
object:property
account:username,
account:active,
account:fullName,
account:manager,
account:mbox,
account:phone,
account:skype,
account:title,
account:department,
account:language,
account:office.

```
account:username a object:Property, cmw:Property;
cmw:propertyType xsd:string;
cmw:propertyName
<http://comindware.com/text/cmw/platform/account#username>;
cmw:propertyDescription
<http://comindware.com/text/cmw/platform/account/username#description>;
cmw:propertyAttributes cmw:unique;
object:alias "username".
account:displayName a cmw:Property;
cmw:propertyType xsd:string.
in ?account.
{
once
{
?account a account:Account.
or { ?account account:fullName ?name1. ?name1 -> ?name}
or { ?account account:username ?name2. ?name2 -> ?name}
}
} => { ?account account:displayName ?name. }.
account:Account ui:displayNamePredicate account:displayName.
```

## Запросы N-Triples

###### ❖ # —комментарий

###### ❖ a —принадлежность субъекта к объекту

###### ❖ - > —присваивание значения

###### ❖ @prefix —объявление префиксов built-in пакетов

###### ❖? —объявление переменных

###### ❖. —терминатор триплета

###### ❖ {} —объявление формулы

###### ❖ () —объявление списка

###### ❖ [] – неявное использование субъекта


## Запросы N-Triples

##### ❖ Запросы пишутся аналогично фактам в виде набора триплетов

##### ❖ У запроса есть входные (в некоторых случаях) и выходные данные

##### ❖ Запрос выполняется последовательно сверху вниз по каждому триплету

##### ❖ Если запрос ничего не вернул, то это считается пустым результатом

##### ❖ Ризонер (Reasoner) -специальный механизм, выполняющий запросы

###### in ?item.

###### {

###### #наш код

###### } => { ?item attribute:value ?value. }.


##### Существует 4 вида запросов

## Запросы N-Triples

###### субъект предикат? Поиск объекта по заданному предикату и субъекту

###### ? предикат объект Поиск субъекта по заданному предикату и объекту

###### субъект предикат объект Проверка наличия факта по заданным аргументам

###### ? предикат? Поиск субъекта и объекта по заданному предикату


## Запросы N-Triples

```
?accounts a account:Account.
?accounts account:username "ivanov_ii".
?accounts -> ?value.
```
```
?accounts account:Account
```
```
a
```
```
Создается
нумератор по всем
пользователям
```
```
Следующий триплет
```
```
?accounts “ivanov_ii”
```
```
account:username
```
```
Пользователь 1
```
```
Следующий триплет
```
```
?accounts ?value
```
**- >**

```
Выходной
параметр
```
```
Поиск факта
```
```
Следующий
пользователь
```

```
Сравним с искомым литералом
```
## Запросы N-Triples

#### ?tasks a cmw:UserTask.

#### (

#### {?tasks cmw:possibleAssignee ?accounts.}

#### {?tasks cmw:assignee ?accounts.}

#### ) assert:union true.

#### ?accounts account:username "ivanov_ii".

#### ?tasks -> ?value.

```
Получим все задачи на исполнение
```
```
Получим всех исполнителей задачи,
включая назначенных
```
```
Id задачи в выходной параметр
```

## Запросы N-Triples

**Полезные конструкции и встроенные функции**

```
❖ ("tempAlias""attrAlias") object:findProperty ?p - возвращает ID атрибута
```
```
❖ once {}. - выходит после первой успешной итерации
```
```
❖ or {} or {} ... or {}. - оператор логическое ИЛИ
```
```
❖ if {} then {} else {}. - условный оператор
```
```
❖ from {} select ?v -> ?vList. - получение типа Список
```
```
❖ ?list math:sum ?sum. - получение суммы
```
```
❖ {} assert:count ?c. - выводит количество записей
```
```
❖ ({} ... {}) assert:union true. - объединение итераторов в один
```

## Запросы N-Triples

```
@prefix object: <http://comindware.com/ontology/object#>.
{
("currentTemplate" "Region") object:findProperty ?Region.
("Biznesstruktura" "Region") object:findProperty ?Region2.
```
```
once {
?item ?Region ?RegionVal.
?check ?Region2 ?RegionVal.
}.
true -> ?value.
}
```
#### Примеры (once)


## Запросы N-Triples

```
@prefix cmw: <http://comindware.com/logics#>.
{
cmw:securityContext cmw:currentUser ?user. #получим текущего пользователя
?tasks a cmw:UserTask.
```
```
or {?tasks cmw:possibleAssignee ?user.}
or {?tasks cmw:assignee ?user.}.
```
```
?tasks -> ?value.
}
```
#### Примеры (or)


## Запросы N-Triples

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
#### Примеры (if)


## Запросы N-Triples

```
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
@prefix object: <http://comindware.com/ontology/object#>.
{
("Nakladnaya" "PoziciiNakladnoy") object:findProperty ?Positions.
("PoziciiNakladnoy" "Summa") object:findProperty ?Summa.
```
```
from {
?item ?Positions ?PositionsVal.
??PositionsVal ?Summa ?SummaVal.
} select ?SummaVal -> ?SummaList.
?SummaList math:sum ?value.
}
```
#### Примеры (from, sum)


## Запросы N-Triples

```
@prefix object: <http://comindware.com/ontology/object#>.
@prefix assert: <http://comindware.com/logics/assert#>.
{
("Nakladnaya" "PoziciiNakladnoy") object:findProperty ?Positions.
```
```
{
?item ?Positions ?PositionsVal.
} assert:count ?value.
}
```
#### Примеры (count)


## Запросы N-Triples

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
#### Примеры (distinct)


## Запросы N-Triples

```
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix object: <http://comindware.com/ontology/object#>.
{
("Nakladnaya" "Gruzootpravitel") object:findProperty ?ShippedBy.
("Nakladnaya" "Poluchatel") object:findProperty ?Receiver.
```
```
(
{?item ?ShippedBy ?Contractor.}
{?item ?Receiver ?Contractor.}
) assert:union true.
?Contractor -> ?value.
}
```
#### Примеры (union)


## Запросы N-Triples

##### ЗАДАНИЕ 4

##### Напишите запрос по сравнению двух атрибутов с множественными данными,

##### который возвращает true, если все значения одного атрибута полностью

##### совпадают со всеми значениями второго атрибута

##### Исходные данные:

- Шаблон записи: **test**
- Атрибут 1: **attr1**
- Атрибут 2: **attr2**
- Выходной параметр: **?value**


## Запросы N-Triples

##### ЗАДАНИЕ 4 Решение

@prefix object: <http://comindware.com/ontology/object#>.

{

```
("test" "attr1") object:findProperty ?attr1.
("test" "attr2") object:findProperty ?attr2.
```
```
?item ?attr1 ?attr1Val.
?item ?attr2 ?attr2Val.
```
```
if {?attr1Val == ?attr2Val.}
then {true -> ?value.}
else {false -> ?value.}
```
}

```
1 итерация attr1 = 1 и attr2 = 1
```
```
attr1 = (1,3)
attr2 = (1,2,3)
```

## Запросы N-Triples

##### ЗАДАНИЕ 4 Решение

@prefix object: <http://comindware.com/ontology/object#>.

{

```
("test" "attr1") object:findProperty ?attr1.
("test" "attr2") object:findProperty ?attr2.
```
```
?item ?attr1 ?attr1Val.
?item ?attr2 ?attr2Val.
```
```
if {?attr1Val == ?attr2Val.}
then {true -> ?value.}
else {false -> ?value.}
```
}

```
последняя итерация attr1 = 3 и attr2 = 3
```
```
attr1 = (1,3)
attr2 = (1,2,3)
```

## Запросы N-Triples

##### ЗАДАНИЕ 4 Решение

@prefix assert: <http://comindware.com/logics/assert#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
{
("test" "attr1") object:findProperty ?attr1.
("test" "attr2") object:findProperty ?attr2.
from {
?item ?attr1 ?attr1Val.
} select ?attr1Val -> ?attr1ValList.
(?attr1ValList sort:stringComparer) assert:sort ?attr1ValListSort.
(" " ?attr1ValListSort) cmwstring:join ?attr1ValListSortStr.
...
if {?attr1ValListSortStr == ?attr2ValListSortStr}
} ?value -> fhsjhd

```
Получить список
```
```
Отсортировать список
Сформировать строку
Выполнить аналогичное действие для attr2
Сравнить полученные строки
```

## Запросы N-Triples

##### ЗАДАНИЕ 5

##### Написать запрос, который показывает количество уникальных контрагентов,

##### указанных в накладной.

##### Исходные данные:

- Шаблон записи: **Nakladnaya**
- Атрибуты-контрагенты: **Platelschik** , **Gruzopoluchatel** , **Zakazchik**
- Выходной параметр: **?value**


## Запросы N-Triples

##### ЗАДАНИЕ 5 Решение

@prefix assert: <http://comindware.com/logics/assert#>.
@prefix object: <http://comindware.com/ontology/object#>.
{
("Nakladnaya" "Platelschik") object:findProperty ?Platelschik.
("Nakladnaya" "Gruzopoluchatel") object:findProperty ?Gruzopoluchatel.
("Nakladnaya" "Zakazchik") object:findProperty ?Zakazchik.
{
{
(
{?item ?Platelschik ?Contractors.}
{?item ?Gruzopoluchatel ?Contractors.}
{?item ?Zakazchik ?Contractors.}
) assert:union true.
} assert:distinct ?Contractors.
} assert:count ?value.
}


## Использование N-Triples в платформе

#### Параметры на входе и выходе

```
Раздел Вход Выход
```
```
Атрибут → Вычисляемое
значение
```
```
?item-текущая запись (id) ?value—значение атрибута
```
```
Таблица → Системный
фильтр
```
- ?item—записи для вывода в
    таблице(id)

```
Кнопка → Условие
отображения
```
```
?item -текущая запись (id) ?value-true или false
```
```
Форма → Фильтр на поле ?item -текущая запись (id) ?value–искомые записи (id)
```

## Использование N-Triples в платформе

#### Параметры на входе и выходе

```
Раздел Вход Выход
```
```
Роль → Разрешения →
Шаблон записи, аккаунта,
процесса → Условие
применения
```
```
?item -текущая запись (id)
```
```
?value – true(строка
разрешений применяется) или
false(не применяется)
```
```
Роль → Разрешения →
Шаблон записи, аккаунта,
процесса → Фильтр аккаунтов
(Переназначение)
```
```
?value-текущий аккаунт(id) ?item–список аккаунтов(id)
```

## Использование N-Triples в платформе

#### Параметры на входе и выходе

```
Раздел Вход Выход
```
```
Правила для формы →
Вычисляемое значение для
действия
```
```
?item-текущая запись (id) ?value—значение атрибута
```
```
Правила для формы →
Правило → Условие
выполнения
```
```
?item-текущая запись (id)
```
```
?value—true (правило
сработает), false или пусто (не
сработает)
```
```
Правила для формы →
Действие → Условие
выполнения
```
```
?item-текущая запись (id)
```
```
?value-true (действие
сработает), false или пусто (не
сработает)
```

## Использование N-Triples в платформе

#### Параметры на входе и выходе

```
Раздел Вход Выход
```
```
Сценарий → Смена контекста
→ Вычисление набора
объектов
```
```
?item-текущая запись (id) ?value—запись для перехода
```
```
Сценарий → Дублирование
записи → Вычисление набора
объектов
```
```
?item-текущая запись (id) ?value—записи для
дублирования
```

## Использование N-Triples в платформе

#### Параметры на входе и выходе

```
Раздел Вход Выход
```
```
Сценарий → Проверка
результата выражения →
Выражение для проверки
```
```
?item-текущая запись (id)
```
```
?value-true (проверка
пройдена), false или пусто
(проверка не пройдена)
```
```
Сценарий → Изменение
значений атрибутов →
Вычисление значения
```
```
?item-текущая запись (id) ?value—значение атрибута
```
```
Сценарий → Изменение
значений переменных →
Вычисление значения
```
```
?item-текущая запись (id)
```
```
?value—значение
переменной
```

## Использование N-Triples в платформе

#### Параметры на входе и выходе

```
Раздел Вход Выход
```
```
Сценарий → Повтор по
числовому счётчику →
Количество итераций
```
```
?item-текущая запись (id) ?value—количество итераций
```
```
Сценарий → Повтор по
количеству объектов →
Вычисление набора объектов
```
```
?item-текущая запись (id) ?value—список объектов
```
```
Сценарий → Выполнение по
условиям → Условие
выполнения действий
```
```
?item-текущая запись (id)
```
```
?value-true (проверка
пройдена), false или пусто
(проверка не пройдена)
```

## Использование N-Triples в платформе

##### ЗАДАНИЕ 6

##### Написать запрос в вычисляемом атрибуте и вывести на форму, который

##### показывает количество уникальных контрагентов, указанных в накладной.

##### Исходные данные:

- Шаблон записи: **Nakladnaya**
- Атрибуты-контрагенты: **Platelschik** , **Gruzopoluchatel** , **Zakazchik**


## Использование N-Triples в платформе

##### ЗАДАНИЕ 7

##### Написать запрос на вывод списка просроченных работ, где текущий

##### пользователь является исполнителем

##### Исходные данные:

- Шаблон записи: **Rabota**
- Атрибут Срок выполнения: **Srok**
- Атрибут Исполнитель: **Ispolnitel**


