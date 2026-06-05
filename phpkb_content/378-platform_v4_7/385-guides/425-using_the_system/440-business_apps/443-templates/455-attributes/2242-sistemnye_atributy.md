---
title: 'Системные атрибуты'
kbId: 2242
url: 'https://kb.comindware.ru/article.php?id=2242'
updated: '2024-10-14 14:12:51'
---

# Системные атрибуты

## Определения

- Системные атрибуты имеются у каждого объекта, например у приложения, шаблона и даже у самого атрибута.
- Набор системных атрибутов зависит от типа объекта.
- Системные атрибуты не подлежат изменению, удалению и архивированию.
- Системные атрибуты создаются автоматически при создании объекта.

## Перечень системных атрибутов

- **ID** (id) — уникальный идентификатор объекта. Тип: **[Запись](https://kb.comindware.ru/article.php?id=2243)**.
- **Создатель** (\_creator) — аккаунт, создавший объект. Тип: **[Аккаунт](https://kb.comindware.ru/article.php?id=2249)**.
- **Дата создания** (\_creationDate) — дата и время создания объекта. Тип: **[Дата и время](https://kb.comindware.ru/article.php?id=2246)**.
- **Дата изменения** (\_lastWriteDate) — дата и время последнего изменения данных объекта. Тип: **[Дата и время](https://kb.comindware.ru/article.php?id=2246)**.
- **Архивный** (\_isDisabled) — флаг нахождения объекта в архиве (по умолчанию `false`). Тип: **[Логический](https://kb.comindware.ru/article.php?id=2245)**. См. «*[Архивирование и разархивирование атрибута](https://kb.comindware.ru/article.php?id=2252#attributes_archive)*» и «*[Архивирование и разархивирование шаблона](https://kb.comindware.ru/article.php?id=2219#templates_archive_unarchive)*».
- **Цвет** (\_color) — задаёт цвет отображения записи в таблицах, шевронах и диаграммах. Тип: **Цвет**. См. *«[Атрибут «Цвет](https://kb.comindware.ru/article.php?id=2627)»* и  *«[Динамические элементы формы. Цвет](https://kb.comindware.ru/article.php?id=2531#form_dynamic_elements_color)»*.
- **Связанные процессы** (\_processes) — содержит идентификаторы экземпляров процессов, связанных с записью. Тип: **Связанные процессы**. См. *«[Динамические элементы формы. Связанные процессы](https://kb.comindware.ru/article.php?id=2531#form_dynamic_elements_linked_processes)*.

--8<-- "related_topics_heading.md"

**[Атрибуты. Определения, типы, настройка, архивирование, удаление](https://kb.comindware.ru/article.php?id=2252)**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
