---
title: Антивирусное ПО. Настройка исключений
kbTitle: 'Антивирусное ПО. Настройка сканирования и исключений'
kbId: 4602
---

# Антивирусное ПО. Настройка сканирования и исключений {: #antivirus_exceptions_configure }

## Введение {: #antivirus_exceptions_configure_intro }

Здесь представлены сведения о настройке антивирусного программного обеспечения (далее «Антивирусное ПО») для обеспечения работоспособности ПО **{{ productName }}**. Перечисленные ниже компоненты ПО необходимы для его корректной работы, поэтому их необходимо добавить в список исключений в антивирусном и ином ПО, которое может их блокировать.

Так как антивирусное ПО расходует вычислительные ресурсы, настоятельно рекомендуется протестировать всю систему на основе **{{ productName }}** под полной нагрузкой перед установкой и включением антивирусного ПО и после включения антивирусного ПО, чтобы измерить любые изменения стабильности и производительности. Это позволит определить, как антивирусное ПО влияет на производительность машины, на которой выполняется **{{ productName }}**.

Кроме того, здесь перечислены объекты, которые следует включить в область сканирования антивирусного ПО, для предотвращения загрузки вредоносных файлов пользователями.

## Процессы, файлы и пути для добавления в исключения антивирусного ПО {: #antivirus_exceptions_configure_objects }

{% if adminGuideLinux or kbExport %}

### Linux {: #antivirus_exceptions_configure_objects_linux }

#### ПО {{ productName }} {: #antivirus_exceptions_configure_objects_linux_product }

По умолчанию файлы экземпляра ПО находятся в каталоге `/var/lib/comindware/<instanceName>`, где `<instanceName>` — имя экземпляра ПО.

*См. также статью «[Пути и содержимое папок экземпляра ПО][paths]».*

Обеспечьте санирование с помощью антивирусного ПО содержимого следующих директорий:

- `/var/lib/comindware/<instanceName>/Temp` — временное хранилище загруженных файлов и скомпилированных C#-скриптов;
- `/var/lib/comindware/<instanceName>/LocalTemp` — временные файлы резервных копий;
- `/var/lib/comindware/<instanceName>/Streams` — файлы, загруженные пользователями и сформированные ПО.

Добавьте в исключения антивирусного ПО следующие объекты:

- Процесс `w3wp / mono-boehm`.
- `comindware<instanceName>.service` — служба экземпляра ПО;
- `apigateway<instanceName>.service` — служба шлюза экземпляра ПО;
- `/var/lib/comindware/<instanceName>` — папка с экземпляром ПО;
- `/usr/share/comindware/configs/instance/` — папка с конфигурациями экземпляров ПО;
- `/usr/share/comindware/configs/instance/<instanceName>.yml` — файл конфигурации экземпляра ПО;
- `/var/www/<instanceName>` — исполняемые и конфигурационные файлы экземпляра ПО;
- `/var/lib/comindware/<instanceName>/Database/Scripts` — DLL-файлы, скомпилированные из скриптов на языке C#;
- `/var/lib/comindware/<instanceName>/Database/FullTextSearch` — индексы полнотекстового поиска;
- `/var/log/comindware/<instanceName>/Logs` — журналы экземпляра ПО.

#### {{ apacheIgniteVariants }} {: #antivirus_exceptions_configure_objects_linux_ignite }

Добавьте в исключения антивирусного ПО следующие объекты:

- `/var/lib/comindware/<instanceName>/Database/db` — база данных {{ apacheIgniteVariants }};
- `/var/lib/comindware/<instanceName>/Database/wal` — журнал предварительной записи {{ apacheIgniteVariants }};
- `/var/Lib/comindware/<instanceName>/Database/log` — журналы {{ apacheIgniteVariants }};
- `/var/lib/comindware/<instanceName>/Database/snapshots` — снимки БД {{ apacheIgniteVariants }}.

#### {{ apacheKafkaVariants }} {: #antivirus_exceptions_configure_objects_linux_kafka }

Добавьте в исключения антивирусного ПО следующие объекты:

- `kafka.service` — служба Kafka.
- `/usr/share/kafka/` — исполняемые файлы Kafka.
- `/var/log/comindware/.kafka/` — база данных с топиками Kafka.
- `/var/log/comindware/.kafka/` — журналы Kafka.

#### {{ openSearchVariants }} {: #antivirus_exceptions_configure_objects_linux_elasticsearch }

Добавьте в исключения антивирусного ПО следующие объекты:

- `elasticsearch.service` — служба ElasticSearch.
- `/var/lib/elasticsearch` — БД ElasticSearch, см. директиву `path.data` в файле конфигурации `/etc/elasticsearch/elasticsearch.yml`;
- `/var/backups/elasticsearch/logs` — журналы ElasticSearch, см. директиву `path.logs` в файле конфигурации `/etc/elasticsearch/elasticsearch.yml`;
- `/var/log/elasticsearch/repo` — репозиторий ElasticSearch, см. директиву `path.repo` в файле конфигурации `/etc/elasticsearch/elasticsearch.yml`.

{% endif %}

{% if adminGuideWindows or kbExport %}

### Windows {: #antivirus_exceptions_configure_objects_windows }

#### ПО {{ productName }} {: #antivirus_exceptions_configure_objects_windows_product }

По умолчанию файлы экземпляра ПО находятся в каталоге `C:\ProgramData\Comindware\Instances\<instanceName>`, где `<instanceName>` — имя экземпляра ПО.

*См. также статью «[Пути и содержимое папок экземпляра ПО][paths]».*

Обеспечьте санирование с помощью антивирусного ПО содержимого следующих директорий:

- `C:\ProgramData\Comindware\Instances\<instanceName>\Temp` — временное хранилище загруженных файлов и скомпилированных C#-скриптов;
- `C:\ProgramData\Comindware\Instances\<instanceName>\LocalTemp` — временные файлы резервных копий;
- `C:\ProgramData\Comindware\Instances\<instanceName>\Streams` — файлы, загруженные пользователями и сформированные ПО.

Добавьте в исключения антивирусного ПО следующие объекты:

- `C:\Program Files\Comindware\CBAP` — исполняемые файлы ПО разных версий;
- `C:\ProgramData\Comindware\configs` — общие файлы конфигурации ПО;
- `C:\ProgramData\Comindware\Instances` — директория с экземплярами ПО;
- `C:\ProgramData\Comindware\Instances\<instanceName>` — экземпляр ПО;
- `C:\ProgramData\Comindware\Instances\<instanceName>\Config` — конфигурация экземпляра ПО;
- `C:\ProgramData\Comindware\Instances\<instanceName>\Data\Scripts` — DLL-файлы, скомпилированные из скриптов на языке C#;
- `C:\ProgramData\Comindware\Instances\<instanceName>\Data\FullTextSearch` — индексы полнотекстового поиска;
- `C:\ProgramData\Comindware\Instances\<instanceName>\Logs` — журналы экземпляра ПО.

#### Apache Ignite {: #antivirus_exceptions_configure_objects_windows_ignite }

Добавьте в исключения антивирусного ПО следующие объекты:

- `C:\Program Files\Comindware\CBAP\X.X.X.X\bin\Apache.Ignite*` — исполняемые файлы {{ apacheIgniteVariants }} для ПО версии `X.X.X.X`;
- `C:\ProgramData\Comindware\Instances\<instanceName>\Data\db` — БД {{ apacheIgniteVariants }};
- `C:\ProgramData\Comindware\Instances\<instanceName>\Data\wal` — журнал предварительной записи {{ apacheIgniteVariants }};
- `C:\ProgramData\Comindware\Instances\<instanceName>\Data\snapshots` — снимки БД {{ apacheIgniteVariants }};
- `C:\ProgramData\Comindware\Instances\<instanceName>\Logs` — журналы {{ apacheIgniteVariants }}.

#### Apache Kafka {: #antivirus_exceptions_configure_objects_windows_kafka }

Добавьте следующие объекты в исключения антивирусного ПО:

- `C:\kafka_2.XX-X.X.X` — исполняемые файлы Kafka;
- `C:\kafka_2.XX-X.X.X` — БД с топиками Kafka;
- `C:\kafka_2.XX-X.X.X\zookeeper-data` — данные Zookeper;
- `C:\kafka_2.XX-X.X.X\kafka-logs` — журналы Kafka.

Здесь `X:\kafka\_2.XX-X.X.X` — директория, в которой установлено ПО Kafka версии 2.XX-X.X.X.

#### ElasticSearch {: #antivirus_exceptions_configure_objects_windows_elasticsearch }

Добавьте в исключения антивирусного ПО следующие объекты:

- `C:\Program Files\Elastic\Elasticsearch\8.X.X` — директория с исполняемыми файлами ElasticSearch версии 8.X.X;
- `C:\ProgramData\Elastic\Elasticsearch\data` — папка с БД, см. директиву `path.data` в файле конфигурации `X:\Program Files\Elastic\Elasticsearch\8.X.X\config\elasticsearch.yml`;
- `C:\ProgramData\Elastic\Elasticsearch\repo` — папка с репозиторием, см. директиву `path.repo` в файле конфигурации `X:\Program Files\Elastic\Elasticsearch\8.X.X\config\elasticsearch.yml`;
- `C:\ProgramData\Elastic\Elasticsearch\logs` — папка с журналами, см. директиву `path.logs` в файле конфигурации `X:\Program Files\Elastic\Elasticsearch\8.X.X\config\elasticsearch.yml`.

{% endif %}

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Пути и содержимое папок экземпляра ПО][paths]
- [Конфигурация экземпляра, компонентов ПО и служб][configuration_files_linux]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
