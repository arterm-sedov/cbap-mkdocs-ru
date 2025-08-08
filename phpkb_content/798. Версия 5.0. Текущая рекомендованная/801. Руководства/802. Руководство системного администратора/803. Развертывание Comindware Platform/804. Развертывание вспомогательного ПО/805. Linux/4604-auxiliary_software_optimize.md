---
title: Настройка конфигурации вспомогательного ПО для оптимизации работы Comindware Platform
kbId: 4604
---

# Настройка конфигурации вспомогательного ПО для оптимизации работы {{ productName }}

## Введение

**{{ productName }}** использует следующее вспомогательное ПО:

- Apache Ignite — распределенная база данных;
- JVM — виртуальная машина Java;
- Elasticsearch — поисковая система;
- NGINX — обратный прокси-сервер.

Для повышения производительности и выделения дополнительных ресурсов **{{ productName }}** (далее «экземпляр ПО») можно изменить некоторые параметры конфигурации вспомогательного ПО.

## Настройка Apache Ignite

### Изменение размера выделяемой области памяти

В Apache Ignite можно назначить максимальный размер области памяти с помощью директивы `maxSize`.

1. Откройте файл `/var/www/instancename/Ignite.config`, где `instancename` — имя экземпляра ПО.
2. Найдите раздел `<bean class="org.apache.ignite.configuration.DataRegionConfiguration">` в разделе `dataRegionConfigurations`, содержащий директиву `<property name="persistenceEnabled" value="true" />`.
3. Внутри этого раздела найдите директиву `property name="maxSize"`.
4. Установите требуемый размер области памяти, например 8 ГБ:

   ```
   <property name="maxSize" value="#{8L * 1024 * 1024 * 1024}" />
   ```
5. Перезапустите экземпляр ПО, чтобы изменения вступили в силу.

### Изменение размера кучи JVM

Для JVM Apache Ignite можно назначить минимальный (начальный) и максимальный размер области памяти для кучи с помощью директив `Xms` и `Xmx`.

Примечание

- JVM может фактически использовать больше памяти, чем размер кучи, заданный директивами и `Xms` и `Xmx`.
- Размер кучи можно задать в гигабайтах, мегабайтах, килобайтах: `-Xms<size>[g|G|m|M|k|K]`. Если не указать единицу измерения, то размер кучи будет задан в байтах.

1. Установите переменную среды `JVM_OPTS`, указав в ней требуемый начальный и максимальный размер кучи, например `-Xms10m` (начальный. 10 МБ) и `-Xmx16g` (макс. 16 ГБ):

   ```
   export JVM_OPTS="-Xms10m -Xmx16g
   -XX:MaxDirectMemorySize=1g
   -Djava.net.preferIPv4Stack=true
   -XX:+AlwaysPreTouch -XX:+UseG1GC
   -XX:+ScavengeBeforeFullGC -XX:+DisableExplicitGC
   --add-opens=java.base/sun.nio.ch=ALL-UNNAMED
   --add-opens=java.base/java.io=ALL-UNNAMED
   --add-opens=java.base/java.nio=ALL-UNNAMED
   --add-opens=java.base/java.util=ALL-UNNAMED
   --add-opens=java.base/java.lang=ALL-UNNAMED
   --add-exports=java.base/jdk.internal.misc=ALL-UNNAMED
   --add-exports=java.base/sun.nio.ch=ALL-UNNAMED
   --add-exports=java.management/com.sun.jmx.mbeanserver=ALL-UNNAMED
   --add-exports=jdk.internal.jvmstat/sun.jvmstat.monitor=ALL-UNNAMED
   --add-exports=java.base/sun.reflect.generics.reflectiveObjects=ALL-UNNAMED
   --add-opens=jdk.management/com.sun.management.internal=ALL-UNNAMED
   -DIGNITE_QUIET=false
   -DIGNITE_NO_ASCII=true"
   ```
2. Перезапустите экземпляр ПО, чтобы изменения вступили в силу.

#--8<-- "related_topics_heading.md"

- [Общие рекомендации по оптимизации производительности Apache Ignite](https://ignite.apache.org/docs/latest/perf-and-troubleshooting/general-perf-tips) (английский язык, официальное руководство Apache Ignite)
- [Настройка памяти и JVM](https://ignite.apache.org/docs/latest/perf-and-troubleshooting/memory-tuning) (английский язык, официальное руководство Apache Ignite)

## Настройка Elasticsearch

### Изменение количества шардов

Для Elasticsearch можно изменить максимальное количество шардов на каждый в кластере по следующему правилу:

- для повышения производительности Elasticsearch количество шардов следует уменьшить до минимально необходимого (от 100 шардов на одно приложение в экземпляре ПО);
- в случае нехватки ресурсов для Elasticsearch при большом объеме данных количество шардов следует увеличить (но при этом производительность может снизиться).

1. Откройте файл конфигурации Elasticsearch: `elasticsearch.yml`
2. Установите требуемое количество шардов с помощью директивы `cluster.max_shards_per_node`:

   ```
   сluster.max_shards_per_node: 3000

   ```
3. Перезапустите службу Elasticsearch, чтобы изменения вступили в силу.

### Изменение размера кучи JVM

Для JVM Elasticsearch можно назначить минимальный (начальный) и максимальный размер области памяти для кучи с помощью директив `Xms` и `Xmx`.

Примечание

- Для кучи JVM Elasticsearch рекомендуется выделять не более половины оперативной памяти машины, чтобы оставался достаточный объем ОЗУ для работы Lucene.
- Чем меньше размер кучи Elasticsearch, тем выше будет производительность Elasticsearch и Lucene.
- Не следует выделять для кучи JVM более 32 ГБ, так как это может привести к снижению производительности и перерасходу памяти.
- JVM может фактически использовать больше памяти, чем размер кучи, заданный директивами и `Xms` и `Xmx`.
- Размер кучи можно задать в гигабайтах, мегабайтах, килобайтах: `-Xms<size>[g|G|m|M|k|K]`. Если не указать единицу измерения, то размер кучи будет задан в байтах.

1. Откройте файл конфигурации JVM Elasticsearch: `/etc/elasticsearch/jvm.options`
2. Установите размер кучи начальный и максимальный размер кучи, например `-Xms4g` (начальный. 4 ГБ) и `-Xmx32g` (макс. 32 ГБ):

   ```
   -Xms4g
   -Xmx32g
   ```
3. Перезапустите службу Elasticsearch, чтобы изменения вступили в силу.

#--8<-- "related_topics_heading.md"

- [Ускорение поиска](https://www.elastic.co/guide/en/elasticsearch/reference/current/tune-for-search-speed.html) (английский язык, официальное руководство Elasticsearch)
- [Ускорение индексации](https://www.elastic.co/guide/en/elasticsearch/reference/current/tune-for-indexing-speed.html) (английский язык, официальное руководство Elasticsearch)
- [Масштабирование кластера Elasticsearch](https://habr.com/ru/articles/224877/)
- [Оптимизация производительности кластера Elasticsearch](https://gals.software/blog/2022-12-08-elasticsearch-optimization?ysclid=lmrhkxl35g269901813)
- [Как уменьшить/увеличить потребление памяти Elasticsearch](https://sergeymukhin.com/blog/kak-umensituvelicit-potreblenie-pamyati-elasticsearch)
- [Elasticsearch Heap: Размер и Свопинг](https://g-soft.info/articles/1679/elasticsearch-heap-razmer-i-svoping/)
- [Настройка размера кучи](https://www.elastic.co/guide/en/elasticsearch/reference/8.1/important-settings.html#heap-size-settings) (английский язык, официальное руководство Elasticsearch)
- [Оптимизация размера кучи Java для Elasticsearch](https://opster.com/guides/elasticsearch/capacity-planning/elasticsarch-java-heap-size) (английский язык)

## Настройка NGINX

В конфигурации NGINX для экономии трафика и уменьшения времени загрузки страниц можно включить сжатие, а также увеличить количество подключений.

1. Откройте для редактирования файл `/etc/nginx/nginx.conf`
2. В разделе `events` задайте количество подключений с помощью директивы `worker_connections`:

   ```
   events {
   ...
   worker_connections 768;
   ...
   }
   ```
3. В разделе http включите и настройте сжатие:

   ```
   http {
   ...
   gzip on;
   gzip_vary on;
   gzip_proxied any;
   gzip_comp_level 6;
   gzip_buffers 16 8k;
   gzip_http_version 1.1;
   gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
   ...
   }

   ```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
