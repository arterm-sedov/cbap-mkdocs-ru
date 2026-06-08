---
title: 'Установка, запуск, инициализация и остановка Comindware Business Application Platform'
kbId: 2344
url: 'https://kb.comindware.ru/article.php?id=2344'
updated: '2025-01-17 16:38:44'
---

# Установка, запуск, инициализация и остановка Comindware Business Application Platform

## Введение

Для работы **Comindware Business Application Platform** требуются операционная система, сервер базы данных, веб-сервер, обратный прокси-сервер и сервер журналов.

Для быстрого развёртывания **Comindware Business Application Platform** в Linux компания **Comindware** предоставляет дистрибутив с установщиком, настраивающим необходимое программное обеспечение. См. *[Comindware Business Application Platform 4.7. Перечень стороннего программного обеспечения для Linux](https://kb.comindware.ru/article.php?id=2398)*.

Здесь представлены инструкции по развёртыванию и инициализации **Comindware Business Application Platform** из дистрибутива в ОС Linux.

## Установка Comindware Business Application Platform

1. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
2. Скачайте и распакуйте дистрибутив **Comindware Business Application Platform**, полученный по ссылке от компании **Comindware** ( `X.X`, `<versionNumber>` — номер версии ПО, `<osname>` — название операционной системы):

   ```
   tar -xf X.X-release-ru-<versionNumber>.<osname>.tar.gz
   ```

   Совет

   По завершению распаковки архив можно удалить для экономии места:

   ```
   rm -f X.X-release-ru-<versionNumber>.<osname>.tar.gz
   ```
3. Перейдите в распакованную директорию:

   ```
   cd <distPath>/CMW_<osname>/
   ```

   Здесь: `<distPath>/CMW_<osname>/` — путь к распакованному дистрибутиву ПО.
4. Установите ПО из дистрибутива:

   ```
   sh install.sh -p [-k] [-e]
   ```

   Скрипт `install.sh` поддерживает следующие ключи:

   - `p` — установить ПО Comindware Business Application Platform.
   - `k` — установить ПО Kafka (необязательный ключ).
   - `e` — установить ПО Elasticsearch (необязательный ключ).
   - `h` — вызов краткой справки по использованию скрипта (указывать только без остальных ключей).

   Примечание

   Скрипт `install.sh` устанавливает ПО Comindware Business Application Platform и необходимые для него компоненты, включая Java, .NET, Mono, NGINX.

   Вызов справки для скриптов

   Для ознакомления с ключами и назначением любого скрипта используйте ключ `-h` без каких-либо других ключей, например:

   ```
   sh install.sh -h
   ```
5. По окончании установки скрипт выведет информацию об установленных компонентах. Удостоверьтесь, что компоненты успешно установлены.

   Пример результата выполнения скрипта с ключом `-p` без установки Elasticsearch и Kafka:

   ```
   Environment details
   Status     | Software   | Version
   -----------------------------------------
   OK         | mono       | 6.12.0.182
   OK         | dotnet     | 6.0.417
   OK         | java       | 17.0.7
   OK     NGINX installed.
   FAILED NGINX started.
   OK     CBAP version folder created.
   OK     CBAP configs folder created.
   FAILED CBAP data folder created.
   FAILED CBAP logs folder created.
   OK     CBAP dotnet folder created.
   OK     Local elasticsearch server installed: No
   OK     Local elasticsearch server started: No
   OK     Local kafka server installed: No
   OK     Local kafka server started: No
   FAILED Final status.
   ```

   Примечание

   В примере выше для большинства пунктов указан статус `OK`.

   При этом указан статус `FAILED` для `NGINX started`, `CBAP data folder created`, `CBAP logs folder created` и `Final status`.

   Это означает, что установлены необходимые компоненты, но не создан экземпляр ПО, то есть установка ПО выполнена успешно.

   Экземпляр ПО следует создать отдельно согласно инструкциям в параграфе *«[Создание экземпляра ПО](#создание-экземпляра-по)»*.
6. Если отобразится запрос на перезагрузку ОС, выполните перезагрузку:

   ```
   reboot
   ```

   После перезагрузки ОС заново запустите [установку ПО из дистрибутива (шаг 4)](#install.sh).
7. После успешного завершения установки подождите 3–5 минут. Этого времени обычно достаточно для автоматического запуска и инициализации установленных служб (в зависимости от конфигурации машины).
8. Удостоверьтесь, что ПО установлено, просмотрев список установленных версий ПО:

   ```
   ls /var/www/.cmw_version/
   ```

## Создание экземпляра ПО

### Подготовка к созданию экземпляра ПО

Перед созданием экземпляра ПО необходимо проверить конфигурацию Linux и при необходимости внести в неё перечисленные ниже изменения.

1. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
2. Откройте для редактирования файл `limits.conf`:

   ```
   nano /etc/security/limits.conf
   ```
3. Установите следующие директивы:

   - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

   ```
   www-data soft nproc 200000
   www-data hard nproc 200000
   www-data soft nofile 200000
   www-data hard nofile 200000
   ```

   - **РЕД ОС**, **Rocky** (RPM-based)

   ```
   nginx soft nproc 200000
   nginx hard nproc 200000
   nginx soft nofile 200000
   nginx hard nofile 200000
   ```

   - **Альт Сервер**

   ```
   _nginx soft nproc 200000
   _nginx hard nproc 200000
   _nginx soft nofile 200000
   _nginx hard nofile 200000
   ```
4. Откройте для редактирования файл `common-session`:

   ```
   nano /etc/pam.d/common-session
   ```
5. Установите следующую директиву:

   ```
   session required pam_limits.so
   ```
6. Откройте для редактирования файл `sysctl.conf`:

   ```
   nano /etc/sysctl.conf
   ```
7. Установите следующие директивы:

   ```
   fs.file-max=2097152
   vm.max_map_count=262144
   fs.inotify.max_user_instances=524288
   ```
8. Откройте для редактирования файл `user.conf`:

   ```
   nano /etc/systemd/user.conf
   ```
9. Установите следующую директиву:

   ```
   DefaultLimitNOFILE=200000
   ```
10. Откройте для редактирования файл `system.conf`:

    ```
    nano /etc/systemd/system.conf
    ```
11. Установите следующую директиву:

    ```
    DefaultLimitNOFILE=200000
    ```
12. После внесения изменений перезапустите демоны:

    ```
    sysctl -p
    systemctl daemon-reexec
    ```

### Создание единственного экземпляра ПО

1. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
2. Перейдите в директорию со скриптами для развёртывания ПО **Comindware Business Application Platform**:

   ```
   cd <distPath>/CMW_<osname>/scripts/instance
   ```

   Здесь: `<distPath>/CMW_<osname>/` — путь к распакованному дистрибутиву ПО.
3. Разверните экземпляр ПО:

   ```
   sh create.sh -n=<instanceName> -v=<versionNumber> [-p=<portNumber>]
   ```

   Скрипт `create.sh` поддерживает следующие ключи:

   - `-n=<instanceName>` — имя экземпляра ПО (**обязательный** ключ).
   - `-v=<versionNumber>` — номер версии ПО вида `X.X.XXXX.X` (например: 4.7.2222.0, **обязательный** ключ). Версия должна быть установлена, см. *«[Установка Comindware Business Application Platform](#deploy_guide_linux_install_sw)»*.
   - `-p=<portNumber>` — порт для экземпляра ПО, по умолчанию: 80 (необязательный ключ).
   - `-h` — вызов краткой справки по использованию скрипта (указывать только без остальных ключей).
4. Удостоверьтесь, что была создана директория с файлами конфигурации экземпляра ПО.

   ```
   ls -lhF /var/www/<instanceName>/
   ```
5. По ответу команды `ls` удостоверьтесь, что в путях указана верная версия ПО, например `4.7.3084.0`:

   ```
   lrwxrwxrwx. 1 nginx nginx   36 Oct 11 17:54 bin -> /var/www/.cmw_version/4.7.3084.0/bin/
   lrwxrwxrwx. 1 nginx nginx   41 Oct 11 17:54 compiled -> /var/www/.cmw_version/4.7.3084.0/compiled/
   lrwxrwxrwx. 1 nginx nginx   37 Oct 11 17:54 data -> /var/www/.cmw_version/4.7.3084.0/data/
   lrwxrwxrwx. 1 nginx nginx   44 Oct 11 17:54 favicon.ico -> /var/www/.cmw_version/4.7.3084.0/favicon.ico
   lrwxrwxrwx. 1 nginx nginx   44 Oct 11 17:54 Global.asax -> /var/www/.cmw_version/4.7.3084.0/Global.asax
   lrwxrwxrwx. 1 nginx nginx   39 Oct 11 17:54 mobile -> /var/www/.cmw_version/4.7.3084.0/mobile/
   lrwxrwxrwx. 1 nginx nginx   46 Oct 11 17:54 redirect.aspx -> /var/www/.cmw_version/4.7.3084.0/redirect.aspx
   lrwxrwxrwx. 1 nginx nginx   42 Oct 11 17:54 resources -> /var/www/.cmw_version/4.7.3084.0/resources/
   lrwxrwxrwx. 1 nginx nginx   43 Oct 11 17:54 robots.txt -> /var/www/.cmw_version/4.7.3084.0/robots.txt
   lrwxrwxrwx. 1 nginx nginx   45 Oct 11 17:54 unauthorized -> /var/www/.cmw_version/4.7.3084.0/unauthorized/
   ```

### Создание дополнительного экземпляра ПО

На одном сервере можно развернуть несколько экземпляров ПО **Comindware Business Application Platform**.

1. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
2. Просмотрите список имеющихся экземпляров ПО **Comindware Business Application Platform**:

   ```
   cat /usr/share/comindware/configs/instance/* | grep -E '(configPath:)'
   ```
3. Просмотрите список используемых портов:

   ```
   ss -tunlp
   ```

   Также можно узнать, используется ли определённый порт (`<portNumber>`):

   ```
   ss -tunlp | grep :<portNumber>
   ```
4. Просмотрите список установленных версий ПО:

   ```
   ls /var/www/.cmw_version/
   ```
5. Создайте новый экземпляр ПО согласно приведённым выше [инструкциям](#создание-экземпляра-по), указав для него уникальные имя и порт.
6. Откройте для редактирования три службы каждого из установленных экземпляров ПО (`<instanceName>`):

   ```
   nano /usr/lib/systemd/system/comindware<instanceName>.service
   nano /usr/lib/systemd/system/apigateway<instanceName>.service
   nano /usr/lib/systemd/system/adapterhost<instanceName>.service
   ```
7. Если используются локальные службы Kafka и Elasticsearch, откройте их для редактирования:

   ```
   nano /usr/lib/systemd/system/kafka.service
   nano /usr/lib/systemd/system/elasticsearch.service
   ```
8. В каждом файле службы установите следующие директивы:

   ```
   # Макс. количество открытых файлов
   LimitNOFILE=200000
   # Макс. количество процессов
   LimitNPROC=8192
   ```

## Запуск экземпляра ПО

1. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
2. Удостоверьтесь, что основные службы установлены, запущены и имеют статус `Active (running)`:

   ```
   systemctl status comindware<instanceName>
   systemctl status kafka
   systemctl status nginx
   systemctl status elasticsearch
   ```
3. Если какая-либо служба не работает, запустите её:

   ```
   systemctl start comindware<instanceName>
   systemctl start kafka
   systemctl start nginx
   systemctl start elasticsearch
   ```
4. Выполните инициализацию ПО.

## Инициализация Comindware Business Application Platform

1. Запустите веб-браузер и в адресной строке введите ссылку следующего вида, при необходимости указав порт, на котором был развёрнут экземпляр ПО:

   ```
   http://localhost:<portNumber>
   ```
2. Дождитесь запуска и отображения веб-сайта **Comindware Business Application Platform**, что может занять примерно 5 минут.
3. Откроется страница создания аккаунта администратора **Comindware Business Application Platform**.

   ![Страница создания аккаунта администратора](https://kb.comindware.ru/assets/deploy_guide_admin_account_create.png)

   Страница создания аккаунта администратора
4. Введите учётные данные аккаунта администратора и нажмите кнопку «**Создать аккаунт**».

   Внимание!

   - В экземпляре ПО всегда должен оставаться хотя бы один аккаунт администратора. Он может потребоваться для восстановления системы.
   - Аккаунт администратора, созданный при инициализации экземпляра ПО, не следует удалять, даже если впоследствии аккаунты будут синхронизироваться с Active Directory.
5. При необходимости откроется страница инициализации служб. Выберите службы, которые должны быть запущены, и нажмите кнопку «**Далее**».

   ![Страница инициализации служб](https://kb.comindware.ru/assets/deploy_guide_system_initialize.png)

   Страница инициализации служб
6. При необходимости откроется страница активации ПО. Выполните **онлайн-** или **ручную активацию** либо нажмите кнопку «**Пропустить**» для первоначального ознакомления с ПО без активации.
7. При необходимости откроется страница настройки подключения к службе Elasticsearch.
8. В поле «**URI**» введите адрес сервера Elasticsearch, например: `http://localhost:9200`
9. Оставьте **имя пользователя** и **пароль** Elasticsearch пустыми. Или введите их, если в конфигурации Elasticsearch включена аутентификация.
10. Установите уникальный **префикс индекса**, например `mycompanyprefix`. Он служит для идентификации в Elasticsearch данных экземпляра ПО. Поэтому во избежание конфликтов данных для каждого экземпляра ПО следует указывать собственный префикс индекса.
11. Нажмите кнопку «**Далее**».
12. При необходимости откроется страница инициализации данных в Elasticsearch.

    ![Страница инициализации данных в Elasticsearch](https://kb.comindware.ru/assets/deploy_guide_elasticsearch_initialize.png)

    Страница инициализации данных в Elasticsearch
13. Нажмите кнопку «**Обновить**».
14. Дождитесь открытия начальной страницы **Comindware Business Application Platform**.

    ![Начальная страница Comindware Business Application Platform](https://kb.comindware.ru/assets/deploy_guide_desktop.png)

    Начальная страница Comindware Business Application Platform
15. На этом этапе развертывание экземпляра **Comindware Business Application Platform** завершено и можно приступать к созданию и использованию приложений.

## Остановка экземпляра ПО

1. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
2. Перед тем как выполнять любые действия с файлами ПО и базы данных, остановите службы, поддерживающие работу ПО:

   ```
   systemctl stop comindware<instanceName>
   systemctl stop kafka
   systemctl stop nginx
   systemctl stop elasticsearch
   ```
3. Удостоверьтесь, что службы остановлены:

   ```
   systemctl status comindware<instanceName>
   systemctl status kafka
   systemctl status nginx
   systemctl status elasticsearch
   ```

## Удаление экземпляра ПО

1. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
2. Остановите экземпляр ПО согласно [инструкции](#остановка-экземпляра-по).
3. Перейдите в директорию со скриптами для развёртывания ПО **Comindware Business Application Platform**:

   ```
   cd <distPath>/CMW_<osname>/scripts/instance
   ```
4. Запустите удаление экземпляра ПО:

   ```
   sh delete.sh -n=<instanceName>
   ```

   Скрипт `delete.sh` поддерживает следующие ключи:

   - `-n=<instanceName>` — создать экземпляр ПО с указанным именем (**обязательный** ключ).
   - `-h` — вызов краткой справки по использованию скрипта (указывать только без остальных ключей).

## Удаление версии ПО

1. Перейдите в режим суперпользователя:

   ```
   sudo -s
   ```

   или

   ```
   su -
   ```
2. Просмотрите список экземпляров ПО с указанием версий:

   ```
   cat /usr/share/comindware/configs/instance/* | grep -E '(configPath:|version:)'
   ```
3. Удалите все экземпляры с версией ПО, которую требуется удалить, или обновите их до другой версии. Удалить версию ПО, которая используется в каких-либо экземплярах, не удастся. См. *«[Удаление экземпляра ПО](#удаление-экземпляра-по)»*.
4. Удалите версию ПО:

   ```
   rm -r /var/www/.cmw_version/<versionNumber>
   ```

   Здесь: `<versionNumber>` — номер версии ПО вида `X.X.XXXX.X` (например: `4.7.2222.0`).

## Связанные статьи

- *[Пути и содержимое директорий экземпляра ПО](https://kb.comindware.ru/article.php?id=2502)*
- *[Конфигурация экземпляра, компонентов ПО и служб. Настройка](https://kb.comindware.ru/article.php?id=5068)*
- *[Развёртывание Comindware Business Application Platform в кластере](https://kb.comindware.ru/article.php?id=5076)*