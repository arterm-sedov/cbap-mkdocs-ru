---
title: 'Урок 2. Синтаксис N3, переменные и формы запросов'
kbTitle: 'Урок 2. Синтаксис N3, переменные и формы запросов'
kbId: 
tags:
    # Common tutorial_n3 tags
    - ElasticData
    - N3
    - Notation3
    - RDF
    - Turtle
    - выражения
    - разработка
    - обучение
    - платформа
    - триплеты
    - тройки
    - уроки
    - учебник
    # Lesson-specific tags
    - синтаксис
    - переменные
    - формы-запросов
    - HR
hide: tags
---

# Урок 2. Синтаксис N3, переменные и формы запросов {: #tutorial_n3_lesson_2 }

## Введение {: #tutorial_n3_lesson_2_intro }

В этом уроке мы расширим основы из [урока 1][tutorial_n3_lesson_1]: разберём варианты присвоения в триплетах, поведение интерпретатора (последовательность и конъюнкция), проверки пустоты, правила нейминга переменных и мини‑рефактор Формула → N3.

**Предусловия:** пройден [урок 1 «Введение в графовую СУБД и язык N3»][tutorial_n3_lesson_1].

**Расчётная продолжительность:** 1 час.

!!! warning "Бизнес-логика"

    Контекст примеров — HR (кандидаты, отделы, статусы). Синтаксис и паттерны универсальны и применимы в любых приложениях на **{{ productName }}**.

{% include-markdown ".snippets/tutorial_version_notice.md" %}

## Темы, навыки и задания урока {: #tutorial_n3_lesson_2_taxonomy }

### Темы {: #tutorial_n3_lesson_2_topics }

- Переменные и правила записи триплетов
- `?item` и `?value` в разных контекстах
- Пять форм/типов запросов и минимальные примеры
- Шорткаты: `a`, `[]`, `=`, оператор результата `->`
- Проверки пустоты и точного совпадения

### Навыки {: #tutorial_n3_lesson_2_skills }

- Корректно объявлять префиксы и переменные
- Составлять минимальные выражения для извлечения значений
- Применять пять форм присвоения и проверки совпадений
- Возвращать результат корректного типа через `-> ?value`

### Задания {: #tutorial_n3_lesson_2_tasks }

- Написать короткие выражения для навигации и получения значения
- Применить проверку на пустоту и точное совпадение
- Использовать платформенный `->` для возврата результата

<div class="admonition question" markdown="block">

## Определения {: .admonition-title #tutorial_n3_lesson_2_definitions}

- **Точное совпадение** — триплет, где заданы субъект, предикат и объект; используется для проверки «есть ли ровно такой факт».
- **Шорткаты** — синтаксические сокращения: `a` (rdf:type), `[]` (шаблон пустого узла), `=` (связывание/равенство).

</div>

## Именование переменных и типизация данных `?item`/`?value` {: #tutorial_n3_lesson_2_core }

- Переменные должны отражать смысл: `?candidate`, `?departmentCode`, а не `?x`, `?y`.
- Типы `?item`/`?value` зависят от контекста; подробности см. [урок 1][tutorial_n3_lesson_1] и [Справочник по N3][n3_guide_reference].
- Тип в `?value` обязан совпадать с типом атрибута‑приёмника (строка/число/логический/URI/список).

Пример: получить код отдела менеджера кандидата и вернуть строку (не повторяя материалы урока 1):

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
    ("Кандидаты" "Должность") object:findProperty ?positionAttr.
    ("Должности" "Название") object:findProperty ?titleAttr.

    ?item ?positionAttr ?position.
    ?position ?titleAttr ?title.
    ?title -> ?value.
}
```

## Пять форм присвоения и проверки (компактно) {: #tutorial_n3_lesson_2_query_forms }

Ниже — компактные варианты присвоения и проверки, опирающиеся на [Учебник по N3][n3_tutorial_original] и [Справочник по N3][n3_guide_reference].

1. Известны субъект и предикат — находим объект

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
    ("Кандидаты" "Отдел") object:findProperty ?deptAttr.
    ("Отделы" "Код") object:findProperty ?deptCodeAttr.

    ?item ?deptAttr ?dept.
    ?dept ?deptCodeAttr ?code.
    ?code -> ?value.
}
```

2. Известны предикат и объект — находим субъект

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
    ("Отделы" "Код") object:findProperty ?deptCodeAttr.
    ?dept ?deptCodeAttr "IT".
    ?dept -> ?value.
}
```

3. Точное совпадение: заданы все три части

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
    ("Кандидаты" "Статус") object:findProperty ?statusAttr.
    ("Статусы кандидата" "Код") object:findProperty ?statusCodeAttr.

    ?item ?statusAttr ?st.
    ?st ?statusCodeAttr "new".
    true -> ?value.
}
```

4. Проверка на пустоту значения

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
    ("Кандидаты" "Телефон") object:findProperty ?phoneAttr.
    not { ?item ?phoneAttr ?. }.
    true -> ?value.
}
```

5. Навигация по ссылке и возврат результата

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
    ("Кандидаты" "Менеджер") object:findProperty ?managerAttr.
    ("Сотрудники" "ФИО") object:findProperty ?fioAttr.

    ?item ?managerAttr ?m.
    ?m ?fioAttr ?fio.
    ?fio -> ?value.
}
```

## Шорткаты и платформенные особенности (без повторов) {: #tutorial_n3_lesson_2_shorthands }

- `a` эквивалентно `rdf:type` и используется для указания типа ресурса.
- `[]` позволяет сопоставлять «пустой узел» (анонимный ресурс) по шаблону.
- `=` — связывание/равенство для сопоставления значений.
- `->` — платформенный оператор возврата результата в `?value`.
- Импликация `=>` в стандартных выражениях платформы не используется.

Пример использования `a` для фильтрации задач пользователя см. в разделе [Дайджест примеров N3][n3_examples_digest].

## Интерпретатор: порядок и конъюнкция (AND) {: #tutorial_n3_lesson_2_interpreter }

- Триплеты выполняются сверху вниз; при `false` текущая ветка отбрасывается.
- Между триплетами по умолчанию — конъюнкция (логическое И). Условие считается истинным, если все триплеты ветки истинны.

Мини‑пример: оба поля даты пусты (истина только при пустоте обоих):

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
    ("Заявки" "ПланНачало") object:findProperty ?start.
    ("Заявки" "ПланОкончание") object:findProperty ?end.

    not { ?item ?start ?. }.
    not { ?item ?end  ?. }.
    true -> ?value.
}
```

## Мини‑рефактор: Формула → N3 {: #tutorial_n3_lesson_2_formula_to_n3 }

Простая формула: `=$IssueTypeRef->Title` эквивалентна выражению N3:

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
{
    ("Issue" "IssueType") object:findProperty ?issueTypeAttr.
    ("Type"  "Title")     object:findProperty ?titleAttr.

    ?item ?issueTypeAttr ?t.
    ?t    ?titleAttr     ?value.
}
```

## Ошибки и гигиена синтаксиса {: #tutorial_n3_lesson_2_hygiene }

- Проверяйте регистр имён переменных.
- Возвращайте значение совместимого типа: строка в текстовый атрибут, число в числовой и т.д.
- Повторное использование переменных должно быть осознанным.

## Практическое задание {: #tutorial_n3_lesson_2_practical_task }

Задача: в шаблоне _«Кандидаты»_ вычислить текстовый атрибут _«Строка визитки»_ в формате «ФИО — Отдел».

Подсказка: используйте `not { … ?. }` и точное совпадение; результат должен быть логическим (`true`/`false`). Для вывода строки воспользуйтесь `cmwstring:format`.

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
{
    ("Кандидаты" "Менеджер") object:findProperty ?managerAttr.
    ("Сотрудники" "ФИО") object:findProperty ?fioAttr.
    ("Сотрудники" "Отдел") object:findProperty ?deptAttr.
    ("Отделы" "Название") object:findProperty ?deptNameAttr.

    ?item ?managerAttr ?m.
    ?m ?fioAttr ?fio.
    ?m ?deptAttr ?d.
    ?d ?deptNameAttr ?deptName.

    ("{0} — {1}" ?fio ?deptName) cmwstring:format ?result.
    ?result -> ?value.
}
```

Проверьте работу выражения на нескольких записях.

## Итоги урока {: #tutorial_n3_lesson_2_summary }

Вы закрепили базовый синтаксис N3, проработали `?item`/`?value`, разобрали пять форм работы с триплетами, шорткаты и правила «гигиены» выражений. На практике вы построили несколько минимальных запросов и собрали результирующую строку для HR‑сценария.

В ходе [следующего урока][tutorial_n3_lesson_3] вы изучите префиксы, URI и поиск атрибутов, в том числе `object:findProperty` в глубину.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Справочник по N3][n3_guide_reference]
- [Учебник по N3][n3_tutorial_original]
- [Дайджест примеров N3][n3_examples_digest]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}


