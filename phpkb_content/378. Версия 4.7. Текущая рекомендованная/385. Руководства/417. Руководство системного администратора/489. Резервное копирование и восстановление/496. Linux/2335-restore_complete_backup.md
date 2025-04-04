---
title: Восстановление базы данных, вложенных файлов и журналов из полной резервной копии
kbId: 2335
---

# Восстановление базы данных, вложенных файлов и журналов из полной резервной копии

## Введение

В этой статье представлены инструкции по восстановлению базы данных экземпляра ПО **{{ productName }}** (далее «экземпляр ПО»), развёрнутого в среде Linux.

Данные инструкции подходят для восстановления из резервной копии, созданной по инструкциям в статье *«[Создание полной резервной копии (базы данных, вложенных файлов и журналов) без остановки экземпляра ПО][complete_running_instance_backup]»*.

В данных инструкциях используются только стандартные средства операционной системы и Elasticsearch.

В статье рассмотрены два сценария:

- восстановление базы данных при её переносе на новую машину;
- восстановление базы данных на ранее работавшей системе c имеющейся базой данных.

Для восстановления базы данных экземпляра ПО из файла резервной копии необходимо распаковать архив резерва в пользовательскую или временную директорию, откуда уже перенести файлы и директории в целевые директории.

Для восстановления журнала операций требуется зарегистрировать репозиторий в Elasticsearch и из зарегистрированного репозитория восстановить данные.

Исходные данные

Для восстановления данных перейдите в директорию с резервной копией базы данных экземпляра ПО, созданной по инструкции в статье *«[Создание полной резервной копии (базы данных, вложенных файлов и журналов) без остановки экземпляра ПО][complete_running_instance_backup]»*.

В настоящей статье предполагается, что архив резервной копии находится папке `/tmp/`.

## Подготовка к восстановлению из резервной копии

1. Для выполнения всех операций перейдите в режим суперпользователя `root`:

```
sudo -i
```

или

```
su -
```
2. Перед тем как выполнять любые действия с файлами ПО и базы данных, остановите экземпляр ПО и его вспомогательные службы и удостоверьтесь, что они остановлены:

```
systemctl stop elasticsearch nginx kafka comindware<instancename>
systemctl status elasticsearch nginx kafka comindware<instancename>
```

Здесь `<instancename>` — имя экземпляра ПО.
3. Если восстановление из резервной копии производится в рамках переноса продукта на чистый экземпляр ПО без базы данных, переходите к [этапу 3](#mcetoc_1grg5gft85).
4. Для сохранения целостности данных перед восстановлением из резервной копии требуется очистить директории c базой данных и загруженными файлами:

```
rm -rf /var/lib/comindware/<instancename>/Database/*
rm -rf /var/lib/comindware/<instancename>/Streams/*
```

## Восстановление базы данных и загруженных файлов из резервной копии

1. Перейдите в директорию с загруженным архивом резервной копии (например, `tmp)`:

```
cd /tmp/
```
2. Распакуйте архив с резервной копией (например, `backup_2023_01_23_10_17.tar.bz2`):

```
tar -xf backup_2023_01_23_10_17.tar.bz2
```
3. Войдите в директорию резервной копии и просмотрите её содержимое:

```
cd backup_2023_01_23_10_17/
ll
```

![Содержимое папки резервной копии](https://kb.comindware.ru/assets/Pasted image 20230125133846.png)

Содержимое директории резервной копии

Распакованная директория резервной копии должна иметь следующую структуру:

    - - `Database` — файлы базы данных.
        - `Scripts` — скомпилированные библиотеки для скриптов на языке C#.
        - `snapshots` — снимок данных Apache Ignite Ignite.
        - `wal` — журнал предварительной записи.
        - `elastic` — копия репозитория Elasticsearch.
        - `Streams` — загруженные пользователями и сформированные системой файлы, которые прикреплены к соответствующим атрибутам.

_![Структура резервной копии](https://kb.comindware.ru/assets/Pasted image 20230125134843.png)_
4. Перенесите снимок данных Apache Ignite (в примере — содержимое директории `/tmp/backup_2023_01_23_10_17/Database/snapshots/snapshot_2023_01_23_10_17/`) в рабочую директорию Apache Ignite (`/var/www/comindware/data/Database/`):

```
mv Database/snapshots/snapshot_2023_01_23_10_17/* /var/lib/comindware/<instancename>/Database/
```
5. Перенесите директорию со скриптами из резервной копии в рабочую директорию Apache Ignite:

```
mv Database/Scripts /var/lib/comindware/<instancename>/Database/
```
6. Перенесите директорию с загруженными файлами из резервной копии в целевую директорию:

```
mv Streams /var/lib/comindware/<instancename>/Database/
```
7. Назначьте перенесённым папкам права `rwxr-xr-x`:

```
chmod -R 755 /var/lib/comindware/<instancename>/Database/Streams/
chmod -R 755 /var/lib/comindware/<instancename>/Database/
```
8. Назначьте перенесенным папкам владельца `www-data`:

```
chown -R www-data:www-data /var/lib/comindware/<instancename>/Database/Streams/
chown -R www-data:www-data /var/lib/comindware/<instancename>/Database/
```

## Восстановление индексов Elasticsearch из резервной копии репозитория

1. 4.1. Создайте директорию репозитория Elasticsearch и перенесите в неё файлы из резервной копии:

```
mkdir /var/www/backups/elasticsearch/
mv elastic/* /var/www/backups/elasticsearch/
```
2. Назначьте папке репозитория и её содержимому права `rwxr-xr-x`:

```
chmod -R 755 /var/www/backups/
```
3. Назначьте владельца `elasticsearch` директории репозитория и её содержимому:

```
chown -R elasticsearch:elasticsearch /var/www/backups/
```
4. В файле конфигурации `elasticsearch.yml` с помощью директивы `path.repo: /var/www/backups/elasticsearch` укажите путь к созданному репозиторию (например, с помощью редактора `nano`):

```
nano /etc/elasticsearch/elasticsearch.yml
```

_![Путь к репозиторию в файле конфигурации Elasticsearch](https://kb.comindware.ru/assets/Pasted image 20230125204737.png)_
5. Запустите службу Elasticsearch:

```
systemctl start elasticsearch.service
```
6. Зарегистрируйте новый репозиторий снимков Elasticsearch:

```
curl -X PUT "localhost:9200/_snapshot/elastic_snap?pretty" -H 'Content-Type: application/json' -d' {"type": "fs", "settings": {"location": "/var/www/backups/elasticsearch"}}'
```
7. Проверьте содержимое зарегистрированного репозитория:

```
curl -X GET "localhost:9200/_cat/snapshots/elastic_snap?pretty"
```
8. Выберите необходимый снимок и восстановите состояние Elasticsearch:

```
curl -X POST "localhost:9200/_snapshot/elastic_snap/snapshot2023_01_23_10_17/_restore?pretty"
```
9. Проверьте наличие индексов в восстановленном каталоге:

```
curl -X GET "localhost:9200/_cat/indices?pretty"
```

_![Отображение списка индексов Elasticsearch](https://kb.comindware.ru/assets/Pasted image 20230127153756.png)_

## Запуск и проверка конфигурации экземпляра ПО

1. Запустите необходимые службы и проверьте их статус:

```
systemctl start elasticsearch kafka nginx comindware<instancename>
systemctl status elasticsearch kafka nginx comindware<instancename>
```
2. Откройте в браузере веб-сайт с экземпляром ПО.
3. Дождитесь инициализации экземпляра ПО. Этот процесс может занять некоторое время. Может потребоваться обновить страницу браузера.
4. Проверьте и исправьте конфигурацию экземпляра. См. *«[Проверка и настройка конфигурации экземпляра ПО после восстановления из резервной копии][restore_test_configure]».*

--8<-- "related_topics_heading.md"

**[Проверка и настройка конфигурации экземпляра ПО после восстановления из резервной копии][restore_test_configure]**

**[Создание полной резервной копии (базы данных, вложенных файлов и журналов) без остановки экземпляра ПО][complete_running_instance_backup]**



{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
