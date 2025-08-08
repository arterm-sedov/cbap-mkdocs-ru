---
title: Обновление версии экземпляра ПО без его остановки
kbId: 5097
---

# Обновление версии экземпляра ПО без его остановки

## Введение

Здесь представлены инструкции по обновлению версии экземпляра ПО **{{ productName }}** без его остановки путём создания нового экземпляра на отдельном сервере и последующего переключения DNS на него.

Инструкции даны для обновления с версий 4.7.2 до версий 4.7.3–5.0 в ОС Linux.

Совет

Такой способ обновления можно использовать, если ПО **{{ productName }}** возможно развернуть **на нескольких машинах**.

Тогда каждый экземпляр ПО можно обновить последовательно без его остановки.

**Если вы не можете развернуть дополнительную машину**, следуйте инструкции *«[Обновление версии экземпляра ПО с его остановкой][upgrade_version_linux]»*.

## Порядок обновления версии экземпляра ПО

1. Подготовьте данные старого экземпляра для обновления:

   - Создайте резервную копию базы данных старого экземпляра.
   - Создайте резервную копию файлов конфигурации старого экземпляра.
2. Создайте новый экземпляр ПО:

   - Установите новую версию ПО на отдельном сервере.
   - Создайте и настройте новый экземпляр ПО с чистой базой данных.
   - Подключите вспомогательные службы.
3. Проверьте работу нового экземпляра:

   - Выполните инициализацию и вход в систему.
   - Проверьте работу всех компонентов.
   - Убедитесь в отсутствии ошибок в журналах.
4. Перенесите данные со старого экземпляра:

   - Перенесите значения директив из старых файлов конфигурации в файлы конфигурации нового экземпляра.
   - Перенесите базу данных в новый экземпляр.
   - При необходимости выполните преобразование структуры данных.
   - Проверьте работу экземпляра ПО с перенесёнными данными.
   - Создайте резервную копию обновлённого экземпляра.
5. Переключите DNS или вышестоящий прокси-сервер на новый сервер:

   - Обновите DNS-записи и (или) конфигурацию вышестоящего прокси-сервера.
   - Проверьте работу системы.

## Подготовка данных старого экземпляра ПО к обновлению

Внимание!

Выполните подготовительные действия отдельно для каждого экземпляра ПО, версию которого требуется обновить.

1. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
2. Скопируйте базу данных экземпляра ПО во внешнее хранилище:

   ```
   cp /var/lib/comindware/<instanceName>/Database <database_backup_path>
   ```

   Здесь:

   - `<instanceName>` — имя экземпляра ПО.
   - `<database_backup_path>` — путь к внешнему хранилищу базы данных.
3. Скопируйте файлы конфигурации во внешнее хранилище:

   - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

   ```
   cd /var/www/<instanceName>/
   cp *.config *.yml *.json <config_backup_path>
   cp /var/www/<instanceName>/data/Plugins/Agent/Agent.config <config_backup_path>
   cp /etc/nginx/sites-available/comindware<instanceName> <config_backup_path>
   cp /etc/sysconfig/comindware<instanceName>-env <config_backup_path>
   ```

   - **РЕД ОС**, **Rocky** (RPM-based)

   ```
   cd /var/www/<instanceName>/
   cp *.config *.yml *.json <config_backup_path>
   cp /var/www/<instanceName>/data/Plugins/Agent/Agent.config <config_backup_path>
   cp /etc/nginx/conf.d/comindware<instanceName> <config_backup_path>
   cp /etc/sysconfig/comindware<instanceName>-env <config_backup_path>
   ```

   - **Альт Сервер**

   ```
   cd /var/www/<instanceName>/
   cp *.config *.yml *.json <config_backup_path>
   cp /var/www/<instanceName>/data/Plugins/Agent/Agent.config <config_backup_path>
   cp /etc/nginx/sites-available.d/comindware<instanceName> <config_backup_path>
   cp /etc/sysconfig/comindware<instanceName>-env <config_backup_path>
   ```

   Здесь `<config_backup_path>` — путь к внешнему хранилищу файлов конфигурации.

## Подготовка нового сервера

Выполните следующие инструкции на новом сервере:

1. На новом сервере скачайте и распакуйте дистрибутив с новой версией вспомогательного ПО (`X.X`, `<prerequisitesVersion>` — номер версии):

   ```
   cd <distPath>
   tar -xf X.X-release-ru-<prerequisitesVersion>.prerequisites.<osname>.tar.gz
   ```
2. Перейдите в распакованную директорию библиотек `librdkafka`:

   ```
   cd CMW_<osname>/repo/kafka/librd/
   ```
3. Обновите библиотеки `librdkafka`:

   - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

   ```
   dpkg -i *.deb
   ```

   - **РЕД ОС**, **Rocky** (RPM-based)

   ```
   rpm -i *.rpm
   ```

   - **Альт Сервер**

   ```
   apt-get install -y *.rpm
   ```
4. Скачайте и распакуйте дистрибутив с новой версией ПО (`X.X`, `<version>` — номер версии):

   ```
   cd <distPath>
   tar -xf X.X-release-ru-<version>.<osname>.tar.gz
   ```
5. Перейдите в распакованную директорию:

   ```
   cd CMW_<osname>_<version>/scripts/
   ```
6. Установите новую версию ПО:

   ```
   bash version_install.sh
   ```
7. Проверьте наличие и имя директории установленной версии ПО:

   ```
   bash version_list.sh
   ```
8. Отобразится список установленных версий ПО на сервере.

## Создание нового экземпляра

Выполните следующие инструкции на новом сервере.

1. Создайте новый экземпляр ПО:

   ```
   bash instance_create.sh -n=<instanceName> -p=<portNumber> -v=<version>
   ```

   Здесь:

   - `-n=<instanceName>` — имя экземпляра ПО;
   - `-p=<portNumber>` - порт для экземпляра ПО, по умолчанию: 80 (необязательный ключ);
   - `-v=<version>` — установленная версия ПО.
2. По окончании создания скрипт выведет информацию о компонентах экземпляра ПО. Удостоверьтесь, что компоненты успешно установлены.

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
   OK     Used version: <version>
   OK     Logs configured.
   OK     Sites created.
   OK     Sites enabled.
   OK     API Gateway configured.
   OK     Link to binaries is valid.
   OK     Instance service started.
   OK     Instance API gateway service started.
   OK     NGINX started.
   OK     Final status.
   [Done] Upgrade CBAP instance.
   ```

   Если какая-либо из служб имеет статус `FAILED`, перезапустите её, например:

   ```
   systemctl restart comindware<instanceName>.service
   systemctl restart apigateway<instanceName>.service
   systemctl restart adaperhost<instanceName>.service
   systemctl restart kafka.service
   systemctl restart elasticsearch.service
   ```
3. Отредактируйте конфигурацию NGINX для экземпляра ПО в соответствии с резервной копией, [сохранённой ранее](#upgrade_version_linux_no_stop_old_instance_data_prepare):

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
4. Перезапустите службу NGINX для применения изменений:

   ```
   nginx -s reload
   ```
5. Отредактируйте файлы конфигурации в соответствии с резервными копиями, [сохранёнными ранее](#upgrade_version_linux_no_stop_old_instance_data_prepare):

   ```
   nano /etc/sysconfig/comindware<instanceName>-env
   nano /var/www/<instanceName>/adapterhost.yml
   nano /var/www/<instanceName>/apigateway.yml
   nano /var/www/<instanceName>/Ignite.config
   nano /usr/share/comindware/configs/instance/<instanceName>.yml
   ```

   Внимание!

   - В новейших версиях **{{ productName }}** отсутствует файл `Workers.config`.
   - Настройка соответствующих служб выполняется в файле конфигурации экземпляра ПО `<instanceName>.yml`.
6. Перезапустите сервисы, настройки которых были изменены, например:

   ```
   systemctl restart apigateway<instanceName> comindware<instanceName>
   ```
7. Откройте сайт экземпляра ПО в браузере, одновременно открыв выдачу журналов экземпляра в терминале:

   ```
   tail -f /var/log/comindware/<instanceName>/Log/heartbeat*
   ```
8. В браузере выполните инициализацию экземпляра ПО, выполните вход и проверьте работоспособность ПО.

## Перенос данных

Выполните следующие инструкции на новом сервере.

1. Остановите новый экземпляр ПО:

   ```
   systemctl stop comindware<instanceName>
   ```
2. Удалите базу данных нового экземпляра ПО:

   ```
   rm -r /var/lib/comindware/<instanceName>/Database/
   ```
3. Скопируйте базу данных старого экземпляра ПО в новый экземпляр:

   ```
   cp -r /path/to/backup/Database/* /var/lib/comindware/<instanceName>/Database/
   ```
4. Откройте сайт экземпляра ПО в браузере.
5. Дождитесь завершения обновления структуры данных и проверьте его успешное выполнение.

   Внимание!

   При обновлении с версии 4.7.2 на версии 4.7.3-5.0 обновляется структура базы данных.

   После этого необходимо вручную удалить некоторые данные кэша в старом формате.

   Поэтому продолжать обновление версии экземпляра ПО можно только после успешного обновления структуры данных.

   - Удостоверьтесь, что появились журналы обновления:
     - `/var/log/comindware/<instanceName>/Log/UpgradeOntology.log`
     - `/var/log/comindware/<instanceName>/Log/upgrade<ГГГГ-ММ-ДД>.log`
   - Удостоверьтесь, что в журнале `UpgradeOntology.log` последняя запись содержит строку `Upgrade of ontology completed successfully`.
   - Удостоверьтесь, что в журнале `upgrade<ГГГГ-ММ-ДД>.log` последняя запись содержит строку `Upgrade completed`.
   - Удостоверьтесь, что в журналах отсутствуют ошибки обновления. Найдите их по ключевому слову `error`.
   - Если обновление выполнено успешно, переходите к шагу 6.
   - Если в журнале обновления имеются ошибки:

     1. Не переходите к шагу 6.
     2. Снова установите для экземпляра старую версию ПО.
     3. Восстановите базу данных из резервной копии.
     4. Обратитесь в службу поддержки **Comindware**, предоставив журналы обновления и ошибок для анализа.
6. Создайте резервную копию экземпляра ПО:

   - в формате `.CDBBZ` средствами **{{ productName }}**;

     или
   - c помощью скрипта для создания снимка базы.
7. Остановите экземпляр ПО.
8. Распакуйте резервную копию и удалите из неё следующие директории кэшей:

   ```
   rm -rf cacheGroup-*-TableIdentity
   rm -rf cacheGroup-*-TableIdentityReplicated
   rm -rf cacheGroup-*Value
   rm -rf cacheGroup-*ValueReplicated
   rm -rf cache-ignite-sys-cache
   rm -rf cp
   rm -rf metastorage
   rm -rf cacheGroup-Keys
   ```
9. Очистите директорию с базой данных экземпляра ПО:

   ```
   rm -rf /var/lib/comindware/<instanceName>/Database/*
   ```
10. Скопируйте очищенную резервную копию в директорию с базой данных `/var/lib/comindware/<instanceName>/Database/`.
11. Назначьте владельца директории с базой данных:

    - **Astra Linux, Ubuntu, Debian** (DEB-based)

    ```
    chown -R www-data:www-data /var/lib/comindware/<instanceName>/Database
    ```

    - **РЕД ОС, Rocky** (RPM-based)

    ```
    chown -R nginx:nginx /var/lib/comindware/<instanceName>/Database
    ```

    - **Альт Сервер**

    ```
    chown -R _nginx:_nginx /var/lib/comindware/<instanceName>/Database
    ```
12. Запустите экземпляр ПО.
13. Откройте сайт экземпляра ПО в браузере, дождитесь его инициализации и выполните вход.

## Переключение на новый экземпляр

1. Подготовьте инфраструктуру к переключению на новый IP-адрес:

   - сохраните резервную копию конфигурации DNS и (или) прокси-сервера;
   - подготовьте DNS-записи для используемого доменного имени;
   - подготовьте вышестоящий прокси-сервер для использования нового IP-адреса;
   - проверьте доступность нового IP-адреса, например с помощью утилит `ping` и `telnet`;
   - настройте сетевой экран на использование нового IP-адреса.
2. Выполните переключение:

   - **DNS:**
     - уменьшите TTL в конфигурации DNS за несколько часов до переключения, чтобы ускорить переключение;
     - обновите DNS-записи типа A на новый IP-адрес.
   - **Вышестоящий прокси-сервер:**
     - смените IP-адрес старого экземпляра на новый;
     - проверьте синтаксис новой конфигурации.
3. Проверьте доступность системы:

   - убедитесь, что система доступна по доменному имени из разных сетей;
   - проверьте работу всех основных функций;
   - проконтролируйте отсутствие ошибок в журналах;
   - проверьте время отклика системы;
   - проверьте обновление записей на всех DNS-серверах через `nslookup`;
   - верните исходные значения TTL в конфигурации DNS.

## Действия при возникновении проблем

1. При обнаружении ошибок в журналах обновления:

   - не продолжайте обновление;
   - верните DNS-записи и IP-адреса, указывающие на старый сервер;
   - восстановите исходную конфигурацию DNS и прокси-сервера;
   - сохраните все журналы ошибок;
   - задокументируйте обнаруженные проблемы;
   - если устранить проблему самостоятельно не удаётся, обратитесь в службу поддержки **Comindware**.
2. При проблемах после переключения:

   - верните DNS-записи и IP-адреса, указывающие на старый сервер;
   - восстановите исходную конфигурацию DNS и прокси-сервера;
   - при необходимости восстановите экземпляр ПО из резервной копии;
   - проанализируйте журналы ошибок и сетевые журналы;
   - задокументируйте обнаруженные проблемы;
   - если устранить проблему самостоятельно не удаётся, обратитесь в службу поддержки **Comindware**.

--8<-- "related_topics_heading.md"

- *[Обновление версии экземпляра ПО с его остановкой][upgrade_version_linux]*
- *[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]*
- *[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]*
- *[Подсистема журналирования][logging_engine]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
