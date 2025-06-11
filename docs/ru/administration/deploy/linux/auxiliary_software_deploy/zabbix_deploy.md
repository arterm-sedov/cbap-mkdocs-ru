---
title: Zabbix. Установка и настройка
kbId: 4609
---

# Zabbix. Установка и настройка {: #zabbix_deploy}

## Введение

Система **{{ productName }}** использует службы, которые должны быть постоянно работоспособны.

Для мониторинга работоспособности системы и необходимых ей служб рекомендуется использовать программное обеспечение Zabbix.

Здесь представлены краткие инструкции по установке и настройке Zabbix.

## Основные задачи мониторинга работоспособности

Мониторинг работоспособности системы и служб необходим для устойчивой и бесперебойной работы системы, а также для заблаговременного предотвращения возможных проблем, таких как нехватка места на диске и т.&nbsp;п. Мониторинг работоспособности позволяет решать три основные задачи:

- контроль доступности служб;
- контроль наличия необходимого свободного места на дисках;
- контроль журналов на предмет наличия ошибок.

## Установка и настройка

Zabbix состоит из сервера и агентов:

- сервер можно развернуть только на \*Nix-системе;
- агенты можно установить в любой ОС: \*Nix, Windows, macOS;
- агенты необходимо установить на каждую машину, подлежащую мониторингу.

Подробные инструкции по установке настройке сервера и агентов Zabbix представлены в следующих статьях:

- [Zabbix Server, Zabbix Agent, Zabbix Frontend и MySQL. Инструкции по установке][zabbix_server_deploy]
- [Zabbix Agent. Инструкции по установке][zabbix_agent_deploy]
{% if adminGuideWindows %}
- [Zabbix Agent. Инструкции по установке для Windows][zabbix_agent_deploy_windows]
{% endif %}
- [Официальная инструкция по установке Zabbix (на английском языке)](https://www.zabbix.com/documentation/5.4/ru/manual/appendix/install)
- [Установка и настройка Zabbix 5.0 (на русском языке, serveradmin.ru)](https://serveradmin.ru/ustanovka-i-nastrojka-zabbix-5-0/)
- [Мониторинг web сайта в Zabbix (на русском языке, serveradmin.ru)](https://serveradmin.ru/monitoring-web-sayta-v-zabbix/)
- [Мониторинг времени отклика сайта в Zabbix (на русском языке, serveradmin.ru)](https://serveradmin.ru/monitoring-vremeni-otklika-sayta-v-zabbix/)
- [Мониторинг лог файла в Zabbix (на русском языке, serveradmin.ru)](https://serveradmin.ru/monitoring-log-fayla-v-zabbix/)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
