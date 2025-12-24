
<!-- 
Перенести в следующие уроки

- `[]` — анонимные узлы 
Анонимный узел (когда имя ресурса несущественно):

``` turtle
ex:Position456 ex:requirement [ ex:skill "SQL" ].
```

Коллекция значений (упорядоченный список):

``` turtle
ex:Candidate123 ex:skills ("SQL" "Python" "ETL").
```

Присваивание с `=` используется для связывания значений переменных и термов внутри выражения, когда синтаксис поддерживается контекстом формы запроса. Подробнее: [Руководство по N3][n3_guide], [Нотация N3][n3_notation].

## Пять типов запросов и поведение интерпретатора {: #tutorial_n3_lesson_1_query_forms }

Интерпретатор выражений в **{{ productName }}** поддерживает пять форм (подробно — [Руководство по N3][n3_guide]):

1. Выбор значений (pattern‑match triples)
2. Присваивание/вычисление
3. Утверждение (assert)
4. Отрицание (not { ... })
5. Итерации и коллекции (`from { ... } select ...`)

Основные правила выполнения:

- Тройки в блоке конъюнктивны (по умолчанию AND).
- Выполнение останавливается при несоответствии (fan‑out ограничивается ложью).
- Более избирательные условия располагайте выше для эффективности.

## N‑Triples ↔ N3: соответствие и мини‑рефактор {: #tutorial_n3_lesson_1_ntriples_mapping }

Одна и та же семантика может быть записана как N‑Triples, так и N3.

N‑Triples (простая, построчная форма):

``` turtle
<http://example.com/hr#Candidate123> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/hr#Candidate> .
<http://example.com/hr#Candidate123> <http://example.com/hr#fullName> "Иван Петров" .
```

Эквивалент в N3/Turtle с префиксами и `a`:

``` turtle
@prefix ex: <http://example.com/hr#>.
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.

ex:Candidate123 a ex:Candidate;
    ex:fullName "Иван Петров".
```

Мини‑рефактор Formula → N3 (иллюстрация):

``` turtle
# Было (псевдокод формул)
# fullName = Candidate.name + " " + Candidate.surname

# Стало (N3‑идея):
{ ?candidate a ex:Candidate;
             ex:firstName ?first;
             ex:lastName ?last. }
=> { ?candidate ex:fullName ?full. }.

@prefix w3string: <http://www.w3.org/2000/10/swap/string#>.

{ (?first " " ?last) w3string:concatenation ?full. }
```

Примечание: используйте фактические предикаты и функции, доступные в **{{ productName }}**, см. каталоги и примеры в [Руководство по N3][n3_guide] и раздел «Примеры».

## Пример: от кандидата к отделу {: #tutorial_n3_lesson_1_example_hr }

Задача: находясь в контексте кандидата (`?item` — `ex:Candidate`), получить название отдела, в который открыта вакансия, на которую подаётся кандидат, и вернуть его в `?value`.

``` turtle
@prefix ex: <http://example.com/hr#>.

{ ?item a ex:Candidate;
        ex:appliesFor ?position.
  ?position ex:department ?dept.
  ?dept ex:name ?deptName. }
=> { ?value = ?deptName }.
```

2. Модифицируйте пример «кандидат → отдел», чтобы возвращать пару значений: название отдела и название позиции (подумайте о форме результата в вашем контексте).
3. Найдите в [примерах](#tutorial_n3_lesson_1_links) фрагмент с `from { } select` и объясните, чем отличается такой сбор коллекции от простого сопоставления троек.

!!! example "Отладка и производительность"
    - Сведите выражение к минимальной тройке, воспроизводящей проблему.
    - Переместите самые избирательные условия выше в блоке.
    - Применяйте `once {}` только там, где гарантирована единственность.

-->