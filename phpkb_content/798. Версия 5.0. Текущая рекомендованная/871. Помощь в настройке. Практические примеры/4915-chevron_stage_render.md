---
title: Шевроны. Визуализация этапов процесса. Пример настройки
kbId: 4915
---

# Шевроны. Визуализация этапов процесса. Пример настройки

## Введение

В **{{ productName }}** можно настроить визуальное отображение этапов процесса с помощью шевронов.

В этой статье представлен пример настройки приложения для отображения прогресса открытия магазина в виде цветных шевронов пройденных этапов.

Определения

- **Шевроны** — это представление атрибута типа «**Запись**», хранящего несколько значений, в виде последовательности цветных плашек с заголовками записей связанного шаблона.
- Каждый шеврон содержит заголовок связанной с ним записи в виде гиперссылки на запись.
- Конечный пользователь может нажимать шевроны для просмотра связанных с ними записей во всплывающем окне.
- Цвет шеврона можно задать двумя способами:
  - с помощью системного атрибута «**Цвет**» связанной записи;
  - с помощью **правил окраски** шевронов.
- Подробные сведения о настройке шевронов см. в параграфе *«[Динамические элементы формы. Настройка шевронов][form_dynamic_elements]»*.

_![Пример отображения шевронов](https://kb.comindware.ru/assets/img_6606b8aa257d2.png)_

## Прикладная задача

Имеется процесс открытия магазина, состоящий из семи этапов.

Требуется настроить на форме магазина отображение прогресса пройденных этапов открытия в виде цветных шевронов.

Цвет шевронов должен зависеть от статуса прохождения этапа:

- этап пройден с задержкой — красный;
- этап пройден вовремя — зелёный;
- этап начат — оранжевый;
- этап не начат — серый.

Логика работы приложения

- Для реализации прикладной задачи мы создадим следующие сущности (см. «[Исходные данные](#mcetoc_1hp0o4fhl2)»):
  - шаблон записи *«Магазины»*, в котором будут храниться сведения о магазинах;
  - справочник этапов открытия магазинов — шаблон записи, который будет хранить записи с названиями и номерами этапов;
  - шаблон записи *«Этапы»*, в котором будут храниться данные о прогрессе открытия каждого магазина:
    - при запуске процесса *«Открытие магазина»*магазина стандартный набор этапов открытия магазина заполняется автоматически с помощью процесса *«Копирование этапов из справочника»*;
    - этапы открытия конкретного магазина можно переименовать, добавить или удалить.
  - шаблон процесса *«Копирование этапов из справочника»*, который будет создавать запись в шаблоне *«Этапы»* и копировать в неё название и номер этапа из справочника этапов;
  - шаблон процесса *«Открытие магазина»*, который будет вызывать процесс *«Копирование этапов из справочника»* для каждого этапа из справочника, чтобы скопировать названия и номера этапов в список этапов открытия конкретного магазина*.* Кроме того, в каждый этап открытия магазина процесс поместит ссылку на соответствующий этап в справочнике.
- На форме *«Прогресс открытия магазина»* в шаблоне *«Магазины»* мы разместим шевроны, связанные с шаблоном записи *«Этапы»*.
- Пользователь может указать прогресс выполнения каждого этапа с помощью формы *«Прогресс открытия магазина»*.
- Шевроны на форме *«Прогресс открытия магазина»* будут окрашиваться в соответствии с прогрессом выполнения соответствующих этапов.

## Исходные данные

Создайте приложение *«Управление магазинами»* и настройте перечисленные ниже шаблоны.

### Справочник этапов

1. Создайте **шаблон записи** *«Справочник этапов»* с **системным именем** `Spravochniketapov`.
2. Создайте следующие атрибуты в этом шаблоне:

   | Название атрибута | Свойства |
   | --- | --- |
   | *Название этапа* | **Тип данных: текст**  **Формат отображения:** **обычный текст**  **Использовать как заголовок записей:** флажок установлен |
   | *Номер этапа* | **Тип данных: число**  **Количество знаков после запятой: 0** |
3. В шаблоне создайте записи со следующими данными:

   | Название этапа | Номер этапа |
   | --- | --- |
   | *Оценка* | *1* |
   | *ИК 1* | *2* |
   | *ИК 2* | *3* |
   | *Договор* | *4* |
   | *УФРС* | *5* |
   | *Предв. подготов. к откр.* | *6* |
   | *АПП* | *7* |

### Шаблон записи «Этапы»

В этом вспомогательном шаблоне будут хранится скопированные из [*Справочника этапов*](#mcetoc_1hp157j4m3) данные об этапах для каждой записи в шаблоне *«[Магазины](#mcetoc_1hq4eo04a3)»*.

1. Создайте **шаблон записи** *«Этапы»*.
2. Создайте в шаблоне *«Этапы»*следующие атрибуты:

   | Название атрибута | Свойства |
   | --- | --- |
   | *Название этапа* | **Тип данных: текст**  **Формат отображения:** **обычный текст**  **Использовать как заголовок записей:** флажок установлен |
   | *Номер этапа* | **Тип данных: число**  **Количество знаков после запятой: 0** |
   | *Этап начат* | **Тип данных: логический**  **Системное имя:** `Etapnachat` |
   | *Этап пройден* | **Тип данных: логический**  **Системное имя:** `Etapproyden` |
   | *Этап пройден вовремя* | **Тип данных: логический**  **Системное имя:** `Etapproydenvovremya` |
   | *Этап из справочника* | **Тип данных: запись**  **Формат отображения:** **гиперссылка**  **Связанный шаблон:***Справочник этапов*  **Хранить несколько значений:** флажок снят  **Взаимная связь с атрибутом:**  **не используется** |

### Шаблон процесса «Копирование этапов из справочника»

Этот вспомогательный шаблон будет служить для передачи данных из шаблона *«[Этапы](#mcetoc_1hq4e4r7d0)»* в процесс *«[Открытие магазина](#mcetoc_1hq4erth25)».*

1. Создайте **шаблон процесса** со следующими свойствами:
   - **Название:***Копирование этапов из справочника*
   - **Связь с шаблоном записи**: **с имеющимся**
   - **Связанный шаблон:***Этапы*
2. Откройте вкладку «**Диаграмма**»
3. Постройте простой процесс, состоящий из двух элементов: **начального события** и **конечного события**.
4. В меню элемента начального события выберите пункт «**Сценарий на выходе**».

   ![Создание сценария на выходе из начального события процесса «Копирование этапов из справочника»](https://kb.comindware.ru/assets/img_65f469f19c250.png)

   Создание сценария на выходе из начального события процесса «Копирование этапов из справочника»
5. Отобразится конструктор сценария.
6. Внутри действия «**Сменить контекст**» добавьте действие «**Изменить значения атрибутов**». См. *«[Сценарии. Создание вложенных действий](https://kb.comindware.ru/article.php?id=2153)».*
7. В  свойствах действия «**Изменить значения атрибутов**» настройте таблицу изменения значений атрибутов следующим образом:

   | Атрибут | Операция со значениями | Значение |
   | --- | --- | --- |
   | *Название этапа* | **Заменить** | *Этапы → Название этапа* |
   | *Номер этапа* | **Заменить** | *Этапы → Номер этапа* |
8. Должен получиться сценарий, показанный на следующей иллюстрации:

   ![Сценарий для изменения значений атрибутов на выходе из начального события процесса «Копирование этапов из справочника»](https://kb.comindware.ru/assets/img_65f46a2d2135e.png)

   Сценарий для изменения значений атрибутов на выходе из начального события процесса «Копирование этапов из справочника»
9. Чтобы вернуться из конструктора сценария к конструктору диаграммы процесса, нажмите кнопку «**Назад**» в браузере.
10. Проверьте и опубликуйте диаграмму процесса *«Копирование этапов из справочника».*

### Шаблон записи «Магазины»

1. Создайте **шаблон записи** *«Магазины».*
2. Создайте в шаблоне *«**Магазины» следующие*атрибуты:

   | Название атрибута | Свойства |
   | --- | --- |
   | *Название магазина* | **Тип данных: текст**  **Формат отображения:** **обычный текст** |
   | **Этапы открытия магазина** | **Тип данных: запись**  **Формат отображения:** **гиперссылка**  **Связанный шаблон:***Этапы*  **Хранить несколько значений:** флажок установлен  **Взаимная связь с атрибутом:**  **с новым**  **Свойства нового атрибута:**  - **Название**: *Магазин* - **Хранить несколько значений******:****  флажок снят |

### Шаблон процесса «Открытие магазина»

1. Создайте **шаблон процесса** со следующими свойствами:
   - **Название:***Открытие магазина*
   - **Связь с шаблоном записи**: **Связать с существующим**
   - **Связанный шаблон:***Магазины*

## Настройка шаблона процесса «Открытие магазина»

Мы настроили заполнение данных по этапам, и теперь необходимо настроить вызов нашего процесса копирования

1. Откройте шаблон процесса *«Открытие магазина*».
2. Откройте вкладку «**Диаграмма**».
3. Перетащите на диаграмму элемент «**Вызов процесса**» (рекомендуется сразу после начального события).
4. В меню элемента выберите пункт «**Свойства**» *‌*.
5. Отобразится окно «**Свойства вызова процесса**»
6. На вкладке «**Основные**» настройте параметры следующим образом:
   - **Экспертные настройки:** установите флажок
   - **Шаблон для выборки объектов:** *Справочник этапов*
   - **Выражение для выборки объектов:** `from a in db->Spravochniketapov select a->id` (выражение вернёт **ID** записей в [справочнике этапов](#mcetoc_1hp157j4m3), по количеству которых будет запущен подпроцесс)
   - **Режим выполнения**: **параллельный**
   - **Связь шаблона записи с процессом:** **через атрибут**
   - **Шаблон процесса:** *Копирование этапов из справочника*
   - **Записи, связанные с процессом: создавать новые**
   - **Атрибут связи:** *Этапы открытия магазина → Этап из справочника* (в этот атрибут будет записываться **ID** [этапа из справочника](спра), возвращённый **выражением для выборки объектов**, для каждой созданной записи в шаблоне *«[Этапы](#mcetoc_1hq4e4r7d0)»)*.

   ![Настройка вызова процесса «Копирование этапов из справочника»](https://kb.comindware.ru/assets/img_660a6ed14aa42.png)

   Настройка вызова процесса «Копирование этапов из справочника»
7. Выберите вкладку «**Данные на входе**».
8. Нажмите на кнопку «**Добавить**» и настройте сопоставление атрибутов подпроцесса и текущего процесса:
   - **Атрибут шаблона записи подпроцесса:** *Магазин*
   - **Значение:** *ID*

   В результате каждая запись, созданная процессом *«Копирование этапов из справочника»* будет связана с записью в шаблоне *«[Магазин](#mcetoc_1hq4eo04a3)»*, и благодаря взаимной связи в атрибуте *«Этапы открытия магазина»*   будет записан набор идентификаторов записей из шаблона «[*Этапы*](#mcetoc_1hq4e4r7d0)».
9. Сохраните свойства элемента «**Вызов процесса**».
10. Проверьте и опубликуйте диаграмму процесса.

## Настройка шевронов на форме «Прогресс открытия магазина»

1. Откройте шаблон *«[Магазины](#mcetoc_1hq4eo04a3)»*.
2. Выберите вкладку «**Формы**».
3. Откройте основную форму шаблона.
4. Присвойте области на форме название *«Прогресс открытия магазина».*
5. Перетащите атрибут «*Этапы открытия магазина*» в область *«Прогресс открытия магазина».*
6. На панели «**Свойства поля**» выберите **представление** «**Шевроны**».
7. Настройте свойства шевронов:
   - **Упорядочивание:** *Номер этапа*
   - **Правила окраски записей:** нажимайте **«Создать»**  и настройте следующие правила:

     | Цвет | Условие: формула |
     | --- | --- |
     | Зелёный   #31ff00 | ``` AND($Etapnachat, $Etapproydenvovremya) ``` |
     | Красный  #ff0000 | ``` NOT($Etapproydenvovremya) ``` |
     | Серый  #c0c0c0 | ``` NOT($Etapnachat)AND($Etapnachat, $Etapproydenvovremya) ``` |
     | Оранжевый  #ff9800 | ``` AND($Etapnachat, NOT($Etapproyden)) ``` |

     Примечание

     - Если для одной записи одновременно сработают несколько правил, возвращающих разные цвета, то шеврон будет окрашен в цвет, заданный последним сработавшим правилом.
     - Правил окраски шевронов может быть неограниченное количество, но для оптимальной работы платформы рекомендуется задавать не более 8 условий.
     - Следует помнить, что условие окрашивания шеврона вычисляется в контексте шаблона, связанного с текущим шаблоном посредством с атрибута типа «**Запись**». Поэтому обратиться к атрибутам текущего шаблона, на форме которого размещены шевроны, можно только посредством обратной ссылки. Например, к атрибуту *«Название магазина»* можно обратиться посредством атрибута *«Магазин»* из шаблона *«[Этапы](#mcetoc_1hq4e4r7d0)»:* `$Magazin->Nazvaniemagazina`.
8. Снова перетащите атрибут «*Этапы открытия магазина*» в область *«Прогресс открытия магазина».*
9. На панели «**Свойства поля**» выберите **представление** «**Таблица**».
10. В поле «**Сортировка**» на панели «**Свойства таблицы**» выберите атрибут *«Номер этапа»*.
11. Вынесите в таблицу «*Этапы открытия магазина*» следующие атрибуты шаблона  *«[Этапы](#mcetoc_1hq4e4r7d0)»*  в качестве столбцов:
    - *Магазин*
    - *Номер этапа*
    - *Название этапа*
    - *Этап начат*
    - *Этап пройден*
    - *Этап вовремя*
12. Сохраните форму.

_![Настроенная форма «Прогресс открытия магазина»](https://kb.comindware.ru/assets/img_6606b0a3e5043.png)_

## Проверка работы приложения

1. Откройте шаблон процесса *«Открытие магазина»*.
2. Нажмите кнопку «**Перейти к экземплярам**».
3. Отобразится таблица «**Все записи**» со списком экземпляров процесса.
4. Создайте новый экземпляр процесса.
5. Подождите некоторое время, чтобы процесс выполнился.
6. Обновите список экземпляров, нажав кнопку «**Обновить список**» *‌*.
7. Статус процесса должен смениться на «**Завершен**».
8. Из списка экземпляров процесса перейдите к связанной записи шаблона *«Магазины»* по ссылке в столбце «**Запись**».
9. Отобразится настроенная форма *«Прогресс открытия магазина»*.
10. Расставьте флажки в таблице «Этапы *открытия магазина»*.
11. Цвета шевронов должны меняться в зависимости от состояния флажков *«Этап начат», «Этап пройден», «Этап пройден вовремя»:*
    - серый цвет — установлен флажок *«Этап начат»;*
    - зелёный цвет — установлены все три флажка;
    - красный цвет — установлены флажки *«Этап начат»* и *«Этап пройден».*

_![Проверка отображения шевронов на форме](https://kb.comindware.ru/assets/img_6606b888ea7b7.png)_

--8<-- "related_topics_heading.md"

**[Динамические элементы формы. Настройка шевронов][form_dynamic_elements]**

**[Шевроны. Правила окрашивания. Пример настройки][chevron_color_rules]**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
