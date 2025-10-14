---
title: Фильтр списка по дате, равной сегодняшней
kbId: 4942
---

# Фильтр списка по дате, равной сегодняшней

Для того, чтобы настроить фильтр отображения записей в списке, где какая-либо дата равна сегодняшней (например, для списка сегодняшних заявок) с учетом часового пояса (в данном примере - московского), введите следующее выражение:

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

**где:**

**Zayavki** – системное имя текущего Шаблона записи;

**Data** – системное имя атрибута типа "Дата / Время", которое будет сравниваться с текущим днём;

**Etc/GMT** – определение смещения часового пояса;

**Europe/Moscow** – определение конкретного часового пояса.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
