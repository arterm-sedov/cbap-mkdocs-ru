---
title: Отображение последней записи в коллекции
kbId: 4944
---

# Отображение последней записи в коллекции

Для того, чтобы в коллекции настроить фильтр на отображение последней/их записи/ей, введите следующее выражение:

```

@prefix object: <http://comindware.com/ontology/object#>.
@prefix sort: <http://comindware.com/ontology/dataset/sort#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
 
{
    ("Document" "_creationDate") object:findProperty ?creationDate.
    ("Document" "_isDisabled") object:findProperty ?isDisabled.
  ("Document" "Otchety") object:findProperty ?Otcheti.
 
 
    from {
    ?OtchetiVal ?Otcheti ?item.
    not {?OtchetiVal ?isDisabled true.}.
    ?OtchetiVal ?creationDate ?creationDateVal.
    } select ?creationDateVal -> ?creationDateValList.
 
    (?creationDateValList sort:timeComparer) assert:sort ?orderedCreationDateValList.
    ?orderedCreationDateValList rdf:last ?maxDate.
  once {?OtchetiVal2 ?Otcheti ?item.
    not {?OtchetiVal2 ?isDisabled true.}.
        ?OtchetiVal2 ?creationDate ?maxDate.
  }.
 
    ?OtchetiVal2 -> ?value.
}

```

**где:**

**Document** – системное имя Шаблона записи, на который ссылается коллекция;

**Otchety** – системное имя обратной ссылки в Шаблоне записи, где находится коллекция;

**\_creationDate** – системное имя атрибута "Дата создания", хранящегося в Шаблоне записи **Document**;

**\_isDisabled** – системное имя логического атрибута "В архиве", хранящегося в Шаблоне записи **Document** (для исключения отображения архивных записей).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
