---
title: Вычисление руководителя подразделения из шаблона пользователя
kbId: 4965
---

# Вычисление руководителя подразделения из шаблона пользователя

Для того, чтобы вычислить руководителя подразделения из Шаблона пользователя ( в случае, если руководитель определяется именно там, а не в Шаблоне записи), например, для использования при назначении задач, введите следующее выражение:

```

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

**где:**

**Sotrudniki** – системное имя Шаблона пользователя;

**Rukovoditelbool** – системное атрибута типа "Логический" в **Sotrudniki**, определяющий, является ли пользователь руководителем;

**Podrazdelenie** – системное атрибута типа "Ссылка" в **Sotrudniki**, определяющий подразделение пользователя;

**Naryady** – системное имя текущего Шаблона записи;

**NaryadPodrazdelenie** – системное имя атрибута типа "Ссылка" в **Naryady**;

**Divisions**– системное имя Шаблона записи, на который ссылаются **Podrazdelenie**и **NaryadPodrazdelenie**;

**Title**– системное имя атрибута для поиска в **Divisions**.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
