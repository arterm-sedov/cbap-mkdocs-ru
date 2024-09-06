---
title: Сценарии
tags:
  - сценарии
  - сценарий
  - триггеры
  - события
  - событие сценария
  - сценарий
  - триггер
  - действия сценария
  - действие сценария
  - элементы сценария
  - шаги сценария
  - проверка сценария
  - удаление сценария
  - очистка сценария
  - свойства сценария
hide:
  - tags
kbId: 2151
---

# Сценарии. Определение, создание, настройка, использование {: #scenarios}

!!! question "Определение"

	**Сценарий** — это алгоритм валидации и обработки данных. Сценарий содержит цепочку из [действий][scenario_actions], которая будет запущена при срабатывании указанного [события][scenario_event].

	Новые сценарии можно создавать из списка сценариев или из диаграммы бизнес-процесса. Для их настройки предусмотрен удобный визуальный конструктор.

	Сценарий может запуститься в нескольких случаях:

	- на входе токена в элемент диаграммы процесса;
	- на выходе токена из элемента диаграммы процесса;
	- при запуске процесса;
	- при нажатии кнопки;
	- при создании или изменении записи в целевом шаблоне;
	- при получении сообщения от внешних систем.

	Сценарии являются удобным инструментом настройки приложений **{{ productName}}**. Они позволяют:

	- создавать и изменять записи;
	- переключаться между шаблонами в приложении и редактировать данные;
	- создавать документы;
	- запускать процессы;
	- получать, отправлять и обрабатывать данные из внешних систем;
	- организовывать циклы и условное выполнение операций.

## Просмотр списка сценариев в приложении

1. Откройте страницу [«**Администрирование**» — «**Сценарии**»][administration].
2. Отобразится страница «**Сценарии**», на которой доступны следующие действия:

	- **Создать** — нажмите эту кнопку, чтобы создать [новый сценарий][scenarios].
	- **Удалить** — установите флажки выбора для подлежащих удалению сценариев и нажмите эту кнопку, чтобы удалить их.
	- **Свойства** — установите флажок выбора для одного сценария и нажмите эту кнопку, чтобы настроить [свойства сценария][scenarios].
	- **Открыть** — дважды нажмите строку сценария, чтобы открыть [конструктор сценария][scenarios].

3. Нажмите кнопку «**Создать**».
4. Отобразится окно «**Новый сценарий**».
5. Настройте [свойства сценария][scenario_designer].

    _![Окно свойств нового сценария](scenario_create_properties.png)_

6. Сценарии обладают следующими свойствами:
{: #scenario_properties}

- **ID** — уникальный идентификатор сценария.
- **Название** — наглядное наименование сценария.
- **Событие** — описание события, по которому запускается сценарий.
- **Контекст выполнения** — аккаунт, от имени которого выполняется сценарий.
    - **От имени системы** — сценарий будет выполняться с полными правами аккаунта «**Система**», без учёта роли и разрешений пользователя, инициировавшего событие, по которому запускается сценарий. То есть сценарий сможет выполнять _любые действия_.
    - **От инициатора** — сценарий будет выполняться при наличии необходимых разрешений у пользователя, инициировавшего событие, по которому выполняется сценарий. В случае отсутствия у пользователя разрешений система выдаст ошибку.
- **Статус** — состояние сценария.
    - **Активен** — сценарий выполняется при каждом наступлении заданного события.
    - **Приостановлен** — сценарий не выполняется при наступлении заданного события.

7. Нажмите кнопку «**Сохранить**».
8. Откроется конструктор сценария.
9. [Настройте сценарий][scenario_designer].

_![Список сценариев в приложении](scenarios_list.png)_

## Конструктор сценария {: #scenario_designer}

Для настройки сценариев в **{{ productName }}** предусмотрен удобный визуальный конструктор.

Открыть конструктор сценария можно двумя способами:

* Дважды нажмите строку сценария в [списке сценариев][scenarios].
* Нажмите кнопку «**Сценарий на входе**» или «**Сценарий на выходе**» в меню элемента диаграммы бизнес-процесса.

	_![Кнопки создания сценария на входе и выходе из элемента диаграммы процесса](scenario_exit_enter_process_element.png)_

В конструкторе сценария предусмотрены следующие кнопки настройки сценария:

1. **Свойства** — настройка [свойств сценария](#scenario_properties).
2. **Очистить** — безвозвратное удаление всех элементов сценария. После нажатия этой кнопки в сценарий будет помещено пустое начальное событие «**Нажатие кнопки**», как если бы сценарий был создан заново.
3. **Удалить** — безвозвратное удаление сценария.
4. **Проверить** — проверка целостности и работоспособности сценария. При нажатии этой кнопки отобразится панель «**Результат проверки**» с перечнем выявленных ошибок в сценарии. Элементы сценария с ошибкой будут выделены красным цветом.

    _![Конструктор сценария](scenario_designer.png)_

## Кнопки настройки элементов сценария

При наведении на него указателя мыши на элемент сценария отображаются кнопки настройки элемента.

1. **Изменить** <i class="fa-light  fa-edit"></i> — настройка свойств элемента.
2. **Перейти к контекстному шаблону** <i class="fa-light  fa-external-link"></i> — переход к [шаблону][templates], в контексте которого выполняется элемент сценария.
3. **Удалить** <i class="fa-light  fa-trash-alt"></i> — безвозвратное [удаление действия сценария](#удаление-действия).
4. **Добавить действие** <i class="fa-light  fa-plus-circle"></i> — [создание действия](#создание-действия) после текущего элемента или внутри него.

    _![Кнопки настройки элемента сценария](scenario_element_buttons.png)_

!!! Warning "Внимание!"

    При настройке сценария изменения сохраняются и применяются автоматически.

### Создание действия

!!! note "Примечание"

	Внутрь действий «**Сменить контекст**», «**Выполнить по условиям**», «**Повторять по числовому счётчику**», «**Повторять по количеству объектов**» можно поместить другие действия.

1. Наведите указатель мыши на элемент сценария, после или внутрь которого требуется добавить действие.
2. Нажмите кнопку «**Добавить действие**» <i class="fa-light  fa-plus-circle"></i>.
3. Выберите необходимое действие в раскрывающемся меню.
4. В конструкторе сценария появится новое действие.
5. [Настройте действие](#кнопки-настройки-элементов-сценария).

    _![Создание действия в сценарии](scenario_create_action.png)_

### Удаление действия

1. Наведите указатель мыши на подлежащее удалению действие.
2. Нажмите кнопку «**Удалить**» <i class="fa-light  fa-trash-alt"></i>.
4. Подтвердите удаление действия.

    _![Удаление действия из сценария](scenario_delete_action.png)_

## Примеры использование сценариев в процессах

Существует множество примеров использования сценариев:

- [Пример: согласование заявлений по эл. почте. Настройка подключений, путей передачи данных и диаграммы процесса](https://kb.comindware.ru/article.php?id=2515)
- [Внешняя СУБД (MySQL, MSSQL, Oracle, Postgres). Отправка SQL-запроса SELECT. Настройка подключения, пути передачи данных и сценария](https://kb.comindware.ru/article.php?id=2498)
- [Внешняя СУБД (MySQL, MSSQL, Oracle, PostgreSQL). Получение данных по таймеру. Настройка подключения, пути передачи данных и сценария](https://kb.comindware.ru/article.php?id=2135)
- [Отправка HTTP-запросов типа GET. Пример: настройка подключения, пути передачи данных и сценария для обработки запросов в формате JSON](https://kb.comindware.ru/article.php?id=2509)
- [Настройка универсального процесса согласования](https://kb.comindware.ru/article.php?id=2320)
- [Отправка уведомлений с помощью Telegram. Пример: настройка подключения, пути передачи данных, сценария, приложения и Telegram-бота](https://kb.comindware.ru/article.php?id=2610)
- [Копирование записи вместе с прикреплённым документом. Настройка сценария](https://kb.comindware.ru/article.php?id=2608)
- [Получение сообщений через Kafka. Настройка подключения, пути передачи данных и сценария](https://kb.comindware.ru/article.php?id=2606)
- [Шевроны. Визуализация этапов процесса. Пример настройки](https://kb.comindware.ru/article.php?id=2582)
- [Документы с электронной подписью: настройка приложения и использование](https://kb.comindware.ru/article.php?id=2139)

--8<-- "related_topics_heading.md"

**[Настройка действий сценария][scenario_actions]**

**[Использование переменных в сценарии][scenario_variables]**

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}