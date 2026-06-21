---
title: 'Ввод запроса списка записей шаблона по его системному имени с помощью функции object:alias'
kbId: 2481
url: 'https://kb.comindware.ru/article.php?id=2481'
updated: '2023-08-23 11:38:44'
---

# Ввод запроса списка записей шаблона по его системному имени с помощью функции object:alias

## Инструкции

Функция `object:alias` возвращает записи шаблона с заданным системным именем. При предиктивном вводе для неё формируется заготовка, отображается список подходящих шаблонов и формируется компактный запрос записей выбранного шаблона с использованием квадратных скобок.

1. Внутри фигурных скобок нажмите клавиши `Ctrl` `Пробел`.
2. В отобразившемся списке конструкций дважды нажмите функцию `ObjectAlias`.

_![Список конструкций на языке N3](https://kb.comindware.ru/assets/n3_editor_square_brackets_autocomplete.png)_

3. В выражение будет вставлена заготовка функции:

   ```
   a [object:alias ].
   ```

4. В позиции перед закрывающей квадратной скобкой нажмите клавиши `Ctrl` `Пробел`.
5. Отобразится список шаблонов в приложении.

_![Список шаблонов в приложении](https://kb.comindware.ru/assets/n3_editor_square_brackets_templates_autocomplete.png)_

6. Дважды нажмите системное имя шаблона, например `Zayavkanaotpusk`.
7. В выражение будет вставлен запрос записей выбранного шаблона:

   ```
   ?objectZayavkanaotpusk a [object:alias "Zayavkanaotpusk"].
   ```
8. Чтобы присвоить результат выражения значению вычисляемого атрибута, замените имя переменной `objectZayavkanaotpusk` на `value`.

**Пример: компактное выражение, возвращающее все записи шаблона по его системному имени**

```
@prefix object: <http://comindware.com/ontology/object#>.
{
  # Получаем список записей шаблона Zayavkanaotpusk
  ?value a [object:alias "Zayavkanaotpusk"].
}
```

**Эквивалентное выражение без квадратных скобок**

```
@prefix object: <http://comindware.com/ontology/object#>.
{
  # Получаем ID шаблона Zayavkanaotpusk
  ?zayavkiTemplate object:alias "Zayavkanaotpusk".
  # Получаем список записей шаблона Zayavkanaotpusk
  ?value a ?zayavkiTemplate.
}
```

## Связанные статьи

**[Редактор выражений](https://kb.comindware.ru/article.php?id=2463)**

**[Примеры использования языка N3](https://kb.comindware.ru/category.php?id=408)**