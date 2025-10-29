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

    Представленные здесь скрипты и инструкции следует использовать только с одним узлом.

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

## Полный код скрипта cmw_backups_create.sh {: #backup_linux_script_code }

```sh
#!/bin/bash
## COMINDWARE PLATFORM BACKUP

##  VARS, PATHS and CHECKS

## Common

# Path to backup scripts
export CMW_BACKUP_SCRIPT_HOME="/usr/share/comindware/bin"
# Path to "cred" and "secret" files needed for authentication
export AUTH_FILE_DIR="/usr/share/comindware/bin"
# Platform server to make API calls
server="http://localhost"
# Executor for backup session
origin="cmw_backup_script_${HOSTNAME}"
lockfile="/var/lib/comindware/backup.lock"
logFile="/var/log/comindware/cmwdata/Logs/cmw_backup.log"
backupDepth=7
## ignite
## backupIgnite          # true/false
## backupOpensearch      # true/false
## backupStreams         # true/false

## Apache Ignite
igniteHome="/usr/share/ignite"
backupPrefix=""
# snapshotName          # полное имя
if [ "${backupPrefix:-}" = "" ]; then
    snapshotName="backup"_$(date '+%Y%m%d%H%M')
    else
    snapshotName="${backupPrefix}"_$(date '+%Y%m%d%H%M')
fi
snapshotPath="/var/lib/comindware/cmwdata/Database/snapshots"
# snapshotIsIncremental
# snapshotWithCheck

## OpenSearch

## Streams
# streamsPath

## Archive
# archiveFormat
# archiveEncrypt
# compressionAlgorithm
# compressionLevel
backupsPath="/mnt/share/Backups/Ignite/Snapshots"

## LOGGING
# Flag variables for script options
LOG_ONLY=1
CLEAN_ONLY=0

# Script options
while getopts "vc" opt; do
  case $opt in
    v)
      LOG_ONLY=0
      ;;
    c)
      CLEAN_ONLY=1
      ;;
    *)
      ;;
  esac
 done

## FUNCTIONS

## LOGGING
logBase() {
    timestamp="$(date '+%Y-%m-%d %H:%M:%S')"
    echo "$timestamp [$1] $2" >> "${logFile}"
    if [ $LOG_ONLY -eq 0 ]; then
        echo "$timestamp [$1] $2"
    fi
}

## INFO
log() {
    logBase "INFO" "$1"
}

logError() {
    logBase "ERROR" "$1"
}

logResponseError() {
    local message=$1
    local response=$2
    local errorObj=$(jq ".error" <<< "$response")
    local error=$(jq ".message" <<< "$errorObj")
    local logMessage="$message: $error"
    logError "$logMessage"
}

getDate() {
    echo "$(date -u '+%FT%T')Z"
}

## LOG 1000 LINES
logsShortening() {
    tail -n 1000 "${logFile}" > /tmp/temp_cmw_backup.log && mv /tmp/temp_cmw_backup.log "${logFile}"
    # sed -i -n '$q;1000,$p' "${logFile}"
}

## BACKUP.LOCK FILE CHECK
lockCheck() {
    if [ -f "$lockfile" ]; then
        logError "File '$lockfile' exists. Snapshot creation aborted."
        return 1
    else
        log "File '$lockfile' not found. Snapshot creation started."
        return 0
    fi
}

## IGNITE SNAPSHOTS SCRIPTS
# ## Default snapshot creation script temporary unused!!!
# igniteSnapshotDefault() {
    # log "Apache Ignite snapshot will be created to default snapshots path"
    # ${igniteHome}/bin/control.sh --snapshot create ${snapshotName} --sync && log "Apache Ignite snapshot was created: ${snapshotName}"
    # log "Snapshot size" ## TODO find a way to get snapshot size
# }

igniteSnapshotToDest() {
    log "Apache Ignite snapshot will be created to: ${snapshotPath}"
    if ${igniteHome}/bin/control.sh --snapshot create ${snapshotName} --dest ${snapshotPath} --sync; then
        log "Apache Ignite snapshot was created: ${snapshotName}"
        log "Snapshot size $(du -sh ${snapshotPath}/${snapshotName})"
        return 0
    else
        logError "Failed to create Apache Ignite snapshot"
        return 1
    fi
}

## IGNITE SNAPSHOT CREATION
igniteSnapshot () {
    if [[ -z "${backupPrefix}" ]]; then
    snapshotName="backup"_$(date '+%Y%m%d%H%M')
    else
    snapshotName="${backupPrefix}"_$(date '+%Y%m%d%H%M')
    fi
## SNAPSHOTS PATH CHECK
if [ ! -d ${snapshotPath} ]; then
    mkdir -p ${snapshotPath}
fi

## IGNITE SNAPSHOT CREATION
if [ ! -f ${igniteHome}/bin/control.sh ]; then
    logError "Apache Ignite control script not found"
    return 1
else
    if [ -z "${snapshotPath}" ]; then
        igniteSnapshotDefault
        return $?
    else
        igniteSnapshotToDest
        return $?
    fi
fi
}

snapshotCleaning() {
## SNAPSHOTS CLEANING
    log "Snapshots cleaning started"
    if [ ! -d ${backupsPath} ]; then
        log "Backup path ${backupsPath} not found"
        mkdir -p ${backupsPath}
        log "Backup path ${backupsPath} created"
    fi

    cd ${snapshotPath} || exit
#    if [ -z "$(ls -d */ 2>/dev/null)" ]; then
#        log "No extra snapshots found"
#        exit 0
#    fi

#    latest_snapshot=$(ls -td */ | head -n 1)
#    latest_snapshot=${latest_snapshot%/}
#    log "Snapshot to leave untouched: ${latest_snapshot}"

    for snapshot in $(ls -td */); do
        snapshot=${snapshot%/}
#        if [ "$snapshot" != "$latest_snapshot" ]; then
            log "Creating archive for snapshot: ${snapshot}"
            mkdir -p ${backupsPath}/"${snapshot}"
            consistenceID=$(ls "${snapshot}"/db/*/ | grep -v -e "binary_meta/" -e "marshaller/" | head -n 1 | sed 's|/$||')
            tar -czf "${snapshotPath}/${consistenceID}.tar.gz" "$snapshot" && wait
            log "Archive created to: ${snapshotPath}/${consistenceID}.tar.gz"
            archiveSize=$(du -sb ${snapshotPath}/"${consistenceID}".tar.gz | cut -f1)
            log "Archive size: $(du -sh ${snapshotPath}/"${consistenceID}".tar.gz)"
            log "Snapshot will be deleted: ${snapshot}"
            rm -rf "${snapshot}"
            log "Snapshot was deleted: ${snapshot}"
            log "Archive '${consistenceID}.tar.gz' will be moved to: '${backupsPath}/${snapshot}/'"
            rsync --remove-source-files --bwlimit=1G ${snapshotPath}/"${consistenceID}".tar.gz ${backupsPath}/"${snapshot}"/ && log "Archive was moved to: ${backupsPath}/${snapshot}/"
#        fi
    done

## OLD SNAPSHOTS BACKUPS CLEANING
    oldArchives=$(find ${backupsPath} -type d -mtime +${backupDepth} | tr '\n' ' ')
    log "Chosen for removing old archives: ${oldArchives} "

    find ${backupsPath} -type d -mtime +${backupDepth} -exec rm -rF {} + && log "Chosen archives removed" || echo "Nothing to do"
#    find ${backupsPath} -d -mtime +14 -mindepth 1 -maxdepth 1 -exec rm -rf {} +
}

isSuccessResponse() {
    local response=$1
    local isSuccess=$(jq ".success" <<< "$response")
    if [[ "$isSuccess" == "true" ]]; then
        return 0
    else
        return 1
    fi
}

### CHECK PLATFORM IS ALIVE ###
isPlatformAlive() {
    local isAliveResponse=$(bash $CMW_BACKUP_SCRIPT_HOME/platform_ping.sh "$server")
    if isSuccessResponse "$isAliveResponse"; then
        local isAlive=$(jq ".response" <<< "$isAliveResponse")
        if [[ "$isAlive" == "false" ]]; then
            logError "Platform server is unavaliable"
            return 1
        fi
    else
        logResponseError "Failed to ping platform server" "$isAliveResponse"
        return 1
    fi

    log "Platform is avaliable"
    return 0
}

### CREATE NEW BACKUP SESSION RECORD ###
createBackupSessionRecord() {
    local sessionIdResponse=$(bash $CMW_BACKUP_SCRIPT_HOME/create_record.sh --server "$server" --origin "$origin" --status "InProgress" --start-time "$startTime")
    if isSuccessResponse "$sessionIdResponse"; then
        sessionId=$(echo "$sessionIdResponse" | jq ".response" | sed -e 's/^"//; s/"$//')
        return 0
    else
        logResponseError "Failed to create backup session record" "$sessionIdResponse"
        return 1
    fi
}

### UPDATE BACKUP SESSION RECORD ###
updateBackupSessionRecord() {
    local server=$1
    local sessionId=$2
    local startTime=$3
    local endTime=$4
    local snapshotSize=$5
    local status=$6

    if [ -z "$sessionId" ]; then
        logError "Failed to update backup session. Backup session id was not specified."
        return 1
    fi

    local updateResponse=$(bash $CMW_BACKUP_SCRIPT_HOME/update_record.sh --server "$server" --id "$sessionId" --end-time "$endTime" --size "$snapshotSize" --status "$status")
    if isSuccessResponse "$updateResponse"; then
        return 0
    else
        logResponseError "Failed to update backup session with id \"$sessionId\"" "$updateResponse"
        return 1
    fi
}

updateBackupSessionRecordSuccess() {
    updateBackupSessionRecord "$server" "$sessionId" "$startTime" "$endTime" "$archiveSize" "Completed"
    return $?
}

updateBackupSessionRecordFailed() {
    updateBackupSessionRecord "$server" "$sessionId" "$startTime" "$endTime" "0" "Failed"
    return $?
}

doBackup() {
    lockCheck
    if [ $? -eq 1 ]; then
        return 1
    fi
    igniteSnapshot
    local isSuccess=$?
    if [ $isSuccess -eq 0 ]; then
        snapshotCleaning
    fi
    return $isSuccess
}

log "=======BACKUP SCRIPT STARTED======="
if [ "${snapshotPath:-}" = "" ]; then
    logError "Snapshot path ${snapshotPath} not found but required"
    exit 1
    fi
## MAIN

if [ $CLEAN_ONLY -eq 1 ]; then
    snapshotCleaning
else
    if isPlatformAlive; then
        log "=======BACKUP EXECUTION STARTED======="
        startTime=$(getDate)
        createBackupSessionRecord
        doBackup
        isSuccessIgniteBackup=$?
        endTime=$(getDate)
        if [ $isSuccessIgniteBackup -eq 0 ]; then
            updateBackupSessionRecordSuccess
            log "=======BACKUP EXECUTION COMPLETED======="
        else
            updateBackupSessionRecordFailed
            log "=======BACKUP EXECUTION FAILED======="
        fi
    fi
fi

logsShortening

log "=======BACKUP SCRIPT FINISHED======="

```

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

