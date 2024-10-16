---
title: Диаграммы
kbId: 2211
---

# Диаграммы. Определения, создание, просмотр, удаление  {: #diagrams}

!!! Определения

    - В **{{ productName }}** предусмотрены диаграммы процессов, бизнес-способностей, моделей данных и классов.
    - [**Диаграмма процесса**][process_diagram] составляется по стандарту BPMN 2.0 и позволяет визуализировать и исполнять бизнес-процесс с назначением задач исполнителям, выполнением сценариев, отправкой внутренних и внешних сообщений, просмотром журнала действий.
    - **Диаграмма бизнес-способностей** позволяет представить связи и взаимодействие объектов процессной архитектуры: бизнес-процессов и ресурсов.
    - **Диаграмма модели данных** показывает и позволяет задавать связи шаблонов записей и шаблонов аккаунтов, а также позволяет создавать новые [шаблоны][templates].
    - **Диаграмма классов** показывает и позволяет редактировать и создавать новые шаблоны.

## Просмотр списка диаграмм в приложении и настройка диаграммы {: #diagram_list }

Для каждого приложения предусмотрены отдельные диаграммы процессов, бизнес-способностей, моделей данных и классов.

1. На странице [«**Администрирование**»][administration] в разделе «**Архитектура**» выберите пункт «**Приложения**» <i class="fa-light  fa-project-diagram"></i>.
2. Отобразится список приложений.
3. Дважды нажмите строку приложения в списке.
4. В разделе **«[Администрирование][apps]»** приложения выберите пункт «**Диаграммы**» <i class="fa-light  fa-project-diagram ">‌</i>.
5. Отобразится список диаграмм для данного приложения.
6. [Создайте диаграмму][diagram_creation] или дважды нажмите строку диаграммы в списке.
7. Отредактируйте диаграмму.

## Просмотр списка диаграмм из всех приложений

1. На странице [«**Администрирование**»][administration] в разделе «**Архитектура**» выберите пункт «**Диаграммы**» <i class="fa-light  fa-project-diagram ">‌</i>‌.
2. Отобразится общий список всех диаграмм из всех [приложений][apps].

--8<-- "diagram_list_elements.md"

_![Список диаграмм приложения](diagram_list.png)_

## Создание диаграммы {: #diagram_creation}

Создать вручную можно диаграмму **бизнес-способностей, классов** или **модели данных**.

[**Диаграмма процесса**][process_diagram] создается вместе с [**шаблоном процесса**][process_templates].

1. Откройте [список диаграмм][diagram_list].
2. Нажмите кнопку «**Создать**».
3. Отобразится окно «**Новая диаграмма**».
4. Укажите **название**, **системное имя** и **тип диаграммы**.

    - При создании диаграммы в общем списке диаграмм выберите **приложение**.

5. Нажмите кнопку «**Сохранить**».
6. Созданная диаграмма отобразится в списке.

_![Окно создания новой диаграммы с выбором приложения](diagram_creation_with_app_selection.png)_

## Удаление диаграмм

1. Откройте [список диаграмм][diagram_list].
2. Установите для подлежащих удалению диаграмм флажки выбора.
3. Нажмите кнопку «**Удалить**» над списком диаграмм.
4. Подтвердите удаление диаграмм.

--8<-- "related_topics_heading.md"

**[Управление версиями диаграммы процесса][process_diagram_version_control]**

{%
include-markdown "../../.snippets/hyperlinks_mkdocs_to_kb_map.md"
%}
