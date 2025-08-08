---
title: Модуль GeoIP для NGINX. Установка и настройка. Краткое руководство
kbId: 4610
---

# Модуль GeoIP для NGINX. Установка и настройка. Краткое руководство

## Введение

Для ограничения доступа к сайту пользователей из определенных стран с помощью веб-сервера NGINX, можно использовать модуль GeoIP.

Здесь представлена краткая инструкция по установке и настройке конфигурации модуля GeoIP в ОС Linux для работы с **{{ productName }}**.

Подробные сведения по установке и настройке модуля GeoIP представлены на следующих сайтах:

- <https://dev.maxmind.com/geoip/updating-databases?lang=en>
- <https://itsecforu.ru/2018/08/29/как-установить-mod_geoip-для-apache-в-rhel-и-centos/>

## Установка

1. Для установки необходимых пакетов в операционной системе выполните указанные ниже команды.

   - **Astra/Debian/Ubuntu**: `sudo apt-get install nginx-module-geoip`
   - **Alt**: `sudo apt-get install nginx-geoip`
   - **CentOS**: `yum install nginx-module-geoip`
2. Обновите базы GeoIP до актуальной версии с помощью команд:

   ```
   mv /usr/share/GeoIP/GeoIP.dat /usr/share/GeoIP/GeoIP.dat_bak
   cd /usr/share/GeoIP/
   wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
   gunzip GeoIP.dat.gz
   ```
3. С помощью команды `nginx -V` убедитесь, что веб-сервер собран с параметром `--with-http_geoip_module`. В противном случае необходимо самостоятельно собрать модуль NGINX. Исходные коды GeoIP находятся в открытом доступе.

## Ограничение доступа для пользователей из определенных стран

1. Чтобы запретить доступ к сайту пользователям из Украины и США, в папке с файлами конфигурации веб-сервера NGINX создайте файл `block.map.include` со следующими директивами:

   ```
   geoip_country /usr/share/GeoIP/GeoIP.dat; 
       map $geoip_country_code $allowed_country { 
               default yes;
               UA no;
               US no;
       }
   ```
2. Чтобы разрешить использование сайта только пользователям из России, Китая и Тайваня, используйте в файле конфигурации следующие директивы:

   ```
   geoip_country /usr/share/GeoIP/GeoIP.dat; 
       map $geoip_country_code $allowed_country {
           default no;
           RU yes;
           CN yes;
           TW yes;
       }
   ```
3. В файле конфигурации `/etc/nginx/nginx.conf` в разделе `http` добавьте следующую директиву: `include include/block.map.include;`
4. В настройках хоста (раздел `server`) добавьте следующую директиву:

   ```
   if ($allowed_country = no) {
       return 404;
   }
   ```
5. Примените изменения: `# nginx -s reload`

## Пример скрипта автоматического обновления

Приведенный ниже скрипт загружает последнюю версию базы данных GeoIP каждый месяц. Добавьте его в файл `/etc/cron.monthly`.

```
#!/bin/sh
GEOIP_MIRROR="http://geolite.maxmind.com/download/geoip/database"
GEOIPDIR=/usr/share/GeoIP
TMPDIR=
DATABASES="GeoLiteCity GeoLiteCountry/GeoIP asnum/GeoIPASNum GeoIPv6"
if [ -d "${GEOIPDIR}" ]; then
cd $GEOIPDIR
if [ -n "${DATABASES}" ]; then
TMPDIR=$(mktemp -d geoipupdate.XXXXXXXXXX)
echo "Updating GeoIP databases..."
for db in $DATABASES; do
fname=$(basename $db)
wget --no-verbose -t 3 -T 60 "${GEOIP_MIRROR}/${db}.dat.gz" -O "${TMPDIR}/${fname}.dat.gz"
gunzip -fdc "${TMPDIR}/${fname}.dat.gz" > "${TMPDIR}/${fname}.dat"
mv "${TMPDIR}/${fname}.dat" "${GEOIPDIR}/${fname}.dat"
chmod 0644 "${GEOIPDIR}/${fname}.dat"
done
[ -d "${TMPDIR}" ] && rm -rf $TMPDIR
fi
fi
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
