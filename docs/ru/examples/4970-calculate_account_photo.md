---
title: Вычисление фото из профиля пользователя
kbId: 4970
---

# Вычисление фото из профиля пользователя

Для того, чтобы получить фото из профиля определенного пользователя (например, для составления карточки сотрудника), введите следующее выражение:

```
FORMAT("<img height='150' src = 'https://instance.net/api/GetProfilePhoto?id={0}&size=large'> </img>",LIST($Polzovatel))
```

**где:**

**https://instance.net** — ссылка на текущий инстанс;

**Polzovatel** — системное имя атрибута с типом данных «Пользователь».

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
