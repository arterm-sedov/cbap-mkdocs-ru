---
title: Полное удаление вспомогательных компонентов ПО
kbId: 4625
---

# Полное удаление вспомогательных компонентов ПО

## Введение

В этой статье представлены инструкции по полному удалению вспомогательных компонентов ПО **{{ productName }}**:

- среды исполнения Java Runtime Environment (JRE);
- брокера сообщений Kafka;
- платформы Mono;
- платформы .NET 6.0;
- обратного прокси-сервера NGINX.

Удаление вспомогательных компонентов ПО может потребоваться, например, в следующих случаях:

- для устранения возможных конфликтов файлов перед установкой его новой версии;
- для переустановки ПО после аварийных сбоев.

Инструкции представлены для следующих ОС: Альт Сервер, Astra Linux, Debian, РЕД ОС, Rocky Linux и Ubuntu.

Примечание

Удаление ПО **{{ productName }}** по инструкциям в этой статье не приведёт к удалению установленных версий ПО и развёрнутых экземпляров ПО.

Сведения о расположении файлов экземпляров ПО см. в статье *«[Пути и содержимое папок экземпляра ПО][paths]»*.

## Определения

- **ПО** — программное обеспечение **{{ productName }}**.
- **Экземпляр ПО** — развёрнутый веб-сервер на основе ПО.

## Остановка экземпляров ПО — все ОС Linux

Перед удалением вспомогательных компонентов ПО, остановите все работающие экземпляры ПО.

1. Перейдите в режим суперпользователя:

```
sudo -i
```
2. Остановите экземпляр ПО (*`<instancename>`* — имя экземпляра ) и удостоверьтесь, что он остановлен:

```
systemctl stop comindware<instancename>
systemctl status comindware<instancename>
```
3. Если развёрнуто несколько экземпляров ПО, повторите шаг 2 для остальных экземпляров.

## Удаление компонентов ПО — Альт Сервер

1. Перед выполнением последующих инструкций перейдите в режим суперпользователя:

```
sudo -i
```

### Удаление JRE

1. Удалите бинарные файлы `bellsoft-java17-runtime`:

```
rm -rf /usr/lib/jvm/bellsoft-java17-runtime-amd64/
```
2. Удалите ссылку на исполняемые файлы:

```
rm /usr/bin/java
```
3. Удалите конфигурацию JRE:

```
rm /var/www/.cmw_environment/java
```

### Удаление Kafka

1. Удалите службу Kafka:

```
systemctl stop kafka.service
systemctl disable kafka.service
rm /usr/lib/systemd/system/kafka.service
systemctl daemon-reload
systemctl reset-failed
```
2. Удалите бинарные файлы Kafka:

```
rm -rf /usr/share/kafka
```
3. Удалите журналы Kafka:

```
rm -rf /var/log/comindware/.kafka
```
4. Удалите конфигурацию Kafka:

```
rm /var/www/.cmw_environment/kafka
```

### Удаление Mono

1. Удалите пакеты `mono-core` и `mono-devel` вместе с их зависимостями:

```
apt-get remove --purge -y mono-devel mono-core
```
2. Удалите конфигурацию Mono:

```
rm /var/www/.cmw_environment/mono
```

### Удаление .NET 6.0

1. Удалите бинарные файлы .NET:

```
rm -rf /usr/share/dotnet/
```
2. Удалите ссылку на исполняемые файлы .NET:

```
rm /usr/bin/dotnet
```
3. Удалите конфигурацию .NET:

```
rm /var/www/.cmw_environment/dotnet
```

### Удаление NGINX

1. При необходимости сохраните резервную копию файла конфигурации NGINX: `/etc/nginx/sites-available`
2. Удалите пакет `nginx` и его зависимости:

```
apt-get remove --purge -y nginx
```
3. Удалите конфигурацию NGINX:

```
rm /var/www/.cmw_environment/nginx
```

## Удаление компонентов ПО — Astra Linux

1. Перед выполнением последующих инструкций перейдите в режим суперпользователя:

```
sudo -i
```

### Удаление JRE

1. Удалите пакет `bellsoft-java17-runtime`:

```
apt-get remove --purge -y bellsoft-java17-runtime
```
2. Удалите конфигурацию JRE:

```
rm /var/www/.cmw_environment/java
```

### Удаление Kafka

1. Удалите службу Kafka:

```
systemctl stop kafka.service
systemctl disable kafka.service
rm /usr/lib/systemd/system/kafka.service
systemctl daemon-reload
systemctl reset-failed
```
2. Удалите бинарные файлы Kafka:

```
rm -rf /usr/share/kafka
```
3. Удалите журналы Kafka:

```
rm -rf /var/log/comindware/.kafka
```
4. Удалите конфигурацию Kafka:

```
rm /var/www/.cmw_environment/kafka
```

### Удаление Mono

1. Удалите бинарные файлы Mono:

```
rm -rf /etc/mono/ \
    /usr/lib/libmono* \
    /usr/lib/libMono* \
    /usr/lib/mono/ \
    /usr/lib/mono-source-libs
```
2. Удалите ссылки на исполняемые файлы:

```
rm -rf /usr/bin/mono \
    /usr/bin/mono-* \
    /usr/bin/monop \
    /usr/bin/monop2 \
    /usr/bin/monolinker \
    /usr/bin/mcs \
    /usr/bin/dmcs \
    /usr/bin/fastcgi-mono-server4
```
3. Удалите справочные файлы (man-страницы):

```
rm -rf /usr/share/man/man1/xsp4.1.gz \
    /usr/share/man/man1/mono.1.gz \
    /usr/share/man/man1/fastcgi-mono-server4.1.gz

```
4. Удалите конфигурацию Mono:

```
rm /var/www/.cmw_environment/mono
```

### Удаление .NET 6.0

1. Удалите бинарные файлы .NET:

```
rm -rf /usr/share/dotnet/
```
2. Удалите ссылку на исполняемые файлы .NET:

```
rm /usr/bin/dotnet
```
3. Удалите конфигурацию .NET:

```
rm /var/www/.cmw_environment/dotnet
```

### Удаление NGINX

1. При необходимости сохраните резервную копию файла конфигурации NGINX: `/etc/nginx/sites-available`
2. Удалите пакеты `nginx`, `nginx-core` и  `nginx-common` вместе с их зависимостями:

```
apt-get remove --purge -y nginx nginx-core nginx-common
```
3. Удалите конфигурацию NGINX:

```
rm /var/www/.cmw_environment/nginx
```

## Удаление компонентов ПО — Debian

1. Перед выполнением последующих инструкций перейдите в режим суперпользователя:

```
sudo -i
```

### Удаление JRE

1. Удалите пакет `axiomjdk-java17-runtime-pro`:

```
apt-get remove --purge -y axiomjdk-java17-runtime-pro
```
2. Удалите ссылку на исполняемые файлы:

```
rm /usr/bin/java
```
3. Удалите конфигурацию JRE:

```
rm /var/www/.cmw_environment/java
```

### Удаление Kafka

1. Удалите службу Kafka:

```
systemctl stop kafka.service
systemctl disable kafka.service
rm /usr/lib/systemd/system/kafka.service
systemctl daemon-reload
systemctl reset-failed
```
2. Удалите бинарные файлы Kafka:

```
rm -rf /usr/share/kafka
```
3. Удалите журналы Kafka:

```
rm -rf /var/log/comindware/.kafka
```
4. Удалите конфигурацию Kafka:

```
rm /var/www/.cmw_environment/kafka
```

### Удаление Mono

1. Удалите пакет Mono `mono-runtime` и его зависимости:

```
apt-get remove --purge -y mono-runtime
```
2. Удалите конфигурацию Mono:

```
rm /var/www/.cmw_environment/mono
```

### Удаление .NET 6.0

1. Удалите бинарные файлы .NET:

```
rm -rf /usr/share/dotnet/
```
2. Удалите ссылку на исполняемые файлы .NET:

```
rm /usr/bin/dotnet
```
3. Удалите конфигурацию .NET:

```
rm /var/www/.cmw_environment/dotnet
```

### Удаление NGINX

1. При необходимости сохраните резервную копию файла конфигурации NGINX: `/etc/nginx/sites-available`
2. Удалите пакет `nginx-common` и его зависимости:

```
apt-get remove --purge -y nginx-common

```
3. Удалите конфигурацию NGINX:

```
rm /var/www/.cmw_environment/nginx
```

## Удаление компонентов ПО — РЕД ОС

### Удаление JRE

1. Удалите пакет `bellsoft-java17-runtime`:

```
yum autoremove -y bellsoft-java17-runtime
```
2. Удалите ссылку на исполняемые файлы:

```
rm /usr/bin/java
```
3. Удалите конфигурацию JRE:

```
rm /var/www/.cmw_environment/java
```

### Удаление Kafka

1. Удалите службу Kafka:

```
systemctl stop kafka.service
systemctl disable kafka.service
rm /usr/lib/systemd/system/kafka.service
systemctl daemon-reload
systemctl reset-failed
```
2. Удалите бинарные файлы Kafka:

```
rm -rf /usr/share/kafka
```
3. Удалите журналы Kafka:

```
rm -rf /var/log/comindware/.kafka
```
4. Удалите конфигурацию Kafka:

```
rm /var/www/.cmw_environment/kafka
```

### Удаление Mono

1. Удалите бинарные файлы Mono:

```
rm -rf /etc/mono/ \
    /usr/share/pkgconfig \
    /usr/share/mono-2.0 \
    /usr/share/locale \
    /usr/share/gdb \
    /usr/share/aclocal \
    /usr/lib64/pkgconfig \
    /usr/lib64/mono \
    /usr/lib64/libMono* \
    /usr/lib64/libmono* \
    /usr/lib64/libcairo* \
    /usr/lib64/libgdiplus* \
    /usr/lib/xsp \
    /usr/lib/monodoc \
    /usr/lib/mono-source-libs \
    /usr/lib/mono \
    /usr/include/mono-2.0
```
2. Удалите ссылки на исполняемые файлы:

```
rm -rf /usr/bin/xsp* \
    /usr/bin/xbuild \
    /usr/bin/x86_64-redhat-linux-gnu-pkg-config \
    /usr/bin/wsdl* \
    /usr/bin/svcutil \
    /usr/bin/sqlmetal \
    /usr/bin/sgen* \
    /usr/bin/setreg \
    /usr/bin/resgen* \
    /usr/bin/pkgconf \
    /usr/bin/pkg-config \
    /usr/bin/mozroots \
    /usr/bin/peverify \
    /usr/bin/permview \
    /usr/bin/pedumb \
    /usr/bin/pdb2mdb \
    /usr/bin/pcre-config \
    /usr/bin/mprof-report \
    /usr/bin/monop* \
    /usr/bin/monolinker \
    /usr/bin/monodoc* \
    /usr/bin/monodis \
    /usr/bin/mono-* \
    /usr/bin/mono \
    /usr/bin/mod-mono* \
    /usr/bin/mkbundle \
    /usr/bin/mcs \
    /usr/bin/ilasm \
    /usr/bin/ikdasm \
    /usr/bin/fastcgi* \
    /usr/bin/csharp \
    /usr/bin/asp-*
```
3. Удалите конфигурацию Mono:

```
rm /var/www/.cmw_environment/mono
```

### Удаление .NET 6.0

1. Удалите бинарные файлы .NET:

```
rm -rf /usr/share/dotnet/
```
2. Удалите ссылку на исполняемые файлы .NET:

```
rm /usr/bin/dotnet
```
3. Удалите конфигурацию .NET:

```
rm /var/www/.cmw_environment/dotnet
```

### Удаление NGINX

1. При необходимости сохраните резервную копию файла конфигурации NGINX: `/etc/nginx/conf.d`
2. Удалите пакет `nginx` и его зависимости:

```
yum autoremove -y nginx
```
3. Удалите конфигурацию NGINX:

```
rm /var/www/.cmw_environment/nginx
```

## Удаление компонентов ПО — Rocky Linux

1. Перед выполнением последующих инструкций перейдите в режим суперпользователя:

```
sudo -i
```

### Удаление JRE

1. Удалите пакет `bellsoft-java17-runtime`:

```
yum autoremove -y bellsoft-java17-runtime
```
2. Удалите ссылку на исполняемые файлы:

```
rm /usr/bin/java
```
3. Удалите конфигурацию JRE:

```
rm /var/www/.cmw_environment/java
```

### Удаление Kafka

1. Удалите службу Kafka:

```
systemctl stop kafka.service
systemctl disable kafka.service
rm /usr/lib/systemd/system/kafka.service
systemctl daemon-reload
systemctl reset-failed
```
2. Удалите бинарные файлы Kafka:

```
rm -rf /usr/share/kafka
```
3. Удалите журналы Kafka:

```
rm -rf /var/log/comindware/.kafka
```
4. Удалите конфигурацию Kafka:

```
rm /var/www/.cmw_environment/kafka
```

### Удаление Mono

1. Удалите бинарные файлы Mono:

```
rm -rf /etc/mono/ \
    /usr/share/pkgconfig \
    /usr/share/mono-2.0 \
    /usr/share/locale \
    /usr/share/gdb \
    /usr/share/aclocal \
    /usr/lib64/pkgconfig \
    /usr/lib64/mono \
    /usr/lib64/libMono* \
    /usr/lib64/libmono* \
    /usr/lib64/libcairo* \
    /usr/lib64/libgdiplus* \
    /usr/lib/xsp \
    /usr/lib/monodoc \
    /usr/lib/mono-source-libs \
    /usr/lib/mono \
    /usr/include/mono-2.0
```
2. Удалите ссылки на исполняемые файлы:

```
rm -rf /usr/bin/xsp* \
    /usr/bin/xbuild \
    /usr/bin/x86_64-redhat-linux-gnu-pkg-config \
    /usr/bin/wsdl* \
    /usr/bin/svcutil \
    /usr/bin/sqlmetal \
    /usr/bin/sgen* \
    /usr/bin/setreg \
    /usr/bin/resgen* \
    /usr/bin/pkgconf \
    /usr/bin/pkg-config \
    /usr/bin/mozroots \
    /usr/bin/peverify \
    /usr/bin/permview \
    /usr/bin/pedumb \
    /usr/bin/pdb2mdb \
    /usr/bin/pcre-config \
    /usr/bin/mprof-report \
    /usr/bin/monop* \
    /usr/bin/monolinker \
    /usr/bin/monodoc* \
    /usr/bin/monodis \
    /usr/bin/mono-* \
    /usr/bin/mono \
    /usr/bin/mod-mono* \
    /usr/bin/mkbundle \
    /usr/bin/mcs \
    /usr/bin/ilasm \
    /usr/bin/ikdasm \
    /usr/bin/fastcgi* \
    /usr/bin/csharp \
    /usr/bin/asp-*
```
3. Удалите конфигурацию Mono:

```
rm /var/www/.cmw_environment/mono
```

### Удаление .NET 6.0

1. Удалите бинарные файлы .NET:

```
rm -rf /usr/share/dotnet/Rocky
```
2. Удалите ссылку на исполняемые файлы .NET:

```
rm /usr/bin/dotnet
```
3. Удалите конфигурацию .NET:

```
rm /var/www/.cmw_environment/dotnet
```

### Удаление NGINX

1. При необходимости сохраните резервную копию файла конфигурации NGINX: `/etc/nginx/conf.d`
2. Удалите пакеты `nginx`, `nginx-core` и  `nginx-filesystem` вместе с их зависимостями:

```
yum autoremove -y nginx nginx-core nginx-filesystem
```
3. Удалите конфигурацию NGINX:

```
rm /var/www/.cmw_environment/nginx
```

## Удаление компонентов ПО — Ubuntu

1. Перед выполнением последующих инструкций перейдите в режим суперпользователя:

```
sudo -i
```

### Удаление JRE

1. Удалите пакет `bellsoft-java17-runtime`:

```
apt-get remove --purge -y bellsoft-java17-runtime
```
2. Удалите ссылку на исполняемые файлы:

```
rm /usr/bin/java
```
3. Удалите конфигурацию JRE:

```
rm /var/www/.cmw_environment/java
```

### Удаление Kafka

1. Удалите службу Kafka:

```
systemctl stop kafka.service
systemctl disable kafka.service
rm /usr/lib/systemd/system/kafka.service
systemctl daemon-reload
systemctl reset-failed
```
2. Удалите бинарные файлы Kafka:

```
rm -rf /usr/share/kafka
```
3. Удалите журналы Kafka:

```
rm -rf /var/log/comindware/.kafka
```
4. Удалите конфигурацию Kafka:

```
rm /var/www/.cmw_environment/kafka
```

### Удаление Mono

1. Удалите пакеты Mono `mono-devel` и `mono-runtime-common` вместе с их зависимостями:

```
apt-get remove --purge -y mono-devel mono-runtime-common
```
2. Удалите конфигурацию Mono:

```
rm /var/www/.cmw_environment/mono
```

### Удаление .NET 6.0

1. Удалите пакеты .NET:

```
apt-get remove --purge -y dotnet-sdk-6.0 \
    dotnet-runtime-6.0 \
    dotnet-targeting-pack-6.0 \
    aspnetcore-targeting-pack-6.0 \
    netstandard-targeting-pack-2.1 \
    dotnet-templates-6.0 \
    dotnet-host \
    dotnet-apphost-pack-6.0
```
2. Удалите конфигурацию .NET:

```
rm /var/www/.cmw_environment/dotnet
```

### Удаление NGINX

1. При необходимости сохраните резервную копию файла конфигурации NGINX: `/etc/nginx/sites-available`
2. Удалите пакет `nginx-common` и его зависимости:

```
apt-get remove --purge -y nginx-common
```
3. Удалите конфигурацию NGINX:

```
rm /var/www/.cmw_environment/nginx
```

--8<-- "related_topics_heading.md"

**[Пути и содержимое папок экземпляра ПО][paths]**



 

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
