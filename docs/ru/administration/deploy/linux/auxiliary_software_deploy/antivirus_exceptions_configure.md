---
title: Антивирусное ПО. Настройка исключений
kbTitle: 'Антивирусное ПО. Настройка исключений: пути и файлы {{ productName }}'
kbId: 4602
---

# Антивирусное ПО. Настройка исключений {: #antivirus_exceptions_configure }

## Введение

Здесь представлены сведения о настройке антивирусного программного обеспечения (далее «Антивирусное ПО») для обеспечения работоспособности ПО **{{ productName }}**. Перечисленные ниже компоненты ПО необходимы для его корректной работы, поэтому их необходимо добавить в список исключений в антивирусном и ином ПО, которое может их блокировать.

Так как антивирусное ПО расходует вычислительные ресурсы, настоятельно рекомендуется протестировать всю систему на основе **{{ productName }}** под полной нагрузкой перед установкой и включением антивирусного ПО и после включения антивирусного ПО, чтобы измерить любые изменения стабильности и производительности. Это позволит определить, как антивирусное ПО влияет на производительность машины, на которой выполняется **{{ productName }}**.

## Процессы, файлы и пути для добавления в исключения антивирусного ПО

{% if adminGuideLinux or kbExport %}

### Linux

#### ПО {{ productName }}

По умолчанию файлы экземпляра ПО находятся в каталоге `/var/lib/comindware/<instanceName>`, где `<instanceName>` — имя экземпляра ПО.

*См. также статью «[Пути и содержимое папок экземпляра ПО][paths]».*

Рекомендуется добавить в область сканирования антивирусного ПО следующие директории:

- `/var/lib/comindware/<instanceName>/Temp` — временные файлы.
- `/var/lib/comindware/<instanceName>/LocalTemp` — 
- `/var/lib/comindware/<instanceName>/Streams` — файлы, загруженные пользователями и сформированные ПО.

Добавьте в исключения антивирусного ПО перечисленные ниже объекты.

- Процесс `w3wp / mono-boehm`.
- `comindware<instanceName>.service` — служба экземпляра ПО.
- `apigateway<instanceName>.service` — служба шлюза экземпляра ПО.
- `/var/lib/comindware/<instanceName>` — папка с экземпляром ПО;
- `/usr/share/comindware/configs/instance/` — папка с конфигурациями экземпляров ПО;
- `/usr/share/comindware/configs/instance/<instanceName>.yml` — файл конфигурации экземпляра ПО;
- /var/www/`<instanceName>` — исполняемые и конфигурационные файлы экземпляра ПО.
- `/var/lib/comindware/<instanceName>/Database/Scripts` — DLL-файлы, скомпилированные из скриптов на языке C#.
- `/var/lib/comindware/<instanceName>/Database/FullTextSearch` — индексы полнотекстового поиска.
- `/var/log/comindware/<instanceName>/Logs` — журналы экземпляра ПО.


#### {{ apacheIgniteVariants }}

Добавьте в исключения антивирусного ПО перечисленные ниже объекты.

- `/var/lib/comindware/<instanceName>/Database/db` — база данных {{ apacheIgniteVariants }}.
- `/var/lib/comindware/<instanceName>/Database/wal` — журнал предварительной записи {{ apacheIgniteVariants }}.
- `/var/Lib/comindware/<instanceName>/Database/log` — журналы {{ apacheIgniteVariants }}.
- `/var/lib/comindware/<instanceName>/Database/snapshots` — снимки БД {{ apacheIgniteVariants }}.

#### Apache Kafka

Добавьте в исключения антивирусного ПО перечисленные ниже объекты.

- `kafka.service` — служба Kafka.
- `/usr/share/kafka/` — исполняемые файлы Kafka.
- `/var/log/comindware/.kafka/` — база данных с топиками Kafka.
- `/var/log/comindware/.kafka/` — журналы Kafka.

#### ElasticSearch

Добавьте в исключения антивирусного ПО перечисленные ниже объекты.

- `elasticsearch.service` — служба ElasticSearch.
- `/var/lib/elasticsearch` — БД ElasticSearch, см. директиву `path.data` в файле конфигурации `/etc/elasticsearch/elasticsearch.yml`.
- `/var/backups/elasticsearch/logs` — журналы ElasticSearch, см. директиву `path.logs` в файле конфигурации `/etc/elasticsearch/elasticsearch.yml`.
- `/var/log/elasticsearch/repo` — репозиторий ElasticSearch, см. директиву `path.repo` в файле конфигурации `/etc/elasticsearch/elasticsearch.yml`.

{% endif %}

{% if adminGuideWindows or kbExport %}

### Windows

#### ПО {{ productName }}

По умолчанию файлы экземпляра ПО находятся в каталоге `C:\ProgramData\Comindware\Instances\<instanceName>`, где `<instanceName>` — имя экземпляра ПО.

*См. также статью «[Пути и содержимое папок экземпляра ПО][paths]».*

Добавьте в исключения антивируса перечисленные ниже объекты.

- `C:\Program Files\Comindware\CBAP` — исполняемые файлы ПО разных версий.
- `C:\ProgramData\Comindware\configs` — общие файлы конфигурации ПО.
- `C:\ProgramData\Comindware\Instances` — директория с экземплярами ПО.
- `C:\ProgramData\Comindware\Instances\<instanceName>` — экземпляр ПО.
- `C:\ProgramData\Comindware\Instances\<instanceName>\Config` — конфигурация экземпляра ПО.
- `C:\ProgramData\Comindware\Instances\<instanceName>\Data\Scripts` — DLL-файлы, скомпилированные из скриптов на языке C#.
- `C:\ProgramData\Comindware\Instances\<instanceName>\Data\FullTextSearch` — индексы полнотекстового поиска.
- `C:\ProgramData\Comindware\Instances\<instanceName>\Temp` — временные файлы.
- `C:\ProgramData\Comindware\Instances\<instanceName>\Logs` — журналы экземпляра ПО.
- `C:\ProgramData\Comindware\Instances\<instanceName>\Streams` — файлы, загруженные пользователями и сформированные ПО.

#### {{ apacheIgniteVariants }}

- `C:\Program Files\Comindware\CBAP\X.X.X.X\bin\Apache.Ignite*` — исполняемые файлы {{ apacheIgniteVariants }} для ПО версии `X.X.X.X`;
- `C:\ProgramData\Comindware\Instances\<instanceName>\Data\db` — БД {{ apacheIgniteVariants }}.
- `C:\ProgramData\Comindware\Instances\<instanceName>\Data\wal` — журнал предварительной записи {{ apacheIgniteVariants }}.
- `C:\ProgramData\Comindware\Instances\<instanceName>\Data\snapshots` — снимки БД {{ apacheIgniteVariants }}.
- `C:\ProgramData\Comindware\Instances\<instanceName>\Logs` — журналы {{ apacheIgniteVariants }}.

#### Apache Kafka

Добавьте перечисленные ниже объекты в исключения антивирусного ПО, здесь X:\kafka\_2.XX-X.X.X — директория, в которой установлено ПО Kafka версии 2.XX-X.X.X.

- `C:\kafka_2.XX-X.X.X` — исполняемые файлы Kafka.
- `C:\kafka_2.XX-X.X.X` — БД с топиками Kafka.
- `C:\kafka_2.XX-X.X.X\zookeeper-data` — данные Zookeper.
- `C:\kafka_2.XX-X.X.X\kafka-logs` — журналы Kafka.

#### ElasticSearch

- `C:\Program Files\Elastic\Elasticsearch\8.X.X` — директория с исполняемыми файлами ElasticSearch версии 8.X.X.
- `C:\ProgramData\Elastic\Elasticsearch\data` — папка с БД, см. директиву `path.data` в файле конфигурации `X:\Program Files\Elastic\Elasticsearch\8.X.X\config\elasticsearch.yml`.
- `C:\ProgramData\Elastic\Elasticsearch\repo` — папка с репозиторием, см. директиву `path.repo` в файле конфигурации `X:\Program Files\Elastic\Elasticsearch\8.X.X\config\elasticsearch.yml`.
- `C:\ProgramData\Elastic\Elasticsearch\logs` — папка с журналами, см. директиву `path.logs` в файле конфигурации `X:\Program Files\Elastic\Elasticsearch\8.X.X\config\elasticsearch.yml`.

{% endif %}

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Пути и содержимое папок экземпляра ПО][paths]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
