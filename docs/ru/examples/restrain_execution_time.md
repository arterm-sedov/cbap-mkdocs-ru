---
title: Ограничение срока выполнения определенным периодом
kbId: 4985
tags:
    - атрибуты
    - пример
    - процессы
hide: tags
---

# Ограничение срока выполнения определенным периодом {: #restrain_execution_time }

Для того чтобы ограничить срок выполнения задачи/проекта определенным периодом (например, месяцем), введите следующее выражение в Правило на форме - Показать ошибку:

```sql
AND(GREATEREQ($Srokvypolneniya,STARTOFMONTH($OtchetnyyperiodRef->Mesyats)),LESSEQ($Srokvypolneniya,ENDOFMONTH($OtchetnyyperiodRef->Mesyats)))
```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| `Srokvypolneniya` | Атрибут типа «**Дата / Время**», который заполняется пользователем на форме. |
| `$OtchetnyyperiodRef->Mesyats` | Атрибут типа «**Дата / Время**» с форматом отображения месяца. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
