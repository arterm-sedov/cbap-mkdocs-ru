---
title: Работа с ИИ
kbTitle: Работа с ИИ. Настройка адаптера, low-code-агентов и тестирование
tags:
  - AI
  - LLM
  - low-code-агенты
  - mock-операции
  - адаптер ИИ
  - ассистент
  - бям
  - искусственный интеллект
  - кнопки
  - операции
  - подключения
  - пути передачи данных
  - чат
hide: tags
---

# Работа с ИИ. Настройка адаптера, low-code-агентов и тестирование{: #ai_features_guide }

## Введение {: #ai_features_guide_intro }

Здесь представлены инструкции по настройке и использованию функций искусственного интеллекта в **{{ productName }}**:

- [Настройка адаптера, подключения и пути передачи данных](#ai_features_guide_adapter_setup) — получение ключа API для языковой модели (LLM), создание адаптера, подключения и пути передачи данных.
- [Настройка low-code-агентов](#ai_features_guide_lowcode_agents) — настройка сценариев для обработки сообщений из чата с использованием LLM.
- [Тестирование операций (mock)](#ai_features_guide_mock_testing) — проверка операций без взаимодействия с LLM.
- [Примеры поддерживаемых операций](#ai_features_guide_operations_list) — типы операций и пояснения к полям (справочник).
- [Полные примеры JSON по операциям](#ai_features_guide_full_json) — готовые JSON для каждой из восьми бизнес-задач (MockNavigation и MessageToNavigation) (справочник).

## Настройка адаптера, подключения и пути передачи данных {: #ai_features_guide_adapter_setup .pageBreakBefore }

### Получение ключа для работы с API {: #ai_features_guide_adapter_api_key }

Для работы с языковой моделью необходимо получить ключ API.

Поддерживаются провайдеры GigaChat и OpenRouter.

Ниже даны инструкции для GigaChat.

1. Перейдите на сайт <https://developers.sber.ru>.
2. Войдите в личный кабинет через SberID.
3. Откройте проект GigaChat API в личном кабинете Studio.
4. В левой панели выберите раздел «**Настройки API**».
5. Нажмите кнопку «**Получить ключ**».
6. Сохраните ключ в надёжном месте и используйте его при настройке пути передачи данных для LLM.
7. Скомпилируйте адаптер для обмена данными с LLM.

### Компиляция адаптера {: #ai_features_guide_adapter_compile }

1. На странице «**Администрирование**» выберите пункт «**Инфраструктура**» — «**Адаптеры**».
2. В списке адаптеров создайте адаптер.
3. В свойствах адаптера введите уникальное **системное имя** адаптера, например `ArtificialIntelligence`.
4. Загрузите файл `AIAdapter.zip` в поле «**Исходный код адаптера**».
5. **Сохраните** адаптер.
6. Нажмите кнопку «**Опубликовать**», чтобы скомпилировать адаптер.
7. После успешной компиляции и публикации адаптера создайте для него подключение и путь передачи данных.

См. также _«[Адаптеры. Определения, настройка, удаление][adapters]»_.

### Создание подключения к LLM {: #ai_features_guide_connection_create }

Для взаимодействия с LLM необходимо создать подключение на основе ранее скомпилированного адаптера для LLM.

1. На странице «**Администрирование**» выберите пункт «**Инфраструктура**» — «**Подключения**».
2. Создайте «**пользовательское подключение**» типа «**AI agent adapter**».
3. Введите уникальное **системное имя** (например, `LLMConnection`) и наглядное **описание** подключения.
4. Сохраните подключение.

### Создание пути передачи данных {: #ai_features_guide_route_create }

1.  На странице «**Администрирование**» выберите пункт «**Архитектура**» — «**Пути передачи данных**».
2. Создайте путь передачи данных типа «**Пользовательские подключения**» — «**AI agent adapter**».
3. На вкладке «**Основные свойства**»:

    - введите уникальное **системное имя** (например, `LLMCommunicationRoute`)
    - введите наглядное **описание** пути передачи данных;
    - выберите созданное ранее **подключение** `LLMConnection`.
4. На вкладке «**Атрибуты сообщений**» выберите **Тип сообщения GigaChat**.
5. Настройте параметры на вкладке **Интеграции**:

- **Модель (Llm Model)** — имя языковой модели точно в том виде, в котором его предоставляет провайдер, например `GigaChat-2`.
- **Ключ API (Llm API Key)** — полученный ранее ключь для доступа к API языковой модели.
- **Эндпоинт авторизации (Llm OAuth Endpoint)** — <https://ngw.devices.sberbank.ru:9443/api/v2/oauth>: аутентификация и авторизация при работе с API.
- **Зона авторизации (Llm OAuth Scope)** — набор разрешений при аутентификации через OAuth. Для GigaChat обычно используется `GIGACHAT_API_PERS`.
- **Эндпоинт инференса (Llm Endpoint)** — URL-адрес для взаимодействия c LLM. Для Для GigaChat обычно используется <https://gigachat.devices.sberbank.ru/api/v1/chat/completions>.

!!! tip "Чат с отбивкой вместо реальных ответов ИИ"

    Чтобы в чате отображалась отбивка, а не реальные ответы ИИ, установите флажок **ResponseWithMocks** на вкладке **Интеграции**. Mocks — сервер-заглушка для имитации поведения объектов; находится в адаптере.

## Настройка low-code-агентов {: #ai_features_guide_lowcode_agents .pageBreakBefore }

Low-cod-агент реализуется **одним сценарием** — такой сценарий выступает мини-агентом: сообщение из чата попадает в сценарий, классифицируется при помощи LLM, формируется операция и в чат пользователю отправляется сообщение с действием (кнопкой).

### Предварительные условия {: #ai_features_guide_lowcode_prereq }

- В платформу добавлен адаптер ИИ.
- Создано подключение и путь передачи данных.
- Поля в пути соответствуют провайдеру (например, GigaChat).

В чате можно общаться на любые темы; чаты можно перемещать, удалять и переименовывать.

### Настройка блоков сценария {: #ai_features_guide_lowcode_blocks }

#### 1. Событие: получение сообщения из чата {: #ai_features_guide_event_chat_message }

Это новый блок события. Обрабатываются сообщения только из системного чата.

- **Тип:** Получение сообщения из чата.
- **Контекстный шаблон:** Любой (на настройку не влияет).
- **Имя переменной** — локальная переменная, в которой хранятся сообщение пользователя и его аккаунт. Может быть любым.

Структура переменной:

``` json
{
  "Title": "Сообщение, введённое пользователем",
  "Creator": "id аккаунта пользователя, отправившего сообщение"
}
```

Поле **Title** содержит контент сообщения, а не заголовок.

#### 2. Формирование сообщения для LLM {: #ai_features_guide_form_message_llm }

- Укажите имя набора переменных (любое).
- Создайте переменную с именем **Message** — это зарезервированное системное имя в адаптере; в запросе и ответе оно должно совпадать с переменной в таблице «запрос» пути передачи данных.
- В эту переменную поместите динамически сформированное сообщение пользователя (UserMessage; SystemMessage не используется).

_Пример полного промпта для классификации намерения (Клиент / Сделка / Не определено):_

``` text
FORMAT("Проанализируй входящее сообщение пользователя и определи его намерение: хочет ли он создать Клиента или Сделку.
Учитывай только явные или косвенные указания на создание одной из этих сущностей. Игнорируй все прочие действия (редактирование, просмотр, удаление, уточнение и т.п.), а также любые дополнительные детали, не относящиеся к выбору между «Клиент» и «Сделка».
Если в сообщении содержится запрос на создание клиента (например: «создай клиента», «добавь нового клиента», «хочу завести клиента» и т.п.) — ответь строго: Клиент.
Если в сообщении содержится запрос на создание сделки (например: «создай сделку», «новая сделка», «заведи сделку по клиенту» и т.п.) — ответь строго: Сделка.
Если намерение неясно или отсутствует — ответь: Не определено.
Формат ответа: одно слово — Клиент, Сделка или Не определено. Никаких пояснений, преамбул или дополнительных символов.
Запрос пользователя {0}", LIST($$chat_message->Title))
```

#### 3. Отправка сообщения в LLM {: #ai_features_guide_send_llm }

- **Подключение** — выберите подключение от AI adapter.
- **Путь передачи данных** — выберите путь от AI adapter.
- Переменная сообщения будет промптом для LLM.
- Переменная для успешного ответа хранит ответ от LLM в виде, например: `"response": { "Message": "Ответ LLM" }` (в виде простого текста).

#### 4. Условия обработки ответа LLM {: #ai_features_guide_conditions_llm }

- В зависимости от ответа LLM направляйте выполнение в разные ветки сценария.
- Обязательно предусмотрите ветку условия (маршрут) для непредвиденного ответа модели.
- Далее — обычная логика сценария.

#### 5. Формирование операций (кнопок) {: #ai_features_guide_form_operations }

С помощью действия **Изменить значения переменных** сформируйте массив операций (кнопок), которые нужно отправить вместе с ответом в чат.

!!! important "Порядок и отображение операций"

    Порядок операций важен: первая операция всегда выполняется автоматически и остаётся в чате для повторного использования. Все кнопки в чате исчезают после обновления страницы.

- **Набор переменных** — имя переменной, которая будет содержать кнопку действия.
- **Переменная «operation»** (строго это имя) — структура данных с кнопкой/операцией; это системное поле сообщения, хранящее список операций.
- Операция задаётся в формате JSON: укажите имя кнопки в чате, id объекта, шаблон и форму.

_Пример операции навигации на форму новой записи (клиент):_

``` json
{
  "$type": "Comindware.Conversation.Entities.NavigateOperation, Comindware.Conversation.Entities",
  "type": "Navigate",
  "name": "Создать компанию",
  "payload": {
    "$type": "Comindware.Conversation.Entities.FormNavigationPayload, Comindware.Conversation.Entities",
    "type": "Form",
    "objectId": "cmw.temp.1",
    "template": "oa.1",
    "form": "form.143",
    "complexObjectChanges": []
  }
}
```

- **objectId** для новой записи — идентификатор несуществующей записи (например, `cmw.temp.1`).
- **template** — id шаблона записи; на тройках можно собрать операцию с системными именами, преобразовав алиасы в id.
- **form** — id формы; аналогично можно получить через тройки.
- **complexObjectChanges** — служебное поле; не используется, на поведение не влияет.

_Вторая операция (например, переход на форму новой сделки) — тот же набор переменных, другие значения:_

``` json
{
  "$type": "Comindware.Conversation.Entities.NavigateOperation, Comindware.Conversation.Entities",
  "type": "Navigate",
  "name": "Создать сделку",
  "payload": {
    "$type": "Comindware.Conversation.Entities.FormNavigationPayload, Comindware.Conversation.Entities",
    "type": "Form",
    "objectId": "cmw.temp.2",
    "template": "oa.2",
    "form": "form.144",
    "complexObjectChanges": []
  }
}
```

Последующие операции формируйте по той же схеме с тем же именем набора переменных, но с другими значениями (другая форма, другой template).

#### 6. Отправка ответа агента в чат пользователю {: #ai_features_guide_send_to_chat }

- **Тело сообщения** — текст, который получит пользователь в чат; можно передать любые текстовые данные, в том числе ответ LLM с предыдущих шагов. Используется простой текст без форматирования.
- **Получатели** — пользователь (или набор пользователей), который получит сообщение в свой системный чат; другим пользователям оно не видно.
- **Имя набора переменных с операциями** — укажите имя набора переменных с операциями (в примере выше — _action_).

### Формирование динамических операций {: #ai_features_guide_dynamic_operations }

Для навигации на запись с передачей id записи из переменной используйте `FORMAT()` с экранированием фигурных скобок удвоением `{{` и `}}`:

``` text
FORMAT(
  '{{ "$type": "Comindware.Conversation.Entities.NavigateOperation, Comindware.Conversation.Entities",
  "type": "Navigate", "name": "Карточка звонка", "payload": {{ "$type": "Comindware.Conversation.Entities.FormNavigationPayload, Comindware.Conversation.Entities",
  "type": "Form", "objectId": {0}, "template": "oa.13", "form": "form.216" }} }}',
  LIST($$Call->id)
)
```

При использовании `FORMAT()` фигурные скобки в JSON экранируются двумя фигурными скобками, иначе операция не будет работать.

В полях пути передачи данных (MockNavigation, MessageToNavigation) и в действии **Изменить значения переменных** используйте обычный JSON без экранирования (одиночные `{` и `}`).

## Тестирование операций (mock) {: #ai_features_guide_mock_testing .pageBreakBefore }

В пути передачи данных есть раздел для тестирования операций без обращения к LLM.

### Включение режима mock {: #ai_features_guide_mock_enable }

1. В пути передачи данных на вкладке **Интеграции** установите флажок **ResponseWithMocks**.
2. После этого во всех чатах (всех пользователей), кроме системного, интерфейс будет ожидать ключевое слово и реагировать на него выводом кнопок mock-операций и выполнением первой операции.
3. Сообщение пользователя должно содержать ключевое слово (без учёта регистра).

!!! warning "Отключение LLM при mock"

    При установленном флажке **ResponseWithMocks** взаимодействие с LLM во всех чатах (включая системный) отключается.

### Поле MockNavigation {: #ai_features_guide_mock_navigation }

Поле **MockNavigation** принимает массив операций в формате JSON (без экранирования). Вставьте нужные операции. Пример — операция нажатия кнопки из шаблона записи (UserCommand):

``` json
[
  {
    "$type": "Comindware.Conversation.Entities.UserCommandPageOperation, Comindware.Conversation.Entities",
    "type": "UserCommand",
    "name": "Проанализировать звонок",
    "payload": {
      "$type": "Comindware.Conversation.Entities.UserCommandPayload, Comindware.Conversation.Entities",
      "UserCommandId": "event.910",
      "ObjectId": "629",
      "Kind": "UserEvent"
    }
  }
]
```

- **name** — имя операции; по нему выполняется маппинг ключевой фразы и операции (отображается как кнопка в чате).
- **UserCommandId** — id кнопки (события) в шаблоне записи.
- **ObjectId** — id записи, для которой выполняется операция.

### Поле MessageToNavigation {: #ai_features_guide_message_to_navigation }

Поле **MessageToNavigation** принимает JSON для вызова mock-операций по ключевой фразе. Пример:

``` json
{
  "Звонок": {
    "operations": ["Проанализировать звонок"],
    "responseText": "Звонок проанализирован"
  }
}
```

- Ключ (например, _Звонок_) — **ключевая фраза**, на которую срабатывает mock; при вводе этого слова пользователем в любой чат (кроме системного) возвращается ответ.
- **operations** — массив имён операций из MockNavigation.
- **responseText** — текст ответа пользователю.

### Результат вызова {: #ai_features_guide_mock_result }

После ввода ключевой фразы пользователь видит в чате ответ с текстом из **responseText** и кнопки mock-операций; первая операция из списка выполняется автоматически.

## Перечень поддержанных операций и их составление {: #ai_features_guide_operations_list .pageBreakBefore }

Ниже приведены типы операций, которые можно задавать в **MockNavigation** и вызывать через **MessageToNavigation**, а также пояснения к полям.

### 1. Открыть экземпляр шаблона записи (форма) {: #ai_features_guide_op_open_instance }

**MockNavigation** — элемент типа `NavigateOperation` с `FormNavigationPayload`:

- **objectId** — id записи.
- **template** — id шаблона записи.
- **form** — id формы.
- **name** — название кнопки в чате.

**MessageToNavigation:** ключ — фраза пользователя; в `operations` — значение **name** операции; `responseText` — ответ пользователю.

### 2. Открыть настроенный список {: #ai_features_guide_op_open_list }

**Предусловие:** настроен список с вынесенными колонками, двумя фильтрами и одной сортировкой.

**MockNavigation** — элемент с `DatasetNavigationPayload` (`type`: `RecordTemplateList`):

- **template** — id шаблона записи.
- **name** — название кнопки в чате.
- **query** — объект запроса: **datasetId** (id таблицы, например `lst.262`), **columns** (массив id колонок, например `ds.2288`, …), **filter**, **sorting** (в т.ч. **datasourceId**, **direction** — направление сортировки), **paging**. Идентификаторы **ds.***, **datasetId** и параметр **sorting** можно посмотреть в браузере: F12 → вкладка **Network** → запрос Query → Payload.

**MessageToNavigation** — по той же схеме (ключ фраза, `operations`, `responseText`).

### 3. Актуализация данных (пользовательская операция) {: #ai_features_guide_op_actualize }

**Предусловие:** в шаблоне записи есть текстовые атрибуты (например, ОГРН, ИНН, Адрес).

**MockNavigation** — элемент типа `UserCommandPageOperation` с `UserCommandPayload`:

- **UserCommandId** — id созданной операции (события).
- **ObjectId** — id записи.
- **name** — название кнопки в чате.

**MessageToNavigation** — может объединять несколько операций в одном ответе (например, «Открыть список» и «Актуализировать информацию»).

### 4. Создание записи {: #ai_features_guide_op_create_record }

**Предусловие:** перед составлением JSON откройте инструменты разработчика (F12), создайте новый экземпляр записи в интерфейсе, заполните данные, нажмите **Сохранить** — в Network (вкладка **Network**) найдите запрос Execute и возьмите из ответа (вкладка Response) данные для **dataformChanges** (виджеты **fw.***, **literal**, **time**).

**MockNavigation** — элемент `NavigateOperation` с `FormNavigationPayload` и **dataformChanges**:

- **objectId** — например, `cmw.temp.1` для новой записи.
- **template**, **form** — id шаблона записи и формы.
- В **dataformChanges.widgetChanges** укажите **tempId**, **changes** (виджет **fw.*** и **literal** — вводимые данные). Данные можно взять из ответа запроса Execute (вкладка Response).

**MessageToNavigation** — ключ фраза, `operations` с именем операции, `responseText`.

### 5. Открытие задачи {: #ai_features_guide_op_open_task }

**MockNavigation** — элемент `NavigateOperation` с `TaskNavigationPayload`:

- **taskId** — id задачи.
- **name** — название кнопки в чате.

**MessageToNavigation** — ключ фраза, `operations`, `responseText`.

### 6. Поиск записей {: #ai_features_guide_op_search }

**MockNavigation** — элемент с `GlobalSearchNavigationPayload`:

- **SearchText** — искомое значение.
- **name** — название кнопки в чате.

**MessageToNavigation** — ключ фраза, `operations`, `responseText`.

### 7. Переход в детализацию дашбордов {: #ai_features_guide_op_dashboard }

**Предусловие:** выполнен запрос детализации с фильтром по колонке.

**MockNavigation** — элемент с `ChartNavigationPayload` и вложенным **ChartQuery**:

- **widgetId**, **widgetConfigId**, **datasetId** — id диаграммы/виджета.
- **name** — название кнопки в чате.
- Запрос (columns, filter и т.д.) можно посмотреть: F12 → вкладка **Network** → запрос Get → Payload.

**MessageToNavigation** — ключ фраза, `operations`, `responseText`.

### 8. Навигация на виджет (конкретное поле) {: #ai_features_guide_op_navigate_widget }

**MockNavigation** — элемент `NavigateOperation` с `FormNavigationPayload` и полем **widget**:

- **objectId** — id записи.
- **widget** — id виджета на форме.
- **template** — id шаблона записи.
- **form** — id формы.
- **name** — название кнопки в чате.

**MessageToNavigation** — ключ фраза, `operations`, `responseText`.

### Примеры ключевых фраз и ответов {: #ai_features_guide_operations_examples }

В **MessageToNavigation** ключом служит фраза пользователя; в `operations` указывается **name** операции из **MockNavigation**; в `responseText` — текст ответа в чат. Примеры соответствия:

| Ключевая фраза (пример) | name операции (пример) | responseText (пример) |
| ----------------------- | ---------------------- | --------------------- |
| _Открой экземпляр шз1_ | шз1 | Открыл вам карточку шз1 |
| _Покажи список таблицы 1_ | Все записи | Таблица отображена |
| _Создай тестовую запись_ | Создать тестовую запись | Создал запись и заполнил вашими данными |
| _Открой мне мою задачу_ | Навигация на задачу | Навигация на задачу выполнена |
| _Найди мне все Записи с значением: Тест_ | Записи с значением: Тест | Результаты поиска записей с значением: Тест |
| _Открой Дашборды_ | Дашборд | Открыл вам дашборд |
| _Найди мне текстовое поле_ | Навигация на текстовое поле | Навигировал на текстовый атрибут |

## Полные примеры JSON по операциям {: #ai_features_guide_full_json .pageBreakBefore }

Ниже приведены **полные JSON** для каждой из восьми бизнес-задач: один или несколько элементов для **MockNavigation** и соответствующий фрагмент для **MessageToNavigation**. Идентификаторы (objectId, template, form, datasetId, ds.*, fw.*, taskId, widgetId, UserCommandId и т.д.) в примерах — из черновиков; замените их на значения вашего окружения. Как получить нужные id: F12 → вкладка **Network** → запрос Query/Execute/Get → Payload или Response.

Пошаговые инструкции см. выше в разделах [Настройка адаптера и операций](#ai_features_guide_adapter_setup), [Настройка low-code-агентов](#ai_features_guide_lowcode_agents) и [Тестирование операций (mock)](#ai_features_guide_mock_testing).

### Операция 1: открыть экземпляр шаблона записи (форма) {: #ai_features_guide_full_json_open_instance }

**Задача:** по ключевой фразе открыть карточку конкретной записи (форма).

В **MockNavigation** укажите массив с одним элементом `NavigateOperation` и `FormNavigationPayload`. В **MessageToNavigation** ключ — фраза пользователя; в `operations` — значение **name** из MockNavigation; в `responseText` — ответ в чат.

**MockNavigation** (один элемент):

``` json
[
  {
    "$type": "Comindware.Conversation.Entities.NavigateOperation, Comindware.Conversation.Entities",
    "type": "Navigate",
    "name": "шз1",
    "payload": {
      "$type": "Comindware.Conversation.Entities.FormNavigationPayload, Comindware.Conversation.Entities",
      "type": "Form",
      "objectId": "469",
      "template": "oa.13",
      "form": "form.287"
    }
  }
]
```

**MessageToNavigation** (фрагмент; ключ — фраза, `operations` — массив имён операций, `responseText` — текст ответа):

``` json
{
  "Открой экземпляр шз1": {
    "operations": ["шз1"],
    "responseText": "Открыл вам карточку шз1"
  }
}
```

Поля: **objectId** — id записи; **template** — id шаблона записи; **form** — id формы; **name** — название кнопки в чате.

### Операция 2: открыть настроенный список {: #ai_features_guide_full_json_open_list }

**Задача:** по ключевой фразе открыть список записей с заданными колонками, фильтрами и сортировкой.

**Предусловие:** настроен список с вынесенными колонками, двумя фильтрами и одной сортировкой. Идентификаторы **datasetId** (id таблицы), **columns** (id колонок ds.*), **filter** (FilterTree/FilterLeaf), **sorting** (datasourceId, direction) возьмите из F12 → Network → запрос Query → Payload.

**MockNavigation** (один элемент с `DatasetNavigationPayload`, `type`: `RecordTemplateList`):

``` json
[
  {
    "$type": "Comindware.Conversation.Entities.NavigateOperation, Comindware.Conversation.Entities",
    "type": "Navigate",
    "name": "Все записи",
    "payload": {
      "$type": "Comindware.Conversation.Entities.DatasetNavigationPayload, Comindware.Conversation.Entities",
      "type": "RecordTemplateList",
      "template": "oa.13",
      "query": {
        "$type": "Comindware.Conversation.Entities.DatasetQuery, Comindware.Conversation.Entities",
        "datasetId": "lst.262",
        "columns": ["ds.2288", "ds.2289", "ds.2290", "ds.2291", "ds.2292", "ds.2293", "ds.2294", "ds.2295", "ds.2296"],
        "isPersonal": true,
        "filter": {
          "$type": "Comindware.Conversation.Entities.FilterTree, Comindware.Conversation.Entities",
          "type": "FilterTree",
          "groupOperator": "and",
          "children": [
            {
              "$type": "Comindware.Conversation.Entities.FilterLeaf, Comindware.Conversation.Entities",
              "type": "FilterLeaf",
              "datasourceId": "ds.2294",
              "operator": "gt",
              "value": 1
            },
            {
              "$type": "Comindware.Conversation.Entities.FilterLeaf, Comindware.Conversation.Entities",
              "type": "FilterLeaf",
              "datasourceId": "ds.2295",
              "operator": "eq",
              "value": "account.12"
            }
          ]
        },
        "grouping": [],
        "sorting": [
          {
            "$type": "Comindware.Conversation.Entities.SortingConfiguration, Comindware.Conversation.Entities",
            "datasourceId": "ds.2296",
            "direction": "Desc",
            "nullValuesOnTop": false
          }
        ],
        "paging": {
          "$type": "Comindware.Conversation.Entities.PagingConfiguration, Comindware.Conversation.Entities",
          "page": 0,
          "size": 50
        },
        "stickedColumnsCount": 0,
        "excludeValues": []
      }
    }
  }
]
```

**MessageToNavigation** (фрагмент):

``` json
{
  "Покажи список таблицы 1": {
    "operations": ["Все записи"],
    "responseText": "Таблица отображена"
  }
}
```

### Операция 3: актуализация данных (пользовательская операция) {: #ai_features_guide_full_json_actualize }

**Задача:** выполнить операцию (кнопку) из шаблона записи, например обновление данных по ОГРН/ИНН/Адресу.

**Предусловие:** в шаблоне записи есть текстовые атрибуты (например, ОГРН, ИНН, Адрес). **UserCommandId** — id созданной операции (события) в шаблоне записи; **ObjectId** — id записи.

**MockNavigation** (один элемент `UserCommandPageOperation`):

``` json
[
  {
    "$type": "Comindware.Conversation.Entities.UserCommandPageOperation, Comindware.Conversation.Entities",
    "type": "UserCommand",
    "name": "Актуализировать информацию",
    "payload": {
      "$type": "Comindware.Conversation.Entities.UserCommandPayload, Comindware.Conversation.Entities",
      "UserCommandId": "event.1333",
      "ObjectId": "469",
      "Kind": "UserEvent"
    }
  }
]
```

**MessageToNavigation** может объединять несколько операций в одном ответе:

``` json
{
  "Открой экземпляр записи": {
    "operations": ["Все записи", "Актуализировать информацию"],
    "responseText": "Открыл вам карточку шз1"
  }
}
```

### Операция 4: создание записи {: #ai_features_guide_full_json_create_record }

**Задача:** по ключевой фразе открыть форму новой записи и предзаполнить поля (данные взять из запроса Execute при сохранении формы: F12 → создать экземпляр → заполнить данные → Сохранить → в Network найти Execute → Response).

**Предусловие:** через F12 зафиксирован запрос Execute при создании экземпляра (заполнение данных и нажатие **Сохранить**). В **dataformChanges.widgetChanges** укажите **tempId**, **changes** (виджеты **fw.*** и **literal** — вводимые данные); **commandKind**: `Create`, **typeId** — id шаблона записи.

**MockNavigation** (один элемент с **dataformChanges**):

``` json
[
  {
    "$type": "Comindware.Conversation.Entities.NavigateOperation, Comindware.Conversation.Entities",
    "type": "Navigate",
    "name": "Создать тестовую запись",
    "payload": {
      "$type": "Comindware.Conversation.Entities.FormNavigationPayload, Comindware.Conversation.Entities",
      "type": "Form",
      "objectId": "cmw.temp.1",
      "template": "oa.13",
      "form": "form.287",
      "dataformChanges": {
        "widgetChanges": [
          {
            "objId": null,
            "tempId": "cmw.temp.1",
            "changes": {
              "fw.1879": { "origin": "Store", "literal": 123.0, "time": 1763542700000 },
              "fw.1881": { "origin": "Store", "literal": "account.2", "time": 1763542700001 },
              "fw.1885": { "origin": "Store", "literal": "http://10.9.0.185:8081/", "time": 1763542700002 },
              "fw.1884": { "origin": "Store", "literal": "2222222222", "time": 1763542700003 },
              "fw.1880": { "origin": "Store", "literal": "125009, г. Москва, ул. Тверская, д. 7", "time": 1763542700004 }
            },
            "commandKind": "Create",
            "typeId": "oa.13"
          }
        ],
        "complexObjectChanges": []
      }
    }
  }
]
```

**MessageToNavigation** (фрагмент):

``` json
{
  "Создай тестовую запись": {
    "operations": ["Создать тестовую запись"],
    "responseText": "Создал запись и заполнил вашими данными"
  }
}
```

Поле **complexObjectChanges** зарезервировано и не используется.

### Операция 5: открытие задачи {: #ai_features_guide_full_json_open_task }

**Задача:** по ключевой фразе открыть задачу (TaskNavigationPayload). **taskId** — id задачи.

**MockNavigation** (один элемент с `TaskNavigationPayload`):

``` json
[
  {
    "$type": "Comindware.Conversation.Entities.NavigateOperation, Comindware.Conversation.Entities",
    "type": "Navigate",
    "name": "Навигация на задачу",
    "payload": {
      "$type": "Comindware.Conversation.Entities.TaskNavigationPayload, Comindware.Conversation.Entities",
      "type": "Task",
      "taskId": "474",
      "widget": null,
      "selected": [],
      "dataformChanges": {
        "widgetChanges": [],
        "complexObjectChanges": []
      }
    }
  }
]
```

**MessageToNavigation** (фрагмент):

``` json
{
  "Открой мне мою задачу": {
    "operations": ["Навигация на задачу"],
    "responseText": "Навигация на задачу выполнена"
  }
}
```

### Операция 6: поиск записей {: #ai_features_guide_full_json_search }

**Задача:** по ключевой фразе выполнить глобальный поиск с заданным текстом. **SearchText** — искомое значение.

**MockNavigation** (один элемент с `GlobalSearchNavigationPayload`):

``` json
[
  {
    "$type": "Comindware.Conversation.Entities.NavigateOperation, Comindware.Conversation.Entities",
    "type": "Navigate",
    "name": "Записи с значением: Тест",
    "payload": {
      "$type": "Comindware.Conversation.Entities.GlobalSearchNavigationPayload, Comindware.Conversation.Entities",
      "type": "GlobalSearch",
      "SearchText": "Тест"
    }
  }
]
```

**MessageToNavigation** (фрагмент):

``` json
{
  "Найди мне все Записи с значением: Тест": {
    "operations": ["Записи с значением: Тест"],
    "responseText": "Результаты поиска записей с значением: Тест"
  }
}
```

### Операция 7: переход в детализацию дашбордов {: #ai_features_guide_full_json_dashboard }

**Задача:** по ключевой фразе открыть детализацию дашборда (диаграммы). **Предусловие:** выполнен запрос детализации с фильтром по колонке. Идентификаторы **widgetId**, **widgetConfigId**, **datasetId** и тело запроса **ChartQuery** возьмите из F12 → Network → запрос Get → Payload.

**MockNavigation** (один элемент с `ChartNavigationPayload` и вложенным **ChartQuery**):

``` json
[
  {
    "$type": "Comindware.Conversation.Entities.NavigateOperation, Comindware.Conversation.Entities",
    "type": "Navigate",
    "name": "Дашборд",
    "payload": {
      "$type": "Comindware.Conversation.Entities.ChartNavigationPayload, Comindware.Conversation.Entities",
      "type": "Chart",
      "widgetId": "dwc.14",
      "query": {
        "$type": "Comindware.Conversation.Entities.ChartQuery, Comindware.Conversation.Entities",
        "widgetConfigId": "dwc.14",
        "dataPointIndex": 0,
        "dateFilterType": "Undefined",
        "datasetId": "dwc.14",
        "columns": ["ds.2332", "ds.2333", "ds.2334"],
        "isPersonal": true,
        "filter": {
          "$type": "Comindware.Conversation.Entities.FilterTree, Comindware.Conversation.Entities",
          "type": "FilterTree",
          "groupOperator": "and",
          "children": [
            {
              "$type": "Comindware.Conversation.Entities.FilterLeaf, Comindware.Conversation.Entities",
              "type": "FilterLeaf",
              "datasourceId": "ds.2334",
              "operator": "gt",
              "value": 1
            }
          ]
        },
        "grouping": [],
        "excludeValues": [],
        "withRows": true
      }
    }
  }
]
```

**MessageToNavigation** (фрагмент):

``` json
{
  "Открой Дашборды": {
    "operations": ["Дашборд"],
    "responseText": "Открыл вам дашборд"
  }
}
```

### Операция 8: навигация на виджет (конкретное поле) {: #ai_features_guide_full_json_navigate_widget }

**Задача:** по ключевой фразе открыть форму записи с фокусом на конкретном виджете (поле). **widget** — id виджета на форме; **objectId** — id записи; **template**, **form** — id шаблона записи и формы.

**MockNavigation** (один элемент с полем **widget** в FormNavigationPayload):

``` json
[
  {
    "$type": "Comindware.Conversation.Entities.NavigateOperation, Comindware.Conversation.Entities",
    "type": "Navigate",
    "name": "Навигация на текстовое поле",
    "payload": {
      "$type": "Comindware.Conversation.Entities.FormNavigationPayload, Comindware.Conversation.Entities",
      "type": "Form",
      "objectId": "469",
      "widget": "fw.1880",
      "template": "oa.13",
      "form": "form.287",
      "dataformChanges": {
        "widgetChanges": [],
        "complexObjectChanges": []
      }
    }
  }
]
```

**MessageToNavigation** (фрагмент):

``` json
{
  "Найди мне текстовое поле": {
    "operations": ["Навигация на текстовое поле"],
    "responseText": "Навигировал на текстовый атрибут"
  }
}
```

## Ограничения и планы развития {: #ai_features_guide_limits_and_roadmap }

В статье описана только реализованная на текущий момент функциональность. Ограничения и запланированные изменения:

- **Обработка сообщений:** обрабатываются сообщения только из системного чата; выбор источника сообщений (системный чат или чат сценария) в текущей версии недоступен.
- **Планы:** планируется появление сценариев со своими чатами и возможность выбора, из какого чата обрабатывать сообщения (системный или чат сценария).

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Адаптеры. Определения, настройка, удаление][adapters]_
- _[Подключения. Определения, типы, создание, настройка, удаление][connections]_
- _[Пути передачи данных][communication_routes]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
