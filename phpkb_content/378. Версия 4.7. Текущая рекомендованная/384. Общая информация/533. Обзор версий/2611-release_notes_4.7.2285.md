---
title: Сведения о выпуске 4.7.2285
kbId: 2611
---

# Сведения о выпуске 4.7.2285

## Введение

В **{{ productName }}** версии 4.7.2285 от 22.05.2024 реализованы перечисленные ниже новые возможности, улучшения и исправления.

### Ключевые изменения

- Добавлены новые функции для работы с документами, включая управление подписями и предпросмотр.
- Расширены возможности журналирования с добавлением журналов новых типов.
- Оптимизирован пользовательский интерфейс, включая улучшение диаграмм и поддержку мобильных приложений.
- Обновлены инфраструктурные подсистемы, включая версии Apache Ignite и OpenSearch, улучшена интеграция с Kafka и OData.
- Усилен контроль лицензирования, добавлена поддержка именных и конкурентных лицензий.
- Реализованы уведомления о смене пароля и повышена производительность системы.
- Исправлены ошибки в инфраструктурных компонентах, интерфейсе пользователя, работе с документами, внешних подключениях и мобильном приложении.

## Новые возможности и улучшения

### Документы

- **Данные о подписях:** в окне выбора подписи отображаются подробные сведения о каждом сертификате.
- **Подписание нескольких документов:**  реализована возможность подписать несколько документов нажатием одной кнопки.
- **Предпросмотр:** реализован предпросмотр нескольких прикреплённых документов.
- **Удаление подписей:** реализована возможность удаления электронных подписей у документов.
- **Управление документами:** внесены изменения в механизм выбора документов при большом количестве записей. Теперь выбор происходит быстрее и стабильнее.

### Журналирование

- **Журнал событий адаптеров:** добавлен подробный журнал событий обработки сообщений адаптерами, который содержит наглядные и понятные сведения.
- **Журнал статистики транзакций:** добавлен журнал транзакций для улучшенного мониторинга и диагностики работы системы.
- **Сведения о запуске:** реализован вывод подробных сведений о переменных среды и параметрах ПО при запуске экземпляра ПО.

### Интерфейс пользователя

- **Диаграммы и графики:**
    - улучшено отображение фильтров данных на страницах с диаграммами и графиками;
    - усовершенствован конструктор гистограммы.
- **Диалоговое окно:** реализована возможность настройки размера диалоговых окон.
- **Коллекции:** в мобильном приложении реализована поддержка добавления и удаления записей в таблицы и карточки на формах.
- **Редактор выражений:** улучшена работа предиктивного ввода, например отображается подсказка контекста шаблона процесса при настройке ролей.
- **Смена типа атрибута:** добавлены предупреждения о негативных последствиях смены типа атрибута.
- **Список аккаунтов:** добавлены столбцы «**Способ аутентификации**», «**Включён**» и «**В архиве**», удалены неинформативные столбцы.
- **Страницы:** улучшен предпросмотр страницы в конструктор страницы.
- **Таблицы:** реализована возможность закрепления столбцов в таблице.
- **Улучшено отображение:** реестров процессов и оргединиц в панели навигации.
- **Установка точки на карте при поиске:** при поиске на карте отображается место, которое выбрал пользователь, и автоматически проставляется метка с заполненными данными.
- **Хлебные крошки:** улучшена работа навигационной цепочки при переходе по разделам навигации.

### Инфраструктура

- **Apache Ignite:** используемая версия поднята до 2.16.
- **API**: реализован полнотекстовый поиск в методах API для поиска записей (`webapiReferenceDataList`, `webapiReferenceDataGet`).
- **Collabora:** реализован механизм отображения встроенного редактора Collabora на том же языке, что интерфейс **{{ productName }}**.
- **HMAC-аутентификация:** добавлена поддержка авторизации через HMAC.
- **Kerberos**: реализована авторизация через Kerberos.
- **Kafka**:
    - реализована возможность выбора номера обслуживаемой шины данных;
    - улучшено журналирование взаимодействия с Kafka.
- **OData:** улучшена совместимость с системами 1C.
- **OpenSearch:** реализована поддержка использования службы OpenSearch наряду с Elasticsearch.

Экспериментальная функция

Поддержка OpenSearch находится на стадии разработки. См. *«[Поддержка экспериментальных функций][experimental_feature_support]»*.
- **Управление версиями приложений**:

    - реализована возможность импорта одного и того же файла CTF в разные приложения;
    - улучшена работа функций экспорта и импорта приложений вручную и с помощью Git.
- **Эл. почта:** повышена производительность обработки входящих писем.

### Лицензирование

- **Контроль лицензий:** усилен контроль за наличием лицензии у пользователей.
- **Типы лицензий:** реализована поддержка именных и конкурентных лицензий.

### Прочее

- **Атрибут «Цвет»:** реализована возможность изменения значения атрибута с помощью правил для формы.
- **Напоминание о необходимости смене пароля:** реализована рассылка пользователям уведомлений о необходимости смены пароля за срок, указанный в глобальной конфигурации.
- **Повышение производительности:** улучшена общая производительность системы в различных сценариях использования.

## Исправленные ошибки

### Инфраструктура

- **Active Directory:** устранена проблема, не позволявшая использовать скобки в DN объекта в фильтрах синхронизации с AD.
- **Exchange:**
    - устранена проблема, не позволявшая прочитать письма с телом в формате `Content-Type: text/plain`;
    - устранена проблема, вследствие которой не считывались входящие письма с вложенными в текст изображениями.
- **Kerberos:** повышена безопасность авторизации посредством Kerberos.
- **Общие уведомления**: устранена проблема, не позволявшая включить ранее настроенный и отключенный путь передачи данных для общих уведомлений.
- **Резервное копирование:** устранены проблемы с резервным копированием очень больших баз данных.
- **Системные службы:** усовершенствовано управление работой системных служб.
- **Управление адаптерами:** исправлено поведение системы при отсутствии хост-службы управления адаптерами.
- **Эл. почта:** устранена проблема, вследствие которой считывались не все входящие письма.

### Карты

- **Долгота и широта:** исправлен порядок заполнения широты и долготы.
- **Отображение карты с помощью правил для формы:** устранена проблема, вследствие которой при скрытии и отображении области с картой карта отображалась поверх следующей области.
- **Отображение свойств карты:** устранена проблема, вследствие которой для повторного редактирования карты на форме приходилось удалять с формы и заново выносить атрибут для карты на форму.

### Документы

- **Сохранение документов:** исправлена ошибка при сохранении документа с некоторыми параметрами, которая могла приводить к потере данных.
- **Шаблоны экспорта**:
    - исправлено именование экспортируемых файлов.
    - устранена проблема, вследствие которой в экспортированном документе не отображались подписи полей;
    - устранена проблема, вследствие которой при экспорте значений ссылочных атрибутов вместо атрибутов-заголовков записей использовались ID записей.

### Интерфейс пользователя

- **Внешние формы:** исправлен переход к внешним формам в мобильном приложении.
- **Гистограммы:** исправлено отображение столбиков гистограммы в горизонтальной ориентации.
- **Диаграммы процессов:** устранены проблема, приводившая к ошибкам при вложении дорожек.
- **Загрузка изображений:** улучшено отображение индикатора загрузки файла.
- **Значок сайта:** реализована проверка формата загружаемого файла (ранее можно было загрузить файл неподходящего формата).
- **Карты:** при выборе атрибутов во время настройки карты на форме устранена возможность выбора одного и того же атрибута для разных свойств карты.
- **Навигационная панель:** устранена проблема, вследствие которой в поиск в навигационной панели не находил пункты в свёрнутых разделах.
- **Навигация:** исправлено отображение панели навигации для пользователей без доступа к бизнес-приложениям, использующих **Comindware Architect**.
- **Обсуждения:** исправлена работа функции ответа на сообщение, повышена стабильность работы обсуждений.
- **Отображение данных:** устранены проблемы с отображением данных на некоторых страницах, улучшена стабильность интерфейса.
- **Поле типа «Длительность»:**
    - устранена возможность ввода длительности вне заданных пределов;
    - исправлен формат отображения длительности.
- **Правила для формы:** устранена проблема, вследствие которой не срабатывало действие «**Показать ошибку**».
- **Рабочий стол:** устранено зависание системы при наличии на рабочем столе или странице временной шкалы без заполненных дат.
- **Разделы навигации:** устранена проблема, вследствие которой мог не отображаться раздел навигации, используемый по умолчанию, и терялась возможность редактировать разделы навигации.
- **Страницы:** устранена проблема, вследствие которой невозможно было очистить содержимое страницы.
- **Сценарии:** устранены ошибки при создании сценариев, срабатывающий при создании или завершении задачи.
- **Таблицы на формах:** устранена проблема, вследствие которой не отображалась таблица на форме, если в таблицу был вынесен системный атрибут «**Связанные процессы**».
- **Текстовое поле:** устранена возможность ввода текста длиннее заданного лимита.
- **Фильтрация таблиц:** исправлена работа фильтров по пустым значениям числовых атрибутов.

### Мобильное приложение

- **Аутентификация:**

    - при работе нескольких пользователей на одном мобильном устройстве, устранен риск входа под учётными данными другого пользователя;
    - устранена возможность входа в мобильном приложении с использованием аккаунта, который уже удалён.
    - устранена возможность входа в мобильном приложении с использованием пароля после его смены;
    - устранена проблема, вследствие которой не отображалось сообщение о неверно введённом PIN-коде;
    - устранена проблема, вследствие которой отображался запрос на установку PIN-кода, хотя он уже был задан.
- **Безопасность:** устранены выявленные уязвимости мобильного приложения.
- **Сеансы пользователей:** устранены проблемы, вследствие которых:
    - мог не происходить выход и выход из системы;
    - могли не отображаться значения в текстовых полях.
    - не происходил выход из системы по истечении предельной длительности сеанса, если пользователь вошёл с использованием PIN-кода;
    - при переходе по внешней ссылке происходил выход пользователя из системы.
- **Таблицы и карточки:**
    - исправлена работа фильтрации, сортировки и группировки в таблицах и карточках;
    - улучшено отображение заголовков столбцов таблиц.

## Прочее

- **Атрибуты:**

    - скрыты атрибуты типа «**Оргединица**» при назначении исполнителей пользовательских задач;
    - устранена проблема, вследствие которой иногда не удавалось создать атрибут типов «**Документ**», «**Роль**», «**Оргединица**», «**Изображение**»;
    - устранена проблема, вследствие которой не всегда было возможно отредактировать атрибут «**Цвет**» в таблицах.
- **Версионирование:** исправлена работа подсистемы версионирования в **Comindware Architect**.
- **Дизайн страниц входа и регистрации:** устранены ошибки, иногда возникавшие при публикации конфигурации страниц входа и регистрации.
- **Области кнопок:** системные имена областей кнопок теперь нумеруются автоматически во избежание конфликтов.
- **Обновление версии ПО:** устранены проблемы, приводившие к неполадкам при обновлении версии экземпляра ПО.
- **Общие улучшения:** реализованы исправления и улучшения для повышения общей стабильности и производительности системы.
- **Самостоятельная регистрация:** устранены ошибки, вследствие которых иногда пользователю не удавалось самостоятельно создать аккаунт в **{{ productName }}** (кода эта возможность включена).
- **Совместимость:** реализованы исправления и улучшения для улучшения совместимости с различными операционными системами и браузерами.
- **Сценарии:** устранена проблема, вследствие которой сценарии не всегда создавали записи в шаблонах.
- **Установка в Linux:** исправлены недочёты при формировании файла конфигурации в процессе установки ПО.
- **Экспорт регламентов:** реализована возможность экспорта регламентов пользователями без прав администратора.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
