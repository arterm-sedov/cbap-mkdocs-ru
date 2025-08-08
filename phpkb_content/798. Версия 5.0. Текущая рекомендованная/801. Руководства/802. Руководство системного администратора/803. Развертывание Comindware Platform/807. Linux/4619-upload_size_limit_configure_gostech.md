---
title: Максимальный размер загружаемых файлов. Настройка для экземпляра ПО
kbId: 4619
---

# Максимальный размер загружаемых файлов. Настройка для экземпляра ПО

## Введение

Здесь представлены инструкции по настройке максимально допустимого размера загружаемых файлов для экземпляра ПО **{{ productName }}**.

К загружаемым файлам относятся документы и изображения, прикреплённые к атрибутам типов «[**Документ**][attribute_document]», «[**Изображение**][attribute_image]» и «**Чертёж**», изображения загруженные на страницах «[**Темы**][themes]» и «[**Дизайн страниц входа и регистрации**][login_and_registration_page_design]», а также [изображения **аккаунтов**][accounts].

## Расположение загруженных файлов

По умолчанию файлы, загружаемые конечными пользователями и формируемые автоматически, хранятся в следующем каталоге:

- `/var/lib/comindware/<instanceName>/Streams` — Linux
- `C:\ProgramData\Comindware\` `Instances\<instanceName>\Streams` — Windows

`/var/lib/comindware/<instanceName>/Streams`

`C:\ProgramData\Comindware\` `Instances\<instanceName>\Streams`

Здесь и далее `<instanceName>` — имя экземпляра ПО.

Подробные сведения о расположении загружаемых файлов см. в статье *«[Пути и содержимое папок экземпляра ПО][paths]».*

## Настройка лимита на объем загружаемых файлов

При развёртывании экземпляра ПО в конфигурации экземпляра ПО и конфигурации сервера NGINX по умолчанию устанавливается максимальный размер передаваемых данных в форме.

Логика работы лимита

- В файле конфигурации `Web.config` (в Linux и Windows) задаются два лимита:
  - `httpRuntime maxRequestLength` — максимальный размер запроса для .NET;
  - `requestLimits maxAllowedContentLength` — максимальный размер запроса для сервера IIS.
- В файле конфигурации NGINX (в Linux) задаётся лимит `client_max_body_size` — максимальный размер запроса.
- Применяется меньший из трёх лимитов.
- Если, например, установлен лимит в 300 МБ:
  - На форме имеется три поля типа «**Документ**» и несколько полей любых типов.
    - К каждому полю типа «**Документ**» можно прикрепить файл объёмом 99 МБ (то есть три файла суммарным размером 297 МБ) и ввести в другие поля формы ещё 3 МБ данных.
    - Можно прикрепить к одному полю типа «**Документ**» файл объёмом 299 МБ и ввести в другие поля формы ещё 1 МБ данных.
    - Можно прикрепить к одному полю типа «**Документ**» файл объёмом 300 МБ.
    - Нельзя прикрепить к полям типа «**Документ**» три файла по 110 МБ.

### Изменение лимита в Linux

Для изменения лимита на размер загружаемых файлов в ОС Linux необходимо отредактировать конфигурацию экземпляра ПО, а также конфигурацию NGINX.

1. Перейдите в режим суперпользователя `root`:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
2. Откройте для редактирования файл `/var/www/comindware<instanceName>/Web.config`:

   ```
   sudo nano /var/www/comindware<instanceName>/Web.config
   ```
3. Установите лимит (например, 1 ГБ) с помощью директив `httpRuntime maxRequestLength` (в килобайтах) и `requestLimits maxAllowedContentLength` (в байтах):

   ```
   <httpRuntime maxRequestLength="1048576" maxUrlLength="4096" requestValidationMode="2.0" shutdownTimeout="300" executionTimeout="3000" targetFramework="4.8" enableVersionHeader="false" />

   ...

   <requestLimits maxAllowedContentLength="1073741824" />
   ```
4. Откройте для редактирования файл `/etc/nginx/sites-available/comindware<instanceName>`:

   ```
   sudo nano /etc/nginx/sites-available/comindware<instanceName>
   ```
5. Откройте для редактирования файл `/etc/nginx/sites-available/comindware<instanceName>`:

   ```
   sudo nano /etc/nginx/sites-available/comindware<instanceName>
   ```
6. Установите лимит в мегабайтах с помощью директивы `client_max_body_size`:

   ```
   client_max_body_size 1024m;
   ```
7. Перезагрузите экземпляр ПО и NGINX:

   ```
   systemctl restart nginx
   systemctl restart comindware<instanceName>
   ```

### Изменение лимита в Windows

Для изменения лимита на размер загружаемых файлов в ОС Windows необходимо отредактировать конфигурацию экземпляра ПО.

1. Откройте для редактирования файл `C:\ProgramData\Comindware\Instances\<instanceName>\Config\Web.config`.
2. Установите лимит (например, 1 ГБ) с помощью директив `httpRuntime maxRequestLength` (в килобайтах) и `requestLimits maxAllowedContentLength` (в байтах):

   ```
   <httpRuntime maxRequestLength="1048576" maxUrlLength="4096" requestValidationMode="2.0"
   shutdownTimeout="300" executionTimeout="3000" targetFramework="4.8" enableVersionHeader="false" />
   ...
   <requestLimits maxAllowedContentLength="1073741824" />
   ```
3. Перезагрузите экземпляр ПО с помощью Утилиты администрирования (либо с помощью *Диспетчера служб IIS* перезагрузите сервер приложений и сайт экземпляра ПО).

--8<-- "related_topics_heading.md"

- *[Пути и содержимое папок экземпляра ПО][paths]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
