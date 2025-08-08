---
title: Аутентификация через Active Directory. Настройка контроллера домена и экземпляра ПО
kbId: 4605
---

# Аутентификация через Active Directory. Настройка контроллера домена и экземпляра ПО

Внимание!

Представленные здесь инструкции зависят от конфигурации сторонних систем и окружения, в котором развёрнут экземпляр ПО **{{ productName }}** (далее «экземпляр ПО»).

Описать все возможные варианты и сочетания конфигураций сторонних систем не представляется возможным, поэтому данные инструкции могут не подойти для вашего случая.

Для корректной настройки конфигурации контроллера домена, экземпляра ПО и компьютеров конечных пользователей следует обратиться за консультацией в службу поддержки **Comindware** по адресу:

<https://www.comindware.ru/company/contact-us/#tab_support>

## Введение

Здесь представлены инструкции по настройке контроллера домена и экземпляра ПО **{{ productName }}** для аутентификации пользователей через Active Directory. Инструкции приведены для контроллера домена под управлением ОС Windows и экземпляра ПО под управлением ОС Linux.

## Определения

- **Контроллер домена** — машина с развёрнутыми доменными службами Active Directory.
- **Домен Active Directory** — группа объектов в сети.

## Примеры значений параметров

Здесь примеры значений параметров заключены в угловые скобки `< >`. При настройке конфигурации заменяйте их на фактические значения, как показано в следующей таблице.

| Пример параметра | Пример фактического значения |
| --- | --- |
| `<DCName>` | `DC` |
| `<DCName>.<domain.name>` | `DC.example.com` |
| `HTTP/<DCName>.<domain.name>@<DOMAIN.NAME>` | `HTTP/DC.example.com@EXAMPLE.COM` |
| `<linuxHost>` | `server-host-name` |
| `<domain.controller.ip.address>` | `192.168.0.254` |

Примечание

Протокол аутентификации Kerberos учитывает регистр символов — там, где в инструкциях даны примеры параметров в верхнем регистре, следует подставлять фактические значения также в верхнем регистре.

## Конфигурация машины linuxHost с экземпляром ПО {{ productName }}

| Параметр | Значение |
| --- | --- |
| Операционная система | Linux |
| Имя хоста | `<linuxHost>` |
| IP-адрес хоста | `<linux.host.ip.address>` |

## Конфигурация машины DCName с контроллером домена

| Параметр | Значение |
| --- | --- |
| Операционная система | Windows Server 2016 |
| Имя хоста | `<DCName>` |
| FQDN контроллера домена | `<DCName>.<domain.name>` |
| Доменное имя | `<domain.name>` |
| IP-адрес контроллера домена | `<domain.controller.ip.address>` |

## Настройка машины linuxHost с экземпляром ПО для Astra Linux и Ubuntu

### Настройка конфигурации Kerberos

1. Установите пакеты `krb5-user`, `krb5-config` и зависимости для них:

   ```
   apt install krb5-user krb5-config
   ```
2. Откройте файл конфигурации Kerberos для редактирования:

   ```
   vim /etc/krb5.conf
   ```
3. Отредактируйте файл `krb5.conf` согласно следующему примеру:

   ```
   #astra-winbind
   [libdefaults]
       default_realm = <DOMAIN.NAME>
       kdc_timesync = 1
       ccache_type = 2
       forwardable = true
       proxiable = true
       fcc-mit-ticketflags = true
       dns_lookup_realm = false
       default_ccache_name = DIR:/tmp
   [realms]
       <DOMAIN.NAME> = {
           kdc = <DCName>.<domain.name>
           admin_server = <DCName>.<domain.name>
           default_domain = <domain.name>
       }
   [domain_realm]
       .<domain.name> = <DOMAIN.NAME>
       <domain.name> = <DOMAIN.NAME>
   [login]
       krb4_convert = false
       krb4_get_tickets = false
   ```

### Настройка конфигурации экземпляра ПО

1. Войдите в экземпляр ПО с помощью браузера.
2. Настройте [подключение к серверу каталогов][ad_connection], которое будет использоваться для синхронизации аккаунтов.
3. На вкладке «**Основные**»:

   - установите флажок «**Использовать по умолчанию**»;
   - в поле «**Аутентификация пользователей**» — выберите протокол проверки подлинности **Kerberos**.
4. Остальные параметры настройте согласно конфигурации сервера каталогов.
5. Сохраните свойства подключения.
6. Перезапустите экземпляр ПО:

   ```
   systemctl restart comindware<instance_name>
   ```

   Здесь `<instance_name>` — имя экземпляра ПО.

### Проверка вывода трассировщика ошибок в Shell

1. Выполните команду, чтобы проверить работоспособность Kerberos:

   ```
   KRB5_TRACE=/dev/stdout kinit <username>
   ```

   Здесь `<username>` — любой пользователь домена, для которого известен пароль.

## Настройка машины linuxHost с экземпляром ПО для Rocky Linux

### Настройка конфигурации Kerberos

1. Установите пакеты `krb5-user`, `krb5-config` и зависимости для них:

   ```
   yum install krb5-workstation
   ```
2. Откройте файла конфигурации Kerberos для редактирования:

   ```
   vim /etc/krb5.conf
   ```
3. Отредактируйте файл `krb5.conf` согласно следующему примеру:

   ```
   [libdefaults]
       default_realm = <DOMAIN.NAME>
       kdc_timesync = 1
       ccache_type = 2
       forwardable = true
       proxiable = true
       fcc-mit-ticketflags = true
       dns_lookup_realm = false
   [realms]
       <DOMAIN.NAME> = {
           kdc = <DCName>.<domain.name>
           admin_server = <DCName>.<domain.name>
           default_domain = <domain.name>
       }
   [domain_realm]
       .<domain.name> = <DOMAIN.NAME>
       <domain.name> = <DOMAIN.NAME>
   [login]
       krb4_convert = false
       krb4_get_tickets = false
   ```
4. Откройте файл конфигурации `kcm_default_ccache` для редактирования:

   ```
   vim /etc/krb5.conf.d/kcm_default_ccache
   ```
5. Отредактируйте файл `kcm_default_ccache` согласно следующему примеру:

   ```
   [libdefaults]
   default_ccache_name = DIR:/tmp
   ```

### Настройка конфигурации экземпляра ПО

1. Войдите в экземпляр ПО с помощью браузера.
2. Настройте [подключение к серверу каталогов][ad_connection], которое будет использоваться для синхронизации аккаунтов.
3. На вкладке «**Основные**»:

   - установите флажок «**Использовать по умолчанию**»;
   - в поле «**Аутентификация пользователей**» — выберите протокол проверки подлинности **Kerberos**.
4. Остальные параметры настройте согласно конфигурации сервера каталогов.
5. Сохраните свойства подключения.
6. Перезапустите экземпляр ПО:

   ```
   systemctl restart comindware<instance_name>
   ```

### Проверка вывода трассировщика ошибок в Shell

1. Выполните команду, чтобы проверить работоспособность Kerberos:

   ```
   KRB5_TRACE=/dev/stdout kinit <username>
   ```

   Здесь `<username>` — имя любого пользователя домена, для которого известен пароль.

--8<-- "related_topics_heading.md"

**[Сервер каталогов. Настройка подключения][ad_connection]**

**[Синхронизация с сервером каталогов (Active Directory)][accounts_dc_sync]**

**[Аутентификация через единый вход (SSO). Настройка контроллера домена, экземпляра ПО и компьютера конечного пользователя][sso_authentication_configure]**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
