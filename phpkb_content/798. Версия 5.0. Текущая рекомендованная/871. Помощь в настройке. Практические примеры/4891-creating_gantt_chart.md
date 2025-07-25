---
title: Диаграмма Ганта. Настройка
kbId: 4891
---

# Диаграмма Ганта. Настройка

## Введение

На форме можно разместить диаграмму Ганта, которая будет строиться динамически по данным приложения.

Для формирования диаграммы Ганта потребуется настроить несколько шаблонов и атрибутов определённых типов.

См. также статью «**[Диаграмма Ганта. Использование][gantt_chart_use]**».

_![Пример диаграммы Ганта](https://kb.comindware.ru/assets/gantt_chart_example.png)_

## Настройка шаблонов и форм

1. Создайте три **[шаблона записи][record_templates]**:

   - *Работы*
   - *План работ*
   - *Зависимости работ*
2. В шаблоне *«Работы»* создайте и поместите на форму атрибуты:

   - *Дата начала*
   - *Дата начала плановая*
   - *Дата окончания*
   - *Дата окончания плановая*
     - **Тип данных: дата и время**
   - *Дочерние работы*
     - **Тип данных: запись**.
     - **Связанный шаблон**: *Работы*
     - **Хранить несколько значений**: флажок установлен.
     - **Взаимная связь с новым атрибутом**: *Родительская работа*.
   - *Зависимости работ*
     - **Тип данных: запись**.
     - **Связанный шаблон**: *Зависимости работ*.
     - **Хранить несколько значений**: флажок установлен.
     - **Взаимная связь с новым атрибутом**: *Зависимая работа*.
   - *Исполнитель*
     - **Тип данных: аккаунт**.
   - *Наименование работы*
     - **Тип данных: текст**.
     - **Использовать как заголовок записей**: флажок установлен.
   - *Позиция в иерархии*
     - **Тип данных: текст**.
   - *Прогресс*
     - **Тип данных: число**.
     - **Количество знаков после запятой: не преобразовывать**![Основная форма шаблона «Работы»](https://kb.comindware.ru/assets/creating_gantt_chart_work_template_form.png)

   Основная форма шаблона «Работы»
3. В шаблоне *«Зависимости работ»* создайте и поместите на основную форму атрибуты:

   - *Задержка*

     - **Тип данных: длительность**.
   - *Предшествующая работа*

     - **Тип данных: запись**.
     - **Связанный шаблон**: *Работы*.
   - *Наименование зависимости*

     - **Тип данных: текст**.
     - **Вычислять автоматически**: флажок установлен.
     - **Вычисляемое значение**:

     ```
     CONCAT(LIST($Predshestvuyuschayarabota->Naimenovanieraboty,
         " -> ",
         $Zavisimayarabota->Naimenovanieraboty))
     ```

     - Свойство «**Доступ**» на форме: **только чтение**.
   - *Тип связи*

     - **Тип данных: список значений**.
     - **Список значений** — четыре значения:

       Внимание!

       **Системные имена** значений данного атрибута должны быть именно такими, как указано ниже. В противном случае диаграмма Ганта не будет формироваться должным образом.

       | Системное имя | EN | RU |
       | --- | --- | --- |
       | *startToStart* | *Start to start* | *Начало-начало* |
       | *startToEnd* | *Start to end* | *Начало-окончание* |
       | *endToStart* | *End to start* | *Окончание-начало* |
       | *endToEnd* | *End to end* | *Окончание-окончание* |![Список значений атрибута «Тип связи»](https://kb.comindware.ru/assets/creating_gantt_chart_link_type_value_list.png)

   Список значений атрибута «Тип связи»

   ![Основная форма шаблона «Зависимости»](https://kb.comindware.ru/assets/creating_gantt_chart_work_dependency.png)

   Основная форма шаблона «Зависимости»
4. В шаблоне *«Планы работ»* создайте и **дважды** поместите на форму атрибут:

   - *Работы*

     - **Тип данных: запись**.
     - **Связанный шаблон**: *Работы*
     - **Хранить несколько значений**: флажок установлен.
     - **Взаимная связь с новым атрибутом**: *Связь*.![Основная форма шаблона «План работ»](https://kb.comindware.ru/assets/creating_gantt_chart_work_plan_form.png)

   Основная форма шаблона «План работ»
5. Для первого поля *«Работы»* на форме выберите **представление «Диаграмма Ганта»** и установите следующие свойства диаграммы, выбрав ранее созданные атрибуты:

   - **Наименование**: *Наименование работы*.
   - **Исполнитель**: *Исполнитель*.
   - **Дата начала плановая**: *Дата начала плановая*.
   - **Дата начала**: *Дата начала*.
   - **Дата окончания плановая**: *Дата окончания плановая*.
   - **Дата окончания**: *Дата окончания*.
   - **Процент выполнения**: *Прогресс*.
   - **Форма**: *Работы - Основная форма*.
   - **Дочерние работы**: *Дочерние работы*.
   - **Упорядочивание**: *Номер работы*.
   - **Зависимости**: *Зависимости*.
   - **Предшествующая работа**: *Предшествующая работа*.
   - **Типы связей**: *Тип связи*.
   - **Задержка/опережение**: *Задержка*.![Свойства диаграммы Ганта на форме](https://kb.comindware.ru/assets/creating_gantt_chart_properties.png)

   Свойства диаграммы Ганта на форме
6. Для второго поля *«Работы»* на форме выберите **представление «Таблица»** и установите следующие свойства таблицы, выбрав ранее созданные атрибуты:

   - **Доступ**: *Разрешить ввод*.
   - **Дочерние записи**: *Дочерние работы*.
   - **Упорядочивание**: *Номер работы*.
   - **Иерархическая нумерация**: *Позиция в иерархии*.
   - Перетащите на область кнопок таблицы кнопки **«Создать»**, **«Добавить»**, **«Исключить»**, **«Редактировать»**, **«Удалить»**.
   - Перетащите в таблицу атрибуты шаблона *«Работы»*:

     - *«Позиция в иерархии»* (свойство столбца **«Доступ»: только чтение**),
     - *«Наименование работы»*,
     - *«Исполнитель»*,
     - *«Прогресс»*,
     - *«Дата начала плановая»*,
     - *«Дата начала»*,
     - *«Дата окончания плановая»*,
     - *«Дата окончания»*,
     - *«Зависимости»* (в свойствах столбца установите флажки **«Разрешить создание записей»** и **«Разрешить редактирование записей»**).![Свойства таблицы работ на форме](https://kb.comindware.ru/assets/creating_gantt_chart_table_properties.png)

   Свойства таблицы работ на форме

--8<-- "related_topics_heading.md"

**[Диаграмма Ганта. Использование][gantt_chart_use]**

**[Шаблон записи][record_templates]**

**[Атрибуты. Определения, типы, настройка, архивирование, удаление][attributes]**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
