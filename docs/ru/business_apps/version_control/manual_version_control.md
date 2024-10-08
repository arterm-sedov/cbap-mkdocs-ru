---
tags:
  - трансфер
  - трансфер метаданных
  - импорт приложения
  - экспорт приложения
  - ручной трансфер
  - ручное управление версиями
hide:
  - tags
---

# Ручное управление версиями

В **{{ productName }}** предусмотрены импорт и экспорт версий приложения посредством файлов с расширением `CTF`.

!!! Note "Примечание"
      В файле `CTF` по умолчанию сохраняется только конфигурация приложения, записи сохраняются только для шаблонов, у которых установлен флажок «**Переносить данные при трансфере**» на вкладке [«**Свойства**» шаблона записи][свойства-шаблона-записи].

## Переход к ручному управлению версиями

1. В разделе **«[Администрирование][администрирование-приложения]»** приложения выберите пункт «**Управление версиями**».
2. Нажмите заголовок страницы «**Управление версиями через Git**» и в раскрывающемся меню выберите пункт «**Ручное управление версиями**».

    *![Переход к ручному управлению версиями](verstion_control_switch_to_manual.png)*

3. Отобразится раздел «**Ручное управление версиями**» с двумя подразделами:

    * **Экспорт** — настройка аккаунта для подключения к Git и выбор или создание ветви в репозитории для хранения версий приложения.
    * **Импорт** — импорт версии приложения из репозитория Git.

    *![Страница «Ручное управление версиями»](manual_version_control.png)*

## Ручной экспорт версии приложения

1. В подразделе «**Экспорт**» нажмите кнопку «**Экспортировать**».
2. Браузер скачает файл с системным именем приложения и расширением `.CTF` вида: `businessApplicationSystemName.ctf`.

## Ручной импорт версии приложения

1. В подразделе «**Импорт**» загрузите файл  `CTF` с версией приложения.

      * Нажмите кнопку «**Выберите файл**» и в отобразившемся окне выберите файл.

      **ИЛИ**

      * Перетащите из проводника файл на область с кнопкой «**Выберите файл**».

2. Отобразятся сведения об импортируемом приложении и параметры импорта.
3. [Проверьте целостность приложения](#проверка-целостности-импортируемого-приложения), нажав кнопку «**Проверить**».
4. Нажмите кнопку «**Импортировать**».

    *![Настройка импорта приложения из файла CTF](manual_version_import_properties.png)*

### Сведения об импортируемом приложении

* **Название** — наименование приложения.
* **Системное имя** — уникальное имя приложения.
* **Описание** — комментарий относительно назначения приложения.
* **Дата экспорта** — дата, когда приложение было экспортировано в файл CTF.
* **Сервер** — адрес сервера, с которого было экспортировано приложение.
* **Версия** — номер версии экспортированного приложения.

### Параметры импорта
* **Опубликовать диаграммы процессов после импорта** — установите этот флажок, чтобы опубликовать все импортированные диаграммы процессов.
* **Состояния компонентов приложения после импорта** — выберите состояние, в которое следует привести компоненты приложения после импорта.
    -  **Импортировать состояния** — будут активированы и приостановлены компоненты приложения, которые были активны и приостановлены в импортируемой версии.
    -  **Оставить текущие состояния** — останутся активны те компоненты, которые активны в текущей версии приложения.
    -  **Активировать все компоненты** — будут активированы все компоненты приложения.
    -  **Приостановить все компоненты** — будут приостановлены все компоненты приложения.

!!! Question "Определение"
      Компоненты приложения — это задачи и элементы бизнес-процессов, интеграции, подключения и прочие сервисы приложения. Список и состояния компонентов приложения отображаются на странице «**Активность компонентов**».

### Проверка целостности импортируемого приложения

1. Чтобы проверить данные в импортируемом файле `CTF` на предмет целостности и непротиворечивости, нажмите кнопку «**Проверить**» в подразделе «**Импорт**».
2. Отобразится окно с результатом проверки:

    *![Результат проверки без ошибок](manual_version_import_check_no_errors.png)*

    *![Результат проверки с ошибками](manual_version_import_check_errors.png)*

3. При необходимости нажмите кнопку «**Скачать результат проверки**».
4. Браузер скачает текстовый файл в формате JSON с именем «`import validation.log`».

--8<-- "related_topics_heading.md"

**[Управление версиями приложения][управление-версиями-приложения]**

**[Управление версиями через Git](git_version_control.md)**
