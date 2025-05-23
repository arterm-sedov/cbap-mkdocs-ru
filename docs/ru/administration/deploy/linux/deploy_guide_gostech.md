---
title: Установка и инициализация ПО
kbId: 
---

# Установка и инициализация ПО {: #deploy_guide_linux}

## Введение

Для работы **{{ productName }}** требуются операционная система, сервер базы данных, веб-сервер, обратный прокси-сервер и сервер журналов.

Для быстрого развёртывания **{{ productName }}** в Linux компания **{{ companyName }}** предоставляет дистрибутив с установщиком, настраивающим необходимое программное обеспечение.

Здесь представлены инструкции по развёртыванию и инициализации **{{ productName }}** из дистрибутива в ОС Linux.

## Порядок развёртывания ПО {{ productName }}

1. Убедитесь, что установлен модуль Ansible `kubernetes.core`:

    ``` sh
    ansible-galaxy collection install kubernetes.core
    ```

2. Настройте конфигурацию развёртывания в Ansible Playbook, отредактировав файл `deploy_cmw_chart.yml`, по следующему образцу:

    ``` yaml
    - hosts: localhost
        tasks:
            - name: Deploy CMW Helm chart
            kubernetes.core.helm:
                name: <Name>
                # Укажите путь Helm chart
                chart_ref: </path/to/cmw/chart>
                # Укажите имя пространства имён
                release_namespace: <namespaceName>
                values:
                    global:
                        # Укажите адрес {{ openSearchVariants }} 
                        elasticsearch:
                            elasticsearchUrl: "<platformVSearchIP>:9200"
                        # Укажите адрес брокера сообщений
                        kafka:
                            service_bootstrap: "<kafkaIP>:9092"
                platform:
                    config:
                        # Укажите данные данные интеграции с {{ authServiceVariants }}
                        auth_openId_enabled: "true"
                        auth_openId_server: <plarformViAMServerAddress>
                        auth_openId_realm: <plarformViAMServerRealm>
                        auth_openId_clientId: <plarformViAMServerClientId>
                        auth_openId_clientSecret: <plarformViAMClientSecret>
                    env:
                        # Задайте переменные среды, при необходимости
                        #NEW_ENV_VAR: "<new_value>"
                        #JAVA_HOME: "</new/java/home>"
                initContainers:
                    # Конфигурация репозитория резервных копий
                    url: "https://<new-url-for-backup>.tgz"
                set_values:
                # Конфигурация персистентности
                - "platform.volumes.cmw_database.storageClassName=<new-storage-class>"
                - "platform.volumes.cmw_logs.storageClassName=<new-storage-class>"
                - "platform.volumes.cmw_streams.storageClassName=<new-storage-class>"
                - "platform.volumes.cmw_temp.storageClassName=<new-storage-class>"
                - "platform.volumes.cmw_backup.storageClassName=<new-storage-class>"
    ```

3. В случае необходимости создать values.yml который содержащий требуемые переопределения значений Helm-чарта `comindware-chart`:

    ``` yaml
    platform:
        env:
            <append_your_env_if_needed>: <value>
    volumes:
        cmw-backup:
            storage: 30Gi
            storageClassName: <storageClassName>
        cmw-database:
            storage: 30Gi
            storageClassName: <storageClassName>
        cmw-streams:
            storage: 30Gi
            storageClassName: <storageClassName>
        cmw-temp:
            storage: 30Gi
            storageClassName: <storageClassName>
    ```

4. Запустите Ansible Playbook:

    - Без переопределения значений:

    ``` sh
    ansible-playbook deploy_cmw_chart.yml
    ```

    - С переопределением значений:

    ``` sh
    ansible-playbook deploy_cmw_chart.yml -e “@values.yml
    ```

5. Настройте внешний доступ (эндпоинт) к сервису `comindware-platform-proxy` для Ingress.
6. Откройте эндпоинт, созданный на шаге 5.
7. Дождитесь запуска **{{ productName }}**.
8. Выполните инициализацию ПО.

## Инициализация {{ productName }} {: #deploy_guide_linux_initialize .pageBreakBefore }

{%
include-markdown "./deploy_guide.md"
start="<!--initialize-start-->"
end="<!--initialize-end-->"
%}

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
