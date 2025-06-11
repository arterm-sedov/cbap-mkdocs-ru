---
title: Ручной перенос базы данных экземпляра ПО
kbId: 4649
---

# Ручной перенос базы данных экземпляра ПО {: #db_move_manually}

## Введение

Здесь представлена инструкция по переносу копии кэша {{ apacheIgniteVariants }} (далее «Снимки») в новый экземпляр ПО **{{ productName }}** под управлением ОС Linux. Снимки можно создавать онлайн, под пользовательской нагрузкой.

Для примера мы рассмотрим перенос базы данных из снимка, созданного на одной машине, в экземпляр ПО, развёрнутый на другой машине.

На обеих машинах ПО установлено по умолчанию в папке `/var/www/comindware/`

Снимок базы данных {{ apacheIgniteVariants }} будет создан в папке `/var/lib/comindware/<instanceName>/Database/snapshots/`

!!! warning "Внимание!"

    Перенос базы данных можно осуществить только посредством создания снимка {{ apacheIgniteVariants }}! Не пытайтесь создавать копию базы данных на файловом уровне — это приведёт к утрате её работоспособности.

!!! note "Примечание"

    Рекомендуется предварительно прочесть всю инструкцию для понимания процедуры в целом.

## Создание снимка базы данных {: .pageBreakBefore }

1. Все последующие команды следует выполнять от имени суперпользователя `root`. Для этого введите команду:

    --8<-- "linux_sudo.md"

2. Перейдите в папку ПО:

    ```
    cd /var/www/comindware/

    ```

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

3. Откройте файл `Ignite.config` в текстовом редакторе nano:

    ```
    nano -v Ignite.config
    ```

4. Проверьте содержимое директивы `<workDirectory>`:

    ```
    <workDirectory>/path/to/WorkDir</workDirectory>
    ```

    _![Путь к рабочей папке в файле конфигурации {{ apacheIgniteVariants }}](https://kb.comindware.ru/assets/img_63567910ececd.png)_

    Если директива `<workDirectory>` имеется, она содержит путь к рабочей папке базы данных экземпляра ПО.

    Если директива `<workDirectory>` отсутствует, база данных экземпляра ПО хранится в папке `var/www/comindware/data/Database/`

    Путь к базе данных экземпляра ПО: `/var/lib/comindware/<instanceName>/Database/db`. См. _«[Пути и содержимое папок экземпляра ПО][paths]»_.

5. Закройте nano:

    ```
    ctrl+X
    ```

6. Перейдите в папку с базой данных экземпляра ПО в рабочей папке и выведите на экран её содержимое:

    ```
    cd /var/lib/comindware/<instanceName>/Database/dbdb/ && ll

    ```

    _![Просмотр содержимого папки с базой данных экземпляра ПО](https://kb.comindware.ru/assets/img_635679e668157.png)_

7. Проверьте актуальность данных по дате последней записи — она должна совпадать с датой последней активности платформы. В примере на иллюстрации видно, что содержимое папок `/marshaller` и `/node-29690-2969e7d-e435-43b4-983a-7979ccec12c7/` изменялось 21 октября.
8. Перейдите в папку `/tmp/`:

    ```
    cd /tmp/
    ```

9.  Создайте с помощью nano скрипт `snapshot.sh`:

    ```
    nano snapshot.sh
    ```

    _![Создание скрипта с помощью nano](https://kb.comindware.ru/assets/img_63567a89286c4.png)_

10. Введите скрипт создания снимка, например:

    ```
    now=$(date +%Y_%m_%d)
    /usr/share/ignite/bin/control.sh --snapshot create snapshot_$now
    ```

11. Сохраните скрипт: `ctrl+O` и закройте nano: `ctrl+X`.
12. Запустите созданный скрипт из папки `/tmp/`:

    ```
    sh snapshot.sh
    ```

    _![Запуск скрипта создания снимка](https://kb.comindware.ru/assets/img_63567b113131e.png)_

13. Просмотрите содержимое папки со снимками {{ apacheIgniteVariants }}:
{: .pageBreakBefore }

    ```
    cd /var/lib/comindware/<instanceName>/Database/snapshots/ && ll 
    ```

    _![Содержимое папки со снимками {{ apacheIgniteVariants }}](https://kb.comindware.ru/assets/img_63567d1f7a888.png)_

1.  Создайте архив папки снимка, например, /snapshot\_2022\_10\_21/, и перенесите его на внешнее хранилище.

!!! warning "Важно!"
    При перезапуске ОС содержимое папки `/tmp/` удаляется. Поэтому при необходимости перенесите созданный скрипт в личную папку пользователя.

## Восстановление базы данных экземпляра ПО из снимка на новой машине

1. На чистой машине установите ОС Linux и {{ productName }} последней версии согласно инструкции в статье «[Проверка и настройка конфигурации экземпляра ПО после восстановления из резервной копии][restore_test_configure]».
2. Все последующие команды следует выполнять от имени суперпользователя `root`. Для этого введите команду:

    --8<-- "linux_sudo.md"

3. Создайте папку для базы данных экземпляра ПО (например, `/cmw-db/`):

    ```
    mkdir /var/www/cmw-db/
    ```

    !!! note "Примечание"
        Любые операции копирования в папку базы данных экземпляра ПО и из неё следует выполнять только после отключения сервисов {{ openSearchVariants }}, comindware***<instanceName>*** (где  `<instanceName>` — имя экземпляра ПО), {{ nginxVariants }}, Kafka и Zookeeper.

4. Остановите сервисы:
{: .pageBreakBefore }

    ```
    systemctl stop elasticsearch.service comindware<instanceName>.service nginx.service kafka.service zookeeper.service
    ```

5. Убедитесь, что сервисы остановлены. Статус должен быть `Active: inactive (dead)`:

    ```
    systemctl status zookeeper.service kafka.service nginx.service comindware<instanceName>.service elasticsearch.service

    ```

    _![Проверка остановки сервисов {{ openSearchVariants }}, comindware<instanceName>, {{ nginxVariants }}, Kafka и Zookeeper](https://kb.comindware.ru/assets/img_63567da91a5c6.png)_

6. Скопируйте архив со снимком базы данных экземпляра ПО в папку `/tmp/`.
7. Распакуйте архив в текущую папку.
8. Перенесите содержимое папки снимка (например, `/tmp/snapshot_2022_10_21`) в папку базы данных экземпляра ПО: `/var/www/cmw-db/`

    _![Содержимое папки снимка](https://kb.comindware.ru/assets/img_63567e41566e4.png)_

9. Перейдите в папку с ПО:

    ```
     cd /var/www/comindware/
    ```

10. Откройте файл `Ignite.config` в текстовом редакторе nano:

    ```
    nano Ignite.config
    ```

11. Найдите директиву `<workDirectory>` и укажите в ней путь папке базы данных экземпляра ПО:

    ```
    <workDirectory>/var/www/cmw-db</workDirectory>
    ```

    _![Путь к новой папке базы данных в файле конфигурации {{ apacheIgniteVariants }}](https://kb.comindware.ru/assets/img_63567eabb2a14.png)_

12. Проверьте наличие, а также дату и время создания файлов и папок в папке с базой данных экземпляра ПО:

    ```
    cd /var/www/cmw-db/ && ll
    cd /var/www/cmw-db/db/ && ll
    ```

    Должны быть указаны дата и время создания снимка, если дата и время не совпадают с временем создания снимка, необходимо повторить перенос базы данных.

    _![Проверка наличия, даты и времени создания файлов и папок в папке базы данных экземпляра ПО](https://kb.comindware.ru/assets/img_63567efdbf883.png)_

13. Замените права доступа и владельцев папок:

    ```
    cd /var/www/
    chmod -R 777 cmw-db/
    sudo chown -R www-data:www-data cmw-db/
    ```

14. Проверьте права доступа и владельцев папок:

    ```
    ll
    ```

    _![Проверка прав доступа и владельцев папок](https://kb.comindware.ru/assets/img_635680c397312.png)_

## Запуск и проверка конфигурации экземпляра ПО

1. Запустите необходимые службы и проверьте их статус. Статус должен быть `Active: running`:

    ```
    systemctl start elasticsearch kafka nginx comindware<instanceName>
    systemctl status elasticsearch kafka nginx comindware<instanceName>
    ```

    _![Проверка активного состояния сервисов](https://kb.comindware.ru/assets/img_635680edb9d1d.png)_

2. Перезапустите машину.
3. Откройте в браузере веб-сайт с экземпляром ПО, например `localhost`.
4. Дождитесь инициализации экземпляра ПО после перезапуска. Этот процесс может занять некоторое время. Может потребоваться обновить страницу браузера.

    - Если загрузка веб-страницы экземпляра ПО завершается ошибкой, заново выполните перенос базы данных с полным удалением всего содержимого папки базы данных экземпляра ПО и использованием предыдущей резервной копии.

5. Проверьте и исправьте конфигурацию экземпляра ПО, как указано в статье *«[Проверка и настройка конфигурации экземпляра ПО после восстановления из резервной копии][restore_test_configure]».*

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Проверка и настройка конфигурации экземпляра ПО после восстановления из резервной копии][restore_test_configure]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}