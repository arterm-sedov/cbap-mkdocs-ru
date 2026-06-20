---
title: 'Проверка на пустое поле и статус'
kbId: 5232
url: 'https://kb.comindware.ru/article.php?id=5232'
updated: '2026-06-20 17:34:07'
---

# Проверка на пустое поле и статус

Для того чтобы установить правило с условием на пустое поле и наличием определённого статуса, введите следующее выражение:

```
AND(EMPTY($Fakticheskietrudozatraty), ($StatusRef->Title == "Ready for build" || $StatusRef->Title == "Acceptance" || $StatusRef->Title == "Closed" || $StatusRef->Title == "In Review"))
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Fakticheskietrudozatraty` | Системное имя атрибута любого типа. |
| "Ready for build","Acceptance", "Closed", "In Review" | Статусы. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
