---
title: Использование диаграммы экземпляра процесса
kbId: 4723
---

# Использование диаграммы экземпляра процесса

## Введение

Диаграмма экземпляра процесса позволяет просмотреть текущие позиции токенов на элементах выполняющегося процесса, [создавать](#token_create), [перезапускать и удалять токены](#tokens-tab), остановить процесс, просмотреть [цепочку событий](#events_chain_view) процесса.

Здесь представлена информация о том, как перейти к диаграмме экземпляра процесса, какие данные она содержит, как создать токен, остановить или архивировать процесс и просмотреть цепочку событий.

## Переход к диаграмме экземпляра процесса

### Переход из списка экземпляров

1. Откройте шаблон процесса.
2. На странице «**Свойства**» шаблона нажмите кнопку «**Перейти к экземплярам**».
3. Отобразится список экземпляров процесса.
4. Дважды нажмите строку экземпляра в списке.
5. Отобразится диаграмма экземпляра.

### Переход из списка версий

1. Откройте шаблон процесса.
2. Перейдите на вкладку «**Диаграмма**».
3. Откройте [список версий][process_diagram_version_control] диаграммы процесса.
4. В столбце «**Запущенные экземпляры**» нажмите гиперссылку с ID экземпляра процесса.
5. Отобразится диаграмма экземпляра.

## Области на странице диаграммы экземпляра процесса

1. **Кнопки управления экземпляром процесса**

   - **Остановить процесс** — удаление всех токенов с диаграммы экземпляра процесса. **[Статус](#process_status)** процесса сменится на «**Отменён**». Эта кнопка отображается,если на диаграмме имеется хотя бы один токен и не выбран ни один элемент.
   - **Архивировать** — архивирование экземпляра процесса. Архивные экземпляры не отображаются в списке экземпляров (если в конфигурации соответствующей таблицы не установлен флажок «**Показывать архивные записи**»).
   - **Создать токен** — [создание токена](#token_create) на выбранном элементе для запуска выполнения процесса с этого элемента. Эта кнопка отображается, если выбран элемент диаграммы.
   - **Журнал изменений** *‌* — вызов панели со сведениями об экземпляре процесса.
2. **Сведения об экземпляре процесса**

   - **Свойства** — контекст экземпляра процесса:
     - **Статус**
       - **Активен** — на элементах диаграммы процесса есть токены.
       - **Неактивен** — на элементах диаграммы процесса нет токенов.
       - **Завершён** — процесс завершился ожидаемым образом, на элементах нет токенов.
       - **Отменён** — процесс был остановлен с удалением всех токенов.
     - **Дата создания** — дата и время создания экземпляра процесса.
     - **Создатель** — ссылка на аккаунт создателя экземпляра процесса.
     - **Шаблон процесса** — ссылка на страницу конструктора диаграммы процесса.
     - **Запись** — ссылка на запись, связанную с экземпляром процесса.
     - **Шаблон записи** — ссылка на список записей шаблона, связанного с шаблоном данного процесса.
     - **Версия** — ссылка на версию диаграммы, по которой был запущен экземпляр процесса. См. *«[Управление версиями диаграммы процесса][process_diagram_version_control]»*.
   - **Токены** — список токенов с указанием элементов диаграммы процесса, на которых они находятся. Для процессов со статусом «**Завершён**» эта вкладка содержит надпись «**Нет данных для отображения**». При выборе элемента отображается панель «**Действия**» со следующими кнопками:
     - **Перейти** *‌* к форме пользовательской задачи или к диаграмме подпроцесса. Для этого также можно дважды нажать пользовательскую задачу или подпроцесс на диаграмме.
     - **Перезапустить токен** *‌* на выбранном элементе.
     - **Удалить токен** *‌* с выбранного элемента.
   - **Журнал изменений** — список событий, произошедших в ходе выполнения процесса. В журнале изменений отображается подробная информация обо всех токенах и шагах процесса:
     - дата и время создания токена;
     - наименование события;
     - инициатор — аккаунт, создавший токен на элементе;
     - фактический исполнитель задачи;
     - исполнители, указанные в свойствах задачи;
     - дата и время выхода токена из элемента;
     - цепочка событий — нажмите значок рядом с элементом в журнале изменений, чтобы просмотреть цепочку событий для этого элемента. См. *«[Просмотр цепочки событий](#events_chain_view)»*.
3. **Кнопки масштабирования диаграммы**

   - **Показать всю диаграмму** *‌*
   - **Увеличить** *‌*
   - **Уменьшить** *‌*
   - Масштабировать диаграмму также можно с помощью колёсика прокрутки мыши.
   - Чтобы переместить диаграмму на экране, нажмите и перетащите её пустую область.
4. **Позиции токенов** — элементы, на которых находятся токены, выделяются жёлтой или зелёной рамкой.

_![Диаграмма экземпляра процесса](/platform/v5.0/business_apps/diagrams/process_diagram/img/process_diagram_view_instance.png)_

## Создание токена

На диаграмме процесса может быть одновременно несколько токенов на разных элементах.

Создайте токен, чтобы запустить выполнение процесса начиная с произвольного элемента диаграммы.

1. Выберите элемент на диаграмме.
2. Нажмите кнопку «**Создать новый токен**».
3. В отобразившемся окне выберите, следует ли выполнять сценарий на входе в выбранный элемент.
4. Созданный токен отобразится на вкладке «**Токены**».

## Просмотр цепочки событий

1. Перейдите на вкладку «**Журнал изменений**».
2. Нажмите значок слева от события.

   ![Значок события в журнале изменений](/platform/v5.0/business_apps/diagrams/process_diagram/img/process_diagram_view_instance_event_icon.png)

   Значок события в журнале изменений
3. Отобразится окно «**Цепочка событий**».
4. Выбранное событие будет выделено в цепочке и отмечено кружком.
5. Справа от цепочки отобразится информационная панель со сведениями о событии.

   - Чтобы изменить ширину информационной панели, потяните мышью влево или вправо границу между ней и цепочкой событий.
   - Нажимайте гиперссылки на информационной панели, чтобы перейти к соответствующим объектам.
   - Если выбрано событие внутри события «**Массовое редактирование**» или «**Массовое создание**», то в информационной панели отобразится таблица «**События группы**». Нажимайте строки в этой таблице, чтобы просмотреть сведения о событиях из этой группы.
6. Выбирайте события в цепочке, чтобы просмотреть сведения о них.

_![Просмотр цепочки событий экземпляра процесса](/platform/v5.0/business_apps/diagrams/process_diagram/img/process_diagram_view_events_chain.png)_

--8<-- "related_topics_heading.md"

- *[Управление версиями диаграммы процесса][process_diagram_version_control]*
- *[Публикация диаграммы процесса][process_diagram]*
- *[Просмотр диаграммы процесса][process_diagram]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
