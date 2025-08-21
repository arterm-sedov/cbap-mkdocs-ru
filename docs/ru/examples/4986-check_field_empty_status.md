---
title: Проверка на пустое поле и статус
kbId: 4986
---

# Проверка на пустое поле и статус

Для того, чтобы установить правило с условием на пустое поле и наличием определённого статуса, введите следующее выражение:

```
AND(EMPTY($Fakticheskietrudozatraty), ($StatusRef->Title == "Ready for build" || $StatusRef->Title == "Acceptance" || $StatusRef->Title == "Closed" || $StatusRef->Title == "In Review"))
```

**где:**

**Fakticheskietrudozatraty** - системное имя атрибута любого типа;

**"Ready for build","Acceptance", "Closed", "In Review"**- статусы.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
