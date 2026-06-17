---
title: 'Проверка на пустое поле и статус'
kbId: 4986
url: 'https://kb.comindware.ru/article.php?id=4986'
updated: '2026-06-17 14:09:56'
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