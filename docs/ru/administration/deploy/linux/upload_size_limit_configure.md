---
title: Максимальный размер загружаемых файлов. Настройка для экземпляра ПО
kbId: 2569
---

# Максимальный размер загружаемых файлов. Настройка для экземпляра ПО

## Введение

В данной статье представлены инструкции по настройке максимально допустимого размера загружаемых файлов для экземпляра ПО **{{ productName }}** в операционных системах Windows и Linux (Astra Linux, Альт Сервер, РЕД ОС, Rocky Linux, Ubuntu и т. п.).

К загружаемым файлам относятся документы и изображения, прикреплённые к атрибутам типов «[**Документ**]({{ kbArticleURLPrefix }}2241)», «[**Изображение**]({{ kbArticleURLPrefix }}2253)» и «**Чертёж**», изображения загруженные на страницах «[**Темы**]({{ kbArticleURLPrefix }}2199)» и «[**Дизайн страниц входа и регистрации**]({{ kbArticleURLPrefix }}2198)», а также  [изображения **аккаунтов**]({{ kbArticleURLPrefix }}2194#mcetoc_1gjrh0knp6).

## Расположение загруженных файлов

По умолчанию файлы, загружаемые конечными пользователями и формируемые автоматически, хранятся в следующем каталоге:

- `/var/lib/comindware``/instancename/Streams` — Linux
- `C``:\``ProgramData``\``Comindware``\`  `Instances``\instancename\Streams` — Windows

Здесь и далее `instancename` — имя экземпляра ПО.

Подробные сведения о расположении загружаемых файлов см. в статье *«[Пути и содержимое папок экземпляра ПО][paths]».*

## Настройка лимита на объем загружаемых файлов

При развёртывании экземпляра ПО в конфигурации экземпляра ПО и конфигурации сервера NGINX по умолчанию устанавливается максимальный размер передаваемых данных в форме.

Логика работы лимита

- В файле конфигурации `Web.config` (в Linux и Windows) задаются два лимита:
	- `httpRuntime maxRequestLength` — максимальный размер запроса для .NET;
	- `requestLimits maxAllowedContentLength` — максимальный размер запроса для сервера IIS.
- В файле конфигурации NGINX (в Linux) задаётся лимит `client_max_body_size` — максимальный размер запроса.
- Применяется меньший из трёх лимитов.
- Если, например, установлен лимит в 300 МБ:
	- На форме имеется три поля типа «**Документ**» и несколько полей любых типов.
		- К каждому полю типа «**Документ**» можно прикрепить файл объёмом 99 МБ (то есть три файла суммарным размером 297 МБ) и ввести в другие поля формы ещё 3 МБ данных.
		- Можно прикрепить к одному полю типа «**Документ**» файл объёмом 299 МБ и ввести в другие поля формы ещё 1 МБ данных.
		- Можно прикрепить к одному полю типа «**Документ**» файл объёмом 300 МБ.
		- Нельзя прикрепить к полям типа «**Документ**» три файла по 110 МБ.

### Изменение лимита в Linux

Для изменения лимита на размер загружаемых файлов в ОС Linux необходимо отредактировать конфигурацию экземпляра ПО, а также конфигурацию NGINX.

1. Перейдите в режим суперпользователя `root`: 


```
sudo -i
```
2. Откройте для редактирования файл `/var/www/``comindwareinstancename``/Web.config`: 


```
sudo nano /var/www/comindwareinstancename/Web.config
```
3. Установите лимит (например, 1 ГБ) с помощью директив `httpRuntime maxRequestLength` (в килобайтах) и `requestLimits maxAllowedContentLength` (в байтах):

```
<httpRuntime maxRequestLength="1048576" maxUrlLength="4096" requestValidationMode="2.0" shutdownTimeout="300" executionTimeout="3000" targetFramework="4.8" enableVersionHeader="false" />

...

<requestLimits maxAllowedContentLength="1073741824" />       
```
4. Откройте для редактирования файл `/etc/nginx/sites-available/comindwareinstancename`:


```
sudo nano /etc/nginx/sites-available/comindwareinstancename
```
5. Откройте для редактирования файл `/etc/nginx/sites-available/comindwareinstancename`:


```
sudo nano /etc/nginx/sites-available/comindwareinstancename
```
6. Установите лимит в мегабайтах с помощью директивы `client_max_body_size`:

```
client_max_body_size 1024m;
```
7. Перезагрузите экземпляр ПО и NGINX:

```
systemctl restart nginx  
systemctl restart comindwareinstancename
```

### Изменение лимита в Windows

Для изменения лимита на размер загружаемых файлов в ОС Windows необходимо отредактировать конфигурацию экземпляра ПО.

1. Откройте для редактирования файл `C``:\``ProgramData``\``Comindware``\``Instances``\instancename``\``Config``\Web.config`.
2. Установите лимит (например, 1 ГБ) с помощью директив `httpRuntime maxRequestLength` (в килобайтах) и `requestLimits maxAllowedContentLength` (в байтах):

```
<httpRuntime maxRequestLength="1048576" maxUrlLength="4096" requestValidationMode="2.0" shutdownTimeout="300" executionTimeout="3000" targetFramework="4.8" enableVersionHeader="false" />

...

<requestLimits maxAllowedContentLength="1073741824" />
```
3. Перезагрузите экземпляр ПО с помощью Утилиты администрирования (либо с помощью Диспетчера служб IIS перезагрузите сервер приложений и сайт экземпляра ПО).

--8<-- "related_topics_heading.md"

**[Пути и содержимое папок экземпляра ПО][paths]**

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}