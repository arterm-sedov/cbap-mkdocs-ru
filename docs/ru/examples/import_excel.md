---
title: Импорт данных в Excel
kbId: 5310
tags:
    - API
    - атрибуты
    - импорт
    - кнопки
    - пример
hide: tags
---

# Импорт данных в Excel {: #import_excel }

Для использования данных **{{ productName }}**, например, в Excel (Power Query) или BI-системах, существует возможность их выгрузки через API.

## Получение URL запроса {: #import_excel_request_url }

Для просмотра перечня справочников перейдите в область API, введя после доменного имени системы `/docs`, затем перейдите в раздел **Solution API**. Найдите нужный справочник по системному имени, нажмите на него и выберите метод `GET` (без `{id}`) для получения всех данных шаблона записи. Нажмите кнопку «**Try it out**». Скопируйте значение в поле **Request URL**.

Пример: `https://yourinstance/api/public/solution/Languages`

_![Пример запроса в API](https://kb.comindware.ru/assets/bi_excel_0.jpg)_

!!! note "Примечание"

    Формат предоставления данных — JSON.

## Порядок импорта в Excel {: #import_excel_setup }

1. Выберите закладку **Power Query** → «**Из Интернета**» и в адресе запроса укажите ссылку, скопированную из **Request URL**.

    Надстройка Power Query встроена в Excel 2016 и выше. Для более ранних версий Excel требуется [установка][ms_power_query].

    _![Пример запроса в Excel](https://kb.comindware.ru/assets/bi_excel_2.jpg)_

2. В окне «**Доступ к веб-содержимому**» выберите вариант «**Базовый**» и введите логин и пароль пользователя, который имеет доступ к данному шаблону записи. Нажмите кнопку «**Подключение**».

    _![Окно «Доступ к веб-содержимому»](https://kb.comindware.ru/assets/bi_excel_3.jpg)_

3. В открывшемся окне отобразятся полученные данные.

    _![Окно редактора Power Query](https://kb.comindware.ru/assets/bi_excel_4.jpg)_

4. Нажмите кнопку «**В таблицу**», а затем «**ОК**».

    _![Настройка таблицы](https://kb.comindware.ru/assets/bi_excel_5.jpg)_

5. Разверните список всех атрибутов данного шаблона записи и выберите необходимые для отображения в таблице.

    _![Настройка столбцов таблицы](https://kb.comindware.ru/assets/bi_excel_6.jpg)_

6. Нажмите кнопку «**Закрыть и загрузить**» для отображения данных в стандартном интерфейсе Excel.

    _![Перенос настройки таблицы в интерфейс Excel](https://kb.comindware.ru/assets/bi_excel_7.jpg)_

Пример полученной таблицы Excel:

_![Пример полученной таблицы Excel](https://kb.comindware.ru/assets/bi_excel_8.jpg)_

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Solution API][api_solution]
- [Шаблоны записей][record_templates]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
