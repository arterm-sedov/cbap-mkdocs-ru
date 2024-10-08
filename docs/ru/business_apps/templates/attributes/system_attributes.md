---
title: Системные атрибуты
kbId: 2242
---

# Системные атрибуты {: #attributes_system}

!!! Question "Определения"

    - Системные атрибуты имеются у каждого объекта, например у приложения, шаблона и даже у самого атрибута.
    - Набор системных атрибутов зависит от типа объекта.
    - Системные атрибуты не подлежат изменению, удалению и архивированию.
    - Системные атрибуты создаются автоматически при создании объекта.

## Перечень системных атрибутов

- **ID** (id) — уникальный идентификатор объекта. Тип: **[Запись](attribute_record.md)**.
- **Создатель** (_creator) — аккаунт, создавший объект. Тип: **[Аккаунт](attribute_account.md)**.
- **Дата создания** (_creationDate) — дата и время создания объекта. Тип: **[Дата и время](attribute_date_time.md)**.
- **Дата изменения** (_lastWriteDate) — дата и время последнего изменения данных объекта. Тип: **[Дата и время](attribute_date_time.md)**.
- **Архивный** (_isDisabled) — флаг нахождения объекта в архиве (по умолчанию `false`). Тип: **[Логический](attribute_boolean.md)**. См. «[Архивирование и разархивирование атрибута][архивирование-атрибута]» и «[Архивирование и разархивирование шаблона][архивирование-и-разархивирование-шаблона]».
- **Цвет** (_color) — задаёт цвет отображения записи в таблицах, шевронах и диаграммах. Тип: **Цвет**. См. «[Динамические элементы формы. Цвет][form_dynamic_elements_color]».
- **Связанные процессы** (_processes) — содержит идентификаторы экземпляров процессов, связанных с записью. Тип: **Связанные процессы**. См. «[Динамические элементы формы. Связанные процессы](https://kb.comindware.ru/article.php?id=2531#mcetoc_1hlakq13b1).

--8<-- "related_topics_heading.md"

**[Атрибуты. Определения, типы, настройка, архивирование, удаление][attributes]**

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}
