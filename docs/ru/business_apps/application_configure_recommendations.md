---
title: Рекомендации по настройке приложений
kbId: 4716
---

# Рекомендации по настройке приложений {: #application_configure_recommendations }

## Введение {: #application_configure_recommendations_intro }

После установки **{{ productName }}** и первого входа в систему администратору предоставляется доступ ко всем разделам.

По умолчанию при установке система создаёт «**Первое приложение**» со всеми необходимыми разделами конфигурации. См. _«[Приложения. Определения и настройка][apps]»_.

Приложение можно использовать для решения одной или нескольких бизнес-задач.

Прежде чем приступать к разработке приложений, прочтите:

- [Рекомендации по циклу разработки бизнес-приложений](#production_deploy)
- [Сведениями об ответственности за разработку](#optimization_responsibility)
- [Общие рекомендации по разработке](#application_configure_recommendations_general)
- [Учебные материалы][tutorial]

{% include-markdown ".snippets/disclaimer_production_deploy.md" %}

{% include-markdown ".snippets/disclaimer_optimization.md" %}

## Общие рекомендации {: #application_configure_recommendations_general }

Рекомендуется создавать отдельные приложения под каждую бизнес-задачу, например «_Согласование договоров», «CRM», «Управление кадрами»_ или _«ТОиР»_.

Перед тем как приступить к настройке приложения, требуется базовое понимание следующих аспектов (на примере создания CRM-системы):

- Перечень необходимой информации (справочников/разделов):
    - Контрагенты
    - Контактные лица
    - Заявки
    - Договоры
    - Прочие справочники
- Перечень процессов для автоматизации:
    - Обработка заявки
    - Формирование коммерческого предложения
    - Согласование договора
    - Прочие процессы
- Перечень ролей, участвующих в процессах:
    - Менеджер по продажам
    - Руководитель отдела продаж
    - Финансовый директор
    - Прочие роли
- Перечень необходимых отчетов:
    - План продаж
    - Загрузка менеджеров
    - Прочие роли

Когда перечень необходимых справочников, процессов, ролей и отчетов определен, можно переходить к созданию и настройке шаблонов, процессов, конфигурации ролей и других элементов приложения.

Для визуального моделирования можно использовать следующие диаграммы:

- Диаграмма бизнес-процессов
- Диаграмма бизнес-способностей
- Диаграмма модели данных
- Диаграмма модели классов

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
