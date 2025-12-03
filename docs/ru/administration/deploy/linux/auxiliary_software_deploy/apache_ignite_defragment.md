---
title: Apache Ignite. Дефрагментация данных
kbId: 4603
---

# Apache Ignite. Дефрагментация данных {: #apache_ignite_defragment}

## Введение

Здесь представлены инструкции по дефрагментации хранилища данных Apache Ignite для ПО **{{ productName }}** в Linux. Дефрагментация хранилища Apache Ignite позволяет повысить производительность работы ПО и сократить объем данных хранилища на диске.

!!! warning "Внимание!"

    Во время дефрагментации хранилища Apache Ignite экземпляр ПО будет недоступен. Поэтому дефрагментацию следует выполнять в нерабочее время.

## Порядок дефрагментации

1. Создайте резервную копию базы данных экземпляра ПО.
2. Скачайте бинарный дистрибутив Apache Ignite, например [apache-ignite-2.17.0-bin.zip](https://downloads.apache.org/ignite/2.17.0/apache-ignite-2.17.0-bin.zip) или более новую версию.
3. Перейдите в режим суперпользователя:


    --8<-- "linux_sudo.md"

4. Распакуйте дистрибутив Apache Ignite в домашнюю папку (здесь и далее `username` — имя текущего пользователя):

    ``` sh
    unzip apache-ignite-2.17.0-bin.zip -d /usr/share/ignite
    ```

5. Задайте переменную среды `IGNITE_HOME`:

    ``` sh
    export IGNITE_HOME=/usr/share/ignite
    ```

6. Скопируйте в папку `/usr/share/ignite` файл `Ignite.config` из папки `/var/www/<instanceName>` (где `<instanceName>` — имя экземпляра ПО):

    ``` sh
    cp /var/www/<instanceName>/Ignite.config /usr/share/ignite/
    ```

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

7. Перейдите в папку `bin` Apache Ignite:

    ``` sh
    cd /usr/share/ignite/bin
    ```

8. В файле `control.sh` измените директиву `DEFAULT_CONFIG`:

    ``` sh
    DEFAULT_CONFIG=config/Ignite.config
    ```

9. Получите список узлов, зарегистрированных в базовой топологии:

    ``` sh
    bash control.sh --baseline
    ```

10. Назначьте дефрагментацию данных Apache Ignite при перезапуске экземпляра ПО, указав вместо `<id>` идентификаторы узлов, полученные на шаге 9:

    ``` sh
    bash control.sh --defragmentation schedule --nodes <id>
    ```
11. Остановите и запустите экземпляр ПО:

    ``` sh
    systemctl stop comindware<instanceName>
    systemctl start comindware<instanceName>

    ```

    Здесь `<instanceName>` — имя экземпляра ПО.

12. Инициируйте экземпляр ПО:

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

13. Дождитесь завершения дефрагментации данных.

    !!! note "Примечание"

        - В процессе дефрагментации для просмотра статуса используйте команду:
        
        ```
        watch -cd bash control.sh --defragmentation status
        ```

        - В процессе дефрагментации Apache Ignite будет вносить сведения в файл журнала вида `/var/lib/comindware/<instanceName>/Database/log/ignite-xxxxxxxx.0.log`. 
        - По завершении дефрагментации:
            - в журнале Apache Ignite должно появиться событие: `Defragmentation process complete`;
            - команда  `watch -cd bash control.sh --defragmentation status` должна вывести сообщение `Defragmentation process complete`.

14. Перезапустите экземпляр ПО, чтобы его снова можно было использовать.

    ``` sh
    systemctl restart comindware<instanceName>
    ```

15. Инициируйте экземпляр ПО, также как на шаге 12.

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
    DefaultLimitNOFILE=65536
    ```

5. Раскомментируйте строку и задайте значение в файле `/etc/systemd/system.conf`:

    ```
    DefaultLimitNOFILE=65536
    ```

6. Откройте для редактирования конфигурацию сервиса экземпляра ПО:

    ```  sh
    systemctl edit comindware<instanceName>.service
    ```

7. Добавьте в него строки:

    ```  sh
    [Service]
    LimitNOFILE=65536
    LimitNOFILESoft=65536
    ```

8. Перезагрузите машину и экземпляр ПО.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Резервное копирование и восстановление][backup_configure]_
- _[Дефрагментация персистентного хранилища](https://ignite.apache.org/docs/2.11.1/persistence/native-persistence-defragmentation)_ (руководство Apache Ignite, английский язык)
- _[Активация, деактивация и управление топологией](https://ignite.apache.org/docs/2.11.1/tools/control-script#activation-deactivation-and-topology-management)_ (руководство Apache Ignite, английский язык)

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
