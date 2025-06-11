---
title: 'Установка, запуск, инициализация и остановка ПО'
kbId: 4622
---

# Установка, запуск, инициализация и остановка ПО {: #deploy_guide_linux }

## Введение {: #deploy_guide_linux_intro }

Для работы **{{ productName }}** требуются операционная система, сервер базы данных, веб-сервер, обратный прокси-сервер и сервер журналов.

Для быстрого развёртывания **{{ productName }}** в Linux компания **{{ companyName }}** предоставляет дистрибутив с установщиком, настраивающим необходимое программное обеспечение. См. _[{{ productName }} {{ productVersion }}. Перечень стороннего программного обеспечения для Linux][auxiliary_software_list]_.

Здесь представлены инструкции по развёртыванию и инициализации **{{ productName }}** из дистрибутива в ОС Linux.

{% include-markdown ".snippets/deploy_traffic_filter_admonition.md" %}

## Порядок развёртывания ПО {{ productName }} {: #deploy_guide_linux_order }

1. Установите и настройте необходимое вспомогательное ПО.
2. Установите ПО **{{ productName }}**.
3. Создайте экземпляр ПО.
4. Запустите экземпляр ПО.
5. Инициализируйте экземпляр ПО.

### Требования к внешним службам

Для работы **{{ productName }}** необходимо развернуть следующие внешние службы:

- сервер журналирования транзакций {{ openSearchVariants }};
- сервер брокера сообщений {{ apacheKafkaVariants }}.

Установите и настройте это ПО согласно следующим инструкциям:

- _[Elasticsearch. Установка в Linux][elasticsearch_deploy_Linux]_
- _[Apache Kafka. Установка в Linux][kafka_deploy_linux]_

## Установка вспомогательного ПО {: #deploy_guide_linux_prerequisites_install }

Прежде чем приступать к установке вспомогательного ПО, необходимого для работы **{{ productName }}**, ознакомьтесь с демонстрационным роликом и инструкциями, представленными ниже.

### Видеоинструкция {: #deploy_guide_linux_prerequisites_install_video }

[Ссылка на видеоролик](https://kb.comindware.ru/platform/v5.0/administration/deploy/linux/img/deploy_guide_linux_auxiliary_software.mp4)

<video controls="controls" width="100%" height="100%">
<source src="https://kb.comindware.ru/platform/v5.0/administration/deploy/linux/img/deploy_guide_linux_auxiliary_software.mp4" type="video/mp4" />
</video>

### Порядок установки вспомогательного ПО {: #deploy_guide_linux_prerequisites_install_order }

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Скачайте и распакуйте дистрибутив с вспомогательным ПО **{{ productName }}**, полученный по ссылке от компании **{{ companyName }}** (`X.X`, `<versionNumber>` — номер версии ПО, `<osname>` — название операционной системы):

    ``` sh
    tar -xf X.X-release-ru-<versionNumber>.prerequisites.<osname>.tar.gz
    ```

    !!! tip "Совет"

        После распаковки архив можно удалить для экономии места:

        ``` sh
        rm -f X.X-release-ru-<versionNumber>.prerequisites.<osname>.tar.gz
        ```

3. Перейдите в директорию со скриптами для развёртывания вспомогательного ПО:

    ``` sh
    cd <prerequisitesDistPath>/CMW_<osname>/scripts
    ```

    Здесь:  `<prerequisitesDistPath>/CMW_<osname>/` — путь к распакованному дистрибутиву со вспомогательным ПО.

4. Установите ПО из дистрибутива:

    ``` sh
    sh prerequisites_install.sh -p [-k] {% if openSearchKey %}[-o]{% else %}[-e]{% endif %}
    ```

    Скрипт `prerequisites_install.sh` поддерживает следующие ключи:
    {: .pageBreakBefore }

    - `-p` — установить обязательное вспомогательное ПО.
    {% if openSearchKey %}
    - `-o` — установить службу OpenSearch (необязательный ключ).
    {% else %}
    - `-e` — установить службу Elasticsearch (необязательный ключ).
    {% endif %}
    - `-k` — установить службу Kafka (необязательный ключ).
    - `-kc` — установить клиент Apache Kafka (необязательный ключ).
    - `-kh=<hostname>` или `--kafkaHost=<hostname>` — использовать указанный хост для подключения к ПО Kafka (необязательный ключ).
    - `-kp=<portNumber>` или `--kafkaPort=<portNumber>` — использовать указанный порт для подключения к ПО Kafka (необязательный ключ).
    - `-h` — вызов краткой справки по использованию скрипта (указывать только без остальных ключей).

    !!! note "Примечание"

        Скрипт `prerequisites_install.sh` устанавливает необходимые для **{{ productName }}** компоненты, включая Java, .NET, Mono, {{ nginxVariants }}.

    !!! tip "Вызов справки для скриптов"

        Для ознакомления с ключами и назначением любого скрипта используйте ключ `-h` без каких-либо других ключей, например:

        ``` sh
        sh prerequisites_install.sh -h
        ```

5. По окончании установки скрипт выведет информацию об установленных компонентах. Удостоверьтесь, что компоненты успешно установлены (имеют статус `OK`).

    Пример результата выполнения скрипта с ключом `-p` без установки {{ openSearchVariants }} и Kafka:

    ``` sh
    [Done] Creating CBAP Data Dir.
    -----------------------------------------
    Environment details
    Status     | Software   | Version   
    -----------------------------------------
    OK         | mono       | 6.12.0.200     
    OK         | dotnet     | 6.0.417        
    OK         | java       | 17.0.7            
    OK     NGINX installed.
    OK     NGINX started.
    OK     CBAP version folder created.
    OK     CBAP configs folder created.
    OK     CBAP data folder created.
    OK     CBAP logs folder created.
    OK     CBAP dotnet folder created.
    OK     Local elasticsearch server installed: No 
    OK     Local elasticsearch server started: No 
    OK     Local kafka server installed: No 
    OK     Local kafka server started: No 
    OK     Final status.
    ```

6. Удостоверьтесь, что компоненты установлены:

    ``` sh
    sh prerequisites_list.sh
    ```

## Установка ПО {{ productName }} {: #deploy_guide_linux_install_sw }

Прежде чем приступать к установке ПО **{{ productName }}**, ознакомьтесь с видеороликом и инструкциями, представленными ниже.

### Видеоинструкция {: #deploy_guide_linux_install_sw_video }

[Ссылка на видеоролик](https://kb.comindware.ru/platform/v5.0/administration/deploy/linux/img/deploy_guide_linux_software.mp4)

<video controls="controls" width="100%" height="100%">
<source src="https://kb.comindware.ru/platform/v5.0/administration/deploy/linux/img/deploy_guide_linux_software.mp4" type="video/mp4" />
</video>

### Порядок установки ПО {{ productName }} {: #deploy_guide_linux_install_order }

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Скачайте и распакуйте дистрибутив ПО **{{ productName }}**, полученный по ссылке от компании **{{ companyName }}**:

    ``` sh
    tar -xf X.X-release-ru-<versionNumber>.<osname>.tar.gz
    ```

    !!! tip "Совет"

        После распаковки архив можно удалить для экономии места:

        ``` sh
        rm -f X.X-release-ru-<versionNumber>.<osname>.tar.gz
        ```

3. Перейдите в директорию со скриптами для развёртывания ПО:
{: #install_sh}

    ``` sh
    cd <distPath>/CMW_<osname>_<versionNumber>/scripts
    ```

    Здесь:  `<distPath>/CMW_<osname>_<versionNumber>/` — путь к распакованному дистрибутиву со ПО **{{ productName }}**.

4. Установите ПО из дистрибутива:

    ``` sh
    sh version_install.sh
    ```

    !!! note "Если отобразится запрос на перезагрузку ОС"

        - Выполните перезагрузку:

            ``` sh
            reboot
            ```

        - После перезагрузки:
            - перейдите в режим суперпользователя;
            - заново запустите [установку ПО из дистрибутива (шаг 3)](#install_sh).

5. После успешного завершения установки подождите 3–5 минут. Этого времени обычно достаточно для автоматического запуска и инициализации установленных служб (в зависимости от конфигурации машины).
6. Удостоверьтесь, что ПО установлено, просмотрев список установленных версий ПО:

    ``` sh
    sh version_list.sh
    ```

## Создание экземпляра ПО {: #deploy_guide_linux_instance_create .pageBreakBefore }

Прежде чем приступать к установке экземпляра ПО **{{ productName }}**, ознакомьтесь с видеороликом и инструкциями, представленными ниже.

### Видеоинструкция

[Ссылка на видеоролик](https://kb.comindware.ru/platform/v5.0/administration/deploy/linux/img/deploy_guide_linux_instance.mp4)

<video controls="controls" width="100%" height="100%">
<source src="https://kb.comindware.ru/platform/v5.0/administration/deploy/linux/img/deploy_guide_linux_instance.mp4" type="video/mp4" />
</video>

### Подготовка к созданию экземпляра ПО {: #deploy_guide_linux_instance_create_prepare }

Перед созданием экземпляра ПО проверьте конфигурацию Linux и при необходимости внесите в неё перечисленные ниже изменения.

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Откройте для редактирования файл `limits.conf`:

    ``` sh
    nano /etc/security/limits.conf
    ```

3. Установите следующие директивы:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

    ``` systemd
    www-data soft nproc 200000
    www-data hard nproc 200000
    www-data soft nofile 200000
    www-data hard nofile 200000
    ```

    - **РЕД ОС**, **Rocky** (RPM-based)

    ``` systemd
    nginx soft nproc 200000
    nginx hard nproc 200000
    nginx soft nofile 200000
    nginx hard nofile 200000
    ```

    - **Альт Сервер**

    ``` systemd
    _nginx soft nproc 200000
    _nginx hard nproc 200000
    _nginx soft nofile 200000
    _nginx hard nofile 200000
    ```

4. Откройте файл `common-session` для редактирования:

    ``` sh
    nano /etc/pam.d/common-session
    ```

5. Установите следующую директиву:

    ``` systemd
    session required pam_limits.so
    ```

6. Откройте файл `sysctl.conf` для редактирования:

    ``` sh
    nano /etc/sysctl.conf
    ```

7. Установите следующие директивы:

    ``` cs
    fs.file-max=2097152
    vm.max_map_count=262144
    fs.inotify.max_user_instances=524288
    ```

    !!! tip "Оптимальное значение vm.max_map_count"

        Значение `vm.max_map_count=262144` приведено для примера.

        Определите оптимальное значение `vm.max_map_count` согласно инструкциям в параграфе «[Настройка параметра vm.max_map_count](#оптимизация-параметра-vmmax_map_count)».

8. Откройте файл `user.conf` для редактирования:

    ``` sh
    nano /etc/systemd/user.conf
    ```

9. Установите следующую директиву:

    ``` cs
    DefaultLimitNOFILE=200000
    ```

10. Откройте файл `system.conf` для редактирования:

    ``` sh
    nano /etc/systemd/system.conf
    ```

11. Установите следующую директиву:

    ``` cs
    DefaultLimitNOFILE=200000
    ```

12. После внесения изменений перезапустите демоны:

    ``` sh
    sysctl -p
    systemctl daemon-reexec
    ```

### Создание единственного экземпляра ПО {: #deploy_guide_linux_instance_create_single .pageBreakBefore }

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Перейдите в директорию со скриптами для развёртывания ПО **{{ productName }}**:

    ``` sh
    cd <distPath>/CMW_<osname>_<versionNumber>/scripts
    ```

    Здесь:  `<distPath>/CMW_<osname>_<versionNumber>/` — путь к распакованному дистрибутиву ПО.

3. Разверните экземпляр ПО:

    ``` sh
    sh instance_create.sh -n=<instanceName> -v=<versionNumber> [-p=<portNumber>]
    ```

    Скрипт `instance_create.sh` поддерживает следующие ключи:

    - `-n=<instanceName>` — имя экземпляра ПО (**обязательный** ключ).
    - `-v=<versionNumber>` — номер версии ПО вида `X.X.XXXXX.X` (например: 5.0.00000.0, **обязательный** ключ). Версия должна быть установлена, см. _«[Установка {{ productName }}](#deploy_guide_linux_install_sw)»_.
    - `-p=<portNumber>` — порт для экземпляра ПО, по умолчанию: 80 (необязательный ключ).
    - `-fqdn=<hostName>` или `--instance-fqdn=<hostName>` — имя хоста для экземпляра ПО (необязательный ключ). По умолчанию: localhost.
    - `-el=<hostName>` или `--elasticsearch-url=<hostName>` — использовать указанный URL или IP-адрес для подключения к серверу {{ openSearchVariants }}.
    - `-kf=<hostName>` или `--kafka-url=<hostName>` — использовать указанный URL или IP-адрес для подключения к серверу {{ apacheIgniteVariants }}.
    - `-h` — вызов краткой справки по использованию скрипта (указывать только без остальных ключей).

4. По окончании установки скрипт выведет информацию об установленных компонентах. Удостоверьтесь, что компоненты успешно установлены (имеют статус `OK`).

    Пример результата выполнения скрипта:

    ``` sh
    OK     Instance folder created.
    OK     Instance Web config created.
    OK     Instance Ignite config created.
    OK     Instance binaries linked.
    OK     Instance config created.
    OK     Data folder created.
    OK     Database folder created: No 
    OK     Streams folder created: No 
    OK     Logs folder created: Yes
    OK     Used version: 5.0.0000.0
    OK     Logs configured.
    OK     Sites created.
    OK     Sites enabled.
    OK     API Gateway configured.
    OK     Link to binaries is valid.
    OK     Instance service started.
    OK     Instance API gateway service started.
    OK     Instance adapter host service started.
    OK     NGINX started.
    OK     Final status.
    [Done] Creating a new CBAP instance.
    ```

5. Удостоверьтесь, что была создана директория с файлами конфигурации экземпляра ПО.

    ``` sh
    ls -lhF /var/www/<instanceName>/
    ```

6. По выводу команды `ls` удостоверьтесь, что в путях указана корректная версия ПО, например `5.0.0000.0`:

    ``` sh
    lrwxrwxrwx. 1 nginx nginx   36 Oct 11 17:54 bin -> /var/www/.cmw_version/5.0.0000.0/bin/
    lrwxrwxrwx. 1 nginx nginx   41 Oct 11 17:54 compiled -> /var/www/.cmw_version/5.0.0000.0/compiled/
    lrwxrwxrwx. 1 nginx nginx   37 Oct 11 17:54 data -> /var/www/.cmw_version/5.0.0000.0/data/
    lrwxrwxrwx. 1 nginx nginx   44 Oct 11 17:54 favicon.ico -> /var/www/.cmw_version/5.0.0000.0/favicon.ico
    lrwxrwxrwx. 1 nginx nginx   44 Oct 11 17:54 Global.asax -> /var/www/.cmw_version/5.0.0000.0/Global.asax
    lrwxrwxrwx. 1 nginx nginx   39 Oct 11 17:54 mobile -> /var/www/.cmw_version/5.0.0000.0/mobile/
    lrwxrwxrwx. 1 nginx nginx   46 Oct 11 17:54 redirect.aspx -> /var/www/.cmw_version/5.0.0000.0/redirect.aspx
    lrwxrwxrwx. 1 nginx nginx   42 Oct 11 17:54 resources -> /var/www/.cmw_version/5.0.0000.0/resources/
    lrwxrwxrwx. 1 nginx nginx   43 Oct 11 17:54 robots.txt -> /var/www/.cmw_version/5.0.0000.0/robots.txt
    lrwxrwxrwx. 1 nginx nginx   45 Oct 11 17:54 unauthorized -> /var/www/.cmw_version/5.0.0000.0/unauthorized/
    ```

### Создание дополнительного экземпляра ПО {: #deploy_guide_linux_instance_create_multiple .pageBreakBefore }

На одном сервере можно развернуть несколько экземпляров ПО **{{ productName }}**. Для создания второго и последующих экземпляров ПО выполните указанные ниже действия.

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Просмотрите список имеющихся экземпляров ПО **{{ productName }}**:

    ``` sh
    cat /usr/share/comindware/configs/instance/* | grep -E '(configPath:)'
    ```

3. Просмотрите список используемых портов:

    ``` sh
    ss -tunlp
    ```

    Также можно узнать, используется ли определённый порт (`<portNumber>`):

    ``` sh
    ss -tunlp | grep :<portNumber>
    ```

4. Просмотрите список установленных версий ПО:

    ``` sh
    ls /var/www/.cmw_version/
    ```

5. Создайте новый экземпляр ПО согласно приведённым выше [инструкциям](#deploy_guide_linux_instance_create_single), указав для него **уникальные имя и порт**.
6. Откройте для редактирования три службы **каждого** из установленных экземпляров ПО (`<instanceName>`):

    ``` sh
    nano /usr/lib/systemd/system/comindware<instanceName>.service
    nano /usr/lib/systemd/system/apigateway<instanceName>.service
    nano /usr/lib/systemd/system/adapterhost<instanceName>.service
    ```

7. Если используются локальные службы Kafka и {{ openSearchVariants }}, откройте их для редактирования:

    ``` sh
    nano /usr/lib/systemd/system/kafka.service
    nano /usr/lib/systemd/system/elasticsearch.service
    ```

8. В каждом файле службы установите следующие директивы:

    ``` cs
    # Макс. количество открытых файлов
    LimitNOFILE=200000
    # Макс. количество процессов
    LimitNPROC=8192
    ```

## Запуск экземпляра ПО {: #deploy_guide_linux_instance_start .pageBreakBefore }

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Удостоверьтесь, что основные службы установлены, запущены и имеют статус `Active (running)`:

    ``` sh
    systemctl status apigateway<instanceName>
    systemctl status adapterhost<instanceName>
    systemctl status comindware<instanceName>
    ```

3. Если какая-либо служба не работает, запустите её:

    ``` sh
    systemctl start apigateway<instanceName>
    systemctl start adapterhost<instanceName>
    systemctl start comindware<instanceName>
    ```

4. Выполните инициализацию ПО.

[](){: #instance_initialize }
## Инициализация {{ productName }} {: #deploy_guide_linux_initialize .pageBreakBefore }

<!--initialize-start-->
1. Запустите веб-браузер и в адресной строке введите URL-адрес, на котором был развёрнут экземпляр ПО:

    ``` sh
    http://<instanceHost>:<portNumber>
    ```

2. Дождитесь запуска и отображения веб-сайта **{{ productName }}**, что может занять примерно 5 минут.
3. Откроется страница создания аккаунта администратора **{{ productName }}**.

    _![Страница создания аккаунта администратора](img/deploy_guide_admin_account_create.png)_

4. Введите учётные данные аккаунта администратора и нажмите кнопку «**Создать аккаунт**».

    !!! warning "Внимание!"

        - В **{{ productName }}** всегда должен оставаться хотя бы один аккаунт администратора. Он может потребоваться для восстановления системы.
        - Аккаунт администратора, созданный при инициализации экземпляра ПО, не следует удалять, даже если впоследствии аккаунты будут синхронизироваться с Active Directory.

5. При необходимости откроется страница активации ПО. Выполните **онлайновую** или **ручную активацию** либо нажмите кнопку «**Пропустить**» для первоначального ознакомления с ПО без активации.
6. При необходимости откроется страница настройки подключения к службе {{ openSearchVariants }}.

    - В поле «**URI**» введите адрес сервера {{ openSearchVariants }}, например: `http://<openSearchHost>:<opeSearchPort>`.
    - При необходимости введите **имя пользователя** и **пароль** {{ openSearchVariants }}.
    - Установите уникальный **префикс индекса**, например `mycompanyprefix`.
    - Экземпляр ПО будет взаимодействовать с {{ openSearchVariants }} под указанным пользователем и создавать, наполнять и читать индексы с заданным префиксом.
    - Нажмите кнопку «**Далее**».

7. При необходимости откроется страница инициализации данных в {{ openSearchVariants }}.

    _![Страница инициализации данных в {{ openSearchVariants }}](img/deploy_guide_elasticsearch_initialize.png)_

8. Нажмите кнопку «**Обновить**».
9. Дождитесь открытия начальной страницы **{{ productName }}**.
10. На этом этапе развертывание экземпляра **{{ productName }}** завершено.
11. Подготовьте экземпляр к разработке приложений.

<!--initialize-end-->

## Подготовка экземпляра ПО к разработке приложений {: #deploy_guide_linux_instance_prepare .pageBreakBefore }

<!--instance-prepare-start-->

Прежде чем вносить какие-либо изменения, создавать и использовать приложения, настройте резервное копирование и возможность восстановления паролей. Это позволит обеспечить работоспособность **{{ productName }}** в долгосрочной перспективе.

1. Создайте резервную копию созданного экземпляра **{{ productName }}**:

    - Создайте конфигурацию резервного копирования по расписанию.
    - Запустите резервное копирование вручную, чтобы создать первую резервную копию чистого экземпляра ПО.

    См. _«[Резервное копирование. Настройка, запуск и просмотр журнала сеансов][backup_configure]»_.

2. Настройте подключение к почтовому серверу для отправки писем для сброса пароля и двухфакторной аутентификации:

    - Создайте подключение типа «**Отправка эл.&nbsp;почты из процесса**».
    - Установите в свойствах подключения флажок «**Использовать по умолчанию**».
    - **Отправьте тестовое сообщение**, чтобы удостовериться в работоспособности подключения.
    - Не настраивайте путь передачи данных и процесс. Это не требуется для отправки уведомлений.

    См. _«[Отправка почты из процесса. Настройка подключения][process_sending_connection]»_.

3. Снова запустите резервное копирование вручную, чтобы создать резервную копию работоспособного экземпляра ПО.
4. Теперь можно приступать к созданию приложений на основе **{{ productName }}**.

<!--instance-prepare-end-->

## Оптимизация параметра vm.max_map_count

`vm.max_map_count` — это параметр конфигурации ядра Linx, задающий максимальное количество областей памяти, которые процессу разрешено выделять в своём виртуальном адресном пространстве.

Типовое для **{{ productName }}** значение параметра `vm.max_map_count` равно `262144`.

Чтобы определить оптимальное для вашей конфигурации значение `vm.max_map_count`, выполните указанные ниже инструкции.

Например, оптимизировать `vm.max_map_count` может потребоваться, если после запуска экземпляра ПО команда `journalctl` выдаёт ошибку следующего вида:

```d
mmap(PROT_NONE) failed
```

1. Определите текущее значение `vm.max_map_count`:

    ```sh
    sudo sysctl vm.max_map_count
    ```

2. Определите выделенный объём оперативной памяти:

    ```sh
    free
    ```

    Обратите внимание на общий объём оперативной памяти.

3. Определите размер страницы в оперативной памяти:

    ``` sh
    declare -i NEW_max_map_count=$(vmstat -s | grep -i 'total memory' | awk ' {print $1}')*1024/$(getconf PAGE_SIZE)
    echo $NEW_max_map_count
    ```

4. Полученное значение `NEW_max_map_count` временно присвойте параметру `vm.max_map_count` и проверьте работу экземпляра ПО:

    - Временное изменение значения (например, для тестирования):

    ```sh
    sudo sysctl -w vm.max_map_count=$NEW_max_map_count
    ```

5. Удостоверившись в работоспособности экземпляра ПО, задайте постоянное значение `vm.max_map_count`:

    - Откройте для редактирования файл `/etc/sysctl.conf`:

        ```sh
        sudo nano /etc/sysctl.conf
        ```

    - Установите значение `vm.max_map_count`:

        ``` cs
        vm.max_map_count=<NEW_max_map_count>
        ```

        `<NEW_max_map_count>` замените на полученное на шаге 3 цифровое значение.

    - Примените изменения:

        ``` sh
        sysctl -p
        ```

## Остановка экземпляра ПО {: .pageBreakBefore }

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Перед тем как выполнять любые действия с файлами ПО и базы данных, остановите службы, поддерживающие работу ПО:

    ``` sh
    systemctl stop comindware<instanceName>
    systemctl stop apigateway<instanceName>
    systemctl stop adapterhost<instanceName>
    ```

3. Удостоверьтесь, что службы остановлены:

    ``` sh
    systemctl status comindware<instanceName>
    systemctl status apigateway<instanceName>
    systemctl status adapterhost<instanceName>
    ```

## Удаление версии и экземпляра ПО

Прежде чем приступать к удалению версии и экземпляра ПО **{{ productName }}**, ознакомьтесь с видеороликом и инструкциями, представленными ниже.

### Видеоинструкция

[Ссылка на видеоролик](https://kb.comindware.ru/platform/v5.0/administration/deploy/linux/img/deploy_guide_linux_delete_version_instance.mp4)

<video controls="controls" width="100%" height="100%">
<source src="https://kb.comindware.ru/platform/v5.0/administration/deploy/linux/img/deploy_guide_linux_delete_version_instance.mp4" type="video/mp4" />
</video>

### Удаление экземпляра ПО {: .pageBreakBefore }

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Остановите экземпляр ПО согласно [инструкции](#остановка-экземпляра-по).
3. Перейдите в директорию со скриптами для развёртывания ПО **{{ productName }}**:

    ``` sh
    cd <distPath>/CMW_<osname>_<versionNumber>/scripts
    ```

4. Запустите удаление экземпляра ПО:

    ``` sh
    sh instance_delete.sh -n=<instanceName>
    ```

    Скрипт `delete.sh` поддерживает следующие ключи:

    - `-n=<instanceName>` — удалить экземпляр ПО с указанным именем (**обязательный** ключ).
    - `--deleteData` — безвозвратно удалить все файлы базы данных экземпляра ПО (необязательный ключ). Удаляются файлы, а директория экземпляра ПО остаётся, её можно удалить вручную.
    - `--deleteLogs` — безвозвратно удалить директорию со всеми файлами журналов экземпляра ПО (необязательный ключ).
    - `--deleteBackups` — безвозвратно удалить все резервные копии экземпляра ПО (необязательный ключ).
    - `-h` — вызов краткой справки по использованию скрипта (указывать только без остальных ключей).

5. Удостоверьтесь, что экземпляр ПО был успешно удалён, просмотрев список установленных экземпляров ПО:

    ``` sh
    sh instance_list.sh
    ```

### Удаление версии ПО {: #deploy_guide_linux_delete_version .pageBreakBefore }

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Просмотрите список экземпляров ПО с указанием версий:

    ``` sh
    sh instance_list.sh
    ```

3. Удалите все экземпляры с версией ПО, которую требуется удалить, или обновите их до другой версии. Удалить версию ПО, которая используется в каких-либо экземплярах, не удастся. См. _«[Удаление экземпляра ПО](#удаление-экземпляра-по)»_.
4. Перейдите в директорию со скриптами для развёртывания ПО **{{ productName }}**:

    ``` sh
    cd <distPath>/CMW_<osname>_<versionNumber>/scripts
    ```

5. Просмотрите список установленных версий ПО:

    ``` sh
    sh version_list.sh
    ```

6. Удалите версию ПО:

    ``` sh
    sh version_delete.sh -v=<versionNumber>
    ```

    Здесь: `-v=<versionNumber>` — укажите номер версии ПО вида `X.X.XXXX.X` (например: `5.0.0000.0`).

7. Проверьте, что версия ПО была удалена успешно:

    ``` sh
    sh version_list.sh
    ```

    или

    ``` sh
    ls /var/www/.cmw_version
    ```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Пути и содержимое директорий экземпляра ПО][paths]
- [Обновление версии экземпляра ПО с его остановкой][upgrade_version_linux]
- [Обновление версии экземпляра ПО без его остановки][upgrade_version_linux_no_stop]
- [Резервное копирование. Настройка, запуск и просмотр журнала сеансов][backup_configure]
- [Отправка почты из процесса. Настройка подключения][process_sending_connection]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
