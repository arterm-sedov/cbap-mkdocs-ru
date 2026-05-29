---
title: 'Введение'
kbId: 5161
tags:
    - содержание руководства
    - определения
hide:
    - tags
---

{% if kbExport %}
## Введение

{% elif completeGuide %}

Это полное руководство ПО **{{ productNameEnterprise }}**.

{% elif apiGuide %}

Это руководство по использованию API ПО **{{ productName }}**.

{% elif developerGuide %}

Это руководство по программированию ПО **{{ productName }}**.

Здесь представлены сведения для разработчиков, использующих ПО Comindware Platform по следующим темам:

- составление сценариев;
- составление C#-скриптов;
- составление формул;
- составление выражений на языке N3;
- использование API.

{% elif userGuide %}

Это руководство пользователя ПО **{{ productNameEnterprise }}** с модулем «**{{ productNameArchitect }}**».

{% elif adminGuideLinux %}

Это руководство системного администратора ПО **{{ productName }}** для операционной системы Linux.

{% elif adminGuideWindows %}

Это руководство системного администратора ПО **{{ productName }}** для операционной системы Windows.

{% endif %}

Здесь представлены инструкции для ПО **{{ productName }}** текущей рекомендованной версии **{{productVersion}}**.

Прежде чем приступать к настройке и использованию ПО, ознакомьтесь с приведёнными ниже сведениями.

{% if pdfOutput and not kbExport %}

С полной документацией к продукту и учебником можно ознакомиться в **[базе знаний {{ productName }}]({{ kbSite }})**.

{% endif %}

<div class="admonition question" markdown="block">

## Определения {: .admonition-title #definitions}

- **ПО** — программное обеспечение **{{ productName }}**.
- **Экземпляр ПО** — развёрнутый веб-сервер на основе **ПО**.
- **База данных** — набор директорий и файлов, содержащий все данные и конфигурацию **экземпляра ПО**.
- **Система** — развёрнутый программно-аппаратный комплекс на основе **ПО**.

</div>

{% include-markdown ".snippets/disclaimer_supported_software.md" %}

<div class="admonition danger" markdown="block">

## Уязвимости и обновления {: .admonition-title #vulnerability_policy_disclaimer }

- Версии **{{ productName }}**, выпущенные **до 31.12.2025**, содержат критические уязвимости. Рекомендуется перейти на **текущую рекомендуемую версию {{ productVersion }} или более позднюю**.
- При разработке прикладных решений средствами платформы (C#-скрипты, интеграции и т.&nbsp;п.) гражданские разработчики могут создавать уязвимости, включая повышение привилегий. Ответственность за безопасность разработанных или модифицированных собственными силами бизнес-приложений несёт заказчик.
- О выявленных уязвимостях сообщайте через **[службу поддержки][supportUrl] строго согласно [политике обработки уязвимостей][vulnerability_policy]**.

</div>

 {% if not gostech %}

{% include-markdown ".snippets/disclaimer_experimental_feature_support.md" %}

{% endif %}

{% include-markdown ".snippets/disclaimer_documentation_relevance.md" %}

{% include-markdown ".snippets/disclaimer_production_deploy.md" %}

{% include-markdown ".snippets/disclaimer_optimization.md" %}

<div class="admonition warning" markdown="block">

## Ответственность за использование сервисов третьих сторон {: .admonition-title #third_party_services_disclaimer_responsibility }

{% include-markdown ".snippets/disclaimer_third_party_services.md" %}

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
