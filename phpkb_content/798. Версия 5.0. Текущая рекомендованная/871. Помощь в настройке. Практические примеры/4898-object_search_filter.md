---
title: Расширенный поиск объекта по параметрам. Настройка шаблонов, фильтра и кнопки
kbId: 4898
---

# Расширенный поиск объекта по параметрам. Настройка шаблонов, фильтра и кнопки

Для выбора значения в атрибуте с типом данных «Запись» в выпадающем списке пользователю показывается отображаемый атрибут или ИД объекта целевого шаблона записи. В некоторых случаях этой информации недостаточно, и тогда в отображаемый атрибут можно вывести значения из нескольких атрибутов (см. статью [Объединение нескольких значений в одно](https://kb.comindware.ru/article.php?id=1666)).

Также на прикладном уровне можно настроить расширенный поиск объекта по параметрам. Для этого:

**1.** Создайте технический шаблон записи «*Поиск объектов*».

**2.** Создайте в нем атрибуты, по которым вы планируете искать объекты, например, «*Дата с*» и «*Дата по*».

**3.** Создайте атрибут с типом данных «Запись» и укажите шаблон записи, из которого вы планируете инициировать расширенный поиск.

**4.** В шаблоне записи «*Поиск объектов*» создайте форму «*Поиск*» и вынесите атрибуты для поиска, созданные в п. 2.

**5.** В шаблоне записи, из которого вы планируете инициировать расширенный поиск, создайте кнопку «*Расширенный поиск*» с операцией «*Создать связанную запись*» и выберите шаблон записи «*Поиск объектов*» по созданному в п. 3 атрибуту.

**6.** На форме «*Поиск*» из атрибута, раскройте атрибут, созданный в п. 3 атрибут и вынесите нужный атрибут для поиска, и напишите для него «*Фильтр*». Пример фильтра: *from a in db->Projects where AND(GREATER(a->DueDate,$DateFrom),LESS(a->DueDate,$DateTo))*

**7.** В исходном объекте рядом с атрибутом, по которому требуется поиск по расширенным параметрам, вынесите кнопку «*Расширенный поиск*».

**8.** При нажатии на кнопку должно открыться окно с формой «*Поиск*», с атрибутами для расширенного поиска и искомый атрибут с отфильтрованными значениями. Выберите нужное значение и при сохранении в исходной записи данное значение будет также сохранено.

**Примечание :** вы можете использовать данный шаблон для поиска объектов из разных шаблонов записей. Для этого необходимо создать нужное количество форм, атрибутов для поиска и создать разные кнопки для выбора нужных форм поиска.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
