---
title: 'Apache Ignite. Дефрагментация данных'
kbId: 4603
url: 'https://kb.comindware.ru/article.php?id=4603'
updated: '2025-12-22 12:20:20'
---

# Apache Ignite. Дефрагментация данных

## Введение

Здесь представлены инструкции по дефрагментации хранилища данных Apache Ignite для ПО **Comindware Platform** в Linux. Дефрагментация хранилища Apache Ignite позволяет повысить производительность работы ПО и сократить объем данных хранилища на диске.

Внимание!

Во время дефрагментации хранилища Apache Ignite экземпляр ПО будет недоступен. Поэтому дефрагментацию следует выполнять в нерабочее время.

## Порядок дефрагментации

1. Создайте резервную копию базы данных экземпляра ПО.
2. Скачайте бинарный дистрибутив Apache Ignite, например [apache-ignite-2.17.0-bin.zip](https://downloads.apache.org/ignite/2.17.0/apache-ignite-2.17.0-bin.zip) или более новую версию.
3. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
4. Распакуйте дистрибутив Apache Ignite в домашнюю директорию (здесь и далее `username` — имя текущего пользователя):

   ```
   unzip -q apache-ignite-2.17.0-bin.zip -d /usr/share/ignite
   ```
5. Задайте переменную среды `IGNITE_HOME`:

   ```
   export IGNITE_HOME=/usr/share/ignite/apache-ignite-2.17.0-bin
   ```
6. Задайте переменную среды `IGNITE_CONTROL_UTILITY_USE_CONNECTOR_CONNECTION`:

   ```
   export IGNITE_CONTROL_UTILITY_USE_CONNECTOR_CONNECTION=true
   ```
7. Перейдите в директорию `bin` Apache Ignite:

   ```
   cd /usr/share/ignite/apache-ignite-2.17.0-bin/bin
   ```
8. Получите список узлов, зарегистрированных в базовой топологии:

   ```
   bash control.sh --baseline
   ```

   Пример списка узлов в базовой конфигурации```
   root@NODE1:/usr/share/ignite/apache-ignite-slim-2.17.0-bin/bin# export IGNITE_HOME=/usr/share/ignite/apache-ignite-slim-2.17.0-bin/
   root@NODE1:/usr/share/ignite/apache-ignite-slim-2.17.0-bin/bin# cd apache-ignite-slim-2.17.0-bin/bin/
   root@NODE1:/usr/share/ignite/apache-ignite-slim-2.17.0-bin/bin# bash control.sh --baseline
   Control utility [2.17.0]
   User: root
   Time: 2025-12-04T11:43:07.505

   [BASELINE]
   Arguments: --baseline

   Cluster state: ACTIVE
   Current topology version: 1
   Baseline auto adjustment enabled: softTimeout=3000
   Baseline auto-adjust are not scheduled

   Current topology version: 1
   Coordinator: ConsistentId=a06ff4bf-3a28-4b6c-a66a-323bca97a8e0, Address=localhost/127.0.0.1, Order=1

   Baseline nodes:
   ConsistentId=a06ff4bf-3a28-4b6c-a66a-323bca97a8e0, Address=localhost/127.0.0.1, State=ONLINE, Order=1

   Number of baseline nodes: 1

   Other nodes not found.

   Command [BASELINE] finished with code: 0
   Time: 2025-12-04T11:43:07.839
   Execution time: 334 ms
   ```
9. Назначьте дефрагментацию данных Apache Ignite при перезапуске экземпляра ПО, указав вместо `<id>` идентификаторы узлов (ConsistentId), полученные на шаге 9:

   ```
   bash control.sh --defragmentation schedule --nodes <id>
   ```
10. Остановите и запустите экземпляр ПО:

    ```
    systemctl stop comindware<instanceName>
    systemctl start comindware<instanceName>
    ```

    Здесь `<instanceName>` — имя экземпляра ПО.
11. Инициализируйте экземпляр ПО:

    - С помощью командной строки:

      ```
      curl localhost:<port>
      ```

      или

      ```
      curl <instance_fqdn>
      ```
    - Либо с помощью браузера, перейдя по адресу:

      ```
      <ip>:<port>
      ```

      или

      ```
      <instance_fqdn>
      ```

    Здесь:

    - `<instance_ip>, <port>` — IP-адрес и порт экземпляра ПО;
    - `<instance_fqdn>` — адрес веб-сайта с экземпляром ПО.
12. Дождитесь завершения дефрагментации данных.

    Примечание

    - В процессе дефрагментации для просмотра статуса используйте команду:

    ```
    watch -cd bash control.sh --defragmentation status
    ```

    - В процессе дефрагментации Apache Ignite будет вносить сведения в файл журнала вида `/var/log/comindware/<instanceName>/Logs/igniteClient_xxxxxxxx.log`.
    - По завершении дефрагментации:
      - в журнале Apache Ignite должно появиться событие: `Defragmentation process complete`;
      - команда  `watch -cd bash control.sh --defragmentation status` должна вывести сообщение `Defragmentation process complete`.
13. Перезапустите экземпляр ПО, чтобы его снова можно было использовать.

    ```
    systemctl restart comindware<instanceName>
    ```
14. Инициализируйте экземпляр ПО, также как на шаге 12.

## Решение возможных проблем

Если во время дефрагментации возникнет ошибка *«Слишком много открытых файлов»* (*Too many open files*), выполните указанные ниже шаги (пример приведён для Astra Linux).

1. Добавьте в файл `/etc/security/limits.conf` строки:

   ```
   * soft nproc 65535
   * hard nproc 65535
   * soft nofile 65535
   * hard nofile 65535
   www-data soft nproc 200000
   www-data hard nproc 200000
   www-data soft nofile 200000
   www-data hard nofile 200000
   ```
2. Добавьте в файл `/etc/pam.d/common-session` строку:

   ```
   session required pam_limits.so
   ```
3. Добавьте в файл `/etc/sysctl.conf` строку:

   ```
   fs.file-max = 2097152
   ```
4. Раскомментируйте строку и задайте значение в файле `/etc/systemd/user.conf`:

   ```
   DefaultLimitNOFILE=200000
   ```
5. Раскомментируйте строку и задайте значение в файле `/etc/systemd/system.conf`:

   ```
   DefaultLimitNOFILE=200000
   ```
6. Откройте для редактирования конфигурацию сервиса экземпляра ПО:

   ```
   systemctl edit comindware<instanceName>.service
   ```
7. Добавьте в него строки:

   ```
   [Service]
   LimitNOFILE=200000
   LimitNOFILESoft=200000
   ```
8. Перезагрузите машину и экземпляр ПО.

## Связанные статьи

- [Резервное копирование и восстановление](https://kb.comindware.ru/article.php?id=4642)
- [Дефрагментация персистентного хранилища (руководство Apache Ignite, английский язык)](https://ignite.apache.org/docs/2.11.1/persistence/native-persistence-defragmentation)
- [Активация, деактивация и управление топологией (руководство Apache Ignite, английский язык)](https://ignite.apache.org/docs/2.11.1/tools/control-script#activation-deactivation-and-topology-management)