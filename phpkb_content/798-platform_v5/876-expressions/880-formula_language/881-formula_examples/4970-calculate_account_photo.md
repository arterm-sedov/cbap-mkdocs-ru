---
title: 'Вычисление фото из профиля пользователя'
kbId: 4970
url: 'https://kb.comindware.ru/article.php?id=4970'
updated: '2026-06-20 20:26:25'
---

# Вычисление фото из профиля пользователя

Для того чтобы получить фото из профиля определенного пользователя (например, для составления карточки сотрудника), введите следующее выражение:

```
FORMAT("<img height='150' src = 'https://instance.net/api/GetProfilePhoto?id={0}&size=large'> </img>",LIST($Polzovatel))
```

**Здесь**

| Значение | Описание |
| --- | --- |
| `https://instance.net` | Ссылка на текущий инстанс. |
| `Polzovatel` | Системное имя атрибута типа «**Пользователь**». |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
