---
title: Перенос базы данных из ПО версии 4.2 для Windows в ПО версии 5 для Linux
kbId: 4621
---

# Перенос базы данных из ПО версии 4.2 для Windows в ПО версии 5 для Linux {: #db_migrate_4.2_to_5}

{% include-markdown ".snippets/experimental_feature.md" %}

## Введение

Здесь представлены краткие инструкции по переносу базы данных (БД) **{{ productName }}** (далее «экземпляр ПО») версии 4.2 из ОС Windows 10 в экземпляр ПО версии 5 под управлением ОС Linux.

## Предварительные условия

### Необходимое программное обеспечение

- Развёрнутый и работоспособный экземпляр ПО **{{ productName }}** *версии 4.2* под управлением ОС Windows.
- Установленная утилита миграции *версии 5* под управлением ОС Windows для преобразования базы данных.
- Установленное ПО [Open JDK 17](https://download.java.net/openjdk/jdk17.0.0.1/ri/openjdk-17.0.0.1+2_windows-x64_bin.zip "https://download.java.net/java/GA/jdk17.0.2/dfd4a8d0985749f896bed50d7138ee7f/8/GPL/openjdk-17.0.2_windows-x64_bin.zip") для ОС Windows.
    - В переменных среды Windows должна быть заданы следующие переменные для Open JDK (здесь `<version>` — номер версии Open JDK):
        - `JAVA_HOME` — путь к исполняемым файлам Open JDK 17, например `C:\Program Files\jdk\jdk-<version>`
        - `JAVA_HOME_DLL` — путь к DLL-файлу Open JDK 17, например `C:\Program Files\jdk\jdk-<version>\bin\server\jvm.dll`
        - `JAVA_OPTS` — начальный и максимальный объёмы памяти, выделенные для Java, например `-Xms512m -Xmx3g`
        - `JVM_OPTS`  — конфигурация запуска виртуальной машины Java, рекомендуется использовать следующий набор настроек:
        {: .pageBreakBefore }

        ```
        -Xms512m -Xmx16g -XX:MaxDirectMemorySize=1g -Djava.net.preferIPv4Stack=true -XX:+AlwaysPreTouch -XX:+UseG1GC -XX:+ScavengeBeforeFullGC -XX:+DisableExplicitGC --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-exports=java.base/jdk.internal.misc=ALL-UNNAMED --add-exports=java.base/sun.nio.ch=ALL-UNNAMED --add-exports=java.management/com.sun.jmx.mbeanserver=ALL-UNNAMED --add-exports=jdk.internal.jvmstat/sun.jvmstat.monitor=ALL-UNNAMED --add-exports=java.base/sun.reflect.generics.reflectiveObjects=ALL-UNNAMED --add-opens=jdk.management/com.sun.management.internal=ALL-UNNAMED -DIGNITE_QUIET=false -DIGNITE_NO_ASCII=true
        ```

### Требования к аппаратному обеспечению

- Для преобразования базы данных свободный объем оперативной памяти должен составлять 10 ГБ объём базы данных (рекомендуется минимум 32 ГБ).
- На дисках должно быть достаточно места для хранения исходной БД и преобразованной БД. Объём преобразованной БД может в 10 раз превышать объём исходной БД.

## Создание резервной копии базы данных экземпляра ПО под управлением Windows {: .pageBreakBefore }

1. Откройте веб-сайт системы версии 4.2.
2. В разделе «**Администрирование**» — «**Инфраструктура**» выберите пункт «**Резервное копирование**».
3. В списке конфигураций резервного копирования выберите или создайте конфигурацию резервного копирования. В свойствах конфигурации резервного копирования должны быть установлены флажки «**С файлами**» и «**Со скриптами**». См. статью *«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]».*
4. Нажмите кнопку «**Запустить копирование**».
5. Дождитесь окончания резервного копирования. Статус резервного копирования отображается на вкладке «**Журнал**» страницы «**Резервное копирование**».

_![Запуск резервного копирования экземпляра ПО](https://kb.comindware.ru/assets/Pasted image 20230313144815.png)_

## Преобразование базы данных в Windows {: .pageBreakBefore }

Для преобразования базы данных используется утилита миграции **CBAP Migration Tool** в ОС Windows.

1. Скачайте архив с утилитой миграции `migrationTool.zip` по ссылке, предоставленной службой поддержки Comindware.
2. Распакуйте архив `migrationTool.zip`, например, в папку `C:\MigrationTool`
3. Выделите для {{ apacheIgniteVariants }} достаточно оперативной памяти, как указано ниже

    1. Откройте в текстовом редакторе файл `C:\MigrationTool\Ignite.config`
    2. Найдите блок конфигурации выделенной памяти, например:

        ``` xml
        <property name="dataRegionConfigurations">
            <list>
            <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                <property name="warmUpConfiguration">
                    <bean class="org.apache.ignite.configuration.LoadAllWarmUpConfiguration" />
                </property>
                <property name="name" value="Persistent" />
                <property name="persistenceEnabled" value="true" />
                <property name="initialSize" value="#{20L * 1024 * 1024}" />
                <property name="maxSize" value="#{3L * 1024 * 1024 * 1024}" />
                <property name="pageEvictionMode" value="RANDOM_2_LRU" />
                <!--
                < 1 GB             : MIN (256 MB, Data_Region_Size)
                between 1 GB and 8 : GB Data_Region_Size / 4
                > 8 GB             : 2 GB
                -->
                <property name="checkpointPageBufferSize" value="#{256L * 1024 * 1024}" />
            </bean>
        ```

    3. В показанном выше блоке измените директивы начального и максимального объема памяти, а также объема буфера контрольных точек, как указано ниже:
        ``` xml
        <property name="initialSize" value="#{1L * 1024 * 1024 * 1024}" />
        <property name="maxSize" value="#{8L * 1024 * 1024 * 1024}" />
        ...
        <property name="checkpointPageBufferSize" value="#{2L * 1024 * 1024 * 1024}" />
        ```
        {: .pageBreakBefore }

    4. Сохраните изменённый файл.

4. Откройте папку с резервными копиями, указанную в столбце «**Путь к файлу**» на вкладке «**Конфигурации**» страницы «**Резервное копирование**».

    _![Путь к папке с резервными копиями экземпляра ПО](https://kb.comindware.ru/assets/Pasted image 20230313145410.png)_

5. Измените расширение файла резервной копии с `cdbbz` на `zip`.

    _![Переименование файла резервной копии экземпляра ПО](https://kb.comindware.ru/assets/Pasted image 20230313150026.png)_

6. Распакуйте архив резервной копии, например в папку `C:\DatabaseBackup`

    _![Распакованное содержимое резервной копии экземпляра ПО](https://kb.comindware.ru/assets/Pasted image 20230313153125.png)_

7. Создайте **пустую** папку, в которую будут помещены файлы базы данных, преобразованные утилитой миграции, например `C:\DatabaseMigrated`.
8. Запустите приложение *Windows PowerShell ISE* от *имени администратора* Windows.
9. В окно скриптов скопируйте следующие строки:

    ``` powershell
    Get-ChildItem "C:\migrationTool" -recurse | Unblock-File -confirm
    [Environment]::SetEnvironmentVariable("IsMigrationMode", "true")
    C:\MigrationTool\bin\Comindware.Platform.Migration.exe "C:\DatabaseBackup" "C:\DatabaseMigrated" <instanceName>
    ```

    Здесь:
    {: .pageBreakBefore }

    - `C:\MigrationTool\bin\Comindware.Platform.Migration.exe` — путь к распакованному на [шаге 2](#преобразование-базы-данных-в-windows) исполняемому файлу утилиты миграции базы данных.
    - `C:\DataвaseBackup` — путь к папке с базой данных, подлежащей миграции.
    - `C:\DatabaseMigrated` — путь к папке, в которую будут помещены преобразованные файлы базы данных.
    - `instanceName` — имя нового экземпляра ПО, который будет создан после миграции. Рекомендуется указывать такое же имя экземпляра ПО, как использовалось в среде Windows. См. статью *«[Изменение конфигурации экземпляра ПО][admin_utility_instance_configure]»*.

10. Выделите первую строку скрипта:

    ``` powershell
    Get-ChildItem "C:\migrationTool" -recurse | Unblock-File -confirm
    ```

11. Выполните выделенную строку, нажав клавишу ++f8++ (или щелкнув строку правой кнопкой мыши и выбрав в контекстном меню пункт **Run Selection**).
12. Дождитесь завершения выполнения команды.
13. Выделите и выполните вторую и третьи строки скрипта:

    ``` powershell
    [Environment]::SetEnvironmentVariable("IsMigrationMode", "true")
    C:\MigrationTool\bin\Comindware.Platform.Migration.exe "C:\DataвaseBackup" "C:\DatabaseMigrated" <instanceName>
    ```

14. Утилита миграции выведет на экран данные о процессе миграции.
15. Дождитесь успешного завершения миграции.
16. Удостоверьтесь, что в папке для преобразованной базы данных появились новые папки и файлы.

    _![Папки преобразованной базы данных](https://kb.comindware.ru/assets/Pasted image 20230323134758.png)_

## Развёртывание преобразованной базы данных в экземпляре ПО под управлением Linux {: .pageBreakBefore }

1. Перейдите в режим суперпользователя:

    **Astra Linux, Ubuntu**

    ``` sh
    sudo -i
    ```

    **Альт Сервер, РЕД ОС**

    ``` sh
    su -
    ```

2. Скачайте, разверните и инициализируйте экземпляр ПО.

    - См. *[Установка и запуск {{ productName }}][deploy_guide_linux]*
    - При установке ПО используйте ключ `d=clear` — установить ПО без демонстрационной базы данных:

    **Astra Linux, Ubuntu**

    ``` sh
    sh install.sh -e -p -k -d=clear -u=www-data -g=www-data -i=<instanceName>

    ```

    **Альт Сервер, РЕД ОС**

    ``` sh
    sh install.sh -e -p -k -d=clear -u=_nginx -g=_nginx -i=<instanceName>
    ```

    Здесь `<instanceName>` — имя экземпляра ПО. Если не указать этот параметр, будет задано стандартное имя экземпляра: `cmwdata`

3. Остановите сервисы {{ openSearchVariants }}, {{ nginxVariants }}, comindwareinstanceName и Kafka и удостоверьтесь, что они остановлены:

    ``` sh
    systemctl stop elasticsearch
    systemctl stop nginx
    systemctl stop kafka
    systemctl stop comindware<instanceName>

    systemctl status elasticsearch
    systemctl status nginx
    systemctl status kafka
    systemctl status comindware<instanceName>

    ```

4. Поместите в папку `/var/lib/comindware/<instanceName>/Database/` содержимое папки с преобразованной базой данных. См. _«[Преобразование базы данных в Windows](#преобразование-базы-данных-в-windows)»_.
5. Смените владельца папки `/var/lib/comindware/`:

    **Astra Linux, Ubuntu**

    ``` sh
    chown -R www-data:www-data /var/lib/comindware/
    ```

    **Альт Сервер, РЕД ОС**

    ``` sh
    chown -R _nginx:_nginx /var/lib/comindware/
    ```

## Запуск и проверка конфигурации экземпляра ПО

1. Запустите необходимые службы и проверьте их статус:

    ``` sh
    systemctl start elasticsearch kafka nginx comindware<instanceName>
    systemctl status elasticsearch kafka nginx comindware<instanceName>
    ```

2. Перезапустите систему:

    ``` sh
    reboot
    ```

3. Откройте в браузере веб-сайт с экземпляром ПО.
4. Дождитесь инициализации экземпляра ПО. Этот процесс может занять некоторое время. Может потребоваться обновить страницу браузера.
5. Проверьте и исправьте конфигурацию экземпляра. См. *«[Проверка и настройка конфигурации экземпляра ПО после восстановления из резервной копии][restore_test_configure]».*

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Проверка и настройка конфигурации экземпляра ПО после восстановления из резервной копии][restore_test_configure]_
- _[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]_
- _[Установка и запуск {{ productName }}][deploy_guide_linux]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
