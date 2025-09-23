Кластер развёрнут на трёх узлах со следующими ролями:
`10.0.0.10` - основной веб сервер
`10.0.0.11` - основной сервер интеграций
`10.0.0.12` - резервный сервер/сервер резервного копирования

Основная балансировка выполняется на прокси-сервере, установленном выше по сети, либо на DNS, в процессе обновления изменения в конфигурации балансировщика не производятся.

Последовательность обновления серверов:
- обновление резервного сервера `10.0.0.12`
- перенаправление интеграционного трафика на резервный сервер
- обновление сервера интеграций `10.0.0.11`
- восстановление трафика интеграций на `10.0.0.11`
- перенаправление пользовательского трафика на 

0. СОЗДАТЬ РЕЗЕРВНУЮ КОПИЮ! Или средствами Приложения, или системными.
1. Загрузить в директорию для дистрибутивов на общем СХД дистрибутив версии Приложения
```sh
wget --user <cmw-devops> --ask-password -P /<path/to/shared/folder>/ https://teamcity.comindware.com/repository/download/<path/to/distr>/5.0-<distr>-<version>.<os>.tar.gz
```

2. Перейти в директорию для дистрибутивов и распаковать загруженный архив с версией:
```sh
cd /<path/to/shared/folder>/
tar -xf 5.0-<distr>-<version>.<os>.tar.gz
``` 

3. На каждом узле перейти в директорию со скриптами версии, запустить установку версии:
```sh
cd /<path/to/shared/folder>/CMW_<os>_<version>/scripts
bash version_install.sh
bash version_list.sh
bash instance_list.sh
```
   
4. На каждом узле проверить, и, при необходимости отредактировать конфигурационный файл Приложения:
```sh
nano /usr/share/comindware/configs/instance/<instanceName>.yml
``` 

с версии 5.0.23654.0 упразднены директивы
```yml
isContainerEnvironment:
clusterNodes:
```
и добавлены директивы
```yml
# Ожидает активации кластера перед запуском
db.waitForClusterActivation: true
# Ожидает наличие файла перед запуском
db.waitForFileActivation: /var/www/.cmw_environment/<instanceName>
```
позже они тоже упразднены и добавлены
```yml
# Не загружает платформу пока существует файл db.workDir/hold.lock
db.holdLock: true
```
5. На резервном узле остановить экземпляр и сервисы, запустить скрипт обновления версии экземпляра
```sh 
systemctl stop apigateway<instanceName> && systemctl stop comindware<instanceName> && systemctl stop adapterhost<instanceName>

bash instance_upgrade.sh -n=<instanceName> -vp=/var/www/.cmw_version/<version>
```

После обновления запустится экземпляр Приложения
Проверить статус сервисов
```sh 
systemctl status apigateway<instanceName> comindware<instanceName> adapterhost<instanceName>
``` 
Открыть вывод журнала состояния экземпляра
```sh
tail -f -n 50 /var/log/comindware/<instanceName>/heartbeat_<today>.log
```

Выполнить запрос в узел Приложения через веб-браузер

дождаться  в выводе лога сообщения об ожидании удаления файла `db.workDir/hold.lock`

переключиться на вывод лога `igniteClient`
```sh 
tail -f -n 50 /var/log/comindware/<instanceName>/igniteClient_<today>.log
```

Дождаться сообщения об окончании ребалансировки кластера 
```
... INFO      Skipping rebalancing (nothing scheduled) ...
```

После чего удалить из директории базы данных файл `hold.lock` и снова открыть на вывод журнал состояния экземпляра
```sh
rm /var/lib/comindware/<instanceName>/Database/hold.lock

tail -f -n 50 /var/log/comindware/<instanceName>/heartbeat_<today>.log
```

Дождаться загрузки страницы входа в веб-браузере, выполнить вход в систему

Убедиться в работоспособности узла

6. На интеграционном и пользовательском узлах перед выполнением обновления следует изменить конфигурацию подключения Nginx.
```sh
## Deb
nano /etc/nginx/sites-enabled/comindware<instanceName>
## RH
nano /etc/nginx/conf.d/comindware<instanceName>.conf
```

В блоке  `location /async` и `location /`
изменить правило проксирования - передавать поступающие запросы на соседний работающий узел (желательно необновлённый)
7. выполнить последоватьельность из П.5 
По окончании обновления узла - восстановить конфигурацию подключения
