---
title: 'Обновление версии экземпляра ПО с его остановкой'
kbId: 4624
tags:
    - установка
    - развертывание
    - обновление
    - апгрейд
    - сервисы
    - кафка
    - linux
    - nginx
    - администрирование
    - инициализация
    - конфигурация
    - скрипты
    - база данных
    - резервное копирование
    - экземпляр
hide: tags
---

# Обновление версии экземпляра ПО с его остановкой {: #upgrade_version_linux }

## Введение {: #upgrade_version_linux_introduction }

Здесь представлены инструкции по обновлению версии экземпляра ПО **{{ productName }}** на одном и том же сервере с остановкой экземпляра.

Инструкции даны для обновления с версии 4.7.2 и выше на версию 5.0 в ОС Linux.

!!! tip "Совет"

    Этот способ можно использовать, если ПО **{{ productName }}** развёрнуто на одной машине и нет возможности развернуть новую машину для экземпляра ПО новой версии. Если вы можете развернуть новую машину, то рекомендуется следовать инструкции _«[Обновление версии экземпляра ПО без его остановки][upgrade_version_linux_no_stop]»_.

## Порядок обновления версии экземпляра ПО {: #upgrade_version_linux_update_procedure }

1. Подготовьте экземпляр ПО к обновлению:
    - Сохраните резервную копию экземпляра ПО.
    - Остановите экземпляр ПО.
    - Сохраните конфигурацию экземпляра ПО и вспомогательных служб.
    - Удалите компоненты старой версии ПО.
    - Переместите директорию с базой данных экземпляра ПО в резервную директорию.
2. Обновите версию ПО для экземпляра:
    - Скачайте и распакуйте два дистрибутива: вспомогательного ПО и новой версии ПО.
    - Удостоверьтесь, что все компоненты вспомогательного ПО установлены корректно.
    - При необходимости обновите или установите вспомогательное ПО.
    - Установите новую версию ПО.
    - Удалите экземпляр ПО старой версии.
    - Создайте экземпляр ПО новой версии.
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
3. Обновите конфигурацию ПО и служб:
    - Отредактируйте конфигурационные файлы в соответствии с ранее сохранёнными резервными копиями.
    - Перезапустите экземпляр ПО и вспомогательные службы.
4. Инициализируйте экземпляр ПО:
    - Выполните вход и проверьте работоспособность ПО.
    - Остановите экземпляр ПО.
    - Скопируйте в экземпляр ПО ранее перемещённую директорию с базой данных.
5. Обновите и проверьте структуру данных:
    - Запустите экземпляр ПО.
    - Обновите структуру данных до новой версии.
    - Очистите кэши.
    - Снова перезапустите экземпляр ПО.
6. Подготовьте восстановленный экземпляр ПО к работе.

## Подготовка экземпляра ПО к обновлению {: #upgrade_version_linux_preparation .pageBreakBefore }

!!! warning "Внимание!"

    Выполните подготовительные действия отдельно для каждого экземпляра ПО, версию которого требуется обновить.

1. Создайте и перенесите во внешнее хранилище резервную копию базы данных экземпляра ПО. См. _«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]»_.
2. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

3. Сохраните резервную копию файлов конфигурации, например в директорию `/var/backups/config_tmp`:
{: #NginxBackup}

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

    ``` sh
    mkdir -p /var/backups/config_tmp/
    cd /var/www/<instanceName>/
    cp *.config *.yml *.json /var/backups/config_tmp/
    cp /etc/nginx/sites-available/comindware<instanceName> /var/backups/config_tmp/
    cp /etc/sysconfig/comindware<instanceName>-env /var/backups/config_tmp/
    cp /usr/share/comindware/configs/instance/<instanceName>.yml /var/backups/config_tmp/
    ```

    - **РЕД ОС**, **Rocky** (RPM-based)

    ``` sh
    mkdir -p /var/backups/config_tmp/
    cd /var/www/<instanceName>/
    cp *.config *.yml *.json /var/backups/config_tmp/
    cp /etc/nginx/conf.d/comindware<instanceName> /var/backups/config_tmp/
    cp /etc/sysconfig/comindware<instanceName>-env /var/backups/config_tmp/
    cp /usr/share/comindware/configs/instance/<instanceName>.yml /var/backups/config_tmp/
    ```

    - **Альт Сервер**

    ``` sh
    mkdir -p /var/backups/config_tmp/
    cd /var/www/<instanceName>/
    cp *.config *.yml *.json /var/backups/config_tmp/
    cp /etc/nginx/sites-available.d/comindware<instanceName> /var/backups/config_tmp/
    cp /etc/sysconfig/comindware<instanceName>-env /var/backups/config_tmp/
    cp /usr/share/comindware/configs/instance/<instanceName>.yml /var/backups/config_tmp/
    ```

    Здесь `<instanceName>` — имя экземпляра ПО.

{% include-markdown ".snippets/pdfPageBreakHard.md" %}

4. Остановите экземпляр ПО и вспомогательные службы и удостоверьтесь, что они остановлены:

    ``` sh
    systemctl stop apigateway<instanceName> adapterhost<instanceName> comindware<instanceName>
    systemctl status apigateway<instanceName> adapterhost<instanceName> comindware<instanceName>
    ```

5. Удалите (или переместите в резервное хранилище) неиспользуемые предыдущие дистрибутивы ПО (`<distPath>` — путь к директории с дистрибутивом, `<osname>` — название операционной системы):

    ``` sh
    rm -rf <distPath>/CMW_<osname>
    ```

6. Переместите директорию с базой данных экземпляра ПО (`<username>` — имя пользователя Linux):
{: #ConfigBackup }

    ```sh
    mkdir -p /home/<username>/<instanceName>
    mv /var/lib/comindware/<instanceName> /home/<username>/
    ```

    {% include-markdown ".snippets/pdfEndOfBlockHack.md" %}

## Обновление версии ПО для экземпляра {: #upgrade_version_linux_instance_software_update .pageBreakBefore }

!!! warning "Внимание!"

    Если при обновлении [на шаге 23](#dataUpgrade) будут обнаружены ошибки, не продолжайте обновление, установите старую версию, восстановите экземпляр ПО из резервной копии и обратитесь в службу поддержки **{{ companyName }}**.

!!! note "Обновление нескольких экземпляров ПО"

    Выполните приведённые ниже шаги для каждого экземпляра ПО, версию которого требуется обновить, так как скрипт обновления выполняется отдельно для указанного экземпляра ПО.

    Установка вспомогательного ПО и дистрибутива с новой версией ПО осуществляется только при обновлении первого экземпляра ПО. При обновлении последующих экземплятов ПО на эту версию, повторять шаги 1-5 не требуется.

    После обновления всех экземпляров ПО для экономии места старую версию ПО можно удалить согласно инструкции _«[Удаление версии ПО][deploy_guide_linux_delete_version]»_.

1. Скачайте и распакуйте дистрибутив с новой версией вспомогательного ПО (`X.X`, `<prerequisitesVersion>` — номер версии):

    ``` sh
    cd <distPath>
    tar -xf X.X-release-ru-<prerequisitesVersion>.prerequisites.<osname>.tar.gz
    ```

2. Перейдите в директорию со скриптами для развёртывания вспомогательного ПО:

    ``` sh
    cd <prerequisitesDistPath>/CMW_<osname>/scripts
    ```

    Здесь:  `<prerequisitesDistPath>/CMW_<osname>/` — путь к распакованному дистрибутиву со вспомогательным ПО.

3. Убедитесь, что все компоненты установлены:

    ``` sh
    sh prerequisites_list.sh
    ```

    !!! warning "Внимание!"

        Если какой-то из компонентов не установлен или установлена старая версия, то установите вспомогательное ПО заново. См. _«[Установка вспомогательного ПО][deploy_guide_linux_prerequisites_install]»_.

4. Скачайте и распакуйте дистрибутив с новой версией ПО (`X.X`, `<version>` — номер версии):

    ``` sh
    cd <distPath>
    tar -xf X.X-release-ru-<version>.<osname>.tar.gz
    ```

5. Перейдите в распакованную директорию:

    ``` sh
    cd CMW_<osname>_<version>/scripts/
    ```

6. Установите новую версию ПО:

    ``` sh
    bash version_install.sh
    ```

7. Проверьте наличие и имя директории установленной версии ПО:

    ``` sh
    bash version_list.sh
    ```

8. Отобразится список установленных версий ПО на сервере.
9. Удалите экземпляр ПО старой версии и его данные:

    ```sh
    bash instance_delete.sh -n=<instanceName> --deleteData
    ```

10. Создайте экземпляр ПО новой версии:

    ``` sh
    bash instance_create.sh -n=<instanceName> -p=<portNumber> -v=<version>
    ```

    Здесь:

    - `-n=<instanceName>` — имя экземпляра ПО;
    - `-p=<portNumber>` - порт для экземпляра ПО, по умолчанию: 80 (необязательный ключ);
    - `-v=<version>` — установленная версия ПО.

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

11. По окончании создания скрипт выведет информацию о компонентах экземпляра ПО. Удостоверьтесь, что компоненты успешно установлены.

    Пример результата выполнения скрипта:

    ``` sh
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

    Если какая-либо из служб имеет статус `FAILED`, игнорируйте это и продолжайте выполнение следующих шагов согласно инструкции, так как устранять эти неполадки следует позже.

12. Обновите конфигурацию ПО и служб.

## Обновление конфигурации ПО и служб {: #upgrade_version_linux_config_edit .pageBreakBefore }

1. Отредактируйте конфигурацию NGINX для экземпляра ПО в соответствии с резервной копией, [сохранённой ранее](#NginxBackup):

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        nano /etc/nginx/sites-available/comindware<instanceName>
        ```

    - **РЕД ОС**, **Rocky** (RPM-based)

        ``` sh
        nano /etc/nginx/conf.d/comindware<instanceName>
        ```

    - **Альт Сервер**

        ``` sh
        nano /etc/nginx/sites-available.d/comindware<instanceName>
        ```

2. Перезапустите службу NGINX для применения изменений:

    ```sh
    nginx -s reload
    ```

3. Отредактируйте файлы конфигурации в соответствии с резервными копиями, [сохранёнными ранее](#ConfigBackup):

    ```sh
    nano /etc/sysconfig/comindware<instanceName>-env
    nano /var/www/<instanceName>/adapterhost.yml
    nano /var/www/<instanceName>/apigateway.yml
    nano /var/www/<instanceName>/Ignite.config
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

    !!! warning "Внимание!"

        - В новейших версиях **{{ productName }}** отсутствует файл `Workers.config`.
        - Настройка соответствующих служб выполняется в файле конфигурации экземпляра ПО `<instanceName>.yml`.

4. Перезапустите службы **{{ productName }}**:

    ``` sh
    systemctl restart adapterhost<instanceName>.service
    systemctl restart comindware<instanceName>.service
    systemctl restart apigateway<instanceName>.service
    ```

5. Инициализируйте экземпляра ПО.

## Инициализация экземпляра ПО {: #upgrade_version_linux_initialize .pageBreakBefore }

1. Откройте сайт экземпляра ПО в браузере, одновременно открыв выдачу журналов экземпляра в терминале:

    ``` sh
    tail -f /var/log/comindware/<instanceName>/Logs/heartbeat*
    ```

2. В браузере выполните инициализацию экземпляра ПО, выполните вход и проверьте работоспособность ПО.
3. Остановите экземпляр ПО:

    ``` sh
    systemctl stop comindware<instanceName>
    ```

4. Скопируйте в экземпляр ПО директорию с базой данных экземпляра ПО, сохранённую ранее (`<username>` — имя пользователя Linux):

    ```sh
    cp  -R /home/<username>/<instanceName>/Database /var/lib/comindware/<instanceName>/
    ```

5. Перейдите в папку с экземпляром ПО и поменяйте права для скопированной директории с базой данных:

    ```sh
    cd /var/lib/comindware/<instanceName>/
    chmod -R 777 Database/ 
    sudo chown -R www-data:www-data Database/
    ```

6. Обновите структуру данных.

## Обновление и проверка структуры данных {: #upgrade_version_linux_data_structure_update_and_verification .pageBreakBefore }

!!! warning "Обновление с версии 4.7 на версию 5.0"

    При обновлении с версии 4.7 на версию 5.0 обновляется структура базы данных.

    После этого необходимо вручную удалить некоторые данные кэша в старом формате.

    Поэтому продолжать обновление версии экземпляра ПО можно только после успешного обновления структуры данных. 

1. Запустите экземпляр ПО:

    ``` sh
    systemctl start comindware<instanceName>
    ```

2. Откройте сайт экземпляра ПО в браузере, дождитесь окончания загрузки, одновременно открыв выдачу журналов экземпляра в терминале:

    ``` sh
    tail -f /var/log/comindware/<instanceName>/Logs/heartbeat*
    ```

    См. _«[Подсистема журналирования][logging_engine]»_.

3. Дождитесь завершения обновления структуры данных:
{: #dataUpgrade }

    - Удостоверьтесь, что появились журналы обновления:
        - `/var/log/comindware/<instanceName>/Logs/UpgradeOntology.log`
        - `/var/log/comindware/<instanceName>/Logs/upgrade<ГГГГ-ММ-ДД>.log`
    - Удостоверьтесь, что в журнале `UpgradeOntology.log` последняя запись содержит строку `Upgrade of ontology completed successfully`.
    - Удостоверьтесь, что в журнале `upgrade<ГГГГ-ММ-ДД>.log` последняя запись содержит строку `Upgrade completed`.
    - Удостоверьтесь, что в журналах отсутствуют ошибки обновления. Найдите их по ключевому слову `error`.

{% include-markdown ".snippets/pdfPageBreakHard.md" %}

4. Проверьте результат обновления структуры данных.

    - **Если обновление структуры данных выполнено успешно:**

        - При обновлении с версии 5.0:
            - Обновление структуры данных завершено.
            - Переходите к [подготовке восстановленного экземпляра ПО к работе](#upgrade_version_linux_prepare).
        - При обновлении с версии 4.7 на версию 5.0:
            - Переходите к [шагу 5](#upgrade_version_linux_data_structure_update_and_verification_step5).

    - **Если в журнале обновления имеются ошибки:**

        - Не переходите к шагу 5.
        - Снова установите для экземпляра старую версию ПО.
        - Восстановите базу данных из резервной копии.
        - Обратитесь в службу поддержки **{{ companyName }}**, предоставив журналы обновления и ошибок для анализа.

5. Создайте резервную копию экземпляра ПО:
{: #upgrade_version_linux_data_structure_update_and_verification_step5}
    - в формате `.CDBBZ` средствами **{{ productName }}**;

        или

    - c помощью скрипта для создания снимка базы.

6. Остановите экземпляр ПО.
7. Распакуйте резервную копию и удалите из неё следующие директории кэшей:

    ``` sh
    rm -rf cacheGroup-*-TableIdentity
    rm -rf cacheGroup-*-TableIdentityReplicated
    rm -rf cacheGroup-*Value
    rm -rf cacheGroup-*ValueReplicated
    rm -rf cache-ignite-sys-cache
    rm -rf cp
    rm -rf metastorage
    rm -rf cacheGroup-Keys
    ```

8. Очистите директорию с базой данных экземпляра ПО:

    ``` sh
    rm -rf /var/lib/comindware/<instanceName>/Database/*
    ```

9. Скопируйте очищенную резервную копию в директорию с базой данных:

     ``` sh
     /var/lib/comindware/<instanceName>/Database/
     ```

{% include-markdown ".snippets/pdfPageBreakHard.md" %}

10.  Назначьте владельца директории с базой данных:

    - **Astra Linux, Ubuntu, Debian** (DEB-based)

    ``` sh
    chown -R www-data:www-data /var/lib/comindware/<instanceName>/Database
    ```

    - **РЕД ОС, Rocky** (RPM-based)

    ``` sh
    chown -R nginx:nginx /var/lib/comindware/<instanceName>/Database
    ```

    - **Альт Сервер**

    ``` sh
    chown -R _nginx:_nginx /var/lib/comindware/<instanceName>/Database
    ```

11.  Подготовьте восстановленный экземпляр ПО к работе.

## Подготовка восстановленного ПО к работе {: #upgrade_version_linux_prepare .pageBreakBefore }

1. Запустите экземпляр ПО.
2. Проверьте и при необходимости исправьте конфигурацию экземпляра ПО. См. _«[Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]»_.
3. Проверьте и работоспособность экземпляра ПО.
4. Создайте резервную копию работоспособного экземпляра **{{ productName }}**.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Обновление версии экземпляра ПО без его остановки][upgrade_version_linux_no_stop]
- [Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]
- [Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]
- [Подсистема журналирования][logging_engine]
- [Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
