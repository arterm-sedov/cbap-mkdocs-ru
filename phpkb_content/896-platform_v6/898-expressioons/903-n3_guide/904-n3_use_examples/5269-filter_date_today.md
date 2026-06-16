---
title: 'Фильтр списка по дате, равной сегодняшней'
kbId: 5269
url: 'https://kb.comindware.ru/article.php?id=5269'
updated: '2026-06-16 19:16:47'
---

# Фильтр списка по дате, равной сегодняшней

Для того чтобы настроить фильтр отображения записей в списке, где какая-либо дата равна сегодняшней (например, для списка сегодняшних заявок) с учетом часового пояса (в данном примере - московского), введите следующее выражение:

```
@prefix object: <http://comindware.com/ontology/object#>.
@prefix session: <http://comindware.com/ontology/session#>.
@prefix cmwtime: <http://comindware.com/logics/time#>.
{
  ("Zayavki" "Data") object:findProperty ?DateProperty.
  session:context session:requestTime ?nowUTC.

  (?nowUTC "Etc/GMT" "Europe/Moscow") cmwtime:fromTzToTz ?nowMoscow.
  ?nowMoscow cmwtime:startOfDay ?startOfToday.

  ?result ?DateProperty ?Dates.

  (?Dates "Etc/GMT" "Europe/Moscow") cmwtime:fromTzToTz ?Moscow.
  ?Moscow cmwtime:startOfDay ?startOfToday.

  ?result -> ?item.
}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Zayavki` | Системное имя текущего Шаблона записи. |
| `Data` | Системное имя атрибута типа «**Дата / Время**», которое будет сравниваться с текущим днём. |
| `Etc/GMT` | Определение смещения часового пояса. |
| `Europe/Moscow` | Определение конкретного часового пояса. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
