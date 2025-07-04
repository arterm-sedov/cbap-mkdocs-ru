---
title: 'Записи и коллекции. Выборка элементов из списка по условию с помощью N3'
kbTitle: 'Записи и коллекции. Выборка элементов из списка по условию с помощью N3'
tags:
    - N3
    - Notation 3
    - Notation3
    - RDF
    - атрибут тип «Запись»
    - вычисление
    - вычисляемый атрибут
    - выборка
    - выборка по критериям
    - выборка по условию
    - исключение элементов
    - коллекция
    - коллекции
    - список
    - триплеты
    - тройка
    - тройки
    - фильтрация
    - фильтрация коллекции
    - процессы
    - запись
hide:
    - tags
kbId: 5106
---

# Записи и коллекции. Выборка элементов по условию с помощью N3 {: #n3_collection_select_conditional }

## Введение {: #n3_collection_select_conditional_intro }

**{{ productName }}** позволяет осуществлять выборку из данных списков (коллекций) по определённым условиям.

Это может быть полезно, когда требуется выбрать из набора данных элементы, соответствующие заданным критериям.

Здесь приведён пример вычисления списка позиций заказа, которые ещё не поступили на склад.

## Прикладная задача {: #n3_collection_select_conditional_use_case }

В бизнес-процессе обработки заказов необходимо реализовать следующий сценарий:

- Пользователь видит список всех доступных позиций (например, товары и услуги).
- Пользователь добавляет требуемые позиции в заказ.
- В списке для выбора требуется показывать пользователю только позиции, которые ещё не добавлены в заказ.

## Исходные данные {: #n3_collection_select_conditional_initial_data }

Имеется два шаблона записей: _«Заказы»_ и _«Позиции»_.

В шаблоне _«Заказы»_ имеются атрибуты _«Все позиции»_, _«Позиции заказа»_ и _«Доступные позиции»_ со следующими свойствами:

- **Тип данных: запись**
- **Связанный шаблон:** _Позиции_
- **Хранить несколько значений:** флажок установлен

## Настройка вычислений {: #n3_collection_select_conditional_configure }

1. В свойствах атрибута _«Все позиции»_ установите флажок «**Вычислять автоматически**» и введите **вычисляемое значение** в виде **формулы**:

    ``` sql
    from a in db->Позиции select a->id
    ```

2. В свойствах атрибута  _«Доступные позиции»_ установите флажок «**Вычислять автоматически**» и введите **вычисляемое значение** на **N3**:

    ```turtle
    # Импортируем функции для работы
    # с атрибутами, списками и системные функции
    @prefix object: <http://comindware.com/ontology/object#>.
    @prefix list: <http://www.w3.org/2000/10/swap/list#>.
    @prefix assert: <http://comindware.com/logics/assert#>.
    {
        # Получаем атрибут «Все позиции».
        ("Заказ" "Всепозиции") object:findProperty ?allArticlesAttribute.
        # Получаем атрибут «Позиции заказа».
        ("Заказ" "Позициизаказа") object:findProperty ?orderArticlesAttribute.

        # Для каждой позиции проверяем,
        # добавлена ли она уже на склад.
        from {
            # Получаем список всех имеющихся позиций.
            ?item ?allArticlesAttribute ?article.
            {
                # Проверяем, заказана ли позиция.
                ?item ?orderArticlesAttribute ?orderArticle.
                ?orderArticle == ?article.
            }
            assert:count ?orderedQuantity.
            # Если позиция не заказана (?orderedQuantity == 0),
            # она считается доступной.
            ?orderedQuantity == 0.
        } select ?article -> ?availableArticlesList.
        # Возвращаем список доступных позиций.
        ?availableArticlesList list:member ?value.
    }
    ```

3. Поместите атрибуты _«Все позиции»_, _«Позиции заказа»_ и _«Доступные позиции»_ на форму шаблона _«Заказы»_ и выберите для них **представление** «**Таблица**».
4. Для таблицы _«Позиции заказа»_ добавьте кнопку «**Добавить**» и в раскрывающемся списке «**Добавляемые записи**» укажите атрибут _«Доступные позиции»_.

## Тестирование {: #n3_collection_select_conditional_test }

1. Создайте несколько _позиций_.
2. Создайте _заказ_ и добавьте в него любую позицию.
3. Добавленная позиция должна пропасть из таблицы _«Доступные позиции»_.
4. Добавьте в заказ ещё одну позицию, в списке должны отображаться только _доступные позиции_.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Таблицы. Определения и настройка][table_configure]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
