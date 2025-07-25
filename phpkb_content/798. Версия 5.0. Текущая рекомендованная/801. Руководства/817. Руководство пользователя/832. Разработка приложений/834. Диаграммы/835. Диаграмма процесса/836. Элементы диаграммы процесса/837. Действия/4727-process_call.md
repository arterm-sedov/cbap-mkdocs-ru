---
title: Вызов процесса
kbId: 4727
---

# Вызов процесса

## Определения

**Вызов процесса** запускает внешний процесс из текущего процесса. Это позволяет, например, выполнять одинаковую последовательность действий в нескольких процессах.

По завершении выполнения вызванного процесса токен переходит на следующий элемент диаграммы текущего процесса.

_![Вызов процесса и его меню элемента](/platform/v5.0/business_apps/diagrams/process_diagram/process_diagram_elements/actions/img/process_call.png)_

## Операции в меню элемента «Вызов процесса»

- **Действия**

  - **Свойства** *‌* — переход к окну [свойств вызова процесса](#свойства-вызова-процесса).
  - **Сценарий на входе** *‌* — переход к конструктору сценария на входе в данный элемент.
  - **Сценарий на выходе** *‌* — переход к конструктору сценария на выходе из данного элемента.
  - **Удалить** *‌* — удаление данного элемента из диаграммы процесса.
  - **Диаграмма** *‌* — переход к диаграмме подпроцесса. Также можно нажать кнопку ![Кнопка перехода к диаграмме подпроцесса](/platform/v5.0/business_apps/diagrams/process_diagram/process_diagram_elements/actions/img/process_call_go_to_diagram.png) на самом элементе.
  - **Быстрое создание** — добавление связанного элемента на диаграмму процесса.

## Свойства вызова процесса

В окне свойств **вызова процесса** предусмотрены перечисленные ниже вкладки.

### Основные

Помимо [общих свойств элемента диаграммы процесса][process_diagram_element_common_properties] на этой вкладке можно настроить перечисленные ниже свойства вызова процесса.

#### Базовые настройки

- **Экспертные настройки** — снимите этот флажок, чтобы вызвать процесс с базовыми настройками. Чтобы вызвать процесс с особыми настройками, установите флажок и [настройте экспертные параметры](#экспертные-настройки).
- **Шаблон процесса** — выберите шаблон вызываемого процесса. Его экземпляры будут выполняться по заданным **записям для запуска процесса**. Если атрибут с записями не выбран, процесс будет запущен 1 раз и будет создана новая связанная с ним запись. Когда выбран атрибут с записями, для выбора доступны только шаблоны процессов, связанные с соответствующим шаблоном записи.
- **Записи для запуска процесса** — выберите атрибут, который ссылается на записи в шаблоне, связанном с выбранным **шаблоном процесса**. По этим записям будут запускаться экземпляры вызываемого процесса. Если атрибут с записями не выбран, процесс будет запущен 1 раз и будет создана новая связанная с ним запись. Когда выбран **шаблон процесса**, для выбора доступны только атрибуты связанного с ним шаблона записи.
- **Версия диаграммы процесса** — выберите версию диаграммы, по которой будет запускаться процесс.

  - **Всегда последнюю** — будет использоваться последняя опубликованная версия диаграммы.
  - **1.0…** — будет использоваться диаграмма указанной версии.
- **Выполнение экземпляров процесса** — выберите режим выполнения экземпляров процесса.

  - **Однократное** — будет запущен только один экземпляр вызываемого процесса. Этот режим выбирается автоматически, если не заполнено поле «**Записи для запуска процесса**». В этом режиме элемент «**Вызов процесса**» отображается на диаграмме без линий.
  - **Последовательное** — экземпляры вызываемого процесса будут выполняться последовательно по **записям для запуска процесса**. В этом режиме элемент «**Вызов процесса**» отображается на диаграмме с тремя горизонтальными линиями.
  - **Параллельное** — экземпляры вызываемого процесса будут выполняться параллельно по **записям для запуска процесса**. В этом режиме элемент «**Вызов процесса**» отображается на диаграмме с тремя вертикальными линиями.
- **Условие запуска процесса** — введите формулу, возвращающую `true` при условиях, когда требуется запускать процесс.

_![Основные свойства вызова процесса — обычные настройки](/platform/v5.0/business_apps/diagrams/process_diagram/process_diagram_elements/actions/img/process_call_general_properties.png)_

Пример — вызов процесса с базовыми настройками

**Исходные данные**

- Шаблон основного процесса «*Управление транспортом*» связан с шаблоном записи «*Рейсы*».
- Шаблон «*Рейсы*» содержит атрибут «*Затраты*», связанный с шаблоном записи «*Расходы водителей*».
- Шаблон вызываемого процесса «*Учёт расходов водителей*» связан с шаблоном записи «*Расходы водителей*».
- На диаграмму процесса «*Управление транспортом*» вынесен элемент «**Вызов процесса**».
- В **вызове процесса** выбран шаблон процесса «*Учёт расходов водителей*».
- В поле «**Записи для запуска процессов**» выбран атрибут «*Затраты*» из шаблона «*Рейсы*», основного процесса.

**Результирующее поведение**

- В записи «*Рейс 001*» в атрибуте «*Затраты*» хранятся ссылки на 5 записей с затратами водителей во время рейса.
- Процесс «*Управление транспортом*» связан с записью «*Рейс 001*» и вызывает процесс «*Учёт расходов водителей*».
- Процесс «*Учёт расходов водителей*» будет выполнен 5 раз по каждой записи шаблона «*Расходы водителей*» из атрибута «*Затраты*».

#### Экспертные настройки

- **Экспертные настройки** — установите этот флажок.
- **Выражение для выборки объектов** — введите формулу, возвращающую список объектов, по которым будет выполняться итерация запуска экземпляров вызываемого процесса.
- **Шаблон для выборки объектов** — выберите шаблон записи, в контексте которого требуется вычислять **выражение для выборки объектов**. Связанные с ним шаблоны процессов будут отображаться в списке «**Шаблон процесса**».
- **Режим выполнения**
  - **Параллельный** — экземпляры вызываемого процесса будут выполняться одновременно и параллельно.
  - **Последовательный** — новые экземпляры вызываемого процесса будут запускаться после завершения предыдущего экземпляра.
- **Выполнение экземпляров процесса** — это поле заполняется автоматически:
  - **Однократное** — будет запущен один экземпляр процесса;
  - **Последовательный** — экземпляры процесса будут выполняться последовательно;
  - **Параллельный** — экземпляры процесса будут выполняться параллельно.
- **Связь шаблона записи с процессом** — выберите тип вызываемого процесса.
  - **Непосредственная** — можно выбрать **шаблон процесса**, непосредственно связанный с **шаблоном для выборки объектов**;
  - **Через атрибут** — можно выбрать **шаблон процесса**, связанный с **шаблоном для выборки объектов** посредством атрибута типа «**Запись**».
- **Шаблон процесса** — выберите шаблон, экземпляры которого будут выполняться по записям, на которые указывает **атрибут связи**. Набор шаблонов в этом раскрывающемся списке зависит от **шаблона для выборки объектов** и **связи с процессом**.
- **Версия диаграммы процесса** — выберите версию диаграммы, по которой будет запускаться процесс:

  - **Всегда последнюю** — будет использоваться последняя опубликованная версия диаграммы;
  - **1.0…** — будет использоваться диаграмма указанной версии.
- **Записи, связанные с процессом** — укажите способ обработки записей в шаблоне, связанном с процессом, на которые указывает **атрибут связи**.

  - **Создавать новые** — для каждого экземпляра вызываемого процесса будет создаваться новая запись;
  - **Использовать существующие** — экземпляры вызываемого процесса будут выполняться по имеющимся записям. Если **атрибут связи** не указан, будет создана новая запись.
- **Атрибут связи** — выберите атрибут типа «**Запись**» шаблона записи, связанного с текущим процессом (для выбора в этом списке доступны атрибуты, связанные с **шаблоном процесса**).
- **Действие с записями** — выберите действие с записями, на которые указывает **атрибут связи**, выполняемое при запуске вызываемого процесса.
  - **Не задано** — не выполнять действие.
  - **Добавить** — добавление записи.
  - **Удалить** — удаление записи.

_![Основные свойства вызова процесса — экспертные настройки](/platform/v5.0/business_apps/diagrams/process_diagram/process_diagram_elements/actions/img/process_call_general_properties_expert_settings.png)_

### Данные на входе

На этой вкладке можно настроить передачу данных из текущего процесса в вызываемый. Задайте значения атрибутов в записях, по которым будет запускаться вызываемый процесс. Значения будут присвоены перед запуском каждого экземпляра вызываемого процесса.

Чтобы добавить строку в таблицу сопоставления данных, нажмите кнопку «**Добавить**».

- **Атрибут шаблона записи вызываемого процесса** — укажите в этом столбце атрибут шаблона записи, связанного с процессом.
- **Значение** — задайте в этом столбце значения **атрибутов шаблона процесса**.
  - **Формула** — введите формулу, возвращающую необходимое значение.
  - **Атрибут** — укажите атрибут текущего шаблона (или связанного с ним шаблона), в котором хранится необходимое значение.
  - **Значение** — задайте значение в формате, соответствующем типу данных **атрибута шаблона процесса**.

_![Настройка передачи данных из текущего процесса в вызываемый](/platform/v5.0/business_apps/diagrams/process_diagram/process_diagram_elements/actions/img/process_call_input_data.png)_

### Данные на выходе

На этой вкладке можно настроить передачу данных из вызываемого процесса в текущий. Задайте значения атрибутов в записи, связанной с экземпляром текущего процесса. Значения будут присвоены в записи, связанной с экземпляром текущего процесса, после выполнения экземпляров вызываемого процесса.

Чтобы добавить строку в таблицу сопоставления данных, нажмите кнопку «**Добавить**».

- **Атрибут записи текущего процесса** — укажите в этом столбце атрибут шаблона записи, связанного с текущим процессом.
- **Атрибут шаблона записи вызываемого процесса** — укажите в этом столбце атрибут шаблона записи, связанного с процессом. Значение этого атрибута будет присвоено **атрибуту записи текущего процесса**.

_![Настройка передачи данных в текущий процесс из вызываемого](/platform/v5.0/business_apps/diagrams/process_diagram/process_diagram_elements/actions/img/process_call_output_data.png)_

--8<-- "related_topics_heading.md"

- *[Встроенный подпроцесс][process_diagram_elements_embedded_subprocess]*
- *[Общие свойства элементов диаграммы процесса][process_diagram_element_common_properties]*
- *[Элементы диаграммы процесса][process_diagram_elements]*
- *[Редактирование диаграммы процесса][process_diagram]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
