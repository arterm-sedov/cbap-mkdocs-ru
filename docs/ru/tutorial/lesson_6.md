---
title: Урок 6. Усовершенствованный процесс
kbId: 4870
---

# Урок 6. Усовершенствованный процесс {: #lesson_6 }

## Введение

В ходе этого урока вы усовершенствуете процесс заказа автомобиля, использовав реестры (шаблоны записей) типов автомобилей, автомобилей, затрат и типов затрат, созданные в предыдущей главе, — настроите учёт машин в гараже, а также добавите возможность выбора типа машины из справочника.

**Предусловия:** пройдены [Урок 5. Структуры данных][lesson_5].

**Расчётная продолжительность:** 20 мин.

{% include-markdown ".snippets/tutorial_version_notice.md" %}

## Выбор типа автомобиля при создании заявки

Добавим возможность выбора типа автомобиля для Заказчика при создании заявки.

Для этого настроим основную экранную форму заявки…

1. Перейдите к шаблону _«Заявки на автомобили»_ и выберите вкладку «**Формы**».
2. Откройте конструктор формы _«Заявки на автомобили — Основная форма»_.
3. Перетащите на макет формы атрибут _«Тип автомобиля»_.
4. Нажмите кнопку «**Сохранить**».

_![Добавление атрибута «Тип автомобиля» на форму заявки на автомобиль](https://kb.comindware.ru/assets/img_6243638b64bb5.png)_

## Выбор автомобиля для выполнения рейса

Настроим форму для задачи _«Принять заявку»_, чтобы сотрудник гаража мог выбрать машину для выполнения рейса…

1. Перейдите к диаграмме бизнес-процесса _«Заказ автотранспорта»_ и нажмите кнопку «**Редактировать**».
2. Выберите задачу _«Принять заявку»_ и в меню элемента нажмите кнопку «**Форма**».

    _![Переход к настройке формы задачи «Принять заявку» на диаграмме бизнес-процесса](https://kb.comindware.ru/assets/img_6311c2bd7100c.png)_

3. Разверните атрибут _«Заявки на автомобили»_ на панели элементов и перетащите ссылку _«Автомобиль»_ на область _«Принятие заявки»_.
4. Укажите для поля _«Автомобиль»_ **режим доступа** «**Требовать ввод**» и сохраните форму.

    _![Добавление атрибута-записи «Автомобиль» на форму задачи «Принять заявку»](https://kb.comindware.ru/assets/img_6243655bcc67c.png)_

## Учет затрат во время выполнения рейса

Добавим на форму задачи _«Выполнить рейс»_ раскрывающийся список _«Автомобиль»_ и таблицу _«Затраты»_, чтобы сотрудник гаража видел номерной знак заказанного автомобиля, а также мог добавить новый автомобиль в список и вести учет затрат…

1. На диаграмме процесса выберите задачу _«Выполнить рейс»_ и с помощью меню элемента перейдите к ее форме.
2. Разверните элемент _«Заявки на автомобили»_
3. Перетащите атрибут _«Автомобиль»_ на область _«Выполнить рейс»._
4. Перетащите атрибут _«Затраты»_ на область _«Выполнить рейс»._
5. В панели свойств для поля _«Затраты»_ выберите **представление**«**Таблица**».

    _![Добавление на форму задачи «Выполнить рейс» раскрывающегося списка «Автомобиль» и таблицы «Затраты»](https://kb.comindware.ru/assets/img_62436844c3a8e.png)_

6. Разверните атрибут _«Затраты»_ на панели элементов и перетащите атрибуты: _«Тип затрат»_ и _«Сумма»_ в таблицу _«Затраты» на форме._
7. Выберите **область кнопок** таблицы _«Затраты»_ и перетащите на нее из панели элементов кнопки «**Создать**», «**Редактировать**» и «**Перейти**». Это позволит создавать, редактировать и просматривать записи о затратах из таблицы _«Затраты»_ на форме.

    _![Добавление в таблицу на форме задачи «Выполнить рейс» атрибутов записи «Затраты»](https://kb.comindware.ru/assets/img_62436a3154517.png)_

8. Добавим в реестр _«Заявки на автомобили»_ атрибут с итоговой суммой затрат…
9. Нажмите кнопку «**Добавить атрибут**» у атрибута _«Заявки на автомобили»_ в панели элементов.
10. Создайте атрибут _«Итоговая сумма затрат»_ числового типа, с отображением 2 **знаков после запятой**.

    _![Добавление числового атрибута в шаблон «Заявки на автомобили»](https://kb.comindware.ru/assets/img_6311c609a66c7.png)_

10. Перетащите атрибут _«Итоговая сумма затрат»_ на область _«Выполнить рейс»_ под таблицу _«Затраты»_.
11. Сохраните форму задачи _«Выполнить рейс»_.
12. Вернитесь к диаграмме бизнес-процесса и опубликуйте ее.

!!! note "Примечание"

    Изменения, внесенные в диаграмму бизнес-процесса, вступят в силу только после ее публикации.

    При публикации создаётся новая версия диаграммы. Экземпляр процесса, запущенный по старой версии диаграммы процесса, дорабатывает до конца по этой версии. Новые экземпляры запускаются по новой версии.

## Тестирование

1. Перейдите на вкладку «**Свойства**» шаблона процесса и нажмите кнопку «**Перейти к экземплярам**».
2. В списке экземпляров процесса запустите новый процесс, нажав кнопку «**Создать**».
3. Заполните поля стартовой формы и укажите тип автомобиля. Нажмите кнопку «**Создать**».
4. Перейдите в раздел «**Мои задачи**» с помощью панели навигации слева.
5. Откройте задачу _«Заказ автотранспорта — Рассмотреть заявку»_ и установите флажок _«Заявка одобрена»._
6. Завершите задачу.
7. Вернитесь в раздел «**Мои задачи**» и откройте задачу _«Заказ автотранспорта — Принять заявку»._
8. В поле _«Автомобиль»_ выберите автомобиль из раскрывающегося списка.
9. Укажите _«Принято» — «Да»_ и завершите задачу.
10. Вернитесь в раздел «**Мои задачи**» и откройте задачу _«Выполнить рейс»._
11. Нажмите кнопку «**Создать**» в таблице _«Затраты»_. Укажите сумму и тип затрат в таблице и нажмите кнопку «**Сохранить**».
12. Добавьте еще несколько записей в коллекцию затрат.
13. Завершите задачу.

## Добавление мастер-данных на лету

Настроим возможность ввода данных нового автомобиля сотрудником гаража при выполнении рейса…

1. Вернитесь к диаграмме бизнес-процесса и нажмите кнопку «**Редактировать**».
2. Перейдите к форме задачи _«Выполнить рейс»._
3. Выберите поле _«Автомобиль»_ на форме и в ее свойствах установите флажок «**Создание записей**».
4. Укажите **форму** для создания записей — _«Автомобиль — Основная форма»._

    _![Настройка атрибута «Автомобиль» для создания записей на лету](https://kb.comindware.ru/assets/img_62436fdbdf697.png)_

5. Сохраните форму и опубликуйте диаграмму бизнес-процесса.

!!! note "Примечание"

    Флажок «**Создание записей**» в свойствах раскрывающегося списка означает возможность создавать записи с помощью формы связанного шаблона.

    Когда этот флажок установлен для поля _«Автомобиль»_, сотрудник гаража сможет добавить новый автомобиль «на лету».

Протестируем добавление нового автомобиля…

1. Запустите процесс и пройдите его до задачи _«Выполнить рейс»._
2. Нажмите кнопку «**Создать**» в поле _«Автомобиль»._

    _![Создание автомобиля по ссылке](https://kb.comindware.ru/assets/img_6311ca66b0f71.png)_

3. Заполните поля отобразившейся формы и сохраните ее.
4. Завершите задачу.

## Результаты

В ходе этого урока мы настроили формы задач для сотрудника гаража, настроили возможность выбора типа автомобиля и протестировали усовершенствованный процесс.

В [следующем уроке][lesson_7] вы настроите автоматическое вычисление номера, статуса заявки и итоговой суммы затрат, а также фильтрацию при выборе типа автомобиля.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}