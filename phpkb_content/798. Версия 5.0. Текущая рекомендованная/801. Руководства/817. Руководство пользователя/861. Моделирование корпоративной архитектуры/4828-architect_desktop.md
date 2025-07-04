---
title: Корпоративная архитектура. Описание модуля
kbId: 4828
---

# {{ productNameArchitect }}. Описание модуля

Экспериментальная функция

Представленная здесь функция находится на стадии разработки. См. *«[Поддержка экспериментальных функций][experimental_feature_support]»*.

## Введение

Модуль «**{{ productNameArchitect }}**» — это no-code-конструктор процессной архитектуры и организационной структуры предприятия.

Этот модуль доступен только в **{{ productName }} Enterprise**.

## Знакомство с модулем «{{ productNameArchitect }}»

Прежде чем приступать к моделированию архитектуры предприятия, ознакомьтесь со следующими практическими примерами использования модуля «**{{ productNameArchitect }}**»:

- *[Моделирование корпоративной архитектуры. Описание демонстрационного стенда][architect_demo_instance]*
- *[Построение ОШС и архитектуры процессов организации. Практический пример][architect_demo_organizational_structure_processes]*

## Возможности моделирования корпоративной архитектуры

Модуль «**{{ productNameArchitect }}**» предоставляет перечисленные ниже возможности.

- **[Построение процессной архитектуры][architect_process_architecture_design]** в древовидном представлении и с помощью диаграмм:
  - Составление иерархического реестра процессов с возможностью их группировки.
  - Составление диаграмм бизнес-способностей.
  - **[Составление диаграмм процессов][architect_process_architecture_diagram_designer]** в нотации BPMN 2.0:
    - Поддержка полной палитры элементов BPMN 2.0.
    - Проверка диаграмм процессов на соответствие нотации BPMN 2.0.
    - Проверка диаграмм процессов на возможность их исполнения в **{{ productName }}**.
  - Многократное использование в реестре типовых процессов и групп процессов посредством ссылок на них.
  - Описание свойств процессов и диаграмм бизнес-способностей с использованием произвольного набора атрибутов и настраиваемых экранных форм.
  - **[Импорт диаграмм процессов][architect_import_export]** в виде файлов в формате BPMN и внешних BPM-систем.
  - **[Экспорт диаграмм процессов][architect_exporting_process_entity]** в виде файлов в форматах BPMN, SVG, PNG.
  - Автоматическое **[формирование и экспорт регламента][architect_demo_organizational_structure_processes]** (в формате DOCX) на основе процессной архитектуры.
- **[Построение организационной структуры][architect_organizational_structure_design]**:
  - Построение иерархического реестра подразделений и должностей в организации — организационно-штатной структуры.
  - Описание подразделений с использованием произвольного набора атрибутов и настраиваемых экранных форм.
- **[Обсуждение][architect_conversations]** элементов процессной архитектуры и оргструктуры.
- **[Управление версиями][architect_version_control]** процессной архитектуры и оргструктуры.
- Контроль доступа к элементам корпоративной архитектуры.
- Удобный настраиваемый **[рабочий стол][architect_desktop]** для доступа к реестрам, диаграммам и функциям настройки системы.

## Включение модуля «{{ productNameArchitect }}»

Для использования модуля «**{{ productNameArchitect }}**» его необходимо активировать с помощью **лицензионного ключа** и добавить на **панель навигации**.

1. На странице «[**Администрирование**][administration]» в разделе «**Инфраструктура**» выберите пункт «**Лицензирование**» *‌*.
2. Отобразится список лицензионных ключей.
3. Добавьте лицензионный ключ модуля «**{{ productNameArchitect }}**».
4. При необходимости назначьте лицензии аккаунтам.

   Внимание!

   Тип лицензии модуля «**{{ productNameArchitect }}**», назначенной аккаунту, должен совпадать с типом лицензии **{{ productName }}**, назначенной аккаунту.

   См. также *«[Лицензирование. Активация, назначение, отзыв и продление лицензий][licensing]»*.
5. На странице «[**Администрирование**][administration]» в разделе «**Архитектура**» выберите пункт «**Разделы навигации**» *‌*.
6. Создайте или откройте для редактирования существующий раздел навигации.
7. Добавьте блок «**{{ productNameArchitect }}**» в раздел навигации.
8. Сохраните изменения.

_![Добавление модуля «{{ productNameArchitect }}» в раздел навигации](/platform/v5.0/architect/img/architect_desktop_navigation_settings.png)_

## Рабочий стол «{{ productNameArchitect }}»

После входа в **{{ productName }} Enterprise** отображается Рабочий стол «**{{ productNameArchitect }}**» со ссылками для выполнения базовых операций.

- **Создание архитектуры**
  - **Процессы** — **[построение процессной архитектуры][architect_process_architecture_design]** организации.
  - **Оргструктура** — **[построение организационной структуры][architect_organizational_structure_design]**.
  - **Версии** — **[управление версиями][architect_version_control]** процессной архитектуры и организационной структуры.
- **Настройка продукта**
  - **Внешний вид**
    - **[Темы][themes]**
    - **[Дизайн страниц входа и регистрации][login_and_registration_page_design]**
    - **[Рабочее пространство][navigation_sections_setup]**
  - **Расширенная настройка**
    - **[Резервное копирование][backup_configure]**
    - **[Общесистемные настройки][global_configuration]**
  - **Совместная работа**
    - **[Регистрация и вход][registration_and_login]**
    - **[Роли в приложении][roles]**
    - **[Системные роли][system_roles]**
    - **[Аккаунты][accounts]**

См. также общие сведения о Рабочем столе **{{ productName }}**:

- *[Рабочий стол. Использование][desktop]*
- *[Рабочий стол. Определения и настройка][desktop_setup]*

_![Рабочий стол модуля «{{ productNameArchitect }}»](/platform/v5.0/architect/img/architect_desktop.png)_

--8<-- "related_topics_heading.md"

- *[Моделирование корпоративной архитектуры. Описание демонстрационного стенда][architect_demo_instance]*
- *[Построение ОШС и архитектуры процессов организации. Практический пример][architect_demo_organizational_structure_processes]*
- *[Построение процессной архитектуры][architect_process_architecture_design]*
- *[Построение организационной структуры][architect_organizational_structure_design]*
- *[Рабочий стол. Использование][desktop]*
- *[Рабочий стол. Определения и настройка][desktop_setup]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
