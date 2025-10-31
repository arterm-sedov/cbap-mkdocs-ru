---
title: 'Резервное копирование с помощью внешних средств в ОС Windows'
kbId: 4645
url: 'https://kb.comindware.ru/article.php?id=4645'
---

# Резервное копирование с помощью внешних средств в ОС Windows

Запустить резервное копирование по расписанию можно с помощью встроенного инструмента Windows – Планировщика заданий.

**1.** Создайте файл `powershell` со скриптом для запуска резервного копирования, например `backupscript``.``ps``1`.

**2.** В созданном файле укажите `login` — имя пользователя, `password` — пароль для входа в экземпляр ПО, `backupID` — идентификатор конфигурации резервного копирования в экземпляре системы. См. раздел [*«**Просмотр списка конфигураций резервного копирования*][backup_configure]*[»][backup_configure].*

```
# Enter your credential
$login = «admin»
$password = «admin»

# Enter required backup
configuration ID
$backupID = «backupConfig.1»

# Execution
$localhost = «http://localhost:8081/»
$api = «webapi/backupsession?ConfigurationId=»
$uri = $localhost + $api + $backupID

$WebClient = New-Object System.Net.WebClient
$WebClient.Credentials = New-Object System.Net.NetworkCredential($login, $password)
$WebClient.Encoding = [System.Text.Encoding]::UTF8
$response = $WebClient.UploadString($uri, «POST»,»»)
$response
```

**3.** Откройте Планировщик заданий. До этого удостоверьтесь, что служба планировщика запускается автоматически.

**4.** Откройте раздел «**Windows**».

**5.** Создайте новую задачу, нажав кнопку «**Создать задачу**».

_![Планировщик заданий](https://kb.comindware.ru/assets/img_63bbd8e851cae.png)_

**6.** Укажите имя задачи и условия её выполнения.

_![Создание задачи](https://kb.comindware.ru/assets/img_63bbd93ec6e19.jpeg)_

**7.** Перейдите на вкладку «**Действия**» и нажмите кнопку «**Создать**». В поле «**Программа или сценарий**» укажите программу, с помощью которой будет запущен скрипт. В поле «**Добавить аргументы**» укажите путь к файлу со скриптом.

_![Создание действия](https://kb.comindware.ru/assets/img_63bbd9aa494e5.png)_

**8.** Перейдите на вкладку «**Триггеры**» и нажмите кнопку «**Создать**».

**9.** Составьте расписание, по которому будет запускаться скрипт.

_![](https://kb.comindware.ru/assets/img_63bbda3654a2d.png)_Создание расписания

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
