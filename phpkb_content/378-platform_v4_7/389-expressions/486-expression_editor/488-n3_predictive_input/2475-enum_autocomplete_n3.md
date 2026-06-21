---
title: 'Ввод значений из атрибута типа «Список значений»'
kbId: 2475
url: 'https://kb.comindware.ru/article.php?id=2475'
updated: '2023-09-22 13:05:23'
---

# Ввод значений из атрибута типа «Список значений»

## Инструкции

Если предикат определяет [атрибут типа «Список значений»](https://kb.comindware.ru/article.php?id=2244), предиктивный ввод подсказывает значения из этого списка.

1. Введите предикат, например `cmw:taskStatus`, который определяет системный [атрибут типа «Список значений»](https://kb.comindware.ru/article.php?id=2244), содержащий статус задачи.
2. В позиции через пробел после предиката нажмите клавиши `Ctrl` `Пробел`.
3. В отобразившемся списке значений нажмите требуемое значение, например `taskStatus:inProgress` (активная задача), чтобы вставить его в выражение.

_![Список значений атрибута taskStatus](https://kb.comindware.ru/assets/n3_editor_enum_autocomplete.png)_

**Пример: выражение, возвращающее список задач со статусом «Выполняется»**

```
@prefix cmw: <http://comindware.com/logics#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
{
  ?value cmw:taskStatus taskStatus:inProgress.
}
```

--8<-- "related_topics_heading.md"

**[Редактор выражений](https://kb.comindware.ru/article.php?id=2463)**

**[Примеры использования языка N3](https://kb.comindware.ru/category.php?id=408)**

**[Атрибут типа «Список значений»](https://kb.comindware.ru/article.php?id=2244)**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
