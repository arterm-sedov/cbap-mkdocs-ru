# Пример: JOIN из нескольких шаблонов и фильтры с помощью предикатов storage: {: #n3_example_join }

ЭКСПЕРИМЕНТАЛЬНАЯ ФУНКЦИЯ. НЕ ИСПОЛЬЗОВАТЬ И НЕ ПУБЛИКОВАТЬ В ДОКУМЕНТАЦИИ

Здесь показано, как при помощи предикатов `storage:` собрать SQL‑подобный запрос: собрать атрибуты, выполнить несколько JOIN, применить фильтры и получить результаты в переменную `?item`.

``` turtle
# Импортируем необходимые предикаты
# для обработки SQL-подобных запросов
# и работы с шаблонами и записями
@prefix object: http://comindware.com/ontology/object#.
@prefix storage: http://comindware.com/ontology/logics/storage#.
@prefix container: http://comindware.com/ontology/container#.
@prefix cmw: http://comindware.com/logics#.
{

    # Получаем атрибуты шаблонов записей по их системным именам
    # Здесь используются атрибуты типа «Запись», которые хранят ID записей
    # Атрибут хранится как таблица из двух столбцов: subject, object
    # Субъект — это ID атрибута, а объект — значение атрибута
    # ?schPodr — атрибут Scheta.Podrazdelenie
    # ?schPodr.subject — ID атрибута Scheta.Podrazdelenie
    # ?schPodr.object — значение атрибута Scheta.Podrazdelenie
    ("Scheta" "Podrazdelenie") object:findProperty ?schPodr.
    # ?podrDept — атрибут Podrazdeleniya.Departament
    ("Podrazdeleniya" "Departament") object:findProperty ?podrDept.
    # ?deptRepType — атрибут Departamenty.Vidyatschetadepartamenta
    ("Departamenty" "Vidyatschetadepartamenta") object:findProperty ?deptRepType.

    # ?xDept — атрибут X.Departament
    ("X" "Departament") object:findProperty ?xDept.
    # Текущий пользователь/контекст для WHERE
    cmw:securityContext cmw:currentUser ?value.
    
    # Собираем запрос в переменную ?query
    (
        # Выбираем ID атрибута schPodr — его subject
        # Эквивалент SELECT schPodr.subject
        ?schPodr storage:subject

        # Источники данных и предложения JOIN
        # FROM Scheta.Podrazdelenie
        # JOIN Podrazdeleniya.Departament ON Scheta.Podrazdelenie.object = Podrazdeleniya.Departament.subject
        # JOIN Departamenty.Vidyatschetadepartamenta ON Podrazdeleniya.Departament.object = Departamenty.Vidyatschetadepartamenta.subject
        # JOIN X.Departament ON Scheta.Podrazdelenie.object = X.Departament.subject
        # LEFT JOIN cmw:isDisabled ON Scheta.Podrazdelenie.subject = isDisabled.subject
        (
            ?schPodr 
            # schPodr.object = podrDept.subject
            storage:join ?podrDept (?schPodr storage:object storage:eq ?podrDept storage:subject)
            # podrDept.object = deptRepType.subject
            storage:join ?deptRepType (?podrDept storage:object storage:eq ?deptRepType storage:subject)
            # schPodr.object = xDept.subject
            storage:join ?xDept  (?schPodr storage:object storage:eq ?xDept  storage:subject)
            # Левое соединение: берём строки без/с признаком «отключено», чтобы потом отфильтровать только включённые
            storage:left_join cmw:isDisabled (?schPodr storage:subject storage:eq cmw:isDisabled storage:subject)
        )

        # Условия отбора (WHERE)
        # Значение атрибута ?deptRepType равно текущему пользователю (?value)
        # Значение атрибута ?xDept больше внешней переменной ?xValue
        # Исключаем записи, у которых cmw:isDisabled = true
        (
            # deptRepType.object = ?value
            (?deptRepType storage:object storage:eq ?value)
            # xDept.object > ?xValue
            storage:and (?xDept storage:object storage:gt ?xValue)
            storage:andNot (
                # Имеется значение isDisabled
                (cmw:isDisabled storage:object storage:isNotNull)
                # и оно равно true, тогда исключаем
                storage:and (cmw:isDisabled storage:object storage:eq true)
            )
        )
    ) -> ?query.

    # Выполняем запрос, помещаем итератор с результатами в ?item
    ?query storage:query ?item.
}
```

Коротко: рассматриваем каждый атрибут (schPodr, podrDept, deptRepType) как таблицу из двух столбцов `(subject, object)` и соединяем их по равенствам «subject/object», используя предикаты `storage:join`, `storage:left_join`, а также применяя условия: `storage:eq`, `storage:gt`, `storage:and`, `storage:andNot`.

Эквивалент на SQL:

``` sql
SELECT schPodr.subject
FROM schPodr
JOIN podrDept ON schPodr.object = podrDept.subject
JOIN deptRepType ON podrDept.object = deptRepType.subject
JOIN xDept  ON schPodr.object = xDept.subject
LEFT JOIN isDisabled ON schPodr.subject = isDisabled.subject
WHERE deptRepType.object = :currentUser
  AND xDept.object > :xValue
  AND NOT (isDisabled.object IS NOT NULL AND isDisabled.object = true);
```

Замечания и практические советы:

- Располагайте более избирательные условия выше по списку — это уменьшает «раскладку» итератора и ускоряет вычисление.
- Используйте `storage:left_join` только при необходимости сохранения строк без связанного значения (как в примере — чтобы затем исключить отключённые записи через отрицание условия).
- Переменная `?xValue` ожидается из внешнего контекста выражения (например, из параметров/переменных сценария).
