---
title: Карты. Настройка подключения
kbId: 2572
---

# Карты. Настройка подключения {: #map_configure}

## Введение

Подключение к картографической службе Яндекс Карты используется для отображения карт на формах и добавления на карты географических меток.

В этой статье представлены инструкции по настройке подключения к картографической службе.

Сведения об использовании карт см. в статье _«[Настройка представления карты на форме]({{ kbArticleURLPrefix }}2531#mcetoc_1hliep4ol3)»._

## Создание подключения

1. Откройте страницу [«**Администрирование**» — «**Подключения**»][администрирование].
2. Создайте **системное подключение** типа «**Карты**» или откройте имеющееся подключение, дважды нажав его в списке.
3. В отобразившемся окне настройте свойства подключения к картографической службе:
    - **Отключить** — установите этот флажок, если требуется деактивировать данное подключение;
    - **Название** — введите наглядное наименование подключения;
    - **Использовать по умолчанию** — установите этот флажок, чтобы это подключение использовалось как основное, если имеется несколько подключений типа «**Карты**».
    - **Ключ API** — введите ключ к службе **JavaScript API and Geocoder HTTP API**, полученный в [кабинете разработчика Яндекс](https://developer.tech.yandex.ru/services).

        !!! warning "Внимание!"

            В кабинете разработчика не следует выбирать ключ к службе **Yandex.Maps Static API**. Необходимо выбрать ключ к службе **JavaScript API and Geocoder HTTP API**.

4. Сохраните подключение.

_![Создание подключения к картографической службе](maps_connection_creation.png)_

_![Свойства подключения к картографической службе](maps_connection_properties.png)_

## Настройка шаблонов записи и формы

2. Создайте шаблон записи _«Данные карт»_ для хранения картографических данных со следующими атрибутами:

   - атрибуты типа «**Текст**»: 

       - _Страна_
       - _Населённый пункт_
       - _Улица_
       - _Дом, строение_
       - _Индекс_

   - атрибуты типа «**Число**»:

       - _Широта_
       - _Долгота_

3. Создайте шаблон записи _«Карты»_.
4. Создайте атрибут _«Данные карты»_:

    - **Тип данных: Запись**
    - **Связанный шаблон:** _Данные карт_
    - **Взаимная связь с атрибутом: с новым**
    - **Атрибут:** _Карта_
    - **Хранить несколько значений:** флажок установлен

5. Добавьте атрибут _«Данные карт»_ и выберите для него представление в виде карты.
6. Выставите высоту карты от 200 до 480 пикселей. По умолчанию высота равна 240 пикселям.
7. Соотнесите атрибуты адреса и атрибуты координат с атрибутами шаблона _«Данные карт»_.
8. Вынесите атрибут _«Данные карт»_ ещё раз и выберите представление в виде таблицы.
9. Добавьте в таблицу _«Данные карт»_ атрибуты, созданные в п. 2.
10. В поле кнопок таблицы _«Данные карт»_ вынесите кнопки «**Создать**» и «**Удалить**».
11. Сохраните форму.

--8<-- "related_topics_heading.md"

**[Настройка представления карты на форме]({{ kbArticleURLPrefix }}2531#mcetoc_1hliep4ol3)**

**[Удаление подключения]({{ kbArticleURLPrefix }}2205#mcetoc_1gjrlqi4l6)**

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}