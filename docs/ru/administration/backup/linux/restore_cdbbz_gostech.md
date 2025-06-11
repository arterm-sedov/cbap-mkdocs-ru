---
title: Восстановление базы данных из файла резервной копии в формате .CDBBZ
kbId: 4647
tags: 
    - развёртывание
    - резервное копирование
    - восстановление
hide: tags
---

# Восстановление базы данных из файла резервной копии в формате .CDBBZ {: #backup_restore_cdbbz}

## Введение

Здесь представлены инструкции по восстановлению базы данных **{{ productName }}** для следующего сценария:

- используется ранее настроенный экземпляр ПО **{{ productName }}** под управлением ОС Linux;
- имеется файл резервной копии базы данных с расширением `.CDBBZ`;
- резервная копия создана с помощью встроенной в ПО функции «**Резервное копирование**» (см. *«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]»*);

## Порядок восстановления

1. Подготовьте экземпляр Цифрового продукта к восстановлению из резервной копии, расположив файл резервного копирования на доверенном и доступном URI, например `https://<my-storage-resource>/backup.tgz` (`<my-storage-resource>` — адрес хранилища резервных копий).
2. Добавьте конфигурацию для восстановления из резервной копии к файлу `values.yml`:

    ``` yaml
    initContainers:
        backupfilename: backup.tgz
        repository: busybox
        tag: latest
        # Укажите URI резервной копии
        url: https://<my-storage-resource>/backup.tgz
    
    platform:
        config:
            clusterName: <backupsClusterName>
    ```

3. Запустите Ansible-playbook с конфигурацией `values.yml` для создания экземпляра ПО с восстановлением из резервной копии:

    ``` sh
    ansible-playbook deploy_cmw_chart.yml -e “@values.yml
    ```

4. Удостоверьтесь, что ресурсы экземпляра ПО были развёрнуты:

    ``` sh
    kubectl get pods -n my-namespace
    ```

5. Настройте внешний доступ к сервису `comindware-platform-proxy` для Ingress.
6. Откройте URI, созданный на шаге 5.
7. Дождитесь запуска **{{ productName }}**. Этот процесс может занять некоторое время. Может потребоваться обновить страницу браузера.
8. Выполните [инициализацию {{ productName }}][deploy_guide_linux_initialize].
9. Удостоверьтесь, что все данные из резервной копии восстановлены.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]_
- _[Инициализация {{ productName }}][deploy_guide_linux_initialize]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
