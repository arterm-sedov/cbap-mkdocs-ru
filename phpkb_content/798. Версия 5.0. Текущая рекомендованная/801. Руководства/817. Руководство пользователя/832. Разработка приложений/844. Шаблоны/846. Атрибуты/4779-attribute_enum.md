---
title: Атрибут типа «Список значений»
kbId: 4779
---

# Атрибут типа «Список значений»

## Описание атрибута

Структура атрибута типа «Список значений»

- Атрибут типа «**Список значений**» хранит ID значения, выбранного из предварительно заданного списка.
- Список возможных значений настраивается в свойствах атрибута и не может быть изменён при выполнении приложения.
- Каждое возможное значение содержит:
  - **Системное имя** значения.
  - Отображаемые названия на **русском**, **английском** и **немецком** языках (достаточно указать название на одном языке).
  - **Цвет** — числовой код **в десятичном формате**. Для поиска кодов цветов и их преобразования из шестнадцатеричной в десятичную форму можно воспользоваться, например, сайтом <https://convertingcolors.com/>.
  - **Значок** — строка с кодом FontAwesome. Для поиска кодов значков можно воспользоваться встроенной **галереей значков** или сайтом <https://fontawesome.com/>.

Получение данных из атрибута с помощью формулы

С помощью **формулы** для атрибута типа «**Список значений**» можно получить:

- ID текущего значения атрибута:

  ```
  $EnumAttributeSystemName—>cmw.variantName

  ```
- системное имя значения атрибута:

  ```
  $EnumAttributeSystemName—>cmw.variantAlias

  ```
- код значка значения атрибута:

  ```
  $EnumAttributeSystemName—>cmw.variantIcon

  ```
- цвет значения атрибута в десятичном формате:

  ```
  $EnumAttributeSystemName—>cmw.color

  ```

Установка значения атрибута с помощью формулы

Чтобы c помощью **формулы** задать значение атрибута типа «**Список значений**» (например, для вычисляемого атрибута или правила на форме), необходимо:

- вернуть ID требуемого значения атрибута, указав системные имена атрибута и требуемого значения:

  ```
  ID(ENUMVALUE("EnumAttributeSystemName", "EnumValueSystemName"))

  ```

Сравнение значения атрибута с помощью формулы

С помощью **формулы** сравнить значение атрибута типа «**Список значений**» с требуемым можно по системному имени значения следующими способами:

- равенство

  ```
  $EnumAttributeSystemName == EnumValueSystemName

  ```

  или

  ```
  EQUALS($EnumAttributeSystemName->cmw.variantAlias, "EnumValueSystemName")

  ```

  или

  ```
  EQUALS($EnumAttributeSystemName, ENUMVALUE("EnumAttributeSystemName", "EnumValueSystemName"))

  ```
- неравенство

  ```
  $EnumAttributeSystemName !== EnumValueSystemName

  ```

  или

  ```
  NOT(EQUALS($EnumAttributeSystemName->cmw.variantAlias, "EnumValueSystemName"))

  ```

  или

  ```
  NOT(EQUALS($EnumAttributeSystemName, ENUMVALUE("EnumAttributeSystemName", "EnumValueSystemName")))

  ```

Префиксы N3 для работы с атрибутом

Для работы с атрибутом типа «**Список значений**» в выражениях на N3 (например, в сценариях) могут потребоваться следующие префиксы:

```
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmw: <http://comindware.com/logics#>.
@prefix l10n: <http://comindware.com/ontology/l10n#>.
@prefix cmwentity: <http://comindware.com/ontology/entity#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix convert: <http://comindware.com/logics/convertions#>.

```

Получение данных из атрибута с помощью N3

С помощью **N3** для атрибута типа «**Список значений**» можно получить:

- ID определённого значения:

  ```
  ("EnumAttributeSystemName" "enumValueSystemName") convert:enumValue ?enumValueId.

  ```
- объект с атрибутом:

  ```
  ("TemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.

  ```
- из объекта с атрибутом — массив возможных значений атрибута в текущей записи:

  ```
  ?item ?enumAttribute ?enumAttributeValues.

  ```

  **Из этого массива можно получить:**

  - ID текущего значения атрибута:

    ```
    ?enumAttributeValues cmw:variantName ?enumValueId.

    ```
  - системное имя значения атрибута:

    ```
    ?enumAttributeValues cmw:variantAlias ?enumValueSystemName.

    ```
  - код значка значения атрибута:

    ```
    ?enumAttributeValues cmw:variantIcon ?enumValueIcon.

    ```
  - цвет значения атрибута в десятичном формате:

    ```
    ?enumAttributeValues cmw:color ?enumValueColor.

    ```

Получение значения атрибута на определённом языке с помощью N3

С помощью **N3** для атрибута типа «**Список значений**» можно получить названия значения атрибута на английском, русском и немецком языках:

```
# Находим атрибут EnumAttributeSystemName в шаблоне TemplateSystemName.
("TemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
# Присваиваем переменной ?enumAttributeValues
# объект со списком значений атрибута.
?item ?enumAttribute ?enumAttributeValues.
# Присваиваем переменной ?enumValueId
# объект с выбранным значением атрибута.
?enumAttributeValues cmw:variantName ?enumValueId.
# Присваиваем переменной ?enumAttributeValues массив объектов
# с заполненными названиями значения атрибута на всех языках.
?enumValueId l10n:text ?enumValueLanguageVersions.
# Начинаем цикл по ?enumValueLanguageVersions
    # Присваиваем переменной ?langCodeStr код языка
    # названия значения атрибута на текущей итерации цикла.
    ?enumValueLanguageVersions l10n:lang ?langCode.
    ("{0}" ?langCode) string:format ?langCodeStr.
    # Сравниваем код языка для значения атрибута с желаемым.
    # "ru" — код русского языка, "en" — английского, "de" — немецкого.
    ?langCodeStr cmwentity:contains "ru".
        # Если предыдущее предложение возвращает true,
        # записываем значение на русском языке в вычисляемый атрибут.
        ?names l10n:data ?value.
# переходим к следующей итерации по ?enumValueLanguageVersions.

```

Установка значения атрибута с помощью N3

Чтобы c помощю **N3** задать значение атрибута типа «**Список значений**» (например, для вычисляемого атрибута или правила на форме), необходимо:

- получить ID требуемого значения атрибута:

  ```
  ("EnumAttributeSystemName" "ValueSystemName") convert:enumValue ?enumValueId.

  ```
- вернуть полученный ID:

  ```
  ?enumIdOverdue -> ?value.

  ```

Сравнение значения атрибута с помощью N3

С помощью **N3** для атрибута типа «**Список значений**» можно выполнять сравнение по системному имени его значения:

- Сравнение значения атрибута с требуемым:

  ```
  @prefix object: <http://comindware.com/ontology/object#>.
  @prefix cmw: <http://comindware.com/logics#>.
  {
      # Получаем атрибут типа «Список значений» из шаблона по системному имени.
      ("TemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
      # Получаем коллекцию возможных значений атрибута.
      ?item ?enumAttribute ?enumAttributeValues.
      # Получаем системное имя значения атрибута в текущей записи.
      ?enumAttributeValues cmw:variantAlias ?enumValueSystemName.
      # Сравниваем системное имя значения атрибута с требуемым
      # и возвращаем результат.
      if
      {
          ?enumValueSystemName == "targetValueSystemName".
      }
      then
      {
          true -> ?value.
      }
      else
      {
          false -> ?value.
      }
  }

  ```

Фильтрация значения атрибута с помощью N3

С помощью **N3** для атрибута типа «**Список значений**» можно выполнять фильтрацию по системному имени его значения:

- Фильтрация (в таблице шаблона) записей с требуемым значением атрибута:

  ```
  @prefix convert: <http://comindware.com/logics/convertions#>.
  @prefix object: <http://comindware.com/ontology/object#>.
  {
      # Получаем атрибут типа «Список значений» из шаблона по системному имени.
      ("TemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
      # Получаем ID значения атрибута по системному имени.
      ("EnumAttributeSystemName" "enumValueSystemName") convert:enumValue ?enumValueId.
      # Возвращаем записи, у которых атрибут имеет значение "enumValueSystemName".
      ?item ?enumAttribute ?enumValueId.
  }

  ```
- Фильтрация добавляемых записей (в таблице на форме или раскрывающемся списке на форме) записей с требуемым значением атрибута:

  ```
  @prefix convert: <http://comindware.com/logics/convertions#>.
  @prefix object: <http://comindware.com/ontology/object#>.
  {
      # Получаем атрибут типа «Список значений» из шаблона по системному имени.
      ("TemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
      # Получаем ID значения атрибута по системному имени.
      ("EnumAttributeSystemName" "enumValueSystemName") convert:enumValue ?enumValueId.
      # Фильтруем и возвращаем записи,
      # у которых атрибут имеет значение "enumValueSystemName".
      ?filteredRecordIds ?enumAttribute ?enumValueId.
      ?filteredRecordIds -> ?value.
  }

  ```
- Фильтрация отображаемых записей (в таблице на форме, раскрывающемся списке на форме, вычисляемом атрибуте или правиле для формы) записей с требуемым значением атрибута:

  ```
  @prefix convert: <http://comindware.com/logics/convertions#>.
  @prefix object: <http://comindware.com/ontology/object#>.
  {
      # Получаем атрибут типа «Запись» из шаблона с коллекцией записей.
      ("ParentTemplateSystemName" "RecordAttributeSystemName") object:findProperty ?RecordAttribute.
      # Получаем атрибут типа «Список значений» из связанного шаблона по системному имени.
      ("LinkedTemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
      # Получаем ID значения атрибута по системному имени.
      ("EnumAttributeSystemName" "enumValueSystemName") convert:enumValue ?enumValueId.
      # Получаем коллекцию записей из атрибута RecordAttribute.
      ?item ?RecordAttribute ?filteredRecordIds.
      # Фильтруем и возвращаем записи,
      # у которых атрибут имеет значение "enumValueSystemName".
      ?filteredRecordIds ?enumAttribute ?enumValueId.
      ?filteredRecordIds -> ?value.
  }

  ```

## Настройка свойств атрибута

Помимо **[общих свойств][attribute_common_properties]** для атрибута типа «**Список значений**» предусмотрены перечисленные ниже свойства.

- Вкладка «**Свойства**»

  - «**Вычислять автоматически**» — установите этот флажок, чтобы значение атрибута вычислялось во время работы приложения. См. «**[Вычисляемые атрибуты][attribute_calculated]**».
  - **Формат отображения:**
    - **Текст** — значения атрибута будут отображаться в виде простого текста;
    - **Индикатор** — перед значением атрибута будет отображаться кружок (если не задан значок) или значок заданного цвета;
    - **Бейдж** — значение и значок атрибута будут отображаться на подложке заданного цвета. См. [пример](#attribute_enum_examples).

  ![Свойства атрибута типа «Список значений»](/platform/v5.0/business_apps/templates/attributes/img/attribute_enum_properties.png)

  Свойства атрибута типа «Список значений»
- Вкладка «**Список значений**»

  - **Системное имя** **(обязательное поле)** — системное имя элемента списка.
  - **EN** — английское название пункта в списке.
  - **DE** — немецкое название пункта в списке.
  - **RU** — русское название пункта в списке.
  - **Цвет** — цвет, которым будет отображаться значение атрибута.
  - **Значок** — значок, который будет отображаться рядом со значением атрибута.

  ![Список значений](/platform/v5.0/business_apps/templates/attributes/img/attribute_enum_properties_value_list_tab.png)

  Список значений

### Создание элементов списка значений

1. На вкладке «**Список значений**» нажмите кнопку «**Создать**».
2. Нажмите поле «**Системное имя**» и введите системное имя элемента списка.
3. Нажмите поле «**EN**» и введите английское отображаемое название пункта в списке.
4. Нажмите поле «**RU**» и введите русское отображаемое название пункта в списке.
5. Нажмите поле «**Цвет**» и выберите цвет пункта в списке.
6. Нажмите поле «**Значок**» и выберите значок пункта в списке.
7. Повторите шаги 1–5, чтобы создать остальные элементы списка.
8. Нажмите кнопку «**Сохранить**», чтобы сохранить атрибут.

_![Создание элементов списка значений](/platform/v5.0/business_apps/templates/attributes/img/attribute_enum_create_value_list.png)_

### Удаление элементов из списка значений

1. На вкладке «**Список значений**» установите флажки выбора для элементов, подлежащих удалению.
2. Нажмите кнопку «**Удалить**».
3. В отобразившемся окне подтверждения нажмите кнопку «**Удалить**».
4. Нажмите кнопку «**Сохранить**», чтобы сохранить атрибут.

_![Удаление элементов из списка значений](/platform/v5.0/business_apps/templates/attributes/img/attribute_enum_delete_values.png)_

## Примеры использования

Ознакомьтесь с перечисленными ниже подробными статьями, а также простейшим примером настройки атрибута типа «**Список значений**».

- *[Вычисление текущего значения][attribute_enum_calculate_current_value]*
- *[Вычисление значения по справочнику][attribute_enum_calculate_registry]*
- *[Фильтрация связанных записей по значению атрибута с помощью N3][attribute_enum_value_filter]*
- *[Вычисление значения с помощью N3 и формул][attribute_enum_value_calculation]*

Выбор типа ТС из списка значений на форме

**Исходные данные**

В приложении настроен и помещён на форму следующий атрибут:

- *Тип транспортного средства*

  - **Тип данных: список значений**
  - **Формат отображения: бейдж**
  - **Список значений:**

  | Системное имя | EN | RU | Цвет | Значок |
  | --- | --- | --- | --- | --- |
  | `bus` | *Bus* | *Автобус* | `#ff0000` | *‌* bus |
  | `passengerCar` | *Car* | *Легковой автомобиль* | `#0000ff` | *‌* car |
  | `truck` | *Truck* | *Грузовик* | `#00ff00` | *‌* truck |
  | `van` | *Minivan* | *Микроавтобус* | `#ffff00` | *‌* van-shuttle |

**Результирующее поведение**

- Поле *«Тип транспортного средства»* будет отображаться как раскрывающийся список с названиями и значками автомобилей, пункты списка будут окрашены указанными цветами:

_![Раскрывающийся список значений на форме](/platform/v5.0/business_apps/templates/attributes/img/attribute_enum_example.png)_

--8<-- "related_topics_heading.md"

- *[Атрибут типа «Список значений». Вычисление текущего значения][attribute_enum_calculate_current_value]*
- *[Атрибут типа «Список значений». Вычисление значения по справочнику][attribute_enum_calculate_registry]*
- *[Атрибут типа «Список значений». Фильтрация связанных записей по значению атрибута с помощью N3][attribute_enum_value_filter]*
- *[Атрибут типа «Список значений». Вычисление значения с помощью N3 и формул][attribute_enum_value_calculation]*
- *[Общие свойства атрибутов][attribute_common_properties]*
- *[Атрибуты. Определения, типы, настройка, архивирование, удаление][attributes]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
