Для примера описывается развёртывание кластера Приложения из четырёх узлов на трёх хостах, среди которых:
##### 1. хост_0 `10.10.10.10`:
   - серверный узел Приложения 
   + дополнительный свободный узел Ignite (ключ `-i` при установке пререквизитов распакует приложение в директорию `/usr/share/ignite`)
   + узел Kafka
##### 2. хост_1 `10.10.10.11`
   - серверный узел Приложения
##### 3. хост_2 `10.10.10.12`
   - клиентский узел Приложения

После установки пререквизитов, сервисов и версии Приложения на хостах выполнить 
- настройку узлов ignite для узлов Приложения и узла Ignite
  Прописать директории и хосты:порты для узла Ignite (подробности есть в инструкциях "Кластер CBAP добавление узла Apache Ignite", "Кластер CBAP с тонким клиентом (ассиметричный)", "Кластер CBAP Отказоустойчивый с балансировщиком на одном хосте")

- аналогично выполнить настройку узлов Ignite для Узлов Приложения
- указать в конфигурации Ignite для клиентского узла Приложения 
  `    <property name="clientMode" value="true" />`

### для хост_0

При установке Пререквизитов указать дополнительный ключ `-i`. 
Если установке Пререквизитов уже была выполнена перейти в директорию со скриптами пакета пререквизитолв и выполнить
```sh
bash prerequisites_install.sh -i
```
 При выполнении скрипта в директорию `/usr/share/ignite` будет установлен пакет `Apache Ignite`
 Для создания и настройки дополнительного узла Apache Ignite необходимо выполнить инструкцию  "Кластер CBAP добавление узла Apache Ignite".

Открыть для редактирования конфигурационный файл `Ignite.config` серверного узла Приложения и указать в блоке `"discoverySpi"` хосты и порты будущего кластера

```xml
    <property name="discoverySpi">
      <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
        <property name="localAddress" value="10.10.10.10" />
        <property name="localPort" value="47510" />
        <property name="localPortRange" value="9" />
        <property name="ipFinder">
          <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
            <property name="addresses">
              <list>
                <value>10.10.10.10:47510..47519</value>
                <value>10.10.10.10:47520..47529</value>
                <value>10.10.10.11:47510..47519</value>
                <value>10.10.10.12:47510..47519</value>
              </list>
            </property>
          </bean>
        </property>
      </bean>
    </property>
```

Открыть для редактирования конфигурационный файл `Ignite.config` дополнительного узла `Apache Ignite` и указать в блоке `"discoverySpi"` хосты и порты будущего кластера

```xml
    <property name="discoverySpi">
      <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
        <property name="localAddress" value="10.10.10.10" />
        <property name="localPort" value="47520" />
        <property name="localPortRange" value="9" />
        <property name="ipFinder">
          <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
            <property name="addresses">
              <list>
                <value>10.10.10.10:47510..47519</value>
                <value>10.10.10.10:47520..47529</value>
                <value>10.10.10.11:47510..47519</value>
                <value>10.10.10.12:47510..47519</value>
              </list>
            </property>
          </bean>
        </property>
      </bean>
    </property>
```

Обратить внимание на значения "localPort" в обоих конфигурационных файлах

### для хост_1

Открыть для редактирования конфигурационный файл `Ignite.config` серверного узла Приложения и указать в блоке `"discoverySpi"` хосты и порты будущего кластера

```xml
    <property name="discoverySpi">
      <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
        <property name="localAddress" value="10.10.10.11" />
        <property name="localPort" value="47510" />
        <property name="localPortRange" value="9" />
        <property name="ipFinder">
          <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
            <property name="addresses">
              <list>
                <value>10.10.10.10:47510..47519</value>
                <value>10.10.10.10:47520..47529</value>
                <value>10.10.10.11:47510..47519</value>
                <value>10.10.10.12:47510..47519</value>
              </list>
            </property>
          </bean>
        </property>
      </bean>
    </property>
```

### для хост_2

#### При подключении Клиентского узла Приложения
Открыть для редактирования конфигурационный файл `Ignite.config` серверного узла Приложения и указать в блоке `"discoverySpi"` хосты и порты будущего кластера, а так-же указать клиентский режим работы

```xml
    <property name="discoverySpi">
      <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
        <property name="localAddress" value="10.10.10.12" />
        <property name="localPort" value="47510" />
        <property name="localPortRange" value="9" />
        <property name="ipFinder">
          <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
            <property name="addresses">
              <list>
                <value>10.10.10.10:47510..47519</value>
                <value>10.10.10.10:47520..47529</value>
                <value>10.10.10.11:47510..47519</value>
                <value>10.10.10.12:47510..47519</value>
              </list>
            </property>
          </bean>
        </property>
      </bean>
    </property>
    ...
    ...
    <property name="clientMode" value="true" />
```

#### При подключении узла Приложения ТОНКИМ КЛИЕНТОМ

Для работы экземпляра Приложения на `хост_2` в режиме тонкого клиента необходимо дописать в конфигурацию окружения сервиса Приложения соответствующие строки.
```sh
nano /etc/sysconfig/comindware<instanceName>-env
```

добавить:
```r
PLATFORM_USE_THIN_CLIENT=y
PLATFORM_THIN_CLIENT_ENDPOINTS=<host1>:10800,<host2>:10800
```

Где `<host1>` и `<host2>` -  имена хостов или IP узлов 1 и 2
### На всех узлах Приложения!!!

- в `.yml` файлах конфигурации узлов Приложения удалить/закомментировать следующие строки
```yml
isContainerEnvironment:
clusterNodes:
db.holdLock: true
```

### На хост_0

Распаковать и перенести в целевые директории на первом серверном узле Приложения Резервную копию Приложения, 
Запустить Первый узел 
```sh
systemctl stop apigateway<instanceName> && systemctl stop comindware<instanceName> && systemctl stop adapterhost<instanceName>
```
После обновления запустится экземпляр Приложения

Проверить статус сервисов
```sh
systemctl status apigateway<instanceName> comindware<instanceName> adapterhost<instanceName>
```

В директории базы данных первого узла создать файл `hold.lock` для запуска ребалансировки

Переключиться на вывод лога `igniteClient*.log`

Дождаться сообщения об окончании ребалансировки кластера
```
 ... INFO      Skipping rebalancing (nothing scheduled) ...
```
После чего удалить из директории базы данных файл `hold.lock` и снова открыть на вывод журнал состояния экземпляра

```sh
rm /var/lib/comindware/<instanceName>/Database/hold.lock
```

Дождаться загрузки страницы входа в веб-браузере, выполнить вход в систему

Убедиться в работоспособности узла.

Повторить для второго серверного узла Приложения

Запустить дополнительный узел Ignite

Проверить состояние топологии кластера Ignite при  помощи `bash /usr/share/ignite/bin/control.sh --baseline`
```
