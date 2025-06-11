---
title: Конфигурация экземпляра, компонентов ПО и служб. Настройка
kbId: 5067
---

# Конфигурация экземпляра, компонентов ПО и служб. Настройка {: #configuration_files_linux }

## Введение

Здесь представлены инструкции по настройке файлов конфигурации перед развёртыванием **{{ productName }}**.

## Конфигурация экземпляра ПО

При необходимости тонкой настройки экземпляра ПО, можно изменить файл конфигурации `configmap.yaml` внутри Helm-чарта.

1. Распакуйте файл Helm-чарта.
2. Откройте файл конфигурации экземпляра ПО для редактирования:

    ``` sh
    nano templates/configmap.yaml
    ```

3. При необходимости измените параметры, например:

    - `userStorage.type: LocalDisk` — тип хранилища пользовательских файлов (`LocalDisk` или `S3`).
    - `backup.defaultFolder` — директория для хранения резервных копий экземпляра ПО.
    - `backup.defaultFileName` — имя файла резервной копии экземпляра ПО.

4. Сохраните файл конфигурации.
5. Разверните экземпляр ПО. См. _«[Установка и инициализация ПО][deploy_guide_linux]»_.

### Пример YML-конфигурации экземпляра ПО {: .pageBreakBefore }

<!--instanceYML-start-->
``` yaml
#################### Настройка базовых параметров ПО ####################
# Имя экземпляра {{ productName }}.
clusterName: <instanceName>
# Имя узла экземпляра {{ productName }}.
#nodeName: <instanceName>
# Путь к экземпляру, по которому {{ productName }} находит свою конфигурацию.
configPath: <configPath>
# Адрес службы журналирования {{ openSearchVariants }}.
journal.server: http://<searchHostIP>:<searchHostPort>
# Индекс службы журналирования {{ openSearchVariants }}.
# journal.name: <instanceName>
# URI-адрес экземпляра {{ productName }}.
fqdn: <hostName>
# Порт экземпляра {{ productName }}.
port: <portNumber>
# Версия экземпляра {{ productName }}.
version: <versionNumber>
#################### Настройка базы данных ####################
# Путь к базе данных
# Устаревшая директива: databasePath
db.workDir: /var/lib/comindware/<instanceName>/Database
# Используемый префикс кэшей в базе данных
# Устаревшая директива: databaseName
db.name: <instanceName>
#################### Настройка хранения пользовательских файлов ####################
# Тип хранилища (LocalDisk | S3)
userStorage.type: LocalDisk
# Путь к пользовательским файлам экземпляра
userStorage.localDisk.path: /var/lib/comindware/<instanceName>/Streams
#################### Настройка хранения временных файлов ####################
# Тип хранилища (LocalDisk | S3)
tempStorage.type: LocalDisk
# Путь к временным файлам экземпляра
tempStorage.localDisk.path: /var/lib/comindware/<instanceName>/Temp
# Временная папка
tempWorkingDir: /var/lib/comindware/fooo/LocalTemp
#################### Настройки очереди сообщений ####################
# Адрес и порт сервера очереди сообщений {{ apacheKafkaVariants }}
mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
# Идентификатор группы очереди сообщений
mq.group: <instanceName>
#################### Конфигурация резервного копирования ####################
# Папка для резервного копирования по умолчанию
# Устаревшая директива: backup.config.default.repository.localDisk.path
backup.defaultFolder: /var/lib/comindware/<instanceName>/Backup
# Имя файла для резервного копирования по умолчанию
backup.defaultFileName: Backup
```
<!--instanceYML-end-->

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Пути и содержимое директорий экземпляра ПО][paths]_
- _[Настройка конфигурации вспомогательного ПО для оптимизации работы {{ productName }}][auxiliary_software_optimize]_
- _[Установка и инициализация ПО][deploy_guide_linux]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
