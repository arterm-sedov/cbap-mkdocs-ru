---
title: Подсистема журналирования
kbId: 
---

# Подсистема журналирования {: #logging_engine }

## Описание подсистемы журналирования

Подсистема журналирования **{{ productName }}** использует библиотеку _NLog_ (с открытым исходным кодом), которая записывает данные в журналы.

Полная документация по настройке _NLog_ для журналирования представлена по адресу: _[https://github.com/NLog/NLog/wiki/File-target](https://github.com/NLog/NLog/wiki/File-target)_

ПО позволяет настроить уровень журналирования, правила формирования событий в журналах, место хранения журналов, порядок и набор параметров именования журналов, а также ограничения по размеру и предельному количеству журналов, с помощью конфигурационных файлов.

Подробное описание структуры конфигурационного файла см. в документации _NLog_ по адресу: _[https://github.com/NLog/NLog/wiki/Tutorial](https://github.com/NLog/NLog/wiki/Tutorial)_

## Типы журналов {: .pageBreakBefore }

ПО ведёт следующие журналы:

- [Адаптеры](#logging_engine_adapter_logs)
- [Аудит](#logging_engine_audit_log)
- [Интеграция](#журнал-интеграции)
- [Интеграция — сырые данные](#журнал-интеграции-с-сырыми-данными)
- [Исправность ПО](#журнал-исправности)
- [Обновление](#журнал-обновления)
- [Ошибки](#журнал-ошибок)
- [Процессы](#журнал-процессов)
- [Системный журнал](#системный-журнал)
- [Резервное копирование](#журнал-резервного-копирования)
- Трансфер — в составе журнала [ошибок](#журнал-ошибок)

Каждый журналов содержит структурированный текст с пробелами в качестве разделителей.

В качестве инструментов чтения и анализа журналов можно использовать любой инструмент, представленный на рынке. Например, есть мощный инструмент Kibana _[https://www.elastic.co/products/kibana](https://www.elastic.co/products/kibana)_, который обладает широким спектром функций по сбору журналов с различных ресурсов и их глубокому анализу с различными визуальными представлениями, в том числе в виде графиков.

#### Правила формирования журналов {: #logging_engine_rules }

Журналы формируются и выводятся в `stdout` в следующем формате:

```
[CMW.SeviceName][LogName] - LogLevel – LogMessage
```

Здесь `[LogName]` — имя журнала.

#### Типы событий в журналах {: .pageBreakBefore }

В журналах предусмотрены следующие типы событий:

- `Fatal` — критическая ошибка в работе ПО;
- `Error` — ошибка в работе ПО;
- `Warn` — некорректное поведение, но ПО продолжает свою работу;
- `Info` — обычное событие, например отправка письма, обновление данных аккаунта;
- `Debug` — выполнение запросов, аутентификация пользователей;
- `Trace` — запуск методов, завершение методов.

#### Журнал аудита {: #logging_engine_audit_log .pageBreakBefore }

Журнал аудита содержит перечисленные ниже события:

- Неуспешные попытки входа в Систему.
- Успешный вход в Систему.
- Выход из Системы.
- Веб-запросы клиента, отправляемые пользователями на сервер (запрос данных или сохранение данных).
- Изменения системных ролей и ролей в приложениях.
- Попытки несанкционированного доступа для просмотра, создания, редактирования и удаления данных в следующих разделах:
    - API
    - Записи, экземпляры процессов, аккаунты
    - Прикреплённые к записям файлы
    - Страницы:
        - Администрирование системы
            - Темы
            - Дизайн страницы входа и регистрации
            - Приложения
            - Разделы навигации
            - Шаблоны
            - Функции
            - Пути передачи данных
            - Аккаунты
            - Группы
            - Системные роли
            - Аудит разрешений аккаунтов
            - Замещение
            - Регистрация и вход
            - Мониторинг
            - Журналы событий
            - Лицензирование
            - Резервное копирование
            - Управление системными службами
            - Подключения
            - Производительность
            - Конфигурация журналирования
            - Глобальная конфигурация
        - Администрирование приложения
            - Шаблоны
            - Роли
            - Разделы навигации
            - Функции
            - Переменные
            - Сценарии
            - Интернет-магазин
            - Интеграции
            - Пути передачи данных
            - Active Directory
            - Аудит разрешений аккаунтов
            - Активность компонентов
            - Управление версиями

Стандартное имя журнала аудита: `Audit`
{: .pageBreakBefore }

Журнал сообщений аудита содержит следующие сведения:

- дата события;
- время события;
- тип сообщения;
- ID сеанса;
- имя аккаунта, инициировавшего событие;
- IP-адрес клиента;
- адрес сервера;
- статус обработки запроса;
- длительность обработки запроса;
- запрос или текст сообщения;
- сведения об изменении роли.

#### Журнал интеграции {: .pageBreakBefore }

Журнал интеграции содержит информационные сообщения по событиям, возникающим в ходе работы интеграционных сервисов ПО (таких, как подключения и адаптеры).

Стандартное имя журнала ошибок: `Integration`

Журнал интеграции содержит следующие сведения:

- дата события;
- время события;
- тип сообщения;
- ID сеанса;
- имя аккаунта, инициировавшего событие;
- имя сервера;
- порт сервера
- IP-адрес клиента;
- идентификатор интеграции;
- идентификатор подключения;
- текст сообщения.

#### Журнал интеграции с сырыми данными {: .pageBreakBefore }

Журнал интеграции с сырыми данными содержит те же сведения, что журнал интеграции, но с полным содержимым сообщений от внешних систем.

Стандартное имя журнала с сырыми данными: `Integration_raw`

Журнал интеграции с сырыми данными содержит следующие сведения:

- дата события;
- время события;
- тип сообщения;
- ID сеанса;
- имя аккаунта, инициировавшего событие;
- адрес сервера;
- порт сервера;
- IP-адрес клиента;
- текст сообщения.

#### Журнал исправности {: .pageBreakBefore }

Журнал исправности содержит сведения о состоянии экземпляра ПО: дисковом пространстве, использовании подключений, работе сервиса {{ openSearchVariants }}, работе подсистем, выполнении экземпляров процессов.

Стандартное имя журнала исправности: `Heartbeat`

Журнал исправности ПО содержит следующие сведения:

- дата события;
- время события;
- тип сообщения;
- ID сеанса;
- имя аккаунта, инициировавшего событие;
- адрес сервера;
- порт сервера;
- IP-адрес клиента;
- текст сообщения.

#### Журнал обновления {: .pageBreakBefore }

Журнал обновления содержит сведения о результатах обновления версий ПО.

Журнал обновления разделён на два:

- `UpgradeOntology` — информация об обновлении структуры данных;
- `Update` — информация о ходе процесса обновления.

Журнал обновления содержит следующие сведения:

- дата события;
- время события;
- тип сообщения;
- ID сеанса;
- имя аккаунта, инициировавшего событие;
- адрес сервера;
- порт сервера;
- IP-адрес клиента;
- текст сообщения.

#### Журнал ошибок {: .pageBreakBefore }

Журнал ошибок содержит данные обо всех ошибках, возникающих в ходе работы экземпляра ПО, а также об [импорте и экспорте версий приложений][version_control].

Стандартное имя журнала ошибок: `Error`

Журнал ошибок содержит следующие сведения:

- дата события;
- время события;
- тип сообщения;
- ID сеанса;
- имя аккаунта, инициировавшего событие;
- имя сервера;
- порт сервера;
- IP-адрес клиента;
- идентификатор события;
- имя подсистемы, в которой произошло событие;
- длительность обработки запроса;
- версия ПО;
- идентификатор интеграции;
- идентификатор подключения;
- сообщение об ошибке.

#### Журнал процессов {: .pageBreakBefore }

Журнал процессов содержит сведения о движении токенов по элементам экземпляров процессов.

Стандартное имя журнала процессов: `Process`

Журнал процессов содержит следующие сведения:

- дата события;
- время события;
- тип сообщения;
- идентификатор экземпляра процесса;
- идентификатор токена;
- идентификатор элемента экземпляра процесса;
- текст сообщения;
- длительность выполнения.

##### Рекомендации по чтению журнала процессов {: .pageBreakBefore }

- В журнале процессов отражается факт создания экземпляра процесса с указанием его идентификатора.
- Чтобы журнал процессов содержал более наглядные сведения, при настройке диаграммы процесса давайте элементам понятные системные имена.
- Для элемента диаграммы процесса указываются сведения о трёх событиях:
    - создание токена или вход токена в элемент — строка с идентификатором элемента вида `Enter(psa.XXX) by Flow:psf.XXX` (при создании токена не указывается идентификатор потока);
    - выполнение элемента — строка с идентификатором элемента вида `Execute` или `ContinueExecute`;
    - выход токена из элемента — строка с идентификатором потока вида `Exit by Flow:psf.XXX`.
- В строке события могут быть указаны следующие сведения:
    - идентификатор экземпляра процесса вида `PID:XXX`;
    - идентификатор токена вида `TID:ptkn.XX`;
    - системное имя и идентификатор элемента вида `(elementSystemName)psa.XXX`;
    - системное имя и идентификатор потока вида `psf.XXX`;
    - идентификатор потока с идентификатором потока вида `Flow:psf.XXX`;
    - перечень последующих элементов, начинающийся с ключевого слова `NextActions`.

#### Журнал резервного копирования {: .pageBreakBefore }

Журнал резервного копирования содержит информационные сообщения по результатам резервного копирования экземпляра ПО.

Стандартное имя журнала резервного копирования: `Backup`

Журнал резервного копирования содержит следующие сведения:

- дата события;
- время события;
- тип сообщения;
- ID сеанса;
- имя аккаунта, инициировавшего событие;
- адрес сервера;
- порт сервера;
- IP-адрес клиента;
- текст сообщения.

#### Журнал сценариев {: .pageBreakBefore }

Журнал сценариев содержит сведения о ходе выполнения сценариев.

Стандартное имя журнала сценариев: `Trigger`

Журнал сценариев содержит следующие сведения:

- дата события;
- время события;
- тип сообщения;
- инициатор вызова сценария;
- идентификатор сценария;
- тип события, запустившего сценарий;
- идентификатор шаблона записи;
- идентификатор записи;
- длительность выполнения;
- сведения о действиях, исполненных в ходе сценария:
    - идентификатор действия сценария;
    - тип действия;
    - идентификатор шаблона записи;
    - идентификатор записи;
    - длительность выполнения.

#### Системный журнал {: .pageBreakBefore }

Системный журнал содержит данные о событиях системного уровня в экземпляре ПО.

Стандартное имя системного журнала: `System`

Системный журнал содержит следующие сведения:

- дата события;
- время события;
- тип сообщения;
- ID сеанса;
- имя аккаунта, инициировавшего событие;
- адрес сервера;
- порт сервера;
- IP-адрес клиента;
- текст сообщения.

#### Журналы адаптеров {: #logging_engine_adapter_logs .pageBreakBefore }

Журналы адаптеров содержат данные о событиях подключений и путей передачи данных, относящихся к [адаптерам][adapters] в экземпляре ПО.

Имена журналов адаптеров формируются следующим образом:

- сервис встроенных адаптеров: `adapter_internal`
- сервис пользовательских адаптеров: `adapter_external_system`
- подключение встроенного адаптера: `adapter_internal_<имя_подключения>`
- подключение заказного адаптера: `adapter_external_<имя_подключения>`
- исправность заказного адаптера: `adapter_external_heartbeat`
- подключение заказного адаптера к брокеру сообщений: `adapter_external_kafkaClient`

Журнал адаптера содержит следующие сведения:

- дата события;
- время события;
- тип сообщения;
- описание события;
- контекст события;
- описание исключения (необязательно);
- текст сообщения (необязательно).

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Примеры событий в журналах][log_files_event_examples]_
- _[Пути и содержимое папок экземпляра ПО][paths]_
- _[Адаптеры][adapters]_
- _[Просмотр показателей мониторинга с помощью страницы «Администрирование»][monitoring]_
- _[Просмотр журналов событий с помощью страницы «Администрирование»][logs]_
- _[Просмотр показателей производительности с помощью страницы «Администрирование»][performance]_
- _[Конфигурация журналирования. Настройка, скачивание журналов][logging_configuration]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
