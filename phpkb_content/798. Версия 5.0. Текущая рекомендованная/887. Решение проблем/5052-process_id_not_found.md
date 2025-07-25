---
title: Ошибка «Идентификатор «…» не найден» на схеме процесса
kbId: 5052
---

# Ошибка «Идентификатор «…» не найден» на схеме процесса

При написании выражений в рамках настройки схемы процесса важно понимать контекст. Изначальным контекстом в рамках шаблона процесса является контекст связанного шаблона записи.

Если при проверке или публикации диаграммы процесса вы столкнулись с ошибкой «***Идентификатор «…» не найден, позиция […]***», это значит, что в каком-то выражении вы использовали атрибут, которого нет в текущем контексте, то есть в связанном шаблоне записи. При этом в кавычках указано системное имя такого атрибута, а в квадратных скобках — его позиционирование в написанном вычисляемом выражении.

**Решение**

1. Самый простой способ — создайте нужный атрибут в связанном шаблоне записи.
2. Если же необходимо использовать именно этот атрибут, находящийся в другом шаблоне записи, обратитесь к нему через язык выражений.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
