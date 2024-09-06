---
title: Локальная переменная в C#-скрипте и сценарии. Копирование данных между шаблонами
tags:
    - C#
    - скрипт
    - C#-скрипт
    - кнопка 
    - копирование данных
    - локальная переменная
    - локальные переменные
hide: 
    - tags
kbId: 2630
---

# Локальная переменная в C#-скрипте и сценарии. Использование для копирования данных между шаблонами

## Введение

Локальные переменные для кнопки позволяют передавать введённые пользователем значения из диалогового окна кнопки в сценарий или C#-скрипт. Например, можно передать идентификатор выбранной пользователем записи для её последующей обработки.

Здесь представлена инструкция по настройке копирования данных из одного шаблона записи в другой с использованием локальной переменной и C#-скрипта или сценария по нажатию кнопки.

## Прикладная задача

Требуется копировать справочные данные (мастер-данные) в транзакционные данные, чтобы их можно было изменять в целевой записи, не влияя на исходный справочник.

Справочник (шаблон записи) _«Номенклатура продукции»_ содержит наименования, единицы измерения и стандартную цену товаров.

Шаблон записи _«Конкурсы»_ содержит информацию о проводимых конкурсах на закупку.

С конкурсами связан шаблон _«Позиции в конкурсе»_, в котором хранятся сведения о товарах, добавленных в конкурс на закупку, включая, например, количество и сумму закупки.

Требуется настроить кнопку, которая будет добавлять позиции из справочника, выбранные в таблице, в конкурс на закупку. При этом сведения о выбранных товарах должны копироваться из справочника в шаблон _«Позиции в конкурсе»_. В скопированных позициях можно будет изменять сведения для конкретного конкурса (например, цену), а сведения о товарах в справочнике должны оставаться неизменными.

## Настройка шаблонов записей

1. Создайте шаблон записи _«Номенклатура продукции»_ со следующими **атрибутами**:

    | Название            | Тип       | Свойства                                                  |
    | ------------------- | --------- | --------------------------------------------------------- |
    | _Наименование_      | **Текст** | **Использовать как заголовок записей:** флажок установлен |
    | _Единица измерения_ | **Текст** |                                                           |
    | _Цена_              | **Число** | **Количество знаков после запятой: 2**                    |

2. Добавьте созданные атрибуты на **форму** и в таблицу _«Все записи»_.
3. Создайте шаблон записи _«Позиции в конкурсе»_ с **атрибутами**:

    | Название            | Тип       | Свойства    |
    | ------------------- | --------- | ----------  |
    | _Наименование_      | **Текст** | **Использовать как заголовок записей:** флажок установлен |
    | _Единица измерения_ | **Текст** |                                        |
    | _Цена_              | **Число** | **Количество знаков после запятой: 2** |
    | _Количество_        | **Число** | **Количество знаков после запятой: 0** |
    | _Сумма_             | **Число** | <p>**Количество знаков после запятой: 2**</p><p>**Вычислять автоматически:** флажок установлен</p><p>**Вычисляемое значение: формула**</p><pre>`#!csharp PRODUCT($Tsena, $Kolichestvo)`</pre><p>**Здесь:**</p><p>`PRODUCT()` — вычисляет произведение двух чисел.</p><p>`Tsena` — системное имя атрибута _«Цена»_.</p><p>`Kolichestvo` — системное имя атрибута _«Количество»_.</p> |

4. Создайте шаблон записи _«Конкурсы»_ с **атрибутами**:

    | Название           | Тип        | Свойства |
    | ------------------ | ---------- | ------------------ |
    | _Название_         | **Текст**  | **Использовать как заголовок записей:** флажок установлен |
    | _Позиции конкурса_ | **Запись** | <p>**Связанный шаблон:** _Позиции в конкурсе_</p><p>**Хранить несколько значений:** флажок установлен</p><p>**Взаимная связь с атрибутом:** **с новым**</p><p>**Название:** _Конкурс_</p> |

5. Добавьте атрибуты _«Название»_ и _«Позиции конкурса»_ на **форму**.
6. Выберите для атрибута _«Позиции конкурса»_ отображение в виде таблицы и добавьте в неё созданные атрибуты.

## Настройка кнопки для копирования данных

### Настройка кнопки с использованием C#-скрипта

1. Создайте кнопку _«Добавить позиции в конкурс»_ в шаблоне _«Номенклатура продукции»_.
2. На вкладке «**Локальные переменные**» создайте переменную со следующими свойствами:

    - **Отображаемое название:** _Конкурс_
    - **Тип данных: запись**
    - **Системное имя:** _konkurs_
    - **Шаблон:** _Конкурсы_

3. На вкладке «**Основные**» настройте свойства кнопки:

    - **Отображаемое название:** _Добавить позиции в конкурс_
    - **Контекст операции: запись**
    - **Операция: C# скрипт**
    - **Результат выполнения: обновить данные**
    - **Отображать диалоговое окно:** флажок установлен

4. Сохраните кнопку.
5. Нажмите гиперссылку «**Настроить диалоговое окно**».
6. Вынесите локальную переменную _«Конкурс»_ на форму диалогового окна и сохраните её.
7. На вкладке «**Скрипт**» вставьте следующий код:

    ``` cs
    using System; 
    using System.Collections.Generic;
    using System.Linq;
    using Comindware.Data.Entity;
    using Comindware.TeamNetwork.Api.Data.UserCommands;
    using Comindware.TeamNetwork.Api.Data;

    class Script
    {
        public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
        {
            var data = userCommandContext.LocalVariables;
            string konkursId = "";
            string notify = "Позиции добавлены в выбранный конкурс";
            // Получаем ID конкурса из локальной переменной с системным именем konkurs
            data.TryGetValue("konkurs", out object obj_);
            if (obj_ != null)
            {
                konkursId = (obj_ as object[]).FirstOrDefault().ToString();
            }
            // Проверяем, что в таблице выбрана хотя бы одна строка
            if (userCommandContext.ObjectIds.Count() == 0)
            {
                var resultBad0 = new UserCommandResult
                {
            Success = false,
            Commited = false,
            ResultType = UserCommandResultType.Notificate,
            Messages = new[]
            {
            new UserCommandMessage
            {
                Severity = SeverityLevel.Normal,
                Text = "Ни одной позиции не выбрано"
            }
            }
        };
        return resultBad0;
            }
            
            Decimal posNum = 0;
            foreach (string selectId in userCommandContext.ObjectIds)
            {
                Dictionary<string,object> data_new = new Dictionary<string,object>();
                
                // Собираем данные из шаблона записи «Номенклатура продукции»
                var data_selectId = Api.TeamNetwork.ObjectService.GetPropertyValues(new String[]{selectId}, new String[]{"Naimenovanie", "Edinitsaizmereniya", "Tsena"});
                // Копируем значения атрибутов шаблона «Номенклатура продукции» в атрибуты позиции в конкурсе
                if (data_selectId[selectId].ContainsKey("Naimenovanie"))
                    data_new.Add("Naimenovanie", data_selectId[selectId]["Naimenovanie"]);
                if (data_selectId[selectId].ContainsKey("Edinitsaizmereniya"))
                    data_new.Add("Edinitsaizmereniya", data_selectId[selectId]["Edinitsaizmereniya"]);
                if (data_selectId[selectId].ContainsKey("Tsena"))
                                data_new.Add("Tsena", data_selectId[selectId]["Tsena"]);
                data_new.Add("Produktsiyanazakupku", data_selectId[selectId]["id"]);
                // Если конкурс выбран, проставляем ссылку на него в текущую позицию
                if (konkursId != "") 
                {
                    // Konkurs — системное имя атрибута «Конкурс» шаблона записи «Позиции в конкурсе»
                    data_new.Add("Konkurs", konkursId);
                }
                posNum++;

                // Создаём запись в шаблоне Pozitsiivkonkurse (Позиции в конкурсе) со скопированными данными
                Api.TeamNetwork.ObjectService.CreateWithAlias("Pozitsiivkonkurse", data_new);
            }

        // Завершаем работу скрипта    
        var result = new UserCommandResult
        {
                Success = true,
                Commited = true,
                ResultType = UserCommandResultType.Navigate,
                NavigationResult = new UserCommandNavigationResult
                {
                    Context = ContextType.Task,
                },
                Messages = new[]
        {
            new UserCommandMessage
            {
                Severity = SeverityLevel.Normal,
                Text = notify
            }
        }
        };
        return result;
        }
    }
    ```

8. Сохраните С#-скрипт.
9. Сохраните кнопку.
10. Вынесите кнопку _«Добавить позиции в конкурс»_ на область кнопок таблицы _«Все записи»_ шаблона _«Номенклатура продукции»_.

### Настройка кнопки с использованием сценария

1. Создайте в шаблоне _«Позиции в конкурсе»_ атрибут типа «**Запись**» _«Исходная позиция»_, связанный с шаблоном _«Номенклатура продукции»_.
2. Создайте кнопку _«Добавить позиции в конкурс»_ в шаблоне _«Номенклатура продукции»_.
3. На вкладке «**Локальные переменные**» создайте переменную со следующими свойствами:

    - **Отображаемое название:** _Конкурс_
    - **Тип данных: запись**
    - **Системное имя:** _konkurs_
    - **Шаблон:** _Конкурсы_

4. На вкладке «**Основные**» настройте свойства кнопки:

    - **Отображаемое название:** _Добавить позиции в конкурс_
    - **Контекст операции: запись**
    - **Операция: вызвать событие «Нажата кнопка»**
    - **Результат выполнения: обновить данные**
    - **Отображать диалоговое окно:** флажок установлен

5. Сохраните кнопку.
6. Нажмите гиперссылку «**Настроить диалоговое окно**».
7. Вынесите локальную переменную _«Конкурс»_ на форму диалогового окна и сохраните её.
8. Вынесите кнопку _«Добавить позиции в конкурс»_ на форму таблицы записей шаблона _«Номенклатура продукции»_.
9. Создайте новый сценарий _«Добавить позиции в конкурс»_.
10. В начальном событии «**Нажата кнопка**» выберите контекстный шаблон _«Номенклатура продукции»_ и кнопку _«Добавить позиции в конкурс»_.
11. Добавьте новое событие «**Создать запись**» с целевым шаблоном _«Позиции в конкурсе»_.
12. Внутри события «**Создать запись**» добавьте событие «**Изменить значения атрибутов**».
13. Добавьте следующие атрибуты для изменения:

    | Атрибут           | Операция со значениями        | Значение |
    | ------------------ | ---------- | ------------------ |
    | _Конкурс_         | **Заменить**  | <p>**Формула:** `$$dialogVariables->konkurs`</p><p>**Здесь:**</p><p>`dialogVariables` —  объект с локальными переменными кнопки, которая вызвала сценарий по событию «**Нажатие кнопки**»</p><p>`konkurs` — системное имя локальной переменной _«Конкурс»_.</p> |
    | _Исходная позиция_ | **Заменить** | <p>**Формула:** `$$origin`</p><p>**Здесь:**</p><p><p>`origin` — системная переменная, хранящая ID записи, для которой была нажата кнопка.</p> |
    | _Наименование_ | **Заменить** | <p>**Атрибут:** _Исходная позиция→Наименование_</p> |
    | _Единица измерения_ | **Заменить** | <p>**Атрибут:** _Исходная позиция→Единица измерения_</p> |
    | _Цена_ | **Заменить** | <p>**Атрибут:** _Исходная позиция→Цена_</p> |

_![Сценарий с использованием локальной переменной](script_using_local_variable_scenario.png)_
{{ pdfEndOfBlockHack }}

## Тестирование

1. Создайте и заполните несколько записей в шаблоне _«Номенклатура продукции»_.

    _![Добавление позиций из справочника продукции в конкурс](script_using_local_variable_add_items_from_registry.png)_

2. Создайте запись в шаблоне _«Конкурсы»_, например _«Конкурс №1»_.
3. Выберите одну или несколько позиций в таблице _«Номенклатура продукции»_ и нажмите кнопку _«Добавить позиции в конкурс»_.
4. Выберите _«Конкурс №1»_ в раскрывающемся в списке и нажмите кнопку _«Добавить позиции в конкурс»_.

    _![Выбор конкурса для добавления позиций](script_using_local_variable_select_tender.png)_

5. Откройте запись _«Конкурс №1»_.
6. В таблице _«Позиции в конкурсе»_ должны отобразиться выбранные товары с единицей измерения и ценой из справочника.
7. Отредактируйте цену продукции в любых позициях.
8. Сохраните запись.
9. Удостоверьтесь, что исходные цены в справочнике остались неизменными.

    _![Отображение добавленных позиций в конкурсе](img/script_using_local_variable_tender_positions.png)_

--8<-- "related_topics_heading.md"

**[Кнопки. Определения, настройка, удаление][buttons]**

**[Написание скриптов на языке C#][manual_csharp]**

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}