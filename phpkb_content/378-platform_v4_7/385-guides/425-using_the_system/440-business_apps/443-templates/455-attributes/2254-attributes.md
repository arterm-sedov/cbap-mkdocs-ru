---
title: 'Вычисляемые атрибуты'
kbId: 2254
url: 'https://kb.comindware.ru/article.php?id=2254'
updated: '2024-07-01 13:38:50'
---

# Вычисляемые атрибуты

### Определения

Значение атрибута может вычисляться по формуле, выражению на языке N3, таблице DMN или атрибуту.

Вычисляемыми могут быть атрибуты следующих типов:

- [Аккаунт](https://kb.comindware.ru/article.php?id=2249)
- [Гиперссылка](https://kb.comindware.ru/article.php?id=2259)
- [Дата и время](https://kb.comindware.ru/article.php?id=2246)
- [Длительность](https://kb.comindware.ru/article.php?id=2248)
- [Запись](https://kb.comindware.ru/article.php?id=2243)
- [Логический](https://kb.comindware.ru/article.php?id=2245)
- [Организационная единица](https://kb.comindware.ru/article.php?id=2258)
- [Роль](https://kb.comindware.ru/article.php?id=2240)
- [Атрибут типа «Список значений»](https://kb.comindware.ru/article.php?id=2244)
- [Текст](https://kb.comindware.ru/article.php?id=2257)
- [Число](https://kb.comindware.ru/article.php?id=2251)
- Значение вычисляемого атрибута не хранится в базе данных и недоступно для изменения конечным пользователем приложения.
- Значение вычисляется в момент отображения в интерфейсе пользователя и при обращении к нему.
- Изменения значения вычисляемого атрибута не записываются в журнал.
- Вычисляемый атрибут нельзя использовать для поиска записей.

## Настройка выражения для вычисления значения атрибута

Внимание!

После преобразования атрибута в вычисляемый его имеющиеся значения во всех записях будут безвозвратно удалены.

Примечание

- Вычисляемое выражение должно возвращать результат, соответствующий [типу атрибута](https://kb.comindware.ru/article.php?id=2252#mcetoc_1hpt0brfc0).
- Если снять флажок «**Вычислять по выражению**» и сохранить атрибут, то атрибут перестанет быть вычисляемым и выражение для вычисления значения будет утрачено.

1. Установите флажок «**Вычислять по выражению**» в [свойствах атрибута](https://kb.comindware.ru/article.php?id=2252#mcetoc_1gk3bvt3k0).
2. В отобразившемся поле «**Вычисляемое значение**» выберите способ вычисления значения: «**Формула**», «**DMN**», «**N3**» или «**Атрибут**».

_![Поле «Вычисляемое значение»](https://kb.comindware.ru/assets/calculated_attribute_calculated_expression.png)_

3. Нажмите поле «**Вычисляемое значение**».
4. Введите выражение в компактном редакторе выражений или выберите атрибут с помощью селектора.

_![Компактный редактор выражений](https://kb.comindware.ru/assets/calculated_attribute_compact_editor.png)_

_![Селектор атрибута](https://kb.comindware.ru/assets/calculated_attribute_select_attribute.png)_

5. Чтобы сохранить выражение в компактном редакторе, нажмите кнопку с зеленым флажком.
6. Чтобы изменить выражение в полном редакторе, нажмите кнопку «**Открыть в редакторе**».

_![Полный редактор выражений](https://kb.comindware.ru/assets/calculated_attribute_full_editor.png)_

Подробное описание формул и языка N3 с примерами см. в базе знаний Comindware:

- [Примеры использования формул](https://kb.comindware.ru/category/comindware-business-application-platform/Версия-4/Формулы-для-вычислений/Язык-выражений/409/)
- [Примеры использования языка N3](https://kb.comindware.ru/category/comindware-business-application-platform/Версия-4/Формулы-для-вычислений/Язык-n3/408/)

--8<-- "related_topics_heading.md"

**[Атрибуты. Определения, типы, настройка, архивирование, удаление](https://kb.comindware.ru/article.php?id=2252)**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
