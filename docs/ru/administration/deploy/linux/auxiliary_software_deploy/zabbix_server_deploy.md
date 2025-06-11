---
title: Zabbix Server, Zabbix Agent, Zabbix Frontend и MySQL. Установка и настройка
kbId: 4607
---

# Zabbix Server, Zabbix Agent, Zabbix Frontend и MySQL. Установка и настройка {: #zabbix_server_deploy}

## Введение

Здесь представлены инструкции по установке сервера и агентов Zabbix, используемых для мониторинга работы **{{ productName }}**, развёрнутой на одной или нескольких виртуальных или физических машинах.

*Zabbix Server* можно развернуть только на Linux-машине, здесь приведён пример установки и конфигурирования на Ubuntu 22.04 LTS. В работе *Zabbix Server* использует СУБД MySQL, либо PostgreSQL. Здесь представлены настройки для MySQL.

*Zabbix Agent* можно установить на машину под управлением ОС Windows или Linux. Здесь представлены краткие инструкции по установке и настройке агента на машине с Ubuntu 22.04 LTS и установленным сервером Zabbix. Инструкции по установке Zabbix Agent на отдельной машине см. в статье «[Zabbix Agent. Инструкции по установке][zabbix_agent_deploy]».

## Установка  Zabbix Server

1. Для работы *Zabbix Server* необходимо установить NGINX:

    ``` sh
    sudo apt install -y nginx
    ```

2. Загрузите deb-пакет из репозитория:

    ``` sh
    sudo wget <https://repo.zabbix.com/zabbix/6.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.0-4%2Bubuntu22.04_all.deb>
    sudo dpkg -i zabbix-release_6.0-4+ubuntu22.04_all.deb
    sudo apt update
    ```

3. Установите *Zabbix Server*, *Zabbix Frontend* и *Zabbix Agent*:

    ``` sh
    sudo apt install -y zabbix-server-mysql zabbix-frontend-php zabbix-nginx-conf zabbix-sql-scripts zabbix-agent
    ```

## Установка и конфигурация MySQL {: .pageBreakBefore }

1. Установите и активируйте MySQL:

    ``` sh
    sudo apt install -y mysql-server
    sudo systemctl enable --now mysql
    ```

2. Запустите MySQL от имени суперпользователя root:

    ``` sh
    sudo mysql
    ```

3. После входа в консоль MySQL выполните запрос, подставив свои значения в поля `'root'`,`'localhost'` и `'password'`:

    ``` sh
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
    ```

4. Ожидаемый ответ консоли MySQL с подтверждением внесённых изменений:

    ``` sh
    Query OK, 0 rows affected (0.01 sec)
    ```

5. Выйдите из сеанса для пользователя root :

    ``` sh
    quit;
    ```

6. Запустите скрипт `mysql_secure_installation` и в интерактивном режиме согласитесь удалить тестовую базу данных и аккаунт анонимного пользователя:

    ``` { .sh .pageBreakAfter title="Удаление анонимного пользователя MySQL" }
    /usr/bin/mysql_secure_installation

    Securing the MySQL server deployment.

    Enter password for user root: <password-here>

    VALIDATE PASSWORD COMPONENT can be used to test passwords
    and improve security. It checks the strength of password
    and allows the users to set only those passwords which are
    secure enough. Would you like to setup VALIDATE PASSWORD component?

    Press y|Y for Yes, any other key for No: n

    Using existing password for root.

    Change the password for root ? (Press y|Y for Yes, any other key for No) : n
    {% if pdfOutput %}
    ```

    ``` {: .sh title="Удаление анонимного пользователя MySQL — продолжение" .pageBreakBefore }
    {% endif %}
    By default, a MySQL installation has an anonymous user,
    allowing anyone to log into MySQL without having to have
    a user account created for them. This is intended only for
    testing, and to make the installation go a bit smoother.
    You should remove them before moving into a production
    environment.

    Remove anonymous users? (Press y|Y for Yes, any other key for No) : y

    Normally, root should only be allowed to connect from
    'localhost'. This ensures that someone cannot guess at
    the root password from the network.
    Disallow root login remotely? (Press y|Y for Yes, any other key for No) : n
    By default, MySQL comes with a database named 'test' that
    anyone can access. This is also intended only for testing,
    and should be removed before moving into a production
    environment.

    Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y

    Reloading the privilege tables will ensure that all changes
    made so far will take effect immediately.

    Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y

    Success.
    All done!
    ```

## Создание базы данных для Zabbix в MySQL {: .pageBreakBefore }

1. Начните сеанс пользователя `root` в MySQL:

    ``` sh
    mysql -uroot -p
    ```

2. Создайте базу данных `zabbix`:

    ``` sh
    create database zabbix character set utf8mb4 collate utf8mb4_bin;
    ```

3. Создайте пользователя `zabbix`. Не забудьте задать пароль:

    ``` sh
    create user zabbix@localhost identified by 'password';
    grant all privileges on zabbix.* to zabbix@localhost;
    SET GLOBAL log_bin_trust_function_creators = 1;
    quit;
    ```

4. Создайте схему данных для Zabbix:

    ``` sh
    zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -uzabbix -p zabbix
    ```

5. Введите пароль пользователя zabbix для доступа к MySQL, заданный на шаге 3.3., и дождитесь завершения выполнения скрипта.

## Настройка Zabbix Server

1. Откройте файл конфигурации `zabbix_server.conf` с помощью текстового редактора, например:

    ``` sh
    sudo nano /etc/zabbix/zabbix_server.conf
    ```

2. Укажите пароль пользователя zabbix (заданный на шаге 3.3) для доступа к MySQL:

    ``` sh
    ### Option: DBPassword
    #       Database password.
    #       Comment this line if no password is used.
    #
    # Mandatory: no
    # Default:
    # DBPassword=
    DBPassword=password
    ```

3. Сохраните изменения и выйдите.

## Настройка Zabbix Frontend {: .pageBreakBefore }

1. Отредактируйте `/etc/zabbix/nginx.conf` :

    ``` sh
    sudo nano /etc/zabbix/nginx.conf
    ```

2. Раскомментируйте директивы `listen` и `server_name` и присвойте им значения:

    ``` sh
    listen 8080;
    server_name <hostname>; # замените на своё имя хоста
    ```

3. Запустите службы *Zabbix Server, Zabbix Agent, Zabbix Frontend* и *NGINX*:

    ``` sh
    sudo systemctl daemon-reload
    sudo systemctl enable --now zabbix-server zabbix-agent nginx php8.1-fpm
    ```

## Использование Zabbix Frontend

1. Для доступа к *Zabbix Frontend* перейдите по адресу `http://machine-ip-address:8080`:

    _![Начальная страница Zabbix Frontend](https://kb.comindware.ru/assets/img_63af06de4faf0.png)_

2. Удостоверьтесь, что конфигурация сервера была применена успешно:

    _![Проверка конфигурации Zabbix Server](https://kb.comindware.ru/assets/img_63af06ef8c0a2.png)_

3. Настройте строки подключения к базе данных MySQL:

    _![Настройка подключения Zabbix к БД MySQL](https://kb.comindware.ru/assets/img_63af06fa36a3e.png)_

4. Задайте имя Zabbix Server, настройте часовой пояс и тему Zabbix Frontend:

    _![Настройка имени и часового пояса Zabbix Server](https://kb.comindware.ru/assets/img_63af0705eb46f.png)_

    _![Завершение установки Zabbix Frontend](https://kb.comindware.ru/assets/img_63af071cc182b.png)_

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

5. В открывшейся форме ведите учётные данные встроенного суперпользователя:

    ``` sh
    Admin
    zabbix
    ```

    _![Вход в Zabbix Frontend](https://kb.comindware.ru/assets/img_63af07227b847.png)_

## Настройка службы Zabbix Agent {: .pageBreakBefore }

!!! note "Примечание"

    Следующие шаги предназначены исключительно для настройки мониторинга ресурсов машины с установленным Zabbix Server.

    Для установки и настройки Zabbix Agent на сторонние машины используйте соответствующие инструкции. См. статью «[Zabbix Agent. Инструкции по установке][zabbix_agent_deploy]».

1. Отредактируйте файл конфигурации `/etc/zabbix/zabbix_agentd.conf`:

    ``` sh
    sudo nano /etc/zabbix/zabbix_agentd.conf
    ```

2. В файле конфигурации необходимо указать IP-адрес *Zabbix Server*. Если сервер развёрнут на наблюдаемой машине укажите IP-адрес 127.0.0.1 (если интерфейс loopback не настроен иначе):

    ``` sh
    ### Option: Server
    #       List of comma delimited IP addresses, optionally in CIDR notation, or DNS names of Zabbix ser>
    #       Incoming connections will be accepted only from the hosts listed here.
    #       If IPv6 support is enabled then '127.0.0.1', '::127.0.0.1', '::ffff:127.0.0.1' are treated eq>
    #       and '::/0' will allow any IPv4 or IPv6 address.
    #       '0.0.0.0/0' can be used to allow any IPv4 address.
    #       Example: Server=127.0.0.1,192.168.1.0/24,::1,2001:db8::/32,zabbix.<hostname>
    #
    # Mandatory: yes, if StartAgents is not explicitly set to 0
    # Default:
    # Server=your.server.ip.address
    Server=127.0.0.1
    ```

3. Отредактируйте директиву `ServerActive`:

    ``` sh
    ServerActive=127.0.0.1
    ```

4. Разрешите в сетевом экране использование порта 10050:

    ``` sh
    sudo ufw allow 10050/tcp
    ```

5. Примените изменения:

    ``` sh
    sudo systemctl daemon-reload
    sudo ufw reload
    ```

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

6. Запустите *Zabbix Agent* и добавьте его в список автозагрузки:

    ``` sh
    sudo systemctl enable  --now zabbix-agent
    ```

7. Удостоверьтесь, что служба работает:

    ``` sh
    systemctl status zabbix.agent
    ```

_![Ожидаемый статус сервиса Zabbix Agent](https://kb.comindware.ru/assets/img_63af05a8d77f5.png)_

## Добавление Linux-хоста в сеть мониторинга

Добавление агента в сеть мониторинга выполняется аналогично разделу 4. «Добавление Linux-хоста в сеть мониторинга» инструкции «Zabbix Agent. Инструкции по установке для Ubuntu 22.04». При настройке используйте IP-адрес интерфейса loopback (127.0.0.1).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
