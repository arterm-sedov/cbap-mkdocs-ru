---
title: Проверка на пустое поле и статус
kbId: 4986
tags:
    - атрибуты
    - пример
    - формулы
hide: tags
---

# Проверка на пустое поле и статус {: #check_field_empty_status }

Для того чтобы установить правило с условием на пустое поле и наличием определённого статуса, введите следующее выражение:

```sql
AND(EMPTY($Fakticheskietrudozatraty), ($StatusRef->Title == "Ready for build" || $StatusRef->Title == "Acceptance" || $StatusRef->Title == "Closed" || $StatusRef->Title == "In Review"))
```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| `Fakticheskietrudozatraty` | Системное имя атрибута любого типа. |
| "Ready for build","Acceptance", "Closed", "In Review" | Статусы. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
