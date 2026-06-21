---
title: 'Установка, запуск, инициализация и остановка Comindware Business Application Platform'
kbId: 5072
url: 'https://kb.comindware.ru/article.php?id=5072'
updated: '2024-12-23 15:41:28'
---

# Установка, запуск, инициализация и остановка Comindware Business Application Platform

## Введение

Для работы **Comindware Business Application Platform** требуются операционная система, сервер базы данных, веб-сервер, обратный прокси-сервер и сервер журналирования.

Для быстрого развёртывания **Comindware Business Application Platform** в Windows компания **Comindware** предоставляет дистрибутив с установщиком, настраивающим необходимое программное обеспечение.

Здесь представлены инструкции по развёртыванию и инициализации **Comindware Business Application Platform** из дистрибутива в ОС Windows.

## Установка Comindware Business Application Platform

1. Скачайте и распакуйте архив с дистрибутивом **Comindware Business Application Platform**.
2. Запустите *PowerShell* от имени администратора.
3. Установите неограниченную политику выполнения *PowerShell*:

   ```
   Set-ExecutionPolicy Unrestricted
   ```
4. В запросе на изменение политики выберите вариант «**Да для всех**», введя букву `A`.
5. Перейдите в папку со скриптами для развёртывания ПО:

   ```
   cd "X:\<distPath>\X.X-release-ru-X.X.XXXXX.X.windows\CMW_Windows\scripts\platform"
   ```

   Здесь: `X:\<distPath>\X.X-release-ru-X.X.XXXXX.X.windows` — путь к распакованному дистрибутиву продукта, а `X.X.XXXXX.X` — номер версии ПО.
6. Разблокируйте доступ к скачанным из Интернета установочным файлам:

   ```
   .\files_unblock.ps1
   ```

   Вызов справки для скриптов

   Для ознакомления с ключами и назначением любого скрипта используйте ключ `-h` без каких-либо других ключей, например:

   ```
   .\files_unblock.ps1 -h
   ```
7. Перейдите в папку со скриптами для развёртывания вспомогательного ПО:

   ```
   cd "X:\<distPath>\X.X-release-ru-X.X.XXXXX.X.windows\CMW_Windows\scripts\prerequisites"
   ```
8. Установите необходимое вспомогательное ПО:

   ```
   .\prerequisites_install.ps1
   ```
9. Перезагрузите машину.
10. Запустите *PowerShell* от имени администратора.
11. Перейдите в папку со скриптами для развёртывания вспомогательного ПО:

    ```
    cd "X:\<distPath>\X.X-release-ru-X.X.XXXXX.X.windows\CMW_Windows\scripts\prerequisites"
    ```
12. Проверьте, что дополнительные компоненты установлены:

    ```
    .\prerequisites_list.ps1
    ```

    Если какие-либо дополнительные компоненты не были установлены, повторите шаги 8–12.
13. Перейдите в папку со скриптами для развёртывания ПО **Comindware Business Application Platform**:

    ```
    cd "X:\<distPath>\X.X-release-ru-X.X.XXXXX.X.windows\CMW_Windows\scripts\platform"
    ```
14. Установите ПО:

    ```
    .\version_install.ps1
    ```
15. Удостоверьтесь, что ПО установлено, вызывав список установленных версий ПО:

    ```
    .\version_list.ps1
    ```

## Создание экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **Comindware Business Application Platform**:

   ```
   cd "X:\<distPath>\X.X-release-ru-X.X.XXXXX.X.windows\CMW_Windows\scripts\platform"
   ```
2. Разверните экземпляр ПО:

   ```
   .\instance_create.ps1 -name <instanceName> -port <portNumber> -version <versionNumber>
   ```

   Скрипт `instance_create.ps1` поддерживает следующие ключи:

   - `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.
   - `port <portNumber>` — порт для экземпляра ПО, по умолчанию: 80 (необязательный ключ).
   - `version <versionNumber>` — развернуть ПО указанной версии вида `X.X.XXXXX.X` (например: `4.7.12345.0`) из папки вида `C:\Program Files\Comindware\CBAP\<versionNumber>`.
   - `versionPath <versionPath>` — развернуть ПО из указанной папки `<versionPath>` с версией ПО.
   - `demoDB` — создать экземпляр ПО **Comindware Business Application Platform** c демонстрационной базой данных.
   - `fqdn <hostName>` — имя хоста для экземпляра ПО (необязательный ключ). По умолчанию: `localhost`.
   - `h` — вызвать справку по использованию скрипта (этот ключ следует указывать только без остальных ключей).

   Обязательные ключи для скриптов

   Если не указать обязательный ключ для любого скрипта, он запросит его после запуска.

## Запуск экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **Comindware Business Application Platform**:

   ```
   cd "X:\<distPath>\X.X-release-ru-X.X.XXXXX.X.windows\CMW_Windows\scripts\platform"
   ```
2. Запустите экземпляр ПО:

   ```
   .\instance_start.ps1 -name <instanceName>
   ```

   Здесь: `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.

## Остановка экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **Comindware Business Application Platform**:

   ```
   cd "X:\<distPath>\X.X-release-ru-X.X.XXXXX.X.windows\CMW_Windows\scripts\platform"
   ```
2. Остановите экземпляр ПО:

   ```
   .\instance_stop.ps1 -name <instanceName>
   ```

   Здесь: `-name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.

## Инициализация Comindware Business Application Platform

1. Запустите веб-браузер и в адресной строке введите ссылку следующего вида, при необходимости указав порт, на котором был развёрнут экземпляр ПО:

   ```
   http://localhost:<portNumber>
   ```
2. Дождитесь запуска и отображения веб-сайта **Comindware Business Application Platform**, что может занять примерно 5 минут.
3. Откроется страница создания аккаунта администратора **Comindware Business Application Platform**.

   ![Страница создания аккаунта администратора](/platform/v5.0/administration/deploy/windows/../linux/img/deploy_guide_admin_account_create.png)

   Страница создания аккаунта администратора
4. Введите учётные данные аккаунта администратора и нажмите кнопку «**Создать аккаунт**».

   Внимание!

   - В экземпляре ПО всегда должен оставаться хотя бы один аккаунт администратора. Он может потребоваться для восстановления системы.
   - Аккаунт администратора, созданный при инициализации экземпляра ПО, не следует удалять, даже если впоследствии аккаунты будут синхронизироваться с Active Directory.
5. При необходимости откроется страница инициализации служб. Выберите службы, которые должны быть запущены, и нажмите кнопку «**Далее**».

   ![Страница инициализации служб](/platform/v5.0/administration/deploy/windows/../linux/img/deploy_guide_system_initialize.png)

   Страница инициализации служб
6. При необходимости откроется страница активации ПО. Выполните **онлайн-** или **ручную активацию** либо нажмите кнопку «**Пропустить**» для первоначального ознакомления с ПО без активации.
7. При необходимости откроется страница настройки подключения к службе Elasticsearch.
8. В поле «**URI**» введите адрес сервера Elasticsearch, например: `http://localhost:9200`
9. Оставьте **имя пользователя** и **пароль** Elasticsearch пустыми. Или введите их, если в конфигурации Elasticsearch включена аутентификация.
10. Установите уникальный **префикс индекса**, например `mycompanyprefix`. Он служит для идентификации в Elasticsearch данных экземпляра ПО. Поэтому во избежание конфликтов данных для каждого экземпляра ПО следует указывать собственный префикс индекса.
11. Нажмите кнопку «**Далее**».
12. При необходимости откроется страница инициализации данных в Elasticsearch.

    ![Страница инициализации данных в Elasticsearch](/platform/v5.0/administration/deploy/windows/../linux/img/deploy_guide_elasticsearch_initialize.png)

    Страница инициализации данных в Elasticsearch
13. Нажмите кнопку «**Обновить**».
14. Дождитесь открытия начальной страницы **Comindware Business Application Platform**.

    ![Начальная страница Comindware Business Application Platform](/platform/v5.0/administration/deploy/windows/../linux/img/deploy_guide_desktop.png)

    Начальная страница Comindware Business Application Platform
15. На этом этапе развертывание экземпляра **Comindware Business Application Platform** завершено и можно приступать к созданию и использованию приложений.

## Обновление экземпляра ПО

1. Скачайте и установите ПО новой версии согласно инструкциям в параграфе *«[Установка Comindware Business Application Platform](#deploy_guide_windows_install_sw)»*.
2. Перейдите в папку со скриптами для развёртывания ПО **Comindware Business Application Platform**:

   ```
   cd "X:\<distPath>\X.X-release-ru-X.X.XXXXX.X.windows\CMW_Windows\scripts\platform"
   ```
3. Запустите обновление экземпляра ПО:

   ```
   .\instance_upgrade.ps1 -name <instanceName> -version <versionNumber>
   ```

   Скрипт `instance_upgrade.ps1` поддерживает следующие ключи:

   - `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.
   - `version <versionNumber>` — обновить экземпляр ПО до указанной версии вида `X.X.XXXXX.X` (например: `4.7.12345.0`) из папки вида `C:\Program Files\Comindware\CBAP\<versionNumber>`.
   - `versionPath <versionPath>` — обновить экземпляр ПО до версии из указанной папки `<versionPath>`.
   - `h` — вызвать справку по использованию скрипта (этот ключ следует указывать только без остальных ключей).
4. Просмотрите список установленных экземпляров ПО:

   ```
   .\instance_list.ps1
   ```
5. Рядом с именем экземпляра ПО отобразится номер версии.

## Удаление экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **Comindware Business Application Platform**:

   ```
   cd "X:\<distPath>\X.X-release-ru-X.X.XXXXX.X.windows\CMW_Windows\scripts\platform"
   ```
2. Удалите экземпляр ПО:

   ```
   .\instance_delete.ps1 -name <instanceName>
   ```

   Скрипт `instance_delete.ps1` поддерживает следующие ключи:

   - `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО. Если не указать другие ключи, будет удалена только служба `comindware<instanceName>`.
   - `deleteData` — удалить базу данных из папки вида `C:\ProgramData\Comindware\Instances\<instanceName>\Data` и пользовательские файлы экземпляра ПО из папки вида `C:\ProgramData\Comindware\Instances\<instanceName>\Streams`. Без указания этого ключа или ключа `clear` база данных экземпляра ПО не будет удалена.
   - `clear` — удалить все файлы, папки, базу данных и пользовательские файлы вместе с папкой вида `C:\ProgramData\Comindware\Instances\<instanceName>`, а также службы экземпляра ПО, сайт и пул приложения из IIS.

## Удаление версии ПО

1. Перейдите в папку со скриптами для развёртывания ПО **Comindware Business Application Platform**:

   ```
   cd "X:\<distPath>\X.X-release-ru-X.X.XXXXX.X.windows\CMW_Windows\scripts\platform"
   ```
2. Просмотрите список установленных экземпляров ПО:

   ```
   .\instance_list.ps1
   ```
3. Удалите все экземпляры с версией ПО, которую требуется удалить, или обновите их до другой версии. Удалить версию ПО, которая используется в каких-либо экземплярах, не удастся. См. *«[Удаление экземпляра ПО](#удаление-экземпляра-по)»*.
4. Удалите версию ПО:

   ```
   .\version_delete.ps1 -version <versionNumber>
   ```

   Здесь: `-version <versionNumber>` — указать номер версии ПО вида `X.X.XXXXX.X` (например: `4.7.12345.0`).

## Связанные статьи

- *[Пути и содержимое директорий экземпляра ПО](https://kb.comindware.ru/article.php?id=4620)*