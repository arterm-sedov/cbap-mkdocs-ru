---
title: 'Резервное копирование с помощью скриптов (Linux)'
kbTitle: 'Резервное копирование с помощью скриптов (Linux)'
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

# Резервное копирование с помощью скриптов (Linux) {: #backup_linux_script }

!!! warning "Внимание!"

    Представленные здесь скрипты и инструкции следует использовать **только с одним узлом**.

## Введение {: #backup_linux_script_intro }

Здесь представлены инструкции по резервному копированию данных **{{ productName }}** с помощью скриптов на стороне сервера вместо использования веб-интерфейса.

## Подготовка {: #backup_linux_script_prerequisites }

1. Проверьте наличие в директории `/usr/share/ignite` распакованных скриптов {{ apacheIgniteVariants }} актуальной версии.

    Если скрипты отсутствуют, скачайте и распакуйте их в указанную директорию либо переустановите {{ apacheIgniteVariants }} из дистрибутива вспомогательного ПО **{{ productName }}**. См. 

2. Установите пакеты `xxd` и `jq`, если они не были установлены ранее:

    ```sh title="Дистрибутивы на основе Debian"
    apt install xxd jq
    ```

    ```sh title="Дистрибутивы на основе RPM"
    dnf install xxd jq
    ```

## Настройка {{ apacheIgniteVariants }} {: #backup_linux_script_ignite }

1. Настройте скрипт `control.sh`. Добавьте в начало скрипта `/usr/share/ignite/bin/control.sh` следующие строки:

    ```sh
    export DEFAULT_CONFIG=/var/www/<instanceName>/Ignite.config
    export IGNITE_HOME=/usr/share/ignite
    ```

    Здесь и далее `<instanceName>` — имя экземпляра **{{ productName }}**.

2. В файле конфигурации  `Ignite.config` экземпляра **{{ productName }}** разрешите использование клиентского подключения. Для этого найдите соответствующий блок в файле и скорректируйте его согласно следующему примеру:

    ```xml
    ...
        <property name="clientConnectorConfiguration">
        <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
            <property name="thinClientEnabled" value="true" />
            <property name="host" value="10.1.2.3" />
            <property name="port" value="10800" />
    ...
        </bean>
        </property>

    ...
    ```

## Настройка доступа к API {{ productName }} {: #backup_linux_script_api }

1. В **{{ productName }}** создайте аккаунт с ролью системного администратора, от имени которого будут запускаться сеансы резервного копирования, например `backupuser`.
2. В **{{ productName }}** перейдите на страницу «**Администрирование**» — «**Инфраструктура**» — «**Ключи аутентификации**».
3. Создайте ключ аутентификации для аккаунта `backupuser`.
4. Сохраните в безопасном месте значения токена и ключа (`token` и `key`).
5. Создайте директорию `/usr/share/comindware/bin/creds` и в ней два файла:

    - `cred` — сохранить в файл токен подключения к API
    - `secret` — сохранить в файл ключ подключения к API

## Настройка переменных в скрипте {: #backup_linux_script_variables }

!!! note "Расположение скриптов"

    Файлы скриптов по умолчанию расположены в директории `/usr/share/comindware/bin`.

Скорректируйте пути и имена в переменных скрипта в соответствии с вашей конфигурацией.

1. Откройте скрипт резервного копирования для редактирования

    ```sh
    nano /usr/share/comindware/bin/cmw_backups_create.sh
    ```

2. Настройте переменные переменные:

    - `instanceName` — имя экземпляра **{{ productName }}** на узле кластера;
    - `lockfile` — путь к файлу блокировки выполнения резервного копирования, например `/var/lib/comindware/backup.lock`;
    - `logFile` — путь к файла журнала резервного копирования, например `/var/log/comindware/${instanceName}/Logs/cmw_backup.log`;
    - `snapshotPath` — директория для снимков узла {{ apacheIgniteVariants }}, например `/var/lib/comindware/${instanceName}/Database/snapshots`;
    - `backupsPath` — директория с резервными копиями, например `/mnt/share/${instanceName}/Backups/Snapshots`;
    - `backupDepth` — срок хранения резервных копий в днях, например `14`;
    - `igniteHome` — директория скриптов {{ apacheIgniteVariants }}, например `/usr/share/ignite`.

## Запуск и ключи скрипта cmw_backups_create.sh {: #backup_linux_script_run }

Скрипт `cmw_backups_create.sh` поддерживает следующие ключи:

- `-v` — подробный вывод (verbose), выводит сообщения в терминал помимо записи в лог
- `-c` — только очистка (clean-only), выполняет только операции очистки старых снапшотов без создания нового

## Проверка выполнения {: #backup_linux_script_verify }

Для проверки выполнения скрипта с выдачей сообщений в терминал выполните:

```sh
bash /usr/share/comindware/bin/cmw_backups_create.sh -v
```

!!! note "Примечание"

    Обратите внимание на время создания снимка и время сохранения архива!

## Планировщик (cron) {: #backup_linux_script_cron }

Как пример, настроим выполнение резервного копирования раз в час с 6:00 до 22:00.

Для этого откройте очередь задач `crontab`:

```sh
sudo crontab -e
```

Добавьте строку запуска скрипта. Существует два варианта размещения скрипта:

### Вариант 1: Системный путь (рекомендуется)

```sh
0 6-22 * * * sudo bash /usr/share/comindware/bin/cmw_backups_create.sh
```

**Преимущества:** системный путь, единообразие, проще обслуживать.

### Вариант 2: Пользовательский путь

```sh
0 6-22 * * * sudo bash /home/<user>/cmw_snapshot_create.sh
```

**Преимущества:** удобно для отладки/пользовательских окружений; требуется корректная среда и права.

## Журналы и очистка {: #backup_linux_script_logs }

Скрипт автоматически:

- Ведёт журнал в файле, указанном в переменной `logFile`
- Использует файл блокировки `lockfile` для предотвращения одновременного запуска
- Сокращает журнал до последних 1000 строк при каждом запуске
- Очищает старые архивы резервных копий согласно параметру `backupDepth`

## Ограничения и примечания {: #backup_linux_script_limits }

- Скрипт в текущем состоянии поддерживает работу только с одним узлом
- Время выполнения снапшота и сохранения архива может быть значительным в зависимости от размера данных
- Требуется достаточное место на диске для временного хранения снимков и архивов

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Ключи аутентификации API. Определения, настройка, удаление][authentication_keys]
- [Настройка конфигурации экземпляра ПО][configuration_files_linux]
- [Рекомендации по резервному копированию][backup_recommendations]
- [Пути и содержимое директорий (Linux)][paths_linux]
- [Аккаунты. Администрирование, назначение лицензий][accounts]
- [Системные роли. Определения, настройка, объединение, удаление][system_roles]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
