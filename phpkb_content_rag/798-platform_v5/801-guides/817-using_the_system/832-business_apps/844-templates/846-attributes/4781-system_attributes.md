---
title: 'Системные атрибуты'
kbId: 4781
url: 'https://kb.comindware.ru/article.php?id=4781'
updated: '2025-05-30 18:01:24'
---

# Системные атрибуты

## Определения

- Системные атрибуты имеются у каждого объекта, например у приложения, шаблона и даже у самого атрибута.
- Набор системных атрибутов зависит от типа объекта.
- Системные атрибуты не подлежат изменению, удалению и архивированию.
- Системные атрибуты создаются автоматически при создании объекта.

## Перечень системных атрибутов

- **ID** (id) — уникальный идентификатор объекта. Тип: **[Запись](https://kb.comindware.ru/article.php?id=4780)**.
- **Создатель** (\_creator) — аккаунт, создавший объект. Тип: **[Аккаунт](https://kb.comindware.ru/article.php?id=4774)**.
- **Дата создания** (\_creationDate) — дата и время создания объекта. Тип: **[Дата и время](https://kb.comindware.ru/article.php?id=4777)**.
- **Дата изменения** (\_lastWriteDate) — дата и время последнего изменения данных объекта. Тип: **[Дата и время](https://kb.comindware.ru/article.php?id=4777)**.
- **Архивный** (\_isDisabled) — флаг нахождения объекта в архиве (по умолчанию `false`). Тип: **[Логический](https://kb.comindware.ru/article.php?id=4778)**. См. «*[Архивирование и разархивирование атрибута](https://kb.comindware.ru/article.php?id=4772#attributes_archive)*» и «*[Архивирование и разархивирование шаблона](https://kb.comindware.ru/article.php?id=4709#templates_archive_unarchive)*».
- **Цвет** (\_color) — задаёт цвет отображения записи в таблицах, шевронах и диаграммах. Тип: **Цвет**. См. *«[Атрибут «Цвет](https://kb.comindware.ru/article.php?id=4763)»* и  *«[Динамические элементы формы. Цвет](https://kb.comindware.ru/article.php?id=4785#form_dynamic_elements_color)»*.
- **Связанные процессы** (\_processes) — содержит идентификаторы экземпляров процессов, связанных с записью. Тип: **Связанные процессы**. См. *«[Динамические элементы формы. Связанные процессы](https://kb.comindware.ru/article.php?id=4785#form_dynamic_elements_linked_processes)*.

## Связанные статьи

- [Атрибуты. Определения, типы, настройка, архивирование, удаление](https://kb.comindware.ru/article.php?id=4772)
- [Системные атрибуты шаблона аккаунта](https://kb.comindware.ru/article.php?id=4757#account_template_attribute_system_names)