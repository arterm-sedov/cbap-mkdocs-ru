---
title: Apache Ignite. Установка и настройка
kbId: 4600
---

# Apache Ignite. Установка и настройка {: #apache_ignite_deploy }

## Введение

Для работы **{{ productName }}** требуется программное обеспечение Apache Ignite.

Apache Ignite в минимально необходимой конфигурации устанавливается автоматически при установке **{{ productName }}** с ключом `-e`.

Для продвинутых конфигураций требуется развернуть Apache Ignite самостоятельно.

Здесь представлены краткие инструкции по установке и настройке Apache Ignite 2.16.0 в ОС Linux для работы с **{{ productName }}**.

Полное руководство по Apache Ignite 2.16.0 (на английском языке) представлено на веб-сайте: <https://ignite.apache.org/docs/2.16.0/>

Краткое руководство на русском языке представлено на веб-сайте: <https://platform.digital.gov.ru/docs/data-management/platform-v-ignite-se/quick-start>

## Установка Apache Ignite

1. Скачайте, распакуйте и установите Apache Ignite и задайте права:
    ```sh
    wget https://downloads.apache.org/ignite/2.16.0/apache-ignite-2.16.0-bin.zip
    unzip -q apache-ignite-2.16.0-bin.zip
    mv apache-ignite-2.16.0-bin /usr/share/ignite
    chown -R www-data:www-data /usr/share/ignite
    ```
2. Установите переменную среды `IGNITE_HOME`, указав путь к папке Ignite без завершающего символа `/`: `export IGNITE_HOME=/usr/share/ignite`
3. Дополнительные модули для использования Ignite в сочетании с {{ productName }} не требуются.
4. Скопируйте в папку `/usr/share/ignite` файл `Ignite.config` из папки `/var/www/<instanceName>` (где `<instanceName>` — имя экземпляра ПО).
5. Пример файла `Ignite.config` представлен в параграфе [«Пример файла конфигурации Ignite»](#пример-файла-конфигурации-ignite).
6. Откройте для редактирования скрипт запуска Ignite `ignite.sh`:
    ``` sh
    cd /usr/share/ignite/bin/
    nano ignite.sh
    ```
7. Добавьте в начало скрипта `ignite.sh` следующие строки:
    ``` sh
    export "JVM_OPTS=-Xms512m -Xmx4g -XX:MaxDirectMemorySize=1g -Djava.net.preferIPv4Stack=true -XX:+AlwaysPreTouch -XX:+UseG1GC -XX:+ScavengeBeforeFullGC -XX:+DisableExplicitGC -XX:MinHeapFreeRatio=1 -XX:MaxHeapFreeRatio=10 -DIGNITE_QUIET=false -DIGNITE_NO_ASCII=true--add-opens=java.base/jdk.internal.misc=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.management/com.sun.jmx.mbeanserver=ALL-UNNAMED --add-opens=jdk.internal.jvmstat/sun.jvmstat.monitor=ALL-UNNAMED --add-opens=java.base/sun.reflect.generics.reflectiveObjects=ALL-UNNAMED --add-opens=jdk.management/com.sun.management.internal=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.util.concurrent=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.locks=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.lang.invoke=ALL-UNNAMED --add-opens=java.base/java.math=ALL-UNNAMED --add-opens=java.sql/java.sql=ALL-UNNAMED"
    export IGNITE_WORK_DIR=/var/lib/comindware/<instanceName>/Database
    export DEFAULT_CONFIG=/usr/share/ignite/config/Ignite.config
    ```
8. Откройте для редактирования скрипт `control.sh`:

    ``` sh
    nano control.sh
    ```
9. Добавьте в скрипт `control.sh` следующие строки:
    ``` sh
    DEFAULT_CONFIG=config/Ignite.config
    ```
10. Создайте и откройте для редактирования скрипт `ignite_service_create.sh`. Этот скрипт будет создавать и запускать службу Apache Ignite:
    ``` sh
    nano ignite_service_create.sh
    ```
11. Введите в скрипт `ignite_service_create.sh` следующие директивы:
    ``` sh
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
    User=www-data
    Group=www-data
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
    systemctl daemon-reload
    systemctl enable ignite.service
    ```
12. Инициализируйте и запустите службу Apache Ignite с помощью скрипта `ignite_service_create.sh`:
    ``` sh
    bash ignite_service_create.sh
    ```

## Запуск Apache Ignite {: .pageBreakBefore }

1. Запустите службу Apache Ignite:
    ``` sh
    systemctl start ignite
    ```
2. Проверьте статус узла Apache Ignite:
    ``` sh
    cd /usr/share/ignite/bin/
    bash control.sh --baseline
    ```

## Пример файла конфигурации Ignite {: .pageBreakBefore }

Для стабильной работы Ignite вместе с **{{ productName }}** важны следующие директивы в данном примере:

- `<igniteConfiguration xmlns="http://ignite.apache.org/schema/dotnet/IgniteConfigurationSection" gridName="myGrid1">` — в параметре `gridName` укажите имя сервера узла Ignite. У узлов кластера должно быть одинаковое имя сервера.
- `<discoverySpi type="TcpDiscoverySpi"><ipFinder type="TcpDiscoveryStaticIpFinder"><endpoints> <string>127.0.0.1</string></endpoints></ipFinder></discoverySpi>` — в параметре `TcpDiscoveryStaticIpFinder` укажите адрес сервера.
- `<dataRegionConfigurations type="DataRegionConfiguration"> <dataRegionConfiguration><name>Persistent</name><persistenceEnabled>true</persistenceEnabled>` — в директиве `dataRegionConfiguration` укажите `<persistenceEnabled>true</persistenceEnabled>`.
- `<workDirectory>/var/lib/ignite/</workDirectory>>` — укажите рабочую папку Ignite.
- `<igniteinstanceName>Comindware_Instance2</igniteinstanceName>` — укажите имя экземпляра Ignite.
{% include-markdown ".snippets/pdfPageBreakHard.md" %}

``` {: .xml title="Пример файла конфигурации Ignite" .pageBreakBefore }
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
{% if pdfOutput %}
```
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
``` {: .xml title="Пример файла конфигурации Ignite — продолжение" .pageBreakBefore }
{% endif %}
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

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
