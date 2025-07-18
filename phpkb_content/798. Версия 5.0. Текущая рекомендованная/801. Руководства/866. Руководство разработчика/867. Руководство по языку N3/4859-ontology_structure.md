---
title: Структура описания онтологий
kbId: 4859
---

# Структура описания онтологий

RDF является уточнением XML, для которого верны следующие правила.

- В начале RDF-документа идет список ссылок на онтологии (namespaces).
- Базовым элементом модели RDF является триплет: ресурс (субъект) связан с другим ресурсом (объектом) посредством третьего ресурса — дуги — являющейся предикатом. В этом случае мы говорим, что «субъект имеет свойство предикат со значением объект».
- Каждая вершина может быть задана ссылкой на объект одного из namespaces.

RDF ориентирован на программное обеспечение в качестве конечного потребителя информации, позволяет осуществлять автоматическую обработку Web-ресурсов.

RDFS – язык описания словарей для RDF, определяет классы, свойства и другие ресурсы, является семантическим расширением RDF.

Система классов и свойств схемы RDF похожа на систему типов языков объектноориентированного программирования, таких, например, как Java, но отличается от многих других систем.

Определение в RDF (дескриптивная логика):

Класс («Документ»);

Класс («Человек»);

Свойство («автор», «Документ», «Человек»)

Определение в Java:

Класс «Документ»

{

   «Человек» «автор»

}

В случае появления дополнительной информации о свойствах «Документа», нет необходимости изменять описание класса «Документ». Достаточно добавить новое свойство с соответствующим доменом.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
