# N-Triples

# Обзорный курс

# Содержание

Урок 1\. Онтологии в реальном мире

Урок 2\. Введение в графы

Урок 3\. N\-Triples — что это такое?

Урок 4\. Comindware Elastic Data

Урок 5\. Запросы N\-Triples и как они работают

Урок 6\. Использование N\-Triples в платформе

# Онтологии в реальном мире

![](img/presentation_0.png)

![](img/presentation_1.png)

Окружающий мир состоит из объектов

Объекты имеют различные характеристики

Объекты связаны между собой и/или взаимодействуют

Объекты представляются классами

Классы имеют свойства

Классы взаимодействуют между собой

Классы имеют экземпляры

![](img/presentation_2.png)

__Яблоко 1__

__Яблоко 2__

ЗАДАНИЕ 1

Разложите на классы и их свойства предметы реального мира:

__карандаши в пенале__

# Введение в графы

Граф — это абстрактная фигура\, состоящая из вершин и ребер\, связывающих вершины

![](img/presentation_3.png)

![](img/presentation_4.png)

ЗАДАНИЕ 2

Создайте граф по предметам реального мира из предыдущего задания:

__карандаши в пенале__

# N-Triples

N\-Triples является упрощенным текстовым представлением графов в модели RDF \(resource definition framework\)\, рекомендованной консорциумом всемирной паутины для описания данных и метаданных

Является частью концепции семантической паутины \(предназначенной для обработки машинами\)

Является упрощенным подмножеством нотаций Turtle и Notation3\, представляющих модели RDF в компактном и удобном для чтения виде

![](img/presentation_5.png)

![](img/presentation_6.png)

\<http:/uri/\#Человек> \<http:/uri/\#владеет> \<http:/uri/\#Автомобиль>

\<Иван Иваныч> \<http:/uri/\#является> \<http:/uri/\#Человек>

\<Вольво> \<http:/uri/\#является> \<http:/uri/\#Автомобиль>

\<Иван Иваныч> \<http:/uri/\#владеет> \<Вольво>

ЗАДАНИЕ 3

Преобразуйте граф из предыдущего задания в набор триплетов:

__карандаши в пенале__

# Comindware Elastic Data

База данных представляет собой RDF граф в нотации N\-Triple

Данные Comindware Elastic Data хранятся в виде набора триплетов

Системные метаданные хранятся в виде набора файлов с расширением \*\.n3

Прикладные метаданные и данные хранятся в единой базе данных в виде набора файлов

Все ссылочные данные проиндексированы для выполнения быстрого поиска

\# User:Task class\.

\#

cmw:UserTask a cmw:Class\, container:ItemClass\, object:App;

cmw:parentClass s:Serializable;

cmw:isSystem true;

cmw:counterId true;

cmw:counterPrefix "";

container:alias "\_UserTask";

cmw:classSystemType cmw:UserTask;

object:property

cmw:title\,

cmw:assignee\,

cmw:taskStatus\,

cmw:endDate\,

cmw:dueDate\,

task:objectId\,

cmw:possibleAssignee\,

cmw:isReassignProhibited\,

cmw:startDate;

cmw:property

cmw:estimatedWork\,

cmw:percentComplete\,

cmw:isFollowed\,

cmw:isRecurrent\,

cmw:completionDate\,

cmw:completedBy\.

cmw:assignee a object:Property\.

cmw:assignee cmw:propertyName \<http://comindware\.com/text/cmw/platform/task\#assignee>\.

cmw:assignee cmw:propertyDescription \<http://comindware\.com/text/cmw/platform/task/assignee\#description>\.

cmw:assignee cmw:propertyType cmw:accountProperty\.

cmw:assignee s:serializer s:asQName\.

cmw:assignee object:alias "assignee"\.

@in ?task\.

\{

@from

\{

?task cmw:allChildren ?child\.

not \{ ? cmw:parent ?child \}\.

not \{ ?child cmw:taskStatus taskStatus:completed \}\.

if\-not \{ ?child cmw:remainingWork ?work  \}

then \{ "P0D"^^xsd:duration \-> ?work\. \}\.

\}

@select ?work \-> ?works\.

?works cmwmath:sum ?estimatedWork\.

if \{ ?estimatedWork == null \}

then \{ "P0D"^^xsd:duration \-> ?result\. \}

else \{ ?estimatedWork \-> ?result\. \}\.

\} => \{ ?task cmw:estimatedWork ?result \}\.

\#

\# account:Account class\.

\#

account:Account a cmw:Class\, cmw:Prototype\, object:App;

cmw:isSystem true;

cmw:className "Account";

container:alias "\_Account";

cmw:counterId true;

cmw:counterPrefix "account";

cmw:prototypeName \<http://comindware\.com/text/cmw/platform/account\#prototypeName>;

cmw:prototypeClass account:Account;

cmw:classSystemType account:Account;

object:property

account:username\,

account:active\,

account:fullName\,

account:manager\,

account:mbox\,

account:phone\,

account:skype\,

account:title\,

account:department\,

account:language\,

account:office\.

account:username a object:Property\, cmw:Property;

cmw:propertyType xsd:string;

cmw:propertyName \<http://comindware\.com/text/cmw/platform/account\#username>;

cmw:propertyDescription \<http://comindware\.com/text/cmw/platform/account/username\#description>;

cmw:propertyAttributes cmw:unique;

object:alias "username"\.

account:displayName a cmw:Property;

cmw:propertyType xsd:string\.

in ?account\.

\{

once

\{

?account a account:Account\.

or \{ ?account account:fullName ?name1\. ?name1 \-> ?name\}

or \{ ?account account:username ?name2\. ?name2 \-> ?name\}

\}

\} => \{ ?account account:displayName ?name\. \}\.

account:Account ui:displayNamePredicate account:displayName\.

# Запросы N-Triples

_\# _ — комментарий

_a _ — принадлежность субъекта к объекту

_\->_  — присваивание значения

_@prefix _ — объявление префиксов built\-in пакетов

_? _ — объявление переменных

\. — терминатор триплета

_\{_  _ _  _\}_  — объявление формулы

_\(_  _ _  _\)_  — объявление списка

_\[_  _ _  _\]_  – неявное использование субъекта

Запросы пишутся аналогично фактам в виде набора триплетов

У запроса есть входные \(в некоторых случаях\) и выходные данные

Запрос выполняется последовательно сверху вниз по каждому триплету

Если запрос ничего не вернул\, то это считается пустым результатом

Ризонер \(Reasoner\) \- специальный механизм\, выполняющий запросы

__in ?item\.__

__\{__

__	\#наш код__

__\} => \{ ?item attribute:value ?value\. \}\.__

__Существует 4 вида запросов__

| _субъект_ | _предикат_ | _?_ | Поиск объекта по заданному предикату и субъекту |
| :-: | :-: | :-: | :-: |
| _? _ | _предикат _ | _объект_ | Поиск субъекта по заданному предикату и объекту |
| _субъект_ | _предикат_ | _объект_ | Проверка наличия факта по заданным аргументам |
| _?_ | _предикат_ | _?_ | Поиск субъекта и объекта по заданному предикату |

Создается нумератор по всем пользователям

__?accounts a account:Account\.__

__?accounts account:username __  __"__  __ivanov\_ii__  __"__  __\.__

__?accounts \-> ?value\.__

Следующий пользователь

__Следующий триплет__

__account:username__

Выходной параметр

__Следующий триплет__

__?tasks a cmw:UserTask\.__

__\(__

__\{?tasks cmw:possibleAssignee ?accounts\.\}__

__\{?tasks cmw:assignee ?accounts\.\}__

__\) assert:union true\.__

__?accounts account:username __  __"__  __ivanov\_ii__  __"__  __\.__

__?tasks \-> ?value\.__

_Получим все задачи на исполнение_

_Получим всех исполнителей задачи\,_

_включая назначенных_

_Сравним с искомым литералом_

_Id задачи в выходной параметр_

__Полезные конструкции и __  __встроенные __  __функции__

_\(_  _"_  _tempAlias_  _"_  _ _  _"_  _attrAlias_  _"_  _\) object:findProperty ?p_  \-  __возвращает ID атрибута__

_once \{\}\._  \-  __выходит после первой успешной итерации__

_or \{\} or \{\} … or \{\}\._  \-  __оператор логическое ИЛИ__

_if \{\} then \{\} else \{\}\._  \-  __условный оператор__

_from \{\} select ?v \-> ?vList\._  \-  __получение типа Список__

_?list math:sum ?sum\._  \-  __получение суммы__

_\{\} assert:count ?c\._  \-  __выводит количество записей__

_\(\{\} … \{\}\) assert:union true\._  \-  __объединение итераторов в один__

__@prefix object: \<http://comindware\.com/ontology/object\#>\.__

__\{__

__\("currentTemplate" "Region"\) object:findProperty ?Region\.__

__\("Biznesstruktura" "Region"\) object:findProperty ?Region2\.__

__	once \{__

__?item ?Region ?RegionVal\.__

__		?check ?Region2 ?RegionVal\.__

__\}\.__

__true \-> ?value\.__

__\}__

__@prefix cmw: \<http://comindware\.com/logics\#>\.__

__\{__

__cmw:securityContext cmw:currentUser ?user\. \#получим текущего пользователя__

__?tasks a cmw:UserTask\.__

__or \{?tasks cmw:possibleAssignee ?user\.\}__

__or \{?tasks cmw:assignee ?user\.\}\.__

__?tasks \-> ?value\.__

__\}__

__@prefix cmw: \<http://comindware\.com/logics\#>\.__

__@prefix session: \<http://comindware\.com/ontology/session\#>\. __

__@prefix math: \<http://www\.w3\.org/2000/10/swap/math\#>\.__

__\{__

__session:context session:requestTime ?now\. \#получим текущую дату__

__?tasks a cmw:UserTask\.__

__	if \{?tasks cmw:dueDate ?\.\}__

__	then \{__

__?tasks cmw:dueDate ?dueDateVal\.__

__?dueDateVal math:greaterThan ?now\.__

__?tasks \-> ?value\.__

__\}__

__else \{?tasks \-> ?value\.\}\.__

__\}__

__Примеры \(from\, sum\)__

__@prefix math: \<http://www\.w3\.org/2000/10/swap/math\#>\.__

__@prefix object: \<http://comindware\.com/ontology/object\#>\.__

__\{__

__\("Nakladnaya" "PoziciiNakladnoy"\) object:findProperty ?Positions\.__

__\("PoziciiNakladnoy" "Summa"\) object:findProperty ?Summa\.__

__from  \{__

__?item ?Positions ?PositionsVal\.__

__??PositionsVal ?Summa ?SummaVal\.__

__\} select ?SummaVal \-> ?SummaList\.__

__?SummaList math:sum ?value\.__

__\}__

__@prefix object: \<http://comindware\.com/ontology/object\#>\.__

__@prefix assert: \<http://comindware\.com/logics/assert\#>\.__

__\{__

__\("Nakladnaya" "PoziciiNakladnoy"\) object:findProperty ?Positions\.__

__\{__

__?item ?Positions ?PositionsVal\.__

__\} assert:count ?value\.__

__\}__

__Примеры \(distinct\)__

__@prefix object: \<http://comindware\.com/ontology/object\#>\.__

__@prefix assert: \<http://comindware\.com/logics/assert\#>\.__

__\{__

__\("Nakladnaya" "PoziciiNakladnoy"\) object:findProperty ?Positions\.__

__\("PoziciiNakladnoy" "Nomenklatura"\) object:findProperty ?Items\.__

__\{__

__\{__

__?item ?Positions ?PositionsVal\.__

__?PositionsVal ?Items ?ItemsVal\.__

__\} assert:distinct ?ItemsVal\.__

__\} assert:count ?value\.__

__\}__

__@prefix assert: \<http://comindware\.com/logics/assert\#>\.__

__@prefix object: \<http://comindware\.com/ontology/object\#>\.__

__\{__

__\("Nakladnaya" "Gruzootpravitel"\) object:findProperty ?ShippedBy\.__

__\("Nakladnaya" "Poluchatel"\) object:findProperty ?Receiver\.__

__\(__

__\{?item ?ShippedBy ?Contractor\.\}__

__\{?item ?Receiver ?Contractor\.\}__

__\) assert:union true\.__

__?Contractor \-> ?value\.__

__\}__

ЗАДАНИЕ 4

Напишите запрос по сравнению двух атрибутов с множественными данными\, который возвращает true\, если все значения одного атрибута полностью совпадают со всеми значениями второго атрибута

Исходные данные:

Шаблон записи:  __test__

Атрибут 1:  __attr1__

Атрибут 2:  __attr2__

Выходной параметр:  __?value__

ЗАДАНИЕ 4 Решение

@prefix object: \<http://comindware\.com/ontology/object\#>\.

\{

\("test" "attr1"\) object:findProperty ?attr1\.

\("test" "attr2"\) object:findProperty ?attr2\.

?item ?attr1 ?attr1Val\.

?item ?attr2 ?attr2Val\.

if \{?attr1Val == ?attr2Val\.\}

then \{true \-> ?value\.\}

else \{false \-> ?value\.\}

\}

_1 итерация attr1 = 1 и attr2 = 1_

ЗАДАНИЕ 4 Решение

@prefix object: \<http://comindware\.com/ontology/object\#>\.

\{

\("test" "attr1"\) object:findProperty ?attr1\.

\("test" "attr2"\) object:findProperty ?attr2\.

?item ?attr1 ?attr1Val\.

?item ?attr2 ?attr2Val\.

if \{?attr1Val == ?attr2Val\.\}

then \{true \-> ?value\.\}

else \{false \-> ?value\.\}

\}

_последняя итерация attr1 = 3 и attr2 = 3_

ЗАДАНИЕ 4 Решение

@prefix assert: \<http://comindware\.com/logics/assert\#>\.

@prefix object: \<http://comindware\.com/ontology/object\#>\.

@prefix cmwstring: \<http://comindware\.com/logics/string\#>\.

\{

\("test" "attr1"\) object:findProperty ?attr1\.

\("test" "attr2"\) object:findProperty ?attr2\.

from \{

?item ?attr1 ?attr1Val\.

\} select ?attr1Val \-> ?attr1ValList\.

\(?attr1ValList sort:stringComparer\) assert:sort ?attr1ValListSort\.

\(" " ?attr1ValListSort\) cmwstring:join ?attr1ValListSortStr\.

…

if \{?attr1ValListSortStr == ?attr2ValListSortStr\}

\} ?value \-> fhsjhd

_Отсортировать список_

_Сформировать строку_

_Выполнить аналогичное действие для attr2_

_Сравнить полученные строки_

ЗАДАНИЕ 5

Написать запрос\, который показывает количество уникальных контрагентов\, указанных в накладной\.

Исходные данные:

Шаблон записи:  __Nakladnaya__

Атрибуты\-контрагенты:  __Platelschik__ \,  __Gruzopoluchatel__ \,  __Zakazchik__

Выходной параметр:  __?value__

ЗАДАНИЕ 5 Решение

@prefix assert: \<http://comindware\.com/logics/assert\#>\.

@prefix object: \<http://comindware\.com/ontology/object\#>\.

\{

\("Nakladnaya" "Platelschik"\) object:findProperty ?Platelschik\.

\("Nakladnaya" "Gruzopoluchatel"\) object:findProperty ?Gruzopoluchatel\.

\("Nakladnaya" "Zakazchik"\) object:findProperty ?Zakazchik\.

\{

\{

\(

\{?item ?Platelschik ?Contractors\.\}

\{?item ?Gruzopoluchatel ?Contractors\.\}

\{?item ?Zakazchik ?Contractors\.\}

\) assert:union true\.

\} assert:distinct ?Contractors\.

\} assert:count ?value\.

\}

# Использование N-Triples в платформе

__Параметры на входе и выходе__

| __Раздел__ | __Вход__ | __Выход__ |
| :-: | :-: | :-: |
| Атрибут → Вычисляемое значение | _?item_  \- текущая запись \(id\) | _?value_  — значение атрибута |
| <span style="color:#000000">Таблица → Системный фильтр</span> | \- | _?item_  — записи для вывода в таблице \(id\) |
| <span style="color:#000000">Кнопка → Условие отображения</span> | ?item \- текущая запись \(id\) | _?value_  \- true или false |
| Форма → Фильтр на поле | ?item \- текущая запись \(id\) | _?value_  – искомые записи \(id\) |

__Параметры на входе и выходе__

| __Раздел__ | __Вход__ | __Выход__ |
| :-: | :-: | :-: |
| <span style="color:#000000">Роль → Разрешения → Шаблон записи\, аккаунта\, процесса → Условие применения</span> | ?item \- текущая запись \(id\) | <span style="color:#000000"> _?_ </span>  <span style="color:#000000"> _value_ </span>  <span style="color:#000000"> _ – _ </span>  <span style="color:#000000"> _true_ </span>  <span style="color:#000000"> _ _ </span>  <span style="color:#000000">\(строка разрешений применяется\) или </span>  <span style="color:#000000"> _false_ </span>  <span style="color:#000000"> _ _ </span>  <span style="color:#000000">\(не применяется\)</span> |
| <span style="color:#000000">Роль → Разрешения → Шаблон записи\, аккаунта\, процесса → Фильтр аккаунтов \(Переназначение\)</span> | _?value_  \- текущий аккаунт \(id\) | _?item_  – список аккаунтов \(id\) |

__Параметры на входе и выходе__

| __Раздел__ | __Вход__ | __Выход__ |
| :-: | :-: | :-: |
| Правила для формы → Вычисляемое значение для действия | _?item_  \- текущая запись \(id\) | _?value_  — значение атрибута |
| Правила для формы → Правило → Условие выполнения | _?item_  \- текущая запись \(id\) | _?value_  —  _true _ \(правило сработает\)\,  _false _ или пусто \(не сработает\) |
| Правила для формы → Действие → Условие выполнения | _?item_  \- текущая запись \(id\) | _?value_  \- true \(действие сработает\)\, false или пусто \(не сработает\) |

__Параметры на входе и выходе__

| __Раздел__ | __Вход__ | __Выход__ |
| :-: | :-: | :-: |
| Сценарий → Смена контекста → Вычисление набора объектов | _?item_  \- текущая запись \(id\) | _?value_  — запись для перехода |
| Сценарий → Дублирование записи → Вычисление набора объектов | _?item_  \- текущая запись \(id\) | _?value_  — записи для дублирования |

__Параметры на входе и выходе__

| __Раздел__ | __Вход__ | __Выход__ |
| :-: | :-: | :-: |
| Сценарий → Проверка результата выражения → Выражение для проверки | _?item_  \- текущая запись \(id\) | _?value_  \-  _true _ \(проверка пройдена\)\,  _false _ или пусто \(проверка не пройдена\) |
| Сценарий → Изменение значений атрибутов → Вычисление значения | _?item_  \- текущая запись \(id\) | _?value_  — значение атрибута |
| Сценарий → Изменение значений переменных → Вычисление значения | _?item_  \- текущая запись \(id\) | _?value_  — значение переменной |

__Параметры на входе и выходе__

| __Раздел__ | __Вход__ | __Выход__ |
| :-: | :-: | :-: |
| Сценарий → Повтор по числовому счётчику → Количество итераций | _?item_  \- текущая запись \(id\) | _?value_  — количество итераций |
| Сценарий → Повтор по количеству объектов → Вычисление набора объектов | _?item_  \- текущая запись \(id\) | _?value_  — список объектов |
| Сценарий → Выполнение по условиям → Условие выполнения действий | _?item_  \- текущая запись \(id\) | _?value_  \- true \(проверка пройдена\)\, false или пусто \(проверка не пройдена\) |

ЗАДАНИЕ 6

Написать запрос в вычисляемом атрибуте и вывести на форму\, который показывает количество уникальных контрагентов\, указанных в накладной\.

Исходные данные:

Шаблон записи:  __Nakladnaya__

Атрибуты\-контрагенты:  __Platelschik__ \,  __Gruzopoluchatel__ \,  __Zakazchik__

ЗАДАНИЕ 7

Написать запрос на вывод списка просроченных работ\, где текущий пользователь является исполнителем

Исходные данные:

Шаблон записи:  __Rabota__

Атрибут Срок выполнения:  __Srok__

Атрибут Исполнитель:  __Ispolnitel__

