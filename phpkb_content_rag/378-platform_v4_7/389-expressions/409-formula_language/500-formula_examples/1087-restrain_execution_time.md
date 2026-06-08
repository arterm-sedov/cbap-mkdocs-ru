---
title: 'Ограничение срока выполнения определенным периодом'
kbId: 1087
url: 'https://kb.comindware.ru/article.php?id=1087'
updated: '2023-08-24 09:08:15'
---

# Ограничение срока выполнения определенным периодом

Для того, чтобы ограничить срок выполнения задачи/проекта определенным периодом (например, месяцем), введите следующее выражение в Правило на форме - Показать ошибку:

```
AND(GREATEREQ($Srokvypolneniya,STARTOFMONTH($OtchetnyyperiodRef->Mesyats)),LESSEQ($Srokvypolneniya,ENDOFMONTH($OtchetnyyperiodRef->Mesyats)))
```

**где:**

**Srokvypolneniya** - атрибут типа Дата / Время, который заполняется пользователем на форме;

**OtchetnyyperiodRef->Mesyats** - атрибут типа Дата / Время (формат - месяц).