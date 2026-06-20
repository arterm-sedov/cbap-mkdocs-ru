---
title: 'Вычисление руководителя подразделения из шаблона пользователя'
kbId: 4965
url: 'https://kb.comindware.ru/article.php?id=4965'
updated: '2026-06-20 18:06:10'
---

# Вычисление руководителя подразделения из шаблона пользователя

Для того чтобы вычислить руководителя подразделения из Шаблона пользователя ( в случае, если руководитель определяется именно там, а не в Шаблоне записи), например, для использования при назначении задач, введите следующее выражение:

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

**Здесь:**

| Значение | Описание |
| --- | --- |
| `Sotrudniki` | Системное имя Шаблона пользователя. |
| `Rukovoditelbool` | Системное атрибута типа «**Логический**» в **Sotrudniki**, определяющий, является ли пользователь руководителем. |
| `Podrazdelenie` | Системное атрибута типа «**Ссылка**» в **Sotrudniki**, определяющий подразделение пользователя. |
| `Naryady` | Системное имя текущего Шаблона записи. |
| `NaryadPodrazdelenie` | Системное имя атрибута типа «**Ссылка**» в **Naryady**. |
| `Divisions` | Системное имя Шаблона записи, на который ссылаются **Podrazdelenie**и **NaryadPodrazdelenie**. |
| `Title` | Системное имя атрибута для поиска в **Divisions**. |