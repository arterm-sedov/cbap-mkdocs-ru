---
title: 'Промежуточные события'
kbId: 4742
url: 'https://kb.comindware.ru/article.php?id=4742'
updated: '2025-04-11 11:58:28'
---

# Промежуточные события

## Определения

**Промежуточные события** служат для управления ходом процесса и контроля его выполнения в срок, а также для обмена данными между процессами, элементами процесса и с внешними системами.

## Типы промежуточных событий

- **[Промежуточное событие-таймер](https://kb.comindware.ru/article.php?id=4738)**
- **[Промежуточное событие-отправка сообщения](https://kb.comindware.ru/article.php?id=4740)**
- **[Промежуточное событие-получение сообщения](https://kb.comindware.ru/article.php?id=4739)**
- **[Простое промежуточное событие](https://kb.comindware.ru/article.php?id=4741)**

## Способы использования промежуточного события

1. Любое промежуточное событие можно соединить с потоком управления. В этом случае токен остановится на промежуточном событии до его наступления, а после наступления события перейдёт на следующий элемент.
2. **[Промежуточное событие-таймер](https://kb.comindware.ru/article.php?id=4738)** и **[промежуточное событие-получение сообщения](https://kb.comindware.ru/article.php?id=4739)** можно присоединить к [действию](https://kb.comindware.ru/article.php?id=4732). В этом случае при наступлении данного события на нём будет создан новый токен, который перейдёт на элемент, соединённый с событием.

_![Варианты расположения промежуточного события](/platform/v5.0/business_apps/diagrams/process_diagram/process_diagram_elements/events/intermediate/img/intermediate_event_pacement_types.png)_

## Создание промежуточного события на диаграмме

1. Перетащите промежуточное событие с панели элементов на поток управления, границу [действия](https://kb.comindware.ru/article.php?id=4732) или пустое место диаграммы.
2. Будет создано **[промежуточное событие-таймер](https://kb.comindware.ru/article.php?id=4738)**.
3. При необходимости смените [тип события](#process_diagram_elements_events_intermediate) с помощью [меню элемента](https://kb.comindware.ru/article.php?id=4721#process_diagram_call_element_menu).

## Связанные статьи

- *[События](https://kb.comindware.ru/article.php?id=4733)*
- *[Элементы диаграммы процесса](https://kb.comindware.ru/article.php?id=4724)*
- *[Редактирование диаграммы процесса](https://kb.comindware.ru/article.php?id=4721#process_diagram_designer)*