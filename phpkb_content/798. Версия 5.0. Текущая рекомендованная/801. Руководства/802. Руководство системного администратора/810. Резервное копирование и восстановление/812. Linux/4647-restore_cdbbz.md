---
title: 'Восстановление базы данных из файла резервной копии в формате CDBBZ'
kbId: 4647
url: 'https://kb.comindware.ru/article.php?id=4647'
---

# Восстановление базы данных из файла резервной копии в формате CDBBZ

## Введение

Здесь представлены инструкции по восстановлению базы данных **{{ productName }}** для следующего сценария:

- используется ранее настроенный экземпляр ПО **{{ productName }}** под управлением ОС Linux;
- имеется файл резервной копии базы данных с расширением `.CDBBZ` (архив резервной копии);
- резервная копия создана с помощью встроенной в ПО функции «**Резервное копирование**» (см. *«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]»*);
- индексы OpenSearch (Elasticsearch) восстанавливаются отдельно от восстановления базы данных экземпляра ПО.

Прежде чем приступать к восстановлению экземпляра ПО **{{ productName }}** из резервной копии, ознакомьтесь с видеороликом и инструкциями, представленными ниже.

## Порядок восстановления

1. Восстановите [базу данных и скрипты](#backup_restore_cdbbz_db_scripts).
2. При необходимости восстановите [лицензионные ключи](#backup_restore_cdbbz_license_keys).
3. При необходимости восстановите [индексы OpenSearch (Elasticsearch)](#backup_restore_cdbbz_indexes).

Фактические пути и имена файлов

При выполнении инструкций будьте внимательны: указывайте фактические имена файлов и пути, которые используются в вашей системе.

Такие имена указаны в угловых скобках, например:

- `<backupName>.cdbbz` — имя файла резервной копии в формате CDBBZ;
- `<Database>` — директория базы данных экземпляра ПО (например, `/var/lib/comindware/<instanceName>/Database`);
- `<instanceName>` — имя экземпляра ПО, для которого выполняется восстановление;
- `<instanceName>.yml` — файл конфигурации экземпляра ПО;
- `<path/to>` — путь к директории или файлу в вашей системе; замените на фактический путь согласно своей структуре каталогов.
- `<Scripts>` — директория, содержащая C#-скрипты экземпляра ПО;
- `<serviceName>` — имя службы, которую требуется проверить или остановить (например, `comindware<instanceName>`,`apigateway<instanceName>`, `adapterhost<instanceName>`);
- `<user>` — имя пользователя, в домашней директории которого находится файл резервной копии;

См. *«[Пути и содержимое директорий экземпляра ПО][paths]»*.

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
3. Остановите службу adapterhost:

   ```
   systemctl stop adapterhost<instanceName>

   ```
4. С помощью команды `systemctl status <serviceName>` удостоверьтесь, что службы остановлены.
5. Перейдите в директорию с CDBBZ-файлом резервной копии, например `/home/<user>`:

   ```
   cd /home/<user>

   ```
6. Создайте временную директорию для распакованной резервной копии (например, `tmp`):

   ```
   mkdir tmp

   ```
7. Распакуйте архив резервной копии в директорию `tmp`:

   ```
   unzip -q <backupName>.cdbbz -d tmp/

   ```
8. Перейдите в директорию `tmp` и просмотрите её содержимое:

   ```
   cd tmp
   ls

   ```
9. Архив будет распакован в несколько директорий.

   Фактический набор директорий

   В дальнейших инструкциях используются директории `Database`, `Scripts` и `Streams`.

   - В архиве всегда имеется директория `Database` с резервной копией базы данных.
   - Если в резервной копии нет директорий `Scripts` и `Streams`, пропускайте связанные с ними инструкции.
   - Если в резервной копии имеется директория `History` с данными OpenSearch (Elasticsearch), их следует восстанавливать средствами OpenSearch (Elasticsearch). См. *«[Восстановление индексов OpenSearch (Elasticsearch) из файла резервной копии репозитория](#backup_restore_cdbbz_indexes)»*.
10. Для восстановления резервной копии используйте пути, указанные в следующих директивах YML-файла конфигурации экземпляра ПО `/usr/share/comindware/configs/instance/<instanceName>.yml`:

    - `db.workDir: <path/to/Database>` — путь к директории базы данных;
    - `userStorage.localDisk.path: <path/to/Streams>` — путь к директории пользовательских файлов.

    Восстановление резервной копии на другом экземпляре ПО

    При создании экземпляра ПО база данных привязывается к имени, которое указано в директиве `db.name` (имя базы данных) файла конфигурации `<instanceName>.yml`.

    Если вы восстанавливаете резервную копию на новом экземпляре ПО, необходимо убедиться, что в YML-файле конфигурации задано такое же значение `db.name`, как у экземпляра ПО, на котором была создана резервная копия.

    Просмотрите файл конфигурации с помощью следующей команды:

    ```
    cat /usr/share/comindware/configs/instance/<instanceName>.yml

    ```
11. Убедитесь в наличии директорий `<Database>` и `<Streams>`, указанных в YML-файле конфигурации:

    ```
    ls -lh <path/to/Database>
    ls -lh <path/to/Streams>

    ```

    - Если папки присутствуют, удалите их содержимое:

      ```
      rm -rf <path>/Database/*
      rm -rf <path>/Streams/*

      ```
    - Если папки отсутствуют, создайте их:

      ```
      mkdir -p <path>/Database
      mkdir -p <path>/Streams

      ```
12. Перейдите в директорию распакованной резервной копии (например, `/home/<user>/tmp/`).
13. Переместите директорию `Scripts` в `Database`:

    ```
    mv Scripts Database

    ```
14. Переместите содержимое резервной копии в директории экземпляра ПО:

    ```
    mv Database/* <path/to/Database>
    mv Streams/* <path/to/Streams>

    ```
15. Назначьте перенесённым директориям права `rwxrw-rw-`:

    ```
    chmod -R 766 <path/to/Database> <path/to/Streams> /var/lib/comindware/<instanceName>

    ```
16. Назначьте перенесенным директориям владельца:

    ```
    chown -R <User>:<Group> <path/to/Database> <path/to/Streams> /var/lib/comindware/<instanceName>

    ```

    Здесь `<User>`, `<Group>` — значения соответствующих параметров из файла `/usr/lib/systemd/system/comindware<instanceName>.service`
17. Если в файле конфигурации экземпляра ПО отсутствует параметр `nodeName` (имя узла экземпляра ПО), добавьте его:

    - Откройте файл конфигурации для редактирования:

      ```
      nano /usr/share/comindware/configs/instance/<instanceName>.yml

      ```
    - Добавьте директиву:

      ```
      nodeName: <instanceName>

      ```

    Имя узла и лицензионные ключи

    Чтобы использовать на восстановленном экземпляре ПО прежние лицензионные ключи, скопируйте имя узла из конфигурации исходного экземпляра ПО.

    См. *«[Восстановление лицензионных ключей](#backup_restore_cdbbz_license_keys)»*.
18. При необходимости [восстановите индексы OpenSearch (Elasticsearch)](#backup_restore_cdbbz_indexes) из резервной копии.
19. Запустите службы экземпляра ПО и проверьте их статус:

    ```
    systemctl start adapterhost<instanceName>
    systemctl start comindware<instanceName>
    systemctl start apigateway<instanceName>

    ```

    ```
    systemctl status comindware<instanceName>
    systemctl status apigateway<instanceName>
    systemctl status adapterhost<instanceName>

    ```
20. Откройте веб-сайт экземпляра ПО.
21. Дождитесь инициализации экземпляра ПО. Этот процесс может занять некоторое время. Может потребоваться обновить страницу браузера. См. *«[Инициализация {{ productName }}][deploy_guide_linux]»*.
22. Удостоверьтесь, что все данные из резервной копии восстановлены.
23. Проверьте и исправьте конфигурацию экземпляра ПО. См. *«[Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]»*.
24. Удалите временную директорию с распакованной резервной копией:

    ```
    rm -r /home/<user>/tmp

    ```

## Восстановление лицензионных ключей

Внимание!

Лицензионные ключи привязаны к имени экземпляра ПО (`<instanceName>`) и уникальному идентификатору оборудования сервера (Hardware ID).

Поэтому восстановление возможно только на том же сервере, на котором была создана резервная копия.

При развёртывании на новом оборудовании необходимо заново выполнить активацию лицензионных ключей.

Чтобы использовать на восстановленном экземпляре ПО прежние лицензионные ключи, выполните указанные ниже действия.

1. Откройте файл конфигурации для редактирования:

   ```
   nano /usr/share/comindware/configs/instance/<instanceName>.yml

   ```
2. Укажите такое же значение `nodeName` (имя узла экземпляра ПО), как в конфигурации исходного экземпляра ПО:

   ```
   nodeName: <instanceName>

   ```
3. Включите директиву `isContainerEnvironment`:

   ```
   isContainerEnvironment: true

   ```
4. Перезапустите экземпляр ПО:

   ```
   systemctl restart comindware<instanceName>

   ```
5. Удостоверьтесь, что лицензионные ключи присутствуют на странице «**Администрирование**» — «**[Лицензирование][licensing]**».
6. Назначьте лицензионные ключи аккаунтам и группам.

## Восстановление индексов OpenSearch (Elasticsearch) из файла резервной копии репозитория

Логика работы репозитория снимков OpenSearch (Elasticsearch)

OpenSearch (Elasticsearch) сохраняет и восстанавливает резервные копии своих данных в виде снимков в директорию, заданную директивой `path.repo` в файле конфигурации `/etc/elasticsearch/elasticsearch.yml`.

Эта директория служит как для сохранения резервных копий, так и для их восстановления.

1. Остановите службу OpenSearch (Elasticsearch) и удостоверьтесь, что она остановлена:

   ```
   systemctl stop elasticsearch
   systemctl status elasticsearch

   ```
2. Создайте папку репозитория OpenSearch (Elasticsearch) (например, `/var/backups/elasticsearch/`) и перенесите в неё файлы из каталога `History` ранее [распакованной резервной копии](#unpack_backup):

   ```
   mkdir /var/backups/elasticsearch/
   mv /var/lib/comindware/<instanceName>/History/* /var/backups/elasticsearch/

   ```
3. Назначьте папке репозитория и её содержимому полные права доступа:

   ```
   chmod -R 777 /var/backups/elasticsearch/

   ```
4. Назначьте владельца `elasticsearch` папке репозитория и её содержимому:

   ```
   chown -R elasticsearch:elasticsearch /var/backups/elasticsearch/

   ```
5. В файле конфигурации `/etc/elasticsearch/elasticsearch.yml` укажите путь к созданному репозиторию:

   ```
   path.repo: /var/backups/elasticsearch

   ```
6. Запустите службу OpenSearch (Elasticsearch):

   ```
   systemctl start elasticsearch

   ```
7. Зарегистрируйте репозиторий (например, `<repository_backup>`) с резервной копией снимка OpenSearch (Elasticsearch) (`<openSearchHost>` — адрес сервера OpenSearch (Elasticsearch)) :

   - **С авторизацией в OpenSearch (Elasticsearch):**

     ```
     curl -X PUT "https://<openSearchHost>:<opeSearchPort>/_snapshot/<repository_backup>?pretty" \\
     -u <username>:<password> \\
     -H 'Content-Type: application/json' -d \\
     '{
         "type": "fs",
         "settings": {
             "location": "/var/backups/elasticsearch"
         }
     }'

     ```
   - **Без авторизации в OpenSearch (Elasticsearch):**

     ```
     curl -X PUT "https://<openSearchHost>:<opeSearchPort>/_snapshot/<repository_backup>?verify=false&pretty" \\
     -H 'Content-Type: application/json' -d \\
     '{
         "type": "fs",
         "settings": {
             "location": "/var/backups/elasticsearch"
         }
     }'

     ```

   Примечание

   Шаги 7 и 8 не требуются при восстановлении снимка из хранилища S3.

   Для восстановления снимка из хранилища S3 используйте репозиторий с именем, совпадающим с префиксом индекса OpenSearch (Elasticsearch).

   Этот репозиторий создаётся автоматически при запуске резервного копирования

   Префикс индекса задаётся в свойствах подключения к OpenSearch (Elasticsearch).
8. Проверьте содержимое зарегистрированного репозитория:

   ```
   curl -X GET "https://<openSearchHost>:<opeSearchPort>/_snapshot/<repository_backup>?pretty"

   ```
9. Восстановите снимок OpenSearch (Elasticsearch):

   ```
   curl -X POST "https://<openSearchHost>:<opeSearchPort>/_snapshot/<repository_backup>/<backupsessionXX>/_restore?pretty"

   ```

   - В качестве репозитория укажите имя репозитория, созданного на шаге 7, или префикс индекса OpenSearch (Elasticsearch) при восстановлении из хранилища S3 (см. [примечание](#s3_repository) выше).
   - В качестве имени снимка укажите идентификатор резервной копии **без точки перед номером и строчными буквами** (например, `backupSession.123` указывайте как `backupsession123`) со страницы [«Администрирование» – «Инфраструктура» – «Резервное копирование» – «Журнал»](../configure.html#backup_configure_sessions_list "Просмотр списка сеансов резервного копирования").
10. Проверьте наличие индексов в восстановленном каталоге:

    ```
    curl -X GET "https://<openSearchHost>:<opeSearchPort>/_cat/indices?pretty"

    ```

--8<-- "related_topics_heading.md"

- [Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]
- [Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]
- [Пути и содержимое директорий экземпляра ПО][paths]
- [Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]
- [Регистрация репозитория OpenSearch (Elasticsearch) (официальное руководство, английский язык)](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-filesystem-repository.html)
- [Восстановление снимка OpenSearch (Elasticsearch) (официальное руководство, английский язык)](https://www.elastic.co/guide/en/elasticsearch/reference/current/restore-snapshot-api.html)
- [Создание полной резервной копии (базы данных, вложенных файлов и журналов) без остановки экземпляра ПО][complete_running_instance_backup]
- [Восстановление базы данных, вложенных файлов и журналов из полной резервной копии][restore_complete_backup]
- [Лицензирование. Активация, назначение, отзыв и продление лицензий][licensing]

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
