---
title: Антивирусное ПО. Настройка исключений: пути и файлы Comindware Business Application Platform
kbId: 2581
---

# Антивирусное ПО. Настройка исключений: пути и файлы {{ productName }}

## Введение

В данной статье представлены сведения о настройке антивирусного программного обеспечения (далее «Антивирусное ПО») для обеспечения работоспособности ПО **{{ productName }}** (далее «ПО»). Перечисленные ниже компоненты ПО необходимы для его корректной работы, поэтому их необходимо добавить в список исключений в антивирусном и ином ПО, которое может их блокировать.

Так как антивирусное ПО расходует вычислительные ресурсы, настоятельно рекомендуется протестировать всю систему на основе **{{ productName }}** под полной нагрузкой перед установкой и включением антивирусного ПО и после включения антивирусного ПО, чтобы измерить любые изменения стабильности и производительности. Это позволит определить, как антивирусное ПО влияет на производительность машины, на которой выполняется **{{ productName }}**.

## Процессы, файлы и пути для добавления в исключения антивирусного ПО

### Linux

#### ПО {{ productName }}

По умолчанию файлы экземпляра ПО находятся в каталоге `/var/lib/comindware/instancename`, где `instancename` — имя экземпляра ПО.

*См. также статью «[Пути и содержимое папок экземпляра ПО](https://kb.comindware.ru/article.php?id=2502)».*

Добавьте в исключения антивирусного ПО перечисленные ниже объекты.

- Процесс `w3wp / mono-boehm`.
- `comindwareinstancename.service` — служба экземпляра ПО.
- `apigatewayinstancename.service` — служба шлюза экземпляра ПО.
- `/var/lib/comindware/instancename` — папка с экземпляром ПО;
- `/usr/share/comindware/configs/instance/` — папка с конфигурациями экземпляров ПО;
- `/usr/share/comindware/configs/instance/instancename.yml` — файл конфигурации экземпляра ПО;
- /var/www/`instancename` — исполняемые и конфигурационные файлы экземпляра ПО.
- `/var/lib/comindware/instancename/Database/Scripts` — DLL-файлы, скомпилированные из скриптов на языке C#.
- `/var/lib/comindware``/instancename/Database/FullTextSearch` — индексы полнотекстового поиска.
- `/var/lib/comindware``/instancename/Temp` — временные файлы.
- `/var/log/comindware/instancename/Logs` — журналы экземпляра ПО.
- `/var/lib/comindware/instancename/Streams` — файлы, загруженные пользователями и сформированные ПО.

#### Apache Ignite

Добавьте в исключения антивирусного ПО перечисленные ниже объекты.

- `/var/lib/comindware``/instancename/Database/db` — база данных Apache Ignite.
- `/var/lib/comindware``/instancename/Database/wal` — журнал предварительной записи Apache Ignite.
- `/var/Lib/comindware/instancename/Database/log` — журналы Apache Ignite.
- `/var/lib/comindware/instancename/Database/snapshots` — снимки БД Apache Ignite.

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
- `/var/backups/elasticsearch/logs` — журналы ElasticSearch, см. директиву `path.logs` в файле конфигурации `/etc/elasticsearch/``elasticsearch.yml`.
- `/var/log/elasticsearch/repo` — репозиторий ElasticSearch, см. директиву `path.repo` в файле конфигурации `/etc/elasticsearch/``elasticsearch.yml`.

### Windows

#### ПО {{ productName }}

По умолчанию файлы экземпляра ПО находятся в каталоге `C``:\``ProgramData``\``Comindware``\``Instances``\instancename`, где `instancename` — имя экземпляра ПО.

*См. также статью «[Пути и содержимое папок экземпляра ПО](https://kb.comindware.ru/article.php?id=2302)».*

Добавьте в исключения антивируса перечисленные ниже объекты.

- `C:\Program Files\Comindware\CBAP` — исполняемые файлы ПО разных версий.
- `C:\ProgramData\Comindware\configs` — общие файлы конфигурации ПО.
- `C``:\``ProgramData``\``Comindware``\``Instances` — директория с экземплярами ПО.
- `C``:\``ProgramData``\``Comindware``\``Instances``\instancename` — экземпляр ПО.
- `C``:\``ProgramData``\``Comindware``\``Instances``\instancename\Config` — конфигурация экземпляра ПО.
- `C``:\``ProgramData``\``Comindware``\``Instances``\instancename\Data\Scripts` — DLL-файлы, скомпилированные из скриптов на языке C#.
- `C``:\``ProgramData``\``Comindware``\``Instances``\instancename\Data\FullTextSearch` — индексы полнотекстового поиска.
- `C``:\``ProgramData``\``Comindware``\``Instances``\instancename\Temp` — временные файлы.
- `C``:\``ProgramData``\``Comindware``\``Instances``\instancename\Logs` — журналы экземпляра ПО.
- `C``:\``ProgramData``\``Comindware``\``Instances``\instancename\Streams` — файлы, загруженные пользователями и сформированные ПО.

#### Apache Ignite

- `C:\Program Files\Comindware\CBAP\X.X.X.X\bin\Apache.Ignite*` — исполняемые файлы Apache Ignite для ПО версии `X.X.X.X`;
- `C``:\``ProgramData``\``Comindware``\``Instances``\instancename\Data\db` — БД Apache Ignite.
- `C``:\``ProgramData``\``Comindware``\``Instances``\instancename\Data\wal` — журнал предварительной записи Apache Ignite.
- `C``:\``ProgramData``\``Comindware``\``Instances``\instancename\Data\snapshots` — снимки БД Apache Ignite.
- `C``:\``ProgramData``\``Comindware``\``Instances``\instancename\Logs` — журналы Apache Ignite.

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

--8<-- "related_topics_heading.md"

**`![](https://kb.comindware.ru/images/marker.png) Пути и содержимое папок экземпляра ПО (Linux) {Article-ID:2502}`**

**`![](https://kb.comindware.ru/images/marker.png) Пути и содержимое папок экземпляра ПО (v4.2 для Windows) {Article-ID:2302}`**



{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
