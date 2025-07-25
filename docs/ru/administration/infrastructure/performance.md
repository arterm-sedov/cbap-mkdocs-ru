---
title: Производительность
kbId: 4669
---

## Введение {: #performance}

В **{{ productName }}** предусмотрена возможность просмотра и сброса показателей производительности процессов, скриптов, системных служб, сеансов получения и отправки сообщений, а также сеансов вычисления выражений.

!!! Note "Примечание"

    Сведения на данной странице отображаются, только если установлен флажок «**Включить мониторинг производительности**» в разделе «**Глобальная конфигурация**».

## Просмотр показателей производительности

1. В разделе «[**Администрирование**» — «**Инфраструктура**][administration]» выберите пункт «**Производительность**» <i class=" fal  fa-tachometer ">‌</i>:
2. Отобразится страница «**Производительность**»:

    _![Страница «Производительность»](performance_page.png)_

3. Выберите требуемый подраздел, нажав пункт «**Процессы**».

    _![Выбор показателей производительности для просмотра](performance_view_selection.png)_

4. Отобразятся соответствующие показатели производительности.

## Сброс показателей

Чтобы обнулить показатели производительности и начать их отсчет заново, нажмите кнопку «**Сбросить счетчик**».

## Поиск показателей

--8<-- "list_search.md"

## Показатели производительности {: .pageBreakBefore }

### Процессы

_![Показатели производительности процессов](performance_page.png)_

- **ID процесса** — уникальный идентификатор шаблона бизнес-процесса.
- **Активно** — количество активных в текущий момент экземпляров бизнес-процесса.
- **Неактивно** — суммарное количество завершенных и отмененных экземпляров бизнес-процесса.
- **Завершено** — количество экземпляров бизнес-процесса, выполнение которых завершилось.
- **Отменено** — количество экземпляров бизнес-процесса, выполнение которых было отменено.
- **Длительность (мс)** — суммарная продолжительность выполнения экземпляров бизнес-процессов.

### Скрипты {: .pageBreakBefore }

_![Показатели производительности скриптов](performance_scripts.png)_

- **Точка входа** — имя функции точки входа DLL-библиотеки скрипта C#;
- **Библиотека** — путь к скомпилированной DLL-библиотеке.
- **Всего** — количество запущенных экземпляров скрипта.
- **Успешно** — количество успешно выполненных экземпляров скрипта.
- **С ошибками** — количество экземпляров скрипта, выполнение которых завершилось с ошибкой.
- **Средняя длительность (мс)** — среднее время выполнения скрипта.

### Системные службы {: .pageBreakBefore }

_![Показатели производительности системных служб](performance_system_services.png)_

- **Название** — наименование системной службы.
- **Запущено** — количество запущенных экземпляров службы.
- **Активно** — количество активных экземпляров службы.
- **Выполнено** — количество завершивших работу экземпляров службы.
- **С ошибками** — количество экземпляров службы, работа которых завершилась с ошибкой.
- **Длительность (мс)** — суммарная продолжительность работы экземпляров службы.

### Сообщения {: .pageBreakBefore }

_![Показатели производительности сеансов получения и отправки сообщений](performance_messages.png)_

- **Всего** — суммарное количество полученных и отправленных сообщений.
- **Успешно** — суммарное количество сообщений, переданных без ошибок.
- **С ошибками** — суммарное количество сообщений, при передаче которых возникли ошибки.

### Выражения {: .pageBreakBefore }

_![Показатели производительности сеансов вычисления выражений](performance_expressions.png)_

- **ID выражения** — уникальный идентификатор выражения.
- **ID контейнера** — уникальный идентификатор места вызова выражения.
- **Всего** — суммарное количество сеансов вычисления выражения.
- **Успешно** — количество успешно выполненных сеансов вычисления.
- **С ошибками** — количество сеансов вычисления выражения, завершившихся с ошибками.
- **Средняя длительность (мс)** — среднее время вычисления выражения.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Мониторинг][monitoring]_
- _[Журналы событий][logs]_
- _[Подсистема журналирования][logging_engine]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}