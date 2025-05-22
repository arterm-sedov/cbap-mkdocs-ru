---
title: 'Обновление версии экземпляра ПО в Windows'
kbId: 5102
---

# Обновление версии экземпляра ПО в Windows {: #upgrade_version_windows }

## Введение {: #upgrade_version_windows_intro }

Здесь представлены инструкции по обновлению версии экземпляра ПО **{{ productName }}** на одном и том же сервере с остановкой экземпляра.

Инструкции даны для обновления с версий 4.7.2 до версий 4.7.3–5.0 в ОС Windows.

!!! tip "Совет"

    Этот способ можно использовать, если ПО **{{ productName }}** развёрнуто на одной машине и нет возможности развернуть новую машину для экземпляра ПО новой версии.

## Порядок обновления версии экземпляра ПО {: #upgrade_version_windows_sequence }

1. Подготовьте экземпляр ПО к обновлению:

    - Создайте резервную копию экземпляра ПО.
    - Сохраните конфигурацию экземпляра ПО и вспомогательных служб.
    - Остановите экземпляр ПО и вспомогательные службы.
    - Удалите компоненты старой версии ПО.
    - Переместите директорию с базой данных экземпляра ПО в резервную директорию.

2. Обновите версию экземпляра ПО:

    - Скачайте и распакуйте два дистрибутива: вспомогательного ПО и новой версии ПО.
    - Убедитесь, что установлены все необходимые компоненты вспомогательного ПО.
    - Установите новую версию ПО.
    - Удалите экземпляр ПО старой версии
    - Создайте экземпляр ПО новой версии.
    - Обновите конфигурацию экземпляра ПО и вспомогательных служб.
    - Перезапустите экземпляр ПО и вспомогательные службы.
    - Инициализируйте экземпляр ПО.
    - Остановите экземпляр ПО.
    - Скопируйте в экземпляр ПО ранее перемещённую директорию с базой данных.
    - Запустите экземпляр ПО.
    - Обновите структуру данных до новой версии.
    - Снова перезапустите экземпляр ПО.

## Примечания по установке {: #upgrade_version_windows_notes .pageBreakBefore }

{%
include-markdown "./deploy_guide.md"
start="<!--windows-deploy-notes-start-->"
end="<!--windows-deploy-notes-end-->"
%}
    - `<config_backup_path>` — путь к папке для сохранения резервных копий файлов конфигурации (например, `X:\backups\config_tmp`).
    - `<iis-config-backup>` — имя резервной копии конфигурации IIS.
    - `<ГГГГ-ММ-ДД>` — текущая дата.

[](){: #powershell_execution_policy }
{%
include-markdown "./deploy_guide.md"
start="<!--powershell-execution-policy-start-->"
end="<!--powershell-execution-policy-end-->"
%}

## Подготовка экземпляра ПО к обновлению {: #upgrade_version_windows_prepare .pageBreakBefore }

!!! warning "Внимание!"

    Выполните подготовительные действия отдельно для каждого экземпляра ПО, версию которого требуется обновить.

1. Создайте и перенесите во внешнее хранилище резервную копию базы данных экземпляра ПО. См. _«[Настройка конфигураций и запуск резервного копирования][backup_configure_list_view]»_.
2. Запустите _PowerShell_ от имени администратора.
3. Сохраните резервную копию конфигурации экземпляра ПО и вспомогательных служб:
{: #ConfigBackup }

    - Создайте директорию для резервных копий файлов конфигурации:

        ``` powershell
        New-Item -Path "<config_backup_path>" -ItemType "Directory"
        ```

    - Скопируйте все файлы `.yml` и `.config` в директорию `<config_backup_path>`:

        ``` powershell
        Copy-Item -Path "C:\ProgramData\сomindware\Instances\<instanceName>\сonfig\*" -Destination "<config_backup_path>" -Recurse -Include "*.yml", "*.config"
        ```

    - Сохраните резервную копию файла конфигурации экземпляра ПО `<instanceName>.yml`:

        ``` powershell
        Copy-Item -Path "C:\ProgramData\comindware\configs\instance\<instanceName>.yml" -Destination "<config_backup_path>"
        ```

    - Создайте резервную копию конфигурации IIS:

        ``` powershell
        cd c:\Windows\system32\inetsrv
        appcmd add backup "<iis-config-backup>"
        ```

        Удостоверьтесь, что после выполнения этой команды в папке `c:\Windows\system32\inetsrv\backup` появилась папка `<iis-config-backup>`.

    - Сохраните резервную копию конфигурации Java из следующих переменных среды (например, скопируйте их в текстовый файл):
        - `JAVA_HOME` — путь к исполняемым файлам Open JDK.
        - `JAVA_HOME_DLL` — путь к DLL-файлу Open JDK.
        - `JAVA_OPTS` — начальный и максимальный объёмы памяти, выделенные для Java.
        - `JVM_OPTS` — конфигурация запуска виртуальной машины Java

4. Остановите экземпляр ПО и вспомогательные службы и удостоверьтесь, что они остановлены

    - Перейдите в директорию со скриптами для развёртывания ПО **{{ productName }}**:
        ``` powershell
        cd "<distPath>\CMW_Windows<versionNumber>\scripts"
        ```

    - Остановите экземпляр ПО, службу `adapterhost` и службу `apigateway` :

        ``` powershell
        .\instance_stop.ps1 -name <instanceName>
        .\adapterhost_stop.ps1 <instanceName>
        .\apigateway_stop.ps1 <instanceName>
        ```

5. Проверьте статус экземпляра ПО в IIS:

    Запустите **Диспетчер служб IIS** (Internet Information Services (IIS) Manager):

     - В левой древовидной панели **«Подключения»** (Connections), разверните меню с названием своего сервера.
     - Выберите **«Пулы приложений»** (Application Pools).
     - Убедитесь, что напротив служб `Comindware <instanceName>`, `Comindware <instanceName>_adapterhost`, `Comindware <instanceName>_apigateway` стоит статус «**Остановлено**» (Stopped).

6. Удалите (или переместите в резервное хранилище) неиспользуемые предыдущие дистрибутивы ПО (`<distPath>` — путь к директории с дистрибутивом, `<versionNumber>` — версия ПО):

    ``` powershell
    Remove-Item <distPath>\CMW_Windows<versionNumber> -Recurse
    ```

7. Сохраните резервную копию директории с базой данных экземпляра ПО:

    ``` powershell
    Copy-Item -Path "C:\ProgramData\сomindware\Instances\<instanceName>\Database" -Destination "<config_backup_path>" -Recurse
    ```

## Обновление версии ПО для экземпляра {: #upgrade_version_windows_install .pageBreakBefore }

!!! warning "Внимание!"

    Если при обновлении [на шаге 28](#dataUpgrade) будут обнаружены ошибки, не продолжайте обновление, установите старую версию ПО, восстановите экземпляр ПО из резервной копии и обратитесь в службу поддержки **{{ companyName }}**.

!!! note "Обновление нескольких экземпляров ПО"

    Выполните приведённые ниже шаги 9–21 для каждого экземпляра ПО, версию которого требуется обновить, так как скрипт обновления выполняется отдельно для указанного экземпляра ПО.

    После обновления всех экземпляров ПО для экономии места старую версию ПО можно удалить согласно инструкции _«[Удаление версии ПО][deploy_guide_windows_version_delete]»_.

1. Скачайте и распакуйте дистрибутив с новой версией вспомогательного ПО для **{{ productName }}**.
2. Запустите _PowerShell_ от имени администратора.
3. При необходимости установите неограниченную политику выполнения _PowerShell_. См. _«[Политика выполнения PowerShell](#powershell_execution_policy)»_.
4. Перейдите в директорию со скриптами для развёртывания вспомогательного ПО:

    ``` powershell
    cd "<prerequisitesDistPath>\CMW_Windows<versionNumber>\scripts"
    ```

    Здесь `<prerequisitesDistPath>` — путь к распакованному дистрибутиву вспомогательного ПО (например, `<distPath>\X.X-release-ru-<versionNumber>.prerequisites.windows`).

5. Разблокируйте доступ к скачанным из интернета установочным файлам:

    ``` powershell
    .\files_unblock.ps1
    ```

6. Проверьте, что установлены все компоненты вспомогательного ПО:

    ``` powershell
    .\prerequisites_list.ps1
    ```

    !!! warning "Внимание!"

        Важно, чтобы были установлены все компоненты вспомогательного ПО.

        Если каких-либо компонентов не хватает, то установите вспомогательное ПО:

        ``` powershell
        .\prerequisites_install.ps1
        ```

7. Скачайте и распакуйте архив с дистрибутивом новой версией ПО.
8. В запросе на изменение политики выберите вариант «**Да для всех**», введя букву ++a++.
9. Перейдите в директорию со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "<distPath>\CMW_Windows<versionNumber>\scripts"
    ```

    Здесь: `<distPath>` — путь к распакованному дистрибутиву ПО **{{ productName }}** (например, `<distPath>\X.X-release-ru-<versionNumber>.windows`).

10. Разблокируйте доступ к скачанным из нтернета установочным файлам:

    ``` powershell
    .\files_unblock.ps1 
    ```

11. Установите новую версию ПО:

    ``` powershell
    .\version_install.ps1
    ```

12. Удостоверьтесь, что ПО установлено, вызвав список установленных версий ПО:

    ``` powershell
    .\version_list.ps1
    ```

    Пример списка установленных версий ПО:

    ``` powershell
    Running script version_list.ps1.
    ====================================================================
    Source folder: C:\Program Files\Comindware\CBAP
    ====================================================================
    Version
    ====================================================================
    5.0.13286.0
    5.0.13334.0

    ####################################################################
    Command executed.
    Complete script version_list.ps1.
    ####################################################################
    Status: Completed
    ```

13. Удалите экземпляр ПО старой версии:

    ``` powershell
    .\instance_delete.ps1 -name <instanceName> -clear
    ```

    Ключи:

    - `-name` — имя экземпляра.
    - `-clear` — удалить следующие объекты:
        - все файлы, папки, базу данных и пользовательские файлы экземпляра ПО;
        - директорию экземпляра ПО вида `C:\ProgramData\Comindware\Instances\<instanceName>`;
        - все службы экземпляра ПО;
        - сайт и пул приложения из IIS.

14. Создайте экземпляр ПО новой версии:

    ``` powershell
    .\instance_create.ps1 -name <instanceName> -port <portNumber> -version <versionNumber>
    ```  

    Ключи:

    - `-name` — имя экземпляра;
    - `-version` — номер версии ПО;
    - `-port` (необязательно) — порт для экземпляра ПО (по умолчанию: 80).

15. По окончании создания скрипт выведет информацию о компонентах экземпляра ПО. Удостоверьтесь, что компоненты успешно установлены.

    Если какая-либо из служб имеет статус `FAILED`, перезапустите её. Например:

    ``` powershell
    .\instance_stop.ps1 -name <instanceName>
    .\adapterhost_stop.ps1 <instanceName>
    .\apigateway_stop.ps1 <instanceName>
    ```

    ``` powershell
    .\instance_start.ps1 -name <instanceName>
    .\adapterhost_start.ps1 <instanceName>
    .\apigateway_start.ps1 <instanceName>
    ```

16. Восстановите конфигурацию IIS для экземпляра ПО из резервной копии:

    ``` powershell
    cd c:\Windows\system32\inetsrv\
    appcmd restore backup "<iis-config-backup>"
    ```

17. Перезапустите службу IIS для применения изменений:

    ``` powershell
    Restart-WebAppPool -Name <instanceAppPool>
    ```

    Здесь `<instanceAppPool>` — имя пула приложений для экземпляра ПО.

18. Отредактируйте файлы конфигурации экземпляра ПО и вспомогательных служб в соответствии с резервными копиями, [сохранёнными ранее](#ConfigBackup):

    - `C:\ProgramData\сomindware\Instances\<instanceName>\сonfig\adapterhost.yml`
    - `C:\ProgramData\сomindware\Instances\<instanceName>\сonfig\apigateway.yml`
    - `C:\ProgramData\сomindware\Instances\<instanceName>\сonfig\Ignite.config`
    - `C:\ProgramData\сomindware\configs\instance\<instanceName>.yml`

19. Восстановите локальные переменные среды согласно сохранённым резервным копиям:

    ``` powershell
    rundll32 sysdm.cpl,EditEnvironmentVariables
    ```

20. Перезапустите службы, настройки которых были изменены, например:

    ``` powershell
    cd "<distPath>\CMW_Windows<versionNumber>\scripts"
    .\instance_stop.ps1 -name <instanceName>
    .\apigateway_stop.ps1 -name <instanceName>
    .\adapterhost_stop.ps1 -name <instanceName>
    ```

    ``` powershell
    .\apigateway_start.ps1 -name <instanceName>
    .\instance_start.ps1 -name <instanceName>
    .\adapterhost_start.ps1 -name <instanceName>
    ```

21. Откройте сайт экземпляра ПО в браузере, одновременно открыв выдачу журналов экземпляра в _PowerShell_:

    ```powershell
    Get-Content "C:\ProgramData\comindware\Instances\<instanceName>\Logs\heartbeat_<ГГГГ-ММ-ДД>.log" -Wait
    ```

    Здесь `<ГГГГ-ММ-ДД>` — текущая дата.

    См. _«[Подсистема журналирования][logging_engine]»_.

22. В браузере выполните инициализацию экземпляра ПО, выполните вход и проверьте работоспособность ПО.
23. Остановите экземпляр ПО:

    ``` powershell
    .\instance_stop.ps1 -name <instanceName>
    ```

24. Удалите или переименуйте директорию `Database` в  директории  экземпляра ПО:

    ``` powershell
    Remove-Item -Path "C:\ProgramData\comindware\Instances\<instanceName>\Database" -Recurse
    ```

25. Скопируйте в экземпляр ПО [сохранённую ранее](#ConfigBackup) резервную копию директории с базой данных экземпляра ПО:

    ``` powershell
    Copy-Item -Path "<config_backup_path>\Database" -Destination "C:\ProgramData\сomindware\Instances\<instanceName>" -Recurse -Force
    ```

26. Запустите экземпляр ПО:

    ``` powershell
    .\instance_start.ps1 -name <instanceName>
    ```

27. Откройте сайт экземпляра ПО в браузере, одновременно открыв выдачу журналов экземпляра в _PowerShell_:

    ``` powershell
    Get-Content "C:\ProgramData\comindware\Instances\<instanceName>\Logs\heartbeat_<ГГГГ-ММ-ДД>.log" -Wait
    ```

28. Дождитесь завершения обновления структуры данных и проверьте его успешное выполнение.
{: #dataUpgrade }

    !!! warning "Внимание!"

        При обновлении с версии 4.7.2 на версии 4.7.3-5.0 обновляется структура базы данных.

        После этого необходимо вручную удалить некоторые данные кэша в старом формате.

        Поэтому продолжать обновление версии экземпляра ПО можно только после успешного обновления структуры данных. 

    - Удостоверьтесь, что появились журналы обновления:
        - `C:\ProgramData\сomindware\Instances\<instanceName>\Logs\UpgradeOntology_<ГГГГ-ММ-ДД>.log`
        - `C:\ProgramData\сomindware\Instances\<instanceName>\Logs\upgrade<ГГГГ-ММ-ДД>.log`
    - Удостоверьтесь, что в журнале `UpgradeOntology_<ГГГГ-ММ-ДД>.log` последняя запись содержит строку `Upgrade of ontology completed successfully`.
    - Удостоверьтесь, что в журнале `upgrade<ГГГГ-ММ-ДД>.log` последняя запись содержит строку `Upgrade completed`.
    - Удостоверьтесь, что в журналах отсутствуют ошибки обновления. Найдите их по ключевому слову `error`.
    - Если обновление выполнено успешно, переходите к шагу 29.
    - Если в журнале обновления имеются ошибки:

        1. Не переходите к шагу 29.
        2. Снова установите для экземпляра старую версию ПО.
        3. Восстановите базу данных из резервной копии.
        4. Обратитесь в службу поддержки **{{ companyName }}**, предоставив журналы обновления и ошибок для анализа.

29. Создайте резервную копию экземпляра ПО. См. _«[Настройка конфигураций и запуск резервного копирования][backup_configure_list_view]»_.
30. Остановите экземпляр ПО.
31. Распакуйте резервную копию.
32. Перейдите в директорию `<dbBackupFolder>\Database\db\node*`.

    Здесь `<dbBackupFolder>` — путь к распакованной резервной копии экземпляра ПО.

33. Удалите из неё следующие директории кэшей:

    ``` powershell
    Remove-Item cacheGroup-*-TableIdentity -Recurse -Force
    Remove-Item cacheGroup-*-TableIdentityReplicated -Recurse -Force
    Remove-Item cacheGroup-*Value -Recurse -Force
    Remove-Item cacheGroup-*ValueReplicated -Recurse -Force
    Remove-Item cache-ignite-sys-cache -Recurse -Force
    Remove-Item cp -Recurse -Force
    Remove-Item metastorage -Recurse -Force
    Remove-Item cacheGroup-Keys -Recurse -Force
    ```

34. Очистите директорию с базой данных экземпляра ПО:

    ``` powershell
    Remove-Item -Path "C:\ProgramData\comindware\Instances\<instanceName>\Database\*" -Recurse -Force
    ```

35. Скопируйте очищенную резервную копию в директорию с базой данных:

    ``` powershell
    Copy-Item -Path "<dbBackupFolder>\Database\*" -Destination "C:\ProgramData\comindware\Instances\<instanceName>\Database" -Recurse -Force
    ```

36. Запустите экземпляр ПО.
37. Откройте сайт экземпляра ПО в браузере, дождитесь его инициализации и выполните вход.
38. Проверьте и при необходимости исправьте конфигурацию экземпляра ПО. См. _«[Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]»_.
39. Проверьте и работоспособность экземпляра ПО.
40. Создайте резервную копию работоспособного экземпляра **{{ productName }}**.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Пути и содержимое директорий экземпляра ПО][paths]
- [Установка вспомогательного ПО][deploy_guide_windows_install_prerequisites]
- [Установка, запуск, инициализация и остановка Comindware Platform в Windows][deploy_guide_windows]
- [Резервное копирование и восстановление Comindware Platform. Краткое руководство для ОС Windows][backup_restore_windows]
- [Настройка конфигураций и запуск резервного копирования][backup_configure_list_view]
- [Подсистема журналирования][logging_engine]
- [Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
