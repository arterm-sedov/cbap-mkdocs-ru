---
title: 'Ограничение срока выполнения определенным периодом'
kbId: 5230
url: 'https://kb.comindware.ru/article.php?id=5230'
updated: '2026-06-20 17:34:21'
---

# Ограничение срока выполнения определенным периодом

Для того чтобы ограничить срок выполнения задачи/проекта определенным периодом (например, месяцем), введите следующее выражение в Правило на форме - Показать ошибку:

```
AND(GREATEREQ($Srokvypolneniya,STARTOFMONTH($OtchetnyyperiodRef->Mesyats)),LESSEQ($Srokvypolneniya,ENDOFMONTH($OtchetnyyperiodRef->Mesyats)))
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Srokvypolneniya` | Атрибут типа «**Дата / Время**», который заполняется пользователем на форме. |
| `$OtchetnyyperiodRef->Mesyats` | Атрибут типа «**Дата / Время**» с форматом отображения месяца. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
