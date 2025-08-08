---
title: Создание полной резервной копии (базы данных, вложенных файлов и журналов) без остановки экземпляра ПО
kbId: 4650
---

# Создание полной резервной копии (базы данных, вложенных файлов и журналов) без остановки экземпляра ПО

## Введение

Здесь представлены инструкции по созданию резервной копии базы данных экземпляра ПО **{{ productName }}** без его остановки.

Для создания полной резервной копии базы данных в ОС Linux необходимо с помощью терминала выполнить следующие действия:

- создать снимки состояния памяти Apache Ignite и Elasticsearch;
- скопировать содержимое папок со скриптами и вложенными файлами.

Сведения о последующем восстановлении данных см. в статье *«[Восстановление базы данных, вложенных файлов и журналов из полной резервной копии][restore_complete_backup]»*.

## Сбор данных об экземпляре ПО

Для создания резервной копии соберите перечисленные ниже данные об экземпляре ПО.

1. Имя экземпляра ПО: `<instanceName>`. Можно получить в ответе на запрос localhost:9200/\_cat/indices, например `cmw_cmw-study`, как показано на следующей иллюстрации.

   ![Определение имени экземпляра ПО](https://kb.comindware.ru/assets/Pasted%20image%2020221229181253.png)

   Определение имени экземпляра ПО
2. Директория с базой данных экземпляра ПО: `/var/lib/comindware/<instanceName>/Database`. Может быть задана другая директория с помощью директивы `<workDirectory>` в файле конфигурации `/var/www/comindware/Ignite.config`. Если в файле конфигурации директива `<workDirectory>` не содержит директории, используется директория по умолчанию.
3. Путь для сохранения снимков базы данных Apache Ignite, по умолчанию: `/var/lib/comindware/<instanceName>/Database/snapshots/`
4. Имя репозитория Elasticsearch, заданное при его регистрации, например: `elastic_search_repo_name`
5. Путь для сохранения резервных копий Elasticsearch:

   - например, `/var/www/backups/elasticsearch`
   - должен быть указан в директиве `path.repo` в файле `/etc/elasticsearch/elasticsearch.yml`
   - должен ссылаться на существующий диск;
   - должен находиться на отдельном диске, отдельно от базы данных.![Определение пути для резервных копий Elasticsearch](https://kb.comindware.ru/assets/Pasted%20image%2020221229181640.png)

   Определение пути для резервных копий Elasticsearch
6. Имя снимка, заданное администратором, например, в формате `<instanceName><Date><Time>`

## Установка и настройка исполняемых скриптов Apache Ignite

1. Для установки исполняемых скриптов перейдите в режим суперпользователя `root`:

   ```
   sudo -i
   ```

   или

   ```
   su -
   ```
2. Проверьте наличие пакета `apache-ignite` на машине:

   ```
   dpkg -s apache-ignite
   ```

   Если пакет имеется, пропустите шаги 3–7 и переходите к [назначению прав директории](#assignRights).
3. Если пакета нет, загрузите zip-архив со скриптами:

   ```
   wget -P /tmp/ https://archive.apache.org/dist/ignite/2.16.0/apache-ignite-2.16.0-bin.zip
   ```
4. Если на машине ранее не был установлен пакет `zip`, установите его:

   ```
   apt install zip
   ```
5. Разархивируйте пакет в директорию `/var/www/`:

   ```
   unzip /tmp/apache-ignite-2.16.0-bin.zip -d /var/www
   ```
6. Переименуйте получившуюся директорию со скриптами `Apache Ignite` в `apache-ignite`:

   ```
   mv /var/www/apache-ignite-2.16.0-bin /var/www/apache-ignite
   ```
7. Прейдите в директорию `/var/www/`:

   ```
   cd /var/www/
   ```
8. Назначьте папке `apache-ignite` права на чтение-запись `rwxrwxrwx`:

   ```
   chmod -R 777 apache-ignite/
   ```
9. Смените владельца директории `apache-ignite`:

   **Astra Linux, Ubuntu, Rocky**

   ```
   chown -R www-data:www-data apache-ignite/
   ```

   **Альт Сервер**

   ```
   chown -R _nginx:_nginx apache-ignite/
   ```
10. Создайте директории для сохранения резервных копий:

    ```
    mkdir /var/www/backups/
    ```
11. Создайте директорию репозитория Elasticsearch:

    ```
    mkdir /var/www/backups/elasticsearch
    ```
12. Присвойте директории `backups` права на чтение-запись `rwxrwxrwx`:

    ```
    chmod -R 777 backups/
    ```
13. Смените владельца директории `backups`:

    **Astra Linux, Ubuntu, Rocky**

    ```
    chown -R www-data:www-data backups/
    ```

    **Альт Сервер**

    ```
    chown -R _nginx:_nginx backups/
    ```

## Создание резервной копии

Примечание

При создании снимка после перезагрузки машины необходимо убедиться в том, что экземпляр ПО запущен и Apache Ignite работает. Для этого достаточно в браузере открыть веб-сайт с экземпляром ПО.

1. Задайте переменную `now`:

   ```
   now=$(date  %Y_%m_%d_%H_%M)
   ```
2. Проверьте окружение и создайте снимок состояния Apache Ignite:

   ```
   bash /var/www/apache-ignite/bin/control.sh --baseline
   bash /var/www/apache-ignite/bin/control.sh --snapshot create snapshot_name_$now --sync
   ```
3. Зарегистрируйте репозиторий Elasticsearch. Вместо `elasticsearch_repo_name` и `/var/www/backups/elasticsearch` подставьте своё имя репозитория и путь к его папке:

   ```
   curl -X PUT "localhost:9200/_snapshot/elasticsearch_repo_name?pretty" -H ’Content-Type: application/json’ -d’ {"type": "fs", "settings": {"location": "/var/www/backups/elasticsearch"}}’
   ```
4. Создайте снимок состояния Elasticsearch, заменив ***`elasticsearch_repo_name`*\*,** `snapshot_name`\* и `prefix_name`(префикс индекса, указанный в конфигурации экземпляра ПО) на свои значения:

   ```
   curl -X PUT "localhost:9200/_snapshot/elasticsearch_repo_name/snapshot_name_$now?wait_for_completion=true&pretty" -H ’Content-Type: application/json’ -d’ {"indices": "cmw_prefix_name*", "ignore_unavailable": true, "include_global_state": false}’
   ```
5. Создайте директории для хранения компонентов резервной копии:

   ```
   mkdir /var/www/backups/backup_$now
   mkdir /var/www/backups/backup_$now/Database
   mkdir /var/www/backups/backup_$now/elastic
   mkdir /var/www/backups/backup_$now/Streams
   mkdir /var/www/backups/backup_$now/Scripts
   mkdir /var/www/backups/backup_$now/wal
   ```
6. Перенесите и скопируйте компоненты в директорию резервной копии:

   ```
   mv /var/www/comindware/data/Database/snapshots/snapshot_name_$now /var/www/backups/backup_$now/Database
   cp -r /var/www/backups/elasticsearch/* /var/www/backups/backup_$now/elastic
   cp -r /var/www/comindware/data/Database/wal/* /var/www/backups/backup_$now/wal
   cp -r /var/www/comindware/data/Database/Scripts/* /var/www/backups/backup_$now/Scripts
   cp -r /var/www/comindware/data/Streams/* /var/www/backups/backup_$now/Streams
   ```
7. Создайте архив с резервной копией:

   ```
   tar -cvjf backup_$now.tar.bz2 /var/www/backups/backup_$now
   ```
8. Перенесите архив с резервной копией во внешнее хранилище.

--8<-- "related_topics_heading.md"

- *[Восстановление базы данных, вложенных файлов и журналов из полной резервной копии][restore_complete_backup]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
