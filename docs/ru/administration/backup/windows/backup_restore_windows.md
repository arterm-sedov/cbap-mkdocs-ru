---
title: 'Резервное копирование и восстановление в Windows'
kbId: 4644
---

# Резервное копирование и восстановление {{ productName }} в ОС Windows {: #backup_restore_windows }

## Введение {: #backup_restore_windows_intro }

Здесь представлены инструкции по резервному копированию и восстановлению данных **{{ productName }}** в ОС Windows.

См. также «_[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]»_.

## Подготовка к резервному копированию и восстановлению данных {: #backup_restore_windows_prepare }

Для создания резервных копий и восстановления из них данных **{{ productName }}** необходимо подготовить перечисленные ниже сведения.

1. Подготовьте данные о конфигурации экземпляра ПО:

    - Имя экземпляра ПО — `<instanceName>`.
    - Путь к папке резервных копий базы данных — `<DatabaseBackupPath>` (например, `X:\DatabaseBackups`).  См. _«[Настройка конфигураций и запуск резервного копирования][backup_configure_list_view]»_.
    - `<distPath>` — путь к распакованному дистрибутиву ПО **{{ productName }}**.

2. Подготовьте данные о конфигурации {{ openSearchVariants }}:

    - Путь к файлу конфигурации {{ openSearchVariants }} `elasticsearch.yml` (например: `C:\ElasticsearchData\elasticsearch.yml`)
    - Имя репозитория снимков {{ openSearchVariants }} — `<repository_name>` (например, `elastic_backup`).
    - Путь к репозиторию снимков {{ openSearchVariants }} — `<elastic_backup_path>`(например, `e:\elastic_backup`).
    - Имя снимка {{ openSearchVariants }} — `<snapshot_name>` (например, `<instanceName>01022022080800` — в формате `<instanceName><Date><Time>`).

    См. [документацию {{ openSearchVariants }} по формированию имён снимков](https://www.elastic.co/guide/en/elasticsearch/reference/current/api-conventions.html#api-date-math-index-names).

## Порядок резервного копирования данных экземпляра ПО {: #backup_restore_windows_prepare_sequence_backup }

Данные экземпляра ПО находятся в двух хранилищах: базе данных экземпляра ПО и на сервере {{ openSearchVariants }}. Cм. _«[Подготовка к резервному копированию и восстановлению данных](#backup_restore_windows_prepare)»_.

Здесь представлен следующий порядок резервного копирования:

1. [Сохраните резервную копию базы данных экземпляра продукта][backup_configure_list_view].
2. [Создайте снимок сервера {{ openSearchVariants }}](#backup_restore_windows_registry_snapshot). Этот шаг может не потребоваться в зависимости от вашей конфигурации {{ openSearchVariants }}.

### Регистрация репозитория и создание снимка {{ openSearchVariants }} {: #backup_restore_windows_registry_snapshot }

!!! question "Определения"

    **{{ openSearchVariants }}** — служба журналирования транзакций в составе **{{ productName }}**.

    **Снимок** — набор данных, сохранённый на определённый момент времени.

1. Настройте конфигурацию репозитория снимков сервера {{ openSearchVariants }} в файле `elasticsearch.yml`:

    ``` yaml
    path.repo: <elastic_backup_path>
    ```

2. Чтобы зарегистрировать репозиторий, выполните следующую команду, указав в URL имя репозитория `<repository_name>` (см. _«[Подготовка к резервному копированию и восстановлению данных](#backup_restore_windows_prepare)»_), а в параметре `location` — путь к репозиторию из директивы `path.repo` в файле конфигурации сервера {{ openSearchVariants }}:

    ``` sh
    curl -X PUT "<openSearchHost>:<opeSearchPort>/_snapshot/<repository_name>?pretty" -H 'Content-Type: application/json' -d' {"type": "fs", "settings": {"location": "<elastic_backup_path>"}}'
    ```

    См. [документацию {{ openSearchVariants }} по регистрации репозитория](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-register-repository.html).

3. Чтобы создать снимок {{ openSearchVariants }}, выполните следующую команду, указав имя снимка `<snapshot_name>`, а в параметре `indices` — индексы, которые требуется включить в снимок (индексы {{ productName }} имеют префикс, например, `cmw_<instanceName>_`):

    ``` sh
    curl -X PUT "<openSearchHost>:<opeSearchPort>/_snapshot/<repository_name>/<snapshot_name>?wait_for_completion=true&pretty" -H 'Content-Type: application/json' -d' {"indices": "cmw_<instanceName>_*", "ignore_unavailable": true, "include_global_state": false}'
    ```

    См. [документацию {{ openSearchVariants }} по созданию снимков](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-take-snapshot.html).

## Порядок восстановления данных экземпляра ПО  {: #backup_restore_windows_prepare_sequence_restore }

!!! warning "Внимание!"

    Перед восстановлением данных остановите экземпляр ПО.

    См. _«[Установка, запуск, инициализация и остановка Comindware Platform в Windows][deploy_guide_windows]»_.

1. [Восстановите базу данных экземпляра ПО](#backup_restore_windows_instance).
2. [Восстановите снимок данных {{ openSearchVariants }}](#backup_restore_windows_opensearch). Этот шаг может не потребоваться в зависимости от вашей конфигурации {{ openSearchVariants }}.

### Восстановление базы данных экземпляра продукта {: #backup_restore_windows_instance }

1. Запустите _PowerShell_ от имени администратора.
2. Перейдите в директорию со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "<distPath>\CMW_Windows<versionNumber>\scripts"
    ```

3. Остановите экземпляр ПО:

    ``` powershell
    .\instance_stop.ps1 -name <instanceName>
    ```

4. Удалите или переместите директорию `Database` из  директории  экземпляра ПО:

    ``` powershell
    Remove-Item -Path "C:\ProgramData\comindware\Instances\<instanceName>\Database" -Recurse
    ```

5. Распакуйте zip-архив резервной копии экземпляра ПО с расширением `CDBBZ` из папки `<DatabaseBackupPath>`.
6. Скопируйте в экземпляр ПО распакованную резервную копию базы данных:

    ``` powershell
    Copy-Item -Path "<config_backup_path>\Database" -Destination "C:\ProgramData\сomindware\Instances\<instanceName>" -Recurse -Force
    ```

    Здесь: `<config_backup_path>` — директория с распакованной резервной копией.

7. Запустите экземпляр ПО:

    ``` powershell
    .\instance_start.ps1 -name <instanceName>
    ```

8.  Откройте сайт экземпляра ПО в браузере, одновременно открыв выдачу журналов экземпляра в _PowerShell_:

    ``` powershell
    Get-Content "C:\ProgramData\comindware\Instances\<instanceName>\Logs\heartbeat_<ГГГГ-ММ-ДД>.log" -Wait
    ```

9. Проверьте и при необходимости исправьте конфигурацию экземпляра ПО. См. _«[Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]»_.
10. Проверьте и работоспособность экземпляра ПО.
11. Создайте резервную копию работоспособного экземпляра **{{ productName }}**.

### Восстановление снимка {{ openSearchVariants }} {: #backup_restore_windows_opensearch }

1. Выполните следующую команду, указав имя репозитория `<repository_name>` и имя снимка `<snapshot_name>` (см. _«[Подготовка к резервному копированию и восстановлению данных](#backup_restore_windows_prepare)»_):

``` sh
curl -X POST "<openSearchHost>:<opeSearchPort>/_snapshot/<repository_name>/<snapshot_name>/_restore?pretty"
```

Подробные сведения о восстановлении снимков {{ openSearchVariants }} см. в официальной документации (на английском языке): <https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-restore-snapshot.html>

--8<-- "related_topics_heading.md"

- [Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]
- [Пути и содержимое директорий экземпляра ПО][paths]
- [Установка, запуск, инициализация и остановка Comindware Platform в Windows][deploy_guide_windows]
- [Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]
- [Документация {{ openSearchVariants }} по формированию снимков (на английском языке)](https://www.elastic.co/guide/en/elasticsearch/reference/current/api-conventions.html#api-date-math-index-names)
- [Документация {{ openSearchVariants }} по регистрации репозитория (на английском языке)](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-register-repository.html)
- [Документация {{ openSearchVariants }} по созданию снимков (на английском языке)](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-take-snapshot.html)
- [Документация {{ openSearchVariants }} по о восстановлению снимков (на английском языке)](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-restore-snapshot.html)

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
