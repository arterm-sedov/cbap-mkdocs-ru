---
title: Диаграмма процесса. Определения, просмотр, редактирование, публикация
kbId: 2360
---

# Диаграмма процесса. Определения, просмотр, редактирование, публикация

### Определения

**Диаграмма процесса** служит для моделирования и исполнения бизнес-процесса. Она обладает следующими характеристиками:

- привязана к [шаблону процесса][process_templates];
- создаётся при создании шаблона процесса;
- строится в нотации BPMN 2.0;
- задаёт последовательность выполнения задач и действий в рамках бизнес-процесса;
- позволяет моделировать и исполнять бизнес-процесс с назначением задач исполнителям, выполнением сценариев, отправкой внутренних и внешних сообщений, просмотром журнала действий.

**Токен** — это маркер текущей позиции выполнения процесса. Он обладает следующими характеристиками:

- на диаграмме процесса может быть один или несколько токенов, каждый из которых будет двигаться по своему пути;
- токены создаются в начальных событиях, некоторых промежуточных событиях и на расходящихся развилках;
- токены удаляются в конечных событиях и на сходящихся развилках;
- в качестве аналогии, токен можно представить себе как фишку, которая двигается по процессу.

## Просмотр диаграммы процесса

1. Откройте [шаблон процесса][process_templates].
2. Перейдите на вкладку «**Диаграмма**».
3. Отобразится диаграмма процесса в режиме просмотра со следующими кнопками:
    - Операций с диаграммой
        - **Выбрать версию** — [управление опубликованными версиями][process_diagram_version_control] диаграммы процесса.
        - **Экспортировать** — выгрузка диаграммы процесса в виде файла формата `SVG`. При нажатии этой кнопки браузер скачает файл вида `export_2023-03-03T15_25_23 03_00.svg`.
        - **Редактировать** — переход к [конструктору диаграммы процесса][process_diagram].
    - Масштабирование диаграммы
    
    
        - **Показать всю диаграмму** *‌*
        - **Увеличить** *‌*
        - **Уменьшить** *‌*Масштабировать диаграмму также можно с помощью колёсика прокрутки мыши. Перемещать видимую область диаграммы можно, нажав и перетащив её пустую область.

_![Диаграмма шаблона процесса в режиме просмотра](https://kb.comindware.ru/assets/process_diagram_view.png)_

## Переход к конструктору диаграммы процесса

Конструктор диаграммы процесса позволяет [редактировать диаграмму][process_diagram]   путем перетаскивания необходимых элементов и настроить логику исполнения процесса. 

1. Откройте вкладку «**[Диаграммы](https://kb.comindware.ru/article.php?id=2359)**» шаблона процесса.
2. При необходимости [выберите версию диаграммы][process_diagram_version_control].
3. Нажмите кнопку «**Редактировать**».
4. Отобразится конструктор диаграммы процесса.
5. [Отредактируйте диаграмму процесса][process_diagram].

_![Конструктор диаграммы процесса](https://kb.comindware.ru/assets/process_diagram_designer.png)_

## Области конструктора диаграммы процесса

1. **Кнопки операций с диаграммой**

    - **Выбрать версию** — [управление опубликованными версиями][process_diagram_version_control] диаграммы процесса.
    - **Очистить** — удаление всех элементов с диаграммы процесса. При нажатии этой кнопки отобразится запрос подтверждения.
    - **Восстановить** — [восстановление][process_diagram_version_control] опубликованной версии диаграммы процесса.
    - **Опубликовать** — [публикация](https://kb.comindware.ru/article.php?id=2361) текущей диаграммы бизнес-процесса.
    - **Проверить** — [проверка](https://kb.comindware.ru/article.php?id=2357) диаграммы процесса на ошибки, не позволяющие опубликовать её.
    - **Экспортировать** — выгрузка диаграммы процесса в виде файла формата `SVG`. При нажатии этой кнопки браузер скачает файл вида `export_2023-03-03T15_25_23 03_00.svg`.
2. **Панель элементов** — содержит [элементы][process_diagram_elements], которые можно перетащить на диаграмму процесса.
3. **Панель свойств элемента** — отображается, когда выбран элемент диаграммы и содержит [общие свойства элемента][process_diagram_element_common_properties]:

    - системное имя;
    - отображаемое название;
    - описание.
4. **Диаграмма-процесса** — область построения диаграммы.
5. **Кнопки масштабирования**

    - **Показать всю диаграмму** *‌*
    - **Увеличить** *‌*
    - **Уменьшить** *‌*Масштабировать диаграмму также можно с помощью колёсика прокрутки мыши. Перемещать видимую область диаграммы можно, нажав и перетащив её пустую область.
6. **Меню элемента** — содержит команды для работы с выбранным элементом. См. «*[Вызов меню элемента](#mcetoc_1h28cr6421)*».

## Добавление элемента

1. Перетащите элемент из панели элементов на диаграмму.
2. Для нового элемента отобразится его контекстное меню.

_![Добавление элемента на диаграмму](https://kb.comindware.ru/assets/process_diagram_designer_add_element.png)_

## Вызов меню элемента

1. Нажмите элемент диаграммы.
2. Отобразится его контекстное меню. Набор команд в этом меню зависит от [типа элемента][process_diagram_elements].

_![Меню элемента диаграммы](https://kb.comindware.ru/assets/process_diagram_designer_element_menu.png)_

## Выбор элементов

- Чтобы выбрать один элемент, нажмите его.
- Чтобы выбрать несколько элементов, обведите их, удерживая нажатой клавишу `Shift`.
- Чтобы выбрать все элементы диаграммы, нажмите клавиши `Ctrl` `A`.

## Перемещение элементов

[Выберите](#mcetoc_1h28cr6432) один или несколько элементов и перетащите их в требуемую позицию на диаграмме.

## Изменение размера элемента

1. Наведите указатель мыши на границу элемента.
2. Если размер элемента можно изменить, отобразится курсор перетаскивания *‌*.
3. Перетащите границу элемента, чтобы изменить его размер.

## Переименование элемента

1. Дважды нажмите название элемента на диаграмме или нажмите кнопку «**Свойства**» *‌*в меню элемента.
2. Введите новое название элемента.

## Удаление элемента

1. [Выберите](#mcetoc_1h28cr6432) один или несколько элементов.
2. В отобразившемся меню элемента нажмите кнопку «**Удалить**» *‌* или нажмите клавишу `Del`.
3. Подтвердите удаление элементов.

## Публикация диаграммы процесса

1. Откройте [конструктор диаграммы](#mcetoc_1h2d97s1m0).
2. Нажмите кнопку «**Опубликовать**».
3. Будет выполнена [проверка диаграммы](https://kb.comindware.ru/article.php?id=2357).
4. Если проверка прошла успешно, отобразится запрос выбора способа публикации. Если будут обнаружены ошибки, исправьте их, прежде чем публиковать диаграмму.
5. Выберите способ публикации диаграммы:
    - **Заменить опубликованную версию** — все экземпляры процесса данной версии будут обновлены (включая завершенные). Например, при публикации диаграммы версии **3.1** она заменит версию **3.0** и будет применена для всех экземпляров процесса версии **3.0**.
    - **Создать новую версию** — по ней будут выполняться новые экземпляры процесса. Например, если уже имеется **10** версий диаграммы, при публикации диаграммы версии **3.1** будет создана версия **11**, которая будет использоваться для новых экземпляров процесса.

## Проверка диаграммы процесса и типичные ошибки

Перед [публикацией](#mcetoc_1hpj864hq0) диаграммы будет автоматически выполнена её проверка.

Для проверки диаграммы вручную, нажмите кнопку «**Проверить**».

Примечание

Опубликовать диаграмму с ошибками невозможно, поэтому после проверки все ошибки необходимо устранить.

- После проверки элементы с ошибками выделяются красной рамкой с восклицательным знаком *‌* и на верхней информационной панели отображается флаг *‌* с количеством ошибок.
- Для просмотра списка [сообщений об ошибках](#mcetoc_1h2b77qlu0) нажмите флаг *‌* в верхней информационной панели.
- Для просмотра сообщения об ошибке для элемента нажмите восклицательный знак *‌* рядом с ним.

_![Просмотр ошибок диаграммы процесса](https://kb.comindware.ru/assets/process_diagram_validation_errors.png)_

## Типичные ошибки диаграммы процесса

Проверка диаграммы процесса может выявить ошибки, которые не позволяют опубликовать диаграмму. В следующей таблице представлены некоторые типичные ошибки с описанием причин их возникновения и способами устранения.

| Ошибка | Элемент диаграммы | Причина | Способ устранения |
| --- | --- | --- | --- |
| Диаграмма пуста | Диаграмма | Диаграмма не содержит ни одного элемента | Добавьте на диаграмму элементы: как минимум начальное и конечное события |
| Диаграмма должна содержать хотя бы одно начальное событие | Диаграмма | На диаграмме отсутствует начальное событие | Добавьте на диаграмму начальное событие |
| У этого элемента должен быть один исходящий поток управления | Начальное событие | У начального события отсутствует исходящий поток или несколько исходящих потоков | Подсоедините только один исходящий поток к начальному событию |
| На диаграмме не может быть более одного простого (нетипизированного) начального события | Простое начальное событие | На диаграмме имеется несколько простых начальных событий | Удалите все простые начальные события кроме одного либо измените типы начальных событий |
| Необходим хотя бы один входящий поток управления | Конечное событие | У конечного события отсутствует входящий поток | Подсоедините входящий поток к конечному событию |
| Необходим хотя бы один входящий поток управления | Пользовательская задача | У пользовательской задачи отсутствует входящий поток | Подсоедините входящий поток к пользовательской задаче |
| У этого элемента должен быть один исходящий поток управления | Пользовательская задача | У пользовательской задачи отсутствует исходящий поток или несколько исходящих потоков | Подсоедините только один исходящий поток к пользовательской задаче |
| У этого элемента нет потоков управления или к нему невозможно перейти из начального с события | Пользовательская задача | У пользовательской задачи отсутствует входящий поток или ни входящий поток не соединён с начальным событием | Подсоедините к пользовательской задаче входящий поток, соединённый с начальным событием напрямую или через другие элементы |
| Пользовательская задача должна иметь минимум одного ответственного | Пользовательская задача | В свойствах пользовательской задачи не указан исполнитель данной задачи | В свойствах пользовательской задачи выберите исполнителей на вкладке «Дополнительные» |
| Необходимо указать исходящий поток управления «иначе» | Развилка «или/или» | В свойствах развилки «или/или» не указан поток «иначе» | В свойствах развилки укажите указать один поток «иначе» на вкладке «Дополнительные» в соответствии с логикой процесса. |
| У этого элемента нет потоков управления или к нему невозможно перейти из начального с события | Развилка «или/или» | У развилки «или/или» отсутствует входящий поток или ни один входящий поток не соединён с начальным событием | Подсоедините к развилке «или/или» входящий поток, соединённый с начальным событием напрямую или через другие элементы |
| Необходим хотя бы один входящий поток | Развилка «или/или» | У развилки «или/или» отсутствует входящий поток | Подсоедините входящий поток к развилке «или/или» |
| Недопустимое определение потока управления | Развилка «или/или» | У развилки «или/или» несколько исходящих потоков, но не указан поток «иначе» или не задано условие для одного из исходящих потоков | В свойствах развилки «или/или» на вкладке «Дополнительные» укажите поток «иначе» и настройте условия для всех остальных потоков |
| В событии-таймере не настроен таймер | Промежуточное событие-таймер | В свойствах промежуточного события-таймера не задан интервал | В промежуточного свойствах события-таймера настройте интервал таймера на вкладке «Дополнительные» |
| Необходим хотя бы один входящий поток управления | Промежуточное событие | У промежуточного события отсутствует входящий поток | Добавить входящий поток промежуточному событию |
| У этого элемента должен быть один исходящий поток управления | Промежуточное событие | У промежуточного события отсутствует исходящий поток или несколько исходящих потоков | Добавить исходящий поток промежуточному событию |
| В начальном событии не настроен таймер | Начальное событие-таймер | В свойствах начального события-таймера не настроен таймер | В свойствах начального события-таймера настройте таймер на вкладке «Дополнительные» |
| Поток управления не соединен с конечной точкой | Поток управления | Поток управления не соединен с целевым элементом | Соедините поток управления с целевым элементом диаграммы |

--8<-- "related_topics_heading.md"

**[Элементы диаграммы процесса][process_diagram_elements]**

**[Стартовая форма и форма пользовательской задачи][process_diagram_forms]**

**[Проверка диаграммы процесса](https://kb.comindware.ru/article.php?id=2357)**

**[Использование диаграммы экземпляра процесса][process_diagram_view_instance]**

**[Управление версиями диаграммы процесса][process_diagram_version_control]**

**[Диаграммы в приложении][diagrams]**

**[Шаблон процесса][process_templates]**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
