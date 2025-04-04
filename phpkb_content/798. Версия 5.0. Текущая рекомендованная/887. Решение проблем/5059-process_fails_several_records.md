---
title: Не получается запустить процесс по нескольким записям
kbId: 5059
---

# Не получается запустить процесс по нескольким записям

В **{{ productName }}** можно настроить кнопку для запуска процесса по записи. Однако возможность выбрать несколько записей на списке может несколько смутить. Запустить процесс по нескольким записям стандартной кнопкой нельзя, так как будут возникать конфликты в атрибутах, правилах и т.д.

**Решение**

Если же вы всё-таки хотите давать пользователям возможность выбирать несколько записей для старта процесса, то вам понадобится создать кнопку  со скриптовой операцией, которая по каждой записи будет стартовать свой экземпляр процесса, или которая [по нескольким записям будет запускать связанный процесс](https://kb.comindware.ru/article.php?id=5021).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
