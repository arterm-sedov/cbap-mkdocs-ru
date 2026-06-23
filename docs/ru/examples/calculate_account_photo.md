---
title: Вычисление фото из профиля пользователя
kbId: 5238
tags:
    - атрибуты
    - пример
    - формулы
hide: tags
---

# Вычисление фото из профиля пользователя {: #calculate_account_photo }

Для того чтобы получить фото из профиля определенного пользователя (например, для составления карточки сотрудника), введите следующее выражение:

```sql
FORMAT("<img height='150' src = 'https://instance.net/api/GetProfilePhoto?id={0}&size=large'> </img>",LIST($Polzovatel))
```

**Здесь**

| Значение | Описание |
| -------- | -------- |
| `https://instance.net` | Ссылка на текущий инстанс. |
| `Polzovatel` | Системное имя атрибута типа «**Пользователь**». |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
