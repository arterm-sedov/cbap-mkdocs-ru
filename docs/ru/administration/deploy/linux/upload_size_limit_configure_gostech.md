---
title: Максимальный размер загружаемых файлов. Настройка для экземпляра ПО
kbId: 4619
---

# Максимальный размер загружаемых файлов. Настройка для экземпляра ПО { #upload_size_limit_configure}

## Введение

Здесь представлены инструкции по настройке максимально допустимого размера загружаемых файлов для экземпляра ПО **{{ productName }}**.

К загружаемым файлам относятся документы и изображения, прикреплённые к атрибутам типов «[**Документ**][attribute_document]», «[**Изображение**][attribute_image]» и «**Чертёж**», изображения загруженные на страницах «[**Темы**][themes]» и «[**Дизайн страниц входа и регистрации**][login_and_registration_page_design]», а также  [изображения **аккаунтов**][accounts].

## Расположение загруженных файлов

По умолчанию файлы, загружаемые конечными пользователями и формируемые автоматически, хранятся внутри контейнера в следующей директории:
`/var/lib/comindware/<instanceName>/Streams`

Здесь и далее `<instanceName>` — имя экземпляра ПО.

Подробные сведения о расположении загружаемых файлов см. в статье *«[Пути и содержимое папок экземпляра ПО][paths]».*

## Настройка лимита на объем загружаемых файлов {: .pageBreakBefore }

При развёртывании экземпляра ПО в конфигурации экземпляра ПО и конфигурации сервера NGINX по умолчанию устанавливается максимальный размер передаваемых данных в форме.

!!! warning "Логика работы лимита"

    - Лимит на размер файла задаётся в файле конфигурации `values.yaml` Helm-чарта:
    - Если, например, установлен лимит в 300 МБ:
        - На форме имеется три поля типа «**Документ**» и несколько полей любых типов.
            - К каждому полю типа «**Документ**» можно прикрепить файл объёмом 99 МБ (то есть три файла суммарным размером 297 МБ) и ввести в другие поля формы ещё 3 МБ данных.
            - Можно прикрепить к одному полю типа «**Документ**» файл объёмом 299 МБ и ввести в другие поля формы ещё 1 МБ данных.
            - Можно прикрепить к одному полю типа «**Документ**» файл объёмом 300 МБ.
            - Нельзя прикрепить к полям типа «**Документ**» три файла по 110 МБ.

1. Перед тем как развёртывать **{{ productName }}** измените в конфигурационном файле `values.yaml` Helm-чарта следующую директиву:

    ``` yaml
    ...
    # Максимальный размер загружаемого файла в мегабайтах
    client_max_body_size: xxxxx
    ...
    ```

2. Сохраните файл конфигурации.
3. Разверните экземпляр ПО. См. _«[Установка и инициализация ПО][deploy_guide_linux]»_.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Пути и содержимое папок экземпляра ПО][paths]_
- _[Установка и инициализация ПО][deploy_guide_linux]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
