---
title: Автонумерация записей с пересчётом при удалении
kbId: 5092
---

# Автонумерация записей с пересчётом при удалении

## Введение

В **{{ productName }}** каждой записи, пользовательской задаче, форме, экземпляру процесса и любому объекту присваиваются уникальный ID. В рамках одного экземпляра **{{ productName }}** ID не повторяются. После удаления объекта его ID не используется повторно. Кроме того, ID записей имеют сквозную нумерацию для всех шаблонов и приложений, не являются наглядными и малоинформативны для бизнеса.

При этом в приложениях зачастую требуется присваивать записям наглядные номера или коды и пересчитывать их при создании и удалении записей.

Здесь представлен пример настройки сценария для автонумерации записей из связанного шаблона с пересчётом номеров при их удалении.

Примеры настройки автонумерации записей при их создании см. в статье *«[Автонумерация записей с помощью формулы, C#-скрипта или выражения N3][auto_numerating_records]»*.

## Прикладная задача

Имеется шаблоны *«Заявки»* и *«Реестр документов»*.

Каждая заявка связана с записями о расходах из *реестра документов*.

Требуется настроить автонумерацию записей в *Реестре документов* с использованием кодов вида: `Док. <N> по заявке <requestNumber>.`, где `<N>` — порядковый номер документа, а `<requestNumber>` — номер заявки.

При этом для каждой *Заявки* нумерация записей из *Реестра документов* должна начинаться заново.

При удалении записи из *Реестра документов*, нумерация должна пересчитываться.

## Исходные данные

Имеются шаблон *«Заявки»* и *«Реестр документов»*.

В шаблоне *«Заявки»* имеются атрибуты:

- *Номер заявки*:

  - **Тип данных: текст**
  - **Системное имя:** `Номерзаявки`

  Совет

  В этом примере не рассматривается формирование *Номера заявки*.

  Для этого можно воспользоваться приёмами из статьи *«[Автонумерация записей с помощью формулы, C#-скрипта или выражения N3][auto_numerating_records]»*
- *Документы о расходах*:

  - **Тип данных: запись**
  - **Связанный шаблон:** *Реестр документов*
  - **Системное имя:** *Documents*
  - **Хранить несколько значений:** флажок установлен

В шаблоне *«Реестр документов»* имеется атрибут *«Код документа»* типа «**Текст**»;

На форму шаблона *«Заявки»* вынесен атрибут *«Документы»* с представлением в виде **таблицы**.

В таблицу *«Документы»* добавлены столбцы *«ID»* и *«Код документа»*.

На область кнопок таблицы *«Документы»* помещены кнопки «**Создать**» и «**Удалить**».

## Настройка автонумерации связанных записей

1. Создайте новый сценарий *«Автонумерация»*.
2. Настройте начальное событие «**Нажата кнопка**»:

   - **Контекстный шаблон:** *Заявки*
   - **Кнопка: Сохранить**
3. Добавьте действие «**Проверить результат выражения**» со следующими свойствами:

   - **Выражение: N3**

     ```
     # Импортируем функции для работы
     # с записями, строками, базой данных и переменными
     @prefix object: <http://comindware.com/ontology/object#>.
     @prefix variable: <http://comindware.com/ontology/session/variable#>.
     @prefix operator: <http://comindware.com/ontology/session/operator#>.
     {
         # Создаём переменную-индекс и
         # задаём ей значение 0
         variable:index operator:replace 0.
         # Создаём переменную requestNumber
         # и присваиваем ей номер заявки
         ("Заявки" "Номерзаявки") object:findProperty ?requestNumberAttribute.
         ?item ?requestNumberAttribute ?requestNumberAttributeValue.
         variable:requestNumber operator:replace ?requestNumberAttributeValue.

         # Возвращаем true, чтобы сценарий выполнялся далее
         true -> ?value.
     }
     ```
4. Добавьте действие «**Сменить контекст**» со следующими свойствами:

   - **Целевой шаблон записи:** *Реестр документов*
   - **Атрибут или выражения для поиска объектов: формула**

     ```
     # Собираем ID всех записей,
     # связанных с атрибутом Documents (Документы о расходах)
     from a in $Documents select a->id
     ```
5. Добавьте действие «**Изменить значения атрибутов**» внутрь действия «**Сменить контекст**» со следующими свойствами:

   - **Атрибут:** *Код документа*
   - **Действие: заменить**
   - **Значение: N3**

     ```
     # Импортируем функции для работы с переменными, строками и числами
     @prefix variable: <http://comindware.com/ontology/session/variable#>.
     @prefix operator: <http://comindware.com/ontology/session/operator#>.
     @prefix session: <http://comindware.com/ontology/session#>.
     @prefix string: <http://www.w3.org/2000/10/swap/string#>.
     @prefix math: <http://www.w3.org/2000/10/swap/math#>.
     {
         # Находим переменную index и помещаем
         # её в ?startValue
         session:context variable:index ?startValue.
         # Увеличиваем значение ?startValue на 1
         # и помещаем результат в ?newIndex
         (?startValue 1) math:sum ?newIndex.
         # Находим переменную requestNumber и помещаем
         # её в ?requestNumberValue
         session:context variable:requestNumber ?requestNumberValue.
         # Приводим значение ?newIndex к типу данных «Текст»
         # и помещаем в ?codeFormatted вместе с ?requestNumberValue
         ("Док. {0} по заявке {1}" ?newIndex ?requestNumberValue) string:format ?codeFormatted.
         # Заменяем значение переменной индекс
         # на значение ?newIndex
         variable:index operator:replace ?newIndex.
         # Возвращаем в значение атрибута ?codeFormatted
         ?codeFormatted -> ?value.
     }
     ```

## Тестирование

1. Создайте запись в шаблоне *«Заявки»*.
2. В форме заявки создайте несколько записей в таблице *«Документы о расходах»*.
3. Сохраните заявку.
4. В столбце *«Код документа»* отобразятся нумерация записей, а в столбце *«ID»* — их системные номера.
5. Удалите одну или несколько записей в таблице *«Документы о расходах»*.
6. Сохраните заявку.
7. Номера в столбце *«Код документа»* обновятся, а их ID останутся неизменными.

--8<-- "related_topics_heading.md"

- *[Автонумерация записей с помощью формулы, C#-скрипта или выражения N3][auto_numerating_records]*
- *[Переменные приложения. Просмотр списка, настройка и использование][variables]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
