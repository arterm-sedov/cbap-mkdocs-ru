---
kbId: 4579
title: Введение
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

Это руководство по использованию API ПО **{{ productNameEnterprise }}**.

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

<div class="admonition warning" markdown="block">

## Поддерживаемые версии ПО {: .admonition-title #supported_software}

- Компания **{{ companyName }}** осуществляет поддержку двух версий ПО:
    - текущей рекомендованной версии для установки и использования — это версия 5.0;
    - предыдущей поддерживаемой версии — это версия 4.7.
- Поддержка версии 4.7 будет осуществляться до момента выхода новой текущей рекомендованной версии (например, 5.5), после чего поддержка версии 4.7 будет прекращена.
- Версии ПО ниже 4.7 не поддерживаются и не рекомендованы к установке, пользователи используют их на свой страх и риск.
- Для получения технической поддержки пользователям ПО версий ниже 4.7 следует обновить ПО до текущей рекомендованной версии.

</div>

 {% if not gostech %}

<div class="admonition danger" markdown="block">

## Поддержка экспериментальных функций {: .admonition-title #experimental_feature_support}

- В ПО имеется ряд экспериментальных функций, которые находятся на стадии разработки.
- Наличие, возможности и работоспособность экспериментальных функций могут быть изменены в значительной степени без предварительного уведомления.
- Компания **{{ companyName }}** не предоставляет услуги поддержки для экспериментальных функций.
- Используя экспериментальные функции, пользователи принимают на себя все сопутствующие риски.

</div>

{% endif %}

<div class="admonition note" markdown="block">

## Актуальность документации {: .admonition-title #documentation_relevance}

При составлении документации были приложены разумные усилия для достижения соответствия содержимого функциональным возможностям ПО.

Тем не менее, в некоторых случаях описания, примеры, снимки экрана и ожидаемое поведение могут отличаться от фактического состояния ПО.

Это связано с тем, что ПО постоянно совершенствуется (с целью повышения удобства пользователей ПО) и не является недостатком ПО или документации.

В свою очередь, настоящее руководство также периодически совершенствуется и пополняется (с целью устранения выявляемых недостатков).

</div>

{% include-markdown ".snippets/disclaimer_production_deploy.md" %}

{% include-markdown ".snippets/disclaimer_optimization.md" %}

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
