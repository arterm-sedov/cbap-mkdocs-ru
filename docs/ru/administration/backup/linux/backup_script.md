---
title: 'Скрипт для резервного копирования данных Comindware Platform (Linux)'
kbTitle: 'Настройка и использование скрипта для резервного копирования данных Comindware Platform (Linux)'
kbId: 5140
tags:
    - Apache Ignite
    - cron
    - Linux
    - OpenSearch
    - администрирование
    - журналы
    - крон
    - бэкапы
    - бекапы
    - резервное копирование
    - скрипты
hide: tags
---

# Настройка и использование скрипта для резервного копирования данных {{ productName }} (Linux) {: #backup_linux_script }

{% include-markdown ".snippets/experimental_feature.md" %}

## Введение {: #backup_linux_script_intro }

Здесь представлены инструкции по резервному копированию данных **{{ productName }}** с помощью скриптов на стороне сервера вместо использования веб-интерфейса.

Это позволяет системному администратору более гибко управлять процессом и параметрами резервного копирования.

Резервное копирование с помощью скриптов включает следующие шаги:

- создание снимка данных {{ apacheIgniteVariants }}, архивирование и копирование снимка в хранилище резервных копий, очистка использованных ресурсов;
- создание снимка данных {{ openSearchVariants }}, архивирование и копирование снимка в хранилище резервных копий, очистка использованных ресурсов;
- синхронизация сетевой папки с пользовательскими файлами (`Streams`), архивирование и копирование файлов в хранилище резервных копий, очистка использованных ресурсов.

Скрипт резервного копирования  (`cmw_backups_create.sh`) выполняет следующие операции:

- ведёт журнал по пути, указанном в переменной `logFile`;
- сокращает журнал до последних 1000 строк при каждом запуске;
- использует файл блокировки `backup.lock` для предотвращения нескольких одновременных запусков резервного копирования;
- удаляет старые архивы резервных копий согласно параметру `backupDepth`.

!!! warning "Внимание"

    - Создание снимка и сохранение архива могут занимать значительное время в зависимости от размера данных.
    - Требуется достаточное место на диске для временного хранения снимков и архивов.
 
    См. _«[Рекомендации по резервному копированию][backup_recommendations]»_ и _«[Развёртывание ПО. Архитектура и ИТ-ландшафт][architecture_landscape]»_.

## Подготовка и настройка {{ apacheIgniteVariants }} {: #backup_linux_script_prerequisites .pageBreakBefore }

1. Проверьте наличие в директории `/usr/share/ignite` распакованных скриптов {{ apacheIgniteVariants }} актуальной версии.

    Если скрипты отсутствуют, скачайте и распакуйте их в указанную директорию либо переустановите {{ apacheIgniteVariants }} из дистрибутива вспомогательного ПО **{{ productName }}**. См. _«[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]»_ и _«[Пути и содержимое директорий (Linux)][paths_linux]»_.

    !!! note "Расположение скриптов"

        Файлы скриптов резервного копирования по умолчанию расположены в директории `/usr/share/comindware/bin`.

2. Разрешите использование клиентского подключения в файле конфигурации `Ignite.config` {{ apacheIgniteVariants }} на узлах **{{ productName }}** в экземпляра **{{ productName }}**. Для этого найдите соответствующий блок в файле и скорректируйте его согласно следующему примеру:

    ```xml
    ...
        <property name="clientConnectorConfiguration">
        <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
            <property name="thinClientEnabled" value="true" />
            <property name="host" value="127.0.0.1" />
            <property name="port" value="10800" />
    ...
        </bean>
        </property>
    ...
    ```

3. Откройте скрипт резервного копирования `cmw_backups_create.sh` для редактирования:

    ``` sh
    nano /usr/share/comindware/bin/cmw_backups_create.sh
    ```

4. Настройте в скрипте пути и имена в переменных в соответствии с вашей конфигурацией:

    - `instanceName` — имя экземпляра **{{ productName }}** на узле кластера;
    - `snapshotPath` — директория для снимков узла {{ apacheIgniteVariants }}, по умолчанию `/var/lib/comindware/${instanceName}/Database/snapshots`;
    - `backupsPath` — директория с резервными копиями, по умолчанию `/mnt/share/${instanceName}/Backups/Snapshots`;
    - `backupDepth` — срок хранения резервных копий в днях, по умолчанию `14`;
    - `igniteHome` — директория скриптов {{ apacheIgniteVariants }}, по умолчанию `/usr/share/ignite`.
    - `logFile` — путь к файла журнала резервного копирования, по умолчанию `/var/log/comindware/${instanceName}/Logs/cmw_backup.log`.

    !!! warning "Внимание!"

        В кластерной конфигурации необходимо учитывать, что выполнение команды снимка данных на одном узле произведёт формирование снимка данных на каждом узле кластера {{ apacheIgniteVariants }}.
        
        Это может привести к заполнению свободного места и падению узлов **{{ productName }}**.
        
        Поэтому рекомендуется директорию со снимками данных {{ apacheIgniteVariants }} (`backupsPath`) размещать на выделенной области SSD-хранилища типа NVMe.

5. Проверьте выполнения скрипта `cmw_backups_create.sh`, выполнив команду:

    ``` sh
    bash /usr/share/comindware/bin/cmw_backups_create.sh -v
    ```

    !!! warning "Внимание!"

        Обратите внимание на время создания снимка и время сохранения архива.

    !!! tip "Ключи скрипта cmw_backups_create.sh"

        Скрипт `cmw_backups_create.sh` поддерживает следующие ключи:

        - `-v` — подробный вывод (verbose), выводит сообщения в терминал помимо записи в лог
        - `-c` — только очистка (clean-only), выполняет только операции очистки старых снимков без создания нового.

## Запуск скрипта с помощью планировщика (cron) {: #backup_linux_script_cron .pageBreakBefore }

Здесь представлен пример настройки резервного копирования по расписанию: раз в час с 6:00 до 22:00.

1. Откройте очередь задач `crontab`:

    ``` sh
    sudo crontab -e
    ```

2. Добавьте строку запуска скрипта `cmw_backups_create.sh`:

    ``` sh
    0 6-22 * * * sudo bash /usr/share/comindware/bin/cmw_backups_create.sh
    ```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Настройка конфигурации экземпляра ПО][configuration_files_linux]
- [Рекомендации по резервному копированию][backup_recommendations]
- [Пути и содержимое директорий (Linux)][paths_linux]
- [Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]
- [Развёртывание ПО. Архитектура и ИТ-ландшафт][architecture_landscape]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
