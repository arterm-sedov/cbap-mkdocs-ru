---
title: List of Comindware Expression Language Operators
kbId: 2087
---


# List of Comindware Expression Language Operators

This article provides the syntax and usage of operators in the CMW Platform Expression Language.

| from |  |
| --- | --- |
| Description | The query expression must begin with the ***from*** operator. The query expression can also contain subqueries also starting with ***from***. The ***from*** operator consists of the following components:  The data source which the request is made for (for example, record template, user database, etc.).A local variable that represents each element of the data source (for example, an entry in a template or a user account). |
| Syntax | from *variable* in *datasource* |
| Arguments | variable: local variabledatasource: record template or user database |
| where |  |
| Description | The ***where***operator is used in a query expression and determines which elements from the data source will be returned. It applies a boolean condition (predicate) to each element of the source (represented by a local variable) and returns those elements for which the condition is true. A single query expression can contain multiple ***where*** statements, and a single ***where*** statement can contain multiple predicates. |
| Syntax | where *predicate* |
| Arguments | Predicate: A Boolean value or an expression that evaluates to a Boolean value. |
| select |  |
| Description | In a query expression, the ***select*** operator determines which property of the object will be the result of the query. The final result takes into account both the work of previous operators and any expressions in the ***select*** operator itself. |
| Syntax | Select *object\_property* |
| Arguments | Object\_property: record template attribute, database field, etc. |

The following words cannot be used as local variables:

- item;
- source;
- db;
- group;
- any word that starts with an underscore (\_).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
