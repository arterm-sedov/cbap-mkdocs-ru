---
title: 'Восстановление базы данных из файла резервной копии в формате .CDBBZ'
kbId: 2500
url: 'https://kb.comindware.ru/article.php?id=2500'
updated: '2024-12-10 13:40:32'
---

# Восстановление базы данных из файла резервной копии в формате .CDBBZ

## Введение

Здесь представлены инструкции по восстановлению базы данных **{{ productName }}** для следующего сценария:

- используется ранее настроенный экземпляр ПО **{{ productName }}** под управлением ОС Linux;
- имеется файл резервной копии базы данных с расширением `.CDBBZ`;
- резервная копия создана с помощью встроенной в ПО функции «**Резервное копирование**» (см. *«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов](https://kb.comindware.ru/article.php?id=2190)»*);
- индексы Elasticsearch восстанавливаются отдельно от восстановления базы данных экземпляра ПО.

## Восстановление базы данных и скриптов

1. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
2. Остановите службы экземпляра ПО (где `<instanceName>` — имя экземпляра ПО):

   ```
   systemctl stop comindware<instanceName>
   systemctl stop apigateway<instanceName>
   ```

   ```
   ps -fax | grep <instanceName> | grep Agent
   kill -9 $(ps -eo pid,args | grep <instanceName> | grep Agent | awk {'print $1'})
   #или
   systemctl stop adapterhost<instanceName>
   ```
3. С помощью команды `systemctl status <serviceName>` удостоверьтесь, что службы остановлены.
4. Перейдите в директорию с резервной копией, например `/home/<user>`

   ```
   cd /home/<user>
   ```
5. Создайте временную директорию для распакованной резервной копии (например, `tmp`):

   ```
   mkdir tmp
   ```
6. Распакуйте архив резервной копии в директорию `tmp`:

   ```
   unzip -q <backupName>.cdbbz -d tmp/
   ```
7. Перейдите в директорию `tmp` и просмотрите её содержимое:

   ```
   cd tmp
   ls
   ```
8. После распаковки архива в директории быть 3 директории: `Database`, `Scripts`, `Streams`.

   Примечание

   Если в распакованной резервной копии имеется директория `Ignite` вместо `Database`, переименуйте её в `Database`:

   ```
   mv Ignite Database
   ```
9. Для восстановления резервной копии используйте следующие параметры из YML-файла конфигурации экземпляра ПО `/usr/share/comindware/configs/instance/<instanceName>.yml`:

   `databasePath: <path/to/Database>` — путь к директории базы данных; `userStorage.localDisk.path: <path/to/Streams>` — путь к директории пользовательских файлов;

   Просмотрите откройте файл конфигурации с помощью следующей команды:

   ```
   cat /usr/share/comindware/configs/instance/<instanceName>.yml
   ```
10. Убедитесь в наличии директорий `<path/to/Database>` и `<path/to/Streams>`:

    ```
    ls -lh `<path/to/Database>`
    ls -lh `<path/to/Streams>`
    ```

    - Если папки отсутствуют, создайте их:

      ```
      mkdir -p `<path/to/Database>`
      mkdir -p `<path/to/Streams>`
      ```
11. Перейдите в директорию распакованной резервной копии (например, `/home/<user>/temp/`).
12. Переместите директорию `Scripts` в `Database`:

    ```
    mv Scripts Database
    ```
13. Переместите содержимое резервной копии в директории экземпляра ПО:

    ```
    mv Database/* <path/to/Database>
    mv Streams/* <path/to/Streams>
    ```
14. Назначьте перенесённым директориям права `rwxrw-rw-`:

    ```
    chmod -R 766 <path/to/Database/folder> <path/to/Streams> /var/lib/comindware/<instanceName>
    ```
15. Назначьте перенесенным директориям владельца:

    ```
    chown -R <User>:<Group> <path/to/database/folder> <path/to/streams/folder> /var/lib/comindware/<instanceName>
    ```

    Здесь `<User>`, `<Group>` — значения соответствующих параметров из файла `/usr/lib/systemd/system/comindware<instanceName>.service`
16. Если в файле конфигурации экземпляра ПО отсутствует параметр `nodeName` (имя узла экземпляра ПО), добавьте его:

    - Откройте файл конфигурации для редактирования:

      ```
      nano /usr/share/comindware/configs/instance/<instanceName>.yml
      ```
    - Добавьте директиву:

      ```
      nodeName: <instanceName>
      ```
17. При необходимости [восстановите индексы Elasticsearch](#восстановление-индексов-elasticsearch-из-файла-резервной-копии-репозитория) из резервной копии.
18. Запустите службы экземпляра ПО и проверьте их статус:

    ```
    systemctl start comindware<instanceName>
    systemctl start apigateway<instanceName>
    systemctl start adapterhost<instanceName>
    ```

    ```
    systemctl status comindware<instanceName>
    systemctl status apigateway<instanceName>
    systemctl status adapterhost<instanceName>
    ```
19. Откройте веб-сайт экземпляра ПО.
20. Дождитесь инициализации экземпляра ПО. Этот процесс может занять некоторое время. Может потребоваться обновить страницу браузера. См. *«[Инициализация {{ productName }}](https://kb.comindware.ru/article.php?id=2344#deploy_guide_linux_initialize)»*.
21. Удостоверьтесь, что все данные из резервной копии восстановлены.
22. Проверьте и исправьте конфигурацию экземпляра ПО. См. *«[Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии](https://kb.comindware.ru/article.php?id=2618)»*.
23. Удалите временную директорию с распакованной резервной копией:

    ```
    rm -r /home/<user>/tmp
    ```

## Восстановление индексов Elasticsearch из файла резервной копии репозитория

1. Остановите службу Elasticsearch и удостоверьтесь, что она остановлена:

   ```
   systemctl stop elasticsearch
   systemctl status elasticsearch
   ```
2. Создайте папку репозитория Elasticsearch (например, `/var/www/backups/elasticsearch/`) и перенесите в неё файлы из каталога `History` ранее [распакованной резервной копии](#unpack_backup):

   ```
   mkdir /var/www/backups/elasticsearch/
   mv /var/lib/comindware/<instanceName>/History/* /var/www/backups/elasticsearch/
   ```
3. Назначьте папке репозитория и её содержимому права `rwxr-xr-x`:

   ```
   chmod -R 755 /var/www/backups/
   ```
4. Назначьте владельца `elasticsearch` папке репозитория и её содержимому:

   ```
   chown -R elasticsearch:elasticsearch /var/www/backups/
   ```
5. В файле конфигурации `/etc/elasticsearch/elasticsearch.yml` укажите путь к созданному репозиторию:

   ```
   path.repo: /var/www/backups/elasticsearch
   ```
6. Запустите службу Elasticsearch:

   ```
   systemctl start elasticsearch.service
   ```
7. Зарегистрируйте репозиторий (например, `repostory_backup`) с резервной копией снимка Elasticsearch:

   ```
   curl -X PUT "localhost:9200/_snapshot/repostory_backup?pretty" -H ’Content-Type: application/json’ -d’
   {
   "type": "fs",
   "settings": {
               "location": "/var/www/backups/elasticsearch"
               }
   }
   ```

   Примечание

   Шаги 7 и 8 не требуются при восстановлении снимка из хранилища S3.

   Для восстановления снимка из хранилища S3 используйте репозиторий с именем, совпадающим с префиксом индекса Elasticsearch.

   Этот репозиторий создаётся автоматически при запуске резервного копирования

   Префикс индекса задаётся в [свойствах подключения к Elasticsearch](https://kb.comindware.ru/article.php?id=2593), используемого по умолчанию.
8. Проверьте содержимое зарегистрированного репозитория:

   ```
   curl -X GET "localhost:9200/_cat/snapshots/repostory_backup?pretty"
   ```
9. Восстановите снимок Elasticsearch:

   ```
   curl -X POST "localhost:9200/_snapshot/repostory_backup/backupSession123/_restore?pretty"
   ```

   - В качестве репозитория укажите имя репозитория, созданного на шаге 7, или префикс индекса Elasticsearch (см. [примечание](#s3_repository) выше).
   - В качестве имени снимка укажите идентификатор резервной копии **без точки перед номером** (например, `backupSession.123` указывайте как `backupSession123`) со страницы [«Администрирование» – «Инфраструктура» – «Резервное копирование» – «Журнал»](https://kb.comindware.ru/article.php?id=2190).
10. Проверьте наличие индексов в восстановленном каталоге:

    ```
    curl -X GET "localhost:9200/_cat/indices?pretty"
    ```

--8<-- "related_topics_heading.md"

- *[Резервное копирование. Настройка и запуск, просмотр журнала сеансов](https://kb.comindware.ru/article.php?id=2190)*
- *[Установка, запуск, инициализация и остановка ПО](https://kb.comindware.ru/article.php?id=2344)*
- *[Пути и содержимое директорий экземпляра ПО](https://kb.comindware.ru/article.php?id=2502)*
- *[Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии](https://kb.comindware.ru/article.php?id=2618)*
- *[Регистрация репозитория Elasticsearch (официальное руководство, английский язык)](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-filesystem-repository.html)*
- *[Восстановление снимка Elasticsearch (официальное руководство, английский язык)](https://www.elastic.co/guide/en/elasticsearch/reference/current/restore-snapshot-api.html)*
- *[Elasticsearch. Настройка подключения](https://kb.comindware.ru/article.php?id=2593)*
- *[Создание полной резервной копии (базы данных, вложенных файлов и журналов) без остановки экземпляра ПО](https://kb.comindware.ru/article.php?id=2117)*
- *[Восстановление базы данных, вложенных файлов и журналов из полной резервной копии](https://kb.comindware.ru/article.php?id=2335)*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
