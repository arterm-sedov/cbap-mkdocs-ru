---
title: 'Вычисление исполнителя активной задачи'
kbTitle: 'Вычисление исполнителя текущей активной задачи'
tags:
    - N3
    - Notation 3
    - RDF
    - аккаунты
    - вычисление
    - задачи
    - исполнитель
    - процессы
    - триплеты
    - тройка
    - тройки
hide:
    - tags
kbId: 4950
---

# Вычисление исполнителя активной задачи с помощью N3 {: #n3_calculate_active_task_assignee }

## Введение {: #n3_calculate_active_task_assignee_intro }

В **{{ productName }}** можно вычислить исполнителя активной задачи по записи, связанной с экземпляром бизнес-процесса. Это может быть полезно для отображения информации об ответственном за задачу или в иных вычислениях.

## Прикладная задача {: #n3_calculate_active_task_assignee_use_case }

Имеется бизнес-процесс с пользовательскими задачами.

Задаче может быть назначен как один исполнитель, так список возможных исполнителей.

С бизнес-процессом связана запись.

Для этой записи требуется:

- получить список исполнителей активных задач и поместить его в атрибут типа «**Аккаунт**»;
- определить, имеются ли задачи у текущего пользователя, и записать соответственно значение `True` или `False` в **логический** атрибут.

## Исходные данные {: #n3_calculate_active_task_assignee_initial_data }

Имеется шаблон процесса _«Оформление заявок»_, связанный с шаблоном записи _«Заявки»_.

В шаблоне _«Оформление заявок»_ имеются пользовательские задачи, которым назначены различные исполнители.

## Настройка вычислений {: #n3_calculate_active_task_assignee_configure }

1. На диаграмме процесса _«Оформление заявок»_ назначьте себя исполнителем любой из задач.
2. В шаблоне _«Заявки»_ создайте атрибут со следующими свойствами:

    - **Название:** _Ответственные_
    - **Тип данных: аккаунт**
    - **Хранить несколько значений**: флажок установлен
    - **Вычислять автоматически**: флажок установлен
    - **Вычисляемое значение: N3**

    ``` turtle
    # Импортируем функции для работы 
    # с логикой, задачами и статусами задач.
    @prefix cmw: <http://comindware.com/logics#>.
    @prefix task: <http://comindware.com/ontology/task#>.
    @prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
    @prefix account: <http://comindware.com/ontology/account#>.
    @prefix role: <http://comindware.com/ontology/role#>.
    {
        # Получаем задачи, связанные с текущей записью.
        ?tasks task:objectId ?item.
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
        # Исключаем отключенные аккаунты.
        not {?value cmw:isDisabled true.}.
    }
    ```

3. Создайте атрибут со следующими свойствами:

    - **Название:** _У вас имеются задачи_
    - **Тип данных: логический**
    - **Вычислять автоматически**: флажок установлен
    - **Вычисляемое значение: N3**

    ``` turtle
    # Импортируем функции для работы 
    # с логикой, задачами и статусами задач.
    @prefix cmw: <http://comindware.com/logics#>.
    @prefix task: <http://comindware.com/ontology/task#>.
    @prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
    @prefix account: <http://comindware.com/ontology/account#>.
    @prefix role: <http://comindware.com/ontology/role#>.
    {
        # Получаем аккаунт текущего пользователя из контекста безопасности.
        cmw:securityContext cmw:currentUser ?currentUser.
        # Получаем роли текущего пользователя.
        ?roles role:roleMembers ?currentUser.
        # Получаем группы, в которые входит пользователь.
        ?userGroups account:groupUsers ?currentUser.
        ?groupRoles role:roleMembers ?userGroups.
        # Получаем задачи, связанные с текущей записью.
        ?tasks task:objectId ?item.
        # Получаем активные задачи.
        ?tasks cmw:taskStatus taskStatus:inProgress.
        # Проверяем различные варианты назначения задачи.
        once {
            or {
                # Проверяем, назначена ли задача на текущего пользователя.
                ?tasks cmw:assignee ?currentUser.
            }
            or {
                # Проверяем, является ли пользователь возможным исполнителем.
                ?tasks cmw:possibleAssignee ?currentUser.
            }
            or {
                # Проверяем, назначена ли задача на роль пользователя.
                ?tasks cmw:assignee ?roles.
            }
            or {
                # Проверяем, является ли роль пользователя возможным исполнителем.
                ?tasks cmw:possibleAssignee ?roles.
            }
            or {
                # Проверяем, назначена ли задача на группу пользователя.
                ?tasks cmw:assignee ?groupRoles.
            }
            or {
                # Проверяем, является ли группа пользователя возможным исполнителем.
                ?tasks cmw:possibleAssignee ?groupRoles.
            }.
        }.
        # Возвращаем True, если у текущего пользователя есть задачи.
        ?true -> ?value
    }
    ```

4. Поместите атрибуты _«Ответственные»_ и _«У вас имеются задачи»_ на форму шаблона _«Заявки»_.
5. Установите для поля _«У вас имеются задачи»_ на форме отображение в качестве **переключателя**.

## Тестирование {: #n3_calculate_active_task_assignee_test }

1. Запустите процесс _«Оформление заявок»_.
2. Откройте _заявку_, созданную при запуске процесса.
3. В поле _«Ответственные»_ должен отображаться список исполнителей текущей задачи по _заявке_.
4. В поле _«У вас имеются задачи»_ должно отобразиться значение «**Да**»

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Вычисление пользователей с активными задачами][example_n3_calculate_active_task_accounts]
- [Периодические напоминания об открытых задачах][example_n3_periodic_task_notifications]
- [Уведомления. Типы, назначение, настройка, использование][notification_types]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
