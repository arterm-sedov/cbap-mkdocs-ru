!!! warning "Внимание!"

    Директивы `isFederationAuthEnabled` и `manageAdapterHost` требуется удалить, если они присутствуют.
    
    Значения параметров `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений,) и `cluster.name` / `clusterName` (имя экземпляра ПО) должны совпадать в трёх файлах конфигурации:

    - `/usr/share/comindware/configs/instance/<instanceName>.yml`
    - `/var/www/<instanceName>/adapterhost.yml`
    - `/var/www/<instanceName>/apigateway.yml`

    При этом:

    - `mq.group` и `mq.node` не должны совпадать между собой;
    - **если узлов несколько**, значения параметра `mq.node` должны быть разными на разных узлах.

    Пример конфигурации **с одним узлом**:

    ``` yaml
    # Имя экземпляра ПО
    clusterName: <instanceName>
    ##### Настройка очереди сообщений #####
    # Адрес и порт сервера очереди сообщений {{ apacheKafkaVariants }}.
    mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
    # Идентификатор группы очереди сообщений.
    mq.group: <instanceName>
    # Префикс имени очередей сообщений.во
    mq.name: <instanceName>
    # Идентификатор узла очереди сообщений.
    # Должен быть разным на разных узлах.
    # Не должен совпадать с mq.group.
    mq.node: <instanceName>_Exclusive
    ```
