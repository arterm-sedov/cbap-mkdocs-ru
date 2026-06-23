---
title: 'Настройка мониторинга с использованием Zabbix'
kbId: 5160
url: 'https://kb.comindware.ru/article.php?id=5160'
updated: '2026-06-20 20:24:42'
---

# Настройка мониторинга с использованием Zabbix

Здесь представлены инструкцию развёртыванию системы мониторинга **{{ productName }}** на базе Zabbix версии 7.4: импорт шаблона, привязка к хосту, установка компонентов на Linux-хосте и настройка обязательных макросов.

## Порядок развёртывания

Для настройки мониторинга выполните следующие операции:

1. **Подготовка серверной инфраструктуры**:

   - Установите и настройте Zabbix Server версии 7.4.
   - Установите Zabbix Agent 2 на целевые серверы с **{{ productName }}**.
2. **Получение и импорт пакета мониторинга**:

   - Запросите пакет для развёртывания мониторинга в компании **Comindware**.
   - Импортируйте шаблон `zbx_export_templates_comindware.yaml` в Zabbix.
3. **Установка компонентов на целевом сервере**:

   - Скопируйте установщик `comindware-host-installer/` на сервер.
   - Запустите `install.sh` от имени `root`.
4. **Настройка хоста в Zabbix**:

   - Создайте хост в Zabbix.
   - Привяжите шаблон **Comindware Complete Monitoring** к хосту.
   - Настройте обязательные макросы: `{$INSTANCENAME}` и `{$FQDN}`.
5. **Проверка работоспособности**:

   - Проверьте поступление данных в веб-интерфейсе Zabbix.
   - Убедитесь в корректной работе триггеров и дашбордов.

## Состав пакета мониторинга

Чтобы развёрнуть Zabbix для мониторинга **{{ productName }}**, запросите пакет для развёртывания мониторинга в компании **Comindware**.

Пакет для развёртывания мониторинга включает следующие компоненты:

| Путь | Назначение |
| --- | --- |
| `zbx_export_templates_comindware.yaml` | Готовый шаблон конфигурации Zabbix (*Comindware Complete Monitoring**) с группой шаблонов для мониторинга* *{{ productName }}* *(*Comindware Monitoring\*\*) |
| `comindware-host-installer/` | Установщик UserParameter, скриптов, stub\_status nginx, автоматическая установка `python3`/`gawk` при необходимости, настройка группы `adm` для чтения логов nginx |
| `comindware-host-installer/install.sh` | Скрипт установщика (запускать от `root`) |
| `comindware-host-installer/files/zabbix_agent2.d/custom_metrics.conf` | Конфигурация пользовательских ключей: `ignite.metrics`, `nginx.access.*`, `service.*` и др. |
| `comindware-host-installer/files/scripts/` | Скрипты сбора метрик: `ignite_metrics.sh`, `nginx_access_log_metrics.sh`, `nginx_access_log_metrics.py`, `service_memory.sh`, `service_processes.sh` |
| `comindware-host-installer/files/nginx/zabbix_stub_status_81.conf` | Конфигурация nginx `stub_status` на `127.0.0.1:81` |

## Предварительные условия

Перед началом настройки убедитесь, что выполнены следующие требования:

- **Серверная инфраструктура:**
  - **Zabbix Server** (или Zabbix Proxy) версии **7.4** с веб-интерфейсом.
  - На целевых серверах установлены:
  - **Zabbix Agent 2** (`zabbix-agent2`);
  - **systemd** (система инициализации);
  - **NGINX** — веб-сервер (требуется для метрик из журнала доступа и `stub_status`).
- **Сетевая конфигурация:**
  - Шаблон использует **активный опрос** (тип элементов `ZABBIX_ACTIVE`).
  - Агент должен иметь корректные параметры:
    - `Server` — для пассивных проверок (при необходимости);
    - `ServerActive` — для отправки активных проверок.
  - Обеспечена сетевая доступность с Zabbix Server/Proxy до контрольного URL: `https://{$FQDN}/api/health`.
  - Настроены TLS, DNS и правила сетевого экрана для доступа к API.
- **Сертификаты и безопасность:** доверенный SSL/TLS-сертификат на веб-сервере.
- **Журналирование:**
  - Для метрик **журнала NGINX** имеется файл `/var/log/nginx/<INSTANCENAME>-access.log`.
  - Журнал хранится в формате JSON-подобных строк с полями `time`, `status`, `duration` (типовой `log_format` **{{ productName }}**).

## Импорт шаблона в Zabbix

1. Войдите в веб-интерфейс Zabbix: **Data collection → Templates** (или **Configuration → Templates** в зависимости от версии UI).
2. Нажмите кнопку **Import**.
3. Выберите файл шаблона: `release/zbx_export_templates_comindware.yaml`
4. Настройте опции импорта:

   - выберите параметры согласно политике вашей организации;
   - обычно: создавать/обновлять обнаруженные сущности при необходимости.
     5. Завершите импорт и проверьте результат:
   - убедитесь, что появился шаблон **Comindware Complete Monitoring**;
   - шаблон должен находиться в группе **Comindware Monitoring**.

## Создание хоста и привязка шаблона

1. Выберите пункты **Data collection → Hosts → Create host** (или откройте существующий хост).
2. Настройте параметры хоста:

   **Host name:**

   - должен совпадать с параметром `Hostname=` в файле `zabbix_agent2.conf` на сервере;
   - должен совпадать со значением, передаваемым установщику через параметр `--hostname`.

   **Groups:**

   - выберите организационную группу хостов;
   - не путать с группой шаблонов **Comindware Monitoring**.
3. Привяжите шаблон:

   - перейдите на вкладку **Templates → Link templates**;
   - выберите шаблон **Comindware Complete Monitoring**.
4. Сохраните конфигурацию хоста

## Настройка макросов на уровне хоста

### Обязательные макросы

Многие ключи мониторинга содержат макрос `{$INSTANCENAME}` и имена юнитов `systemd` вида `comindware{$INSTANCENAME}.service`.

Значение макроса **должно** совпадать с именем экземпляра **{{ productName }}** в путях на сервере.

**Пример:** журнал nginx `/var/log/nginx/<instanceName>-access.log` → экземпляр `<instanceName>`

1. Откройте настройки хоста.
2. Выберите пункт **Macros**.
3. Задайте следующие макросы:

| Макрос | Назначение | Пример значения |
| --- | --- | --- |
| `{$INSTANCENAME}` | Имя экземпляра **{{ productName }}** (используется в путях журналов, Apache Ignite, юнитах `systemd`) | `<instanceName>` |
| `{$FQDN}` | Публичное имя DNS для проверки состояния API по HTTPS (`https://{$FQDN}/api/health`). В шаблоне **нет** значения по умолчанию — без этого макроса сценарий работать не будет | `app.example.com` |

### Рекомендуемые макросы

Проверьте и при необходимости переопределите следующие макросы на уровне хоста:

| Макрос | Назначение | Значение по умолчанию |
| --- | --- | --- |
| `{$NET_IF}` | Имя сетевого интерфейса для виджетов и триггеров | `ens192` |
| `{$NGINX.STUB_STATUS.HOST}` | Хост для получения `stub_status` через `web.page.get` | `127.0.0.1` |
| `{$NGINX.STUB_STATUS.PORT}` | Порт для `stub_status` | `81` |
| `{$NGINX.STUB_STATUS.PATH}` | Путь к расположению `stub_status` | `nginx_status` |
| `{$NGINX.ACCESS.WINDOW}` | Временное окно (в секундах) для метрик из журнала доступа | `300` |

Прочие макросы

Остальные макросы в шаблоне определяют пороги срабатывания триггеров и фильтры Low-Level Discovery (LLD).

Изменяйте их в соответствии с политикой мониторинга вашей организации.

Файловые системы

Мониторинг заполнения файловых систем по точкам монтирования покрывает блок `Filesystems` в шаблоне (автоматическое обнаружение и элементы `vfs.fs.*`).

Отдельные макросы для каталогов не требуются.

## Установка компонентов на хосте

### Подготовка к установке

Скопируйте на целевой сервер каталог `release/comindware-host-installer/` (например, в `/root/comindware-host-installer/`).

### Запуск установщика

1. Выполните установку системы мониторинга **от пользователя root**:

   ```
   cd /root/comindware-host-installer
   sudo bash ./install.sh \\
   --instance <INSTANCENAME> \\
   --zabbix-server-ip <zabbix_server_or_proxy_ip> \\
   --hostname <имя_хоста_как_в_Zabbix>
   ```

   **Параметры установщика:**

   - `--instance <INSTANCENAME>` — имя экземпляра **{{ productName }}**. Если не указан, автоматически определяется из имени файла `/usr/share/comindware/configs/instance/*.yml` (при наличии ровно одного файла).
   - `--zabbix-server-ip <IP>` — IP-адрес Zabbix Server или Zabbix Proxy. Можно опустить, если `zabbix_agent2.conf` уже настроен вручную.
   - `--hostname <hostname>` — имя хоста для конфигурации Zabbix Agent 2. Можно опустить, если `zabbix_agent2.conf` уже настроен вручную.
2. Установщик автоматически выполнит следующие операции:

   - **Установка конфигурации метрик** — копирование `custom_metrics.conf` в `/etc/zabbix/zabbix_agent2.d/`.
   - **Установка скриптов:**
     - копирование скриптов в `/etc/zabbix/scripts/`;
     - нормализация окончаний строк (CRLF → LF) для всех скриптов.
   - **Создание конфигурации инстанса:**
     - запись файла `comindware_instance.conf`.
   - **Установка зависимостей:**
     - попытка установки **Python 3** (при наличии пакетного менеджера);
     - опциональная установка **gawk**.
   - **Настройка NGINX** — включение `stub_status`:
     - Astra Linux, Debian, DEB-дистрибутивы: `sites-available`/`sites-enabled`;
     - РЕД ОС, RPM-дистрибутивы: `/etc/nginx/conf.d/zabbix_stub_status_81.conf`.
   - **Настройка прав доступа** — добавление пользователя `zabbix` в группу `adm` (если группа существует).
   - **Перезапуск службы** — перезапуск `zabbix-agent2`.

### Зависимости скриптов

- **Метрики журнала NGINX:**
  - основной парсер: **Python 3** + скрипт `nginx_access_log_metrics.py`
  - резервный вариант: **gawk** (при отсутствии Python)
- **Метрики Apache Ignite:**
  - требуемые утилиты: `bash`, `grep`, `awk`, `sed`, `tail`, `date`;
  - доступ на чтение логов Ignite под пользователем `zabbix`;
  - пути по умолчанию в `ignite_metrics.sh` можно переопределить через `/etc/zabbix/scripts/ignite_config.conf` (файл создаётся вручную при необходимости, не входит в релиз).

### Настройка прав доступа к логам nginx

Пользователь `zabbix` должен иметь возможность читать файл `/var/log/nginx/<INSTANCENAME>-access.log`.

**Проверка прав доступа:**

```
sudo -u zabbix test -r /var/log/nginx/<INSTANCENAME>-access.log && echo OK
```

**Если проверка не прошла:**

На семействе Debian/Ubuntu установщик автоматически добавляет пользователя `zabbix` в группу `adm` (если она существует). Для других дистрибутивов или при отсутствии группы `adm` настройте права доступа вручную:

- Используйте ACL (Access Control Lists)
- Настройте группу для файлов логов
- Измените политику logrotate/nginx

### Нормализация окончаний строк между Linux и Windows

Скрипты должны использовать переводы строк в формате **LF** (в стиле Unix).

Если столкнулись с ошибками при проверках, либо скрипты редактировались или копировались не через установщик, например в Windows, запустите нормализацию вручную:

```
sudo sed -i 's/\\r$//' /etc/zabbix/scripts/nginx_access_log_metrics.sh
sudo sed -i 's/\\r$//' /etc/zabbix/scripts/nginx_access_log_metrics.py
```

## Проверка работоспособности

### Проверка на хосте

Выполните тестовые запросы к агенту (подставьте имя вашего инстанса вместо `<INSTANCENAME>`):

```
# Проверка метрик Apache Ignite
sudo zabbix_agent2 -t 'ignite.metrics[cpu_cur_load,<INSTANCENAME>]'

# Проверка метрик журнала доступа NGINX
sudo zabbix_agent2 -t 'nginx.access.status_200[<INSTANCENAME>,300]'

# Проверка статуса службы Comindware
sudo zabbix_agent2 -t 'service.status[comindware<INSTANCENAME>.service]'

# Проверка stub_status NGINX
sudo zabbix_agent2 -t 'web.page.get["127.0.0.1","nginx_status","81"]'
```

### Проверка в веб-интерфейсе Zabbix

1. Перейдите в раздел мониторинга: **Monitoring → Hosts → Latest data**.
2. Проверьте поступление данных:

   - убедитесь в появлении данных по элементам шаблона;
   - для **API health** проверьте успешное выполнение шагов веб-сценария;
   - сервер должен успешно обращаться к `https://{$FQDN}/api/health`.

--8<-- "related_topics_heading.md"

- [Развёртывание Zabbix Server](zabbix_server_deploy.html#zabbix_server_deploy "Zabbix Server, Zabbix Agent, Zabbix Frontend и MySQL. Установка и настройка")
- [Развёртывание Zabbix Agent](zabbix_agent_deploy.html#zabbix_agent_deploy "Zabbix Agent. Установка и настройка")
- [Общие сведения о развёртывании Zabbix](zabbix_deploy.html#zabbix_deploy "Zabbix. Установка и настройка")

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
