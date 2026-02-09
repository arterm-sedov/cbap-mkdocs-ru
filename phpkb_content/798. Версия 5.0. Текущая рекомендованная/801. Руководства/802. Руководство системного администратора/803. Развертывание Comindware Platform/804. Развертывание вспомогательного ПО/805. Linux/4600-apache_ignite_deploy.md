---
title: 'Apache Ignite. Установка и настройка'
kbId: 4600
url: 'https://kb.comindware.ru/article.php?id=4600'
updated: '2026-01-29 18:02:55'
---

# Apache Ignite. Установка и настройка

Экспериментальная функция

Представленная здесь функция находится на стадии разработки. См. *«[Поддержка экспериментальных функций][experimental_feature_support]»*.

## Введение

Apache Ignite — это распределенная высокопроизводительная система управления базами данных.

**{{ productName }}** использует Apache Ignite для хранения данных.

Apache Ignite в минимально необходимой конфигурации устанавливается автоматически при установке **{{ productName }}**.

## Прикладная задача

Внимание!

Данная инструкция не требуется для базовых сценариев развёртывания **{{ productName }}**.

Используйте эту инструкцию, только если вам необходимо развернуть Apache Ignite в особой нетипичной конфигурации.

Для продвинутых конфигураций можно развернуть собственный экземпляр Apache Ignite или использовать имеющуюся в вашей организации службу.

Например, можно развернуть кластер Apache Ignite из нескольких узлов, если это необходимо для вашего бизнеса.

Здесь представлены краткие инструкции по установке и настройке Apache Ignite 2.17.0 в ОС Linux для работы с **{{ productName }}** в простейшей конфигурации.

Вам может потребоваться адаптировать конфигурацию Apache Ignite в соответствии со своими бизнес-потребностями.

Полное официальное руководство по Apache Ignite 2 (на английском языке) представлено на сайте: <https://ignite.apache.org/docs/ignite2/latest/>

Краткое руководство на русском языке представлено на сайте: <https://platformv.sbertech.ru/docs/public/IGN/17.6.0/index.html>

## Установка Apache Ignite

1. Скачайте, распакуйте и установите Apache Ignite:

   ```
   wget https://downloads.apache.org/ignite/2.17.0/apache-ignite-2.17.0-bin.zip
   unzip -q apache-ignite-2.17.0-bin.zip
   mv apache-ignite-2.17.0-bin /usr/share/ignite

   ```
2. Назначьте владельца каталога `/usr/share/ignite`:

   **Astra Linux, Debian, DEB-дистрибутивы**

   ```
   chown -R www-data:www-data /usr/share/ignite

   ```

   **РЕД ОС, RPM-дистрибутивы**

   ```
   chown -R nginx:nginx /usr/share/ignite

   ```

   **Альт Сервер**

   ```
   chown -R _nginx:_nginx /usr/share/ignite

   ```
3. Установите переменную среды `IGNITE_HOME`, указав путь к папке Ignite без завершающего символа `/`: `export IGNITE_HOME=/usr/share/ignite`
4. Дополнительные модули для использования Ignite в сочетании с {{ productName }} не требуются.
5. Скопируйте в папку `/usr/share/ignite` файл `Ignite.config` из папки `/var/www/<instanceName>` (где `<instanceName>` — имя экземпляра ПО).
6. Пример файла `Ignite.config` представлен в параграфе [«Пример файла конфигурации Ignite»](#apache_ignite_deploy_configuration_example).
7. Откройте для редактирования скрипт запуска Ignite `ignite.sh`:

   ```
   cd /usr/share/ignite/bin/
   nano ignite.sh

   ```
8. Добавьте в начало скрипта `ignite.sh` следующие строки:

   ```
   export "JVM_OPTS=-Xms512m -Xmx4g -XX:MaxDirectMemorySize=1g -Djava.net.preferIPv4Stack=true -XX:+AlwaysPreTouch -XX:+UseG1GC -XX:+ScavengeBeforeFullGC -XX:+DisableExplicitGC -XX:MinHeapFreeRatio=1 -XX:MaxHeapFreeRatio=10 -DIGNITE_QUIET=false -DIGNITE_NO_ASCII=true--add-opens=java.base/jdk.internal.misc=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.management/com.sun.jmx.mbeanserver=ALL-UNNAMED --add-opens=jdk.internal.jvmstat/sun.jvmstat.monitor=ALL-UNNAMED --add-opens=java.base/sun.reflect.generics.reflectiveObjects=ALL-UNNAMED --add-opens=jdk.management/com.sun.management.internal=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.util.concurrent=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.locks=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.lang.invoke=ALL-UNNAMED --add-opens=java.base/java.math=ALL-UNNAMED --add-opens=java.sql/java.sql=ALL-UNNAMED"
   export IGNITE_WORK_DIR=/var/lib/comindware/<instanceName>/Database
   export DEFAULT_CONFIG=/usr/share/ignite/config/Ignite.config

   ```
9. Откройте для редактирования скрипт `control.sh`:

   ```
   nano control.sh

   ```
10. Добавьте в скрипт `control.sh` следующие строки:

    ```
    DEFAULT_CONFIG=config/Ignite.config

    ```
11. Создайте и откройте для редактирования скрипт `ignite_service_create.sh`. Этот скрипт будет создавать и запускать службу Apache Ignite:

    ```
    nano ignite_service_create.sh

    ```
12. Введите в скрипт `ignite_service_create.sh` следующие директивы:

    ```
    #!/bin/bash
    # create apache ignite daemon service
    # ver 0.1
    #
    sudo cat <<EOF >/lib/systemd/system/ignite.service
    [Unit]
    Description=Apache Ignite Service
    After=network.target
    [Service]
    WorkingDirectory=/usr/share/ignite
    User=<User>
    Group=<Group>
    PrivateDevices=yes
    ProtectSystem=full
    Type=simple
    ExecReload=/bin/kill -HUP $MAINPID
    KillMode=mixed
    KillSignal=SIGTERM
    TimeoutStopSec=10
    ExecStart=/usr/share/ignite/bin/ignite.sh
    SyslogIdentifier=Ignite
    Restart=on-failure
    RestartSec=5s
    [Install]
    WantedBy=multi-user.target
    Alias=ignite.service
    EOF
    # Пример соответствия параметров User/Group различным ОС:
    # Astra Linux, Debian, DEB-дистрибутивы: User=www-data, Group=www-data
    # РЕД ОС, RPM-дистрибутивы:              User=nginx,   Group=nginx
    # Альт Сервер:                     User=_nginx,  Group=_nginx
    systemctl daemon-reload
    systemctl enable ignite.service

    ```
13. Инициализируйте и запустите службу Apache Ignite с помощью скрипта `ignite_service_create.sh`:

    ```
    bash ignite_service_create.sh

    ```

## Запуск Apache Ignite

1. Запустите службу Apache Ignite:

   ```
   systemctl start ignite

   ```
2. Проверьте статус узла Apache Ignite:

   ```
   cd /usr/share/ignite/bin/
   bash control.sh --baseline

   ```

## Пример файла конфигурации Ignite

Для стабильной работы Ignite вместе с **{{ productName }}** важны следующие директивы в данном примере:

- `<igniteConfiguration xmlns="http://ignite.apache.org/schema/dotnet/IgniteConfigurationSection" gridName="myGrid1">` — в параметре `gridName` укажите имя сервера узла Ignite. У узлов кластера должно быть одинаковое имя сервера.
- `<discoverySpi type="TcpDiscoverySpi"><ipFinder type="TcpDiscoveryStaticIpFinder"><endpoints> <string>127.0.0.1</string></endpoints></ipFinder></discoverySpi>` — в параметре `TcpDiscoveryStaticIpFinder` укажите адрес сервера.
- `<dataRegionConfigurations type="DataRegionConfiguration"> <dataRegionConfiguration><name>Persistent</name><persistenceEnabled>true</persistenceEnabled>` — в директиве `dataRegionConfiguration` укажите `<persistenceEnabled>true</persistenceEnabled>`.
- `<workDirectory>/var/lib/ignite/</workDirectory>>` — укажите рабочую папку Ignite.
- `<igniteinstanceName>Comindware_Instance2</igniteinstanceName>` — укажите имя экземпляра Ignite.

Пример файла конфигурации Ignite```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <configSections>
      <section name="igniteConfiguration" type="Apache.Ignite.Core.IgniteConfigurationSection, Apache.Ignite.Core" />
  </configSections>
  <runtime>
      <gcServer enabled="true"/>
  </runtime>
  <igniteConfiguration xmlns="http://ignite.apache.org/schema/dotnet/IgniteConfigurationSection" gridName="myGrid1">
      <localhost></localhost>
      <networkTimeout>1000</networkTimeout>
      <networkSendRetryDelay>1000</networkSendRetryDelay>
      <jvmOptions>
          <string>-Xms512m</string>
          <string>-Xmx3g</string>
          <string>--add-exports=java.base/jdk.internal.misc=ALL-UNNAMED</string>
          <string>--add-exports=java.base/sun.nio.ch=ALL-UNNAMED</string>
          <string>--add-exports=java.management/com.sun.jmx.mbeanserver=ALL-UNNAMED</string>
          <string>--add-exports=jdk.internal.jvmstat/sun.jvmstat.monitor=ALL-UNNAMED</string>
          <string>--add-exports=java.base/sun.reflect.generics.reflectiveObjects=ALL-UNNAMED</string>
          <string>--add-opens=jdk.management/com.sun.management.internal=ALL-UNNAMED</string>
          <string>-Djava.net.preferIPv4Stack=true</string>
          <string>--illegal-access=warn</string>
      </jvmOptions>

      <discoverySpi type="TcpDiscoverySpi">
          <ipFinder type="TcpDiscoveryStaticIpFinder">
              <endpoints>
                  <string>127.0.0.1</string>
              </endpoints>
          </ipFinder>
      </discoverySpi>
      <atomicConfiguration type="AtomicConfiguration">
          <atomicSequenceReserveSize>1000</atomicSequenceReserveSize>
          <cacheMode>Partitioned</cacheMode>
          <backups>1</backups>
      </atomicConfiguration>
      <dataStorageConfiguration type="DataStorageConfiguration">
          <walPath>wal/</walPath>
          <walArchivePath>wal/</walArchivePath>
          <defaultDataRegionConfiguration type="DataRegionConfiguration">
              <name>Default_Region</name>
              <persistenceEnabled>false</persistenceEnabled>
              <initialSize>10485760</initialSize>
              <maxSize>20971520</maxSize>
          </defaultDataRegionConfiguration>
          <dataRegionConfigurations type="DataRegionConfiguration">
                  <dataRegionConfiguration>
                      <name>Persistent</name>
                      <persistenceEnabled>true</persistenceEnabled>
                      <initialSize>10485760</initialSize>
                      <maxSize>1147483648</maxSize>
                      <pageEvictionMode>RandomLru</pageEvictionMode>
                  </dataRegionConfiguration>
                  <dataRegionConfiguration>
                      <name>InMemory</name>
                      <persistenceEnabled>false</persistenceEnabled>
                      <initialSize>10485760</initialSize>
                      <maxSize>50485760</maxSize>
                  </dataRegionConfiguration>
          </dataRegionConfigurations>
      </dataStorageConfiguration>
      <clientMode>false</clientMode>
      <includedEventTypes></includedEventTypes>
      <workDirectory>/var/lib/ignite/</workDirectory>
      <jvmDllPath></jvmDllPath>
      <igniteinstanceName>Comindware_Instance2</igniteinstanceName>
      <autoGenerateIgniteinstanceName>false</autoGenerateIgniteinstanceName>

</igniteConfiguration>
</configuration>

```

--8<-- "related_topics_heading.md"

- [Apache Ignite. Дефрагментация и обслуживание кластера][apache_ignite_defragment]
- [Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]
- [Создание полной резервной копии без остановки экземпляра ПО][complete_running_instance_backup]
- [Восстановление базы данных из полной резервной копии][restore_complete_backup]
- [Оптимизация работы вспомогательного ПО][auxiliary_software_optimize]

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
