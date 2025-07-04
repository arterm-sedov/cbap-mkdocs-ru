---
title: Таблицы. Использование и персональная настройка
kbId: 4815
---

# Таблицы. Использование и персональная настройка

## Введение

Таблицы в ПО **{{ productName }}** настраиваются на двух уровнях:

- для таблицы в шаблоне или на форме разработчик настраивает первичную конфигурацию, которую конечный пользователь может изменить в ограниченных пределах;
- конечный пользователь может настроить персональное представление таблицы, которое будет привязано к его аккаунту:

  - скрыть или отобразить столбцы;
  - задать порядок столбцов;
  - задать ширину столбцов;
  - скрыть и отобразить форму записей рядом с таблицей;
  - закрепить столбцы;
  - включить и отключить ручную загрузку данных;
  - задать фильтры, группировку и подсчёт итогов в таблице.

При переходе к таблице отображается персональное представление таблицы, настроенное конечным пользователем.

Если у пользователя не настроено персональное представление таблицы, то используется представление, настроенное в приложении.

Здесь даны инструкции по персональной настройке таблиц для конечного пользователя.

Сведения о настройке таблиц для разработчиков приложений см. в статьях *«[Настройка таблицы в шаблоне][table_configure]»* и *«[Динамические элементы формы: настройка таблицы][form_dynamic_elements]».*

## Элементы управления для таблицы

При просмотре таблицы конечному пользователю доступны различные элементы управления в зависимости от его [разрешений][account_permission_audit]:

1. [Кнопки][buttons], настроенные для конкретной таблицы.
2. Стандартные кнопки для таблицы

   - **Обновить** *‌* — загрузка актуальных данных таблицы.
   - **На весь экран** *‌* — развёртывание таблицы на весь экран. Эта кнопка предусмотрена только у таблиц на формах.
   - **Мои настройки** *‌*

     - **Настроить внешний вид** — [настройка персонального представления таблицы](#настройка-внешнего-вида-таблицы) для текущего пользователя.
     - **Удалить все фильтры** — сброс [настроенных пользователем фильтров](#table_personal_use_filter).
     - **Сбросить** — сброс всех персональных настроек таблицы: возвращение исходного внешнего вида таблицы, а также сброс всех фильтров, ширины столбцов и параметров группировки и сортировки.
     - **Настроить таблицу** — переход к [конструктору таблицы][table_configure].
     - **Настроить шаблон** — переход к странице свойств [шаблона][templates], к которому относится текущая запись.
   - **Поиск** *‌* — нажмите эту кнопку и введите искомые слова, в таблице отобразятся строки, содержащие искомый текст.
3. **Записей на странице** — нажмите кнопку  *‌* рядом с этим пунктом и выберите количество строк, которые должны отображаться на одной странице таблицы. Этот пункт не предусмотрен у таблиц на формах.
4. **Флажки выбора**: служат для выбора записей, с которыми будут выполняться операции при нажатии кнопок.

_![Элементы управления для таблицы](/platform/v5.0/using_the_system/img/table_personal_use_elements.png)_

## Взаимодействие с таблицей с помощью клавиатуры

Для работы с таблицами можно использовать перечисленные ниже клавиши.

- Таблицы на формах и в шаблонах

  - `Down` `Up` — переход на строку вниз или вверх.
  - `Page Down` `Page Up` — переход на страницу вниз или вверх.
  - `Пробел` — выбор строки.
- Таблицы на формах

  - `Tab` или `Right` — переход на одну ячейку вправо.
  - `Shift`+`Tab` или `Left` — переход на одну ячейку влево.
  - `F2` — редактирование значения в ячейке.

## Настройка внешнего вида таблицы

1. Откройте таблицу или форму с таблицей, внешний вид которой хотите настроить.
2. Чтобы настроить ширину столбцов, перетащите с помощью мыши границы заголовков таблицы.

   ![Изменение ширины столбцов таблицы](/platform/v5.0/using_the_system/img/ColumnResize.gif)

   Изменение ширины столбцов таблицы
3. Чтобы настроить отображение и порядок столбцов, нажмите кнопку «**Мои настройки**» *‌* над таблицей и в раскрывающемся меню выберите пункт «**Настроить внешний вид**».

   ![Переход к настройке внешнего вида таблицы](/platform/v5.0/using_the_system/img/table_personal_use_table_settings_transfer.png)

   Переход к настройке внешнего вида таблицы
4. Отобразится форма настройки внешнего вида таблицы.
5. Настройте внешний вид таблицы.
6. Нажмите кнопку «**Сохранить**», чтобы применить изменения и просмотреть таблицу в новом представлении.

### Настройка таблицы на форме и в шаблоне

- Выберите столбцы, которые должны отображаться, установив или сняв флажки радом с их названием.
- Перетащите столбцы в требуемые позиции, взявшись за вертикальное троеточие *‌* слева от флажков выбора.
- В поле «**Закрепить столбцы**» укажите количество столбцов, которые не должны прокручиваться по горизонтали.

_![Изменение порядка столбцов таблицы](/platform/v5.0/using_the_system/img/ColumnReorder.gif)_

### Настройка таблицы в шаблоне

- В поле «**Показ формы редактирования**» выберите, где следует отображать форму записи при нажатии строки в таблице:
  - **Вместо таблицы** — при двойном нажатии строки в таблице форма с записью отобразится вместо таблицы;
  - **Справа от таблицы** —  при нажатии строки в таблице форма записи отобразится справа от таблицы, границу между таблицей и формой можно будет перемещать;
  - **Под таблицей** — при нажатии строки в форма записи отобразится под таблицей, границу между таблицей и формой можно будет перемещать.
- В поле «**Загрузка данных**» установите или снимите флажок «**Вручную**». Если он установлен, при открытии таблица будет отображаться без данных, а для загрузки потребуется нажать кнопку «**Загрузить данные** ».

_![Таблица с ручной загрузкой данных](/platform/v5.0/using_the_system/img/table_personal_use_hand_load.png)_

## Настройка фильтрации

Для каждого столбца таблицы можно настроить один или несколько фильтров по значениям соответствующих атрибутов. В таблице будут отображаться только строки, соответствующие настроенным фильтрам.

1. Нажмите значок *‌* в заголовке столбца.
2. Установите флажок «**Фильтровать данные**» в раскрывающемся меню.
3. Выберите тип фильтра и задайте его значение:

   - Для атрибутов всех типов
     - **Равно** — значение атрибута должно точно соответствовать указанному. Для атрибутов типа «**Запись**» и «**Список значений**» можно выбрать несколько значений.
     - **Не равно** — значение атрибута не должно соответствовать указанному. Для атрибутов типа «**Запись**» и «**Список значений**» можно выбрать несколько значений.
     - **Не указано** — значение атрибута должно быть пустым.
     - **Указано** — атрибут должен иметь любое значение, то есть не должен быть пустым.
   - Для атрибутов типов «**Число**», «**Длительность**» и «**Дата и время**»
     - **Больше чем** — значение атрибута должно быть больше указанного.
     - **Меньше чем** — значение атрибута должно быть меньше указанного.
     - **Между** — значение атрибута должно быть больше значения в первом поле и меньше значения во втором поле.
   - Для атрибутов типа «**Текст**»
     - **Содержит строку** — значение атрибута должно содержать указанную строку.
     - **Не содержит строку** — значение атрибута не должно содержать указанную строку.
     - **Начинается с** — значение атрибута должно начинаться с указанной строки.
     - **Заканчивается** — значение атрибута должно заканчиваться указанной строкой.
     - **Умный поиск** — значение атрибута должно содержать указанную строку, в отличие от фильтра «**Содержит строку**» при поиске будут исправлены незначительные опечатки.
4. Чтобы добавить ещё один фильтр, нажмите кнопку *‌* и настройте дополнительный фильтр.
5. Чтобы применить фильтр, нажмите кнопку «**Сохранить**».

_![Настройка фильтров для столбца таблицы](/platform/v5.0/using_the_system/img/table_personal_use_filter_settings.png)_

## Расширенная фильтрация

С помощью **форм поиска** можно применить расширенный фильтр к списку записей в таблице. Это обеспечивает фасетный поиск с учётом логических условий.

Логика расширенной фильтрации

- Расширенный фильтр комбинируется с уже применёнными [фильтрами в таблице](#table_personal_use_filter).
- Расширенный фильтр применяется для всех записей на всех страницах таблицы.
- Если для шаблона настроено несколько **форм поиска**:
  - они отображаются на отдельных вкладках на панели расширенной фильтрации;
  - применяется фильтр с вкладки, на которой была нажата кнопка «**Найти**».

Настройка форм поиска для расширенной фильтрации

Инструкции по настройке форм поиска: *[Расширенная фильтрация. Настройка форм поиска][search_forms]*.

1. Нажмите кнопку «**Настроить фильтры**» *‌* над таблицей.
2. Отобразится панель расширенной фильтрации.
3. Выберите вкладку с требуемой формой поиска.
4. Задайте значения атрибутов, по которым следует отфильтровать записи.

   - Чтобы задать тип фильтра, нажмите кнопку «**Функция**» *‌* справа от поля атрибута.
   - Фильтрация настраивается также, как для столбцов таблицы. См. *«[Настройка фильтрации](#table_personal_use_filter)»*.
5. Чтобы применить настроенный расширенный фильтр, нажмите кнопку «**Найти**».
6. Чтобы отменить расширенную фильтрацию, нажмите кнопку «**Сбросить фильтры**».

_![Настройка расширенной фильтрации](/platform/v5.0/using_the_system/img/table_personal_use_filter_extended.png)_

## Настройка сортировки, группировки и подсчёта итогов

Настроив сортировку, группировку и подсчёт итогов в таблице можно упорядочить записи для их более наглядного представления.

_![Пример таблицы с группировкой по столбцу «Тип заявки», подсчётом итогов по столбцам «Тип заявки» и «Длительность» и сортировкой по столбцам «Тип заявки» и «Статус»](/platform/v5.0/using_the_system/img/table_personal_use_example.png)_

### Настройка сортировки

Параметры сортировки и [группировки](#настройка-группировки) строк в таблице взаимосвязаны. Например, с помощью группировки можно добиться иерархической сортировки строк по значениям нескольких столбцов.

1. Для **сортировки** значений таблицы нажимайте текст заголовка столбца. При каждом нажатии будет циклически меняться порядок сортировки:

   - по возрастанию значений в столбце *‌*;
   - по убыванию значений в столбце *‌*;
   - исходный порядок, заданный в приложении (см. *«[Настройка таблицы в шаблоне][table_configure]»)*.
2. Для отображения строк с пустыми значениями вверху таблицы:

   1. Настройте для столбца сортировку по возрастанию или убыванию.
   2. Нажмите значок *‌* в заголовке столбца.
   3. Установите флажок «**Пустые строки сверху**».
   4. Нажмите кнопку «**Сохранить**».

_![Настройка сортировки по столбцу](/platform/v5.0/using_the_system/img/table_personal_use_column_settings.png)_

### Настройка группировки

Примечание

Группировка недоступна для таблиц на форме.

При включенной группировке по столбцу строки с одинаковыми значениями в этом столбце располагаются в отдельных группах, и для каждой группы появляется специальная строка в таблице.

Можно включить группировку по нескольким столбцам таблицы. В этом случае будут сформированы подгруппы в соответствии с порядком включения группировки по столбцам.

Группы в таблице можно свёртывать и развёртывать.

При включённой группировке можно настроить иерархическую сортировку по всем столбцам с группировкой и одному столбцу без группировки.

1. Нажмите значок *‌* в заголовке столбца
2. Установите флажок «**Группировать**».
3. Нажмите кнопку «**Сохранить**».

_![Настройка группировки по столбцу](/platform/v5.0/using_the_system/img/table_personal_use_column_group_settings.png)_

### Настройка подсчёта итогов

Примечание

Подсчёт итогов недоступен для таблиц на форме.

Подсчёт итогов возможен, если для любого из столбцов таблицы включена группировка. При этом подсчитать итоги можно для любого из столбцов.

Для каждой группы будет указано количество записей или сумма значений в столбцах, для которых включён подсчёт итогов.

1. Нажмите значок *‌* в заголовке столбца
2. Установите флажок «**Группировать**».
3. Для атрибутов типов «**Число**» и «**Длительность**» установите флажок «**Показать итоги** » и выберите пункт « **количество**» или «**сумма**».
4. Для атрибутов всех остальных типов, установите флажок «**Подсчитать количество**».
5. Нажмите кнопку «**Сохранить**».

_![Настройка подсчёта итогов по столбцу](/platform/v5.0/using_the_system/img/table_personal_use_column_count_settings.png)_

## Сброс персональных настроек таблицы

1. Чтобы вернуть исходный внешний вид таблицы (порядок и видимость столбцов, закрепление столбцов, способ отображения формы записей, режим загрузки данных) с сохранением остальных персональных настроек (ширины столбцов, фильтров, сортировки, группировки, сортировки):

   1. Нажмите кнопку «**Мои настройки**» *‌* над таблицей.
   2. Выберите пункт «**Настроить внешний вид**».
   3. Отобразится форма настройки внешнего вида таблицы.
   4. Нажмите кнопку «**Сбросить**».
   5. Нажмите кнопку «**Сохранить**».

   ![Сброс внешнего вида таблицы](/platform/v5.0/using_the_system/img/table_personal_use_drop_settings.png)

   Сброс внешнего вида таблицы
2. Чтобы сбросить все персональные настройки таблицы (вернуть исходный внешний вид таблицы и сбросить все фильтры, ширину столбцов, а также параметры группировки и сортировки), выберите пункт «**Сбросить**» в раскрывающемся меню «**Мои настройки**» *‌* над таблицей.

   ![Полный сброс персональных настроек таблицы](/platform/v5.0/using_the_system/img/table_personal_use_full_drop_settings.png)

   Полный сброс персональных настроек таблицы

--8<-- "related_topics_heading.md"

- *[Настройка таблицы в шаблоне][table_configure]*
- *[Расширенная фильтрация. Настройка форм поиска][search_forms]*
- *[Мобильное приложение. Использование][mobile_app_use]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
