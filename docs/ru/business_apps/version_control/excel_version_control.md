---
title: Экспорт и импорт версий приложения с помощью Excel
kbId:
tags:
  - трансфер
  - импорт приложения
  - экспорт приложения
  - трансфер через Excel
  - управление версиями через Excel
hide: tags
---

# Экспорт и импорт версий приложения с помощью Excel {: #excel_version_control}

--8<-- "experimental_feature.md"

## Введение

В **{{ productName }}** предусмотрены импорт и экспорт версий приложения посредством файла Excel.

!!! note "Примечание"

    В файл Excel сохраняется только шаблоны и конфигурация приложения, записи из шаблонов не сохраняются.

## Переход к управлению версиями с помощью Excel

1. На странице «**[Администрирование][apps]**» приложения выберите пункт «**Управление версиями**» <i class="fa-light fa-code-branch"></i>.
2. Нажмите заголовок страницы «**Управление версиями через Git**» и в раскрывающемся меню выберите пункт «**Управление версиями через Excel**».

    _![Переход к управлению версиями через Excel](img/excel_version_control_switch_to_excel.png)_

3. Отобразится страница «**Управление версиями**» с двумя вкладками:

    - **Экспорт** — экспорт приложения в формате Excel.
    - **Импорт** — импорт версии приложения из документа в формате Excel.

## Экспорт версии приложения

!!! warning "Внимание!"

    Перед экспортом приложения подготовьте его, как указано в параграфе _«[Подготовка приложения к экспорту][version_control_app_prepare]»_.

1. Перейдите на вкладку «**Экспорт**».
2. Нажмите кнопку «**Экспортировать**».
3. Отобразится окно «**Конфигурация экспорта**».
4. На шаге «**Параметры экспорта**» установите флажки для элементов приложения, которые требуется экспортировать:

    - Шаблоны записей
    - Шаблоны ролей
    - Шаблоны аккаунтов
    - Шаблоны оргединиц
    - Роли
    - Разделы навигации
    - Страницы

5. Нажмите кнопку «**Далее**».
6. Отобразится шаг «**Проверка**».
7. Нажмите кнопку «**Экспортировать**».
8. Если при экспорте не будет выявлено ошибок, браузер скачает файл с системным именем приложения и расширением `.XLSX` вида: `businessApplicationSystemName.xlsx`.

    - Импортируйте этот файл в целевое приложение.

9. Если будут обнаружены ошибки, устраните их и повторите экспорт.

!!! question "Содержимое файла Excel с экспортированным приложением"

    Файл Excel с экспортированным приложением содержит несколько листов с данными различных сущностей, например:
    
    - **Templates** — шаблоны всех типов.
    - **Attributes** — атрибуты всех типов кроме списков значений.
    - **AttributesVariants** — атрибуты типа «**Список значений**».
    - **UserCommands** — кнопки.
        - **UserCommandsRelatedActions** — операции кнопок.
        - **ConfirmationModelConfigurations** — диалоговые окна кнопок.
        - **UserCommandsScriptRules** — C#-скрипты кнопок.
        - **UserCommandsScriptRuleActions**
        - **ScriptRuleDefinitions**
        - **ScriptRulePropertyMaps**
        - **ScriptRulePropertyMapKeys**
    - **Forms** — формы.
        - **FormComponents** — элементы форм.
        - **FormCompsLabels** — подписи элементов форм.
        - **FormCompsPredefinedValueLabels**
        - **FormCompsUserCommandLabels** — подписи кнопок на формах.
        - **FormComponentColorMaps** — цвета кнопок на формах.
        - **FormComponentConnections**
    - **FormRules** — правила для форм.
    - **FormRuleRuleActions** — действия правил для форм.
    - **Toolbars** — области кнопок.
        - **ToolbarItems** — элементы областей кнопок.
        - ToolbarItemCollectionActions
    - **Datasets** — таблицы.
        - **DatasetPagings** — параметры разбиения таблиц на страницы.
        - **DatasetSortings** — параметры сортировки данных в таблицах.
        - **DatasetGroupings** — параметры группировки данных в таблицах.
        - **DatasetGroupingFields** — поля для группировки данных в таблицах.
        - **DatasetGroupingFieldLayouts** — параметры отображения групп в таблицах
        - **DatasetColumns** — столбцы таблиц.
        - **DatasetColumnLayouts** — параметры отображения столбцов в таблицах.
    - **DocumentExportTemplates** — шаблоны экспорта.
        - **ExportSourceTemplates** — файлы шаблонов экспорта.
        - **OutputFileNameTemplates** — имена целевых файлов экспорта.
    - **Roles** — роли.
        - **ResourcePrivilegeDescriptors** — разрешения ролей.
    - **Workspaces** — разделы навигации.
        - **WorkspaceNavigationItems** — пункты разделов навигации.
    - **Pages** — страницы в разделах навигации.
        - **PageComponents** — компоненты страниц.
        - **Steps** — виджеты «**Шаги**».
        - **Links** — виджеты «**Баннеры**».
    - **ReferencesToConnection** — ссылки на подключения.

    В файле Excel c экспортированным приложением используются следующие специальные термины:

    - **Alias** — системное имя.
    - **Disabled** — архивный объект.
    - **Global alias** — глобальный псевдоним объекта вида: 
        ```
        Attribute@templateSystemName.attributeSystemName
        ```
    - **Instance** — экземпляр **{{ productName }}**.
    - **Property** — атрибут.
    - **Record template** — связанный шаблон.
    - **Solution** — приложение.
    - **Script** — С#—скрипт.
    - **Toolbar** — область кнопок.
    - **User command** — кнопка.

## Импорт версии приложения

{%
include-markdown "./index.md"
start="<!--version-control-warning-start-->"
end="<!--version-control-warning-end-->"
%}

1. Перейдите на вкладку «**Импорт**».
2. Нажмите кнопку «**Импортировать**».
3. Отобразится окно «**Конфигурация импорта**».
4. На шаге «**Импортируемый файл**» выберите файл конфигурации приложения с расширением `.xslx` и нажмите кнопку «**Далее**».
5. На вкладке «**Параметры импорта**» установите флажки для элементов приложения, которые требуется импортировать:

    - Шаблоны записей
    - Шаблоны ролей
    - Шаблоны аккаунтов
    - шаблоны оргединиц
    - Роли
    - Разделы навигации
    - Страницы

6. Нажмите кнопку «**Далее**».

7. На вкладке «**Проверка**» нажмите кнопку «**Импортировать**».
8. При успешном импорте отобразится надпись «**Импорт выполнен**».
9. Если будут обнаружены ошибки, устраните проблемы и конфликты в исходном и целевом приложениях, экспортируйте исходное приложение заново, загрузите исправленный файл Excel и повторите импорт.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Управление версиями приложения][version_control]_
- _[Ручное управление версиями][version_control_manual]_
- _[Управление версиями через Git][version_control_git]_

</div>

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}