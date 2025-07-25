---
title: Язык формул. Общие сведения
kbId: 4999
---

# Язык формул. Общие сведения

## Описание языка формул Comindware

Настройка рабочей среды и пользовательского интерфейса **{{ productName }}** производится простым перетаскиванием элементов и не требует программирования.

В случае если ваш бизнес требует нетривиального подхода, воспользуйтесь возможностями языка формул Comindware, легкого, но эффективного языка программирования, встроенного в продукт.

С помощью формул вы сможете неограниченно масштабировать бизнес-процессы в согласии с нуждами вашего бизнеса.

Возможности языка формул Comindware:

- Изменение и определение значений атрибутов на основе данных, хранящихся в различных шаблонах записи.
- Проверка и изменение процессных данных.
- Задание временных рамок выполнения тех или иных процессных действий, например, разрешенные запросы в техподдержку могут закрываться автоматически после двух недель в неактивном состоянии.
- Назначение исполнителей задачи на основании того или иного условия (например, в зависимости от категории запроса).
- Настройка межпроцессного взаимодействия.
- Настройка вызова стороннего процесса внутри текущего.
- Настройка условий ветвления процесса.
- Защита платформы от негативного влияния человеческого фактора.

См. также:

- [Литералы и функции в формулах. Справочник, описания, примеры][formula_function_list]
- [Форматирование значений атрибутов в файле шаблона экспорта и формулах][export_template_file_formula_format_values]
- [Системные атрибуты шаблона аккаунта][account_templates]
- [Примеры формул](https://kb.comindware.ru/category.php?id=881)

## Контекст вычисления формул. Понятие и изменение

Понятие контекста всегда используется для настройки бизнес-логики и вычислений в **{{ productName }}**. В первую очередь, у любой информационной системы есть база данных, и чтобы получить какие-то данные из нее, нужно написать запрос к базе.

**Контекст** — это отправная точка запроса к базе данных. Границами контекста являются шаблоны записи, шаблоны процессов и пользовательские задачи, в которых пишется запрос (в форме вычисляемых атрибутов, правил на форме, фильтров и т.д.), и их нужно различать для правильного написания формулы.

`$` — обозначение изначального контекста.

Для смены контекста используются атрибуты типа «Запись» или запроса вида `from a in db`. Чтобы поменять контекст на связанную запись, используются системные имена атрибутов типа «Запись» после `$` и символы `->` после системного имени атрибута. В сценариях можно менять контекст по самим атрибутам типа «Запись» или по выражению типа `from a in db`.

### Примеры смены контекста

- **Пример 1:** искомый атрибут находится в другом шаблоне, и в текущем контексте (шаблоне) есть ссылка на связанный шаблон.

  ```
  $link->atributSystemName

  ```

  Здесь:

  - `link`: системное имя атрибута типа «**Запись**»;
  - `atributSystemName` — системное имя атрибута в связанной записи.

  Больше о вызове связанных данных читайте в статье [Вызов связанных данных](https://kb.comindware.ru/article.php?id=4998).
- **Пример 2:** искомый атрибут находится в другом шаблоне записи, но в текущем контексте (шаблоне записи) нет ссылки на другой шаблон записи.

  ```
  from a in db->recordTemplateSystemName
  where EQUALS(a->attirbute1, $attribute2)
  select a->id

  ```

  Здесь:

  - `recordTemplateSystemName`: системное имя искомого шаблона;
  - `attribute1`: системное имя атрибута в искомом шаблоне;
  - `attribute2`: системное имя атрибута в текущем шаблоне, с которым нужно сравнить `attribute1`.

См. *«[Составление запросов на языке формул](#formula_guide_queries)»*.

- **Пример 3:** текущий контекст — это контекст задачи, а искомый атрибут находится в связанном с шаблоном процесса шаблоне записи.

  ```
  $cmw.task.objectId->op.11

  ```

  Здесь `op.11` — ID атрибута в связанном шаблоне записи.
- **Пример 4:** текущий контекст — это контекст процесса, а искомый атрибут находится в связанном шаблоне записи.

  ```
  $$BusinessObject->attributeSystemName

  ```

  Здесь `attributeSystemName` — системное имя атрибута в связанном шаблоне записи.

## Основные правила написания формул

Работая с формулами в **{{ productName }}**, придерживайтесь следующих правил:

1. В формулах используйте только идентификаторы и системные имена, а не отображаемые названия объектов.
2. Для идентификаторов и системных имен учитывается регистр: буквы `A` и `а` считаются разными.
3. Системные имена должны начинаться с буквы или символа подчеркивания (`_`). В самом системном имени можно использовать латинские и русские буквы (`A`–`Z`, `a`–`z`, `А`–`Я`, `а`–`я`), числа (`0`–`9`) и символы подчеркивания (`_`).
4. Системные имена должны быть уникальны только в рамках одного шаблона. Системные атрибуты создаются автоматически под формализованными именами, такими как `id`, `_creationDate`, `_creator`, `_lastWriteDate` и др.
5. Для того чтобы обратиться к тому или иному свойству текущего объекта, используйте оператор `$attributeSystemName` (`$->attributeSystemName`), где символ `$` представляет текущий шаблон, а `attributeSystemName` — системное имя атрибута этого шаблона.
6. Вы можете складывать и вычитать значения атрибутов типа «**Дата и время**» и «**Длительность**» между собой, руководствуясь следующей таблицей:

| Действие | Результат |
| --- | --- |
| Длительность +/- Длительность | Длительность |
| Дата и время +/- Длительность | Дата и время |
| Дата и время - Дата и время | Длительность |

См. также *«[Составление запросов на языке формул](#formula_guide_queries)»*.

## Вызов связанных данных

Для того чтобы обратиться к данным связанного шаблона записи через атрибут типа «**Запись**», который ссылается на этот шаблон, введите системное имя атрибута типа «**Запись**», символ `->` и системное имя атрибута связанного шаблона записи.

Пример:

| Шаблоны записи | Атрибуты |
| --- | --- |
| `Staff` (Персонал) | `Name` (Имя) — системное имя атрибута с Ф. И. О. сотрудника. |
| `Cars` (Автомобили) | `Driver` (Водитель) — системное имя атрибута типа «**Запись**», ссылающегося на шаблон записи Staff (Персонал). |

Чтобы получить имя водителя для записи из шаблона *«Автомобили»*, используйте следующее выражение:

```
$Driver->Name

```

Переходить по ссылкам можно неограниченное количество раз, но будьте внимательны, чтобы не образовалось зацикливание.

## Составление запросов на языке формул

Здесь представлен синтаксис и примеры предложений и операторов для запросов на языке формул **{{ productName }}**.

Зарезервированные слова

Следующие слова нельзя использовать в запросе в качестве локальной переменной, так как они зарезервированы как системные:

- `and`, `ascending`, `between`, `by`, `db`, `descending`, `equals`, `from`, `group`, `in`, `into`, `item`, `join`, `let`, `on`, `orderby`, `select`, `source`, `where`;
- слова, начинающиеся с символа подчеркивания (`_`);
- имена [функций и литералов][formula_function_list];

### Синтаксис запроса from where select

| `from` | |
| --- | --- |
| **Описание** | Запрос должен начинаться с предложения `from`. Предложение `from` состоит из следующих частей:   - оператор `from`; - объявление локальной переменной (например, `queryVar`), которая представляет отдельные элементы источника данных (например, запись в шаблоне или аккаунт); - оператор `in`; - источник данных, по которому выполняется запрос. - `from queryVar` — объявление локальной переменной-селектора `queryVar`, в которую будут помещены записи из источника данных. - `in` — объявление источника данных:   - `db->TemplateName` — шаблон записи с системным именем `TemplateName`;   - `$RecordAttributeName` — атрибут типа «**Запись**» с системным именем `RecordAttributeName`, хранящий несколько значений;   - `(from ... where ... select)` — вложенный запрос. Вложенный запрос необходимо заключить в скобки и использовать в нём уникальную переменную-селектор:   Примечание   - В качестве источника данных для запроса `from where select` рекомендуется использовать атрибут типа «**Запись**», содержащий ID записей, из которых требуется произвести выборку. - Запрос по записям, связанным с атрибутом, выполняется быстрее, чем запрос по всем записям из шаблона. - В качестве источника данных можно использовать атрибуты типа «**Запись**», у которых установлен флажок «**Хранить несколько значений**». - Атрибуты, подходящие для запроса, отображаются в подсказке в начале списка с префиксом `$` и суффиксом `(запрос)`: `$AttributeName (запрос)`. |
| **Синтаксис** | `from queryVar in dataSource` |
| **Аргументы** | - `queryVar`: имя локальной переменной - `dataSource`:   - `db->templateName`: шаблон;   - `$path->to->attribute`: путь к атрибуту шаблона;   - `(from queryVar2 in $dataSource2 where condition2 select queryVar2->attribute2)`: вложенный запрос (необходимо заключить в скобки и использовать в нём уникальную переменную-селектор). |
| `where` | |
| **Описание** | Предложение `where condition` задаёт условие выборки записей из источника данных, для которых выражение `condition` возвращает `True`.  Условие `condition` может содержать несколько предикатов, возвращающих `True` или `False`. Используйте для этого логические операторы `&&` (И), `||` (ИЛИ), `==` (РАВНО), `!=` (НЕ РАВНО) и функций `AND()`, `OR()`, `EQUALS()`, `IF()`, `NOT()`, `ANY()`, `ALL()`. |
| **Синтаксис** | `where condition` |
| **Аргументы** | `condition`: логическое значение или выражение, возвращающее `True` или `False`. |
| `orderby` | |
| **Описание** | Предложение `orderby` позволяет отсортировать результаты запроса по значению атрибута найденных записей.  Предложение `orderby` следует использовать между предложениями `where` и `select`.  Предложение `orderby` состоит из следующих частей:   - оператор `orderby`; - атрибут вида `queryVar->sortAttribute`, по которому следует выполнять сортировку результатов запроса; - оператор порядка сортировки:   - `ascending` по возрастанию (по умолчанию, можно не указывать)   - `descending` — по убыванию. |
| **Синтаксис** | - Сортировка по возрастанию: `orderby queryVar->sortAttribute ascending` или `orderby queryVar->sortAttribute` - Сортировка по убыванию: `orderby queryVar->sortAttribute descending` |
| **Аргументы** | `templateAttribute`: атрибут шаблона (источника данных). |
| `select` |
| **Описание** | Предложение `select` задаёт атрибут источника данных, значения которого вернёт запрос.  Оператор `select` может содержать выражение.  В конечном результате учитываются как работа предыдущих операторов, так и любые выражения в самом операторе `select`. |
| **Синтаксис** | `select queryVar->returnAttribute` |
| **Аргументы** | `queryVar->returnAttribute`: атрибут источника данных. |

### Примеры запросов

- Запрос записей районов Москвы с сортировкой по убыванию названия района.

  ```
  from a in db->Cities
  where a->CityName == "Москва"
  orderby a->Districts->DistrictName descending
  select a->Districts

  ```
- Запрос названий и авторов книг, у которых указан автор, с сортировкой по возрастанию имени автора и выводом в формате *«Название: название книги. Автор: имя автора»*.

  ```
  from book in db->Books
  where NOT(EMPTY(book->Author))
  orderby book->Author->Name
  select CONCAT(
      LIST(
          'Название: ', book->Name, '. Автор: ', book->Author->Name
      )
  )

  ```
- Запрос просроченных отправлений (основной запрос) со склада в Сибири (вложенный запрос).

  ```
  from shipment in (
  from warehouse in db->Warehouses
  where warehouse->Region == "Сибирь"
  select warehouse->shipments
  )
  where shipment->DeliveryDate < NOW() select shipment->id

  ```

--8<-- "related_topics_heading.md"

- [Литералы и функции в формулах. Справочник, описания, примеры][formula_function_list]
- [Форматирование значений атрибутов в файле шаблона экспорта и формулах][export_template_file_formula_format_values]
- [Системные атрибуты шаблона аккаунта][account_templates]
- [Примеры формул](https://kb.comindware.ru/category.php?id=881)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
