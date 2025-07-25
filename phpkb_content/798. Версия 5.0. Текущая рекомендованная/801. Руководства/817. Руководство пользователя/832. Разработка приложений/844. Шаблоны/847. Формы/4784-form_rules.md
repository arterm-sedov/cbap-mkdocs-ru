---
title: Правила для формы. Определения, логика работы и настройка
kbId: 4784
---

# Правила для формы. Определения, логика работы и настройка

## Определения

- **Правила для формы** предназначены для реализации трех сценариев работы конечного пользователя:
  - автоматическое условное и безусловное заполнение данными полей формы (значения по умолчанию, зависимости полей и т.д.);
  - динамическое изменение внешнего вида формы (изменение доступности и видимости полей и областей);
  - проверка значений, введенных в поля формы.
- Каждое [правило](#настройка-правила) состоит из одного или нескольких действий над [элементами формы][forms] и задаёт условие их выполнения.
- Каждое [действие](#настройка-действия) выполняется над одним элементом формы.
- Действие входит в состав правила.
- Для каждого действия можно задать отдельное условие выполнения.
- Правила и действия выполняются независимо друг от друга и последовательно, сверху вниз по порядку их расположения в конструкторе.

## Переход к конструктору правил для формы

Настроить правила для формы можно с помощью визуального конструктора следующим образом.

1. Откройте [конструктор формы][forms].
2. Нажмите значок *‌* рядом с заголовком формы в конструкторе.
3. В раскрывающемся меню выберите пункт «**Правила для формы**».

_![Переход к конструктору правил для формы](https://kb.comindware.ru/assets/form_rules_menu.png)_

4. Отобразится конструктор правил для формы, состоящий из следующих областей:

   **(1) Панель элементов** — содержит элементы, которые можно перетащить в рабочую область.

   - [**Правило**](#настройка-правила) — набор действий, выполняющихся последовательно при соблюдении заданного условия.
   - [**Действие**](#настройка-действия) — действие над [элементом формы][forms], которое будет выполняться при соблюдении условий, заданных в правиле и действии.

   **(2) Рабочая область** — содержит правила и действия для формы.

   **(3) Панель свойств** — позволяет настроить правила и действия для формы.

   **(4) Кнопки:**

   - **Сохранить** — сохранение правил для формы.
   - **Очистить** — удаление всех правил для формы.
   - **Настроить шаблон** *‌* — переход к странице «**Свойства**» шаблона.
5. Перетащите правила и действия с панели элементов на рабочую область конструктора правил для формы.
6. Настройте [правила](#настройка-правила) и [действия](#настройка-действия) с помощью панели свойств.

_![Конструктор правил для формы](https://kb.comindware.ru/assets/form_rules_designer.png)_

## Настройка правила

**Правило** является контейнером для действий и задаёт базовое условие их выполнения.

Логика работы правил

Правила выполняются независимо друг от друга, последовательно по порядку следования в конструкторе — сверху вниз.

Это важно понимать, так как если в разных правилах есть действия, выполняющие действия над одним и тем же элементом формы и при этом условия выполнения этих правил вернули `true`, в итоге над этим элементом формы будут выполнены действия из правила, которое находится ниже в конструкторе, т. е. выполнится последним.

1. Перетащите правило из панели элементов на рабочую область или выберите имеющееся правило.
2. Чтобы изменить порядок выполнения правил, перетаскивайте их в рабочей области.
3. Настройте правило с помощью панели «**Свойства правила**»:

   - **Название** — наглядное наименование правила.
   - **Условие выполнения**— формула или выражение на языке N3, которое должно возвращать `true` или `false`.
     - Если выражение вернёт `true`, то будут последовательно выполнены действия внутри правила (сверху вниз по порядку их расположения в конструкторе).
     - Если выражение вернёт `false` или пустое значение, действия внутри правила не будут выполняться.
     - Проверка условий выполнения правил происходит после внесения изменений в любое поле на форме, а также при открытии формы.

   Контекст условия выполнения правила

   - Условие выполнения правила для формы вычисляется в контексте записи, для которой открыта форма.
   - Если форма с правилами вложена в другую форму, то контекстом для условий выполнения правил вложенной формы является запись, которая выводится о вложенной форме:
     - если вложенная форма относится к текущей записи, то контекстом является текущая запись;
     - если вложенная форма относится к шаблону, связанному с [атрибутом типа «**Запись**»][attribute_record], то контекстом является запись, указанная в этом атрибуте.

_![Настройка правила](https://kb.comindware.ru/assets/form_rules_properties.png)_

## Настройка действия

**Действие** определяет изменение, которое необходимо произвести с элементом формы или данными в поле при соблюдении условия выполнения действия и его родительского правила.

Логика работы действий

Действия выполняются независимо друг от друга, последовательно по порядку следования в правиле — сверху вниз.

Если в правиле есть действия над одним и тем же элементом формы, будут последовательно выполнены все эти действия с учётом их условий выполнения.

1. Перетащите действие из панели элементов в правило или выберите имеющееся действие.
2. Настройте [свойства действия](#типы-и-свойства-действий) с помощью панели «**Свойства действия**».
3. Чтобы изменить порядок выполнения действий, перетаскивайте их в правилах.

### Типы и свойства действий

Предусмотрены действия следующих типов, применимые к различным элементам формы:

- [**Изменить доступ**](#свойства-действия-изменить-доступ) — позволяет определить доступность элемента формы для конечного пользователя;
- [**Установить значение**](#свойства-действия-установить-значение) — позволяет задать новое значение полей атрибутов;
- [**Показать ошибку**](#свойства-действия-показать-ошибку) — позволяет вывести на форме сообщение, привязанное к указанному элементу.

#### Доступные действия для различных элементов формы

| Тип элемента формы | Изменить доступ | Установить значение | Показать ошибку |
| --- | --- | --- | --- |
| Статические элементы | **+** | **−** | **−** |
| Поля атрибутов | **+** | **+** | **+** |
| Столбцы таблиц | **+** | **+** | **+** |
| Вложенные формы | **+** | **−** | **−** |

#### Общие свойства действий

У действий всех типов предусмотрены перечисленные ниже свойства.

- **Элемент формы** — элемент, над которым необходимо выполнить действие: статический элемент, поле, столбец таблицы или вложенная форма.
- **Действие** — [тип действия](#типы-и-свойства-действий), которое необходимо выполнить над выбранным элементом. Появляется после выбора элемента формы.
- **Условие выполнения** — условие, которое применяется дополнительно к [условию выполнения правила](#настройка-правила).
  - Действие «[**Изменить доступ**](#свойства-действия-изменить-доступ)» или «[**Установить значение**](#свойства-действия-установить-значение)» будет выполнено, если выражение вернёт `true`.
  - Действие «[**Показать ошибку**](#свойства-действия-показать-ошибку)» будет выполнено, если выражение вернёт `false` или пустое значение.
  - Проверка условий выполнения и выполнение действий происходят после внесения изменений в любое поле на форме, а также при открытии формы.

Контекст условия выполнения действия

Контекст вычисления условия выполнения действия зависит от того, к какому элементу формы применяется действие:

- если элемент не является столбцом таблицы, то контекстом является текущая запись, для которой открыта форма;
- если элемент является столбцом таблицы, то контекстом является запись, которая относится к строке таблицы атрибута типа «**Запись**».

_![Настройка действия](https://kb.comindware.ru/assets/form_rules_properties_action.png)_

Свойства действий каждого типа представлены в ниже.

#### Свойства действия «Изменить доступ»

Это действие предназначено для смены режима доступа и видимости элемента на форме.

Действие «**Изменить доступ**» выполняется при открытии формы и после внесения изменений в любое поле формы, если условия выполнения правила и действия возвращают `true`.

Помимо [общих свойств](#общие-свойства-действий) у этого действия предусмотрено свойство «**Новое значение**».

В этом поле следует выбрать режим доступа для указанного элемента формы:

- **Требовать ввод**— значение поля должно быть обязательно заполнено на момент сохранения формы;
- **Разрешить ввод** — в поля внутри выбранного элемента можно вводить значения;
- **Только чтение** — элемент отображается, но поля внутри него нельзя вводить значения;
- **Скрыть** — элемент не отображается на форме.

Логика работы действия «Изменить доступ»

Изменение режима доступа к элементу формы применяется только до следующего изменения данных на форме:

- При изменении данных на форме для элемента устанавливается исходный режим доступа, заданный в конструкторе формы.
- Все правила и действия выполняются заново.
- Если для новых данных условия выполнения правил и действий больше не выполняются, устанавливается исходный режим доступа, заданный в конструкторе формы.

**Доступные режимы доступа для элементов формы различных типов**

| Тип элемента формы | Требовать ввод | Разрешить ввод | Только чтение | Скрыть |
| --- | --- | --- | --- | --- |
| Статические элементы | **−** | **+** | **+** | **+** |
| Поля атрибутов | **+** | **+** | **+** | **+** |
| Столбцы таблиц | **+** | **+** | **+** | **+** |
| Поля вычисляемых атрибутов | **−** | **−** | **+** | **+** |
| Вложенные формы | **−** | **+** | **+** | **+** |

#### Свойства действия «Установить значение»

Это действие предназначено для изменения данных в полях атрибутов и столбцов таблиц на форме.

Действие «**Установить значения**» выполняется при открытии формы и после внесения изменений в любое поле формы, если условия выполнения правила и действия возвращают `true`.

Помимо [общих свойств](#общие-свойства-действий) у этого действия предусмотрено свойство «**Новое значение**».

В это поле следует вести **формулу**, выражение на языке **N3** или **значение.**

Тип **нового значения** должен соответствовать типу данных атрибута, с которым связано поле на форме:

- **Аккаунт** — один или несколько идентификаторов аккаунтов;
- **Гиперссылка** — строка с URL-адресом;
- **Дата и время**— `DATE()`;
- **Длительность** — `DURATION()`;
- **Документ** — один или несколько идентификаторов документов;
- **Запись** — один или несколько идентификаторов записей из связанного шаблона.
- **Изображение** — один или несколько идентификаторов изображений;
- **Логический** — `true` или `false`;
- **Организационная единица** — один или несколько идентификаторов оргединиц;
- **Роль** — один или несколько идентификаторов ролей;
- **Список значений** — идентификатор значения из списка;
- **Текст** — строковое значение;
- **Чертёж** — идентификаторы записей, привязанных к чертежу;
- **Число** — `DECIMAL()`;
- **Штрихкод** — строка, которая будет закодирована в штрихкоде.

Контекст вычисления нового значения

Контекст вычисления **нового значения** поля зависит от того, к какому элементу формы применяется действие:

- если элемент не является столбцом таблицы, то контекстом является текущая запись, для которой открыта форма;
- если элемент является столбцом таблицы, то контекстом является запись, которая относится к строке таблицы атрибута типа «**Запись**».

Если **новое значение** будет пустым, то при выполнении действия поле на форме будет очищено.

Значение поля на форме может изменить другое действие или конечный пользователь.

#### Свойства действия «Показать ошибку»

Это действие предназначено для проверки значений полей атрибутов и столбцов таблиц и вывода сообщения у поля на форме.

Действие «**Показать ошибку**» выполняется только при попытке сохранения экранной формы, если условие выполнения правила возвращает `true` и условие выполнения действия возвращает `false`.

Помимо [общих свойств](#общие-свойства-действий) у этого действия предусмотрены перечисленные ниже свойства.

- **Тип сообщения**:
  - **Предупреждение** — при сохранении формы выводит предупреждение на указанном поле формы, при этом данные на форме будут сохранены.
  - **Ошибка** — при сохранении формы выводит ошибку на указанном поле формы, при этом данные на форме нельзя будет сохранить, пока ошибка не будет устранена.
- **Сообщение** — введите строковое **значение** с текстом сообщения либо **формулу** или выражение на языке **N3**, возвращающие текст сообщения.

_![Внешний вид сообщения об ошибке на поле](https://kb.comindware.ru/assets/form_rules_show_error.png)_

## Удаление правил и действий

1. Откройте [конструктор правил для формы](#переход-к-конструктору-правил-для-формы).
2. Выберите правило или действие и перетащите его на панель элементов.
3. Подтвердите удаление удаления правила или действия.
4. Для очистки всех настроенных правил и действий можно нажать кнопку «**Очистить**».
5. Чтобы сохранить изменения, нажмите кнопку «Сохранить».

_![Удаление правила для формы](https://kb.comindware.ru/assets/form_rules_delete.png)_

Удаление правил для формы

--8<-- "related_topics_heading.md"

**[Формы. Определения, редактирование, удаление][forms]**

**[Динамические элементы формы: поля атрибутов и вложенные формы. Настройка представления][form_dynamic_elements]**

**[Статические элементы формы: области, вкладки, колонки, статичный текст. Настройка представления][form_static_elements]**

**[Атрибуты. Определения, типы, настройка, архивирование, удаление][attributes]**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
