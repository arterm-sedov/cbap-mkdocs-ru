---
title: Урок 2. Мой первый реестр данных
kbId: 4873
---

# Урок 2. Мой первый реестр данных {: #lesson_2 }

## Введение

В рамках обучения мы разработаем корпоративное приложение для заказа корпоративного транспорта.

В ходе этого урока вы создадите **приложение**, **шаблон записи** (реестр заявок), настроите **атрибуты** для хранения данных заявок, их отображение в виде **таблицы** и **формы**, а затем оформите несколько заявок.

!!! warning "Бизнес-логика"

    Мы реализуем следующий процесс бронирования автомобиля:

    1. _Заказчик_ подает заявку на автомобиль.
    2. _Секретарь_ рассматривает и одобряет либо отклоняет заявку.
    3. Если запрос одобрен:

        - _Диспетчер гаража_ назначает транспортное средство для поездки.
        - _Заказчик_ получает уведомление о бронировании автомобиля.
        - _Водитель_ выполняет поездку.

    4. Если запрос отклонен, _Заказчик_ получает уведомление об отказе.

    Подробные сведения о приложениях в **{{ productName }}** см. в разделе «[Разработка приложений][apps_kb]».

**Предусловия:** выполнена авторизация, пройден _[урок 1 «Первое знакомство»][lesson_1]_.

**Расчётная продолжительность:** 60 мин.

{% include-markdown ".snippets/tutorial_version_notice.md" %}

<div class="admonition question" markdown="block">

## Определения {: .admonition-title #definitions}

- **Приложение** — настроенная в **{{ productName }}** совокупность  бизнес-процессов, диаграмм, моделей данных, экранных форм, механизмов обработки данных и ролевой модели для решения определённых задач.
- **Шаблон записи** — модель бизнес-сущности (в виде атрибутов) и хранилище (реестр) данных в **{{ productName }}** (аналог таблицы реляционной базы данных или листа Excel). Записи из шаблона могут быть представлены в виде таблиц, карточек и форм. Подробные сведения о шаблонах представлены в статье _«[Шаблоны. Определения и настройка][record_templates]»_.
- **Запись** — набор данных (значений атрибутов) в шаблоне, описывающий экземпляр бизнес-сущности (элемент справочника, транзакцию и т.&nbsp;п.).
- **Атрибут** — простейший элемент данных, описывающий бизнес-сущность (аналог поля в реляционной БД или столбца в Excel), например: место подачи (строка), количество пассажиров (число), время подачи автомобиля (дата/время), автомобиль (ссылка) и т.&nbsp;п.
- **Форма** — страница с полями для отображения и ввода данных.
- **Таблица** — список, содержащий записи в строках со значениями атрибутов в столбцах. В таблице можно настроить фильтры для для отображения определённых записей.

</div>

## Создание приложения

Создадим приложение для автоматизации заявок на корпоративный автотранспорт.

!!! tip "Совет"

    Во всех последующих инструкциях и уроках, необходимость изменения любых параметров при настройке приложения указана явно. Если не указано изменение какого-либо параметра, это означает, что его состояние при настройте следует оставлять неизменным (исходным по умолчанию).

    То есть при прохождении уроков во время настройки приложения и других элементов изменяйте только те поля, значения и флажки, которые указаны в инструкциях. Не изменяйте остальные параметры.

    Соблюдение этой рекомендации поможет достичь ожидаемого поведения результирующего приложения.

    При этом вы можете экспериментировать со значениями полей при заполнении форм во время тестирования приложения в роли конечного пользователя.

1. На панели навигации слева выберите пункт «**Настройки**» — «**Приложения**».
2. Нажмите кнопку «**Создать**».

    _![Переход к созданию приложения](img/lesson_2_app_create.png)_

3. Введите наглядное название приложения, например _«Управление автопарком»_. После заполнения имени поле «**Системное имя**» заполнится автоматически, при желании вы можете ввести собственное системное имя.

    !!! question "Системное имя и отображаемое название"

        - У сущностей в **{{ productName }}** предусмотрены **системное имя** и **название**.
        - **Системное имя** — это идентификатор сущности (атрибута, шаблона, поля и т.&nbsp;п.), используемый в сценариях, скриптах, правилах, формулах и выражениях.
            --8<-- "system_name_requirements.md"
        - **Название** и **отображаемое название** — это наглядная подпись сущности (атрибута, шаблона, формы, поля, кнопки, таблицы и т.&nbsp;п.). Название может содержать любые символы и по возможности должно быть кратким и понятным.

4. Нажмите кнопку «**Сохранить**».

    _![Настройка свойств нового приложения](img/lesson_2_app_configure.png)_

5. Дважды нажмите строку созданного приложения в списке.
6. Отобразится страница «**Администрирование**» приложения.

    _![Переход к странице администрирования приложения](img/lesson_2_app_list.png)_

## Создание шаблона записи

Определим данные заявки на автомобиль, которые необходимо хранить в **шаблоне записи**.

Создадим шаблон записи для заявки на автомобиль.

1. На странице «**Администрирование**» приложения _«Управление автопарком»_. выберите пункт «**Шаблоны**» <i class="fa-light fa-briefcase "></i>.

    _![Переход к списку шаблонов приложения](img/lesson_2_template_list_open.png)_

2. Отобразится список всех шаблонов приложения.
3. Выберите вкладку «**Шаблоны записей**».
4. Нажмите кнопку «**Создать**».

    _![Переход к созданию шаблона записи](img/lesson_2_record_template_create.png)_

5. Отобразится окно «**Новый шаблон**».
6. В поле «**Название**» введите наглядное наименование шаблона — _«Заявки на автомобили»_.
7. **Системное имя** будет заполнено автоматически.
8. В поле «**Тип шаблона**» должно быть автоматически выбрано значение «**Шаблон записи**».
9. Остальные поля оставьте без изменений.
10. Нажмите кнопку «**Создать**».

    _![Создание шаблона записи](img/lesson_2_record_template_configure.png)_

## Создание атрибутов шаблона записи

Добавим атрибуты заявки на автомобиль.

Мы создадим минимальный набор атрибутов, необходимый для оформления и обработки заявки на корпоративный автомобиль.

!!! note "Примечание"

    Следуя гибкой методологии, на начальном этапе мы не зададим все атрибуты, а ограничимся минимально необходимыми.
   
    Наша цель — как можно быстрее сделать работоспособное приложение и показать первым пользователям.
   
    Затем, получив от обратную связь от пользователей, мы будем добавлять в нашу таблицу новые атрибуты и вносить другие доработки по их пожеланиям.

!!! question "Типы атрибутов"

    В **{{ productName }}** предусмотрены атрибуты различных типов для хранения бизнес-данных.

    - **Текст** — строковое значение. Можно выбрать **формат отображения** значения атрибута:
        - **Обычный текст** — без форматирования;
        - **Размеченный текст** — базовое форматирование (жирный, курсив, списки).
        - **HTML-текст** — расширенное форматирование с помощью тегов HTML.
        - **Телефон (РФ)**, **Адрес эл.&nbsp;почты**, **Паспорт (РФ)**, **Индекс (РФ)**, **ИНН юрлица**, **ИНН физлица**, **ОГРН (РФ)**, **Регистрационный номер ТС (РФ)**, **Особая маска** — значение атрибута форматируется с использованием маски в виде регулярного выражения.
    - **Число** — числовое значение. Можно выбрать **количество знаков после запятой**:
        - **Не преобразовывать** — значение отображается в том же формате, что его ввёл пользователь;
        - **0** — значение отображается в виде целого числа;
        - **1–6** — значение отображается в виде десятичной дроби с указанным количеством знаков после запятой;
    - **Дата и время** — значение даты и времени. Доступно несколько **форматов отображения**, позволяющих выводить либо только дату, либо дату и время.
    - **Документ** — к атрибуту можно прикрепить любые файлы, например в формате Word, PDF или ZIP.
    - **Изображение** — к атрибуту можно прикрепить изображения, например сканы документов или фотографии.

    Кроме того, **{{ productName }}** поддерживает атрибуты следующих типов: **Аккаунт**, **Гиперссылка**, **Длительность**, **Запись**, **Логический**, **Организационная единица**, **Роль**, **Список значений**. С некоторыми из них мы познакомимся позже.

    Подробные сведения об атрибутах см. в статье _«[Атрибуты. Определения и настройка][attributes]»_

1. Выберите вкладку «**Атрибуты**».
2. Нажмите кнопку «**Создать**».

    _![Переход к созданию атрибута шаблона записи](img/lesson_2_attribute_create.png)_

3. Отобразится окно «**Новый шаблон**».
4. Выберите **тип данных** «**Текст**».
5. Введите **название** _«Место подачи»_.
6. **Системное имя** будет заполнено автоматически.
7. Остальные поля оставьте без изменений.
8. Нажмите кнопку «**Сохранить**».

    _![Настройка свойств атрибута](img/lesson_2_attribute_configure.png)_

9. Аналогично создайте следующие атрибуты:

    | Тип данных       | Название       |
    | ---------------- | -------------- |
    | **Дата и время** | _Время подачи_ |
    | **Текст**        | _Маршрут_      |
    | **Число**        | _Пассажиры_    |

## Создание формы для просмотра и ввода данных

Теперь настроим экранную форму для просмотра и ввода данных заявки на автомобиль.

1. На странице шаблона записи _«Заявки на автомобили»_ выберите вкладку «**Формы**».

    !!! note "Основная форма шаблона"

        При создании шаблона записи автоматически создаётся пустая **основная форма**, в которой по умолчанию открываются записи шаблона.
       
        Для шаблона записи _«Заявки на автомобили»_ была создана форма _«Заявки на автомобили — Основная форма»_.

2. В списке форм дважды нажмите пункт _«Заявки на автомобили — Основная форма»_.

    _![Переход к редактированию формы из списка](img/lesson_2_form_edit.png)_

3. Отобразится **конструктор формы**:

    _![Конструктор формы](img/lesson_2_form_designer.png)_

    !!! question "Конструктор формы"

        **Конструктор формы** разбит на четыре области:

        **(1)** **Панель элементов** — палитра элементов, которые можно перетащить на форму: атрибуты и вспомогательные визуальные элементы (**Область**, **Вкладки**, **Группа кнопок**, **Разделитель кнопок**, **Колонки**, **Статичный текст**).

        **(2)** **Макет формы** — эскиз экранной формы.

        **(3)** **Панель свойств** — позволяет просмотреть и изменить свойства выбранного элемента.

        **(4)** **Кнопки** — **Сохранить**, **Очистить**, **Клонировать**, **Настроить шаблон** <i class="fa-light  fa-pen-square"></i>, **Связи** <i class="fa-light  fa-link-horizontal"></i>.

        В **конструкторе форм** предусмотрен богатый набор элементов и функций, но в данном уроке мы рассмотрим только основные из них. Вы можете самостоятельно поэкспериментировать с элементами и настройками формы.
       
        Подробные сведения о настройке форм см. в статье _«[Формы. Определения и настройка][forms]»_.

4. Перетащите на макет формы элемент «**Область**» с панели элементов.
5. Перетащите на макет формы атрибут _«Время подачи»_ с панели элементов.

    _![Перетаскивание атрибута на форму](img/lesson_2_form_add_field.png)_

6. Аналогичным образом перетащите на макет формы атрибуты _«Место подачи», «Маршрут», «Пассажиры»_.

    !!! warning "Бизнес-логика"

        В поле _«Время подачи» Заказчик_ должен вводить дату и время. Но по умолчанию для этого атрибута выбран **формат отображения** только даты. Изменим формат отображения атрибута.

7. На панели элементов щелкните значок «**Редактировать**» <i class="fa-light fa-pencil"></i> у атрибута _«Время подачи»_.

    _![Переход к редактированию атрибута из панели элементов](img/lesson_2_form_edit_attribute.png)_

8. Отобразится окно свойств атрибута.
9. Выберите **формат отображения**, включающий время, например «**4 сент. 1986 г. 07:30**».
10. Нажмите кнопку «**Сохранить**».

    _![Выбор формата отображения атрибута типа «Дата / время»](img/lesson_2_attribute_date_time_edit.png)_

### Назначение обязательных для заполнения полей

1. Выберите на форме поле _«Время подачи»_.
2. В поле «**Доступ**» на панели свойств поля выберите режим «**Требовать ввод**».

    _![Выбор режима доступа к полю в форме](img/lesson_2_form_field_access_select.png)_

3. Аналогично сделайте обязательным поле _«Место подачи»_.

    !!! note "Визуальные элементы формы"

        Чтобы сделать форму более удобной для пользователя, используйте следующие элементы:

        - **Область** — визуально группирует поля, имеет заголовок и может содержать кнопки. На форме должна быть как минимум одна область.
        - **Статичный текст** — отображает текст, доступный только для чтения.
        - **Вкладки** — позволяет распределить поля по вкладкам, между которыми пользователь может переходить.
        - **Колонки** — позволяет расположить поля в несколько столбцов.

4. Перетащите на форму элемент «**Колонки**» с панели элементов.
5. Перетащите поля _«Время подачи»_ и _«Место подачи»_ с макета формы соответственно в левый и правый столбцы элемента «**Колонки**».

    _![Упорядочивание элементов формы с помощью колонок](img/lesson_2_form_columns_arrange.png)_

6. Выберите заголовок **новой области** и с помощью панели свойств присвойте её наглядное **отображаемое название**: _Форма заявки на автомобиль_.
7. Сохраните форму, нажав кнопку «**Сохранить**» в конструкторе форм.

    _![Переименование области формы и сохранение формы](img/lesson_2_form_rename.png)_

## Тестирование: ввод и редактирование заявок

Мы создали форму для заявки на автомобиль. Теперь мы протестируем её от лица _Заказчика_.

1. Нажмите кнопку «**Настроить шаблон**» <i class="fa-light fa-pen-square"></i>.

    _![Переход из конструктора формы к настройке шаблона записи](img/lesson_2_form_template_edit.png)_

2. Нажмите кнопку «**Перейти к экземплярам**».

    _![Переход к списку записей шаблона](img/lesson_2_template_open_record_list.png)_

3. Отобразится список записей шаблона.
4. Нажмите кнопку «**Создать**», чтобы оформить новую заявку на автомобиль — запись в шаблоне.

    _![Переход к созданию записи из списка записей шаблона](img/lesson_2_template_record_create.png)_

5. Откроется _форма заявки на автомобиль_.
6. Заполните все поля и нажмите кнопку «**Сохранить**».

    _![Заполнение заявки на автомобиль](img/lesson_2_request_create.png)_

7. Нажмите ссылку «**Заявки на автомобили**» над формой, чтобы вернуться к списку заявок.

    _![Переход с формы к списку записей шаблона](img/lesson_2_request_return_to_list.png)_

8. Создайте несколько заявок на автомобиль таким же образом.
9. Созданные записи будут отображаться в списке.
10. Двойным нажатием в списке записей откройте созданную запись, измените данные заявки и сохраните её.

    _![Открытие записи из списка](img/lesson_2_template_record_open.png)_

## Доработка формы: добавление поля согласования заявки секретарем

Созданную заявку должен рассмотреть _Секретарь_, но в шаблоне записи _«Заявки на автомобили»_ не хватает атрибута для результата рассмотрения заявки. Добавим этот атрибут.

1. Перейдите к настройке шаблона записи. Для этого нажмите кнопку «**Мои настройки**» <i class=" fa-light fa-edit ">‌</i> на странице «**Все записи**» и выберите пункт «**Настроить шаблон**».

    _![Переход к настройкам шаблона из списка записей](img/lesson_2_template_edit_from_list.png)_

2. На странице шаблона записи выберите вкладку «**Атрибуты**».
3. Нажмите кнопку «**Создать**».

    _![Переход к созданию атрибута в шаблоне](img/lesson_2_template_attribute_create.png)_

4. Отобразится окно «**Новый атрибут**».
5. Введите **название** _«Заявка одобрена»_ и выберите **тип данных** «**Логический**».
6. Нажмите кнопку «**Сохранить**».

    _![Создание атрибута «Заявка одобрена» типа «Логический»](img/lesson_2_template_attribute_configure.png)_

## Настройка таблицы со списком записей

В шаблоне записи по умолчанию предусмотрена таблица «**Все записи**», которая показывает список заявок и системные атрибуты: **ID**, **Создатель**,  **Дата создания**, **В архиве**, **Дата изменения**.

Список заявок на автомобили в таблице «**Все записи**» не информативен, так как не содержит необходимых данных о заявке. Доработаем этот список.

1. Перейдите на вкладку «**Таблицы**» шаблона записи и дважды нажмите строку «**Все записи**».

    _![Переход к конструктору таблицы](img/lesson_2_template_table_edit.png)_

2. Отобразится конструктор таблицы, который позволяет настроить набор и порядок отображения столбцов.

3. Для начала удалим столбцы, которые пользователю не интересны.
4. Выберите элемент «**ID**» в макете таблицы и перетащите его за пределы макета, например на панель элементов.
5. Таким же образом уберите из таблицы столбцы «**Дата создания**», «**В архиве**» и «**Используется в процессе**».
6. Оставьте в таблице столбцы «**Создатель**» и «**Дата изменения**».

    _![Конструктор таблицы — удаление столбцов](img/lesson_2_table_designer_column_delete.png)_

7. Теперь добавим в таблицу необходимые столбцы.
8. Перетащите следующие атрибуты с панели элементов на макет таблицы: _«Время подачи», «Место подачи», «Маршрут», «Пассажиры»_.

    !!! note "Примечание"

        Последовательность, в которой элементы расположены в конструкторе таблицы, определяет последовательность столбцов при её отображении. То есть элемент, который расположен вверху в конструкторе таблицы, отобразится первым (слева) в таблице.

9. Нажмите кнопку «**Сохранить**».
10. Будут сохранены параметры отображения таблицы по умолчанию для всех пользователей.
11. В меню <i class="fa-light fa-edit">‌</i> выберите пункт «**Настроить шаблон**».

    _![Конструктор таблицы — добавление столбцов и возврат к настройке шаблона](img/lesson_2_table_designer_column_add.png)_

12. Отобразится вкладка «**Свойства**» шаблона.
13. Нажмите кнопку «**Перейти к экземплярам**», чтобы открыть список заявок в виде таблицы с настроенными столбцами.

    _![Таблица со список заявок на автомобили с настроенными столбцами](img/lesson_2_request_list.png)_

## Поиск и фильтрация записей в таблице

Используем дополнительные настройки отображения записей в таблице — отфильтруем и отсортируем записи в нужном нам порядке, затем настроим группировку и подсчет итогов.

### Настройка параметров фильтрации, сортировки и группировки записей списка для текущего пользователя

!!! note "Примечание"

    - В этом параграфе представлены инструкции по настройке параметров отображения столбцов таблицы для **текущего пользователя**. Эти настройки хранятся в платформе индивидуально для каждого пользователя.
    - Помимо этого, в конструкторе таблицы можно настроить параметры отображения столбцов, которые будут использоваться **для всех пользователей по умолчанию**. См. _«[Настройка и сохранение параметров сортировки, группировки, подсчета итогов и фильтрации данных в таблице для всех пользователей](#настройка-параметров-сортировки-группировки-подсчета-итогов-и-фильтрации-данных-в-таблице-для-всех-пользователей)»_.

#### Сортировка записи

Отсортируем заявки на автомобили по времени подачи.

1. Нажмите  заголовок столбца _«Время подачи»_, чтобы отсортировать данные по этому столбцу:

    - по возрастанию;
    - по убыванию;
    - по умолчанию.

    Порядок сортировки обозначается стрелкой вниз (по убыванию), стрелкой вверх (по возрастанию) или отсутствием стрелки (по умолчанию) в заголовке столбца.

    _![Сортировка таблицы нажатием заголовка столбца](img/lesson_2_table_sort.png)_

#### Фильтр записей

Для отображения записей, содержащих определённое значение, можно использовать фильтр «**Равно**» или «**Содержит строку**».

1. Нажмите значок фильтра <i class="fa-light fa-filter"></i> в столбце _«Маршрут»_.
2. В раскрывшемся меню установите флажок «**Фильтровать данные**» и выберите тип фильтра «**Начинается с**» или «**Содержит строку**».
3. Введите искомый текст для фильтра в поле «**Введите текст**», например первые буквы названия маршрута любой заявки.
4. Нажмите кнопку «**Сохранить**».

    _![Применение фильтра записей по содержимому столбца](img/lesson_2_table_filter.png)_

5. В списке отобразятся записи, соответствующие указанному фильтру.
6. Чтобы сбросить фильтр записей, нажмите значок фильтра <i class="fa-light fa-filter"></i> в столбце _«Маршрут»_, снимите флажок «**Фильтровать данные**» и нажмите кнопку «**Сохранить**».

    _![Отключение фильтрации записей в таблице](img/lesson_2_table_filter_disable.png)_

#### Группировка записей

Сгруппируем заявки на автомобиль с одинаковым маршрутом.

1. Нажмите значок фильтра <i class="fa-light fa-filter"></i> в столбце _«Маршрут»_.
2. В раскрывшемся меню установите флажок «**Группировать**» и нажмите кнопку «**Сохранить**».

    _![Группировка записей в таблице](img/lesson_2_table_group.png)_

#### Скрытие столбца

Скроем столбец «**Дата изменения**».

1. Нажмите кнопку <i class=" fa-light fa-edit ">‌</i> над таблицей
2. В раскрывшемся меню выберите пункт «**Настроить внешний вид**».

    _![Переход к пользовательской настройке внешнего вида таблицы](img/lesson_2_table_go_to_personal_config.png)_

3. Отобразится страница настройки внешнего вида таблицы.
4. Снимите флажок «**Дата изменения**», чтобы скрыть из таблицы этот столбец.
5. Нажмите кнопку «**Сохранить**».
6. Чтобы восстановить исходную конфигурацию отображения таблицы, нажмите кнопку «**Сбросить**».

    _![Настройка пользовательской конфигурации внешнего вида таблицы](img/lesson_2_table_personal_config.png)_

### Настройка параметров сортировки, группировки, подсчета итогов и фильтрации данных в таблице для всех пользователей

!!! note "Примечание"

    - В этом параграфе представлены инструкции по настройке параметров отображения столбцов таблицы, которые будут использоваться  **для всех пользователей по умолчанию**.
    - Кроме того, каждый пользователь может настроить отображение столбцов индивидуально в соответствии со своими потребностями. См. параграф _«[Настройка параметров фильтрации, сортировки и группировки записей списка для текущего пользователя](#настройка-параметров-фильтрации-сортировки-и-группировки-записей-списка-для-текущего-пользователя)»_.

1. Нажмите кнопку <i class=" fa-light fa-edit ">‌</i> и в раскрывшемся меню выберите пункт «**Настроить таблицу**».
2. Отобразится конструктор таблицы.

    _![Переход к конструктору таблицы](img/lesson_2_table_go_to_designer.png)_

3. Выберите вкладку «**Дополнительные**» в панели «**Свойства таблицы**».
4. Перетащите атрибуты из макета таблицы в области «**Сортировка**», «**Группировка**» и «**Фильтрация**».
5. Настройте параметры сортировки, группировки и фильтрации данных в таблице для всех пользователей.
6. Нажмите кнопку «**Сохранить**».

    _![Настройка параметров сортировки, группировки и фильтрации списка по умолчанию для всех пользователей](img/lesson_2_table_designer_advanced_properties.png)_

## Результаты

Вы создали свой первый шаблон записи (реестр данных), настроили форму, научились её заполнять и настроили таблицу со списком записей.

В [следующем уроке][lesson_3] вы узнаете, как спроектировать и запустить бизнес-процесс.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
