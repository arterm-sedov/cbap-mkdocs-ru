---
title: NGINX. Установка и настройка
kbId: 4611
---

# NGINX. Установка и настройка

## Введение

Здесь представлена краткая инструкция по установке и настройке конфигурации HTTP-сервера NGINX в Linux для использования NGINX в сочетании с {{ productName }}.

Внимание!

Если продуктовый контур **{{ productName }}** изолирован внешним межсетевым экраном, необходимо настроить правила фильтрации для разрешения входящего трафика HTTP/HTTPS и WS/WSS в контур **{{ productName }}**.

Подробные сведения по установке и настройке NGINX представлены на следующих сайтах:

- <http://nginx.org/ru/docs/beginners_guide.html>
- <https://ruvds.com/ru/helpcenter/kak-nastroit-nginx-na-ubuntu-20-04/>
- <https://webdevblog.ru/bezopasnost-nginx-kak-uluchshit-konfiguraciju-vashego-servera/>

## Установка NGINX

Войдите в систему под учётной записью, имеющей разрешение на запуск команды `sudo`, и выполните следующие команды:

```
sudo apt update
sudo apt install NGINX

```

Первая команда обновляет базу данных пакетов, доступных для установки. Вторая — устанавливает компоненты NGINX.

После установки NGINX настройте его конфигурацию.

## Настройка сервера NGINX

Конфигурация NGINX хранится в файле `NGINX.conf`. По умолчанию файл `NGINX.conf` находится в следующей папке:

- `/etc/NGINX` или `/usr/local/etc/NGINX` — в системах Linux;
- `<папка установки NGINX>/conf` — в системах Windows.

### Пример конфигурации прокси-сервера

```
server {
    server_name  domain.com;
    reset_timedout_connection  on;
    listen 80;
    location /robots.txt { root /var/www/html; }
    return 301 https://$host$request_uri;
}

server {
    server_name  domain.com;
    reset_timedout_connection  on;
    listen 443 ssl;
    location / {
    proxy_pass http://backend-server:8081/;
    proxy_next_upstream error timeout invalid_header http_500 http_503;

    # do not set HOST header
    proxy_set_header  Host                $host;
    proxy_set_header  X-Forwarded-For     $proxy_add_x_forwarded_for;
    proxy_set_header  X-Forwarded-Proto   $scheme;
    proxy_set_header  X-Real-IP           $remote_addr;
    proxy_connect_timeout     90;
    proxy_send_timeout        1000;
    proxy_read_timeout        1000;

    # enable WebSockets
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    client_max_body_size 100m;
    error_log /var/log/NGINX/domain-error.log error;
    access_log /var/log/NGINX/domain-access.log;
  }
}

```

### Настройка UFW

Для защиты подключений рекомендуется настроить межсетевой экран с помощью утилиты Uncomplicated Firewall (UFW).

Просмотреть профили приложений можно с помощью команды: `$ sudo ufw app list`

Для просмотра и изменения параметров используйте соответствующие команды. Например, команда для подключения к NGINX посредством HTTP: `$ sudo ufw allow 'NGINX HTTP'`

Команда для проверки статуса: `$ sudo ufw status`

### Отключение команды server\_tokens

По умолчанию команда `server_tokens`возвращает номер версии NGINX.

Чтобы скрыть версию NGINX, отключите команду `server_tokens`, добавив в файле конфигурации NGINX следующую директиву: `server_tokens off`

### Контроль ресурсов и ограничения

Для предотвращения DoS-атак на NGINX можно установить ограничения на размер буфера для всех клиентов. Для это в разделе `server` файла конфигурации NGINX используйте следующие директивы:

- `client_body_buffer_size` — размер буфера тела запроса клиента. Типовое значение — 8 или 16 КБ, но рекомендуется установить его равным 1 КБ с помощью следующей директивы: `client_body_buffer_size 1k`.
- `client_header_buffer_size` — размер буфера заголовка запроса клиента. Размер буфера 1 КБ подходит для большинства запросов, например: `client_header_buffer_size 1k`
- `client_max_body_size` — максимально допустимый размер тела клиентского запроса, например: `client_max_body_size`. Размера 1 КБ должно быть достаточно, но его следует увеличить, если загрузка файлов осуществляется методом POST.
- `large_client_header_buffers` —максимальное количество и размер буферов, которые будут использоваться для чтения больших заголовков клиентских запросов. Например, чтобы установить максимальное количество буферов равным 2, каждый с максимальным размером 1 КБ, и разрешить прием URI-данных размером 2 КБ, используйте следующую директиву: `large_client_header_buffers 2 1k`

### Настройка NGINX для включения заголовков безопасности

Чтобы дополнительно защитить веб-сервер NGINX, можно добавить определенные заголовки HTTP. Ниже приведены рекомендованные варианты таких заголовков.

#### X-Frame-Options

Заголовок HTTP-ответа `X-Frame-Options` используется чтобы указать, разрешено ли браузеру отображать страницу в фреймах `<frame>`, `<iframe>`, `<embed>` и `<object>`. Чтобы разрешить отображение страниц во фреймах только с того же домена, на котором размещен веб-сайт, добавьте следующую директиву в раздел server файла конфигурации NGINX:

```
add_header X-Frame-Options "SAMEORIGIN";

```

#### Strict-Transport-Security

[HTTP Strict Transport Security (HSTS)](https://www.acunetix.com/blog/articles/what-is-hsts-why-use-it/) — это механизм, позволяющий веб-сайту сообщать браузеру, что доступ к нему разрешен только через безопасное соединение (HTTPS). Если веб-сайт объявил политику HSTS, браузер должен отклонять все HTTP-соединения и запретить пользователям принимать незащищенные SSL-сертификаты. Чтобы сервер NGINX возвращал заголовок HSTS, добавьте следующую директиву в раздел `server`:

```
add_header Strict-Transport-Security "max-age=31536000; includeSubdomains; preload";

```

#### Политика CSP

Политика безопасности контента (CSP) защищает веб-сервер от определенных типов атак, включая атаки с использованием [Cross-site Scripting](https://www.acunetix.com/websitesecurity/cross-site-scripting/) (XSS) и атаки с использованием data injection. Чтобы реализовать CSP, добавьте заголовок Content-Security-Policy, как показано в следующем примере (фактический заголовок должен быть настроен в соответствии с вашими уникальными требованиями) в раздел `server`:

```
add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;

```

#### Заголовок X-XSS-Protection

Заголовок HTTP X-XSS-Protection поддерживают браузеры IE и Safari. Он не требуется для современных браузеров, если используется строгая политика безопасности содержимого. Однако, чтобы предотвратить атаки типа XSS при использовании старых браузеров (которые не поддерживают CSP), добавьте заголовок X-XSS Protection в раздел `server`:

```
add_header X-XSS-Protection "1; mode=block”;

```

### Настройка SSL и наборов шифров Cipher Suite

Конфигурация NGINX по умолчанию позволяет использовать небезопасные старые версии протокола TLS, которые н рекомендуется применять. Следует изменить конфигурацию для поддержки только новых, безопасных версий TLS. Для этого добавьте следующую директиву в раздел `server` файла конфигурации NGINX:

```
ssl_protocols TLSv1.2 TLSv1.3;

```

Укажите конкретные наборы шифров (криптографических алгоритмов), чтобы предотвратить использование уязвимых наборов не поддерживаются. Либо для автоматического выбора шифра на стороне сервера добавьте следующую директиву в раздел `server`:

```
ssl_prefer_server_ciphers on;

```

### Регулярное обновление сервера

Следует регулярно устанавливать последние обновления NGINX с официального сайта: <http://nginx.org/en/security_advisories.html>

### Проверка состояния сервера

Команда проверки статуса веб-сервера NGINX:

```
$ systemctl status NGINX

```

_![Статус веб-сервера NGINX](https://kb.comindware.ru/assets/Picture_10.png)_

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
