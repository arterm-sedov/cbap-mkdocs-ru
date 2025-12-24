!!! warning "Внимание!"

    Директивы `isFederationAuthEnabled` и `manageAdapterHost` требуется удалить, если они присутствуют.
    
    Значения параметров `mq.server` (адрес и порт брокера сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений,) и `cluster.name` / `clusterName` (имя экземпляра ПО) должны совпадать в трёх файлах конфигурации:

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
    # Адрес и порт брокера сообщений {{ apacheKafkaVariants }}.
    mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
    # Идентификатор группы очереди сообщений.
    mq.group: <instanceName>
    # Префикс имени очередей сообщений.
    mq.name: <instanceName>
    # Идентификатор узла очереди сообщений.
    mq.node: <instanceName>
    ```
