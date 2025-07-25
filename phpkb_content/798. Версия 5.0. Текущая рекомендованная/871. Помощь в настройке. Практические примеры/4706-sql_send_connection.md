---
title: Внешняя СУБД (MySQL, MSSQL, Oracle, PostgreSQL). Отправка SQL-запроса. Настройка подключения, пути передачи данных и сценария
kbId: 4706
---

# Внешняя СУБД (MySQL, MSSQL, Oracle, PostgreSQL). Отправка SQL-запроса. Настройка подключения, пути передачи данных и сценария

## Введение

Здесь представлены инструкции по настройке подключения, пути передачи данных и сценария для отправки SQL-запросов во внешнюю систему управления базами данных (СУБД) с целью получения данных из внешней базы данных (БД) в приложение на основе **{{ productName }}** (далее «Приложение»).

Для обмена данными с СУБД поддерживаются следующие SQL-запросы:

- `SELECT`
  - задайте таблицу для выборки записей из СУБД;
  - задайте условие `WHERE` (необязательно) для выборки записей из СУБД;
  - задайте атрибут для хранения полученных записей из СУБД;
- `UPDATE`
  - задайте таблицу для выборки записей из СУБД;
  - задайте условие `WHERE` (необязательно) для выборки записей из СУБД;
  - задайте атрибуты (поля) записей, которые требуется изменить в СУБД;
- `INSERT`
  - задайте таблицу для выборки записей из СУБД;
  - задайте атрибуты (поля) записей, которые требуется создать в СУБД;
- `DELETE`
  - задайте таблицу для выборки записей из СУБД;
  - задайте условие `WHERE` (обязательно) для выборки записей, которые требуется удалить из СУБД;
- пользовательский запрос:
  - задайте собственный шаблон запроса, в который можно подставить значения **атрибутов сообщения**, например:

    ```
    -- {my_id} — заполнитель с системным именем атрибута сообщения,
    -- значение которого будет подставлено в запрос
    SELECT * FROM TableName WHERE Id={my_id}
    ```
  - задайте атрибут для хранения полученного результата;
  - задайте тип возвращаемого результата:
    - **без результата**;
    - **набор записей**;
    - **скалярное значение** (возвращаемое скалярной функцией SQL).

Настройка приложения для обмена данными с СУБД MySQL, MSSQL, Oracle и PostgreSQL осуществляется аналогичным образом.

См. также статью *«[Внешняя СУБД (MySQL, MSSQL, Oracle, PostgreSQL). Получение данных по таймеру. Настройка подключения, пути передачи данных и сценария][sql_receive_connection]».*

## Прикладная задача

Посредством запроса `SELECT` к внешней СУБД необходимо получать из таблицы `cities` названия городов, находящихся в стране, по трехбуквенному коду страны в формате ISO 3166-1.

### Исходные данные

Внешняя БД содержит таблицу `cities` со следующими столбцами:

- `countryCode` типа `CHAR(3)` — трехбуквенный код страны, в которой находится город;
- `cityName` типа `TINYTEXT` — название города.

В приложении имеется шаблон записи *«Страны»* с атрибутами:

- *Код страны* (системное имя *CountryCode*):
  - **Тип данных: текст**
- *Города страны*
  - **Системное имя:** *Cities*
  - **Тип данных: запись**
  - **Связанный шаблон**: *Города*
  - **Хранить несколько значений**: флажок установлен

В приложении имеется шаблон записи *«Города»* с атрибутом:

- *Название города*
  - **Системное имя**: *cityName*
  - **Тип данных: текст**
  - **Использовать как заголовок записей**: флажок установлен

В шаблоне записи *«Страны»* на основную форму вынесены следующие атрибуты:

- *Код страны* — текстовое поле;
- *Города страны* — таблица со столбцом *«Название города».*

## Подготовка сервера СУБД

Перед подключением из **{{ productName }}** необходимо подготовить конфигурацию сервера СУБД, как указано ниже.

### Настройка конфигурации сервера PostgreSQL

Настройка серверов MySQL, MSSQL и Oracle осуществляется аналогично.

1. Откройте для редактирования файл `postgresql.conf`.

   - В ОС Linux путь к этому файлу можно узнать с помощью следующей команды:

     ```
     sudo -u postgres psql -c 'SHOW config_file'
     ```
   - В ОС Windows путь к файлу по умолчанию:

     ```
     C:\ProgramData\PostgreSQL\X.X\data\postgresql.conf
     ```

     Здесь `X.X` — номер версии PostgreSQL.
2. В файле `postgresql.conf` добавьте следующие директивы:

   - Разрешите подключение со всех IP адресов:

     ```
     listen_addresses = '*'
     ```
   - Задайте локаль для вывода сообщений об ошибках:

     ```
     lc_messages = 'en_EN.utf-8'
     ```
3. Откройте для редактирования конфигурационный файл `pg_hba.conf` (в той же директории, что файло `postgresql.conf`).
4. В файле `pg_hba.conf` разрешите подключение с адреса сервера **{{ productName }}** (например, `123.45.67.89`):

   ```
   host    all    all    123.45.67.89    md5
   ```
5. Перезапустите службу `postgresql`:

   **Linux**

   ```
   sudo systemctl restart postgresql
   ```

   **Windows**

   ```
   net stop postgresql-x64-<номер_версии>
   ```

## Создание подключения к СУБД

1. Откройте страницу «**Администрирование**» — «**Подключения**».
2. Создайте **SQL-подключение** типа «**Отправки запросов в СУБД**».

   ![Меню создания подключения для отправки запросов в СУБД](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_menu.png)

   Меню создания подключения для отправки запросов в СУБД
3. В поле «**Системное имя**» введите уникальное имя подключения, например `SendRquestToDBConnection`.
4. В поле «**Описание**» введите наглядное описание назначения подключения, например *«Подключение для отправки запросов в СУБД»*.
5. В поле «**Запись в файловые журналы**» укажите, какие события при обмене данными с сервером СУБД следует регистрировать в журнале:

   - **Полные сведения об обработке сообщения**
   - **Только ошибки**
   - **Отключить**
6. В поле «**Строка подключения**» введите адрес сервера, имя базы данных, имя пользователя и пароль для подключения к СУБД:

   **MySQL**

   ```
   Server=ServerAddress;Database=DataBaseName;Uid=Username;Pwd=Password;
   ```

   **MSSQL**

   ```
   Server=ServerAddress;Database=DataBaseName;User Id=Username;Pwd=Password;
   ```

   **Oracle**

   ```
   Data Source=DataBaseName;User Id=Username;Password=Password;Integrated Security=no;
   ```

   **PostgreSQL**

   ```
   Host=ServerAddress;Database=DataBaseName;User ID=Username;Password=Password;
   ```
7. В поле «**Система управления базами данных**» выберите тип СУБД:

   - **MySQL**
   - **MSSQL**
   - **Oracle**
   - **PostgreSQL**
8. Нажмите кнопку «**Создать**».
9. В списке подключений дважды нажмите строку созданного подключения.
10. В окне свойств подключения нажмите кнопку «**Проверить соединение**».
11. Если проверка соединения не выдала ошибок, нажмите кнопку «**Сохранить**».

## Создание пути для обмена данными с СУБД

1. Со страницы «**Администрирование**» приложения перейдите в раздел «**Пути передачи данных**».
2. Создайте **путь передачи данных** типа «**SQL-подключения — Отправка запросов в СУБД**».

   ![Меню создания пути передачи данных для отправки запросов в СУБД](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_menu_paths.png)

   Меню создания пути передачи данных для отправки запросов в СУБД
3. В поле «**Подключение**» выберите ранее созданное подключение для отправки запросов в СУБД, например *«Отправка запросов в СУБД»*.
4. В поле «**Системное имя**» введите уникальное имя пути передачи данных, например `SendRequestToDBCommunicationRoute`.
5. В поле «**Описание**» введите наглядное описание пути передачи данных, например *«Путь для отправки данных в СУБД»*.
6. Откройте вкладку «**Атрибуты сообщений**».
7. В поле «**Тип сообщения**» выберите пункт «**Выполнить запрос SELECT**».
8. В таблице «**Запрос**» оставьте созданные автоматически атрибуты, они будут использоваться в сценарии для формирования SQL-запроса.
9. В области «**Ответ**» нажмите кнопку «**Добавить**», чтобы создать:

   - атрибут `Cities` типа «**Объект**» с установленным флажком «**Массив**» — этот атрибут будет содержать массив названий городов, полученных из внешней БД (системное имя этого атрибута может быть любым);
10. В таблице атрибутов установите флажок у атрибута `Cities` и нажмите кнопку «**Добавить**», чтобы создать:

    - вложенный атрибут `cityName` типа «**Строка**» — этот атрибут будет содержать название города, и его системное имя должно совпадать с именем столбца с названиями городов в таблице полученной из внешней БД.
    - вложенный атрибут `countryCode` типа «**Строка**» — этот атрибут будет содержать код страны, и его системное имя должно совпадать с именем столбца с кодами стран в таблице полученной из внешней БД.![Настройка атрибутов для отправки SQL-запроса SELECT и получения ответа от СУБД](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_attributes_settings.png)

    Настройка атрибутов для отправки SQL-запроса SELECT и получения ответа от СУБД
11. Откройте вкладку «**Интеграция**».
12. В поле «**Таблица**» укажите имя таблицы в базе данных, из которой требуется получать данные, например `cities`.
13. В поле «**Атрибут для хранения полученных записей**» укажите системное имя атрибута `Cities`, созданного на вкладке «**[Атрибуты сообщений](#message_attributes)**».
14. Поле «**SQL-запрос**» оставьте пустым. Если его заполнить, то будет проигнорирован запрос, сформированный с помощью сценария и атрибутов на вкладке «[**Атрибуты сообщений**](#message_attributes)».
15. Сохраните настроенный путь для обмена данными с СУБД.

    ![Настройка параметров интеграции для отправки запроса в СУБД](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_parametres_settings.png)

    Настройка параметров интеграции для отправки запроса в СУБД

## Создание кнопки для отправки SQL-запроса в СУБД

1. Откройте вкладку «**Кнопки**» шаблона записи *«Страны»*.
2. Создайте кнопку *«Получить города из СУБД»* со следующими свойствами:

   - **Контекст операции: запись**
   - **Операция: вызвать событие «Нажата кнопка»**
   - **Результат выполнения: обновить данные**![Настройка кнопки «Получить города из СУБД»](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_receive_cities.png)

   Настройка кнопки «Получить города из СУБД»
3. Добавьте кнопку *«Получить города из СУБД»* на основную форму шаблона *«Страны»*.

   ![Добавление кнопки «Получить города из СУБД» на основную форму шаблона «Страны»](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_country_button.png)

   Добавление кнопки «Получить города из СУБД» на основную форму шаблона «Страны»

## Создание сценария для отправки SQL-запроса и получения данных из СУБД

1. Со страницы «**Администрирование**» приложения перейдите в раздел «**Сценарии**».
2. Создайте новый сценарий, нажав кнопку «**Создать**».
3. Настройте свойства сценария:

   - **Название** — введите наглядное название сценария, например *«Запрос городов из СУБД»*.
   - **Системное имя** — введите уникальное имя сценария, например `getCitiesFromDB`.
   - **Контекст выполнения** — выберите пункт «**От имени системы**».
4. Сохраните сценарий.
5. Откройте конструктор сценария, дважды нажав строку созданного сценария в списке сценариев.
6. В отобразившемся конструкторе сценария нажмите кнопку изменить на элементе «**Нажатие кнопки**».

   ![Переход к свойствам элемента сценария](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_scenario_properties_transfer.png)

   Переход к свойствам элемента сценария
7. Настройте свойства события:

   - **Контекстный шаблон** — выберите шаблон записи *«Страны»*;
   - **Кнопка** — выберите ранее созданную кнопку *«Получить города из СУБД»*.
8. Нажмите кнопку «**Сохранить**».

   ![Настройка события получения сообщения из СУБД в сценарии](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_scenario_receive_cities.png)

   Настройка события получения сообщения из СУБД в сценарии
9. Нажмите кнопку «**Добавить действие**» под элементом «**Нажата кнопка**».

   ![Добавление действия «Изменить значение переменных» в сценарий](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_scenario_change.png)

   Добавление действия «Изменить значение переменных» в сценарий
10. Добавьте действие «**Изменить значения переменных**» и настройте его свойства:

    - **Операция со значениями переменных** — **добавить**.
    - **Набор переменных** — укажите наглядное имя, например `SqlRequestBody`, оно будет использоваться в последующих действиях сценария.
    - Нажмите кнопку «**Создать**» над таблицей переменных и добавьте две переменных:

      - **FilterAttributes** — в поле «**Значение**» введите имя столбца `countryCode` из таблицы `cities` во внешней БД.
      - **FilterValues** — в поле «**Значение**» выберите **атрибут** *«Код страны»*.
      - Из этих переменных в последующем действии «**Отправить сообщение**» в SQL-запросе будет сформировано предложение `WHERE FilterAttributes=FilterValues` (например, `WHERE countryCode='RUS'`).
    - Сохраните действие «**Изменить значения переменных**».![Настройка свойств действия «Изменить значения переменных»](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_scenario_change_settings.png)

    Настройка свойств действия «Изменить значения переменных»
11. После действия «**Изменить значения переменных**» добавьте действие «**Отправить сообщение**» и настройте его свойства:

    - **Подключение** — выберите ранее созданное *Подключение для отправки запросов в СУБД*.
    - **Путь передачи данных** — выберите ранее созданный *Путь для отправки данных в СУБД*.
    - **Переменная с сообщением** — введите наглядное имя **набора переменных** `SqlRequestBody`, заданное в предшествующем действии «**Изменить значения переменных**».
    - **Переменная для успешного ответа** — введите наглядное имя переменной для хранения записей, полученных из внешней БД, например `SqlResponse`.
    - введите имя переменной для хранения ответа сервера об успешной операции.
    - **Переменная для ответа с ошибкой** — введите имя переменной для хранения ответа сервера об операции, которую не удалось выполнить.
    - Сохраните действие «**Отправить сообщение**».![Настройка свойств действия «Отправить сообщение»](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_send_message_settings.png)

    Настройка свойств действия «Отправить сообщение»
12. За действием «**Отправить сообщение**» добавьте действие «**Повторять по количеству объектов**» и настройте его свойства:

    - В поле «**Переменная**» введите наглядное имя переменной для итераций в цикле, например `currentRecord`;
    - В поле «**Атрибут или выражение для поиска объектов**» введите следующее выражение:

      - **Формула**

        ```
        $$SqlResponse->City
        ```
      - **N3**

        ```
        @prefix session: <http://comindware.com/ontology/session#>.
        @prefix var: <http://comindware.com/ontology/session/variable#>.
        {
            session:context var:SqlResponse ?message.
            ?message var:City ?value.
        }
        ```
      - Здесь:

        - `SqlResponse` — имя **переменной для успешного ответа**, указанное в свойствах свойствах события «**[Отправить сообщение](#send_message)**».
        - `City` — системное имя атрибута-массива, созданного [на вкладке «**Атрибуты сообщений**»](#message_attributes) в свойствах пути передачи данных.
    - Сохраните действие «**Повторять по количеству объектов**».![Настройка цикла по количеству объектрв в сценарии](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_scenario_cycle_settings.png)

    Настройка цикла по количеству объектрв в сценарии
13. Внутри действия «**Повторять по количеству объектов**» добавьте действие «**Создать запись**» и настройте его свойства:

    - В поле «**Целевой шаблон записи**» выберите шаблон *«Города»*, в котором будут создаваться записи с данными, полученными из внешней БД.![Настройка действия «Создать запись» в сценарии](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_create_record_settings.png)

    Настройка действия «Создать запись» в сценарии
14. Внутри действия «**Создать запись**» добавьте действие «**Изменить значения атрибутов**».
15. В действии «**Изменить значения атрибутов**» на вкладке «**Дополнительно**» установите флажок «**Сбрасывать кэш значений**».
16. На вкладке «**Основные**»:

    - Нажмите кнопку «**Создать**».
    - В столбце «**Атрибут**» выберите атрибут шаблона, указанного [в свойствах действия «**Создать запись**»](#create_record), в который будут помещаться названия городов, полученные из внешней БД.
    - В столбце «**Операция со значениями**» выберите пункт «**Заменить**».
    - В Столбце «**Значение**» введите следующее выражение:

      - **Формула**

        ```
        $$currentRecord->cityName
        ```
      - **N3**

        ```
        @prefix session: <http://comindware.com/ontology/session#>.
        @prefix var: <http://comindware.com/ontology/session/variable#>.
        {
            session:context var:currentRecord ?record.
            ?record var:cityName ?value.
        }
        ```
      - Здесь:

        - `currentRecord` — имя переменной, заданное [в свойствах действия «**Повторять по количеству объектов**»](#object_cycle).
        - `cityName` — системное имя строкового атрибута (в массиве `City`), созданного [на вкладке «**Атрибуты сообщений**»](#message_attributes) в свойствах пути передачи данных.
    - Сохраните действие «**Изменить значения атрибутов**».![Настройка действия «Изменить значения атрибутов» в сценарии](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_change_attributes_settings.png)

    Настройка действия «Изменить значения атрибутов» в сценарии
17. Должен получиться показанный на следующей иллюстрации сценарий.

    ![Сценарий для сохранения данных из внешней БД в шаблон записи](/platform/v5.0/administration/connections_communication_routes/sql_connections/img/sql_send_connection_scenario.png)

    Сценарий для сохранения данных из внешней БД в шаблон записи

## Тестирование сценария

1. Создайте запись в шаблоне *«Страны»* и заполните поле *«Код страны».*
2. Нажмите кнопку *«Получить города из СУБД»*.
3. [Настроенный для кнопки сценарий](#создание-сценария-для-отправки-sql-запроса-и-получения-данных-из-субд) должен создать в шаблоне записи *«Города»* записи с названиями городов, полученных из внешней БД по указанному коду страны.

--8<-- "related_topics_heading.md"

- *[Внешняя СУБД (MySQL, MSSQL, Oracle, PostgreSQL). Получение данных по таймеру. Настройка подключения, пути передачи данных и сценария][sql_receive_connection]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
