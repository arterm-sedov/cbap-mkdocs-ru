---
title: Атрибут типа «Документ»
kbId: 4782
---

# Атрибут типа «Документ»

## Свойства атрибута

Структура атрибута типа «Документ»

- Атрибут типа «**Документ**» хранит одну или несколько ссылок на записи (**документы**) в системном шаблоне документа, к которым прикрепляются файлы (например, загруженные пользователями).
- В шаблоне документа имеется атрибут `currentRevision` (текущая **версия**), который хранит ссылку на запись в системном шаблоне версии.
- В шаблоне версии имеются атрибуты `title` (имя) и `content` (содержимое), которые хранят имя файла и ссылку на файл, физически хранящийся в папке `Streams` на сервере.

Извлечение файлов из атрибута помощью C#

Чтобы считать файл из атрибута типа «**Документ**» с помощью C#-скрипта, необходимо:

- из текущей записи получить массив идентификаторов файлов, прикреплённых к атрибуту:

  ```
  var fileIds = Api.TeamNetwork.ObjectService.GetPropertyValues(recordId, new [] {"documentAttributeSystemName"})`;

  ```
- получить массив объектов с прикреплёнными файлами:

  ```
  var attachedFileObjects = fileIds[docId].TryGetValue("Files", out object fileObject)
                              && fileObject != null ? fileObject as object[] : null;

  ```
- получить объект файла (`attachedFile`):

  ```
  var attachedFile = Api.TeamNetwork.DocumentService.GetContent(attachedFileObject[0].ToString());

  ```
- получить имя файла с расширением (`attachedFile.Name`);
- получить содержимое файла (`attachedFile.Data`);
- при необходимости получить объект с метаданными документа:

  ```
  var attachedFile = Api.TeamNetwork.DocumentService.GetDocument(attachedFileObject[0].ToString());

  ```

  - `attachedFile.Title` — имя файла с расширением;
  - `attachedFile.Extension` — расширение файла.

Добавление файлов в атрибут с помощью C#

Чтобы прикрепить к атрибуту типа «**Документ**» файл с помощью C#-скрипта, необходимо:

- сформировать объект типа `Document`:

  ```
  var document = new Document
      {
          Title = "имя файла.расширение",
          Extension = ".расширение"
      };

  ```
- сформировать массив байтов `byte[] fileBytes` с содержимым файла;
- из массива байтов создать поток `MemoryStream()` для прикрепления документа к атрибуту:

  ```
      var fileStream = new MemoryStream();
      fileStream.Write(fileBytes, 0, fileBytes.Length);
      fileStream.Seek(0, SeekOrigin.Begin);

  ```
- преобразовать поток в объект документа для прикрепления к атрибуту:

  ```
  string documentObject = Api.TeamNetwork.DocumentService.CreateDocumentWithStream(document, fileStream, "");

  ```
- сформировать словарь из системного имени атрибута и объекта документа:

  ```
  var documentDict = new Dictionary<string,object>
      {
          { "DocumentAttributeSystemName", documentObject }
      };

  ```
- прикрепить результирующий документ к атрибуту записи `reсordId`:

  ```
      Api.TeamNetwork.ObjectService.EditWithAlias(reсordId, documentDict)

  ```

Префиксы N3 для работы с атрибутом

Для работы с атрибутом типа «**Документ**» в выражениях на N3 могут потребоваться следующие префиксы:

```
@prefix object: <http://comindware.com/ontology/object#>.
@prefix document: <http://comindware.com/ontology/document#>.

```

Извлечение файлов из атрибута с помощью N3

Чтобы считать файл из атрибута типа «**Документ**» с помощью выражения N3, необходимо:

- получить объект с атрибутом:

  ```
  ("TemplateSystemName" "DocumentAttributeSystemName") object:findProperty ?DocumentAttribute.

  ```
- из объекта с атрибутом получить значение атрибута в текущей записи:

  ```
  ?item documentAttribute ?documentAttributeValue.

  ```
- из значения атрибута получить текущую версию документа:

  ```
  ?documentAttributeValue document:revision ?revision.

  ```
- из версии получить содержимое файла в формате `base64`:

  ```
  ?revision document:content ?content.

  ```
- из версии получить имя файла:

  ```
  ?revision document:title ?title.

  ```

Добавление файлов в атрибут с помощью N3

Чтобы прикрепить к атрибуту типа «**Документ**» файл с помощью выражения N3, необходимо:

- сформировать содержимое файла в формате `base64`:

  ```
  ?documentContentSource document:content ?content.

  ```
- сформировать имя файла:

  ```
  ?documentTitleSource document:title ?title.

  ```
- прикрепить полученный файл к атрибуту типа «**Документ**», т. е. поместить на него ссылку в версию:

  ```
  (?content ?title) document:attach ?documentAttributeValue.

  ```

## Настройка свойств атрибута

Помимо **[общих свойств][attribute_common_properties]** для атрибута типа «**Документ**» предусмотрены перечисленные ниже свойства.

- «**Формат отображения**» — выберите способ представления загруженных файлов в полях атрибута на формах:

  - «**Без предпросмотра**» — отображение только имен загруженных файлов;
  - «**С предпросмотром**» — отображение миниатюр с содержимым загруженных файлов (поддерживаются только файлы PDF);
  - «**Документ с цифровой подписью**» — отображение кнопок «**Подписать**» и «**Перейти к форме**» для работы с цифровыми подписями.
  - «**Фильтр расширений файлов**» — выберите типы файлов, которые можно будет загрузить в атрибут: **PDF**, **TXT**, **PNG**, **JPG**, **CSV**, **XLSX**, **DOCX**, **PPTX**, **VSDX**, **MSG**, **ZIP**, **BMP**, **EMF**. Если не выбрано ни одно расширение, то можно будет загрузить файлы любых типов. Этот раскрывающийся список не отображается, если выбран формат отображения «**С предпросмотром**»
  - «**Хранить несколько значений**» — установите этот флажок, чтобы в атрибут можно было загрузить несколько файлов (по умолчанию флажок установлен).
  - «**Удалять связанные записи**» — установите этот флажок, чтобы можно было удалять загруженные в атрибут файлы.
  - «**Использовать для поиска записей**» — установите этот флажок, чтобы записи шаблона можно было искать по именам и содержимому загруженных в атрибут файлов. См. раздел «**[Атрибуты для поиска записей шаблона][attribute_searchable]**».

_![Свойства атрибута типа «Документ»](/platform/v5.0/business_apps/templates/attributes/img/attribute_document_properties.png)_

## Примеры использования

Ознакомьтесь с перечисленными ниже подробными статьями, а также простейшим примером настройки атрибутов типа «**Документ**».

- *[Клонирование записи вместе с прикреплёнными файлами][example_document_clone_scenario_n3]*
- *[Скачивание архива с файлами из всех строк таблицы с прикреплением архива к атрибуту][example_document_download_archive_related_records_csharp]*;
- *[Скачивание архива с файлами из выбранных строк таблицы и записи][example_document_download_archive_csharp]*
- *[Скачивание файлов в папку на сервере][example_document_download_to_server_csharp]*

Прикрепление к записи актов, приложений и документов на подпись

**Конфигурация приложения**

| Атрибут | Формат отображения | Хранить несколько значений |
| --- | --- | --- |
| *Акты* | **Без предпросмотра** | Флажок установлен |
| *Приложение* | **С предпросмотром** | Флажок снят |
| *Документы на подпись* | **Документ с цифровой подписью** | Флажок установлен |

**Результирующее поведение**

_![Поле «Акты»: документы без предпросмотра](/platform/v5.0/business_apps/templates/attributes/img/attribute_document_example_no_preview.png)_

_![Поле «Приложение»: документ с предпросмотром](/platform/v5.0/business_apps/templates/attributes/img/attribute_document_example_preview.png)_

_![Поле «Документы на подпись»: документы с цифровой подписью](/platform/v5.0/business_apps/templates/attributes/img/attribute_document_example_digital_signature.png)_

--8<-- "related_topics_heading.md"

- *[Копирование записи вместе с прикреплённым документом. Настройка сценария][example_document_clone_scenario_n3]*
- *[Общие свойства атрибутов][attribute_common_properties]*
- *[Атрибуты. Определения, типы, настройка, архивирование, удаление][attributes]*
- *[Атрибут типа «Документ». Скачивание архива с файлами из всех строк таблицы с прикреплением архива к атрибуту][example_document_download_archive_related_records_csharp]*
- *[Атрибут типа «Документ». Скачивание архива с файлами из выбранных строк таблицы и записи][example_document_download_archive_csharp]*
- *[Атрибут типа «Документ». Клонирование записи вместе с прикреплёнными файлами][example_document_clone_scenario_n3]*
- *[Атрибут типа «Документ». Скачивание файлов в папку на сервере][example_document_download_to_server_csharp]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
