---
title: Apache Ignite. Установка и настройка. Краткое руководство
kbId: 2093
---

# Apache Ignite. Установка и настройка. Краткое руководство

## Введение

Для работы **{{ productName }}** требуется программное обеспечение Apache Ignite.

Apache Ignite в минимально необходимой конфигурации устанавливается автоматически при развертывании **{{ productName }}** в ОС Linux и Windows.

Для продвинутых конфигураций требуется развернуть Apache Ignite самостоятельно.

В настоящем документе представлены краткие инструкции по установке и настройке Apache Ignite 2.16.0 в ОС Linux для работы с **{{ productName }}**.

Полное руководство по Apache Ignite 2.16.0 (на английском языке) представлено на веб-сайте: <https://ignite.apache.org/docs/2.16.0/>

Краткое руководство на русском языке представлено на веб-сайте: <https://platform.digital.gov.ru/docs/data-management/platform-v-ignite-se/quick-start>

 

## 1. Установка Apache Ignite

**1.1.** Скачайте установочный файл Ignite с веб-сайта: <https://ignite.apache.org/download.cgi#binaries>

**1.2.** Распакуйте архив в папку Ignite, например: `/var/www/ignite`

**1.3.** Установите переменную среды `IGNITE_HOME`, указав путь к папке Ignite без завершающего символа `/`: `export IGNITE_HOME=var/www/ignite`

**1.4.** Дополнительные модули для использования Ignite в сочетании с {{ productName }} не требуются.

**1.5.** Настройте конфигурацию Ignite, изменив файл `Apache.Ignite.exe.config`: `$IGNITE_HOME/platforms/dotnet/bin/Apache.Ignite.exe.config`

**1.6.** Пример файла `Apache.Ignite.exe.config` приведён в разделе [«Пример файла конфигурации Ignite»](#mcetoc_1g773nmjt5).

 

## 2. Запуск Apache Ignite

**2.1.** Запустите службу Apache Ignite с помощью команды: `/$IGNITE_HOME/bin/ignite.sh -v`; параметр `-v` включает вывод подробных данных в журнал (по умолчанию в журнал Ignite выводятся только краткие сведения).

**2.2.** Если запустить Ignite не удалось, проверьте информацию в журнале, по умолчанию он хранится в папке `$IGNITE_HOME/work/log`.

 

## 3. Пример файла конфигурации Ignite

Для стабильной работы Ignite вместе с {{ productName }} важны следующие директивы в данном примере:

- `<igniteConfiguration xmlns="http://ignite.apache.org/schema/dotnet/IgniteConfigurationSection" gridName="myGrid1">` — в параметре `gridName` укажите имя сервера узла Ignite. У узлов кластера должно быть одинаковое имя сервера.
- `<discoverySpi type="TcpDiscoverySpi"><ipFinder type="TcpDiscoveryStaticIpFinder"><endpoints> <string>127.0.0.1</string></endpoints></ipFinder></discoverySpi>` — в параметре `TcpDiscoveryStaticIpFinder` укажите адрес сервера.
- `<dataRegionConfigurations type="DataRegionConfiguration"> <dataRegionConfiguration><name>Persistent</name><persistenceEnabled>true</persistenceEnabled>` — в директиве `dataRegionConfiguration` укажите `<persistenceEnabled>true</persistenceEnabled>`.
- `<workDirectory>/var/lib/ignite/</workDirectory>>` — укажите рабочую папку Ignite.
- `<igniteInstanceName>Comindware_Instance2</igniteInstanceName>` — укажите имя экземпляра Ignite.

```
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

      <igniteInstanceName>Comindware_Instance2</igniteInstanceName>

      <autoGenerateIgniteInstanceName>false</autoGenerateIgniteInstanceName>

</igniteConfiguration>
</configuration>
```



{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
