---
title: Вычисление руководителя подразделения из шаблона пользователя
kbId: 5291
tags:
    - N3
    - атрибуты
    - выражение на N3
    - пример
    - процессы
hide: tags
---

# Вычисление руководителя подразделения из шаблона пользователя {: #calculate_dept_manager }

Для того чтобы вычислить руководителя подразделения из Шаблона пользователя ( в случае, если руководитель определяется именно там, а не в Шаблоне записи), например, для использования при назначении задач, введите следующее выражение:

```turtle
@prefix cmw: <http://comindware.com/logics#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix account: <http://comindware.com/ontology/account#>.
{

    ("Sotrudniki" "Rukovoditelbool") object:findProperty ?rukovoditel.
    ("Sotrudniki" "Podrazdelenie") object:findProperty ?userDiv.
    ("Naryady" "NaryadPodrazdelenie") object:findProperty ?divNar.
    ("Divisions" "Title") object:findProperty ?divID.

        ?item ?divNar ?div.
        ?div ?divID ?divtext.
        ?user a account:Account.
        ?user ?userDiv ?userDivValue.
        ?userDivValue == ?divtext.
        ?user ?userDiv ?divtext.
        ?user ?rukovoditel true.
        ?user account:active true.
        ?value == ?user.
}
```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| `Sotrudniki` | Системное имя Шаблона пользователя. |
| `Rukovoditelbool` | Системное атрибута типа «**Логический**» в **Sotrudniki**, определяющий, является ли пользователь руководителем. |
| `Podrazdelenie` | Системное атрибута типа «**Ссылка**» в **Sotrudniki**, определяющий подразделение пользователя. |
| `Naryady` | Системное имя текущего Шаблона записи. |
| `NaryadPodrazdelenie` | Системное имя атрибута типа «**Ссылка**» в **Naryady**. |
| `Divisions` | Системное имя Шаблона записи, на который ссылаются **Podrazdelenie**и **NaryadPodrazdelenie**. |
| `Title` | Системное имя атрибута для поиска в **Divisions**. |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
