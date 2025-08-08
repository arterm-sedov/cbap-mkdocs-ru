---
title: Обновление версии экземпляра ПО
kbId: 
---

# Обновление версии экземпляра ПО {: #upgrade_version_linux }

## Введение

Здесь представлены инструкции по обновлению версии экземпляра ПО **{{ productName }}** с 4.7.2 до версий 4.7.3–5.0 для ОС Linux.

## Порядок обновления версии экземпляра ПО

Обновить версию экземпляра ПО можно одним из двух способов:

- [обновить контейнеры с ПО](#обновление-контейнеров);
- [обновить Helm-чарт **{{ productName }}**](#обновление-helm-чарта).

### Обновление контейнеров

1. Сохраните резервную копию экземпляра ПО. См. _«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]»_.
2. Выполните команду:

    ``` sh
    helm upgrade --set image.name=<SET-NAME> --set image.tag=<SET-VERSION> <HELM-RELEASE-NAME> <HELM-CHART>
    ```

    **Здесь:**

    - `<SET-NAME>` — имя контейнера для обновления;
    - `<SET-VERSION>` — целевая версия контейнера;
    - `<HELM-RELEASE-NAME>` — имя Helm-релиза для **{{ productName }}**;
    - `<HELM-CHART>` — путь к директории (`./comindware-v.5.W.XYZ.0/`), путь к файлу `.tgz` чарта или FQDN-имя Helm-чарта.

3. Убедитесь, что обновление было выполнено успешно:

    ``` sh
    helm list
    kubectl get pods
    ```

4. В браузере откройте URI Ingress-эндпоинта с **{{ productName }}**.
5. Если отобразится страница режима обслуживания, инициализируйте экземпляр ПО. См. _«[Инициализация {{ productName }}][deploy_guide_linux_initialize]»_.

### Обновление Helm-чарта { .pageBreakBefore }

1. Сохраните резервную копию экземпляра ПО.
2. Ознакомьтесь с разницей между текущей и новой версией чарта:

    ``` sh
    helm diff upgrade <HELM-RELEASE-NAME> <TARGET-HELM-CHART>
    ```

    **Здесь:**

    - `<HELM-RELEASE-NAME>` — имя Helm-релиза для **{{ productName }}**;
    - `<TARGET-HELM-CHART>` — путь к директории (`./comindware-v.5.W.XYZ.0/`), путь к файлу `.tgz` чарта или FQDN-имя Helm-чарта.

3. Выполните обновление с помощью команды:

    ``` sh
    helm upgrade <HELM-RELEASE-NAME> <TARGET-HELM-CHART>
    ```

4. Убедитесь, что обновление было выполнено успешно:

    ``` sh
    helm list
    kubectl get pods
    ```

5. В браузере откройте URI Ingress-эндпоинта с **{{ productName }}**.
6. Если отобразится страница режима обслуживания, инициализируйте экземпляр ПО. См. _«[Инициализация {{ productName }}][deploy_guide_linux_initialize]»_.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]_
- _[Инициализация {{ productName }}][deploy_guide_linux_initialize]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
