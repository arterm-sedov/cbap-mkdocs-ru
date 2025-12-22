---
title: 'Apache Ignite. Дефрагментация данных'
kbId: 4603
tags:
    - Apache Ignite
    - Linux
    - дефрагментация
    - оптимизация хранилища
    - производительность
hide: tags
---

# {{ apacheIgniteVariants }}. Дефрагментация данных {: #apache_ignite_defragment}

## Введение

Здесь представлены инструкции по дефрагментации хранилища данных {{ apacheIgniteVariants }} для ПО **{{ productName }}** в Linux. Дефрагментация хранилища {{ apacheIgniteVariants }} позволяет повысить производительность работы ПО и сократить объем данных хранилища на диске.

!!! warning "Внимание!"

    Во время дефрагментации хранилища {{ apacheIgniteVariants }} экземпляр ПО будет недоступен. Поэтому дефрагментацию следует выполнять в нерабочее время.

## Порядок дефрагментации

1. Создайте резервную копию базы данных экземпляра ПО.
2. Скачайте бинарный дистрибутив {{ apacheIgniteVariants }}, например [apache-ignite-2.17.0-bin.zip](https://downloads.apache.org/ignite/2.17.0/apache-ignite-2.17.0-bin.zip) или более новую версию.
3. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

4. Распакуйте дистрибутив {{ apacheIgniteVariants }} в домашнюю директорию (здесь и далее `username` — имя текущего пользователя):

    ``` sh
    unzip -q apache-ignite-2.17.0-bin.zip -d /usr/share/ignite
    ```

5. Задайте переменную среды `IGNITE_HOME`:

    ``` sh
    export IGNITE_HOME=/usr/share/ignite/apache-ignite-2.17.0-bin
    ```

6. Задайте переменную среды `IGNITE_CONTROL_UTILITY_USE_CONNECTOR_CONNECTION`:

    ``` sh
    export IGNITE_CONTROL_UTILITY_USE_CONNECTOR_CONNECTION=true
    ```

7. Перейдите в директорию `bin` {{ apacheIgniteVariants }}:

    ``` sh
    cd /usr/share/ignite/apache-ignite-2.17.0-bin/bin
    ```

8. Получите список узлов, зарегистрированных в базовой топологии:

    ``` sh
    bash control.sh --baseline
    ```

    ``` sh title="Пример списка узлов в базовой конфигурации"
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

9. Назначьте дефрагментацию данных {{ apacheIgniteVariants }} при перезапуске экземпляра ПО, указав вместо `<id>` идентификаторы узлов (ConsistentId), полученные на шаге 9:

    ``` sh
    bash control.sh --defragmentation schedule --nodes <id>
    ```

10. Остановите и запустите экземпляр ПО:

    ``` sh
    systemctl stop comindware<instanceName>
    systemctl start comindware<instanceName>

    ```

    Здесь `<instanceName>` — имя экземпляра ПО.

11. Инициализируйте экземпляр ПО:

    - С помощью командной строки:

        ``` sh
        curl localhost:<port>
        ```

        или

        ``` sh
        curl <instance_fqdn>
        ```

    - Либо с помощью браузера, перейдя по адресу:

        ``` sh
        <ip>:<port>
        ```

        или

        ``` sh
        <instance_fqdn>
        ```

    Здесь:

    - `<instance_ip>, <port>` — IP-адрес и порт экземпляра ПО;
    - `<instance_fqdn>` — адрес веб-сайта с экземпляром ПО.

12. Дождитесь завершения дефрагментации данных.

    !!! note "Примечание"

        - В процессе дефрагментации для просмотра статуса используйте команду:
        
        ```
        watch -cd bash control.sh --defragmentation status
        ```

        - В процессе дефрагментации {{ apacheIgniteVariants }} будет вносить сведения в файл журнала вида `/var/log/comindware/<instanceName>/Logs/igniteClient_xxxxxxxx.log`. 
        - По завершении дефрагментации:
            - в журнале {{ apacheIgniteVariants }} должно появиться событие: `Defragmentation process complete`;
            - команда  `watch -cd bash control.sh --defragmentation status` должна вывести сообщение `Defragmentation process complete`.

13. Перезапустите экземпляр ПО, чтобы его снова можно было использовать.

    ``` sh
    systemctl restart comindware<instanceName>
    ```

14. Инициализируйте экземпляр ПО, также как на шаге 12.

## Решение возможных проблем {: .pageBreakBefore }

Если во время дефрагментации возникнет ошибка _«Слишком много открытых файлов»_ (_Too many open files_), выполните указанные ниже шаги (пример приведён для Astra Linux).

1. Добавьте в файл `/etc/security/limits.conf` строки:

    ``` sh
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

    ``` sh
    session required pam_limits.so
    ```

3. Добавьте в файл `/etc/sysctl.conf` строку:

    ``` sh
    fs.file-max = 2097152
    ```

4. Раскомментируйте строку и задайте значение в файле `/etc/systemd/user.conf`:

    ```  sh
    DefaultLimitNOFILE=200000
    ```

5. Раскомментируйте строку и задайте значение в файле `/etc/systemd/system.conf`:

    ``` sh
    DefaultLimitNOFILE=200000
    ```

6. Откройте для редактирования конфигурацию сервиса экземпляра ПО:

    ```  sh
    systemctl edit comindware<instanceName>.service
    ```

7. Добавьте в него строки:

    ```  sh
    [Service]
    LimitNOFILE=200000
    LimitNOFILESoft=200000
    ```

8. Перезагрузите машину и экземпляр ПО.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Резервное копирование и восстановление][backup_configure]
- [Дефрагментация персистентного хранилища  (руководство Apache Ignite, английский язык)](https://ignite.apache.org/docs/2.11.1/persistence/native-persistence-defragmentation)
- [Активация, деактивация и управление топологией (руководство Apache Ignite, английский язык)](https://ignite.apache.org/docs/2.11.1/tools/control-script#activation-deactivation-and-topology-management)

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
