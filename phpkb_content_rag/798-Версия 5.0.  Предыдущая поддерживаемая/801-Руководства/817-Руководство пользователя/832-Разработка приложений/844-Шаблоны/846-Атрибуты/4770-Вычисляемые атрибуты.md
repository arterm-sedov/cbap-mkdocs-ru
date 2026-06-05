---
title: 'Вычисляемые атрибуты'
kbId: 4770
url: 'https://kb.comindware.ru/article.php?id=4770'
updated: '2025-04-01 16:19:51'
---

# Вычисляемые атрибуты

## Определения

- Значение атрибута может вычисляться по формуле, выражению на языке N3, таблице DMN или атрибуту.
- Вычисляемыми могут быть атрибуты следующих типов:
  - [Аккаунт](https://kb.comindware.ru/article.php?id=4774)
  - [Гиперссылка](https://kb.comindware.ru/article.php?id=4766)
  - [Дата и время](https://kb.comindware.ru/article.php?id=4777)
  - [Длительность](https://kb.comindware.ru/article.php?id=4775)
  - [Запись](https://kb.comindware.ru/article.php?id=4780)
  - [Логический](https://kb.comindware.ru/article.php?id=4778)
  - [Организационная единица](https://kb.comindware.ru/article.php?id=4767)
  - [Роль](https://kb.comindware.ru/article.php?id=4783)
  - [Атрибут типа «Список значений»](https://kb.comindware.ru/article.php?id=4779)
  - [Текст](https://kb.comindware.ru/article.php?id=4768)
  - [Число](https://kb.comindware.ru/article.php?id=4773)
- Значение вычисляемого атрибута не хранится в базе данных и недоступно для изменения конечным пользователем приложения.
- Значение вычисляется в момент отображения в интерфейсе пользователя и при обращении к нему.
- Изменения значения вычисляемого атрибута не записываются в журнал.
- Вычисляемый атрибут нельзя использовать для поиска записей.

## Настройка выражения для вычисления значения атрибута

Внимание!

После преобразования атрибута в вычисляемый его имеющиеся значения во всех записях будут безвозвратно удалены.

Примечание

- Вычисляемое выражение должно возвращать результат, соответствующий [типу атрибута](https://kb.comindware.ru/article.php?id=4772).
- Если снять флажок «**Вычислять по выражению**» и сохранить атрибут, то атрибут перестанет быть вычисляемым и выражение для вычисления значения будет утрачено.

1. Установите флажок «**Вычислять по выражению**» в [свойствах атрибута](https://kb.comindware.ru/article.php?id=4772#attributes_configure).
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

## Связанные статьи

- *[Атрибуты. Определения, типы, настройка, архивирование, удаление](https://kb.comindware.ru/article.php?id=4772)*
- *[Руководстве по языку формул](https://kb.comindware.ru/category.php?id=880)*
- *[Руководстве по языку N3](https://kb.comindware.ru/category.php?id=877)*
- *[Примеры использования формул](https://kb.comindware.ru/category.php?id=881)*
- *[Примеры использования языка N3](https://kb.comindware.ru/category.php?id=879)*