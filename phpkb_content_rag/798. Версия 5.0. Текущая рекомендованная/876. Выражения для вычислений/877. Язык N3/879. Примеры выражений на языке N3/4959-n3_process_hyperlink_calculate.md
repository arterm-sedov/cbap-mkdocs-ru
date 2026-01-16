---
title: 'Вычисление гиперссылки на историю процесса'
kbId: 4959
url: 'https://kb.comindware.ru/article.php?id=4959'
updated: '2025-12-01 14:42:53'
---

# Вычисление гиперссылки на историю процесса

## Введение

Зачастую требуется дать пользователю быстрый доступ к истории выполнения процесса, например из письма‑уведомления.

В этом примере показано, как с помощью выражения на N3 сформировать HTML‑ссылку на страницу истории процесса, связанного с текущей **[пользовательской задачей](https://kb.comindware.ru/article.php?id=4730)**.

## Прикладная задача

Требуется:

- записать в текстовый атрибут HTML‑ссылку на историю текущего процесса;
- использовать эту ссылку, например, в тексте письма или в других HTML‑элементах;
- формировать ссылку автоматически, без ручного ввода идентификаторов процесса и адреса **Comindware Platform**.

## Пример решения

1. В шаблоне записи, связанном с процессом, создайте атрибут типа «**Текст**» с форматом отображения **HTML‑текст**.
2. Установите в свойствах атрибута флажок «**Вычислять автоматически**» и введите следующее выражение на **N3** в качестве **вычисляемого значения**:

```
@prefix cmw: <http://comindware.com/logics#>.
@prefix process: <http://comindware.com/ontology/process#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix configuration: <http://comindware.com/ontology/configuration#>.
@prefix cmwlist: <http://comindware.com/logics/list#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
@prefix task: <http://comindware.com/ontology/task#>.
{
    once
    {
        # Получаем задачу, связанную с текущей записью,
        # и связанный с задачей экземпляр процесса.
        ?task task:objectId ?item.
        ?task cmw:parent ?process.
        # Преобразуем в строку идентификатор экземпляра процесса.
        ("{0}" ?process) string:format ?s.
        ("." ?s) cmwstring:split ?resultList.
        (?resultList 1) cmwlist:at ?processInstanceId.
        # Формируем ссылкe на экземпляр процесса из двух частей:
        # ?hrefPart1 и ?hrefPart2
        # Вместо «Ссылка на процесс» введите наглядную подпись ссылки.
        ("#process/{0}/map'>Ссылка на процесс</a>" ?processInstanceId) string:format ?hrefPart2.
        # Получаем базовый URL Comindware Platform из конфигурации.
        ?configObject a configuration:Configuration.
        ?configObject configuration:baseUri ?baseUrl.
        ("<a href='{0}" ?baseUrl) string:format ?hrefPart1.
        # Формируем итоговую HTML‑ссылку из двух частей.
        (?hrefPart1 ?hrefPart2) string:concatenation ?resultLink.
        # Возвращаем результирующую ссылку.
        ?resultLink == ?value.
    }
}

```

2. Используйте значение этого атрибута, например, в тексте письма при отправке уведомлений.

## Связанные статьи

- [Пользовательская задача](https://kb.comindware.ru/article.php?id=4730)
- [Шаблон процесса](https://kb.comindware.ru/article.php?id=4758)
- [Справочник по N3](https://kb.comindware.ru/article.php?id=4852)