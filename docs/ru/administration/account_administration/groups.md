---
title: Группы
kbTitle: Группы. Создание, настройка, выбор участников, синхронизация с AD, удаление
kbId: 4654
---

# Группы. Администрирование, выбор участников, синхронизация с AD {: #groups}

<div class="admonition question" markdown="block">

## Определения {: .admonition-title #definitions}

- **Группа** — это коллекция аккаунтов и других групп (группы иерархичны). Группы используются для упрощения и контроля выдачи пользователям разрешений и назначения исполнителей пользовательских задач в процессах.
- Группы могут быть созданы вручную либо при синхронизации с сервером каталогов (например, Active Directory). В настройках синхронизации с сервером каталогов можно указать список групп для синхронизации.
- Страница «**Группы**» позволяет просматривать, создавать и настраивать группы аккаунтов, хранящиеся в системе и синхронизируемые с сервером каталогов.

</div>

## Просмотр списка групп и настройка группы {: #groups_view_and_configure .pageBreakBefore }

1. На странице «[**Администрирование**][administration]» в разделе — «**Администрирование аккаунтов**» выберите пункт «**Группы**» <i class="fa-light  fa-users"></i>.
2. Отобразится страница «**Группы**» со списком групп.

    _![Список групп](img/groups_page.png)_

3. Нажмите кнопку «**Создать**» или дважды нажмите строку в списке.
4. Настройте свойства группы.
5. Сохраните группу.

    _![Настройка группы](img/new_group.png)_

## Выбор участников группы {: #groups_select_members .pageBreakBefore }

1. Откройте группу для настройки.
2. Откройте вкладку «**Участники**».
3. Нажимайте названия групп и аккаунтов в левом списке, чтобы включить их в состав группы.
4. Участники группы отображаются в правом списке.

_![Выбор участников группы](img/groups_member_selection.png)_

## Включение группы в состав другой группы {: #groups_include_in_group}

1. Откройте группу для настройки.
2. Откройте вкладку «**Родительские группы**».
3. Нажимайте названия групп в левом списке, чтобы включить группу в их состав в качестве подгруппы.
4. Родительские группы отображаются в правом списке.

_![Выбор родительских групп](img/groups_parent_selection.png)_

## Настройка синхронизации группы с сервером каталогов {: #groups_sync_settings .pageBreakBefore }

По умолчанию аккаунт, исключённый из группы на сервере каталогов (Active Directory, AD), не архивируется и не деактивируется в **{{ productName }}** Это поведение можно настроить на вкладке «**Сервер каталогов**».

1. Откройте группу для настройки.
2. Откройте вкладку «**Сервер каталогов**». Эта вкладка активна только для групп, полученных из AD.
3. Настройте действия с аккаунтами, исключёнными из группы AD:
    - **Архивировать аккаунты, исключенные из группы на сервере каталогов**
        - Если этот флажок установлен, аккаунты, исключённые из группы AD, будут архивированы и не будут отображаться в списке аккаунтов. Если впоследствии аккаунт будет снова включён в группу в AD, он будет разархивирован.
    - **Отключить аккаунты, исключенные из группы на сервере каталогов**
        - Если этот флажок установлен, пользователи не смогут войти в аккаунты, которые исключены из группы в AD. Если впоследствии аккаунт будет снова включён в группу в AD, он будет активирован.

!!! Note "Примечание"

    Если аккаунт находится в нескольких группах и в свойствах одной из них установлен любой из вышеуказанных флажков, а в других группах этот флажок установлен, то при исключении аккаунта из любой из этих групп в AD, он не будет архивирован (деактивирован) в **{{ productName }}**.

_![Настройка синхронизации группы с сервером каталогов](img/groups_active_directory.png)_

## Системный шаблон группы и его атрибуты {: #groups_attributes }

Группы хранятся в системном шаблоне группы, который не отображается в списках шаблонов и не подлежит изменению.

Для обращения к системному шаблону группы в формулах, выражениях на N3 и C#-скриптах используйте системное имя `_AccountGroup`.

У каждой группы предусмотрены следующие системные атрибуты.

| Системное имя      | Описание            | Тип     |
| ------------------ | ------------------- | ------- |
| `groupDescription` | Описание группы     | Текст   |
| `groupName`        | Название группы     | Текст   |
| `groupParents`     | Родительские группы | Группа  |
| `groupUsers`       | Участники группы    | Аккаунт |
| `subGroups`        | Дочерние группы     | Группа  |

## Удаление групп {: #groups_delete .pageBreakBefore }

1. Выберите одну или несколько групп в списке с помощью флажков выбора.
2. Нажмите кнопку «**Удалить**».
3. Отобразится окно «**Удаление**».
4. Подтвердите удаление группы.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Аккаунты. Создание, настройка, замещение, привязка к шаблону аккаунта, назначение лицензий, удаление][accounts]_

</div>

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}