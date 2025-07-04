---
title: Вычисляемые атрибуты
kbId: 4770
---

# Вычисляемые атрибуты

## Определения

- Значение атрибута может вычисляться по формуле, выражению на языке N3, таблице DMN или атрибуту.
- Вычисляемыми могут быть атрибуты следующих типов:
  - [Аккаунт][attribute_account]
  - [Гиперссылка][attribute_hyperlink]
  - [Дата и время][attribute_date_time]
  - [Длительность][attribute_duration]
  - [Запись][attribute_record]
  - [Логический][attribute_boolean]
  - [Организационная единица][attribute_organizational_unit]
  - [Роль][attribute_role]
  - [Атрибут типа «Список значений»][attribute_enum]
  - [Текст][attribute_text]
  - [Число][attribute_number]
- Значение вычисляемого атрибута не хранится в базе данных и недоступно для изменения конечным пользователем приложения.
- Значение вычисляется в момент отображения в интерфейсе пользователя и при обращении к нему.
- Изменения значения вычисляемого атрибута не записываются в журнал.
- Вычисляемый атрибут нельзя использовать для поиска записей.

## Настройка выражения для вычисления значения атрибута

Внимание!

После преобразования атрибута в вычисляемый его имеющиеся значения во всех записях будут безвозвратно удалены.

Примечание

- Вычисляемое выражение должно возвращать результат, соответствующий [типу атрибута][attributes].
- Если снять флажок «**Вычислять по выражению**» и сохранить атрибут, то атрибут перестанет быть вычисляемым и выражение для вычисления значения будет утрачено.

1. Установите флажок «**Вычислять по выражению**» в [свойствах атрибута][attributes].
2. В отобразившемся поле «**Вычисляемое значение**» выберите способ вычисления значения: «**Формула**», «**DMN**», «**N3**» или «**Атрибут**».

   ![Поле «Вычисляемое значение»](/platform/v5.0/business_apps/templates/attributes/img/calculated_attribute_calculated_expression.png)

   Поле «Вычисляемое значение»
3. Нажмите поле «**Вычисляемое значение**».
4. Введите выражение в компактном редакторе выражений или выберите атрибут с помощью селектора.

   ![Компактный редактор выражений](/platform/v5.0/business_apps/templates/attributes/img/calculated_attribute_compact_editor.png)

   Компактный редактор выражений

   ![Селектор атрибута](/platform/v5.0/business_apps/templates/attributes/img/calculated_attribute_select_attribute.png)

   Селектор атрибута
5. Чтобы сохранить выражение в компактном редакторе, нажмите кнопку с зеленым флажком.
6. Чтобы изменить выражение в полном редакторе, нажмите кнопку «**Открыть в редакторе**».

_![Полный редактор выражений](/platform/v5.0/business_apps/templates/attributes/img/calculated_attribute_full_editor.png)_

## Примеры вычислений

См. подробные описание формул и языка N3 с примерами:

- [Руководстве по языку формул](https://kb.comindware.ru/category.php?id=880)
- [Руководстве по языку N3](https://kb.comindware.ru/category.php?id=877)
- [Примеры использования формул](https://kb.comindware.ru/category.php?id=881)
- [Примеры использования языка N3](https://kb.comindware.ru/category.php?id=879)

--8<-- "related_topics_heading.md"

- *[Атрибуты. Определения, типы, настройка, архивирование, удаление][attributes]*
- *[Руководстве по языку формул](https://kb.comindware.ru/category.php?id=880)*
- *[Руководстве по языку N3](https://kb.comindware.ru/category.php?id=877)*
- *[Примеры использования формул](https://kb.comindware.ru/category.php?id=881)*
- *[Примеры использования языка N3](https://kb.comindware.ru/category.php?id=879)*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
