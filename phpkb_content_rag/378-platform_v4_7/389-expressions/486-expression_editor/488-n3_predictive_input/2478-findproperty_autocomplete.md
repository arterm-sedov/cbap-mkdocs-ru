---
title: 'Ввод запроса ID атрибута с помощью функции object:findProperty'
kbId: 2478
url: 'https://kb.comindware.ru/article.php?id=2478'
updated: '2023-08-23 11:39:16'
---

# Ввод запроса ID атрибута с помощью функции object:findProperty

## Инструкции

Функция `object:findProperty` возвращает ID атрибута шаблона по заданным системным именам шаблона и атрибута. По ID атрибута можно получить его значение. При предиктивном вводе для неё формируется заготовка и для ввода аргументов отображаются списки подходящих шаблонов и атрибутов.

1. Внутри фигурных скобок нажмите клавиши `Ctrl``Пробел`.
2. В отобразившемся списке конструкций дважды нажмите функцию `FindProperty`.

_![Список конструкций на языке N3](https://kb.comindware.ru/assets/n3_editor_findproperty_autocomplete.png)_

3. В выражение будет вставлена заготовка функции:

   `( ) object:findProperty ?foundProperty`
4. В позиции первого аргумента (после открывающей скобки) нажмите клавиши `Ctrl``Пробел`.
5. Отобразится список подходящих шаблонов в приложении.

_![Список шаблонов в приложении](https://kb.comindware.ru/assets/n3_editor_findproperty_argument1_autocomplete.png)_

6. Дважды нажмите системное имя шаблона, например `Zayavkanaotpusk`, чтобы вставить его в выражение.
7. В позиции второго аргумента (через пробел после первого) нажмите клавиши `Ctrl``Пробел`.
8. Отобразится список атрибутов шаблона, выбранного на шаге 4.

_![Список атрибутов шаблона](https://kb.comindware.ru/assets/n3_editor_findproperty_argument2_autocomplete.png)_

9. Дважды нажмите системное имя атрибута, например `_creationDate`, чтобы вставить его в выражение.

**Пример: выражение, возвращающее месяц по значению атрибута типа «Дата и время»**

```
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwtime: <http://comindware.com/logics/time#>.
{
    # Находим атрибут _creationDate шаблона Zayavkanaotpusk
    ("Zayavkanaotpusk" "_creationDate") object:findProperty ?dtProperty.

    # Определяем значение атрибута _creationDate
    # в текущей записи шаблона Zayavkanaotpusk
    ?item ?dtProperty ?dmonth.
    # Извлекаем номер месяца из значения атрибута _creationDate
    ?dmonth cmwutc:month ?value.
}
```

## Связанные статьи

**[Редактор выражений](https://kb.comindware.ru/article.php?id=2463)**

**[Примеры использования языка N3](https://kb.comindware.ru/category.php?id=408)**