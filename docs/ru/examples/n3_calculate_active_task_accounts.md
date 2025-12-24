---
title: 'Вычисление пользователей с активными задачами'
kbTitle: 'Аккаунты и задачи. Вычисление пользователей с активными задачами с помощью N3 (с учетом замещений)'
tags:
    - N3
    - Notation 3
    - RDF
    - автоматизация
    - аккаунты
    - выборка
    - вычисление
    - группы
    - замещения
    - задачи
    - пользователи
    - процессы
    - рассылка
    - роли
    - триплеты
    - тройка
    - тройки
    - уведомления
    - уведомления по задачам
    - фильтрация
hide:
    - tags
kbId: 4966
---

# Аккаунты и задачи. Вычисление пользователей с активными задачами с помощью N3  {: #example_n3_calculate_active_task_accounts }

## Введение {: #example_n3_calculate_active_task_accounts_intro }

В **{{ productName }}** можно вычислить аккаунты всех пользователей, у которых на данный момент есть активные задачи, с учетом всех замещений. Это может быть полезно, например, для запуска подпроцесса отправки уведомлений по задачам.

См. также _«[Периодические напоминания об открытых задачах][example_n3_periodic_task_notifications]»_.

## Прикладная задача {: #example_n3_calculate_active_task_accounts_use_case .pageBreakBefore }

Требуется настроить процесс для отправки уведомлений пользователям, у которых есть активные задачи по всем бизнес-процессам, с учетом всех замещений.

Задаче может быть назначен как один исполнитель, так список возможных исполнителей.

Список аккаунтов, у которых есть задачи, необходимо поместить в атрибут типа «**Аккаунт**».

## Исходные данные {: #example_n3_calculate_active_task_accounts_initial_data }

Имеется несколько шаблонов процессов с пользовательскими задачами, которым назначены различные исполнители.

Имеется шаблон записи _«Уведомления о задачах»_.

## Настройка вычисления {: #example_n3_calculate_active_task_accounts_configure }

1. В шаблоне _«Уведомления о задачах»_ создайте атрибут _«Исполнители»_ типа «**Аккаунт**».
2. В свойствах атрибута установите флажки «**Хранить несколько значений**» и «**Вычислять автоматически**».
3. Введите следующее **вычисляемое значение** на языке **N3**:

    ``` turtle
    # Импортируем основные функции для работы 
    # с логикой, контейнерами, аккаунтами и статусами задач
    @prefix cmw: <http://comindware.com/logics#>.
    @prefix container: <http://comindware.com/ontology/container#>.
    @prefix account: <http://comindware.com/ontology/account#>.
    @prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
    {
        # Получаем все задачи.
        ?tasks a cmw:UserTask.
        # Получаем активные задачи.
        ?tasks cmw:taskStatus taskStatus:inProgress.
        # Получаем фактических и возможных исполнителей задач.
        # Проверяем различные варианты назначения задач.
        or{
            # Возвращаем фактического исполнителя,
            # если он назначен через группы и роли.
            ?tasks cmw:assignee ?assigneeRoles.
            ?assigneeRoles role:roleMembers ?groupMembers.
            ?groupMembers account:groupUsers ?value.
        }
        or {

            # Возвращаем фактического исполнителя,
            # если он назначен через роли.
            ?tasks cmw:assignee ?assigneeRoles.
            ?assigneeRoles role:roleMembers ?value.
        }
        or {
            # Возвращаем фактического исполнителя,
            # если он назначен через аккаунт.
            ?tasks cmw:assignee ?value.
        }
        or{
            # Возвращаем список возможных исполнителей,
            # если они назначены через группы и роли.
            ?tasks cmw:possibleAssignee ?possibleRoles.
            ?assigneeRoles role:roleMembers ?groupMembers.
            ?groupMembers account:groupUsers ?value.
        }
        or {

            # Возвращаем список возможных исполнителей,
            # если они назначены через роли.
            ?tasks cmw:possibleAssignee ?possibleRoles.
            ?assigneeRoles role:roleMembers ?value.
        }
        or {
            # Возвращаем список возможных исполнителей,
            # если они назначены через аккаунты.
            ?tasks cmw:possibleAssignee ?value.
        }.
        # Оставляем только активные аккаунты.
        ?value account:active true.
        # Исключаем отключенные аккаунты
        not {?value cmw:isDisabled true.}.
    }
    ```

3. Поместите атрибут _«Исполнители»_ на форму шаблона _«Уведомления о задачах»_.

## Тестирование {: #example_n3_calculate_active_task_accounts_test }

1. Запустите несколько процессов.
2. Создайте или откройте запись в шаблоне _«Уведомления о задачах»_.
3. В поле _«Исполнители»_ должен отображаться список пользователей с активными задачами по всем процессам.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Периодические напоминания об открытых задачах][example_n3_periodic_task_notifications]
- [Настройка процесса для отправки эл.&nbsp;почты][process_email_configure]
- [Уведомления. Типы, назначение, настройка, использование][notification_types]
- [Замещения. Создание, настройка, удаление][substitution]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
