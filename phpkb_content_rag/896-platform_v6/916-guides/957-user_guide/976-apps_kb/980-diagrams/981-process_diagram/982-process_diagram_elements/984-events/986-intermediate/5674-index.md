---
title: 'Промежуточные события'
kbId: 5674
url: 'https://kb.comindware.ru/article.php?id=5674'
updated: '2025-04-11 11:58:28'
---

# Промежуточные события

## Определения

**Промежуточные события** служат для управления ходом процесса и контроля его выполнения в срок, а также для обмена данными между процессами, элементами процесса и с внешними системами.

## Типы промежуточных событий

- **[Промежуточное событие-таймер](https://kb.comindware.ru/article.php?id=5678)**
- **[Промежуточное событие-отправка сообщения](https://kb.comindware.ru/article.php?id=5676)**
- **[Промежуточное событие-получение сообщения](https://kb.comindware.ru/article.php?id=5677)**
- **[Простое промежуточное событие](https://kb.comindware.ru/article.php?id=5675)**

## Способы использования промежуточного события

1. Любое промежуточное событие можно соединить с потоком управления. В этом случае токен остановится на промежуточном событии до его наступления, а после наступления события перейдёт на следующий элемент.
2. **[Промежуточное событие-таймер](https://kb.comindware.ru/article.php?id=5678)** и **[промежуточное событие-получение сообщения](https://kb.comindware.ru/article.php?id=5677)** можно присоединить к [действию](https://kb.comindware.ru/article.php?id=5664). В этом случае при наступлении данного события на нём будет создан новый токен, который перейдёт на элемент, соединённый с событием.

_![Варианты расположения промежуточного события](/platform/v6.0/business_apps/diagrams/process_diagram/process_diagram_elements/events/intermediate/img/intermediate_event_pacement_types.png)_

## Создание промежуточного события на диаграмме

1. Перетащите промежуточное событие с панели элементов на поток управления, границу [действия](https://kb.comindware.ru/article.php?id=5664) или пустое место диаграммы.
2. Будет создано **[промежуточное событие-таймер](https://kb.comindware.ru/article.php?id=5678)**.
3. При необходимости смените [тип события](#process_diagram_elements_events_intermediate) с помощью [меню элемента](https://kb.comindware.ru/article.php?id=5657#process_diagram_call_element_menu).

## Связанные статьи

- *[События](https://kb.comindware.ru/article.php?id=5669)*
- *[Элементы диаграммы процесса](https://kb.comindware.ru/article.php?id=5662)*
- *[Редактирование диаграммы процесса](https://kb.comindware.ru/article.php?id=5657#process_diagram_designer)*