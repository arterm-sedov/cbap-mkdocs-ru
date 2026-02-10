---
title: 'SSO-аутентификация. Настройка ПО, контроллера домена и ПК пользователя'
kbTitle: 'Аутентификация через единый вход (SSO). Настройка контроллера домена, экземпляра ПО и компьютера конечного пользователя'
kbId: 4613
tags:
  - sso
  - аутентификация
  - единый вход
  - авторизация
  - active directory
  - linux
  - контроллер домена
  - логин
hide: tags
---

# SSO-аутентификация. Настройка ПО, контроллера домена и ПК пользователя {: #sso_authentication_configure}

!!! warning "Внимание!"

    Представленные здесь инструкции зависят от конфигурации сторонних систем и окружения, в котором развёрнут экземпляр ПО **{{ productName }}**.

    Описать все возможные случаи и сочетания конфигураций сторонних систем не представляется возможным, поэтому данные инструкции могут не подойти для вашего случая.

    Для корректной настройки конфигурации контроллера домена, экземпляра ПО и компьютеров конечных пользователей следует обратиться за консультацией в службу поддержки **{{ companyName }}** по адресу:

    <https://www.comindware.ru/company/contact-us/#tab_support>

## Введение {: #sso_authentication_configure_intro }

Здесь представлены инструкции по настройке [контроллера домена](#sso_authentication_configure_dc_configuration), [экземпляра ПО **{{ productName }}**](#sso_authentication_configure_instance) и [компьютера конечного пользователя](#sso_authentication_configure_client_setup) для аутентификации пользователей посредством технологии единого входа (SSO).

Инструкции приведены для контроллера домена под управлением ОС Windows Server 2016, экземпляра ПО под управлением ОС Linux и компьютера конечного пользователя под управлением ОС Windows 10.

!!! question "Определения"

    - **Контроллер домена** — машина с развёрнутыми доменными службами Active Directory.
    - **Домен Active Directory** — группа объектов в сети.
    - **Single Sign-on (SSO)** — технология единого входа, позволяющая пользователям выполнять аутентификацию с использованием одного набора учётных данных в нескольких независимых системах.

## Порядок настройки {: #sso_authentication_configure_sequence }

1. Подготовьте параметры и инфраструктуру аутентификации:

    - Ознакомьтесь с [примерами значений параметров](#sso_authentication_configure_parameter_values_examples).
    - Определите [конфигурацию машины с экземпляром ПО **{{ productName }}**](#sso_authentication_configure_instance).
    - Определите [конфигурацию машины с контроллером домена](#sso_authentication_configure_dc_configuration).
    - При необходимости настройте [надёжные узлы на контроллере домена](#sso_authentication_configure_dc_trusted_hosts).
    - Создайте и настройте [сервисного пользователя домена](#sso_authentication_configure_service_user) и [пользователей для проверки аутентификации](#sso_authentication_configure_test_users).

2. Подготовьте SPN и keytab-файл аутентификации:

    - [Создайте keytab-файл аутентификации и перенесите его на машину с экземпляром ПО **{{ productName }}**](#sso_authentication_configure_keytab_creation).
    - [Настройте обновление keytab-файла аутентификации для аутентификации новых пользователей](#sso_authentication_configure_keytab_update).

3. [Настройте машину с экземпляром ПО **{{ productName }}**](#sso_authentication_configure_linux_host_setup) для использования SSO:

    - [Проверьте требования к машине](#sso_authentication_configure_linux_host_requirements).
    - [Настройте параметры сети](#sso_authentication_configure_linux_host_network_settings).
    - [Проверьте настройку сети](#sso_authentication_configure_linux_host_network_verification).
    - [Настройте синхронизацию времени между контроллером домена и экземпляром ПО](#sso_authentication_configure_time_sync);
    - [Настройте конфигурацию Kerberos](#sso_authentication_configure_kerberos_config)
    - [Установите ПО **{{ productName }}**](#sso_authentication_configure_product_installation)
    - [Включите SSO в экземпляре **{{ productName }}** ПО](#sso_authentication_configure_product_configuration);
    - [Установите и настройте модуль NGINX SPNEGO](#sso_authentication_configure_nginx_spnego)
    - [Синхронизируйте аккаунты экземпляра ПО с сервером каталогов](#sso_authentication_configure_instance_configuration).
    - [Проверьте вывод трассировщика ошибок в Shell](#sso_authentication_configure_kerberos_trace_check)
    - [Запустите и инициализируйте экземпляр ПО](#sso_authentication_configure_client_setup)

4. Настройте клиентские компьютеры для использования Kerberos-аутентификации при подключении к **{{ productName }}**:

    - [Настройте клиентский компьютер](#sso_authentication_configure_client_setup).

## Подготовка параметров и конфигурации машин {: #sso_authentication_configure_preparation .pageBreakBefore }

### Примеры значений параметров {: #sso_authentication_configure_parameter_values_examples }

Здесь примеры значений параметров заключены в угловые скобки `< >`. При настройке конфигурации заменяйте их на фактические значения, как показано в следующей таблице:

| Пример параметра                            | Пример фактического значения      |
| ------------------------------------------- | --------------------------------- |
| `<DCName>`                                  | `DC`                              |
| `<DCName>.<domain.name>`                    | `DC.example.com`                  |
| `HTTP/<DCName>.<domain.name>@<DOMAIN.NAME>` | `HTTP/DC.example.com@EXAMPLE.COM` |
| `<linuxHost>`                               | `server-host-name`                |
| `<domain.controller.ip.address>`            | `192.168.0.254`                   |

!!! note "Примечание"

    Протокол аутентификации Kerberos учитывает регистр символов — там, где в инструкциях даны примеры параметров в верхнем регистре, следует подставлять фактические значения также в верхнем регистре.

### Конфигурации машины `<linuxHost>` с экземпляром ПО {{ productName }} {: #sso_authentication_configure_instance }

В этой статье используются следующие параметры конфигурации машины с экземпляром ПО.

| Параметр             | Значение                  |
| -------------------- | ------------------------- |
| Операционная система | Linux                     |
| Имя хоста            | `<linuxHost>`             |
| IP-адрес хоста       | `<linux.host.ip.address>` |

### Конфигурация машины `<DCName>` с контроллером домена {: #sso_authentication_configure_dc_configuration }

В этой статье используются следующие параметры конфигурации машины с контроллером домена.

| Параметр                    | Значение                         |
| --------------------------- | -------------------------------- |
| Операционная система        | Windows Server 2016              |
| Имя хоста                   | `<DCName>`                       |
| FQDN контроллера домена     | `<DCName>.<domain.name>`         |
| Доменное имя                | `<domain.name>`                  |
| IP-адрес контроллера домена | `<domain.controller.ip.address>` |

### Настройка надёжных узлов на контроллере домена {: #sso_authentication_configure_dc_trusted_hosts }

При необходимости на контроллере домена добавьте хост `<linuxHost>` с экземпляром ПО в список надёжных узлов в рамках интранета, как указано ниже.

1. В Панели управления выберите пункт «**Сеть и интернет**».
2. Откройте пункт «**Свойства: интернет**» (**Internet Properties**).
3. Выберите вкладку «**Безопасность**» (**Security**).
4. Выберите зону «**Надёжные узлы**» (**Trusted sites**).
5. Нажмите кнопку «**Узлы**» (**Sites**).
6. В отобразившемся окне добавьте в список надёжных узлов `<linuxHost>`.

_![Добавление машины с экземпляром ПО в список доверенных узлов на контроллере домена](img/sso_authentication_configure_make_host_machine_trusted.png)_

### Сервисный пользователь домена {: #sso_authentication_configure_service_user .pageBreakBefore }

В домене должен существовать пользователь `<authuser>`, выступающий в роли сервисного аккаунта для модуля аутентификации _NGINX_, работающего на машине `<linuxHost>` с экземпляром ПО.

Если пользователя `<authuser>` в AD нет, необходимо создать его, указав параметры, приведённые в следующей таблице:

| Параметр                                            | Значение                                    |
| --------------------------------------------------- | ------------------------------------------- |
| `name`                                              | `<authuser>`                                |
| `userPrincipalName` (User logon name)               | `HTTP/<DCName>.<domain.name>@<DOMAIN.NAME>` |
| `sAMAccountName` (User logon name pre-Windows 2000) | `<DOMAIN>\<authuser>`                       |

При создании пользователя `<authuser>` на вкладке «**Учётная запись**» (**Account**) необходимо установить флажки «**Пользователь не может менять пароль**» (**User cannot change password**) и «**Срок действия пароля не истекает**» (**Password never expires**), как показано на иллюстрации.

_![Настройка свойств сервисного аккаунта для {{ nginxVariants }}](img/Kerberos_Rocky+Astra_authuser_account_config.png)_

### Пользователи для проверки аутентификации {: #sso_authentication_configure_test_users }

Для проверки работоспособности процедуры аутентификации здесь используются пользователи `user1` и `user2`, см. следующую таблицу:

| Параметр            | Значение              | Значение              |
| ------------------- | --------------------- | --------------------- |
| `name`              | `user1`               | `user2`               |
| `sAmAccountName`    | `<domain>/user1`      | `<domain>/user2`      |
| `userPrincipalName` | `user1@<DOMAIN.NAME>` | `user2@<DOMAIN.NAME>` |

## Подготовка SPN и keytab-файл аутентификации {: #sso_authentication_configure_keytab_prepare .pageBreakBefore }

### Создание keytab-файла аутентификации {: #sso_authentication_configure_keytab_creation }

1. На контроллере домена `<DCName>` выведите список Service Principal Names (SPN), привязанных к пользователю `<authuser>`:

    ``` sh
    setspn -L <authuser>
    ```

2. Добавьте SPN `HTTP/<DCName>.<domain.name>` к пользователю `<authuser>`:

    ``` sh
    setspn -S HTTP/<DCName>.<domain.name> <authuser>
    ```

3. Создайте keytab-файл аутентификации `<authuser>.keytab`:

    **Astra Linux, Debian, DEB-дистрибутивы**

    ``` sh
    ktpass /out <authuser>.keytab /mapuser <authuser> /princ HTTP/<DCName>.<domain.name>@<DOMAIN.NAME> /pass <P@$$W0RD> /crypto RC4-HMAC-NT /ptype KRB5_NT_PRINCIPAL
    ```

    !!! note "Примечание"

        Вместо пароля `<P@$$W0RD>`, подставьте пароль [сервисного пользователя](#sso_authentication_configure_service_user) `<authuser>`.

4. Утилита `ktpass` создаст файл `<authuser>.keytab` в рабочей директории _PowerShell_ на момент вызова команды `ktpass`.
5. [Настройте машину `<linuxHost>`](#sso_authentication_configure_linux_host_setup) с экземпляром ПО.
6. Перенесите keytab-файл `<authuser>.keytab` на машину `<linuxHost>` с экземпляром ПО.

### Обновление keytab-файла аутентификации для аутентификации новых пользователей {: #sso_authentication_configure_keytab_update .pageBreakBefore}

!!! warning "Внимание!"

    Для обеспечения возможности аутентификации новых пользователей, добавленных при синхронизации с сервером каталогов необходимо заново создать keytab-файл на машине `<linuxHost>` с экземпляром ПО.

    Эту операцию необходимо выполнять каждый раз после добавления новых пользователей с сервера каталогов на уже настроенной машине `<linuxHost>`.

    Если не создать новый keytab-файл, пользователи, добавленные с сервера каталогов после создания имеющегося keytab-файла, не смогут войти в систему.

1. [Настройте машину `<linuxHost>`](#sso_authentication_configure_linux_host_setup) с экземпляром ПО.
2. На контроллере домена `<DCName>` выведите список Service Principal Names (SPN), привязанных к пользователю `<authuser>`:

    ``` sh
    setspn -L <authuser>
    ```

3. Добавьте SPN `HTTP/<DCName>.<domain.name>` к пользователю `<authuser>`:

    ``` sh
    setspn -S HTTP/<DCName>.<domain.name> <authuser>
    ```

4. Создайте keytab-файл аутентификации `<authuser>.keytab`:

    **РЕД ОС, RPM-дистрибутивы**

    ```sh
    ktpass /out <authuser>.keytab /mapuser <authuser> /princ HTTP/<DCName>.<domain.name>@<DOMAIN.NAME> /pass <P@$$W0RD> /crypto AES256-SHA1 /ptype KRB5_NT_PRINCIPAL
    ```

    **Astra Linux, Debian, DEB-дистрибутивы**

    ```sh
    ktpass /out <authuser>.keytab /mapuser <authuser> /princ HTTP/<DCName>.<domain.name>@<DOMAIN.NAME> /pass <P@$$W0RD> /crypto RC4-HMAC-NT /ptype KRB5_NT_PRINCIPAL
    ```

    !!! note "Примечание"

        Вместо пароля `<P@$$W0RD>`, подставьте пароль [сервисного пользователя](#sso_authentication_configure_service_user) `<authuser>`.

5. Утилита `ktpass` создаст файл `<authuser>.keytab` в рабочей директории _PowerShell_ на момент вызова команды `ktpass`.
6. Перейдите на уже [настроенную машину `<linuxHost>`](#sso_authentication_configure_linux_host_setup) с экземпляром ПО.
7. Поместите keytab-файл `<authuser>.keytab` в директорию `/etc/nginx/sasl` и сделайте его доступным для чтения:

    ``` sh
    cp /<path_to_keytab>/<authuser>.keytab /etc/nginx/sasl
    chmod 664 /etc/nginx/sasl/<authuser>.keytab
    ```

    Здесь `<path_to_keytab>` — папка, в которой находится keytab-файл `<authuser>.keytab`, взятый с контроллера домена.

8. Выпустите тикет для приложения `HTTP/<DCName>.<domain.name>`:

    ``` sh
    kinit -k -t /etc/nginx/sasl/<authuser>.keytab HTTP/<DCName>.<domain.name>
    ```

## Настройка машины linuxHost с экземпляром ПО {: #sso_authentication_configure_linux_host_setup .pageBreakBefore }

### Требования к машине {: #sso_authentication_configure_linux_host_requirements }

- FQDN `<DCName>.<domain.name>` должно разрешаться.
- Время между машинами `<DCName>` и `<linuxHost>` должно быть синхронизировано.
- Должен быть установлен пакет `libsasl2`.
- Должен быть установлен и сконфигурирован `Kerberos`.
- Должен быть установлен и настроен прокси-сервер _NGINX_ с модулем аутентификации _SPNEGO_ и зависимостями исполняемой среды для него.

### Настройка параметров сети для разрешения DC FQDN {: #sso_authentication_configure_linux_host_network_settings .pageBreakBefore }

#### Изменение файла hosts {: #sso_authentication_configure_linux_host_hosts_file }

1. Откройте файл `/etc/hosts` для редактирования:

    ``` sh
    vim /etc/hosts
    ```

2. Добавьте в файл `hosts` правила для разрешения машины `<linuxHost>` с экземпляром ПО:

    ``` sh
    127.0.0.1                       localhost localhost.localdomain
    127.0.1.1                       <linuxHost>.<domain.name> <linuxHost>
    <domain.controller.ip.address>  <DCName>.<domain.name> <DCName>
    ```

#### Изменение файла resolv.conf {: #sso_authentication_configure_linux_host_resolve_conf }

Если после настройки файла `hosts`, имя контроллера не разрешается, следует отредактировать файл `resolv.conf`.

1. Разрешите редактирование файла `resolv.conf`:

    ``` sh
    chattr -i /etc/resolv.conf
    ```

2. Откройте файл разрешения DNS имен `resolv.conf` для редактирования:

    ``` sh
    vim /etc/resolv.conf
    ```

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

3. Укажите машину `<DCName>` в качестве сервера имён `nameserver`:
{: .pageBreakBefore }

    ``` sh
    domain     <domain.name>
    search     <domain.name>
    nameserver <domain.controller.ip.address>
    ```

4. Запретите редактирование файла `resolv.conf`:

    ``` sh
    chattr +i /etc/resolv.conf
    ```

### Проверка корректности настроек сети {: #sso_authentication_configure_linux_host_network_verification .pageBreakBefore }

1. Убедитесь, что FQDN `<DCName>.<domain.name>` разрешается:

    ``` sh
    # DNS Lookup of DC
    nslookup <DCName>
    nslookup <DCName>.<domain.name>

    host <DCName>.<domain.name>

    # Reverse DNS lookup of `nameserver`
    host <domain.controller.ip.address>
    ```

### Синхронизация времени между машинами DCName и linuxHost {: #sso_authentication_configure_time_sync .pageBreakBefore }

Синхронизацию времени следует настраивать в следующих случаях:

- машины `<DCName>` и `<linuxHost>` находятся в разных часовых поясах;
- машина `<linuxHost>` не подключена к сервису синхронизации времени.

1. Установите пакет `ntp`:

    ``` sh
    apt-get install ntp
    ```

2. Откройте файл конфигурации `ntp.conf` для редактирования:

    ``` sh
    vim /etc/ntp.conf
    ```

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

3. Добавьте в файл конфигурации `ntp.conf` поле `server <DOMAIN.NAME> iburst burst prefer`:

    ``` sh
    driftfile /etc/ntp/drift
    server <DOMAIN.NAME> iburst burst prefer
    server 127.127.1.0 iburst
    fudge  127.127.1.0 stratum 10

    restrict default noquery nomodify
    restrict 127.0.0.1
    ```

4. Примените настройки:

    ``` sh
    systemctl start ntp
    ```

5. Удостоверьтесь, что служба `ntp` работает:

    ``` sh
    systemctl status ntp
    ```

### Настройка конфигурации Kerberos {: #sso_authentication_configure_kerberos_config .pageBreakBefore }

#### Установка вспомогательных пакетов {: #sso_authentication_configure_kerberos_helpers_install }

1. Установите модуль `libsasl2`:

    ``` sh
    apt install libsasl2-modules-gssapi-mit
    ```

2. Убедитесь, что модуль установлен:

    ``` sh
    apt list libsasl*
    ```

3. Убедитесь, что установлены пакеты `krb5-user`, `krb5-config` и зависимости для них:

    ``` sh
    which krb5-user
    which krb5-config
    ```

4. Установите пакеты `kerberos-kdc`:

    ``` sh
    apt-get install krb5-kdc
    ```

#### Настройка аутентификации Kerberos {: #sso_authentication_configure_kerberos_auth .pageBreakBefore }

1. Откройте файл конфигурации Kerberos для редактирования:

    ``` sh
    vim /etc/krb5.conf
    ```

2. Отредактируйте файл `krb5.conf` согласно следующему примеру:
{: .pageBreakInsideAvoid}

    **Astra Linux, Альт Сервер, Debian, DEB-дистрибутивы**

    ``` sh
    #astra/debian-winbind
    [libdefaults]
        default_realm = <DOMAIN.NAME>
        kdc_timesync = 1
        ccache_type = 4
        forwardable = true
        proxiable = true

        fcc-mit-ticketflags = true
        dns_lookup_realm = false
        dns_lookup_kdc = false
        v4_instance_resolve = false
        v4_name_convert = {
            host = {
                rcmd = host
                ftp = ftp
            }
            plain = {
                something = something-else
            }
        }

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

    **Альт Сервер**
    {: .pageBreakBefore }

    ``` sh
    includedir /etc/krb5.conf.d/
    [logging]
    # default = FILE:/var/log/krb5libs.log
    # kdc = FILE:/var/log/krb5kdc.log
    # admin_server = FILE:/var/log/kadmind.log

    [libdefaults]
    dns_lookup_kdc = true
    dns_lookup_realm = false
    ticket_lifetime = 24h
    renew_lifetime = 7d
    forwardable = true
    rdns = false
    default_realm = <DOMAIN.NAME>
    default_ccache_name = KEYRING:persistent:%{uid}

    [realms]
    <DOMAIN.NAME> = {
        kdc = <DCName>.<domain.name>
        admin_server = <DCName>.<domain.name>
        default_domain = <domain.name>
    }

    [domain_realm]
    <.domain.name> = <DOMAIN.NAME>  {{ productName }}
    <domain.name> = <DOMAIN.NAME>
    ```

### Установка экземпляра ПО {: #sso_authentication_configure_product_installation .pageBreakBefore }

1. Установите вспомогательне ПО для **{{ productName }}** согласно инструкциям в параграфе _«[Порядок установки вспомогательного ПО][deploy_guide_linux_prerequisites_install_order]»_.
2. Установите ПО **{{ productName }}** согласно инструкциям в параграфе _«[Порядок установки ПО {{ productName }}][deploy_guide_linux_install_order]»_.

3. Создайте экземпляр ПО **{{ productName }}**, согласно инструкциям в параграфе _«[Создание экземпляра ПО {{ productName }}][deploy_guide_linux_instance_create]»_. Далее `<instanceName>` — имя созданного экземпляра ПО.

!!! warning "Не запускайте и не инициализируйте экземпляр ПО"

    После создания экземпляра ПО **{{ productName }}** не запускайте и не инициализируйте его.

    Вместо этого переходите к следующим этапам настройки SSO.

### Включение SSO в экземпляре ПО {: #sso_authentication_configure_product_configuration .pageBreakBefore }

Для включения функционала SSO аутентификации в экземпляре ПО необходимо настроить его файл конфигурации.

1. Откройте для редактирования файл конфигурации экземпляра ПО (`<instanceName>` — имя экземпляра ПО):

    ``` sh
    vim /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

2. Добавьте в файл директиву `isLinuxSSOAuthorization: true`

_![Пример файла <instanceName>.yml с директивой  isLinuxSSOAuthorization: true](img/sso_authentication_configure_yml_file_example.png)_

### Установка и настройка модуля NGINX SPNEGO {: #sso_authentication_configure_nginx_spnego .pageBreakBefore }

Перед установкой ознакомьтесь с [документацией модуля NGINX SPNEGO][spnego_http_auth_nginx_module] (раздел _Installation_).

1. Все последующие команды следует выполнять от имени суперпользователя `root`. Для этого введите команду:

    --8<-- "linux_sudo.md"

2. Установите модуль _NGINX-SPNEGO_:

    - **Astra Linux (версии 1.8.3 и выше)**

        Установите модуль `ngx_http_auth_spnego_module.so` из пакета `nginx-spnego-module_1.26.3-1_amd64.deb`, который поставляется в составе инсталлятора **{{ productName }}** для Astra Linux 1.8.3 и выше.

    - **Astra Linux (версии ниже 1.8.3), Debian, DEB-дистрибутивы**

        ``` sh
        apt-get update
        apt-get install -y build-essential git wget

        cd /usr/src
        wget http://nginx.org/download/nginx-<nginx.version>.tar.gz
        tar -xvzf nginx-<nginx.version>.tar.gz
        cd nginx-<nginx.version>

        git clone https://github.com/stnoonan/spnego-http-auth-nginx-module.git

        ./configure --add-module=./spnego-http-auth-nginx-module
        make
        make install
        ```

    - **РЕД ОС, RPM-дистрибутивы**

        ``` sh
        yum groupinstall -y "Development Tools"
        yum install -y git wget

        cd /usr/src
        wget http://nginx.org/download/nginx-<nginx.version>.tar.gz
        tar -xvzf nginx-<nginx.version>.tar.gz
        cd nginx-<nginx.version>

        git clone https://github.com/stnoonan/spnego-http-auth-nginx-module.git

        ./configure --add-module=./spnego-http-auth-nginx-module
        make
        make install
        ```

    - **Альт Сервер**

        ``` sh
        apt-get update
        apt-get install -y gcc make git wget

        cd /usr/src
        wget http://nginx.org/download/nginx-<nginx.version>.tar.gz
        tar -xvzf nginx-<nginx.version>.tar.gz
        cd nginx-<nginx.version>

        git clone https://github.com/stnoonan/spnego-http-auth-nginx-module.git

        ./configure --add-module=./spnego-http-auth-nginx-module
        make
        make install
        ```

3. Добавьте модуль _SPNEGO_ к рабочей конфигурации _NGINX_:

    **Любые ОС (кроме Astra Linux 1.8.3):**

    ``` sh
    ln -s /etc/nginx/modules-available.d/http_auth_spnego.conf /etc/nginx/modules-enabled/
    ```

    **Astra Linux 1.8.3 и выше:**

    Добавьте первой строкой в основной файл конфигурации _NGINX_ (`/etc/nginx/nginx.conf`) директиву загрузки модуля _SPNEGO_:

    ``` nginx
    load_module modules/ngx_http_auth_spnego_module.so;
    ```

4. Поместите keytab-файл `<authuser>.keytab` в директорию конфигурации NGINX и сделать его доступным для чтения:

    ``` sh
    cp /<path_to_keytab>/<authuser>.keytab /etc/nginx
    chmod 664 /etc/nginx/<authuser>.keytab
    ```

    Здесь `<path_to_keytab>` — папка, в которой находится keytab-файл `<authuser>.keytab`, взятый с контроллера домена.

5. Откройте для редактирования описание веб-приложения _NGINX_ для экземпляра ПО `<instanceName>`:

    ``` sh
    vim /etc/nginx/sites-available.d/comindware<instanceName>
    ```

6. Отредактируйте файл `comindware<instanceName>` согласно следующему примеру (раскомментируйте все директивы `auth_gss` ):

    !!! warning "Для Astra Linux 1.8.3 и выше"

        Перед включением директивы `auth_gss on;` в конфигурации экземпляра ПО убедитесь, что модуль `ngx_http_auth_spnego_module.so` установлен и загружен, как указано на шагах 1–2.

    ``` { .sh .pageBreakAfter title="Пример файла comindware&lt;instanceName&gt;" }

    ...

    location / {
        # Authentication Configuration
        # Раскомментируйте директивы auth_gss
        auth_gss on;
        auth_gss_realm <DOMAIN.DNS>;
        auth_gss_keytab /etc/nginx/<authuser>.keytab;
        auth_gss_service_name HTTP/<authuser>.<domain.dns>;
        auth_gss_allow_basic_fallback on;

        proxy_set_header  X-Request-ID        $request_id;
        proxy_read_timeout 10000;
        proxy_connect_timeout 10000;
        proxy_send_timeout 10000;
        root                /var/www/<instancename>/;
        fastcgi_pass        unix:/var/www/<instancename>/App_Data/<instancename>.socket;
        include             /etc/nginx/fastcgi.conf;
    }
    ```

7. Проверьте синтаксис веб-приложения _NGINX_ для экземпляра ПО `<instanceName>`:

    ``` sh
    nginx -t
    ```

8. Примените настройки и перезапустите _NGINX_:

    ``` sh
    nginx -s reload
    ```

9. Проверьте статус сервиса _NGINX_:

    ``` sh
    systemctl status nginx
    ```

10. Проверьте статус сервиса экземпляра ПО `<instanceName>`:
{: .pageBreakBefore }

    ``` sh
    systemctl status comindware<instanceName>
    ```

### Синхронизация аккаунтов экземпляра ПО с сервером каталогов {: #sso_authentication_configure_instance_configuration .pageBreakBefore }

1. Войдите в экземпляр ПО с помощью браузера.
2. Откройте свойства [подключения к серверу каталогов][ad_connection], которое будет использоваться для синхронизации аккаунтов.
3. На вкладке «**Основные**» установите флажок «**Использовать по умолчанию**».
4. На вкладке «**Сопоставление атрибутов**» нажмите кнопку «**Восстановить**».
5. Сохраните свойства подключения.
6. Перезапустите экземпляр ПО:

    ``` sh
    systemctl restart comindware<instance_name>
    ```

### Проверка работы функционала Kerberos на машине linuxHost {: #sso_authentication_configure_kerberos_check .pageBreakBefore }

1. Создайте тикет для приложения `HTTP/<DCName>.<domain.name>`:

    ``` sh
    kinit -k -t /etc/nginx/<authuser>.keytab HTTP/<DCName>.<domain.name>
    ```

2. Выведите список тикетов:

    ``` sh
    klist
    ```

### Проверка вывода трассировщика ошибок в Shell {: #sso_authentication_configure_kerberos_trace_check }

1. Выполните команду:

    ``` sh
    KRB5_TRACE=/dev/stdout kinit -k -t /etc/nginx/<authuser>.keytab HTTP/<DCName>.<domain.name>
    ```

### Запуск и инициализация экземпляра ПО {: #sso_authentication_configure_client_setup .pageBreakBefore }

После настройки SSO необходимо запустить и инициализировать экземпляр ПО **{{ productName }}**:

1. Запустите экземпляр ПО согласно инструкциям в параграфе «_[Запуск экземпляра ПО][deploy_guide_linux_instance_start]_».
2. Запустите экземпляр ПО согласно инструкциям в параграфе «_[Инициализация {{ productName }}][deploy_guide_linux_initialize]_».

## Настройка клиента {: #sso_authentication_configure_client_setup .pageBreakBefore }

По умолчанию SSO-авторизация работает в браузерах Edge и Google Chrome, но необходимо в параметрах безопасности браузера добавить сайт в зону местной интрасети и включить режим «**Автоматический вход в сеть только в зоне интрасети**». Сведения о настройке других браузеров см. в соответствующей документации.

_![Окно настройки параметров безопасности браузера](https://kb.comindware.ru/assets/img_63bcecc1b498f.png)_

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]
- [Аутентификация через Active Directory. Настройка контроллера домена и экземпляра ПО][ad_authentication_configure]
- [Аутентификация через OpenID Connect. Настройка подключения и служб][openid_connection]
- [Синхронизация с сервером каталогов (Active Directory)][accounts_dc_sync]
- [Конфигурация экземпляра, компонентов ПО и служб. Настройка][configuration_files_linux]
- [Развёртывание веб-сервера NGINX в Linux][nginx_deploy]
- [Модуль GeoIP для NGINX. Установка и настройка][nginx_geoid_deploy]
- [Документация модуля NGINX SPNEGO][spnego_http_auth_nginx_module]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
