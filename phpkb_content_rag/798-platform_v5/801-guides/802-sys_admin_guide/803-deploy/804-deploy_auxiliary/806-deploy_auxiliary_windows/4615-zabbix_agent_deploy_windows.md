---
title: 'Zabbix Agent. Инструкции по установке для Windows'
kbId: 4615
url: 'https://kb.comindware.ru/article.php?id=4615'
updated: '2026-06-20 20:24:43'
---

# Zabbix Agent. Инструкции по установке для Windows

## Введение

Программное обеспечение *Zabbix Agent* позволяет осуществлять мониторинг устройств, на которые оно установлено. Для сбора и отображения данных мониторинга используется ПО *Zabbix Server*. См. статью «[Zabbix Server, Zabbix Agent, Zabbix Frontend и MySQL. Инструкции по установке](https://kb.comindware.ru/article.php?id=4607)».

Здесь представлены инструкции по установке и настройке Zabbix Agent в операционной системе MS Windows.

## Установка Zabbix Agent из MSI-пакета

1. Скачайте MSI-пакет *Zabbix Agent* по ссылке <https://www.zabbix.com/download_agents>

   ![Скачивание MSI-пакета Zabbix Agent](https://kb.comindware.ru/assets/img_63bbfec30de92.png)

   Скачивание MSI-пакета Zabbix Agent
2. Запустите установку MSI-пакета.
3. В процессе установки выберите папку для установки Zabbix Agent.
4. Настройте конфигурацию службы *Zabbix Agent*:

- **Host name** — имя хоста;
- **Zabbix server IP/DNS** — IP-адрес *Zabbix Server* (в запросах с неизвестных адресов будет отказано);
- **Agent listen port** — номер сетевого порта *Zabbix Agent* (10050 по-умолчанию);
- **Server or Proxy for active checks** — IP-адрес сервера для активных проверок агента Zabbix;
- **Enable PSK** — установите этот флажок, чтобы впоследствии настроить зашифрованный канал связи между *Zabbix Agent* и *Zabbix Server*;
- **Add agent location to the PATH** — установите этот флажок, чтобы добавить путь к агенту в переменную среды PATH.

  ![Настройка конфигурации службы Zabbix Agent](https://kb.comindware.ru/assets/img_63bbfef9ee8a0.png)

  Настройка конфигурации службы Zabbix Agent

## Проверка установки Zabbix Agent

1. Откройте *Брандмауэр Защитника Windows* в режиме администратора.
2. Перейдите на вкладку «**Правила для входящих подключений**».
3. Удостоверьтесь, что установщик *Zabbix Agent* создал правило, разрешающее входящие запросы по сетевому порту 10050.
4. Если правила нет, создайте его и перезагрузите компьютер.

   ![Проверка наличия правила для входящих подключений Zabbix Agent](https://kb.comindware.ru/assets/img_63bbff2a30cfd.png)

   Проверка наличия правила для входящих подключений Zabbix Agent
5. Откройте приложение «*Службы*».
6. Удостоверьтесь, что служба *Zabbix Agent* находится в состоянии «**Выполняется**».
7. Если состояние службы *Zabbix Agent* отличается от «**Выполняется**», установите состояние «**Выполняется**» и перезагрузите компьютер.

   ![Проверка состояния Zabbix Agent в диспетчере служб](https://kb.comindware.ru/assets/img_63bbff44016eb.png)

   Проверка состояния Zabbix Agent в диспетчере служб

## Добавление Windows-хоста в сеть мониторинга

1. Откройте *Zabbix Frontend* (см. *«[Zabbix Server, Zabbix Agent, Zabbix Frontend и MySQL. Инструкции по установке](https://kb.comindware.ru/article.php?id=4607)*). Для э того в адресной строке браузера наберите: `<http://zabbix-server-ip-address:8080>`
2. Откройте раздел «**Monitoring**» > «**Hosts**» и нажмите кнопку «**Create host**».

   ![Создание хоста](https://kb.comindware.ru/assets/img_63bc000e92138.png)

   Создание хоста
3. Задайте имя хоста в поле «**Host name**».
4. Выберите шаблон «**Template OS Linux by Zabbix agent**».
5. Создайте группу мониторинга для хоста или добавьте его в существующую группу.
6. Под полем «**Interfaces**» нажмите кнопку «**Add**» и в раскрывающемся меню выберите пункт «**Agent**».

   ![Настройка свойств хоста Zabbix Agent](https://kb.comindware.ru/assets/img_63bbffd613538.png)

   Настройка свойств хоста Zabbix Agent
7. В поле «**Agent**» задайте IP-адрес или доменное имя компьютера, на котором установлен *Zabbix Agent*.
8. Если при установке *Zabbix Agent* был указан сетевой порт, отличный от 10050, укажите используемый порт
9. Нажмите кнопку «**Add**».

   ![Настройка IP-адреса хоста Zabbix Agent](https://kb.comindware.ru/assets/img_63bbffb0a5b4a.png)

   Настройка IP-адреса хоста Zabbix Agent
10. Перейдите в раздел «**Monitoring**» > «**Hosts**».
11. В списке хостов должна появиться новая запись.
12. Подождите приблизительно 2 минуты, пока индикатор статуса доступности ZBX не станет зелёным.

    ![Статус хоста Zabbix Agent](https://kb.comindware.ru/assets/img_63bbfe8013410.png)

    Статус хоста Zabbix Agent
13. Если индикатор красный, удостоверьтесь, что:

    - сетевой экран на машине, где развернут *Zabbix Server*, разрешает обмен данными через порт 10051;
    - сетевой экран и (или) *Брандмауэр Защитника Windows* на машине, где развернут *Zabbix Agent*, разрешает обмен данными через порт 10050;
    - значения `Server` и `ServerActive` в файле конфигурации *Zabbix Agent* `/etc/zabbix/zabbix_agentd.conf` соответствуют IP-адресу *Zabbix Server*:

    ```
    Server=192.168.0.1 # ip-адрес приведён как пример
    ServerActive=192.168.0.1 # ip-адрес приведён как пример
    ```

    Примечание

    При любых изменениях в файле конфигурации необходимо остановить и снова запустить (при перезапуске используется конфигурация из памяти) сервис *Zabbix Agent* или перезагрузить компьютер.

## Использованные ресурсы

*[Официальная инструкция по установке Zabbix Agent в Windows из MSI-пакета (на английском языке)](https://www.zabbix.com/documentation/current/en/manual/installation/install_from_packages/win_msi)*