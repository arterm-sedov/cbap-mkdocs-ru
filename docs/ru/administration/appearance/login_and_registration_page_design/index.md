---
title: Дизайн страниц входа и регистрации
kbId: 4707
---

# Дизайн страниц входа и регистрации {: #login_and_registration_page_design}

## Использование конструктора страниц входа и регистрации

Конструктор страниц входа и регистрации позволяет настроить внешний вид и состав страниц, которые видят пользователи при входе в систему и регистрации.

1. На странице «[**Администрирование**][administration]» в разделе «**Внешний вид**» выберите пункт «**Дизайн страниц входа и регистрации**» <i class="fa-light fa-file-image">‌</i>.
2. Отобразится [конструктор страниц входа и регистрации](#использование-конструктора-страниц-входа-и-регистрации).
3. Настройте свойства страниц и блоков на них:

    - [страницу входа](#настройка-страницы-входа);
        - [информационный блок](#информационный-блок);
    - [страницу регистрации](#настройка-страницы-регистрации);
    - [логотип](#логотип);
    - [блок социальных сетей](#социальные-сети);
    - [блок ссылок](#ссылки);
    - [фон страниц](#фон).

4. Cохраните изменения. _При этом измененные страницы не будут опубликованы._
5. Опубликуйте сохраненную конфигурацию страниц входа и регистрации, нажав кнопку «**Опубликовать**» (_несохраненная конфигурация опубликована не будет_).
6. После публикации для пользователей будут отображаться страницы входа и регистрации с сохраненной конфигурацией.

_![Пример опубликованной страницы входа](img/published_login_page_example.png)_

### Области конструктора страниц входа и регистрации {: .pageBreakBefore }

1. **Кнопки**

    - **Сохранить** — сохранение текущей конфигурации страниц входа и регистрации;
    - **Опубликовать** — публикация сохраненной конфигурации страниц входа и регистрации;
    - **Сбросить** — восстановление стандартной конфигурации страниц входа и регистрации.

2. **Панель элементов** — позволяет выбирать страницы и блоки, включать и отключать различные блоки страниц входа и регистрации;
3. **Макет страницы** — позволяет выбирать блоки страницы и показывает её предварительное представление;
4. **Панель свойств** — позволяет настроить конфигурацию выбранного элемента.

_![Области конструктора страниц входа и регистрации](img/login_page_design.png)_

## Настройка страницы входа {: .pageBreakBefore }

1. В панели элементов выберите пункт «**Страница входа**».
2. Отобразятся макет и панель свойств страницы входа.
3. В панели «**Свойства страницы входа**» ведите **заголовок страницы** — он будет отображаться во вкладке браузера, когда пользователь находится на странице входа.
4. Настройте [информационный блок](#информационный-блок).
5. Настройте общие блоки страниц входа и регистрации:

    - [Логотип](#логотип)
    - [Социальные сети](#социальные-сети)
    - [Ссылки](#ссылки)
    - [Фон](#фон)

_![Настройка страницы входа](img/login_page_heading.png)_

### Информационный блок {: .pageBreakBefore }

На странице входа может отображаться информационный блок, содержащий изображение-баннер, произвольный текст и гиперссылку для перехода на произвольную веб-страницу.

1. В панели «**[Свойства страницы входа](#настройка-страницы-входа)**» установите флажок «**Информационный блок**», чтобы включить его отображение.
2. В панели элементов выберите пункт «**Информационный блок**», чтобы настроить его.
3. Отобразится панель «**Свойства информационного блока**».
4. Выберите изображение, которое будет отображаться в верхней части информационного блока:

    - **Стандартное** — готовое изображение из **{{ productName }}**;
    - **Новое изображение** — выберите любой файл типа JPG, GIF, PNG или SVG в соответствии с указанными требованиями к размеру;
    - **Без изображения** — информационный блок будет отображаться без баннера.

5. Настройте содержимое информационного блока:
    - **Заголовок** — отображается под изображением-баннером или вместо него (если изображение не выбрано);
    - **Текст** — отображается под заголовком; текст можно отформатировать с помощью встроенных средств редактирования, или можно вставить HTML-текст из буфера обмена;
    - **Текст кнопки** — подпись гиперссылки, расположенной внизу информационного блока;
    - **Ссылка для перехода** — указанная ссылка откроется в новой вкладке браузера при нажатии гиперссылки в информационном блоке.

_![Настройка информационного блока страницы входа](img/information_block_properties.png)_

## Настройка страницы регистрации {: .pageBreakBefore }

1. В панели элементов выберите пункт «**Страница регистрации**».
2. Отобразятся макет и панель свойств страницы регистрации.
3. В панели «**Свойства страницы регистрации**» ведите **заголовок страницы** — он будет отображаться во вкладке браузера, когда пользователь находится на странице регистрации.
4. Настройте общие блоки страниц входа и регистрации:

    - [Логотип](#логотип)
    - [Социальные сети](#социальные-сети)
    - [Ссылки](#ссылки)
    - [Фон](#фон)

_![Настройка заголовка страницы регистрации](img/registration_page_designer.png)_

## Настройка общих блоков страниц входа и регистрации {: .pageBreakBefore }

Для страниц входа и регистрации предусмотрены общие элементы:

- [Логотип](#логотип)
- [Социальные сети](#социальные-сети)
- [Ссылки](#ссылки)
- [Фон](#фон)

_![Общие блоки страниц входа и регистрации](img/login_and_registration_page_blocks.png)_

### Логотип {: .pageBreakBefore }

Блок «**Логотип**» содержит изображение и текстовую подпись, он отображается в верхней части страниц входа и регистрации.

1. Установите флажок «**Логотип**» в панели элементов, чтобы включить этот блок.
2. Отобразится панель «**Свойства логотипа**».
3. Выберите **изображение** логотипа:

    - **Логотип из темы** — изображение логотипа, выбранное в разделе «**[Фирменные изображения][themes_branded_images]**» текущей [темы][themes];
    - **Новое изображение** — выберите любой файл типа JPG, GIF, PNG или SVG в соответствии с указанными требованиями к размеру;
    - **Без логотипа** — блок логотипа будет отображаться без изображения.

4. Введите **текст под логотипом**. Если **изображение** логотипа не выбрано, то в блоке логотипа будет отображаться только текст.
5. Задайте **цвет текста** под логотипом. Если не задать цвет, то будет использоваться **цвет текста**, заданный в разделе «**[Цвета основных элементов][themes_base_colors]**» текущей темы.

_![Настройка логотипа](img/logo_properties.png)_

### Социальные сети {: .pageBreakBefore }

Блок «**Социальные сети**» содержит значки со ссылками на веб-сайты, он отображается по центру в нижней части страниц входа и регистрации.

1. В панели элементов установите флажок «**Социальные сети**», чтобы включить этот блок.
2. Отобразится панель «**Свойства блока «Социальные сети**».
3. Введите заголовок блока, который будет отображаться над значками соцсетей.
4. Добавьте или удалите значки соцсетей с помощью кнопок «**Добавить**»&nbsp;![Кнопка добавления](add_button.png) и «**Удалить**»&nbsp;![Кнопка удаления](delete_button.png).
5. Настройте ссылки на соцсети:

    - **Значок** — дважды нажмите значок, чтобы сменить его;
    - **Ссылка для перехода** — введите адрес веб-сайта соцсети;
    - **Текст при наведении** — введите текст, который будет отображаться при наведении мыши на значок.

_![Настройка блока «Социальные сети»](img/social_network_properties.png)_

### Ссылки {: .pageBreakBefore }

Блок «**Ссылки**» может содержать два элемента следующих типов:

- ссылки для скачивания файлов;
- простой текст;
- ссылки на веб-сайты;
- ссылки на адреса эл.&nbsp;почты.

Этот блок отображается справа в нижней части страниц входа и регистрации.

1. В панели элементов установите флажок «**Ссылки**», чтобы включить этот блок.
2. Отобразится панель «**Свойства блока ссылок**».
3. Добавьте или удалите элементы в блоке ссылок с помощью кнопок «**Добавить**»&nbsp;![Кнопка добавления](img/add_button.png) и «**Удалить**»&nbsp;![Кнопка удаления](img/delete_button.png).
4. Выберите **тип элемента** и настройте его.

    - **Файл**

        - **Выберите файл** — загрузите с компьютера компьютера файл, который можно будет скачать по гиперссылке.
        - **Отображаемый текст** — введите подпись гиперссылки для скачивания выбранного файла.

    - **Простой текст**

        - **Отображаемый текст** — будет отображаться без гиперссылки.

    - **Ссылка**

        - **Отображаемый текст** — введите подпись гиперссылки.
        - **Ссылка для перехода** — введите URL-адрес веб-сайта.

    - **Адрес эл.&nbsp;почты**

        - **Отображаемый текст** — введите адрес эл.&nbsp;почты, который будет отображаться как гиперссылка. Не вводите префикс `mailto:`, он будет добавлен в гиперссылку автоматически.

_![Настройка блока «Ссылки»](img/link_properties_email.png)_

### Фон {: .pageBreakBefore }

Фон — это подложка на которой отображаются остальные элементы страниц входа и регистрации.

1. В панели элементов выберите пункт «**Фон**».
2. Отобразится панель «**Свойства фона страницы**».
3. Выберите **фон страницы**:

    - **Фон из темы** — в качестве фона страниц будет использоваться **фон страниц**, выбранный в разделе «**[Фирменные изображения][themes_branded_images]**». Если изображение не задано, будет использоваться **цвет фона страниц**, выбранный в разделе «**[Цвета основных элементов][themes_base_colors]**» текущей темы;
    - **Новое изображение** — выберите любой файл типа JPG, GIF, PNG или SVG в соответствии с указанными требованиями к размеру;
    - **Без изображения** — укажите **цвет фона** страниц входа и регистрации.

_![Настройка фона страниц входа и регистрации](img/background_properties_new_image.png)_

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Темы. Настройка, применение, предпросмотр][themes]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
