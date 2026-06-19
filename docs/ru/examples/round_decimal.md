---
title: Округление вверх десятичного числа до двух знаков после запятой
kbId: 4958
tags:
    - N3
    - атрибуты
    - выражение на N3
    - пример
hide: tags
---

# Округление вверх десятичного числа до двух знаков после запятой {: #round_decimal }

Для того чтобы округлить десятичное число до двух знаков после  запятой (например, 16.782 до 16.79), введите следующее выражение:

```turtle
@prefix w3math: <http://www.w3.org/2000/10/swap/math#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwmath: <http://comindware.com/logics/math#>.
{
    (
        "Work" "Desyatichnoe") object:findProperty ?DesyatichnoeProperty.
    ?item ?DesyatichnoeProperty ?Desyatichnoe.
    (
        ?Desyatichnoe  100) w3math:product ?number1.
    ?number1 cmwmath:floor ?numberFloor.
    (
        ?number1  ?numberFloor ) cmwmath:difference ?difference.
    if {
        ?difference w3math:greaterThan 0.}
    then {
        (
            ?numberFloor  1 ) cmwmath:sum  ?number2.
        (
            ?number2 100) w3math:quotient ?value.}
    else{
        (
            ?number1 100) w3math:quotient ?value.}
    }
```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| `Work` | Системное имя текущего Шаблона записи. |
| `Desyatichnoe` | Системное имя атрибута типа «**Число**» (десятичное), который нужно округлить. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
