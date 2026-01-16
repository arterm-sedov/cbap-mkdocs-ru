---
title: 'Apache Ignite. Установка и настройка в Windows'
kbId: 4616
url: 'https://kb.comindware.ru/article.php?id=4616'
updated: '2025-12-03 13:20:35'
---

# Apache Ignite. Установка и настройка в Windows

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

1. Скачайте ZIP файл `apache-ignite-2.17.0-bin.zip` по ссылке: <https://ignite.apache.org/download.cgi#binaries>
2. Распакуйте ZIP-файл в папку, например: `C:\\apache-ignite-2.17.0-bin`
3. Установите переменную среды Windows: `set IGNITE_HOME=C:\\apache-ignite-2.17.0-bin`
4. Настройте конфигурацию Ignite, изменив файл `Apache.Ignite.exe.config`: `%IGNITE_HOME%\\platforms\\dotnet\\bin\\Apache.Ignite.exe.config`

## Запуск Apache Ignite

1. Запустите службу Ignite с помощью команды: `%IGNITE_HOME%\\bin\\ignite.bat -v`

   Параметр `-v` включает вывод подробных данных в журнал (по умолчанию в журнал Ignite выводятся только краткие сведения).
2. Если запустить Ignite не удалось, проверьте информацию в журнале, по умолчанию он хранится в папке `%IGNITE_HOME%\\work\\log`.

## Пример файла конфигурации Ignite

Для стабильной работы Ignite вместе с {{ productName }} важны следующие директивы в данном примере:

- `<igniteConfiguration xmlns="http://ignite.apache.org/schema/dotnet/IgniteConfigurationSection" gridName="myGrid1">` — в параметре `gridName` укажите имя сервера узла Ignite. У узлов кластера должно быть одинаковое имя сервера.
- `<discoverySpi type="TcpDiscoverySpi"><ipFinder type="TcpDiscoveryStaticIpFinder"><endpoints> <string>127.0.0.1</string></endpoints></ipFinder></discoverySpi>` — в параметре `TcpDiscoveryStaticIpFinder` укажите адрес сервера.
- `<dataRegionConfigurations type="DataRegionConfiguration"> <dataRegionConfiguration><name>Persistent</name><persistenceEnabled>true</persistenceEnabled>` — в директиве `dataRegionConfiguration` укажите `<persistenceEnabled>true</persistenceEnabled>`.
- `<workDirectory>C:\\apache-ignite-2.17.0-bin\\</workDirectory>>` — укажите рабочую папку Ignite.
- `<igniteInstanceName>Comindware_Instance2</igniteInstanceName>` — укажите имя экземпляра Ignite.

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
            <walPath>wal\\</walPath>
            <walArchivePath>wal\\</walArchivePath>
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
        <workDirectory>C:\\apache-ignite-2.17.0-bin\\</workDirectory>
        <jvmDllPath></jvmDllPath>
        <igniteInstanceName>Comindware_Instance2</igniteInstanceName>
        <autoGenerateIgniteInstanceName>false</autoGenerateIgniteInstanceName>

</igniteConfiguration>
</configuration>

```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
