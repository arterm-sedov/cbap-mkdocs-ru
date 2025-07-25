---
title: Таблицы. Определения и настройка
kbId: 4800
---

# Таблицы. Определения и настройка

## Определения

**Таблица** — это представление данных в виде столбцов и строк.

- Строка таблицы содержит данные одной записи шаблона.
- Столбец таблицы содержит значения атрибутов записи.
- В каждом шаблоне можно настроить произвольное количество таблиц.
- Таблицы, доступные пользователю приложения, отображаются на отдельных вкладках.
- Для каждой таблицы предусмотрены два представления:
- [системное](#table_configure_template) — настраивается на уровне приложения с помощью конструктора таблицы. Это представление будет использоваться по умолчанию для пользователей.
- [пользовательское][table_personal_use] — настраивается пользователем для своего аккаунта. Например, пользователь может скрыть и переместить столбцы, отфильтровать, отсортировать и сгруппировать строки, подсчитать итоги.

В этом разделе представлены инструкции по настройке таблицы в шаблоне. См. также [*«Настройка таблицы на форме»*][form_dynamic_elements].

_![Вкладки с таблицами шаблона](/platform/v5.0/business_apps/templates/tables/img/table_definition_table_templates.png)_

## Просмотр списка и настройка таблиц в шаблоне

1. Откройте любой шаблон.
2. Выберите вкладку «**Таблицы**».
3. Отобразится список таблиц, настроенных для шаблона, с их свойствами.

   ![Список таблиц в шаблоне](/platform/v5.0/business_apps/templates/tables/img/table_definition_tables_list.png)

   Список таблиц в шаблоне
4. Создайте таблицу или дважды нажмите таблицу в списке.
5. Отобразится конструктор таблицы со следующими областями:

   **(1) Панель элементов** — содержит [атрибуты][attributes], которые можно [поместить в качестве столбцов](#table_configure_columns) в таблицу, а также кнопки для добавления в область кнопок.

   Совет

   Панель элементов позволяет создавать и редактировать атрибуты в шаблоне, не покидая конструктор таблицы.

   - Чтобы создать атрибут в текущем шаблоне, наведите указатель мыши на заголовок «**Атрибуты**» и нажмите кнопку «**Добавить атрибут**».
   - Чтобы создать атрибут в связанном с этим атрибутом шаблоне, наведите указатель на название **[атрибута типа запись][attribute_record]** и нажмите кнопку «**Добавить атрибут**».
   - Чтобы отредактировать атрибут, наведите указатель мыши на его название и нажмите кнопку «**Редактировать атрибут**».

   **(2) Область кнопок** — позволяет [настроить кнопки](#table_configure_buttons) для данной таблицы.

   **(3) Макет таблицы** — служит для [настройки столбцов](#table_configure_columns) таблицы.

   **(4) Панель свойств** — служит для настройки элемента, выбранного на макете: [таблицы](#table_configure_properties), [столбца](#table_configure_columns_properties) или [кнопок](#table_configure_buttons).

   **(5) Кнопки**

   - Сохранить — сохранение текущей конфигурации таблицы.
   - **Клонировать** — [создание дубликата](#table_configure_clone) таблицы.
   - **Очистить** — удаление всех столбцов таблицы.
   - **Связи** *‌* — просмотр списка сущностей, с которыми связана таблица.
   - **Перейти к таблице** *‌* — просмотр настроенной таблицы с данными в представлении для пользователя.
   - **Настроить шаблон** *‌* — переход к свойствам шаблона, к которому относится таблица.

   ![Области конструктора таблицы](/platform/v5.0/business_apps/templates/tables/img/table_settings_constructor_areas.png)

   Области конструктора таблицы
6. Настройте [свойства](#table_configure_properties) таблицы, [столбцы](#table_configure_columns) и [кнопки](#table_configure_buttons) таблицы.
7. Сохраните таблицу.

## Настройка свойств таблицы

Примечание

При создании шаблона автоматически создаётся таблица «**Все записи**» с перечисленными ниже столбцами. Эта таблица отображается по умолчанию при нажатии кнопки «**Перейти к экземплярам**» на странице свойств шаблона.

1. Создайте или откройте таблицу для редактирования.
2. Нажмите пустую область макета таблицы.
3. Справа от макета отобразится панель свойств таблицы
4. Настройте свойства таблицы на двух вкладках:

   - [**Основные**](#table_configure_properties_general)
   - [**Дополнительные**](#table_configure_properties_advanced):
     - [**Сортировка**](#table_configure_properties_advanced_sort)
     - [**Группировка**](#table_configure_properties_advanced_group)
     - [**Подсчёт итогов**](#table_configure_properties_advanced_summarize)
     - [**Фильтрация**](#table_configure_properties_advanced_filter)

### Основные свойства

- **Отображаемое название** — наглядный заголовок таблицы, который отображается в списке таблиц шаблона и для пользователей при просмотре таблицы.
- **Системное имя** — уникальное имя таблицы, которое используется в вычислениях.
  Не должно начинаться с цифры. Разрешены английские и русские буквы, цифры и символ «\_». Рекомендуется использовать английские буквы.
  Обычно заполняется автоматически по названию.
- **Ручная загрузка данных** — установите этот флажок , чтобы при открытии таблица отображалась без данных. Пользователь сможет настроить внешний вид таблицы, а затем нажать кнопку «**Загрузить данные**».

  ![Таблица с ручной загрузкой данных](/platform/v5.0/business_apps/templates/tables/img/table_settings_data_load_button.png)

  Таблица с ручной загрузкой данных
- **По умолчанию** — установите этот флажок, чтобы таблица отображалась по умолчанию при просмотре записей в шаблоне. В шаблоне можно назначить только одну таблицу по умолчанию. При этом, если пользователь откроет другую таблицу в шаблоне, она станет отображаться для него по умолчанию.
- **Показывать архивные записи** — установите этот флажок, чтобы в таблице отображались записи помещённые в архив, которые скрыты по умолчанию.
- **Отображение формы** — укажите способ отображения форм записей из таблицы:

  - **Нет** — при двойном нажатии строки таблицы форма с записью отобразится вместо таблицы;
  - **Вертикальное** — при нажатии строки в таблице форма записи отобразится справа от таблицы, границу между таблицей и формой можно будет перемещать с помощью мыши;
  - **Горизонтальное** — при нажатии строки в таблице форма записи отобразится под таблицей, границу между таблицей и формой можно будет перемещать с помощью мыши.
- **Записей на странице** — укажите количество строк отображающихся в таблице при её открытии, по умолчанию: 25.
- **Закрепить столбцы** — укажите количество столбцов начиная слева, которые не будут прокручиваться по горизонтали.
- **Карточки** — выберите представление карточек, которое будет использоваться для отображения данных таблицы в виде плиток. См. *«[Карточки][cards_configure]»*.
- **Системный фильтр** — задайте список ID записей, которые должны отображаться в таблице. Для этого введите **формулу** или выражение на языке **N3** или составьте таблицу **DMN**.

### Дополнительные свойства

Примечание

Перед настройкой дополнительных свойств таблицы её **необходимо сохранить**.

Для настройки сортировки, группировки, подсчёта итогов и фильтрации данных в таблице, перетащите столбцы из макета таблицы в соответствующие блоки на вкладке «**Дополнительные**» справа от макета и настройте параметры блоков, как указано ниже.

Чтобы удалить столбец из блока на вкладке «**Дополнительные**», перетащите его за пределы блока.

#### Сортировка

Перетащите в блок «**Сортировка**» один или несколько столбцов, а затем выберите каждый столбец в блоке и задайте направление сортировки строк таблицы по нему:

- **По возрастанию** — чем меньше значение в данном столбце, тем выше строка будет отображаться в таблице;
- **По убыванию** — чем больше значение в данном столбце, тем выше строка будет отображаться в таблице;
- **Пустые сверху** — установите этот флажок, чтобы строки с пустыми значениями в данном столбце отображались над остальными строками.

Примечание

Правила сортировки строк таблицы по нескольким столбцам будут применяться по порядку следования столбцов в блоке «**Сортировка**»: от первого к последнему.

Чтобы задать порядок сортировки по нескольким столбцам, расположите их в требуемом порядке в блоке «**Сортировка**».

_![Настройка сортировки строк таблицы по двум столбцам](/platform/v5.0/business_apps/templates/tables/img/table_settings_sort_settings.png)_

#### Группировка

Перетащите в блок «**Группировка**» один или несколько столбцов, а затем выберите каждый столбец в блоке и задайте направление группировки строк таблицы по значениям в нём:

- **По возрастанию** — чем меньше значение в данном столбце, тем выше группа строк будет отображаться в таблице;
- **По убыванию** — чем больше значение в данном столбце, тем выше группа строк будет отображаться в таблице;
- **Пустые сверху** — установите этот флажок, чтобы строки с пустыми значениями в данном столбце отображались над остальными строками.

Примечание

Строки группируются по одинаковым значениям в столбце.

При группировке строк по нескольким столбцам в таблице будет сформировано древовидное представление записей.

Правила группировки строк таблицы по нескольким столбцам будут применяться по порядку следования столбцов в блоке «**Группировка**»: от первого к последнему.

Чтобы задать порядок сортировки по нескольким столбцам, расположите их в требуемом порядке в блоке «**Группировка**».

_![Настройка группировки строк таблицы по двум столбцам](/platform/v5.0/business_apps/templates/tables/img/table_settings_group_settings.png)_

#### Подсчёт итогов

Перетащите в блок «**Подсчет итогов**» один или несколько столбцов, а затем выберите каждый столбец в блоке и задайте способ подсчёта итогов по значениям в столбце:

- **Количество** — будет подсчитано количество строк в каждой группе в таблице;
- **Сумма** — для каждой группы строк в таблице будет подсчитана сумма значений в столбце.

Примечание

Подсчет итогов работает только при включённой группировке строк в таблице.

_![Настройка подсчета итогов по столбцу таблицы](/platform/v5.0/business_apps/templates/tables/img/table_settings_count_settings.png)_

#### Фильтрация

Перетащите в блок «**Фильтрация**» один или несколько столбцов, а затем настройте правила фильтрации данных в таблице по значениям в столбцах:

- **Равно**
- **Не равно**
- **Больше чем**
- **Больше или равно**
- **Меньше чем**
- **Меньше или равно**

Примечание

Для фильтров по нескольким столбцам можно выбрать логический оператор `И` либо `ИЛИ`. Для этого нажимайте кнопку «**Поменять оператор**» *‌* рядом с правилами фильтрации.

_![Настройка фильтра с оператором «И» по двум столбцам таблицы](/platform/v5.0/business_apps/templates/tables/img/table_settings_and_settings.png)_

## Настройка столбцов таблицы

Панель элементов конструктора таблицы содержит список атрибутов текущего шаблона и связанных с ним шаблонов. Эти атрибуты можно поместить в таблицу в качестве столбцов.

### Добавление столбца

1. Выберите атрибут в панели элементов слева от макета таблицы.
2. Чтобы выбрать атрибут шаблона, связанного с текущим, раскройте в панели элементов атрибут типа «**Запись**».
3. Перетащите выбранный атрибут на макет таблицы.
4. При необходимости перетащите столбец в требуемую позицию на макете таблицы. При перетаскивании целевая позиция столбца подсвечивается на макете.
5. Справа от макета отобразится панель «**Свойства столбца**».
6. [Настройте свойства столбца](#table_configure_columns_properties).

Примечание

Для конечного пользователя столбцы таблицы будут отображаться слева направо в порядке их следования в макете таблицы: верхний столбец на макете отобразится первым слева в таблице.

_![Добавление и настройка столбца таблицы](/platform/v5.0/business_apps/templates/tables/img/table_settings_column_settings.png)_

### Настройка свойств столбца

1. Добавьте или выберите столбец таблицы на макете.
2. Настройте **свойства столбца** с помощью панели справа от макета таблицы:

   - **Отображаемое название** — заголовок столбца в таблице;
   - **Ширина столбца** — исходная ширина столбца в таблице (пользователь сможет установить персональную ширину столбцов в таблице);
   - **Скрытый** — установите этот флажок, чтобы столбец не отображался для пользователя при просмотре страницы. Этот флажок можно использовать, например, чтобы скрыть столбцы, которые используются для сортировки, группировки или фильтрации таблицы, но не должны быть видны пользователю. При этом пользователь сможет отобразить скрытые столбцы с помощью [персональной настройки таблицы][table_personal_use].
3. Нажмите кнопку «**Сохранить**», чтобы сохранить таблицу.

Примечание

Под свойствами столбца в справочных целях отображаются свойства атрибута, к которому относится столбец:

- **Путь к атрибуту** — полный путь к атрибуту в контексте текущего шаблона;
- **Системное имя** — уникальное имя атрибута;
- **Тип** — тип данных атрибута;
- **Формат отображения** — отображает формат отображения данных атрибута;
- **Вычисляемый** — флажок, указывающий, является ли атрибут вычисляемым;
- **В архиве** — флажок, указывающий, является ли атрибут архивным.

## Настройка кнопок таблицы

В каждой таблице предусмотрена одна [область кнопок][button_area].

- Изначально для таблицы используется область кнопок, в [свойствах][button_area] которой установлен флажок «**По умолчанию для таблиц**». В стандартной области кнопок, например, у шаблона записи находятся кнопки «**Сохранить**» и «**Архивировать**», а у шаблона процесса — «**Создать**», «**Остановить процесс**», «**Мигрировать**» и «**Архивировать**».
- Добавить и удалить кнопки для таблицы можно с помощью конструктора области кнопок, как указано ниже.
- Кроме того, у каждой таблицы предусмотрены перечисленные ниже системные кнопки, которые нельзя добавить и удалить:
  - **Обновить список** — перезагрузка данных таблицы.
  - **Мои настройки** — раскрывающееся меню для настройки таблицы:
    - **Настроить внешний вид** — [персональная настройка][table_personal_use] отображения столбцов таблицы для текущего пользователя.
    - **Удалить все фильтры** — сброс всех настроенных конечным пользователем фильтров данных в таблице.
    - **Сбросить** — удаление всех настроенных конечным пользователем параметров отображения таблицы. То есть будет восстановлено исходное представление таблицы, настроенное в конструкторе.
    - **Настроить таблицу** — перейти к [конструктору таблицы](#table_configure_template) (если у пользователя есть соответствующие права).
    - **Настроить шаблон** — переход к странице настройки шаблона, к которому относится таблица (если у пользователя есть соответствующие права).
  - **Поиск** — нажмите эту кнопку и введите ключевые слова в поле «**Поиск**». В таблице отобразятся строки, содержащие искомые слова.

### Порядок настройки области кнопок таблицы

1. Выберите область кнопок в верхней части макета таблицы.
2. В панели элементов слева отобразится список [кнопок шаблона][buttons].
3. Перетащите необходимые кнопки, группы кнопок и разделители на область кнопок.
4. При необходимости настройте свойства кнопок: переименуйте их, смените их значки или цвет. Эти изменения не отразятся на исходных кнопках, они будут использоваться только для данной таблицы.
5. Чтобы удалить все элементы из области кнопок, нажмите кнопку «**Очистить**» в панели «**Свойства области кнопок**».

   Примечание

   При изменении области кнопок таблицы в [списке областей кнопок][button_area] будет создана новая область кнопок, которая будет использоваться только для этой таблицы. Исходная область кнопок не будет изменена.
6. Чтобы восстановить исходную область кнопок, используемую по умолчанию для таблиц, нажмите кнопку «**Восстановить исходные кнопки**» в панели «**Свойства области кнопок**». После восстановления исходных кнопок и сохранения таблицы созданная для неё особая область кнопок будет удалена из [списка областей кнопок][button_area].
7. Нажмите кнопку «**Сохранить**», чтобы сохранить таблицу.

_![Настройка области кнопок таблицы](/platform/v5.0/business_apps/templates/tables/img/table_settings_buttons_area_settings.png)_

## Создание таблицы со списком задач

Определения

- **Таблица задач** содержит сведения о задачах по процессу.
- Помимо стандартной таблицы на странице «**Мои задачи**» можно настроить особую таблицу задач с произвольным набором столбцов.
- Таблица задач настраивается для шаблона процесса.
- Таблицу задач можно поместить в виде вкладки на страницу «**Мои задачи**».

1. Откройте [шаблон процесса][process_templates].
2. Откройте список [таблиц шаблона](#table_configure_template).
3. Нажмите кнопку «**Создать**».
4. В раскрывающемся меню выберите пункт «**Таблица задач**»
5. Настройте [свойства](#table_configure_properties), [столбцы](#table_configure_columns) и [кнопки](#table_configure_buttons) таблицы.
6. Сохраните таблицу.
7. Добавьте таблицу задач [на страницу «**Мои задачи**»](#table_configure_add_to_my_tasks).

   ![Создание таблицы задач](/platform/v5.0/business_apps/templates/tables/img/table_task_settings_create.png)

   Создание таблицы задач

## Добавление таблицы на страницу «Мои задачи»

1. Откройте [раздел навигации][navigation_sections_setup], в который требуется добавить [таблицу][table_configure] из любого шаблона или [таблицу задач](#table_configure_tasks_view) из шаблона процесса.
2. Раскройте список шаблонов на панели элементов.
3. Раскройте шаблон, содержащий требуемую таблицу.
4. Раскройте группу «**Таблицы**» внутри шаблона.
5. Перетащите таблицу задач в подраздел «**Мои задачи**» на макете раздела навигации. Если этот подраздел отсутствует, перетащите группу «**Мои задачи**» из панели элементов на макет раздела навигации. См. [*«Добавление страницы «Мои задачи» в раздел навигации»*.][my_tasks_page_configure]
6. Настройте свойства вкладки таблицы с помощью панели «**Свойства элемента**»:

   - **Отображаемое название** — введите наглядное название вкладки страницы «**Мои задачи**», на которой будет отображаться таблица.
   - **Описание** — введите краткое описание таблицы.
   - **Значок** — выберите наглядный значок для таблицы.
7. Сохраните раздел навигации.

_![Добавление таблицы задач на страницу «Мои задачи»](/platform/v5.0/business_apps/templates/tables/img/table_my_tasks_addition_add.png)_

## Клонирование таблицы

1. Откройте [список таблиц шаблона](#table_configure_template).
2. Откройте таблицу, дважды нажав её в списке.
3. В конструкторе таблицы нажмите кнопку «**Клонировать**».
4. В окне «**Клонирование**» настройте свойства дубликата таблицы:

   - **Название** — заголовок новой таблицы, который будет отображаться для конечных пользователей;
   - **Системное имя** — уникальное имя таблицы, которое используется в вычислениях.
     Не должно начинаться с цифры. Разрешены английские и русские буквы, цифры и символ «\_». Рекомендуется использовать английские буквы.
     Обычно заполняется автоматически по названию.
5. Нажмите кнопку «**Сохранить**».
6. Дубликат таблицы будет добавлен в список таблиц шаблона.

_![Клонирование таблицы](/platform/v5.0/business_apps/templates/tables/img/table_clone_clone.png)_

## Удаление таблицы

1. Откройте [список таблиц шаблона](#table_configure_template).
2. Установите для подлежащей удалению таблицы флажок в списке.
3. Нажмите кнопку «**Удалить**».
4. Подтвердите удаление.

--8<-- "related_topics_heading.md"

- [Настройка таблицы на форме][form_dynamic_elements]
- [Таблицы. Использование и персональная настройка][table_personal_use]
- [Настройка страницы «Мои задачи»][my_tasks_page_configure]
- [Просмотр и настройка свойств шаблона][template_common_properties]
- [Настройка разделов навигации][navigation_sections_setup]

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
