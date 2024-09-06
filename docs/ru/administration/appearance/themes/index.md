---
title: Темы. Настройка, применение, предпросмотр
kbId: 2199 
---

# Темы. Настройка, применение, предпросмотр {:#themes}

## Использование конструктора тем

1. Чтобы перейти к конструктору тем, на странице «**[Администрирование][administration]**» — «**[Внешний вид][внешний-вид]**» выберите пункт «**Темы**» <i class="fa-light  fa-palette"></i>.
2. Отобразится конструктор тем.
3. Настройте тему с помощью следующих разделов:
      * [Доступные темы][операции-с-темами]
      * [Свойства системы][свойства-системы]
      * [Шрифты][шрифты]
      * [Цветовая палитра][цветовая-палитра]
      * [Предварительный просмотр][предварительный-просмотр]
4. [Сохраните изменения][сохранение-и-сброс-настроек] темы.

## Операции с темами

Для настройки внешнего вида системы вы можете использовать стандартную тему под названием «**{{ companyName }}**», создать новую тему либо клонировать имеющуюся.

Стандартную тему «**{{ companyName }}**» изменить нельзя (для настройки ее следует [клонировать](#клонирование-темы)).

В разделе «**Доступные темы**» отображаются эскизы имеющихся тем и кнопки для выполнения операций с темами:

* [**Создать**](#создание-новой-темы)
* [**Клонировать**](#клонирование-темы)
* [**Удалить**](#удаление-темы)
* [**Применить**](#применение-темы)

_![Доступные темы](available_themes.png)_

### Выбор темы для настройки

1. Нажмите эскиз темы.
2. Выбранная в будет отмечена флажком на ее эскизе.
3. Теперь все внесённые изменения будут применяться для выбранной темы.

_![Выбранная тема отмечена флажком](applied_theme.png)_

### Применение темы

1. Нажмите эскиз темы, которую требуется применить.
2. Нажмите кнопку «**Применить**» для применения выбранной темы.
3. Отобразится запрос на обновление страницы для вступления изменений в силу.
4. Теперь система будет отображаться с использованием применённой темы.

_![Запрос на обновление страницы для применения темы](apply_theme.png)_

### Создание новой темы

1. Нажмите кнопку «**Создать**», для создания новой темы со стандартной конфигурацией.
2. Отобразится окно «**Создание новой темы**».
3. Введите **название новой темы**.
4. Нажмите кнопку «**Создать**».
5. Новая тема будет создана, выбрана и применена.
6. Теперь все внесённые изменения будут применяться для выбранной темы.

_![Окно создания новой темы](new_theme.png)_

### Клонирование темы

1. Нажмите эскиз темы, которую требуется дублировать.
2. Нажмите кнопку «**Клонировать**».
3. Отобразится окно «**Клонирование темы**».
4. Укажите **название новой темы**.
5. Нажмите кнопку «**Клонировать**».
6. Будет создан дубликат выбранной темы.
7. Новая тема будет выбрана.
8. Теперь все внесённые изменения будут применяться для выбранной темы.
9. Если исходная тема была применена, то вместо нее будет применена тема-дубликат.

_![Окно клонирования темы](clone_theme.png)_

### Удаление темы

!!! note "Примечание"

    Тему, которая применена в настоящий момент, удалить нельзя (кнопка «**Удалить**» не будет отображаться).

    Для удаления применённой темы сначала примените другую тему.

1. Нажмите эскиз темы, которую требуется удалить.
2. Нажмите кнопку «**Удалить**».
3. Отобразится окно «**Подтвердите удаление**».
4. Нажмите кнопку «**Удалить**».

## Сохранение и сброс настроек

В разделах, в которых имеется возможность настройки параметров темы, предусмотрены следующие кнопки:

* **Сохранить** — сохранение настроенных параметров раздела;
* **Сбросить настройки** — восстановление ранее сохраненных параметров раздела.

Прежде чем сохранять настройки в разделах темы, ознакомьтесь с [предварительным просмотром](#предварительный-просмотр), чтобы убедиться в правильности конфигурации темы.

Если редактируемая тема применена, после нажатия кнопки «**Сохранить**» отобразится запрос на обновление страницы. Чтобы изменения вступили в силу, подтвердите обновление страницы.

_![Сохранение настроек в разделе «Свойства системы»](apply_theme.png)_

## Свойства системы

Данный раздел отображается только для особых тем и не отображается для стандартной темы под названием «**{{ companyName }}**».

_![Раздел «Свойства системы»](system_properties.png)_

Вы можете задать «**Название системы**», которое будет отображаться в верхней информационной панели:

_![Верхняя информационная панель с заданным названием системы](system_name_theme.png)_

## Фирменные изображения

Для темы можно назначить собственные изображения:

* **Значок сайта** — это изображение будет отображаться во вкладках браузера;
* **Логотип** — это изображение по умолчанию используется в качестве логотипа **[страниц входа и регистрации][дизайн-страниц-входа-и-регистрации]**;
* **Фон страниц** — это изображение по умолчанию используется в качестве фона **страниц входа и регистрации**.

_![Фирменные изображения](branded_images.png)_

Для назначенных теме фирменных изображений предусмотрено меню операций:

* **История** — просмотр журнала изменений загруженного в систему файла изображения;
* **Скачать** — загрузка файла изображения на компьютер;
* **Удалить** — удаление файла изображения из системы.

Чтобы вызвать это меню, нажмите крайнюю правую часть панели с именем файла:

_![Меню операций с изображением](image_manipulation.png)_

## Шрифты

В этом разделе можно настроить **шрифт заголовков** и **шрифт обычного текста** в системе:

* **Шрифт** — выберите гарнитуру шрифта из предложенного списка;
* **Начертание** — выберите вариант шрифта из предложенного списка:
    - Regular (Обычный), Italic (Курсив), Bold (Полужирный), Light (Тонкий), Medium (Средний);
* **Базовый размер** — выберите из предложенного списка размер шрифта, относительного которого будут определяться размеры заголовков и текстов соответственно.

_![Шрифты](fonts.png)_

## Цветовая палитра

В этом разделе можно задать собственные цвета для большинства элементов системы.

### Цвета основных элементов

В этом разделе можно настроить:

* основной **фирменный цвет** — цвет большинства графических элементов: верхней информационной панели, фона заголовков разделов и столбцов, флажков, названия выбранной вкладки, гиперссылок;
* цвета **окон и меню**:
    - **фона страниц**;
    - **фона меню**;
    - **основного фона**;
* **цветовые акценты**:
    - **ошибки** — цвет фона всплывающих сообщений об ошибках;
    - **успех** — цвет фона всплывающих сообщений о выполненных действиях;
    - **предупреждения** — цвет фона всплывающих предупреждениях;
* цвет **текста** — заголовков полей, текста в полях ввода, дат, подписей флажков, названий невыбранных вкладок;
* цвет **выделения** — цвет выделения строк и столбцов в таблицах при их выборе;
* цвета **стандартных кнопок**:
    - **обычной кнопки**;
    - **кнопки отмены**.

_![Цветовая палитра — Основные элементы](palette_basic.png)_

### Цвета приоритетов

В этом разделе можно настроить цвета, которые можно будет назначать различным кнопкам при конструировании бизнес-решений.

_![Подраздел «Цветовая палитра — Приоритеты»](palette_priority.png)_

### Цвета дополнительных элементов

В этом разделе можно настроить цветовое оформление дополнительных элементов интерфейса системы:

* **Тени** — выберите **цвет**, **прозрачность** и **размытие** для различных теней:
    - **теней меню**;
    - **теней раскрывающегося меню**;
    - **теней всплывающего окна**;
    - **теней конструктора**;
* **Рамки** — выберите цвет рамок для различных элементов интерфейса системы:
    - **основных рамок**
    - **рамок таблиц**
    - **рамок элементов меню**

_![Подраздел «Цветовая палитра — Дополнительно»](palette_additional.png)_

### Цвета графиков и диаграмм {: #themes_graphic_diagram_color}

В этом разделе можно задать цвета, которые будут использоваться для линий, столбцов и сегментов графиков и диаграмм, построенных в системе.

_![Подраздел «Цветовая палитра — Графики и диаграммы»](palette_charts.png)_

### Пользовательские стили

В этом разделе можно указать дополнительные пользовательские стили CSS для изменения внешнего вида системы.

_![Подраздел «Цветовая палитра — Пользовательские стили»](palette_custom_css.png)_

## Предварительный просмотр

В этом разделе можно ознакомиться с тем, как интерфейс системы будет выглядеть с заданными настройками. Прежде чем сохранять настройки в разделах темы, ознакомьтесь с предварительным просмотром, чтобы убедиться в правильности конфигурации темы.

### Предпросмотр оформления основных элементов

_![Предварительный просмотр — Основные элементы](preview_basic.png)_

### Предпросмотр оформления форм

_![Предварительный просмотр — Формы](preview_forms.png)_

### Предпросмотр оформления таблиц

_![Предварительный просмотр — Формы](preview_tables.png)_

--8<-- "related_topics_heading.md"

**[Дизайн страниц входа и регистрации][дизайн-страниц-входа-и-регистрации]**