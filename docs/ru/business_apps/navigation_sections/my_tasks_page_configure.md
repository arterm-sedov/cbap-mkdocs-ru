---
title: Страница «Мои задачи». Определения и настройка
tags:
  - мои задачи
  - вкладки на странице «Мои задачи»
  - активные задачи
  - завершенные задачи
  - разделы навигации
kbId: 2411
hide:
  - tags
---

# Страница «Мои задачи». Определения и настройка {: #my_tasks_page_configure}

<div class="admonition question" markdown="block">
## Определения {: .admonition-title #definitions}

* По умолчанию в состав страницы «**Мои задачи**» включены следующие таблицы:
    - **Активные** — задачи, которые требуется обработать;
    - **Завершённые** — обработанные задачи только для просмотра.
* На страницу «**Мои задачи**» можно добавить вкладки с таблицами из шаблонов.
* Страница «**Мои задачи**» отображается, если раздел навигации, в который она включена, доступен аккаунту:
    - в [панели навигации][navigation_sections_setup] отображается пункт «**Мои задачи**»;
    - страница «**Мои задачи**» отображается в качестве начальной страницы при входе в систему пользователя с данным аккаунтом;
    - если аккаунту доступен **[рабочий стол][desktop_setup]**, то при входе в систему он отображается вместо страницы «**Мои задачи**».

</div>

## Добавление страницы «Мои задачи» в раздел навигации

1. Откройте [конструктор раздела навигации][navigation_sections_setup], в состав которого требуется включить страницу «**Мои задачи**».
2. Перетащите элемент «**Мои задачи**» на макет раздела навигации.
3. Нажмите кнопку «**Сохранить**».
4. Обновите страницу в браузере.
5. Пункт «**Мои задачи**» отобразится в панели навигации, если данный раздел навигации доступен аккаунту текущего пользователя.

## Добавление таблиц на страницу «Мои задачи»

1. Раскройте шаблон в панели элементов.
2. Раскройте группу «**Таблицы**» внутри шаблона.
3. Перетащите требуемые таблицы в группу «**Мои задачи**».
4. При необходимости измените **отображаемое название** вкладки с таблицей с помощью панели «**Свойства элемента**». Таблица будет отображаться под этим названием на странице «**Мои задачи**».
5. Нажмите кнопку «**Сохранить**».

    _![Добавление таблицы на страницу «Мои задачи»](my_tasks_add_table.png)_

6. На странице будут отображаться настроенные вкладки с таблицами.

    _![Пункт «Мои задачи» на панели навигации и страница «Мои задачи» с настроенными вкладками](my_tasks_page_with_custom_tabs.png)_

!!! note "Примечание"

    Если на страницу «**Мои задачи**» добавлены таблицы в нескольких разделах навигации, они будут отображаться для пользователей, которым доступны соответствующие разделы навигации.

## Удаление вкладки со страницы «Мои задачи»

1. Откройте [конструктор раздела навигации][navigation_sections_setup], в состав которого входит страница «**Мои задачи**».
2. В макете раздела навигации раскройте группу «**Мои задачи**».
3. Перетащите таблицу за пределы макета раздела навигации.
4. При необходимости подтвердите удаление элемента из раздела навигации.

--8<-- "related_topics_heading.md"

**[Панель и разделы навигации. Определения, настройка, удаление][navigation_sections_setup]**

**[Настройка рабочего стола][desktop_setup]**

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}