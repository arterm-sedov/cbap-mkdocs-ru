---
title: Гиперссылка на задачу. Вычисление с помощью N3 и формулы
kbId: 4879
---

# Гиперссылка на задачу. Вычисление с помощью N3 и формулы

В ходе настройки вашего бизнес-решения может понадобиться передавать в сообщение ссылку на задачу. Или же, например, вы хотите изменить формат системных уведомлений о задачах (см. также: [Уведомления о задачах. Изменение стандартного текста](https://kb.comindware.ru/article.php?id=4683)) и вам нужно вычислить ссылку на задачу. В данной статье мы рассмотрим настройку динамичной гиперссылки на задачу.

**1.** В текущем шаблоне записи создайте два атрибута: один будет отвечать за вычисление ссылки на языке N3,  а другой будет отвечать за вычленение из этой ссылки ИД задачи. Сам первый атрибут использовать в ссылке на задачу мы не можем, так как он вычисляет не конечную ссылку на задачу, но помогает нам получить ссылку для определения ИД задачи.

- Создайте текстовый атрибут «Номер задачи», сделайте его вычисляемым. В поле «Вычисляемое выражение» вставьте следующее выражение на языке N3:

```

@prefix cmw: <http://comindware.com/logics#>.
@prefix process: <http://comindware.com/ontology/process#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix configuration: <http://comindware.com/ontology/configuration#>.
{
    once
          {
        ?processObject process:businessObject ?item.
        ?taskId cmw:parent ?processObject.
        ?taskId a cmw:UserTask.
        ("#task/{0}" ?taskId) string:format ?tempLink2.  
        ?configObject a configuration:Configuration.
        ?configObject configuration:baseUri ?addressLink.
        ("{0}" ?addressLink) string:format ?tempLink1.   
        (?tempLink1 "" ?tempLink2) string:concatenation ?resultLink.
        ?resultLink == ?value.
    }
}

```

- Создайте второй текстовый атрибут «ИД задачи», сделайте его вычисляемым. В поле «Вычисляемое выражение» вставьте следующую формулу:

```
SUBSTRING($Nomerzadachi, 28)
```

**Примечание :** позиция (число) зависит от длины вашего доменного имени.

**2.** В настройках передачи ссылки на задачу введите следующее выражение:

```
FORMAT("<p><a href='https://comindware.com/#task/{0}'>Ссылка на задачу</a></p>",LIST($IDzadachi))
```

**где:**

**https://comindware.com** — ссылка на текущий инстанс;

**IDzadachi** — системное имя атрибута, где хранится/вычисляется ИД задачи.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
