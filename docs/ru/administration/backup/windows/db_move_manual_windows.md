---
title: Ручной перенос базы данных экземпляра ПО в ОС Windows
kbId: 4646
---

# Ручной перенос базы данных экземпляра ПО в ОС Windows {: #db_move_manual_windows}

## Введение

Здесь представлена инструкция резервному копированию или восстановлению базы данных экземпляра ПО **{{ productName }}** в операционной системе Windows.

!!! note "Примечание"

    Рекомендуется предварительно прочесть всю инструкцию для понимания процедуры в целом.

Для примера мы рассмотрим перенос базы данных экземпляра ПО c одной машины на другую.

По умолчанию экземпляры ПО развертываются в папке `C:\ProgramData\Comindware\Instances\`

Просмотреть фактический путь к папкам экземпляра ПО можно в *Утилите администрирования*.

1. Выберите экземпляр ПО в списке «***Экземпляры продукта***».
2. Нажмите кнопку «***Настроить***».
3. В отобразившемся окне «***Конфигурация экземпляра продукта***» выберите вкладку «***Пути***».

_![Просмотр путей к папкам экземпляра ПО](https://kb.comindware.ru/assets/img_63885b8e70846.png)_

## Создание резервной копии базы данных

1. Запустите *Утилиту администрирования Comindware* с помощью команды «***Запуск от имени администратора***».
2. В списке «***Экземпляры продукта***» нажмите правой кнопкой мыши экземпляр ПО, подлежащий резервному копированию.
3. <a id="P1.3"></a>В раскрывающемся меню выберите пункт «***Остановить сайт***».

    _![Остановка экземпляра ПО](https://kb.comindware.ru/assets/img_6387604f05db4.png)_

4. Откройте папку экземпляра ПО, подлежащего резервному копированию:

    ```
    C:\ProgramData\Comindware\Instances\<InstanceName>
    ```

    Здесь `<InstanceName>` — имя экземпляра ПО (отображается в списке «***Экземпляры продукта***» в *Утилите администрирования*).

5. Создайте архив `<InstanceName>_DB_Backup.zip` с папками `Data` и `Streams`.

    _![Создание архива с базой данных экземпляра ПО](https://kb.comindware.ru/assets/img_638761f8a46f3.png)_

    _![Содержимое архива с базой данных экземпляра ПО](https://kb.comindware.ru/assets/img_6387625e81e40.png)_

6. Сохраните архив `<InstanceName>_DB_Backup.zip` на накопителе для резервных копий.

## Восстановление резервной копии экземпляра ПО

1. На машине, на которой требуется развернуть экземпляр ПО из резервной копии, запустите *Утилиту администрирования Comindware*  с помощью команды «  ***Запуск от имени администратора***».
2. Создайте новый экземпляр ПО с таким же именем, как исходный экземпляр ПО `<InstanceName>`. См. см. параграф 1.3 статьи «[Создание экземпляра продукта, добавление скрытого экземпляра][admin_utility_instance_create]».
3. В раскрывающемся меню выберите пункт «***Остановить экземпляр***».

    _![Остановка экземпляра ПО](https://kb.comindware.ru/assets/img_6387604f05db4.png)_

4. Откройте папку экземпляра ПО, который требуется развернуть из резервной копии:

    ```
    C:\ProgramData\Comindware\Instances\<InstanceName>
    ```

    Здесь `<InstanceName>` — имя экземпляра ПО (отображается в списке «***Экземпляры продукта***» в *Утилите администрирования*).

5. Распакуйте в папку `<InstanceName>` содержимое архива `<InstanceName>_DB_Backup.zip`.

    _![Распакованное содержимое архива с резервной копией экземпляра ПО](https://kb.comindware.ru/assets/img_6387667cb6fd0.png)_

6. Удалите архив `<InstanceName>_DB_Backup.zip` из папки `<InstanceName>`.
7. Запустите восстановленный из резервной копии экземпляр ПО, выбрав в *Утилите администрирования* команду «***Запустить сайт***».

    _![Запуск экземпляра ПО](https://kb.comindware.ru/assets/img_6387676681aa3.png)_

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
