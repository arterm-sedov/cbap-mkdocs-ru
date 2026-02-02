# Подробное руководство по синтаксису N3 троек (Notation3)

## ОГЛАВЛЕНИЕ
1. [Общая структура](#общая-структура)
2. [Префиксы](#префиксы)
3. [Блоки правил](#блоки-правил)
4. [Тройки (Triples)](#тройки-triples)
5. [Переменные](#переменные)
6. [Операторы](#операторы)
7. [Условные конструкции](#условные-конструкции)
8. [Конструкции from-select](#конструкции-from-select)
9. [Функции строк](#функции-строк)
10. [Математические функции](#математические-функции)
11. [Работа со списками](#работа-со-списками)
12. [Логические операторы](#логические-операторы)
13. [Операции сравнения](#операции-сравнения)
14. [Назначение значений](#назначение-значений)
15. [Работа с документами](#работа-с-документами)
16. [Специальные конструкции](#специальные-конструкции)
17. [Жесткие правила синтаксиса](#жесткие-правила-синтаксиса)

---

## ОБЩАЯ СТРУКТУРА

### Базовый формат N3 правила:
```
@prefix prefix_name: <URI>.
@prefix prefix_name2: <URI2>.

{
    # Тело правила - тройки и операции
    ?subject ?predicate ?object.
    
    # Результат
    ?result -> ?value.
}
```

**КРИТИЧЕСКИ ВАЖНО:**
- Каждая тройка ОБЯЗАТЕЛЬНО заканчивается точкой (`.`)
- Блок правила ОБЯЗАТЕЛЬНО заключен в фигурные скобки `{}`
- Префиксы объявляются ДО блока правил
- Результат обычно присваивается через `-> ?value`

---

## ПРЕФИКСЫ

### Синтаксис объявления префикса:
```
@prefix prefix_name: <http://example.com/ontology#>.
```

### Обязательные правила:
1. **Префикс ДОЛЖЕН начинаться с `@prefix`**
2. **После двоеточия ОБЯЗАТЕЛЬНО пробел перед `<`**
3. **URI ОБЯЗАТЕЛЬНО заключен в угловые скобки `<>`**
4. **Строка ОБЯЗАТЕЛЬНО заканчивается точкой (`.`)**
5. **Префиксы объявляются ПЕРЕД блоком правил `{}`**

### Примеры из файла:
```n3
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
```

### Часто используемые префиксы:
- `var:` - переменные сессии
- `operator:` - операторы (add, replace, clear)
- `object:` - работа с объектами
- `string:` - строковые функции W3C
- `cmwstring:` - строковые функции Comindware
- `session:` - контекст сессии
- `document:` - работа с документами
- `cmwnullable:` - математические операции с nullable типами
- `cmwlist:` - операции со списками
- `assert:` - операции подсчета и проверки
- `list:` - операции со списками W3C

---

## БЛОКИ ПРАВИЛ

### Синтаксис:
```
{
    # Содержимое блока
    ?item ?property ?value.
    ?result -> ?value.
}
```

### Правила:
1. **Блок ОБЯЗАТЕЛЬНО начинается с `{` и заканчивается `}`**
2. **Внутри блока каждая тройка заканчивается точкой**
3. **Можно использовать вложенные блоки для if-then-else, from-select**
4. **Комментарии начинаются с `#`**

---

## ТРОЙКИ (TRIPLES)

### Базовая структура тройки:
```
?subject ?predicate ?object.
```

### Типы объектов в тройках:

#### 1. Переменные (начинаются с `?`):
```n3
?item ?property ?value.
```

#### 2. Литеральные строки (в двойных кавычках):
```n3
?item ?property "string_value".
```

#### 3. Числовые значения:
```n3
?item ?property 123.
?item ?property 0.25.
```

#### 4. Булевы значения:
```n3
?item ?property true.
?item ?property false.
```

#### 5. Использование префиксов:
```n3
?item object:findProperty ?property.
var:mass operator:add ?item.
```

#### 6. Специальные значения:
```n3
?item ?property ?.  # Пустое значение (null check)
?value a account:Account.  # Тип (rdf:type)
```

### Правила написания троек:
1. **Каждая тройка ОБЯЗАТЕЛЬНО заканчивается точкой (`.`)**
2. **Между элементами тройки ОБЯЗАТЕЛЬНЫ пробелы**
3. **Строковые литералы ОБЯЗАТЕЛЬНО в двойных кавычках**
4. **Переменные ОБЯЗАТЕЛЬНО начинаются с `?`**

---

## ПЕРЕМЕННЫЕ

### Правила именования:
1. **ОБЯЗАТЕЛЬНО начинаются с `?`**
2. **Могут содержать буквы, цифры, подчеркивания**
3. **Регистр важен: `?item` ≠ `?Item`**
4. **Имена должны быть описательными**

### Примеры:
```n3
?item
?District_ExternalID
?DiscountItem_CompensatoryDiscountProperty
?PartyInvolved_BusinessPartnerProp
?KolichestvoVal
```

### Специальные переменные:
- `?item` - обычно входной объект
- `?value` - обычно результат правила
- `?.` - проверка на пустое значение

---

## ОПЕРАТОРЫ

### Оператор `operator:add` - добавление в коллекцию:
```n3
var:mass operator:add ?item.
var:massPartyInvolved operator:add ?item.
var:offerItems operator:add ?item.
var:metersPhoto operator:add ?newString.
```

**Синтаксис:**
```
collection_name operator:add value_to_add.
```

**Правила:**
- Первый аргумент - имя коллекции (обычно с префиксом `var:`)
- Второй аргумент - значение для добавления
- ОБЯЗАТЕЛЬНО заканчивается точкой

### Оператор `operator:replace` - замена значения:
```n3
(?item var:FEATURE) operator:replace "BZIRK".
(?item var:VALUE) operator:replace ?District_ExternalIDVal.
(?item var:PartnerRole) operator:replace "AG".
(?item var:PartnerId) operator:replace ?Account_ExternalIDVal.
```

**Синтаксис:**
```
(target_object target_property) operator:replace new_value.
```

**Правила:**
- Целевой объект и свойство ОБЯЗАТЕЛЬНО в скобках
- Разделены пробелом внутри скобок
- Новое значение может быть переменной или литералом
- ОБЯЗАТЕЛЬНО заканчивается точкой

### Оператор `operator:clear` - очистка коллекции:
```n3
var:pos operator:clear ?item.
```

**Синтаксис:**
```
collection_name operator:clear value_to_clear.
```

---

## УСЛОВНЫЕ КОНСТРУКЦИИ

### Базовая структура if-then-else:
```n3
if {condition.}
then {then_block.}
else {else_block.}.
```

### Правила:
1. **`if` ОБЯЗАТЕЛЬНО в нижнем регистре**
2. **Условие ОБЯЗАТЕЛЬНО в фигурных скобках `{}`**
3. **Условие заканчивается точкой ПЕРЕД закрывающей скобкой**
4. **`then` и `else` ОБЯЗАТЕЛЬНО в нижнем регистре**
5. **Блоки `then` и `else` ОБЯЗАТЕЛЬНО в фигурных скобках**
6. **Вся конструкция заканчивается точкой ПОСЛЕ `else` блока**

### Примеры:

#### Простое условие:
```n3
if {?PartyInvolvedRole_CodeVal == "account" }
then {?list ?PartyInvolved_BusinessPartnerProp ?PartyInvolved_BusinessPartnerVal.}
else {"asdasdsad" -> ?b}.
```

#### Условие с проверкой на пустое значение:
```n3
if {?UslugitranzaktsionnyeValFromCount ?KolichestvoProperty ?. }
then { ?UslugitranzaktsionnyeValFromCount ?KolichestvoProperty ?KolichestvoVal}
else { 1 -> ?KolichestvoVal}.
```

#### Условие с несколькими строками в блоках:
```n3
if {?approvedServiceListToStr == "". }
then {
    "" -> ?availaible.
    "" -> ?availaible1.
}
else {
    "Доступно:" -> ?availaible.
    "Подскажите, когда и в каком районе будет удобно посетить клинику?" -> ?availaible1.
}.
```

#### Вложенные условия:
```n3
if {?item ?Tipotnosheniy ?otnoshenieYrLic.}
then { ?value a account:Account.}
else { 
    if { ?item ?BusinessPartnerRelation_BusinessPartner_1Property ?BusinessPartnerRelation_BusinessPartner_1Val. }
    then {?item ?CreatorProperty ?CreatorVal.}
    else {?value a account:Account. }.
}.
```

#### Условие с `not`:
```n3
if {not{?item ?datazaversheniyraboty ?.}.}
then {?item ?duedate ?duedateval.}
else {?item ?datazaversheniyraboty ?datezav.}.
```

#### Условие с `once`:
```n3
if {
    once{
        ?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal3.
        ?UslugitranzaktsionnyeVal3 ?DokupkaProperty ?DokupkaVal.
        ?DokupkaVal == true.
    }.
}
then {
    "Также вижу, что часть услуг не входит в программу, поискать их со скидкой?" -> ?additionalServiseText.
}
else {"" -> ?additionalServiseText. }.
```

---

## КОНСТРУКЦИИ FROM-SELECT

### Базовая структура:
```n3
from 
{
    # Условия выборки
    ?item ?property ?value.
}
select ?selectedValue -> ?resultList.
```

### Правила:
1. **`from` ОБЯЗАТЕЛЬНО в нижнем регистре**
2. **Блок условий ОБЯЗАТЕЛЬНО в фигурных скобках**
3. **`select` ОБЯЗАТЕЛЬНО в нижнем регистре**
4. **После `select` указывается переменная для выборки**
5. **Результат присваивается через `->`**
6. **Вся конструкция заканчивается точкой**

### Примеры:

#### Простой from-select:
```n3
from 
{
    ?item ?TiketProperty ?TiketVal.
    ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal.
    ?UslugitranzaktsionnyeVal ?StatusProperty ?approvedService.
}
select ?approvedServiceStr -> ?approvedServiceList.
```

#### From-select с кортежами (несколько значений):
```n3
from {
    ?item ?PriceProtocolHeader_PriceProtocolItemProperty ?PriceProtocolHeader_PriceProtocolItemVal.
    ?PriceProtocolHeader_PriceProtocolItemVal ?PriceProtocolItem_StatusProperty ?PriceProtocolItem_StatusVal.
}
select (?Status_CodeVal ?Step_CodeVal ?PriceProtocolItem_PriceVal) -> ?detailingList.
```

**Правила для кортежей:**
- Несколько значений ОБЯЗАТЕЛЬНО в скобках
- Значения разделены пробелами
- Порядок важен

#### From-select с условиями:
```n3
from {
    ?item ?ICSRHeaderProp ?ICPHeader.
    ?ICPHeader ?ICPHMillBPProp ?MillBP.
    ?MillBP ?BPOrgModelProp ?MillOrgModel.
    ?MillRates ?MillRateOrgUnitProp ?MillOrgModel.
    ?MillRates ?MillRateIncotermProp ?MillRateIncoterm.
    ?MillRateIncoterm ?IncotermsCodeProp "FOB".
}
select ?MillRateDates -> ?MillRateDatesList.
```

---

## ФУНКЦИИ СТРОК

### `string:format` - форматирование строки:
```n3
("• {0} - {1} шт." ?NaimenovanieVal ?KolichestvoVal) string:format ?approvedServiceStr.
("data:image/jpeg;base64,{0}" ?Document) string:format ?newString.
("<p><a href='https://system.bau.cbap.ru/DocumentContent?id={0}'>Ссылка на файл {1}</a></p>" ?doc ?title) string:format ?value.
```

**Синтаксис:**
```
(format_string arg1 arg2 ...) string:format result_variable.
```

**Правила:**
- Шаблон и аргументы ОБЯЗАТЕЛЬНО в скобках
- Плейсхолдеры: `{0}`, `{1}`, `{2}` и т.д.
- Аргументы разделены пробелами
- Результат присваивается переменной
- ОБЯЗАТЕЛЬНО заканчивается точкой

### `string:regexReplace` - регулярное выражение:
```n3
(?DocumentNumberVal "^0+" "" ) string:regexReplace ?result.
```

**Синтаксис:**
```
(source_string pattern replacement) string:regexReplace result_variable.
```

### `string:trim` - удаление пробелов:
```n3
?CertificateItem_SmeltingNumberVal string:trim ?trimedCertificateItem_SmeltingNumber.
```

**Синтаксис:**
```
source_string string:trim result_variable.
```

### `string:substring` - подстрока:
```n3
(?Stock_CodeCRMVal 4)string:substring ?Stock_CodeCRMSubVal.
(?OrganizationalModel_IDVal 4)string:substring ?OrganizationalModel_IDSubVal.
```

**Синтаксис:**
```
(source_string start_index) string:substring result_variable.
```

**Правила:**
- Аргументы ОБЯЗАТЕЛЬНО в скобках
- Индекс начинается с указанной позиции

### `string:contains` - проверка содержания:
```n3
(?OrganizationalModel_IDVal) string:contains "ZVD_"
```

**Синтаксис:**
```
(source_string) string:contains search_string
```

### `cmwstring:join` - объединение списка строк:
```n3
(" " ?approvedServiceList) cmwstring:join ?approvedServiceListToStr.
```

**Синтаксис:**
```
(separator list) cmwstring:join result_variable.
```

### `cmwstring:toLower` - преобразование в нижний регистр:
```n3
?PrichinyotkazavsoglasovaniiNaimenovanieStr cmwstring:toLower ?PrichinyotkazavsoglasovaniiNaimenovanieStrToLower.
```

**Синтаксис:**
```
source_string cmwstring:toLower result_variable.
```

---

## МАТЕМАТИЧЕСКИЕ ФУНКЦИИ

### `cmwnullable:remainder` - остаток от деления:
```n3
(?countVal 4) cmwnullable:remainder ?resultReminder.
```

**Синтаксис:**
```
(dividend divisor) cmwnullable:remainder result_variable.
```

### `cmwnullable:product` - умножение:
```n3
(?countVal 0.25) cmwnullable:product ?firstIndexVal.
```

**Синтаксис:**
```
(value1 value2) cmwnullable:product result_variable.
```

### `cmwnullable:sum` - сложение:
```n3
(?firstIndexVal 1) cmwnullable:sum ?secondIndexVal.
```

**Синтаксис:**
```
(value1 value2) cmwnullable:sum result_variable.
```

### `cmwnullable:average` - среднее значение:
```n3
(?valOfFirstIndexVal ?valOsecondIndexValVal)cmwnullable:average ?resultVal.
```

**Синтаксис:**
```
(value1 value2) cmwnullable:average result_variable.
```

### `cmwnullable:max` - максимальное значение:
```n3
?MillRateDatesList cmwnullable:max ?MillRateDatesMax.
?total1List cmwnullable:max ?result.
```

**Синтаксис:**
```
list_or_value cmwnullable:max result_variable.
```

### `cmwnullable:ceiling` - округление вверх:
```n3
?firstIndexVal cmwnullable:ceiling ?firstIndexValAfterCell.
```

**Синтаксис:**
```
value cmwnullable:ceiling result_variable.
```

### `cmwnullable:startOfDay` - начало дня:
```n3
?now cmwnullable:startOfDay ?nowstart.
?duedateval cmwnullable:startOfDay ?duedatevalstart.
```

**Синтаксис:**
```
date_value cmwnullable:startOfDay result_variable.
```

### `cmwnullable:greaterThan` - сравнение "больше":
```n3
?nowstart cmwnullable:greaterThan ?duedatevalstart.
```

**Синтаксис:**
```
value1 cmwnullable:greaterThan value2
```

---

## РАБОТА СО СПИСКАМИ

### `cmwlist:ascending` - сортировка по возрастанию:
```n3
?chisloPropertyValList cmwlist:ascending ?chisloPropertyValListSorted.
```

**Синтаксис:**
```
list cmwlist:ascending result_variable.
```

### `cmwlist:at` - получение элемента по индексу:
```n3
(?chisloPropertyValListSorted ?firstIndexVal) cmwlist:at ?valOfFirstIndexVal.
```

**Синтаксис:**
```
(list index) cmwlist:at result_variable.
```

### `list:member` - проверка членства:
```n3
?detailingList list:member ?datailingListMember1.
```

**Синтаксис:**
```
list list:member member_variable.
```

### `list:ascending` (W3C) - сортировка:
```n3
?PPValList list:ascending ?value.
```

### Работа с кортежами из списка:
```n3
?datailingListMember1 -> (?code1 ?step1 ?total1).
```

**Синтаксис:**
```
tuple_variable -> (var1 var2 var3 ...).
```

**Правила:**
- Кортеж ОБЯЗАТЕЛЬНО в скобках
- Переменные разделены пробелами
- Порядок соответствует порядку в select

---

## ЛОГИЧЕСКИЕ ОПЕРАТОРЫ

### `or` - логическое ИЛИ:
```n3
or{?PrichinyotkazavsoglasovaniiKodVal == "ended_contract".}
or{?PrichinyotkazavsoglasovaniiKodVal == "disease_in_exceptions".}
or{?PrichinyotkazavsoglasovaniiKodVal == "uninsured_event".}
```

**Правила:**
- Каждое условие в отдельном блоке `or{}`
- Условие заканчивается точкой ПЕРЕД закрывающей скобкой
- Используется для множественных проверок

### `or` для альтернативных блоков:
```n3
or
{
    ?total1List cmwnullable:max ?result.
    ?result != 0.
}
or
{
    1 -> ?result.
}.
```

**Правила:**
- Блоки разделены `or`
- Каждый блок в фигурных скобках
- Последний блок заканчивается точкой ПОСЛЕ закрывающей скобки

### `not` - логическое НЕ:
```n3
if {not{?item ?datazaversheniyraboty ?.}.}
```

**Синтаксис:**
```
not{condition.}
```

**Правила:**
- Условие ОБЯЗАТЕЛЬНО в фигурных скобках
- Заканчивается точкой ПЕРЕД закрывающей скобкой

### `once` - выполнение один раз:
```n3
once{
    ?item ?TiketProperty ?TiketVal.
    ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal3.
}.
```

**Синтаксис:**
```
once{statements.}
```

---

## ОПЕРАЦИИ СРАВНЕНИЯ

### Равенство `==`:
```n3
?PartyInvolvedRole_CodeVal == "account"
?approvedServiceListToStr == ""
?resultReminder == 0.
?result != 0.
```

**Правила:**
- Оператор `==` для равенства
- Оператор `!=` для неравенства
- ОБЯЗАТЕЛЬНЫ пробелы вокруг оператора
- Используется в условиях if

### Примеры сравнений:
```n3
?PrichinyotkazavsoglasovaniiKodVal == "ended_contract".
?DokupkaVal == true.
?Tipkontragenta == ?typeKlient.
?strprocessStatus == "process.ActiveStatus".
?nameVal == "Creating_Account".
```

---

## НАЗНАЧЕНИЕ ЗНАЧЕНИЙ

### Оператор `->` - присваивание:
```n3
true -> ?value.
"empty" -> ?value.
?resultVal -> ?value.
?order -> ?value.
```

**Синтаксис:**
```
value -> variable.
```

**Правила:**
- ОБЯЗАТЕЛЬНЫ пробелы вокруг `->`
- Обычно используется для присваивания результата `?value`
- ОБЯЗАТЕЛЬНО заканчивается точкой

### Присваивание кортежа:
```n3
?datailingListMember1 -> (?code1 ?step1 ?total1).
```

### Присваивание в блоках:
```n3
"" -> ?availaible.
"" -> ?availaible1.
```

---

## РАБОТА С ДОКУМЕНТАМИ

### `document:content` - получение содержимого:
```n3
?FaylData document:content ?Document.
```

**Синтаксис:**
```
document_object document:content content_variable.
```

### `document:title` - получение заголовка:
```n3
?FaylData document:title ?title.
?doc document:title ?title.
```

**Синтаксис:**
```
document_object document:title title_variable.
```

---

## СПЕЦИАЛЬНЫЕ КОНСТРУКЦИИ

### `object:findProperty` - поиск свойства:
```n3
("District" "District_ExternalID") object:findProperty ?District_ExternalID.
("DiscountItem" "DiscountItem_CompensatoryDiscount") object:findProperty ?DiscountItem_CompensatoryDiscountProperty.
```

**Синтаксис:**
```
(type_name property_name) object:findProperty result_variable.
```

**Правила:**
- Тип и имя свойства ОБЯЗАТЕЛЬНО в скобках
- Оба значения в двойных кавычках
- Разделены пробелом

### `object:alias` - получение алиаса:
```n3
?template object:alias "ProjectPlans".
```

**Синтаксис:**
```
object_variable object:alias alias_string.
```

### `session:context` - контекст сессии:
```n3
session:context var:product ?productVal.
session:context var:var ?varVal.
session:context session:requestTime ?now.
```

**Синтаксис:**
```
session:context context_key context_value.
```

### `cmw:container` - контейнер объекта:
```n3
?item cmw:container ?template.
```

**Синтаксис:**
```
object cmw:container container_variable.
```

### `cmw:securityContext` - контекст безопасности:
```n3
cmw:securityContext cmw:currentUser ?currentUser.
cmw:securityContext cmw:currentUser ?user.
```

**Синтаксис:**
```
cmw:securityContext cmw:currentUser user_variable.
```

### `assert:count` - подсчет:
```n3
{
    ?item ?pozitsiiProperty ?pozitsiiVal.
} assert:count ?countVal.
```

**Синтаксис:**
```
{conditions.} assert:count result_variable.
```

**Правила:**
- Условия ОБЯЗАТЕЛЬНО в фигурных скобках
- Результат - количество совпадений

### `convert:enumValue` - преобразование enum:
```n3
("Spisokznacheniy" "cancelled") convert:enumValue ?enumVal.
```

**Синтаксис:**
```
(type_name enum_value) convert:enumValue result_variable.
```

### Тип объекта `a`:
```n3
?value a account:Account.
?item a cmw:UserTask.
```

**Синтаксис:**
```
object a type.
```

**Правила:**
- `a` - сокращение для rdf:type
- ОБЯЗАТЕЛЬНЫ пробелы вокруг `a`

### Специальные предикаты:
```n3
?task task:objectId ?item.
?task cmw:taskStatus taskStatus:inProgress.
?processObject process:businessObject ?item.
?processObject process:status ?processStatus.
?processObject process:name ?nameVal.
?item cmw:assignee ?currentUser.
?item cmw:possibleAssignee ?currentUser.
```

---

## ЖЕСТКИЕ ПРАВИЛА СИНТАКСИСА

### 1. ТОЧКИ И ЗАВЕРШЕНИЕ СТРОК
- ✅ **КАЖДАЯ тройка ОБЯЗАТЕЛЬНО заканчивается точкой (`.`)**
- ✅ **Условия в if заканчиваются точкой ПЕРЕД `}`**
- ✅ **Блоки then/else заканчиваются точкой ПОСЛЕ `}`**
- ✅ **Конструкции from-select заканчиваются точкой**
- ✅ **Операторы заканчиваются точкой**

### 2. ФИГУРНЫЕ СКОБКИ
- ✅ **Блоки правил ОБЯЗАТЕЛЬНО в `{}`**
- ✅ **Условия if ОБЯЗАТЕЛЬНО в `{}`**
- ✅ **Блоки then/else ОБЯЗАТЕЛЬНО в `{}`**
- ✅ **Блоки from ОБЯЗАТЕЛЬНО в `{}`**
- ✅ **Блоки or ОБЯЗАТЕЛЬНО в `{}`**

### 3. ПРОБЕЛЫ
- ✅ **ОБЯЗАТЕЛЬНЫ пробелы между элементами тройки**
- ✅ **ОБЯЗАТЕЛЬНЫ пробелы вокруг операторов (`==`, `!=`, `->`)**
- ✅ **ОБЯЗАТЕЛЬНЫ пробелы в скобках функций**
- ✅ **ОБЯЗАТЕЛЬНЫ пробелы после префиксов**

### 4. КАВЫЧКИ
- ✅ **Строковые литералы ОБЯЗАТЕЛЬНО в двойных кавычках `""`**
- ✅ **Имена типов и свойств в object:findProperty ОБЯЗАТЕЛЬНО в кавычках**

### 5. ПЕРЕМЕННЫЕ
- ✅ **Переменные ОБЯЗАТЕЛЬНО начинаются с `?`**
- ✅ **Имена переменных чувствительны к регистру**
- ✅ **Не использовать зарезервированные имена без префиксов**

### 6. РЕГИСТР
- ✅ **Ключевые слова (`if`, `then`, `else`, `from`, `select`, `or`, `not`, `once`) ОБЯЗАТЕЛЬНО в нижнем регистре**
- ✅ **Префиксы сохраняют регистр как объявлены**
- ✅ **Имена свойств и типов сохраняют регистр**

### 7. СКОБКИ
- ✅ **Аргументы функций ОБЯЗАТЕЛЬНО в круглых скобках `()`**
- ✅ **Кортежи ОБЯЗАТЕЛЬНО в круглых скобках**
- ✅ **object:findProperty ОБЯЗАТЕЛЬНО в круглых скобках**

### 8. ПРЕФИКСЫ
- ✅ **Префиксы объявляются ДО блока правил**
- ✅ **Префиксы ОБЯЗАТЕЛЬНО заканчиваются точкой**
- ✅ **URI ОБЯЗАТЕЛЬНО в угловых скобках `<>`**

### 9. РЕЗУЛЬТАТ ПРАВИЛА
- ✅ **Результат обычно присваивается через `-> ?value`**
- ✅ **Может быть `true -> ?value` для успешного выполнения**
- ✅ **Может быть конкретное значение `?result -> ?value`**

### 10. ВЛОЖЕННОСТЬ
- ✅ **Блоки могут быть вложенными**
- ✅ **Каждый уровень вложенности ОБЯЗАТЕЛЬНО в своих скобках**
- ✅ **Точки расставляются по правилам каждого уровня**

---

## ПРИМЕРЫ ПОЛНЫХ ПРАВИЛ

### Пример 1: Простое правило с операторами
```n3
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("District" "District_ExternalID") object:findProperty ?District_ExternalID.
    ?item ?District_ExternalID ?District_ExternalIDVal.
    var:mass operator:add ?item.
    (?item var:FEATURE) operator:replace "BZIRK".
    (?item var:VALUE) operator:replace ?District_ExternalIDVal.
    true -> ?value.
}
```

### Пример 2: Правило с условием
```n3
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("PartyInvolved" "PartyInvolved_PartyInvolvedRole" ) object:findProperty ?PartyInvolved_PartyInvolvedRoleProp.
    ("PartyInvolvedRole" "PartyInvolvedRole_Code") object:findProperty ?PartyInvolvedRole_CodeProp.
    
    ?item ?PartyInvolved_PartyInvolvedRoleProp ?PartyInvolved_PartyInvolvedRoleVal.
    ?PartyInvolved_PartyInvolvedRoleVal ?PartyInvolvedRole_CodeProp ?PartyInvolvedRole_CodeVal.
    
    if {?PartyInvolvedRole_CodeVal == "account" }
    then {
        var:massPartyInvolved operator:add ?item.
        (?item var:PartnerRole) operator:replace "AG".
    }
    else {"asdasdsad" -> ?b}.
    
    true -> ?value.
}
```

### Пример 3: Правило с from-select
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.

{
    ("Usluga" "Naimenovanie") object:findProperty ?NaimenovanieProperty.
    ("Usluga" "Kolichestvo") object:findProperty ?KolichestvoProperty.
    
    from 
    {
        ?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal.
        ?UslugitranzaktsionnyeVal ?StatusProperty ?approvedService.
        ?UslugitranzaktsionnyeValFromName ?NaimenovanieProperty ?NaimenovanieVal.
        ("• {0} - {1} шт." ?NaimenovanieVal ?KolichestvoVal) string:format ?approvedServiceStr.
    }
    select ?approvedServiceStr -> ?approvedServiceList.
    
    (" " ?approvedServiceList) cmwstring:join ?approvedServiceListToStr.
    ?approvedServiceListToStr -> ?value.
}
```

### Пример 4: Правило с математическими операциями
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.
@prefix assert: <http://comindware.com/logics/assert#>.

{
    ("Protokoltsen" "pozitsii") object:findProperty ?pozitsiiProperty.
    
    {
        ?item ?pozitsiiProperty ?pozitsiiVal.
    } assert:count ?countVal.
    
    (?countVal 4) cmwnullable:remainder ?resultReminder.
    
    if {?resultReminder == 0.}
    then {
        (?countVal 0.25) cmwnullable:product ?firstIndexVal.
        (?firstIndexVal 1) cmwnullable:sum ?secondIndexVal.
        ?resultVal -> ?value.
    }
    else {
        ?firstIndexVal cmwnullable:ceiling ?firstIndexValAfterCell.
        ?ValfirstIndexValAfterCell -> ?value.
    }.
}
```

---

## ЧЕКЛИСТ ПРИ НАПИСАНИИ ПРАВИЛА

Перед завершением правила проверьте:

- [ ] Все префиксы объявлены ДО блока правил
- [ ] Все префиксы заканчиваются точкой
- [ ] Блок правил заключен в `{}`
- [ ] Каждая тройка заканчивается точкой
- [ ] Все строковые литералы в двойных кавычках
- [ ] Все переменные начинаются с `?`
- [ ] Ключевые слова в нижнем регистре
- [ ] Условия if-then-else правильно структурированы
- [ ] Конструкции from-select правильно оформлены
- [ ] Результат присвоен через `-> ?value` или `true -> ?value`
- [ ] Пробелы вокруг операторов
- [ ] Скобки правильно расставлены
- [ ] Нет синтаксических ошибок

---

## ЗАКЛЮЧЕНИЕ

Это руководство содержит все основные паттерны и правила синтаксиса N3 троек на основе анализа реальных примеров. При написании новых правил строго следуйте указанным синтаксическим требованиям для обеспечения корректной работы правил.
