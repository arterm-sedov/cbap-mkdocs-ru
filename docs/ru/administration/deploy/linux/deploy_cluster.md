---
kbId: 5080
title: Развёртывание Comindware Platform в кластере
tags:
    - отказоустойчивость
    - доступность
    - кластеризация
    - кластер
hide: tags
---
<!-- ЭТУ СТАТЬЮ НЕ ПУБЛИКОВАТЬ БЕЗ СОГЛАСОВАНИЯ И ПОДРОБНОЙ ПРОВЕРКИ -->
# Развёртывание {{ productName }} в кластере {: #deploy_cluster_linux }

{% include-markdown ".snippets/experimental_feature.md" %}

## Введение

**{{ productName }}** можно развернуть в кластере для увеличения производительности, улучшения отказоустойчивости и обеспечения бесперебойного функционирования ПО.

Кластерная конфигурация позволяет минимизировать время простоя системы и обеспечить непрерывность бизнес-процессов в случае отказа отдельных компонентов.

Здесь представлены инструкции по развёртыванию кластера **{{ productName }}** в простейшей минимальной конфигурации.

Инструкции по настройке стороннего ПО, такого как серверы журналирования, мониторинга и балансировки нагрузки, см. в документации к соответствующему ПО.

См. также общие рекомендации в статье _«[Обеспечение высокой доступности и отказоустойчивости {{ productName }}][availability_fault_tolerance]»_.

## Кластеризация {{ productName }}

**{{ productName }}** использует в качестве распределённого хранилища данных ПО {{ apacheIgniteVariants }}.

В кластерной конфигурации {{ apacheIgniteVariants }} поддерживает автоматическое обнаружение узлов, распределение данных и вычислений, а также репликацию и резервирование данных. Это обеспечивает равномерное распределение нагрузки и доступность при отказе отдельных узлов.

Важными аспектами кластеризации {{ apacheIgniteVariants }} являются настройка топологии кластера, выбор подходящего алгоритма консенсуса для управления состоянием кластера и использование механизмов автоматического восстановления для минимизации времени простоя.

{% if not gostech %}
См. _[рекомендации по кластеризации в документации {{ apacheIgniteVariants }} (на английском языке)][apache_ignite_clustering]_.
{% endif %}

## Преимущества использования {{ apacheIgniteVariants }} в {{ productName }}

{{ apacheIgniteVariants }} является высокопроизводительной платформой для распределённого хранения и обработки данных и обладает следующими преимуществами:

- **Высокая производительность**: ускорение доступа к данным благодаря поддержке хранения данных в оперативной памяти и кэширования.
- **Масштабируемость**: возможность горизонтального масштабирования позволяет эффективно справляться с увеличением нагрузки и объёма данных.
- **Отказоустойчивость**: репликация данных и поддержка автоматического восстановления обеспечивают надёжность даже в случае отказа узлов.
- **Поддержка ACID-транзакций**: возможность работы с критически важными данными.
- **Гибкость интеграции**: наличие клиентских API для Java, .NET, Python и других языков позволяет легко интегрировать {{ apacheIgniteVariants }} в существующую инфраструктуру.

## Преимущества использования {{ apacheIgniteVariants }} в {{ productName }}

{{ apacheIgniteVariants }} является высокопроизводительной платформой для распределённого хранения и обработки данных и обладает следующими преимуществами:

- **Высокая производительность**: ускорение доступа к данным благодаря поддержке хранения данных в оперативной памяти и кэширования.
- **Масштабируемость**: возможность горизонтального масштабирования позволяет эффективно справляться с увеличением нагрузки и объёма данных.
- **Отказоустойчивость**: репликация данных и поддержка автоматического восстановления обеспечивают надёжность даже в случае отказа узлов.
- **Поддержка ACID-транзакций**: возможность работы с критически важными данными.
- **Гибкость интеграции**: наличие клиентских API для Java, .NET, Python и других языков позволяет легко интегрировать {{ apacheIgniteVariants }} в существующую инфраструктуру.

### Рекомендации по повышению доступности и отказоустойчивости кластера

Применение следующих рекомендаций позволит улучшить производительность **{{ productName }}** и обеспечить стабильность работы системы даже при увеличении нагрузки или сбоях отдельных компонентов.

- **Репликация данных**: задайте количество резервных копий данных на нескольких узлах. См. _«[Настройка резервного копирования. Документация Apache Ignite»][apache_ignite_partition_loss_policy]_».
- **Стратегии восстановления данных**: настройте политику поведения при выпадении разделов. См. _«[Настройка восстановления разделов. Документация Apache Ignite»][apache_ignite_partition_partition_loss_policy]_».
- **Мониторинг состояния кластера**:
    - Настройте мониторинг производительности и нагрузки на узлы с помощью встроенных инструментов {{ apacheIgniteVariants }} или сторонних решений, таких как Zabbix.
    - Настройте интеграцию с инструментами мониторинга (например, Prometheus или Grafana) для сбора метрик по работе кластера и своевременного реагирования на инциденты.
    - Включите уведомления для критичных событий (например, падение узла или превышение времени отклика).
- **Резервное копирование**: настройте регулярное резервное копирование с использованием возможностей {{ apacheIgniteVariants }} Native Persistence.
- **Оптимизация конфигурации**: используйте оптимальные параметры хранения и обработки данных для минимизации задержек и повышения производительности.
- **Географическая изоляция**: для критически важных систем рекомендуется распределить узлы кластера по разным географическим регионам.
- **Топология и консистентность**: настройте базовую топологию кластера, чтобы минимизировать риски при добавлении новых узлов и восстановлении после сбоев. См. _«[Настройка базовой топологии. Документация Apache Ignite][apache_ignite_partition_baseline_topology]»_.
- **Управление обнаружением узлов** — чтобы повысить надёжности в кластере с большим количеством узлов, можно использовать Zookeeper Discovery SPI для уменьшения рисков, связанных с сетевой фрагментацией. См. _«[Настройка ZooKeeper Discovery. Документация Apache Ignite][apache_ignite_partition_zookeeper_discovery]»_.

## Конфигурация кластера

В минимальной конфигурации для распределения нагрузки (горизонтального масштабирования) кластер **{{ productName }}** может включать:

- **сервер хранения данных** на отдельной машине, к которому будут обращаться узлы кластера (для этого сервера необходимо обеспечить отказоустойчивость и высокую доступность);
- **узлы кластера**, на каждом из которых установлено ПО **{{ productName }}** одинаковой версии и развёрнут экземпляр ПО с одинаковым именем (`<instanceName>`);
- **сервер {{ openSearchVariants }}** на отдельной машине;
- **сервер Apache Kafka** на отдельной машине;
- **балансировщик нагрузки** на отдельной машине (при необходимости).

## Порядок развёртывания кластера {{ productName }}

1. **Подготовьте серверы**: убедитесь, что все машины, на которых будет развёрнут кластер, соответствуют системным требованиям, установите необходимое программное обеспечение. См. _«[Системные требования {{ productName }}][system_requirements]»._
2. **Установите и настройте компоненты**: установите и настройте все необходимые компоненты, включая серверы приложений, базы данных, серверы журналов и балансировщики нагрузки.
3. **Конфигурация кластерного окружения**: настройте кластерное окружение, включая конфигурацию балансировки нагрузки, резервирования компонентов и мониторинга.
4. **Тестирование и проверка**: проведите тестирование развёрнутого кластера, чтобы убедиться в его работоспособности и отказоустойчивости.
5. **Документирование и обучение**: задокументируйте все шаги и настройки, а также проведите обучение для администраторов кластера по его конфигурированию и поддержанию работоспособности.

## Настройка сервера хранения данных (NFS)

Настройте сервер хранения данных для кластера **{{ productName }}**.

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Создайте директорию для хранения файлов экземпляра ПО:

    ``` sh
    mkdir /share
    ```

3. Установите NFS-сервер:

    ``` sh
    apt install nfs-kernel-server
    systemctl enable nfs-kernel-server.service
    ```

4. Откройте файл `exports` для редактирования:

    ``` sh
    nano /etc/exports
    ```

5. Добавьте в файл `exports` директиву, открывающую доступ к директории `/share` для узлов кластера:

    ``` sh
    /share <nodeIP>/<netMask>(rw,sync,no_subtree_check)
    ```

    Здесь:

    - `/share` — директория, к которой предоставляется общий доступ;
    - `<nodeIP>` — неизменная часть IP-адресов узлов кластера;
    - `<netMask>` — маска подсети.

    Например:

    - `192.168.1.100/32` (маска подсети `255.255.255.255`): один компьютер с IP-адресом `192.168.1.100`.
    - `192.168.1.0/24` (маска подсети `255.255.255.0`): все компьютеры с IP-адресами от `192.168.1.1` до `192.168.1.254`.

6. Чтобы применить изменения, выполните следующую команду:

    ``` sh
    exportfs -a
    ```

7. Запустите NFS-сервер:

    ``` sh
    systemctl start nfs-kernel-server.service
    ```

8. Создайте директории для хранения данных экземпляра ПО:

    ``` sh
    mkdir -p /share/<instanceName>/Streams
    mkdir -p /share/<instanceName>/Scripts
    mkdir -p /share/<instanceName>/Temp
    mkdir -p /share/<instanceName>/Localtemp
    ```

9. Настройте права доступа к созданным директориям:

    ``` sh
    chmod -R 777 /share/<instanceName>
    chown -R nobody:nogroup /share
    ```

## Развёртывание узлов кластера

На каждом узле кластера установите ПО **{{ productName }}**, разверните экземпляр ПО и установите бинарные пакеты Apache Ignite.

### Установка ПО {{ productName }} и бинарных пакетов Apache Ignite

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Установите ПО и разверните экземпляр **{{ productName }}** одинаковой версии. См. _«[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]»_.
3. Скачайте дистрибутив [Apache Ignite](https://downloads.apache.org/ignite/2.16.0/apache-ignite-2.16.0-bin.zip).
4. Распакуйте дистрибутив (например, в директорию `/usr/share/ignite`):

    ``` sh
    unzip apache-ignite-2.16.0-bin.zip -d /usr/share/
    mv /usr/share/apache-ignite* /usr/share/ignite
    ```

5. Задайте переменную среды `IGNITE_HOME`:

    ``` sh
    export IGNITE_HOME=/usr/share/ignite
    ```

6. Скопируйте файл `Ignite.config` из директории экземпляра ПО в директорию `/usr/share/ignite`:

    ``` sh
    cp /var/www/<instanceName>/Ignite.config /usr/share/ignite/
    ```

7. Перейдите в следующую директорию:

    ``` sh
    cd /usr/share/ignite/bin
    ```

8. Откройте файл `control.sh` для редактирования:

    ``` sh
    nano control.sh
    ```

9. Измените директиву `DEFAULT_CONFIG`:

    ``` ini
    DEFAULT_CONFIG=config/Ignite.config
    ```

10. Проверьте получение списка узлов, зарегистрированных в базовой топологии:

    ``` sh
    bash control.sh --baseline
    ```

    !!! note "Примечание"

        Если работа экземпляра ПО приостановлена, запрос должен вернуть пустую топологию.

### Установка NFS-клиента

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Установите службу NFS-клиента:

    ``` sh
    apt install nfs-common
    ```

3. Откройте файл `fstab` для редактирования:

    ``` sh
    nano /etc/fstab
    ```

4. Добавьте в файл `fstab` следующую директиву (`<serverIP>` — адрес [NFS-сервера](#настройка-сервера-хранения-данных-nfs)):

    ``` ini
    <serverIP>:/share /mnt/share nfs auto 0 0
    ```

5. Смонтируйте диски и просмотрите содержимое директории NFS-сервера:

    ``` sh
    mount -a
    ls -lh /mnt/share
    ```

6. Удостоверьтесь, что существует директория `/var/lib/comindware/<instanceName>`, и задайте её владельца:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        chown -R www-data: /var/lib/comindware/<instanceName>
        ```

    - **РЕД ОС**, **Rocky** (RPM-based)

        ``` sh
        chown -R nginx: /var/lib/comindware/<instanceName>
        ```

    - **Альт Сервер**

        ``` sh
        chown -R _nginx: /var/lib/comindware/<instanceName>
        ```

7. Создайте символическую ссылку на директорию со скомпилированными скриптами на NFS-сервере:

    ``` sh
    ln -s /mnt/share/<instanceName>/Scripts /var/lib/comindware/<instanceName>/Database/Scripts
    ```

8. Откройте файл `comindware<instanceName>-env` для редактирования:

    ``` sh
    nano /etc/sysconfig/comindware<instanceName>-env
    ```

9. Проверьте и при необходимости измените лимиты памяти в директиве `JVM_OPTS` — начальный и максимальный размер кучи и максимальный объём области прямого доступа к памяти, например:

    ``` ini
    -Xms512m -Xmx4g -XX:MaxDirectMemorySize=1g
    ```

## Настройка и запуск первого узла кластера

На машине с первым узлом кластера настройте доступ к файлам базы данных и экземпляр ПО.

### Перенос базы данных на NFS-сервер

Если на первом узле был развёрнут экземпляр ПО с базой данных, перенесите её на NFS-сервер.

**Для чистого экземпляра ПО данный этап не требуется.**

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Создайте [резервную копию][complete_running_instance_backup] экземпляра ПО.
3. Скопируйте резервную копию в директорию `/home/<username>` (`<username>` — имя пользователя, `<backupName>` — имя архива резервной копии, `<pathToBackup>` — путь к архиву резервной копии):

    ``` sh
    cp /<pathToBackup>/<backupName>.cdbbz /home/<username>
    ```

4. Перейдите в директорию `/home/<username>`:

    ``` sh
    cd /home/<username>
    ```

5. Распакуйте архив резервной копии:

    ``` sh
    unzip -q <backupName>.cdbbz
    ```

6. Перенесите данные экземпляра ПО на NFS-сервер:

    ``` sh
    cp -r Scripts/* /mnt/share/<instanceName>/Scripts/
    cp -r Streams/* /mnt/share/<instanceName>/Streams/
    mv Database/* /var/lib/comindware/<instanceName>/Database/
    rm -rf Database Scripts Streams
    ```

### Настройка экземпляра ПО

1. Откройте файл `Ignite.config` для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Ignite.config
    ```

2. Отредактируйте файл `Ignite.config` по следующему образцу:

    ``` xml
    <property name="discoverySpi">
      <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
        <!-- Укажите IP-адрес, порт и диапазон портов первого узла -->
        <property name="localAddress" value="<node_1_IP>" />
        <property name="localPort" value="47510" />
        <property name="localPortRange" value="9" />
        <property name="ipFinder">
          <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
            <property name="addresses">
              <list>
                <!-- Укажите IP-адреса всех узлов кластера -->
                <value><node_1_IP>:47510..47519</value>
                <value><node_2_IP>:47510..47519</value>
                ...
                <value><node_N_IP>:47510..47519</value>
              </list>
            </property>
          </bean>
        </property>
      </bean>
    </property>
    <property name="communicationSpi">
      <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
        <property name="localPort" value="47101" />
        <!-- Укажите IP-адрес первого узла -->
        <property name="localAddress" value="<node_1_IP>" />
        <property name="messageQueueLimit" value="1024" />
      </bean>
    </property>
    
    ...

    <property name="dataRegionConfigurations">
      <list>
        <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
          <property name="warmUpConfiguration">
            <bean class="org.apache.ignite.configuration.NoOpWarmUpConfiguration" />
          </property>
          <property name="name" value="Persistent" />
          <property name="persistenceEnabled" value="true" />
            <!-- Проверьте и при необходимости отредактируйте объём выделяемой памяти -->
          <property name="initialSize" value="#{1024L * 1024 * 1024}" />
          <property name="maxSize" value="#{4L * 1024 * 1024 * 1024}" />
          <property name="pageEvictionMode" value="RANDOM_2_LRU" />
          <property name="checkpointPageBufferSize" value="#{1024L * 1024 * 1024}" />
        </bean>
        <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
          <property name="name" value="InMemory" />
          <property name="persistenceEnabled" value="false" />
            <!-- Проверьте и при необходимости отредактируйте объём выделяемой памяти -->
          <property name="initialSize" value="#{10 * 1024 * 1024}" />
          <property name="maxSize" value="#{256 * 1024 * 1024}" />
        </bean>
      </list>
    </property>
    ```

3. Откройте файл конфигурации экземпляра ПО для редактирования:

    ``` sh
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

4. Отредактируйте файл конфигурации экземпляра ПО по следующему образцу (см. _«[Конфигурация экземпляра, компонентов ПО и служб. Настройка][configuration_files_linux]»_):

    ``` yaml
    isFederationAuthEnabled: 0
    databasePath: /var/lib/comindware/<instanceName>/Database
    configPath: /var/www/<instanceName>
    # Укажите примонтированные директории NFS-сервера с файлами экземпляра ПО
    backup.config.default.repository.type: LocalDisk
    backup.config.default.repository.localDisk.path: /mnt/share/comindware/Backup
    userStorage.type: LocalDisk
    userStorage.localDisk.path: /mnt/share/<instanceName>/Streams
    tempStorage.type: LocalDisk
    tempStorage.localDisk.path: /mnt/share/<instanceName>/Temp

    instanceName: <instanceName>
    databaseName: <instanceName>
    configName: <instanceName>
    # Укажите для каждого узла уникальное имя, например общее имя и номер узла
    nodeName: <instanceName><nodeNumber>

    mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
    mq.group: <instanceName>
    manageAdapterHost: true
    elasticsearchUri: <elasticsearchIP>:<elasticsearchPort>
    version: <versionNumber>
    ```

5. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

6. При наличии файла `Workers.config` удалите его:

    ```sh
    rm -f /var/www/<instanceName>/Workers.config
    ```

7. Запустите службу экземпляра ПО:

    ``` sh
    systemctl start comindware<instanceName>
    ```

8. В веб-браузере запустите сайт экземпляра ПО и выполните вход.
9. Откройте файл `Workers.config` для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Workers.config
    ```

10. Отредактируйте файл `Workers.config` по следующему образцу:

    ``` xml
    <?xml version="1.0" encoding="utf-8"?>
    <WorkerEngine xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-i>
      <RebuildThreadWorker>false</RebuildThreadWorker>
      <BackupSessionsQueue>true</BackupSessionsQueue>
      <SessionManagerWorker>false</SessionManagerWorker>
      <NotificationWorker>false</NotificationWorker>
      <EmailListener>false</EmailListener>
      <IndexTasksQueue>false</IndexTasksQueue>
      <ProcessEngineQueueProcessing>false</ProcessEngineQueueProcessing>
      <ProcessEngineTimerProcessing>false</ProcessEngineTimerProcessing>
      <SyncThread>false</SyncThread>
      <SwitchOnFullTextSearch>false</SwitchOnFullTextSearch>
      <PerformanceMonitoring>false</PerformanceMonitoring>
      <!-- Значение ConfigurationId должно совпадать на всех узлах -->
      <ConfigurationId>XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX</ConfigurationId>
    </WorkerEngine>
    ```

11. Задайте владельца файла `Workers.config`:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        chown www-data: /var/www/<instanceName>/Workers.config
        ```

    - **РЕД ОС**, **Rocky** (RPM-based)

        ``` sh
        chown nginx: /var/www/<instanceName>/Workers.config
        ```

    - **Альт Сервер**

        ``` sh
        chown _nginx: /var/www/<instanceName>/Workers.config
        ```

12. Перезапустите экземпляр ПО:

    ``` sh
    systemctl restart comindware<instanceName>
    ```

13. Настройте директорию `LocalTemp`. См. _«[Настройка директории LocalTemp после запуска узлов кластера](#настройка-директории-localtemp-после-запуска-узлов-кластера)»_.

## Настройка и запуск второго и последующих узлов кластера

На машине со вторым и последующими узлами кластера настройте конфигурацию экземпляра ПО.

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Откройте файл `Ignite.config` для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Ignite.config
    ```

3. Скопируйте содержимое файла `Ignite.config` с первого узла.
4. Укажите в директивах `localAddress` IP-адрес узла N (остальные директивы оставьте без изменений):

    ``` xml
    <property name="discoverySpi">
      <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
        <!-- укажите IP-адрес узла N -->
        <property name="localAddress" value="<node_N_IP>" />
        
        ...

      </bean>
    </property>
    <property name="communicationSpi">
      <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
        <property name="localPort" value="47101" />
        <!-- укажите IP-адрес узла N -->
        <property name="localAddress" value="<node_N_IP>" />
        <property name="messageQueueLimit" value="1024" />
      </bean>
    </property>
    ...
    
    ```

5. Откройте файл конфигурации экземпляра ПО для редактирования:

    ``` sh
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

6. Скопируйте содержимое файла `<instanceName>.yml` с первого узла.
7. В директиве `nodeName` укажите уникальное имя узла (например общее имя и номер узла):

    ``` yaml
    nodeName: <instanceName><nodeNumber>
    ```

8. Откройте файл `Workers.config` для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Workers.config
    ```

9. Скопируйте содержимое файла `Workers.config` c первого узла.
10. Удостоверьтесь, что значение директивы `<ConfigurationId>` совпадает на всех узлах.
11. Запустите экземпляр ПО:

    ``` sh
    systemctl start comindware<instanceName>
    ```

12. В браузере запустите сайт экземпляра ПО.
13. На машине, на которой развёрнут первый узел, перейдите в директорию со скриптами Apache Ignite:

    ``` sh
    cd /home/username/ignite/bin
    ```

14. Выполняйте запрос топологии до тех пор, пока не отобразится сообщение о наличии стороннего узла:

    ``` sh
    bash control.sh --baseline
    ```

15. Выполните запрос на включение узла N в топологию (`<nodeNConsistenceId>` — идентификатор узла N в Ignite):

    ``` sh
    bash control.sh --baseline add <nodeNConsistenceId> -y
    ```

16. На машине с узлом N кластера перейдите в директорию со скриптами Apache Ignite:

    ``` sh
    cd /home/username/ignite/bin
    ```

17. Выполните запрос топологии:

    ``` sh
    watch bash control.sh --baseline
    ```

18. Дождитесь включения узла N в топологию.
19. Дождитесь отображения страницы входа в экземпляр ПО в браузере.

## Настройка директории LocalTemp после запуска узлов кластера

При каждом запуске экземпляра ПО заново создаётся локальная папка `/var/lib/comindware/<instanceName>/LocalTemp` и удаляется символьная ссылка на неё на NFS-сервере. После этого необходимо удалить директорию `/var/lib/comindware/<instanceName>/LocalTemp` и пересоздавать символьную ссылку на директорию `LocalTemp` на NFS-сервере.

1. На каждом узле удалите локальную директорию `LocalTemp`:

    ``` sh
    rm -rf /var/lib/comindware/<instanceName>/LocalTemp
    ```

2. С любого узла создайте директорию `LocalTemp` на NFS-сервере:

    ``` sh
    mkdir /mnt/share/<instanceName>/LocalTemp
    ```

3. На каждом узле назначьте владельца директории `LocalTemp` на NFS-сервере:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        chown -R www-data:www-data /mnt/share/<instanceName>/LocalTemp
        ```

    - **РЕД ОС**, **Rocky** (RPM-based)

        ``` sh
        chown -R nginx:nginx /mnt/share/<instanceName>/LocalTemp
        ```

    - **Альт Сервер**

        ``` sh
        chown -R _nginx:_nginx /mnt/share/<instanceName>/LocalTemp
        ```

4. На каждом узле создайте символьную ссылку на директорию `LocalTemp` с NFS-сервера:

    ``` sh
    ln -s /mnt/share/<instanceName>/LocalTemp /var/lib/comindware/<instanceName>/LocalTemp
    ```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]_
- _[Пути и содержимое директорий экземпляра ПО][paths]_
- _[Конфигурация экземпляра, компонентов ПО и служб. Настройка][configuration_files_linux]_
- _[Системные требования {{ productName }}][system_requirements]_
- _[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]_
- _[Обеспечение высокой доступности и отказоустойчивости {{ productName }}][availability_fault_tolerance]_
- _[Apache Ignite. Установка и настройка][apache_ignite_deploy]_
    {% if not gostech %}
- _[Рекомендации по кластеризации. Документация Apache Ignite (на английском языке)][apache_ignite_clustering]_
- _[Настройка базовой топологии. Документация Apache Ignite][apache_ignite_partition_baseline_topology]_
- _[Настройка ZooKeeper Discovery. Документация Apache Ignite][apache_ignite_partition_zookeeper_discovery]_
- _[Настройка резервного копирования. Документация Apache Ignite»][apache_ignite_partition_loss_policy]_
- _[Настройка восстановления разделов. Документация Apache Ignite»][apache_ignite_partition_partition_loss_policy]_
    {% endif %}
</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
