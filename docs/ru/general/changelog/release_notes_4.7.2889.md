---
kbId:
title: Сведения о выпуске 4.7.2889
---

# Сведения о выпуске 4.7.2889 {: #release_notes_4.7.2289}

## Введение

В **{{ productName }}** версии 4.7.2889 от 02.10.2024 были реализованы перечисленные ниже новые возможности, улучшения и исправления по сравнению с [версией 4.7.2721][release_notes_4.7.2721].

## Ключевые изменения

- Расширены функции журналирования и его механизмы.
- Оптимизирована работа HTTP-адаптеров.
- Добавлена поддержка кириллических символов в системных именах.
- Обновлена поддержка интеграции с Collabora.
- Улучшен процесс экспорта данных.
- Устранены ошибки в интерфейсе пользователя, резервном копировании, процессе аутентификации и других компонентах.
- Повышена общая стабильность и функциональность продукта.

## Новые возможности и улучшения

### Журналирование

- **Отслеживание скриптов**: добавлена запись процесса выполнения скриптов в файл `script.log`.
- **Отслеживание сценариев**: реализована запись процесса выполнения сценария в файл `trigger.log`.
- **Продолжительность выполнения действий**: теперь после завершения действия в файл `process.log` записывается время его выполнения в миллисекундах. Это позволит улучшить диагностику и оптимизацию процессов.

### Инфраструктура

- **Отправка ответа на запрос**: для ускорения отклика добавлена возможность асинхронной отправки ответа для HTTP-адаптеров.
- **Поддержка Collabora**: улучшена интеграция с офисным пакетом Collabora.
- **Пути передачи данных**: добавлены атрибуты «ID сообщения» и «Дата получения» для улучшения взаимодействия с почтовыми серверами IMAP и Exchange.

### Разработка приложений

- **Поддержка кириллицы в системных именах**: добавлена поддержка кириллических символов в системных именах для интеграции с внешними системами, включая 1С.
- **Экспорт данных**: улучшено форматирование числовых данных при экспорте в Excel. Теперь они сохраняют числовой тип данных.

## Исправленные ошибки

### Интерфейс пользователя

- **Диаграмма классов**:  исправлена ошибка, которая приводила к исчезновению диаграмм классов и моделей данных после обновления страницы.
- **Диаграммы в {{ productNameArchitect }}**: исправлена ошибка, из-за которой данные на диаграммах могли отображаться некорректно.
- **Настройка таблиц**: устранена проблема с отображением таблиц при наличии персональных настроек.

### Инфраструктура

- **Аутентификация пользователей**: исправлена ошибка с контролем срока действия паролей.
- **Резервное копирование**: устранена проблема, возникавшая при восстановлении системы из файла резервной копии.
- **Active Directory**: исправлена ошибка, из-за которой не выполнялась синхронизация аккаунта с Active Directory.

### Мобильное приложение

- **Запуск процессов**: устранена ошибка, из-за которой по нажатию кнопки не запускался процесс в мобильном приложении.
- **Отображение форм**: устранена проблема с отображением форм вне вкладок при обновлении страницы.

### Прочее

- **Задача-выполнение сценария**: устранена проблема, приводившая к ошибкам исполнения C#-скрипта в задаче-выполнении сценария.
- **Экспорт данных**: исправлена ошибка экспорта данных, возникавшая при наличии незаполненных полей атрибутов типа «Число».

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}