---
title: Настройка конфигурации Утилиты администрирования Comindware
kbId: 4638
---

# Настройка конфигурации Утилиты администрирования Comindware {: #admin_utility_configure}

## Переход к окну «Конфигурация утилиты администрирования»

Окно «**Конфигурация утилиты администрирования**» позволяет выполнить следующие операции:

- просмотреть статус компонентов {{ productName }} и установить недостающие компоненты;
- настроить службу ISS для новых экземпляров продукта;
- настроить пути для новых версий и экземпляров продукта;
- настроить пути для диагностических журналов и просмотреть их;
- провести диагностику экземпляров продукта.

1. Запустите приложение *Comindware Administration Tool*.

![Ярлык Утилиты администрирования](https://kb.comindware.ru/assets/img_667a7d67b3735.png)

Ярлык Утилиты администрирования
2. Если отобразится окно контроля учётных записей, нажмите кнопку «**Да**».

![Окно контроля учётных записей](https://kb.comindware.ru/assets/img_667eab00ba55e.png)

Окно контроля учётных записей
3. Отобразится главное окно Утилиты администрирования.
4. Нажмите кнопку  ![](https://kb.comindware.ru/assets/img_667a7e419e390.png)  в правом верхнем углу окна Утилиты администрирования.

![Переход к настройке конфигурации Утилиты администрирования](https://kb.comindware.ru/assets/img_667ab2b1abb84.png)

Переход к настройке конфигурации Утилиты администрирования
5. Отобразится окно «**Конфигурация утилиты администрирования**».
6. Настройте параметры на следующих вкладках:

    - [**Общее**](#просмотр-статуса-и-установка-компонентов-продукта)
    - [**IIS**](#настройка-службы-iis)
    - [**Пути**](#настройка-путей)
    - [**Диагностика**](#диагностика-утилиты-администрирования)
7. Сохраните конфигурацию.

## Просмотр статуса и установка компонентов продукта

1. Откройте вкладку «**Общее**» в окне «**Конфигурация утилиты администрирования**».
2. В таблице «**Статус компонентов продукта**» отобразится перечень стороннего ПО, необходимого для работы **{{ productName }}**.
    - Если ПО установлено, для него отображается флажок в первом столбце таблицы.
    - Если ПО работает должным образом, для него отображается зелёный флажок в столбце «**Статус**». В противном случае отображается красный значок ошибки.
3. Чтобы установить недостающее ПО, поставьте для него флажок в первом столбце таблицы и нажмите кнопку «**Сохранить**».
    - Выбранное ПО будет автоматически установлено в фоновом режиме.
    - При установке могут отображаться окна `powershell.exe`. Не закрывайте их и дождитесь завершения установки.
4. Сохраните конфигурацию.

![Просмотр статуса и установка компонентов продукта](https://kb.comindware.ru/assets/img_667eab23c9752.png)

Просмотр статуса и установка компонентов продукта

## Настройка службы IIS

1. Откройте вкладку «**IIS**» в окне «**Конфигурация утилиты администрирования**».
2. Настройте параметры веб-сайта, которые будут использоваться по умолчанию для новых экземпляров продукта:
    - **Доменное имя**
    - **Порт**
    - **Включить запись журналов IIS**

При создании экземпляра продукта эти параметры можно будет изменить.
3. Откройте вкладку «**IIS**» в окне «**Конфигурация утилиты администрирования**».
4. Сохраните конфигурацию.

 

![Настройка службы IIS для новых экземпляров продукта](https://kb.comindware.ru/assets/img_667eab3d65c29.png)

Настройка службы IIS для новых экземпляров продукта

## Настройка путей
{{ productName }}
1. Откройте вкладку «**Пути**» в окне «**Конфигурация утилиты администрирования**».
2. В поле «**Новые версии продукта**» укажите папку для установки новых версий продукта **{{ productName }}**.
3. Настройте используемые по умолчанию пути для новых экземпляров продукта:
    - **Экземпляры продукта** — укажите папку для установки новых экземпляров.
    - **Резервные копии** — если это поле оставить пустым, будет использоваться папка `Backup` внутри папки экземпляра продукта.
    - **Журнал системы** — если это поле оставить пустым, будет использоваться папка Logs внутри папки экземпляра продукта.
    - **Загруженные файлы** — если это поле оставить пустым, будет использоваться папка Streams внутри папки экземпляра продукта.
    - **Сервер Elasticsearch** — укажите адрес сервера Elasticsearch.

Указанные пути можно изменить при установке новых версий продукта и создании экземпляров продукта. См. статью *«[Настройка конфигурации и просмотр фактических путей к папкам экземпляра продукта][admin_utility_instance_configure]»*.
4. Сохраните конфигурацию.

![Настройка путей для новых версий и экземпляров продукта](https://kb.comindware.ru/assets/img_667eab5632a66.png)

Настройка путей для новых версий и экземпляров продукта

## Диагностика утилиты администрирования

На вкладке «**Диагностика**» можно настроить пути к различным журналам и провести диагностику экземпляров продукта.

1. В поле «Журнал утилиты администрирования» укажите папку для хранения журнала работы Утилиты администрирования.
2. Чтобы просмотреть этот журнал утилиты администрирования, нажмите кнопку «**Открыть журнал**».

![Журнал утилиты администрирования](https://kb.comindware.ru/assets/img_667aaab71953f.png)

Пример журнала утилиты администрирования
3. В поле «**Результаты диагностики**» укажите папку для хранения журналов диагностики экземпляров продукта.
4. Чтобы открыть папку с файлами журналов диагностики, нажмите кнопку «**Открыть результаты**».


![Папка с результатами диагностики](https://kb.comindware.ru/assets/img_667aaa95e002d.png)

Пример папки с результатами диагностики
5. Нажмите кнопку «**Диагностика**», чтобы провести диагностику экземпляра продукта. См. статью «[Диагностика экземпляра продукта][admin_utility_instance_diagnose]».
6. Сохраните конфигурацию.

![Настройка путей для диагностических журналов Утилиты администрирования](https://kb.comindware.ru/assets/img_667eabfa31eac.png)

Настройка путей для диагностических журналов Утилиты администрирования

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Настройка конфигурации и просмотр фактических путей к папкам экземпляра продукта][admin_utility_instance_configure]_
- _[Диагностика экземпляра продукта][admin_utility_instance_diagnose]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}