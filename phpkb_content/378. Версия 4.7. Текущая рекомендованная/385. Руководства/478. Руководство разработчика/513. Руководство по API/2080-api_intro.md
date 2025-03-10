---
title: Введение в API
kbId: 2080
---

# Введение в API

## Введение

**{{ productName }}** может обращаться к API внешних систем через [подключения](https://kb.comindware.ru/category.php?id=437) и [пути передачи данных](https://kb.comindware.ru/category.php?id=515), а также может обрабатывать запросы из внешних систем через интерфейсы **REST API** трех типов:

- [**Solution API**](https://kb.comindware.ru/article.php?id=2073)
- [**System Core API**](https://kb.comindware.ru/article.php?id=2150)
- [**Web API**][api_web]

### Определения

- **API** (Application Programming Interface) — это интерфейс прикладного программирования — набор методов, классов, библиотек и функций, обеспечивающих возможность взаимодействия между системами.
- **REST API** — это API, соответствующий архитектуре Representational State Transfer (передача репрезентативного состояния). Преимуществами REST API являются возможность оптимального использования протокола HTTP, масштабирования сервисов и разработки приложений с использованием практически любых языков программирования с соблюдением принципов проектирования REST:
    - отсутствие сохранения состояния на сервере — каждый поступающий запрос содержит все необходимые для обработки данные и обрабатывается независимо от других запросов;
    - единообразный интерфейс — сервер передаёт информацию в стандартном формате;
    - независимость клиента и сервера — клиент может взаимодействовать с сервером только посредством URI ресурса, а сервер может лишь передавать на клиент запрошенные данные посредством HTTP;
    - возможность кэширования ресурсов — ответы содержат данные о кэшируемости, запрашиваемые многократно ресурсы могут кэшироваться на стороне сервера или клиента;
    - многоуровневая архитектура системы — клиент может подключаться к авторизованным посредникам между клиентом и сервером, чтобы получать ответы от сервера, а сервер может передавать запросы другим серверам;
    - код по запросу — сервер может расширить возможности клиента, передав исполняемый код, например, для проверки введённых пользователем данных.
- **RESTful** — это веб-служба, реализующая архитектуру **REST**.
- **Ресурс** — это объект или информация в приложении, например шаблон, аккаунт или документ, доступ к которым предоставляет API.
- **URI ресурса** — это универсальный идентификатор ресурса в API.
- **Клиент** — это человек или система, которые осуществляют доступ к ресурсам посредством API.

## Доступ к API

В простейшем случае **RESTful**-службы отправляют и получают HTTP-запросы в строке URL-адреса для получения и отправки данных, запуска команд и выполнения других действий.

Все интеграции с помощью **REST API** настраиваются по одному принципу:

- составьте сценарий интеграции — какая система инициирует вызов API, как часто, какие методы она использует для передачи каких данных, что потом происходит и т. д.;
- используйте документацию по API для тестирования запросов, настройки подключения и формирования финальных «рабочих» запросов.

### Методы API

**{{ productName }}** поддерживает следующие методы API.

- `GET` — получить список всех записей.
- `GET {id}` — получить данные о записи с идентификатором `{id}`.
- `DELETE {id}` — удалить запись с идентификатором `{id}`.
- `POST` — создать новую запись.
- `PUT {id}` — изменить данные о записи с идентификатором `{id}`.

### Инициация запроса из внешней системы

**{{ productName }}** может принимать HTTP-запросы к **API** двумя способами:

- Запрос `GET` или `DELETE` в виде URL-строки, содержащей все параметры запроса.
    - Внешняя система отправляет запрос в строке URL. Заготовку запроса для внешней системы можно сформировать в интерфейсе [Swagger](#mcetoc_1h7csahj80).
    - Такой запрос можно проверить с помощью браузера: скопируйте полученный **Request URL** в адресную строку и нажмите клавишу `Enter`. Если вы уже вошли в систему в этом браузере, аутентификация не потребуется.
- Запрос `POST` или `PUT` с телом, содержащим все параметры (например, имя пользователя и пароль, данные, которые необходимо отправить или получить и т. д.).
    - Внешняя система отправляет запрос в формате JSON или XML. Заготовку запроса для внешней системы можно сформировать в интерфейсе [Swagger](#mcetoc_1h7csahj80).
    - Этот вариант является более гибким, позволяя передать гораздо больше данных в структурированном виде. Но такой запрос нельзя протестировать с помощью браузера. Для тестирования можно использовать встроенный веб-интерфейс Swagger или такие службы, как Postman, SoapUI, Insomnia и т. п.
- **{{ productName }}** возвращает ответ формате JSON или XML.

### Аутентификация внешних систем при доступе к API

API **{{ productName }}** поддерживает два способа аутентификации внешних систем:

- Basic-аутентификация — требуется передать имя пользователя и пароль аккаунта, от имени которого будет выполняться запрос;
- HMAC —  требуется передать токен и секретный ключ, сформированные для аккаунта на странице «**Администрирование**» – «**Ключи аутентификации**».

Примечание

- Для использования методов API и интерфейса [Swagger](#mcetoc_1h7csahj80) следует создать специальный аккаунт и предоставить предоставить ему разрешение «**Вызов API**» в системной роли. См. *«`Системные роли. Определения, настройка, объединение, удаление {Article-ID:2175}`»*. Кроме того, API и Swagger могут использовать пользователи, входящие в системную роль «**Системные администраторы**».
- При вызове методов API в интерфейсе [Swagger](#mcetoc_1h7csahj80) на странице `https://your-host/docs` уже выполнен вход в **{{ productName }}**, и дополнительная аутентификация не требуется.
- При вызове методов API из внешней системы в запросы необходимо добавлять заголовки для аутентификации с использованием аккаунта, которому предоставлен доступ к API.
- Большинство внешних систем обладают интерфейсом настройки метода аутентификации, при отсутствии такового добавьте в `Header` запроса параметр `Authorization`, содержащий зашифрованные в формате `Base64` имя пользователь и пароль.

### Инициация запроса к внешней системе

**REST API** широко применяется в современных системах, и зачастую найти документацию по использованию API конкретной системы можно, введя в поисковой системе запрос вида *«<название системы> REST API»*.

В **{{ productName }}**поддерживает перечисленные ниже способы обращения к API внешних систем:

- Запрос отправляет скрипт на C# (вызываемый [кнопкой][buttons] или [задачей выполнения сценария](https://kb.comindware.ru/article.php?id=22388) в процессе). Скрипт устанавливает подключение к внешней системе, формирует запрос, отправляет его и получает ответ.
- Запрос формирует и отправляет [сценарий](https://kb.comindware.ru/article.php?id=2153) посредством настроенного подключения к внешней системе. Сценарий позволяет сформировать тело запроса, проанализировать полученный ответ и поместить из него данные в атрибуты записей.
- Запрос формирует и отправляет [промежуточное][process_diagram_elements_send_message_intermediate_event] или [конечное событие][process_diagram_elements_send_message_end_event] отправки сообщения в процессе.

Примечание

Для отправки запросов с помощью сценариев и событий процесса требуется настроить [подключение][connections] к внешней службе и [путь передачи данных][communication_routes]. 

### Аутентификация при доступе к API внешних систем

При доступе из к внешним API используйте метод аутентификации, который поддерживает внешняя система. Обратитесь документации API этой системы, чтобы узнать, следует ли указывать имя пользователя b пароль в URL-адресе или теле запроса, или необходимо сгенерировать и использовать токен безопасности вместо передачи пароля в виде обычного текста.

## Использование Swagger

**{{ productName }}** предоставляет встроенный веб-интерфейс API на основе Swagger.

- Swagger предоставляет подробную справку по методам API, включая описания запросов и ответов, а также модели данных с примерами значений.
- Swagger позволяет выполнять запросы и просматривать ответы.
- При выполнении запроса Swagger формирует URI ресурса API для использования во внешних системах, включая синтаксис тела запроса.

1. Чтобы перейти к странице Swagger, введите в адресной строке браузера строку `https://your-host/docs`, где `your-host` — доменное имя вашего сервера.
2. Отобразится страница **{{ productName }} API** со следующими разделами:
    - **RESTful Web API** — общие методы для всех версий ПО (см. [Методы Web API][api_web]);
    - **System Core API** — системные методы, которые могут отличаться для разных версий ПО (см. [Методы System Core API](https://kb.comindware.ru/article.php?id=2150));
    - **Solution API** — методы для шаблонов бизнес-приложений (см. [Методы Solution API](https://kb.comindware.ru/article.php?id=2073)).
3. Перейдите на страницу требуемого API.
4. Раскройте требуемый метод API в списке.
5. Выберите формат запроса и ответа в поле **Response Content Type**.
6. Запустите любой из доступных методов, нажав кнопку **Try it out**.
7. Отобразится заготовка запроса:
    - **Request URL** — скопируйте эту строку во внешнюю систему в качестве URI запроса, для запросов `GET` и `DELETE` она содержит весь запрос;
    - **Example Value** — скопируйте эту строку во внешнюю систему в качестве тела запроса.

_![Страница Swagger UI с разделами API {{ productName }}](https://kb.comindware.ru/assets/img_661d06c21de49.png)_

## Пример вызова метода System Core API

Для создания шаблона записи с помощью System Core API отправьте следующий `POST`-запрос на адрес **Request URL**, указанный в Swagger:

```
http://your-host/api/public/system/TeamNetwork/ObjectAppService/Create
```

- Вместо `your-host` укажите адрес экземпляра **{{ productName }}**.
- В теле запроса (`body`) укажите системное имя шаблона записи (например, `"Car"`).
- В ответ на запрос **{{ productName }}**вернёт ID созданного шаблона записи (например, `"oa.1"`).

--8<-- "related_topics_heading.md"

**[Методы Solution API](https://kb.comindware.ru/article.php?id=2073)**

**[Методы System Core API](https://kb.comindware.ru/article.php?id=2150)**

**[Методы Web API][api_web]**



{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
