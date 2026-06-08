---
title: 'Шаблон. Переключение флажка «Является справочником» с помощью API'
kbId: 5088
url: 'https://kb.comindware.ru/article.php?id=5088'
updated: '2025-02-25 15:37:39'
---

# Шаблон. Переключение флажка «Является справочником» с помощью API

## Введение

У шаблонов в **Comindware Platform** предусмотрен флажок «**Является справочником**».

Если установлен этот флажок, атрибуты в шаблоне могут ссылаться только на шаблоны-справочники.

## Прикладная задача

Требуется снять флажок «**Является справочником**», чтобы шаблон мог ссылаться на шаблоны, не являющиеся справочниками.

В некоторых конфигурациях переключить этот флажок вручную не представляется возможным, например для шаблонов оргединиц и ролей.

В таком случае его можно переключить с помощью следующих методов [System Core API](https://kb.comindware.ru/article.php?id=4862):

- `/Base/OntologyService/RemoveStatement` — снять флажок;
- `/Base/OntologyService/AddStatement` — установить флажок.

## Снятие флажка «Является справочником» с помощью API

Выполните следующий запрос:

```
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
- `https://your-host/` — адрес сервера **Comindware Platform**.

## Установка флажка «Является справочником» с помощью API

Выполните следующий запрос:

```
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
- `https://your-host/` — адрес сервера **Comindware Platform**.

## Связанные статьи

- *[Методы System Core API](https://kb.comindware.ru/article.php?id=4862)*
- *[Шаблоны. Определения, настройка, перенос, архивирование, очистка](https://kb.comindware.ru/article.php?id=4709)*