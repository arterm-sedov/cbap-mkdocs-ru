---
kbId: 5390
title: 'Шаблон. Переключение флажка «Является справочником» с помощью API'
---

# Шаблон. Переключение флажка «Является справочником» с помощью API {: #example_termplate_reference_data_api.md }

## Введение

У шаблонов в **{{ productName }}** предусмотрен флажок «**Является справочником**».

Если установлен этот флажок, атрибуты в шаблоне могут ссылаться только на шаблоны-справочники.

## Прикладная задача

Требуется снять флажок «**Является справочником**», чтобы шаблон мог ссылаться на шаблоны, не являющиеся справочниками.

В некоторых конфигурациях переключить этот флажок вручную не представляется возможным, например для шаблонов оргединиц и ролей.

В таком случае его можно переключить с помощью следующих методов [System Core API][api_system_core]:

- `/Base/OntologyService/RemoveStatement` — снять флажок;
- `/Base/OntologyService/AddStatement` — установить флажок.

## Снятие флажка «Является справочником» с помощью API

Выполните следующий запрос:

``` sh
curl -X POST "https://your-host/api/public/system/Base/OntologyService/AddStatement" \
-H "Content-Type: application/json" -d \
'{
  "subject": "template.id",
  "predicate": "cmw.object.specialization",
  "value": "cmw.object.specializationType.ReferenceData"
}'
```

Здесь:

- `template.id` — идентификатор шаблона;
- `https://your-host/` — адрес сервера **{{ productName }}**.

## Установка флажка «Является справочником» с помощью API

Выполните следующий запрос:

``` sh
curl -X POST "https://your-host/api/public/system/Base/OntologyService/AddStatement" \
-H "Content-Type: application/json" -d \
'{
  "subject": "template.id",
  "predicate": "cmw.object.specialization",
  "value": "cmw.object.specializationType.ReferenceData"
}'
```

Здесь:

- `template.id` — идентификатор шаблона;
- `https://your-host/` — адрес сервера **{{ productName }}**.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Методы System Core API][api_system_core]_
- _[Шаблоны. Определения, настройка, перенос, архивирование, очистка][templates]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
