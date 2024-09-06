---
title: Переменные
tags:
    - переменные
hide:
    - tags
kbId: 2207
---

# Переменные. Просмотр списка и настройка {: #variables}

## Введение

В приложениях предусмотрена возможность создания переменных — атрибутов с заданным значением, которые можно многократно использовать в C#-скриптах и выражениях на языке N3 в любом шаблоне приложения.

Переменные аналогичны атрибутам, которые не привязаны к какому-либо шаблону.

## Просмотр списка переменных и настройка переменной

1. В разделе «**[Администрирование][администрирование-приложения]**» приложения выберите пункт «**Переменные**» <i class="fa-light fa-dice-five"></i>.

2. Отобразится список переменных для данного приложения, со следующими сведениями:

    * **ID** — уникальный идентификатор переменной, формируется автоматически.
    * **Название** — наименование переменной.
    * **Системное имя** — уникальное имя переменной для обращения к ней.
    * **Тип** — тип значения, которое может храниться в переменной.
    * **Описание** — дополнительный комментарий относительно назначения шаблона.

    *![Список переменных приложения](variable_list.png)*

3. Нажмите кнопку «**Создать**» или дважды нажмите строку переменной в списке.
4. Настройте свойства переменной:

      * **Название** — наименование переменной.
      * **Системное имя** — уникальное имя переменной для обращения к ней.
      * **Тип** — тип значения переменной:
          * **Текст** — текстовая строка;
          * **Число** — числовое значение;
          * **Длительность** — длительность в днях, часах, минутах, секундах;
          * **Дата и время** — дата по календарю и время в днях, часах, минутах, секундах;
          * **Логический** — `истина` или `ложь`.
      * **Значение** — в соответствии с типом переменной:
          * введите текстовую строку;
          * введите число;
          * укажите длительность;
          * укажите дату в календаре и время;
          * установите или снимите флажок — (`истина`) или (`ложь`).
      * **Описание** — дополнительный комментарий относительно назначения переменной.

5. Сохраните переменную.

    *![Настройка переменной](variable_properties.png)*
{%
include-markdown "../.snippets/hyperlinks_mkdocs_to_kb_map.md"
%}