---
title: Диаграмма Ганта. Использование
tags:
  - диаграмма Ганта
  - Gantt chart
hide:
  - tags
kbId: 2108
---

# Диаграмма Ганта. Использование {: #using_gantt_chart}

В данном примере предполагается, что диаграмма Ганта создана по инструкциям в разделе **«[Создание диаграммы Ганта](creating_gantt_chart.md)»**.

1. Создайте и откройте запись в шаблоне _«План работ»_.
2. Создайте записи в шаблоне _«Работы»_ с помощью таблицы на форме _«План работ»_ например:
      * _Составить ТЗ_;
      * _Составить технические требования_.
3. Укажите исполнителей, даты начала и окончания работ.
4. Укажите прогресс работ в процентах (без символа %). Прогресс отображается на диаграмме как полоса более тёмного цвета на полосе планового хода работы.
*![Созданные работы в таблице](using_gantt_chart_example_works.png)*
4. Нажмите поле _«Зависимости»_ в строке работы _«Составить технические требования»_.
5. В раскрывающемся списке зависимостей нажмите кнопку **«Создать»**.
*![Создание зависимости работ](using_gantt_chart_example_create_dependency.png)*
6. В форме зависимости работ укажите тип связи работ. От типа связи будет зависеть положение и направление стрелки, связывающей работы на диаграмме:
   * Начало-начало;
   * Начало-окончание;
   * Окончание-начало;
   * Окончание-окончание.
*![Выбор типа связи работ](using_gantt_chart_link_types.png)*
1. Укажите задержку. Если указана задержка и у зависимой работы не указана дата начала или плановая дата начала, то отсутствующая дата будет равна сумме даты окончания предшествующей работы и задержки.
2. Выберите предшествующую и зависимую работы.
3. Нажмите кнопку **«OK»**, чтобы сохранить зависимость работ.
*![Зависимость работ](using_gantt_chart_dependency_example.png)*
4. Чтобы сделать работу _«Составить технические требования»_ дочерней для работы _«Составить ТЗ»_, установите для неё флажок выбора в первом столбце и нажмите кнопку **«На уровень ниже»**.
*![Перевод работы в статус дочерней](using_gantt_chart_child_work_example.png)*
5. Нажмите кнопку **«Сохранить»** в верхней части формы, чтобы сохранить запись плана работ.
6. Выберите интервал отображения диаграммы Ганта: **неделя**, **месяц**, **год** или **десятилетие**.
7. Установите или снимите флажок «**Ожидаемый ход работ**». Ожидаемый ход работ отображается в виде отдельной полосы над полосой планового хода работы.
*![Интервал отображения диаграммы и флажок отображения ожидаемого хода работ](using_gantt_chart_interval.png)*
1. Чтобы просмотреть сведения о работе, нажмите соответствующую полосу на диаграмме.
*![Сведения о работе на диаграмме](using_gantt_chart_work_details.png)*
9. Чтобы просмотреть сведения о зависимости работ, нажмите связывающую их стрелку на диаграмме.
*![Сведения о зависимости работ на диаграмме](using_gantt_chart_dependency_details.png)*

--8<-- "related_topics_heading.md"

**[Диаграмма Ганта. Настройка](creating_gantt_chart.md)**