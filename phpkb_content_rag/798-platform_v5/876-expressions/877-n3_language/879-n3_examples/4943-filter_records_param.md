---
title: 'Фильтр записей в коллекции по заданному параметру'
kbId: 4943
url: 'https://kb.comindware.ru/article.php?id=4943'
updated: '2026-06-20 18:06:09'
---

# Фильтр записей в коллекции по заданному параметру

Здесь приведён пример фильтрации записей в коллекции с помощью выражения N3 по параметру, заданному в текущей записи.

## Прикладная задача

Необходимо отобразить в коллекции только те адреса офисов, у которых область совпадает со значением, указанным в текущей записи организации.

## Модель данных

| Шаблон записи | Атрибут | Назначение |
| --- | --- | --- |
| `Organizatsii` | `Filtrpooblasti` — атрибут типа «**Текст**» | Хранит область, по которой требуется отфильтровать коллекцию. |
| `Organizatsii` | `Adresaofisov_col` — атрибут типа «**Запись**» с несколькими значениями | Хранит коллекцию адресов офисов. |
| `Adresa` | `Oblast` — атрибут типа «**Текст**» | Хранит область, по которой фильтруются адреса. |

## Настройка фильтра

1. Откройте форму шаблона записи `Organizatsii` в конструкторе формы.
2. Выберите коллекцию `Adresaofisov_col`.
3. В поле «**Фильтр записей: для отображения**» вставьте следующее выражение:

```
@prefix object: <http://comindware.com/ontology/object#>.
{
   ("Adresa" "Oblast") object:findProperty ?PropertyOblast.
   ("Organizatsii" "Adresaofisov_col") object:findProperty ?PropertyAdresaofisov_col.
   ("Organizatsii" "Filtrpooblasti") object:findProperty ?PropertyOblastFilter.

   ?item ?PropertyOblastFilter ?filter.
   ?item ?PropertyAdresaofisov_col ?result_A.
   ?result_A ?PropertyOblast ?filter.
   ?result_A -> ?value.
}
```

## Разбор выражения

| Фрагмент | Описание |
| --- | --- |
| `@prefix object: <http://comindware.com/ontology/object#>.` | Подключает префикс `object`, чтобы использовать свойство `object:findProperty`. |
| `("Adresa" "Oblast") object:findProperty ?PropertyOblast.` | Получает ID атрибута `Oblast` из шаблона `Adresa` и записывает его в переменную `PropertyOblast`. |
| `("Organizatsii" "Adresaofisov_col") object:findProperty ?PropertyAdresaofisov_col.` | Получает ID атрибута `Adresaofisov_col` из шаблона `Organizatsii` и записывает его в переменную `PropertyAdresaofisov_col`. |
| `("Organizatsii" "Filtrpooblasti") object:findProperty ?PropertyOblastFilter.` | Получает ID атрибута `Filtrpooblasti` из шаблона `Organizatsii` и записывает его в переменную `PropertyOblastFilter`. |
| `?item ?PropertyOblastFilter ?filter.` | Получает из текущей записи значение атрибута `Filtrpooblasti` и записывает его в переменную `filter`. |
| `?item ?PropertyAdresaofisov_col ?result_A.` | Получает из текущей записи значения атрибута `Adresaofisov_col` и записывает список записей коллекции в переменную `result_A`. |
| `?result_A ?PropertyOblast ?filter.` | Оставляет в списке `result_A` только записи, у которых значение атрибута `Oblast` совпадает со значением переменной `filter`. |
| `?result_A -> ?value.` | Передаёт отфильтрованные записи в переменную `value`, чтобы отобразить их в коллекции. |

Зарезервированные переменные N3

В выражениях N3 используются зарезервированные переменные:

- `item` — ID записи, в контексте которой выполняется выражение;
- `value` — результат выражения.

## Результат

_![Пример фильтрации записей в коллекции](https://kb.comindware.ru/assets/N3_11.PNG)_