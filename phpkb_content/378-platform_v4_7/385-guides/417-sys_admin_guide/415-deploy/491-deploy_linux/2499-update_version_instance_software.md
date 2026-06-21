---
title: 'Обновление версии экземпляра ПО'
kbId: 2499
url: 'https://kb.comindware.ru/article.php?id=2499'
updated: '2024-12-09 16:45:44'
---

# Обновление версии экземпляра ПО

## Введение

Здесь представлены краткие инструкции по обновлению до 4.7.XXXX версии экземпляра ПО **{{ productName }}** под управлением ОС Linux.

## Порядок обновления версии экземпляра ПО

1. Подготовьте экземпляр ПО к обновлению:

   - Сохраните резервную копию экземпляра ПО.
   - Остановите экземпляр ПО.
   - Сохраните конфигурацию экземпляра ПО и вспомогательных служб.
   - Удалите компоненты старой версии ПО.
2. Обновите версию экземпляра ПО:

   - Скачайте и распакуйте дистрибутив новой версии ПО.
   - Установите новую версию ПО.
   - Обновите экземпляр ПО до новой версии.
   - Обновите конфигурацию экземпляра ПО и вспомогательных служб.
   - Перезапустите экземпляр ПО и вспомогательные службы.

## Подготовка экземпляра ПО к обновлению

Выполните подготовительные действия для каждого экземпляра ПО, версию которого требуется обновить.

1. Создайте и перенесите во внешнее хранилище резервную копию базы данных экземпляра ПО. См. статью *«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов](https://kb.comindware.ru/article.php?id=2190)»*.
2. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
3. Сохраните резервную копию конфигурационных файлов, например в директорию `/var/backups/config_tmp`:

   - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

   ```
   mkdir -p /var/backups/config_tmp/
   cd /var/www/<instanceName>/
   cp *.config apigateway.json /var/backups/config_tmp/
   cp /etc/nginx/sites-available/comindware<instanceName> /var/backups/config_tmp/
   ```

   - **РЕД ОС**, **Rocky** (RPM-based)

   ```
   mkdir -p /var/backups/config_tmp/
   cd /var/www/<instanceName>/
   cp *.config apigateway.json /var/backups/config_tmp/
   cp /etc/nginx/conf.d/comindware<instanceName> /var/backups/config_tmp/
   ```

   - **Альт Сервер**

   ```
   mkdir -p /var/backups/config_tmp/
   cd /var/www/<instanceName>/
   cp *.config apigateway.json /var/backups/config_tmp/
   cp /etc/nginx/sites-available.d/comindware<instanceName> /var/backups/config_tmp/
   ```

   Здесь `<instanceName>` — имя экземпляра ПО.
4. Остановите экземпляр ПО и его вспомогательные службы и удостоверьтесь, что они остановлены:

   ```
   systemctl stop apigateway<instanceName> comindware<instanceName>
   systemctl status apigateway<instanceName> comindware<instanceName>
   ```
5. Проверьте, выполняется ли сервис `Comindware.Adapter.Agent.exe`:

   ```
   ps fax | grep Agent
   ```

   - Если процесс `Comindware.Adapter.Agent.exe`, выполняется, завершите его по `PID`:

     ```
     kill -9 <PID>
     ```
6. Проверьте имя и статус экземпляра:

   ```
   systemctl status comindware*
   ```
7. Удалите (или переместите в резервное хранилище) неиспользуемые предыдущие дистрибутивы ПО (`<distPath>` — путь к директории с дистрибутивом, `<osname>` — название операционной системы):

   ```
   rm -rf <distPath>/CMW_<osname>
   ```

## Обновление версии ПО для экземпляра

Выполните шаги 6–13 для каждого экземпляра ПО, версию которого требуется обновить, так как скрипт обновления выполняется отдельно для указанного экземпляра ПО.

1. Скачайте и распакуйте дистрибутив с новой версией ПО (`X.X`, `<versionNumber>` — номер версии ПО):

   ```
   cd <distPath>
   tar -xf X.X-release-ru-<versionNumber>.<osname>.tar.gz
   ```
2. Перейдите в распакованную папку:

   ```
   cd CMW_<osname>/scripts/cbap
   ```
3. Запустите установку распакованного дистрибутива ПО:

   ```
   bash install.sh
   ```
4. Проверьте наличие и имя директории установленной версии ПО:

   ```
   bash list.sh
   ```
5. Отобразится список установленных версий ПО на сервере.
6. Перейдите в директорию скриптов для работы с экземпляром ПО и запустите его обновление до требуемой версии:

   ```
   cd ../instance/
   bash upgrade.sh -n=<instanceName> -vp=/var/www/.cmw_version/<versionNumber>
   ```

   Здесь:

   - `-n=<instanceName>` — имя обновляемого экземпляра ПО;
   - `-vp=/var/www/.cmw_version/<versionNumber>` — укажите путь к папке с установленной версией ПО, где `<versionNumber>` — номер версии ПО.
7. По окончании обновления скрипт выведет информацию о компонентах экземпляра ПО. Удостоверьтесь, что компоненты успешно обновлены.

   Пример результата выполнения скрипта:

   ```
   ...
   [Done] Creating Log Directories.
   OK     Instance folder created.
   OK     Instance Web config created.
   OK     Instance Ignite config created.
   OK     Instance binaries linked.
   OK     Instance config created.
   OK     Data folder created.
   OK     Database folder created: Yes
   OK     Streams folder created: No
   OK     Logs folder created: Yes
   OK     Used version: <versionNumber>
   OK     Logs configured.
   OK     Sites created.
   OK     Sites enabled.
   OK     API Gateway configured.
   OK     Link to binaries is valid.
   OK     Instance service started.
   FAILED Instance API gateway service started.
   OK     NGINX started.
   FAILED Final status.
   [Done] Upgrade CBAP instance.
   ```

   Если какая-либо из служб имеет статус `FAILED`, перезапустите её (`<serviceName>` — имя службы):

   ```
   systemctl restart <serviceName>.service
   ```
8. Проверьте корректность конфигурации NGINX для экземпляра ПО:

   - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

     ```
     nano /etc/nginx/sites-available/comindware<instanceName>
     ```
   - **РЕД ОС**, **Rocky** (RPM-based)

     ```
     nano /etc/nginx/conf.d/comindware<instanceName>
     ```
   - **Альт Сервер**

     ```
     nano /etc/nginx/sites-available.d/comindware<instanceName>
     ```
   - При необходимости восстановите конфигурацию NGINX, [сохранённую ранее](#NginxBackup).

     - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

     ```
     cp /var/backups/config_tmp/comindware<instanceName> /etc/nginx/sites-available/
     nginx -t && nginx -s reload
     ```

     - **РЕД ОС**, **Rocky** (RPM-based)

     ```
     cp /var/backups/config_tmp/comindware<instanceName> /etc/nginx/conf.d/
     nginx -t && nginx -s reload
     ```

     - **Альт Сервер**

     ```
     cp /var/backups/config_tmp/comindware<instanceName> /etc/nginx/sites-available.d/
     nginx -t && nginx -s reload
     ```
9. Откройте для редактирования файл конфигурации `/var/www/<instanceName>/apigateway.json`.

   - Проверьте и при необходимости отредактируйте адрес сервера Kafka:

     ```
     "Kafka": {
         # Укажите адрес сервера Kafka
         # Должен совпадать с mq.server
         # в /usr/share/comindware/configs/instance/<instanceName>.yml
         "BootstrapServer": "<KAFKAIP>:9092",
         # Укажите имя экземпляра ПО
         # Должно совпадать с mq.group
         # в /usr/share/comindware/configs/instance/<instanceName>.yml
         "GroupId": "<instanceName>"
     }
     ```
10. Если выполняется обновление с версии ниже 4.6.1140.0, откройте для редактирования файл конфигурации экземпляра ПО `/usr/share/comindware/configs/instance/<instanceName>.yml`.

    - Замените в конфигурации следующие директивы:

      ```
      # исходная директива
      # backupPath: /var/backups/<instanceName>
      # заменить на:
      backup.config.default.repository.type: LocalDisk
      backup.config.default.repository.localDisk.path: /var/backups/<instanceName> ## backupPath

      # исходная директива
      # tempPath: /var/lib/comindware/<instanceName>/Temp
      # заменить на:
      tempStorage.type: LocalDisk
      tempStorage.localDisk.path: /var/lib/comindware/<instanceName>/Temp ## tempPath

      # исходная директива
      # streamsPath: /var/streams/<instanceName>
      # заменить на:
      userStorage.type: LocalDisk
      userStorage.localDisk.path: /var/streams/<instanceName>
      ```
    - Добавьте в конфигурацию следующие директивы:

      ```
      # Имя конфигурации
      configName: <instanceName>

      # Имя базы данных Apache Ignite
      instanceName: <instanceName>

      manageAdapterHost: true
      useDataBusNumbers:
          - 0
          - 1
          - 2
          - 3
      ```
11. Удостоверьтесь, что итоговый файл конфигурации `/usr/share/comindware/configs/instance/<instanceName>.yml` выглядит аналогично следующему примеру:

    ```
    databasePath: /var/lib/comindware/<instanceName>/Database/
    configPath: /var/www/<instanceName>
    backup.config.default.repository.type: LocalDisk
    backup.config.default.repository.localDisk.path: /var/lib/comindware/<instanceName>/Backup
    userStorage.type: LocalDisk
    userStorage.localDisk.path: /var/lib/comindware/<instanceName>/Streams
    tempStorage.type: LocalDisk
    tempStorage.localDisk.path: /var/lib/comindware/<instanceName>/Temp
    elasticsearchUri: XXX.XXX.XXX.XXX:9200 #адрес сервера ElasticSearch
    instanceName: <instanceName>
    configName: <instanceName>
    databaseName: <instanceName>
    nodeName: prod_0
    linuxAuthenticationType: 1
    ldapAuthenticationType: 1
    isFederationAuthEnabled: 0
    manageAdapterHost: true
    isTestEnvironment: false
    mq.enabled: true
    mq.server: XXX.XXX.XXX.XXX:9092 #адрес сервера Kafka
    mq.group: <instanceName> #имя группы в Kafka
    mq.node: prod_0
    mq.name: <instanceName> #имя очереди в Kafka
    mq.adapter.0.enabled: true
    mq.adapter.1.enabled: true
    mq.adapter.2.enabled: true
    mq.adapter.3.enabled: true
    version: <versionNumber>
    ```
12. Перезапустите сервисы, настройки которых были изменены:

    ```
    systemctl restart apigateway<instanceName> comindware<instanceName>
    ```
13. Откройте сайт экземпляра ПО в браузере, дождитесь окончания загрузки, одновременно открыв выдачу журналов экземпляра в терминале:

    ```
    tail -f /var/log/comindware/<instanceName>/Log/sys*
    ```
14. После обновления всех экземпляров ПО, старую версию ПО можно удалить согласно инструкции *«[Удаление версии ПО](deploy_guide.html#deploy_guide_linux_delete_version)»*.

--8<-- "related_topics_heading.md"

- *[Установка, запуск, инициализация и остановка ПО](https://kb.comindware.ru/article.php?id=2344)*
- *[Резервное копирование. Настройка и запуск, просмотр журнала сеансов](https://kb.comindware.ru/article.php?id=2190)*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
