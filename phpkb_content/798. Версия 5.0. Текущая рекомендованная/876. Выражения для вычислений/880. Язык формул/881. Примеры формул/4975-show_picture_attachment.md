---
title: 'Отображение картинки  во вложении'
kbId: 4975
url: 'https://kb.comindware.ru/article.php?id=4975'
updated: '2023-08-24 09:08:26'
---

# Отображение картинки во вложении

Для отображения картинки, загруженной во вложении, на форме, создайте атрибут типа Текст и введите следующее выражение:

```
FORMAT("<p><img src='/DocumentContent?id=document.{0}'/></p>",LIST($Fotokarty))
```

**где:**

**Fotokarty**  - системное имя атрибута типа "Документ", куда изначально загружается фото.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
