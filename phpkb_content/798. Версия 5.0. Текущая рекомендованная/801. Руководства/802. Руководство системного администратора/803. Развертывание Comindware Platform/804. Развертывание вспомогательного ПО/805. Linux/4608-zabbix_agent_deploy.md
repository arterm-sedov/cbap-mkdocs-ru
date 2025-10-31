---
title: 'Zabbix Agent. Инструкции по установке'
kbId: 4608
url: 'https://kb.comindware.ru/article.php?id=4608'
---

# Zabbix Agent. Инструкции по установке

Программное обеспечение *Zabbix Agent* позволяет осуществлять мониторинг устройств, на которые оно установлено. Для сбора и отображения данных мониторинга используется ПО *Zabbix Server*. См. в статью «[Zabbix Server, Zabbix Agent, Zabbix Frontend и MySQL. Инструкции по установке][zabbix_server_deploy] ».

В настоящей статье представлены инструкции по установке и настройке Zabbix Agent в ОС Linux на примере Ubuntu 22.04.

## 1. Добавление репозитория и установка Zabbix Agent

Основная часть операций выполняется с правами обычного пользователя `username`. Некоторые операции необходимо выполнять с правами суперпользователя `root`.

1.1. Перейдите в папку пользователя `username`:

```
cd /home/username

```

1.2. Для добавления репозитория Zabbix загрузите его deb-пакет:

```
wget https://repo.zabbix.com/zabbix/6.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.0-4%2Bubuntu22.04_all.deb

```

1.3. Распакуйте deb-пакет:

```
sudo dpkg -i zabbix-release_6.0-4+ubuntu22.04_all.deb

```

1.4. Обновите базу данных пакетов в операционной системе:

```
sudo apt update

```

1.5. Установите *Zabbix Agent*:

```
sudo apt install --yes zabbix-agent

```

## 2. Настройка сервиса Zabbix Agent

2.1. На каждой из машин с *Zabbix Agent* отредактируйте файл конфигурации: `/etc/zabbix/zabbix_agentd.conf`:

```
sudo nano /etc/zabbix/zabbix_agentd.conf

```

2.2. В файле конфигурации укажите IP-адрес *Zabbix Server* — в подключениях с неизвестных IP-адресов будет отказано:

```
Server=your.server.ip.address

```

2.3. Отредактируйте директиву `ServerActive`:

```
ServerActive=your.server.ip.address

```

## 3. Запуск сервиса Zabbix Agent

3.1. Разрешите в сетевом экране обращения через порт `10050`:

```
sudo ufw allow 10050/tcp

```

3.2. Примените изменения:

```
sudo systemctl daemon-reload
sudo ufw reload

```

3.3. Запустите службу *Zabbix Agent* и добавьте его в список автозагрузки:

```
sudo systemctl enable --now zabbix-agent

```

3.4. Удостоверьтесь, что служба работает:

```
systemctl status zabbix-agent 
```

_![](https://kb.comindware.ru/assets/img_63ad99c681d0a.png)_Ожидаемый статус сервиса *Zabbix Agent*

## 4. Добавление Linux-хоста в сеть мониторинга

4.1. Откройте *Zabbix Frontend* (см. статью «[Zabbix Server, Zabbix Agent, Zabbix Frontend и MySQL. Инструкции по установке][zabbix_server_deploy]».). Для э того в адресной строке браузера наберите: `http://zabbix-server-ip-address:8080`

4.2. Откройте раздел «**Monitoring**» > «**Hosts**» и нажмите кнопку «**Create host**».

_![](https://kb.comindware.ru/assets/img_63ad9a5b84655.png)_Кнопка создания хоста Zabbix Agent

4.3. Задайте имя хоста в поле «**Host name**».

4.4. Выберите шаблон «**Template OS Linux by Zabbix agent**».

4.5. Создайте группу мониторинга для хоста или добавьте его к существующей группе.

4.6. Под полем «**Interfaces**» нажмите кнопку «**Add**» и в раскрывающемся меню выберите пункт «**Agent**».

_![](https://kb.comindware.ru/assets/img_63ad9b483a473.png)_Настройка свойств хоста *Zabbix Agent*

4.7. В поле «**Agent**» задайте IP-адрес или доменное имя компьютера, на котором установлен *Zabbix Agent*.

Если при установке *Zabbix Agent* был указан сетевой порт, отличный от 10050, укажите соответствующий порт.

4.8. Нажмите кнопку «**Add**».

_![](https://kb.comindware.ru/assets/img_63ad9b9235b26.png)_Настройка IP-адреса хоста Zabbix Agent

4.9. Перейдите в раздел «**Monitoring**» > «**Hosts**».

4.10. В списке хостов должна появиться новая запись.

4.11. Подождите приблизительно 2 минуты, пока индикатор статуса доступности ZBX не станет зелёным.

_![](https://kb.comindware.ru/assets/img_63ad999c17b2e.png)_Статус хоста Zabbix Agent

4.12. Если индикатор красный, удостоверьтесь, что:

- сетевой экран на машине, где развернут *Zabbix Server*, разрешает обмен данными через порт 10051;
- сетевой экран на машине, где развернут *Zabbix Agent*, разрешает обмен данными через порт 10050;
- значения `Server` и `ServerActive` в файле конфигурации *Zabbix Agent* `/etc/zabbix/zabbix_agentd.conf` соответствуют IP-адресу *Zabbix Server*:

```
Server=192.168.0.1 # ip-адрес приведён как пример

```

```
ServerActive=192.168.0.1 # ip-адрес приведён как пример

```

**Примечание**
При любых изменениях в файле конфигурации необходимо остановить и снова запустить (при перезапуске используется конфигурация из памяти) сервис Zabbix Agent или перезагрузить компьютер.

## Использованные ресурсы

[Официальная инструкция по установке Zabbix (на английском языке)](https://www.zabbix.com/documentation/current/en/manual/installation/install#installing-zabbix-daemons)

[Инструкция по установке Zabbix (на английском языке)](https://subscription.packtpub.com/book/networking-and-servers/9781784397586/1/ch01lvl1sec09/agent-installation-and-configuration)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
