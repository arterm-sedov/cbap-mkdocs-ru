---
title: Отправка эл. почты из сценариев
kbId: 2584
tags:
    - сценарий
    - отправка эл. почты
    - отправка писем
    - SMTP
    - Exchange
hide: tags
---

# Отправка эл. почты из сценариев через SMTP и Exchange. Настройка подключения, пути передачи данных и сценария {: #scenario_send_email}

## Введение

В **{{ productName }}** можно настроить отправку эл. почты из [сценариев][scenarios]. При этом письма могут содержать данные из шаблонов, в том числе вложенные файлы.

Для отправки эл. почты с помощью сценариев используются подключения типов «**Отправка эл. почты через SMTP**» и «**Отправка эл. почты через Exchange**». В [процессах][process_diagram] используются подключения типа «**[Отправка эл. почты из процесса][process_sending_connection]**».

Здесь представлены общие инструкции по настройке подключения к почтовому серверу по протоколу SMTP или Exchange, пути передачи данных и сценария для отправки эл. писем.

## Порядок настройки отправки эл. писем из сценария

1. Настройте [подключение](#настройка-подключения-к-почтовому-серверу-для-отправки-почты-из-сценария) к почтовому серверу типа «**Отправка почты через SMTP**» или «**Отправка эл. почты через Exchange**».
2. Настройте [путь передачи данных](#настройка-пути-передачи-данных-для-отправки-эл-почты-из-сценария) типа «**Отправка эл. почты через SMTP**» или «**Отправка эл. почты через Exchange**», использующий созданное подключение.
3. Настройте [шаблон](#настройка-шаблона-записи) с данными для эл. писем.
4. Настройте [сценарий](#настройка-сценария), который будет отправлять письма посредством настроенных подключения и пути передачи данных.

## Настройка подключения к почтовому серверу для отправки почты из сценария

1. Откройте страницу «**Администрирование**» — «**Подключения**».
2. Откройте двойным нажатием в списке или создайте подключение типа «**Подключения к электронной почте**» — «**Отправка почты через SMTP**» или «**Отправка эл. почты через Exchange**».
3. Настройте свойства подключения:

    - **Системное имя** — введите уникальное имя подключения. Рекомендуется использовать буквы латинского алфавита, цифры и символ «_».
    - **Отключить** — установите этот флажок, если требуется временно деактивировать данное подключение.
    - **Описание** — введите наглядное описание подключения, например _«Подключение для отправки писем из сценариев»_.
    - **Запись в файловые журналы** — выберите, какие события следует записывать в журналы:
        - **Полные сведения об обработке сообщения**;
        - **Только ошибки**;
        - **Отключить** — не регистрировать в журнале события отправки писем.
    - **Для SMTP-сервера**
        - **Адрес почтового сервера** — введите адрес SMTP-сервера <u>без указания протокола (`SMTP`, `HTTPS`, `HTTP`)</u>.
        - **Порт** — введите номер порта SMTP-сервера.
        - **Шифрование** — выберите протокол шифрования, который поддерживает SMTP-сервер:
            - **Отсутствует** — не использовать шифрование;
            - **SSL**;
            - **TLS**.
        - **Проверять соединение без отправки сообщения** — установите этот флажок, чтобы проверить соединение без указания получателей тестового письма.
        - **Адреса получателей для проверки работоспособности подключения** — укажите один или несколько (через запятую) адресов эл. почты для проверки соединения.
    - **Для сервера Exchange**
        - **URL веб-сервера Exchange** — введите адрес почтового сервера <u>без указания протокола (`HTTPS`, `HTTP`)</u>.
        - **Версия Exchange** — выберите версию сервера Exchange.
    - **Тип аутентификации** — выберите способ проверки подлинности, используемый сервером Exchange:
        - **Отсутствует**;
        - **Базовая**;
        - **Аутентификация Windows**.
    - **Имя пользователя** — укажите учетную запись для подключения к почтовому серверу.
    - **Пароль** — введите пароль для подключения к почтовому серверу.
    - **Домен** — укажите домен пользователя почтового сервера.
    - **Имя отправителя** — укажите имя, которое будет указано в отправляемых письмах.
    - **Адрес эл. почты отправителя** — укажите адрес эл. почты, который будет указан в отправляемых письмах. Почтовый сервер может проверять соответствие адреса отправителя и **имени пользователя**, отправляющего почту.

        !!! note "Примечание"

            Если **адрес** или **имя отправителя** не совпадает с адресом и именем, указанным в учётной записи, используемой для подключения к почтовому серверу, сервер должен поддерживать замену данных отправителя. В противном случае, почта не будет отправляться.

4. Нажмите кнопку «**Проверить соединение**».
5. Если используется SMTP-сервер, удостоверьтесь, что получателям пришло тестовое письмо от настроенного отправителя.
6. Чтобы просмотреть журнал событий отправки писем, нажмите кнопку «**Скачать журнал**».
7. Сохраните подключение.

## Настройка пути передачи данных для отправки эл. почты из сценария

1. Откройте страницу «**Администрирование**» — «**Пути передачи данных**».
2. Откройте двойным нажатием в списке или создайте подключение типа «**Подключения к электронной почте**» — «**Отправка почты через SMTP**» или «**Отправка эл. почты через Exchange**».
3. Настройте свойства пути передачи данных на следующих вкладках:

    - [**Основные свойства**](#основные-свойства)
    - [**Атрибуты сообщения**](#атрибуты-сообщения)
    - [**Интеграция**](#интеграция)

4. Сохраните путь передачи данных.

### Основные свойства

На вкладке «**Основные свойства**» настройте параметры использования пути передачи данных.

- **Подключение** — выберите [подключение для отправки эл. почты из сценариев через SMTP или Exchange](#настройка-подключения-к-почтовому-серверу-для-отправки-почты-из-сценария).
- **Системное имя** — введите уникальное имя пути передачи данных. Рекомендуются буквы латинского алфавита, цифры и символ «_».
- **Отключить** — установите этот флажок, если требуется временно деактивировать данный путь передачи данных.
- **Описание** — введите наглядное описание пути передачи данных, например _«Путь для отправки писем из сценариев»_.
- **Номер шины данных** — выберите номер от 0 до 3, если требуется распределить потоки данных нескольких путей для повышения производительности.

### Атрибуты сообщения

На вкладке «**Атрибуты сообщения**» настройте атрибуты, значения которых будут подставляться в содержимое в эл. письма.

Значения атрибутов сообщения необходимо присвоить с помощью [сценария](#настройка-сценария).

- В таблице «**Запрос**» имеются готовые атрибуты сообщения в виде массивов объектов:
    - **To** — получатели писем.
        - **Name** — имя получателя.
        - **Address** — адрес эл. почты.
    - **Attachments** — прикреплённые файлы.
        - **Name** — название файла.
        - **Extension** — расширение файла.
        - **Content** — содержимое файла.
    - **Cc** — копии.
        - **Name** — имя получателя.
        - **Address** — адрес эл. почты.
    - **Bcc** — скрытые копии.
        - **Name** — имя получателя.
        - **Address** — адрес эл. почты.
    - **CustomHeaders** — дополнительные заголовки.
        - **Name** — имя заголовка.
        - **Value** — значение заголовка.
        - **ListValues** — массив неименованных значений.
- Добавьте собственные атрибуты сообщения для подстановки в письмо с помощью вкладки [«**Интеграция**»](#интеграция), например:
    - _FullName_ типа «**Строка**» для Ф. И. О. получателя;
    - _Filename_ типа «**Строка**» для имени прикрепляемого файла;
    - _RecepientEmail_ типа «**Строка**» для эл. почты получателя;
    - _Subject_ типа «**Строка**» для темы письма;
    - _Body_ типа «**Строка**» для темы письма;
    - _ReplyAddress_ типа «**Строка**» для выбора электронной почты, на которую должны приходить ответные письма.

### Интеграция

На вкладке «**Интеграция**» настройте дополнительные свойства эл. письма, заполнив их статическими значениями или заполнителями [**атрибутов сообщения**](#атрибуты-сообщения).

!!! danger "Внимание!"

    Прежде чем подставлять в письмо заполнители атрибутов сообщения, их необходимо добавить в таблицу «**Запрос**» на вкладке «**[Атрибуты сообщения](#атрибуты-сообщения)**». В противном случае путь передачи данных будет автоматически отключён.

!!! warning "Подстановка значений атрибутов сообщения в эл. письмо"

    - Чтобы поместить значение **атрибута сообщения** в эл. письмо, введите его системное имя в фигурных скобках `{ }` — **заполнитель** — в соответствующее поле письма на вкладке «**Интеграция**».
    - В текстовые поля (шаблон темы, шаблон текста сообщения, получатели, копия, скрытая копия) можно вводить произвольный текст и подставлять **заполнители атрибутов сообщения**.
    - Например, в поле «**Шаблон темы**» можно ввести строку:
        
        ```
        Уведомление «{Title}» от {Date} 
        ```
        
        Здесь: `{Title}` и `{Date}` — заполнители атрибутов сообщения, содержащее название и дату уведомления.


    !!! note "Примечание"

        Атрибуты сообщения типа «**Объект**» нельзя подставить в письмо посредством заполнителей.

- **Шаблон темы** — введите заголовок письма, например:

    ```cs
    Документ {Filename} к рассмотрению.
    ```

- **Шаблон текста сообщения** — введите текст письма, например:

    ```cs
    Здравствуйте, {FullName}!

    Рассмотрите документ {Filename}.
    ```

- **Дополнительные заголовки** — введите служебные заголовки письма с помощью строковых литералов или заполнителей:
    - Имя заголовка — строка (заполнители не поддерживаются), например:

        ```cs
        # Заголовок адреса для ответа
        Reply-To
        ```

    - Значение заголовка — строка или заполнитель, например:

        ```cs
        # Адрес для ответа на письмо
        {ReplyAddress}
        ```

- **Получатели**, **Копия**, **Скрытая копия** — укажите адресатов письма с помощью строковых литералов или заполнителей, например:
    - **Ф. И. О.**:

        ```cs
        {FullName}
        ```

    - **Адрес**:

        ```cs
        {RecepientEmail}
        ```

- **Прикреплённые файлы**
    - **Название документа** — введите строковый литерал с именем файла, включая расширение (заполнители не поддерживаются). Например:

    ```cs
    example.txt
    ```

    - **Содержимое документа** — введите строку с содержимым файла в формате Base64 (заполнители не поддерживаются). Например:

    ```cs
    0K3RgtC+INC/0YDQuNC80LXRgCDRgdGC0YDQvtC60Lgg0LIg0LrQvtC00LjRgNC+0LLQutC1IEJhc2U2NC4=
    ```

    !!! question "Формат Base64"

        **Base64** — это формат кодирования двоичных данных при помощи 64 символов ASCII. Он широко используется для представления файлов в содержимом письма. 
        
        Например, строка:

        ```cs
        Это пример строки в кодировке Base64.
        ```

        в формате Base64 будет выглядеть следующим образом:

        ```cs
        0K3RgtC+INC/0YDQuNC80LXRgCDRgdGC0YDQvtC60Lgg0LIg0LrQvtC00LjRgNC+0LLQutC1IEJhc2U2NC4=
        ```

## Настройка шаблона записи и сценария для отправки эл. почты

### Настройка шаблона записи

1. Создайте шаблон записи _«Эл. письма»_.
2. Создайте следующие атрибуты:

    - _Получатель_ типа «**Аккаунт**»;
    - _Вложение_ типа «**Документ**».

3. Создайте кнопку _«Отправить письмо»_ со следующими свойствами:

    - **Контекст операции: запись**
    - **Операция: вызвать событие «Нажата кнопка»**
    - **Результат выполнения: обновить данные**

4. Добавьте атрибуты _«Получатель»_ и _«Вложение»_ на форму.
5. Добавьте кнопку _«Отправить письмо»_ на форму.

### Настройка сценария

!!! tip "Сценарий для отправки почты"

    Сценарий для отправки почты можно запускать по любому **[событию][scenario_event]**:

    - нажатие кнопки;
    - создание записи;
    - изменение записи;
    - запуск процесса;
    - получение сообщения;
    - вход токена в элемент диаграммы;
    - выход токена из элемента диаграммы.

1. Создайте сценарий _«Отправка писем»_.
2. В свойствах события «**Нажатие кнопки**» выберите **контекстный шаблон** _«Эл. письма»_ и **кнопку** _«Отправить письмо»_.
3. Создайте действие «**Изменить значения переменных**» со следующими свойствами:

    - **Операция со значениями переменных: заменить**
    - **Набор переменных:** _mail_

4. В свойствах действия «**Изменить значения переменных**» настройте перечисленные ниже переменные.

    !!! warning "Сопоставление переменных-объектов с атрибутами сообщения"

        Имена переменных, значения которых передаются в [**атрибуты сообщения**](#атрибуты-сообщения) с помощью действия сценария «**Отправить сообщение**», должны совпадать с системными именами атрибутов сообщения.

        Для передачи значения переменной в атрибут сообщения типа «**Объект**», необходимо создать переменную с такой же структурой, как у атрибута сообщения, добавив дочерние переменные:

        - Создайте переменную, оставив её значение пустым.
        - Установите флажок у имени родительской переменной в списке и нажмите кнопку «**Создать**».
        - Дважды нажмите значок <i class="fa-light fa-angle-down anchor"></i> рядом с родительской переменной.
        - В таблице отобразится дочерняя переменная.

    - _To_ — с дочерними переменными:

        - _Address_ — **значение: формула**

        ``` cs
        $Poluchatel->mbox
        ```

        - _Name_ — **значение: формула**

         ``` cs
         $Poluchatel->fullName
         ```

    - _FullName_ — **значение: формула**

        ``` cs
        $Poluchatel->fullName
        ```

    - _Filename_  — **значение: N3**

        ``` turtle
        # Импортируем функции для работы с записями и документами
        @prefix object: <http://comindware.com/ontology/object#>.
        @prefix document: <http://comindware.com/ontology/document#>.

        {
            # Находим атрибут Vlozhenie  (Вложение) в шаблоне Elpisma (Эл. письма).
            ("Elpisma" "Vlozhenie") object:findProperty ?VlozhenieAttribute.
            # Присваиваем переменной ?Vlozhenie объект из атрибута «Вложение».
            ?item ?VlozhenieAttribute ?Vlozhenie.
            # В переменную ?currentDocument помещаем
            # последнюю добавленную версию документа.
            ?Vlozhenie document:currentRevision ?currentDocument.
            # Возвращаем имя текущего файла.
            ?currentDocument document:name ?value.
        }
        ```

    - _Attachments_ — с дочерними переменными:

        - _Name_ — **значение: N3**

         ``` turtle
         # Импортируем функции для работы с записями и документами
         @prefix object: <http://comindware.com/ontology/object#>.
         @prefix document: <http://comindware.com/ontology/document#>.

         {
             # Находим атрибут Vlozhenie  (Вложение) в шаблоне Elpisma (Эл. письма).
             ("Elpisma" "Vlozhenie") object:findProperty ?VlozhenieAttribute.
             # Присваиваем переменной ?Vlozhenie объект из атрибута «Вложение».
             ?item ?VlozhenieAttribute ?Vlozhenie.
             # В переменную ?currentDocument помещаем
             # последнюю добавленную версию документа.
             ?Vlozhenie document:currentRevision ?currentDocument.
             # Возвращаем имя текущего файла.
             ?currentDocument document:name ?value.
         }
         ```

        - _Extension_ — **значение: N3**

         ``` turtle
         # Импортируем функции для работы с записями и документами
         @prefix object: <http://comindware.com/ontology/object#>.
         @prefix document: <http://comindware.com/ontology/document#>.

         {
             # Находим атрибут Vlozhenie  (Вложение) в шаблоне Elpisma (Эл. письма).
             ("Elpisma" "Vlozhenie") object:findProperty ?VlozhenieAttribute.
             # Присваиваем переменной ?Vlozhenie объект из атрибута «Вложение».
             ?item ?VlozhenieAttribute ?Vlozhenie.
             # В переменную ?currentDocument помещаем
             # последнюю добавленную версию документа.
             ?Vlozhenie document:currentRevision ?currentDocument.
             # Возвращаем расширение текущего файла.
             ?currentDocument document:revisionExtension ?value.
         }
         ```

        - _Content_ — **значение: N3**

         ``` turtle
         # Импортируем функции для работы с записями и документами
         @prefix object: <http://comindware.com/ontology/object#>.
         @prefix document: <http://comindware.com/ontology/document#>.

         {
             # Находим атрибут Vlozhenie  (Вложение) в шаблоне Elpisma (Эл. письма).
             ("Elpisma" "Vlozhenie") object:findProperty ?VlozhenieAttribute.
             # Присваиваем переменной ?Vlozhenie объект из атрибута «Вложение».
             ?item ?VlozhenieAttribute ?Vlozhenie.
             # В переменную ?currentDocument помещаем
             # последнюю добавленную версию документа.
             ?Vlozhenie document:currentRevision ?currentDocument.
             # Возвращаем содержимое текущего документа.
             ?content document:content ?value.
         }
         ```

5. Добавьте действие «**Отправить сообщение**» со следующими свойствами:

    - **Подключение:** выберите [подключение для отправки эл. почты из сценариев через SMTP или Exchange](#настройка-подключения-к-почтовому-серверу-для-отправки-почты-из-сценария).
    - **Путь передачи данных:** выберите [путь передачи данных эл. почты из сценариев через SMTP или Exchange](#настройка-пути-передачи-данных-для-отправки-эл-почты-из-сценария).
    - **Переменная с сообщением:** _mail_

## Тестирование

1. Создайте запись в шаблоне _«Эл. письма»_.
2. Выберите аккаунт, на эл. почту которого требуется отправить письмо.
3. Загрузите файл в поле _«Вложение»_.
4. Сохраните запись.
5. Нажмите кнопку _«Отправить письмо»_.
6. На эл. почту, выбранного аккаунта, придёт письмо с прикреплённым вложением.

--8<-- "related_topics_heading.md"

**[Получение эл. почты через Exchange. Настройка подключения][exchange_receiving_connection]**

**[Получение эл. почты через IMAP. Настройка подключения][imap_receiving_connection]**

**[Отправка эл. почты из процесса. Настройка подключения][process_sending_connection]**

**[Подключения. Типы, создание, настройка, удаление][connections]**

**[Пути передачи данных. Типы, создание, настройка, удаление][communication_routes]**

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}