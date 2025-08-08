---
title: 'Системные требования'
kbTitle: 'Системные требования Comindware Platform'
kbId: 4659
tags:
  - системные требования
  - оборудование
  - программное обеспечение
  - производительность
hide: tags
---

# Системные требования {{ productName }} {: #system_requirements }

## Введение {: #system_requirements_intro }

Ниже представлены минимальные требования к техническому и программному обеспечению для успешного запуска и использования **{{ productName }}**.

## Требования к техническому обеспечению {: #system_requirements_hardware }

### Сервер базы данных и приложений {: #system_requirements_hardware_server }

{% if gostech %}

**Аппаратные ресурсы для развёртывания подов Kubernetes**

| Название пода | Минимальное кол-во ядер ЦП | Рекоменду-емое кол-во ядер ЦП | Минимальный объём ОЗУ кол-во, ГБ | Рекомендуемый объём ОЗУ, ГБ |
| --- | --- | --- | --- |  --- |
| cmw-adapterhost | 0,5 | 1 | 0,5 | 1 |
| cmw-apigateway | 0,5 | 1 | 0,5 | 1 |
| cmw-platform | 6 | 12 | 8 | 16 |

{% else %}

| Характеристика | До 500 пользователей и до 10&nbsp;000 процессов в месяц | До 5000 пользователей и до 50&nbsp;000 процессов в месяц | Расширение на каждые 4000 пользователей и 30&nbsp;000 процессов в месяц |
| --- | --- | --- | --- |
| Процессор | 8 ядер от 3,7 ГГц | 8 ядер от 3,7 ГГц | + 4 ядра от 3,7 ГГц |
| Память | 32 ГБ | 64 ГБ | + 32 ГБ |
| Дисковый накопитель | SSD (200 ГБ) + HDD для прикладываемых документов | SSD (200 ГБ) + HDD для прикладываемых документов | SSD (200 ГБ) + HDD для прикладываемых документов |
| Сетевое соединение | 1 Гбит/с | 10 Гбит/с |  |

{% endif %}

!!! note "Примечание"

    Для обеспечения оптимальной производительности следует использовать SSD-накопители с интерфейсом NVMe.

### Клиентское рабочее место {: #system_requirements_hardware_client }

| Характеристика | Значение                          |
| ------------------ | --------------------------------- |
| Процессор          | x86 или x64 совместимый процессор |
| Память             | 8 ГБ                              |
| Монитор            | 1024x768 и выше                   |
| Сетевое соединение | 10 Мбит/с                         |

## Требования к программному обеспечению {: #system_requirements_software }

### Сервер баз данных и приложений {: #system_requirements_software_server }

<table markdown="block">
<thead>
<tr>
<th style="width:{% if completeGuide %}25%{% else %}35%{% endif %}">
Характеристика
</th>
{% if adminGuideWindows %}<th>Windows</th>{% endif %}
{% if adminGuideLinux %}<th>Linux</th>{% endif %}
</tr>
</thead>
<tbody markdown="block">
<tr markdown="block">
<td>
{% if gostech %}
Базовый образ контейнера
{% else %}
ОС
{% endif %}
</td>
{% if adminGuideWindows %}<td>Windows Server Standard 2022</td>{% endif %}
{% if adminGuideLinux %}<td markdown="block">
- Astra Linux Special Edition 1.7.5
- Альт Сервер 11, Альт&nbsp;СПАльт&nbsp;11
{% if not gostech %}
- РЕД ОС 8
- Debian 12
{% endif %}
</td>{% endif %}
</tr>
<tr>
<td>СУБД</td>
{% if adminGuideWindows %}
<td>{{ apacheIgniteVariants }}</td>
{% endif %}
{% if adminGuideLinux %}
<td>{{ apacheIgniteVariants }}</td>
{% endif %}
</tr>
<tr>
<td>Веб-сервер</td>
{% if adminGuideWindows %}<td>Internet Information Services (IIS) 10 и выше</td>{% endif %}
{% if adminGuideLinux %}
<td>
{% if gostech %}
{{ nginxVariants }}
{% else %}
NGINX 1.24 и выше
{% endif %}
</td>
{% endif %}
</tr>
<tr markdown="block">
<td>Дополнительное ПО{% if not gostech %} (поставляется и устанавливается вместе с основным пакетом){% endif %}</td>
{% if adminGuideWindows %}
<td markdown="block">
- NET 6.0
- .NET Framework 4.8.1
- {% if gostech %}{{ apacheKafkaVariants }}{% else %}Apache Kafka 3.6.0 и выше{% endif %}
- {% if gostech %}{{ openSearchVariants }}{% else %}OpenSearch 2.18.0 или Elasticsearch 8.10 и выше{% endif %}</td>
{% endif %}
{% if adminGuideLinux %}
<td markdown="block">
- NET 6.0
{% if not gostech %}- Mono 6.12{% endif %}
- {% if gostech %}{{ apacheKafkaVariants }}{% else %}Apache Kafka 3.6.0 и выше{% endif %}
- {% if gostech %}{{ openSearchVariants }}{% else %}OpenSearch 2.18.0 или Elasticsearch 8.10 и выше{% endif %}</td>
{% endif %}
</tr>
</tbody>
</table>

### Клиентское рабочее место {: #system_requirements_software_client }

| Характеристика | Значение                                                                   |
| ------------------ | -------------------------------------------------------------------------- |
| ОС                 | Linux или Windows                                                          |
| Веб-браузер        | Последние публичные версии Google Chrome, Mozilla Firefox и Microsoft Edge |
| Дополнительное ПО  | Для открытия соответствующих файлов, скачиваемых из системы                |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
