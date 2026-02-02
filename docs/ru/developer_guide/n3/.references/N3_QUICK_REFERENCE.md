# N3 Тройки - Краткая шпаргалка

## БАЗОВАЯ СТРУКТУРА

```n3
@prefix prefix: <URI>.
{
    ?subject ?predicate ?object.
    ?result -> ?value.
}
```

## КРИТИЧЕСКИЕ ПРАВИЛА

1. **ТОЧКА** - каждая тройка заканчивается `.`
2. **СКОБКИ** - блоки в `{}`, аргументы функций в `()`
3. **КАВЫЧКИ** - строки в `""`
4. **ПЕРЕМЕННЫЕ** - начинаются с `?`
5. **РЕГИСТР** - `if`, `then`, `else`, `from`, `select` - нижний регистр

## ПРЕФИКСЫ

```n3
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
```

## ОПЕРАТОРЫ

```n3
# Добавление в коллекцию
var:collection operator:add ?item.

# Замена значения
(?item var:property) operator:replace "value".

# Очистка
var:collection operator:clear ?item.
```

## УСЛОВИЯ

```n3
# Простое условие
if {?var == "value".}
then {?result -> ?value.}
else {"" -> ?value.}.

# Проверка на пустое
if {?item ?property ?.}
then {?item ?property ?val.}
else {0 -> ?val.}.

# Вложенное условие
if {condition1.}
then {?val1 -> ?value.}
else {
    if {condition2.}
    then {?val2 -> ?value.}
    else {?val3 -> ?value.}.
}.
```

## FROM-SELECT

```n3
# Простой
from {
    ?item ?property ?value.
}
select ?value -> ?resultList.

# С кортежами
from {
    ?item ?prop1 ?val1.
    ?item ?prop2 ?val2.
}
select (?val1 ?val2) -> ?tupleList.
```

## СТРОКОВЫЕ ФУНКЦИИ

```n3
# Форматирование
("Text {0} and {1}" ?var1 ?var2) string:format ?result.

# Обрезка пробелов
?str string:trim ?trimmed.

# Подстрока
(?str 4) string:substring ?substr.

# Регулярное выражение
(?str "^pattern$" "replacement") string:regexReplace ?result.

# Объединение списка
(" " ?list) cmwstring:join ?joined.

# Нижний регистр
?str cmwstring:toLower ?lower.
```

## МАТЕМАТИКА

```n3
# Остаток
(?val 4) cmwnullable:remainder ?rem.

# Умножение
(?val1 ?val2) cmwnullable:product ?prod.

# Сложение
(?val1 ?val2) cmwnullable:sum ?sum.

# Среднее
(?val1 ?val2) cmwnullable:average ?avg.

# Максимум
?list cmwnullable:max ?maxVal.

# Округление вверх
?val cmwnullable:ceiling ?ceil.

# Начало дня
?date cmwnullable:startOfDay ?start.

# Сравнение
?val1 cmwnullable:greaterThan ?val2.
```

## СПИСКИ

```n3
# Сортировка
?list cmwlist:ascending ?sorted.

# Элемент по индексу
(?list ?index) cmwlist:at ?element.

# Членство
?list list:member ?member.

# Распаковка кортежа
?tuple -> (?var1 ?var2 ?var3).
```

## ЛОГИЧЕСКИЕ ОПЕРАТОРЫ

```n3
# Множественное ИЛИ
or{?var == "val1".}
or{?var == "val2".}
or{?var == "val3".}

# Альтернативные блоки
or {?val1 -> ?result.}
or {?val2 -> ?result.}.

# Отрицание
if {not{?item ?prop ?.}.}
then {?item ?prop ?val.}.

# Один раз
once{?item ?prop ?val.}
```

## СРАВНЕНИЯ

```n3
?var == "value"
?var != "value"
?var1 == ?var2
?num == 0.
?bool == true.
```

## НАЗНАЧЕНИЕ

```n3
?result -> ?value.
true -> ?value.
"text" -> ?value.
?tuple -> (?var1 ?var2).
```

## СПЕЦИАЛЬНЫЕ КОНСТРУКЦИИ

```n3
# Поиск свойства
("Type" "Property") object:findProperty ?prop.

# Контекст сессии
session:context var:key ?value.

# Текущий пользователь
cmw:securityContext cmw:currentUser ?user.

# Подсчет
{conditions.} assert:count ?count.

# Тип объекта
?obj a account:Account.

# Контейнер
?item cmw:container ?template.

# Алиас
?template object:alias "TypeName".
```

## РАБОТА С ДОКУМЕНТАМИ

```n3
# Содержимое
?doc document:content ?content.

# Заголовок
?doc document:title ?title.
```

## ПРИМЕРЫ КОМБИНАЦИЙ

### Условие с from-select
```n3
from {
    ?item ?prop ?val.
    ?val == "target".
}
select ?val -> ?list.

if {?list == "".}
then {"" -> ?result.}
else {?list -> ?result.}.
```

### Множественные условия
```n3
if {
    ?item ?prop1 ?val1.
    ?val1 == "target".
    or{?val2 == "opt1".}
    or{?val2 == "opt2".}
}
then {?result -> ?value.}
else {"" -> ?value.}.
```

### Математика со списками
```n3
from {
    ?item ?prop ?val.
}
select ?val -> ?list.

?list cmwlist:ascending ?sorted.
(?sorted 0) cmwlist:at ?first.
?list cmwnullable:max ?max.
```

## ЧАСТЫЕ ОШИБКИ

❌ `?var == "val"` без точки в условии if
✅ `?var == "val".` с точкой

❌ `if {condition}` без точки
✅ `if {condition.}` с точкой

❌ `then {block}` без точки после }
✅ `then {block.}` или `then {block}.` в зависимости от контекста

❌ `("text" var)` без пробела
✅ `("text" ?var)` с пробелом

❌ `?var->?result` без пробелов
✅ `?var -> ?result` с пробелами

❌ `if {?var == "val"}` регистр
✅ `if {?var == "val".}` нижний регистр

❌ `("Type""Property")` без пробела
✅ `("Type" "Property")` с пробелом
