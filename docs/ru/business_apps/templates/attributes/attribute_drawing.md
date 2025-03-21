---
title: Атрибут типа «Чертёж»
kbId: 4761
---

# Атрибут типа «Чертёж». Настройка шаблонов, атрибутов, форм и полей {: #attribute_drawing}

## Введение

На форме можно разместить чертёж, на котором будут отображаться данные из шаблонов записей с привязкой к объектам на чертеже.

Для использования чертежа в **{{ productName }}** потребуется подготовить файл DWG, создать несколько шаблонов и атрибутов определённых типов, поместить поле атрибута типа «**Чертёж**» на форму и привязать его к шаблонам записей и атрибутам. Конечный пользователь, в свою очередь, должен импортировать файл чертежа в формате DWG и привязать конкретные слои полигонов и маркеров на чертеже к шаблонам и атрибутам, заданным при настройке поля.

См. также _«[Чертёж. Подготовка и импорт файла DWG][attribute_drawing_file_import]»_ и _«[Атрибут типа «Чертёж». Настройка шаблонов, атрибутов, форм и полей][form_dynamic_elements_drawing]»_.

## Прикладная задача

Имеется план этажа с полигонами помещений и рабочих мест. Требуется настроить отображение на форме плана этажа с обозначением помещений и рабочих мест. Необходимо обеспечить возможность оформления и просмотра заявок на обслуживание помещений и рабочих мест на плане. Заявки должны быть представлены на плане в виде цветных маркеров. Цвета помещений и заявок должны соответствовать их статусу, а цвета рабочих мест — их состоянию.

Настроим приложение для работы с планом этажа:

- настроим шаблоны, формы и атрибуты для хранения данных помещений, рабочих мест и заявок;
- создадим и заполним записи помещений и рабочих мест в соответствии с чертежом;
- импортируем файл чертежа в приложение;
- на полученном плане создадим несколько заявок.

### Исходные данные {: .pageBreakBefore }

Имеется подготовленный чертёж в формате DWG с четырьмя слоями. Для корректного импорта чертёж необходимо подготовить в соответствии с требованиями, приведёнными в статье _«[Чертёж. Подготовка и импорт файла DWG][attribute_drawing_file_import]»_.

Свойства исходного чертежа:

- _Помещения_ — полигоны помещений:

    - _Диспетчерская_
    - _Переговорная_
    - _Кабинет руководителя_
    - _Отдел продаж_

- _ID помещений_ — текстовые блоки с идентификаторами полигонов помещений:

    - _Диспетчерская_
    - _Переговорная_
    - _Кабинет руководителя_
    - _Отдел продаж_

- _Рабочие места_ — полигоны рабочих мест:

    - _Диспетчер 1_
    - _Диспетчер 2_
    - _Диспетчер 3_
    - _Стол для переговоров_
    - _Рабочее место руководителя 1_
    - _Специалист по продажам 1_
    - _Специалист по продажам 2_
    - _Специалист по продажам 3_

- _ID рабочих мест_  — текстовые блоки с идентификаторами полигонов рабочих мест:

    - _Диспетчер 1_
    - _Диспетчер 2_
    - _Диспетчер 3_
    - _Стол для переговоров_
    - _Рабочее место руководителя 1_
    - _Специалист по продажам 1_
    - _Специалист по продажам 2_
    - _Специалист по продажам 3_

## Настройка шаблонов и атрибутов

Для настройки и использования чертежа на форме создайте перечисленные ниже шаблоны записей и атрибуты.

Шаблоны и атрибуты необходимо будет привязать к объектам в файле DWG во время настройки поля атрибута типа «**Чертёж**» и при импорте файла DWG конечным пользователем.

1. Создайте три шаблона записей: _Этажи, Помещения, Рабочие места, Заявки_.
2. Настройте в шаблонах атрибуты, как указано ниже.

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th markdown="block" colspan="3">
**Атрибуты шаблона «_Этажи»_**
</th>
</tr>
<tr markdown="block">
<th markdown="block">
**Тип данных**
</th>
<th markdown="block">
**Название**
</th>
<th markdown="block">
**Свойства**
</th>
</tr>
<tr markdown="block">
<td markdown="block">
_Текст_
</td>
<td markdown="block">
_Наименование_
</td>
<td markdown="block">
По умолчанию
</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Чертёж_
</td>
<td markdown="block">
_План_
</td>
<td markdown="block">
По умолчанию
</td>
</tr>
{% if pdfOutput %}
</tbody>
</table>

{% include-markdown ".snippets/pdfPageBreakHard.md" %}

<table markdown="block">
<tbody markdown="block">
{% endif %}
<tr markdown="block">
<th markdown="block" colspan="3">
**Атрибуты шаблона «_Помещения»_**
</th>
</tr>
<tr markdown="block">
<th markdown="block">
**Тип данных**
</th>
<th markdown="block">
**Название**
</th>
<th markdown="block">
**Свойства**
</th>
</tr>
<tr markdown="block">
<td markdown="block">
_Текст_
</td>
<td markdown="block">
_ID помещения_
</td>
<td markdown="block">
Установлены флажки:

- **Использовать как заголовок записей**
- **Контролировать уникальность значений**

</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Запись _
</td>
<td markdown="block">
_Этаж_
</td>
<td markdown="block">

- **Связанный шаблон**: _Этажи_
- **Хранить несколько значений**: флажок снят
- **Взаимная связь с атрибутом:**
    - **С новым**
      - **Название**: _Помещения_
      - **Хранить несколько значений**: флажок установлен

</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Список значений_
</td>
<td markdown="block">
_Статус_
</td>
<td markdown="block">
**Список значений:**

- _Эксплуатируется_
- _Не эксплуатируется_

</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Список значений_
</td>
<td markdown="block">
_Вид_
</td>
<td markdown="block">
**Список значений:**

- _Складское_
- _Санитарное_
- _Общее_
- _Техническое_
- _Офисное_
- _Административное_

</td>
</tr>
{% if pdfOutput %}
</tbody>
</table>
<table markdown="block">
<tbody markdown="block">
{% endif %}
<tr markdown="block">
<th markdown="block" colspan="3">
**Атрибуты шаблона «_Рабочие места»_**
</th>
</tr>
<tr markdown="block">
<th markdown="block">
**Тип данных**
</th>
<th markdown="block">
**Название**
</th>
<th markdown="block">
**Свойства**
</th>
</tr>
<tr markdown="block">
<td markdown="block">
_Текст_
</td>
<td markdown="block">
_ID рабочего места_
</td>
<td markdown="block">
Установлены флажки:

- **Использовать как заголовок записей**
- **Контролировать уникальность значений**

</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Текст_
</td>
<td markdown="block">
_Наименование_
</td>
<td markdown="block">
По умолчанию
</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Список значений_
</td>
<td markdown="block">
_Статус_
</td>
<td markdown="block">
**Список значений:**
- _Свободно_
- _Занято_

</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Список значений_
</td>
<td markdown="block">
_Состояние_
</td>
<td markdown="block">
**Список значений:**

- _Хорошее_
- _Плохое_

</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Запись (Связать с Шаблон записи Помещения)_
</td>
<td markdown="block">
_Помещение_
</td>
<td markdown="block">

- **Связанный шаблон:** _Помещения_
- **Хранить несколько значений:** флажок снят
- **Взаимная связь с атрибутом:**
    - **С новым:**
        - _Название:_ Рабочие места
        - **Хранить несколько значений:** флажок установлен

</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Запись (Связать с Шаблон записи Этажи)_
</td>
<td markdown="block">
_Этаж_
</td>
<td markdown="block">

- **Связанный шаблон:** _Этажи_
- **Хранить несколько значений:** флажок снят
- **Взаимная связь с атрибутом:**
  - **С новым:**
    - _Название:_ Рабочие места
    - **Хранить несколько значений:** флажок установлен

</td>
</tr>
{% if pdfOutput %}
</tbody>
</table>
<table markdown="block">
<tbody markdown="block">
{% endif %}
<tr markdown="block">
<th markdown="block" colspan="3">
**Атрибуты шаблона «_Заявки»_**
</th>
</tr>
<tr markdown="block">
<th markdown="block">
**Тип данных**
</th>
<th markdown="block">
**Название**
</th>
<th markdown="block">
**Свойства**
</th>
</tr>
<tr markdown="block">
<td markdown="block">
_Запись_
</td>
<td markdown="block">
_Этаж_
</td>
<td markdown="block">

- **Связанный шаблон:** _Этажи_
- **Хранить несколько значений:** флажок снят
- **Взаимная связь с атрибутом:**
  - **С новым:**
    - _Название:_ _Заявки_
    - **Хранить несколько значений:** флажок установлен

</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Запись_
</td>
<td markdown="block">
_Помещение_
</td>
<td markdown="block">

- **Связанный шаблон:** _Помещения_
- **Хранить несколько значений:** флажок снят
- **Взаимная связь с атрибутом:**
    - **С новым:**
        - _Название:_ _Заявки_
        - **Хранить несколько значений:** флажок установлен

</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Запись_
</td>
<td markdown="block">
_Рабочее место_
</td>
<td markdown="block">

- **Связанный шаблон:** _Рабочие места_
- **Хранить несколько значений:** флажок снят
- **Взаимная связь с атрибутом:**
    - **С новым:**
      - _Название:_ _Заявки_
      - **Хранить несколько значений:** флажок установлен

</td>
</tr>
<tr markdown="block">
<td markdown="block">
_Список значений_
</td>
<td markdown="block">
_Статус_
</td>
<td markdown="block">
**Список значений:**

- _Открыта_
- _Отменена_
- _Выполняется_
- _Выполнена_
- _Ожидает проверки_
- _Проверена_

</td>
</tr>
</tbody>
</table>

## Настройка форм и полей {: .pageBreakBefore }

1. Вынесите созданные атрибуты на основные формы шаблонов.
2. В шаблоне записи «Этажи» откройте основную форму и выберите поле атрибута «**План**».
3. Выберите блок «**Связи**» на поле чертежа.

    _![Настройка связей между слоями чертежа и шаблонами записи в приложении](img/attribute_drawing_layers_settings.png)_

4. Настройте два уровня связей между слоями чертежа и шаблонами записей с помощью панели «**Свойства связей**»:

    - _Уровень 1_

        - **Шаблон записи:** _Помещения_. В этом шаблоне будут храниться записи, связанные с полигонами слоя _«Помещения»_ на чертеже.
        - **Атрибут:** _ID помещения._ По этому ключевому атрибуту полигоны со слоя _«Помещения»_ на чертеже будут привязаны к записям в шаблоне _«Помещения»_ путем сопоставления наименований полигонов со слоя _«ID помещений»_ со значениями атрибута.
        - **Форма на чертеже:** _Помещения — Основная форма._ Эта форма будет отображаться в информационной панели для полигона, выбранного на чертеже.
        - **Форма для перехода:** _Помещения — Основная форма._ Эта форма будет отображаться при нажатии кнопки _«Перейти к записи»_ в информационной панели для полигона, выбранного на чертеже.
        {% include-markdown ".snippets/pdfPageBreakHard.md" %}

    - _Уровень 2_

        - **Шаблон записи:** _Рабочие места._ В этом шаблоне будут храниться записи, связанные с полигонами слоя _«Рабочих мест»_ на чертеже. Настройте его аналогично _Уровню 1._
        - **Атрибут:** _ID рабочего места_
        - **Форма на чертеже:** _Рабочие места — Основная форма_
        - **Форма на чертеже:** _Рабочие места — Основная форма_

5. Выберите блок «**Маркеры**» на поле чертежа.

    _![Настройка привязки маркеров на плане к записям в приложении и слоям чертежа](img/attribute_drawing_markers_settings.png)_

6. Настройте привязку записей из шаблона _«Заявки»_ к маркерам на плане с помощью панели «**Свойства маркеров**»:

    - **Шаблон записи:** _Заявки._ Записи этого  шаблона, будут отображаться как маркеры на плане.
    - **Форма для перехода:** _Заявки — Основная форма._ Эта форма будет отображаться в информационной панели для маркера, выбранного на чертеже.
    - **Форма на** **чертеже:** _Заявки — Основная форма._ Эта форма будет отображаться при нажатии кнопки «**Перейти к записи**» в информационной панели на чертеже.
    - **Таблица:** _Все записи._ Эта таблица будет отображаться на вкладке «**Заявки**» слева от плана. Если для таблицы назначено [представление карточек][cards_configure], то оно будет отображаться вместо таблицы.
    - **Привязка к слоям** — укажите для каждого уровня связи (слоя на чертеже) атрибут типа «**Запись**» из шаблона _«Заявки»_, ссылающийся на шаблон записи, заданный в **связях**. Маркеры будут привязаны к соответствующим слоям:

        - Слой _«Помещения»:_ атрибут _«Помещение»_
        - Слой _«Рабочие места»: атрибут _«Рабочее место»_

7. Выберите блок «**Метаданные**» на поле чертежа.

    _![Выбор атрибутов, задающих цвета полигонов на плане](attribute_drawing_polygon_colours.png)_

8. На панели «**Свойства метаданных**» оставьте установленными все флажки. Каждый флажок представляет атрибут типа «**Список значений**», задающий цвета полигонов, связанных с записями помещений и рабочих мест. Кроме того, с помощью вкладки «**Цвета**» слева от плана конечный пользователь сможет отфильтровать полигоны по значениям выбранных атрибутов.

    - Слой _«Помещения»:_ установите флажок _«Статус»_  и _«Вид»_
    - Слой _«Рабочие места»:_ установите флажки _«Статус»_ и _«Состояние»_

9. Создайте в шаблоне _«Этажи»_ одну запись с _наименованием «Этаж 1»_.
10. Создайте и заполните записи в шаблонах _«Помещения»_ и _«Рабочие места»._

    - В каждой записи введите ID помещения или рабочего места, соответствующий текстовому идентификатору полигона в подготовленном DWG-файле.
    - Шаблон _«Помещения»_

        - Создайте записи со следующими значениями атрибута _«ID помещения»_:

            - _Диспетчерская_
            - _Переговорная_
            - _Кабинет руководителя_
            - _Отдел продаж_

        - Для всех записей укажите _Этаж 1_.
        - Поля _«Статус»_ и _«Вид»_ заполните произвольными значениями.

    - Шаблон _«Рабочие места»_

        - _Создайте записи со следующими значениями атрибута _«ID рабочего места»_:

            - _Диспетчер 1_
            - _Диспетчер 2_
            - _Диспетчер 3_
            - _Стол для переговоров_
            - _Рабочее место руководителя 1_
            - _Специалист по продажам 1_
            - _Специалист по продажам 2_
            - _Специалист по продажам 3_

        - Для всех записей укажите _Этаж 1_.
        - Для каждого рабочего места, укажите соответствующее помещение.
        - Поля _«Статус»_ и _«Состояние»_ заполните произвольными значениями.

11. Создайте несколько записей в шаблоне _«Заявки»_, указав для них _этаж 1_, произвольное помещение, соответствующее помещению рабочее место и произвольный статус.
12. В поле _«План»_ на форме записи _«Этаж 1»_ нажмите кнопку «**Загрузка файла**».
13. С помощью мастера _«_**Настройка плана**_»_ загрузите DWG-файл и привяжите слои полигонов и слои наименований на чертеже к шаблонам записи:

    | Слой полигонов | Слой наименований | Шаблон записи | Атрибут           |
    | -------------- | ----------------- | ------------- | ----------------- |
    | Помещения      | ID помещений      | Помещения     | ID помещения      |
    | Рабочие места  | ID рабочих мест   | Рабочие места | ID рабочего места |

    _![Привязка слоёв чертежа к шаблонам записей в приложении](attribute_drawing_layers_connect.png)_

14. Отобразится план _этажа 1_.
15. Поэкспериментируйте с планом:

    - выбирайте полигоны и маркеры на плане;
    - просматривайте сведения об объектах и заявках в панели справа от чертежа;
    - выбирайте, скрывайте и отображайте слои, объекты и маркеры с помощью панели слева от чертежа.

    _![Использование плана на форме](img/attribute_drawing_plan_usage.png)_

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Чертёж. Подготовка и импорт файла DWG][attribute_drawing_file_import]_
- _[Чертёж. Настройка поля на форме][form_dynamic_elements_drawing]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
