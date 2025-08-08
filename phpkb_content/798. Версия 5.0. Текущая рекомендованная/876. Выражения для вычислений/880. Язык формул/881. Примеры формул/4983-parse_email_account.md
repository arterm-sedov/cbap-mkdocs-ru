---
title: Парсинг Email до знака @
kbId: 4983
---

# Парсинг Email до знака @

Для того чтобы из электронной почты вывести все символы до знака @ (например, для генерации логина для личного кабинета), введите следующее выражение:

```
SUBSTRING($Email,0,INDEXOF($Email,"@"))
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
