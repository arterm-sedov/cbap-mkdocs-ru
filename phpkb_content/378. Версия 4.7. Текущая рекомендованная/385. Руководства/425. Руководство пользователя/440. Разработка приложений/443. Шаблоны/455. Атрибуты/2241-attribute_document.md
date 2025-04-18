---
title: Атрибут типа «Документ»
kbId: 2241
---

# Атрибут типа «Документ»

## Свойства атрибута

Атрибут типа «**Документ**» содержит один или несколько загруженных конечным пользователем файлов.

Помимо **[общих свойств][attribute_common_properties]** для атрибута типа «**Документ**» предусмотрены перечисленные ниже свойства.

- «**Формат отображения**» — выберите способ представления загруженных файлов в полях атрибута на формах:

    - «**Без предпросмотра**» — отображение только имен загруженных файлов;
    - «**С предпросмотром**» — отображение миниатюр с содержимым загруженных файлов (поддерживаются только файлы PDF);
    - «**Документ с цифровой подписью**» — отображение кнопок «**Подписать**» и «**Перейти к форме**» для работы с цифровыми подписями.
- «**Фильтр расширений файлов**» — выберите типы файлов, которые можно будет загрузить в атрибут: **PDF**, **TXT**, **PNG**, **JPG**, **CSV**, **XLSX**, **DOCX**, **PPTX**, **VSDX**, **MSG**, **ZIP**, **BMP**, **EMF**. Если не выбрано ни одно расширение, то можно будет загрузить файлы любых типов. Этот раскрывающийся список не отображается, если выбран формат отображения «**С предпросмотром**»
- «**Хранить несколько значений**» — установите этот флажок, чтобы в атрибут можно было загрузить несколько файлов (по умолчанию флажок установлен).
- «**Удалять связанные записи**» — установите этот флажок, чтобы можно было удалять загруженные в атрибут файлы.
- «**Использовать для поиска записей**» — установите этот флажок, чтобы записи шаблона можно было искать по именам и содержимому загруженных в атрибут файлов. См. раздел «**[Атрибуты для поиска записей шаблона][attribute_searchable]**».

_![Свойства атрибута типа «Документ»](https://kb.comindware.ru/assets/attribute_document_properties.png)_

## Пример использования

Прикрепление к записи актов, приложений и документов на подпись

**Конфигурация приложения**

| Атрибут | Формат отображения | Хранить несколько значений |
| --- | --- | --- |
| Акты | Без предпросмотра | Флажок установлен |
| Приложение | С предпросмотром | Флажок снят |
| Документы на подпись | Документ с цифровой подписью | Флажок установлен |

**Результирующее поведение**

![Поле «Акты»: документы без предпросмотра](https://kb.comindware.ru/assets/attribute_document_example_no_preview.png)
Поле «Акты»: документы без предпросмотра

![Поле «Приложение»: документ с предпросмотром](https://kb.comindware.ru/assets/attribute_document_example_preview.png)
Поле «Приложение»: документ с предпросмотром

![Поле «Документы на подпись»: документы с цифровой подписью](https://kb.comindware.ru/assets/attribute_document_example_digital_signature.png)
Поле «Документы на подпись»: документы с цифровой подписью

--8<-- "related_topics_heading.md"

**[Атрибут типа «Документ». Копирование записи вместе с прикреплённым документом с помощью сценария по нажатию кнопки][attribute_document_clone_scenario]**

**[Общие свойства атрибутов][attribute_common_properties]**

**[Атрибуты. Определения, типы, настройка, архивирование, удаление][attributes]**



{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
