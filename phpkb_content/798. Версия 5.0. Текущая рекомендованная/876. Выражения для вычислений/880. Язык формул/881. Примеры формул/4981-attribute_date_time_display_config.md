---
title: Настройка отображения атрибута типа «Дата / Время»
kbId: 4981
---

# Настройка отображения атрибута типа «Дата / Время»

Для того чтобы настроить отображение даты определенным образом (в данном примере это ««1» марта 2021г.»), введите следующее выражение:

```
FORMAT("«{0}» {1} {2}г.", LIST( DAY($date), IF ( (MONTH($date) == 1), "января", IF ( (MONTH($date) == 2), "февраля", IF ( (MONTH($date) == 3), "марта", IF ( (MONTH($date) == 4), "апреля", IF ( (MONTH($date) == 5), "мая", IF ( (MONTH($date) == 6), "июня", IF ( (MONTH($date) == 7), "июля", IF ( (MONTH($date) == 8), "августа", IF ( (MONTH($date) == 9), "сентября", IF ( (MONTH($date) == 10), "октября", IF ( (MONTH($date) == 11), "ноября", "декабря"))))))))))), YEAR($date)))
```

**где:**

**date** – атрибут типа «Дата / Время», который нужно преобразовать в определенный формат.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
