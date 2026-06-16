---
title: 'Проверка на принадлежность пользователя к определенной группе'
kbId: 5273
url: 'https://kb.comindware.ru/article.php?id=5273'
updated: '2026-06-16 19:16:51'
---

# Проверка на принадлежность пользователя к определенной группе

Для того чтобы вывести *true*, если пользователь или хотя бы один из пользователей в указанном атрибуте типа «**Пользователь**» входит в обозначенную системную группу (например, для ограничения видимости полей на экранной форме), введите следующее выражение:

```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix group: <http://comindware.com/ontology/group#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix assert: <http://comindware.com/logics/assert#>.
{
    ("Works" "Performers") object:findProperty ?Performers.

    false -> ?value.

    ?group rdf:type account:Group.
    ?group account:groupName "Managers".
    {
        ?group account:groupUsers ?users.
        ?item ?Performers ?PerformersVal.
        ?PerformersVal == ?users.
    } assert:count ?c.
    if {not {?c == 0}}
    then {true -> ?value.}
    else {}.

}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Works` | Системное имя текущего Шаблона записи. |
| `Performers` | Системное имя атрибута типа «**Пользователь**». |
| `Managers` | Название системной группы. |

Примечание

Данная тройка не учитывает пользователей, входящих во вложенные группы.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
