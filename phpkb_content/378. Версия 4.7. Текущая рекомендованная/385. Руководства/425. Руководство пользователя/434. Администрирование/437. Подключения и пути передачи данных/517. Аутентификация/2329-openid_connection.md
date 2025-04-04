---
title: Аутентификация через OpenID Connect. Настройка подключения и служб
kbId: 2329
---

# Аутентификация через OpenID Connect. Настройка подключения и служб

    - [Настройка страницы согласия OAuth](#настройка-страницы-согласия-oauth)
    
        - [Настройка сведений о приложении](#настройка-сведений-о-приложении)
        - [Настройка запрашиваемых разрешений для приложения](#настройка-запрашиваемых-разрешений-для-приложения)
    - [Настройка учётных данных клиента OAuth](#настройка-учётных-данных-клиента-oauth)
- [Настройка подключения в {{ productName }}](#настройка-подключения-в-comindware-business-application-platform)
- [Настройка API и служб Google Cloud — этап 2](#настройка-api-и-служб-google-cloud--этап-2)
- [Настройка реестра Windows для включения аутентификации через OpenID Connect в {{ productName }}](#настройка-реестра-windows-для-включения-аутентификации-через-openid-connect-в-comindware-business-application-platform)
- [Настройка ОС Linux для включения аутентификации через OpenID Connect в {{ productName }}](#настройка-ос-linux-для-включения-аутентификации-через-openid-connect-в-comindware-business-application-platform)
- [Вход в {{ productName }}](#вход-в-comindware-business-application-platform)

## Проверка адреса сервера {{ productName }}

1. Откройте раздел [«**Администрирование**» — «**Глобальная конфигурация**»][administration].
2. Удостоверьтесь, что **URL-адрес сервера** начинается с `https://`.

_![Проверка адреса сервера](https://kb.comindware.ru/assets/openid_connection_check.png)_

## Настройка API и служб Google Cloud — этап 1

1. Откройте веб-сайт <https://console.developers.google.com/>
2. Если проекты отсутствуют, нажмите кнопку «**Create project**».
3. Если имеются проекты, нажмите кнопку «**Select a project**» и в отобразившемся окне нажмите кнопку «**New project**».

_![Создание проекта](https://kb.comindware.ru/assets/openid_connection_project_creation.png)_
4. Отобразится страница «**New project**».
5. Введите «**Project name**», например *Client ID*.
6. Нажмите кнопку «**Create**».

_![Страница свойств нового проекта](https://kb.comindware.ru/assets/openid_connection_project_properties.png)_
7. На отобразившейся странице нажмите кнопку «**Enable APIs and services**».

_![Включение API и служб](https://kb.comindware.ru/assets/openid_connection_api_switch_on.png)_
8. В поле «**Search for APIs & Services**» найдите **Site Verification API**.

_![Поиск Site Verification API](https://kb.comindware.ru/assets/openid_connection_api_search.png)_
9. Перейдите к разделу «**Site Verification API**».

_![Переход к разделу Site Verification API](https://kb.comindware.ru/assets/openid_connection_api_verification.png)_
10. Нажмите кнопку «**Enable**».

_![Включение Site Verification API](https://kb.comindware.ru/assets/openid_connection_api_verification_enabled.png)_

### Настройка страницы согласия OAuth

1. В меню слева выберите пункт «**OAuth consent screen**».
2. В разделе «**User type**» выберите «**External**» и нажмите кнопку «**Create**».

_![Настройка страницы согласия OAuth — тип пользователя](https://kb.comindware.ru/assets/openid_connection_oath_user_type.png)_

#### Настройка сведений о приложении

1. Заполните обязательные поля разделе «**App information**»:

    - в поле «**App name**» укажите, например «*Сайт Mycompany.ru»;*
    - в поле «**User support email**» укажите, например, свой адрес эл. почты._![Настройка страницы согласия OAuth — название приложения и адрес службы поддержки](https://kb.comindware.ru/assets/openid_connection_oath_new_app.png)_
2. В разделе «**App domain**» в поле «**Application home page**» введите [адрес сервера](#проверка-адреса-сервера-comindware-business-application-platform), указанный в глобальной конфигурации {{ productName }}, например [https://mycompany.ru](https://mycompany.ru/)
3. В разделе «**Authorized domains**» нажмите кнопку «**Add domain**» и введите в поле «**Authorized domain 1**» доменное имя сервера без префикса `https://`, например *mycompany.ru*
4. В разделе «**Developer contact information**» в поле «**Email addresses**» введите, например, свой адрес эл. почты.
5. Нажмите кнопку «**Save and continue**».

_![Настройка страницы согласия OAuth — главная страница приложения, домен, контактная информация разработчика](https://kb.comindware.ru/assets/openid_connection_oath_agreement.png)_

#### Настройка запрашиваемых разрешений для приложения

1. На странице «**Scopes**» нажмите кнопку «**Add or remove scopes**».
2. В открывшейся форме установите три первых флажка и нажмите кнопку «**Update**».

_![Настройка страницы согласия OAuth — добавление разрешений для приложения](https://kb.comindware.ru/assets/openid_connection_oath_permission.png)_
3. В нижней части страницы «**Scopes**» нажмите кнопку «**Save and continue**».

_![Настройка страницы согласия OAuth — сохранение настроенных разрешений](https://kb.comindware.ru/assets/openid_connection_oath_permission_saving.png)_
4. На странице «**Test users**» кнопку «**Save and continue**».

_![Настройка страницы согласия OAuth — пропуск теста пользователей](https://kb.comindware.ru/assets/openid_connection_oath_user_test.png)_
5. На странице «**Summary**» проверьте сведения и нажмите кнопку «**Back to dashboard**».

_![Настройка страницы согласия OAuth — проверка введенных сведений](https://kb.comindware.ru/assets/openid_connection_oath_check.png)_
6. На открывшейся странице в разделе «**Publishing status**» нажмите кнопку «**Publish app**».
7. В окне подтверждения нажмите кнопку «**Confirm**».

_![Настройка страницы согласия OAuth — публикация приложения](https://kb.comindware.ru/assets/openid_connection_oath_app_publication.png)_
8. Статус публикации изменится на «**In production**».

_![Настройка страницы согласия OAuth — статус опубликованного приложения](https://kb.comindware.ru/assets/openid_connection_oath_app_status.png)_

### Настройка учётных данных клиента OAuth

1. В левой панели выберите пункт «**Credentials**».
2. На странице «**Credentials**» нажмите кнопку «**Create credentials**».
3. В раскрывающемся меню выберите пункт «**OAuth client ID**»

_![Переход к созданию клиента OAuth](https://kb.comindware.ru/assets/openid_connection_oath_client_creation.png)_
4. В поле «**Application type**» выберите пункт «**Web application**».
5. В поле «Name» введите имя клиента, например «*OAuth client 1*».
6. В разделе «**Authorized JavaScript origins**» нажмите кнопку «**Add URI**».
7. Введите [адрес сервера](#проверка-адреса-сервера-comindware-business-application-platform), указанный в глобальной конфигурации {{ productName }}, например [https://mycompany.ru](https://mycompany.ru/)
8. Нажмите кнопку «**Create**».

_![Настройка и сохранение учётных данных клиента OAuth](https://kb.comindware.ru/assets/openid_connection_oath_client_settings.png)_
9. Отобразится окно с учётными данными созданного клиента OAuth.

_![Созданный клиент OAuth](https://kb.comindware.ru/assets/openid_connection_oath_new_client.png)_
10. Не закрывайте эту вкладку в браузере, чтобы использовать данные с неё на последующих шагах.
11. Чтобы впоследствии посмотреть «**Client ID**» и «**Client Secret**», нажмите гиперссылку с названием клиента в таблице «**OAuth 2.0 Client IDs**» в разделе «**Credentials**».

_![Таблица учётных данных клиентов OAuth](https://kb.comindware.ru/assets/openid_connection_oath_client_table.png)_

## Настройка подключения в **{{ productName }}**

1. Перейдите в раздел «**Администрирование**» — «**Подключения**».
2. Нажмите кнопку «**Cоздать**».
3. В раскрывающемся меню выберите пункт «**Аутентификация через OpenID Connect**».

_![Создание подключения для аутентификации через OpenID Connect](https://kb.comindware.ru/assets/openid_connection_creation.png)_
4. Откроется окно «**Новое подключение**».
5. В поле «**Название**» введите название подключения, например «*Client ID*».
6. В поле «**Поставщик удостоверений**» выберите пункт «**Google**».
7. В поле «**ID клиента**» вставьте **Client ID**, скопированный из Google Cloud.
8. В поле «**Ключ клиента**» вставьте **Client secret**, скопированный из Google Cloud.
9. В поле «**Домены электронной почты**» оставьте домен *gmail.com*.
10. В поле «**Группа**» выбирать группу необязательно.
11. Поле «**Адрес перенаправления после входа**» будет заполнено автоматически после создания подключения.
12. Нажмите кнопку «**Создать**».

_![Настройка нового подключения для аутентификации через OpenID Connect](https://kb.comindware.ru/assets/openid_connection_settings.png)_
13. Откройте созданное подключение.
14. Скопируйте в буфер обмена **адрес перенаправления после входа**.
15. Нажмите кнопку «**Сохранить**».

![Сформированный адрес перенаправления после входа](https://kb.comindware.ru/assets/openid_connection_redirect_address.png)
16. Откройте страницу «**Администрирование**» – «**Регистрация и вход**».
17. Активируйте выключатель «**Разрешить вход**» на плитке «**Google OpenID Connect**».

_![Включение входа через Google OpenID Connect](https://kb.comindware.ru/assets/openid_connection_google.png)_
18. Нажмите кнопку «**Сохранить**».

## Настройка API и служб Google Cloud — этап 2

1. Откройте веб-сайт Google Cloud <https://console.developers.google.com/>
2. В левой панели выберите пункт «**Credentials**».
3. Откройте параметры созданного ранее клиента *OAuth Client 1*, нажав гиперссылку с его названием в таблице «**OAuth 2.0 Client IDs**».
4. В разделе «**Authorized redirect URIs**» нажмите кнопку «**Add URI**».
5. В поле «**URIs 1**» введите ранее скопированный **адрес перенаправления после входа** включая префикс `https://`.
6. Нажмите кнопку «**Save**».

_![Добавление авторизованного адреса перенаправления после входа в клиент OAuth в Google Cloud](https://kb.comindware.ru/assets/openid_connection_google_cloud.png)_

## Настройка реестра Windows для включения аутентификации через OpenID Connect в {{ productName }}

1. Запустите редактор реестра Windows: `regedit.exe`.
2. Откройте раздел реестра `Computer -> HKEY_LOCAL_MACHINE -> SOWTWARE->Сomindware -> Instances -> имя_экземпляра_Comindware_Business_Application_Platform`.
3. Дважды щёлкните параметр `IsFederationAuthEnabled`.
4. Если значение этого параметра **0**, измените его на **1**.
5. Нажмите кнопку «**OK**».

_![Включение федеративной аутентификации для экземпляра {{ productName }} с помощью реестра Windows](https://kb.comindware.ru/assets/openid_connection_windows.png)_
6. В командной строке от администратора выполните команду: `iisreset /restart`
7. Дождитесь перезапуска служб IIS.

![Перезапуск IIS с помощью командной строки](https://kb.comindware.ru/assets/openid_connection_iis_reconnect.png)

## Настройка ОС Linux для включения аутентификации через OpenID Connect в {{ productName }}

1. Перейдите в режим суперпользователя `root`:

```
su -
```

или

```
sudo -i
```
2. Добавьте в файл `/etc/hosts` строку:

```
"xxx.xxx.xxx.xxx" "mycompany.ru"
```

Здесь `xxx.xxx.xxx.xxx` — IP-адрес, `mycompany.ru` адрес сервера **{{ productName }}**, указанный в [*глобальной конфигурации {{ productName }}*](#проверка-адреса-сервера-comindware-business-application-platform) (без указания протокола `HTTP` или `HTTPS`).
3. В файле `/usr/share/comindware/configs/instance/<instanceName>.yml` для параметра `isFederationAuthEnabled` установите значение `1`:

```
isFederationAuthEnabled: 1
```

Примечание

Здесь и далее `<instanceName>` — имя экземпляра ПО.
4. Сформируйте SSL-сертификат на сервере NGINX. Например, согласно инструкциям в статье «[*Генерация SSL сертификата для NGINX (openssl)*](https://webguard.pro/web-services/nginx/generacziya-ssl-sertifikata-dlya-nginx-openssl.html)».
5. Откройте для редактирования файл конфигурации NGINX:

```
vim /etc/nginx/sites-available/comindware<instanceName>
```
6. Настройте конфигурацию SSL-сертификата согласно следующему примеру (добавьте выделенные жёлтым цветом директивы):

```
server {
    listen 80 default;
    listen 443 ssl;

    root /var/www/<instanceName>;
    server_name mycompany.ru;

    ssl_certificate /etc/nginx/ssl/nginx.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx.key;

    client_max_body_size 300m;
    fastcgi_read_timeout 10000;
    location / {
        proxy_read_timeout 10000;
                    proxy_connect_timeout 10000;
                    proxy_send_timeout 10000;
                    root          /var/www/<instanceName>/;
                    fastcgi_pass  unix:/var/www/<instanceName>/App_Data/comindware.socket;
                    include       /etc/nginx/fastcgi.conf
                    }
}
```

{{ pdfEndOfBlockHack }}
7. Проверьте конфигурацию NGINX:

```
nginx -t
```
8. Перезапустите **{{ productName }}**:

```
systemctl restart elasticsearch nginx comindware<instanceName>
```

## Вход в {{ productName }}

1. Откройте веб-сайт экземпляра {{ productName }}, например [https://mycompany.ru](https://mycompany.ru/)
2. Нажмите кнопку «**Войти как администратор**».

_![Переход к странице входа администратора](https://kb.comindware.ru/assets/openid_connection_administrator_entry.png)_
3. Введите свои учётные данные и нажмите кнопку «**Войти**».

_![Вход с аккаунтом администратора](https://kb.comindware.ru/assets/openid_connection_administrator.png)_
4. Выйдите из системы.
5. Отобразится страница входа с кнопкой «**Войти с помощью Google**».

_![Кнопка «Войти с помощью Google»](https://kb.comindware.ru/assets/openid_connection_google_entry.png)_
6. На этом настройка входа через OpenID Connect завершена. Теперь пользователи смогут входить в **{{ productName }}** с помощью своих аккаунтов Google.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
