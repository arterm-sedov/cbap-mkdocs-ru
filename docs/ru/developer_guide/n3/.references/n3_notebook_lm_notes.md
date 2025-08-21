\--------------------------------------------------------------------------------

N3 Querying and Ontology: A Study Guide

Advanced N3 Querying and Ontology: A Comprehensive Study Guide

This study guide is designed to review your understanding of N3 (Notation3) querying and its underlying ontological concepts, as discussed in the provided source material.

\--------------------------------------------------------------------------------

I. Core Concepts of Ontology and Graph Databases

A. Ontology and its Application

- **Definition:** The study of being, existence, and the fundamental categories of reality. In IT, it describes a set of objects, their properties, and relationships.

- **Components:** Objects (entities), Characteristics/Properties (attributes), and Interactions/Relationships (connections).

- **Real-world Analogy:** Explaining concepts like "pencil in a pencil case" using object-oriented principles (classes, properties, relationships).

    - **Classes:** Pencil Case, Pencil

    - **Properties:** Pencil Case has Material, Capacity; Pencil has Color, Condition (sharp, dull), Hardness.

    - **Relationship:** Pencil Case contains Pencil (one-to-many, Pencil can be in 0 or 1 pencil case).

B. Graph Databases

- **Definition:** A database that uses graph structures for semantic queries with nodes, edges, and properties to represent and store data.

- **Components:**

    - **Nodes (Vertices):** Represent entities or values (e.g., classes, instances, literal values).

    - **Edges (Relations):** Represent relationships between nodes (can be directed or undirected).

- **Types of Graphs:** Connected, Isolated, Directed, Undirected, Complete, Planar, Tree-like.

- **Application to Ontology:** Graphs naturally represent ontological models where nodes are objects/classes/instances and edges are relationships.

C. Triplets (N3 and RDF)

- **Definition:** The fundamental unit of data storage in an N3/RDF graph. A triplet consists of three parts: Subject, Predicate, and Object.

- **RDF (Resource Description Framework):** A W3C standard for describing resources, often represented in XML or N3.

- **N3 (Notation3):** A compact and human-readable syntax for RDF, supporting logical expressions.

- **Components of a Triplet:**

    - **Subject:** The resource being described (the source of the arrow in a graph).

    - **Predicate:** The property or relationship (the arrow itself).

    - **Object:** The value or resource that the subject is related to (the destination of the arrow).

- **Directionality:** Triplets are inherently directed. The chosen direction (e.g., Person owns Car vs. Car owned\_by Person) dictates the subject and object. This is crucial for querying.

- **System and Custom Models:** The platform's core systemic model is fixed and uses specific predicates. Custom models defined by users (e.g., in templates) also create triplets, and their directionality is important for query construction.

D. Data Storage in the N3 Database

- **Storage Mechanism:** All data is stored as triplets, whether it's systemic metadata (e.g., class definitions, property types) or applied data (e.g., records in templates, process instances).

- **N3 Files:** System models are described in .n3 files. Applied data (metadata and instances) are stored in separate files (e.g., data.n3).

- **SQLlite Engine:** Used for transactional aspects, but the core data model and logic for serialization/deserialization between triplets and relational views are custom.

- **Types of Data in Triplets:**

    - **Qualified Name (QName):** Long URIs representing resources are often shortened with prefixes for readability (e.g., object:findProperty instead of a full HTTP URI). These are used for subjects, predicates, and objects, especially for complex types.

    - **Simple Literals:** Direct values like strings, numbers, booleans, dates, durations (e.g., "blue", 5, true).

    - **Complex Literals (Formulas and Lists):** Represent collections of facts or ordered sets of values, used in advanced queries. \* **Formulas (****{ ... }****):** A set of triplets that are evaluated together. \* **Lists (****( ... )****):** An ordered collection of values or variables.

- **Axioms vs. Derived Facts:**

    - **Axioms:** Directly stored facts (triplets) in the database.

    - **Derived Facts:** Facts computed on the fly based on axioms and the current context (e.g., calculated attributes, functions). These are not stored but computed at the moment of access.

\--------------------------------------------------------------------------------

II. N3 Query Syntax and Execution

A. Core Syntax Elements

- **Comments (****#****):** Used to add notes.

- **Prefixes (****@prefix****):** Define shortcuts for long URIs, improving readability.

- **Variables (****?****):** Denoted by a question mark followed by an alphanumeric name (e.g., ?item, ?value).

- **Triplet Terminator (****.****):** Every triplet must end with a period.

- **Formula Block (****{ ... }****):** Defines a query block that is executed as a single unit, forming a single iterator result.

- **Lists/Arrays (****( ... )****):** Used to define ordered collections of values.

- **Implicit Subject:** Square brackets (\[ ... \]) can implicitly refer to the subject of the previous triplet.

- **Reserved Keywords:** a (for rdf:type - "is an instance of"), is ... of (inverse property).

- **Assignment (****\=****):** Assigns a value from one variable to another.

- **Conditional (****if ... else ...****):** Controls query flow. If the if condition is false and there's no else block, the query stops.

B. Query Execution Model

- **Sequential Execution:** Queries execute top-down, line by line.

- **Iterative Processing:** If a line (triplet) returns an iterator (multiple values), the subsequent lines are executed for each value in that iterator. This creates nested loops.

- **Iterator Scope:** An iterator's scope is confined to the formula/block it was created in. Once the block finishes, the iterator's result is passed as a single value (or a collection) to the next level.

- **Optimization:** The order of triplets matters significantly for performance. Queries should start with the most restrictive conditions to minimize the size of initial iterators.

- **Match vs. Search:**

    - **Search (unknowns):** When one or more parts of a triplet are variables, the system searches the database for matching facts and populates the variables with iterators. \* S P ?O: Find all objects for a given subject and predicate. \* ?S P O: Find all subjects for a given predicate and object. \* ?S P ?O: Find all subject-object pairs for a given predicate.

    - **Match (all known):** When all parts of a triplet are known values, the system checks for the existence of that exact fact in the database, returning true or false. This does not return an iterator.

C. Common Query Patterns and Operators

- **findProperty****:** A built-in predicate to retrieve the ID of an attribute given its template alias and attribute alias (e.g., ("TemplateAlias" "AttributeAlias") object:findProperty ?attributeId). This always returns a single ID and is highly optimized.

- **assert:union****:** Combines the results of multiple iterators into a single iterator. assert:union true performs a union all (duplicates included), assert:union false would imply distinct (though distinct is a separate function).

- **ones****:** Executes a query and returns only the first successful result, stopping further iteration once a match is found.

- **or****:** Evaluates multiple conditions and returns true if any of them are met. It stops once the first successful condition is found.

- **Built-in Functions (e.g.,** **math:sum****,** **time:dayOfWeek****):** Special predicates that perform calculations in memory rather than querying the database. They can operate on lists of values.

- **value** **and** **item****:** Reserved keywords for output and input parameters, respectively, in expressions. value stores the output, item refers to the current object in context.

\--------------------------------------------------------------------------------

II. Application Contexts for N3 Queries

A. Calculated Attributes

- Defined on a record template to compute a value dynamically.

- item is the input (current object ID), value is the output.

- Calculated on-the-fly whenever the attribute is requested; values are not stored in the database.

B. List Filters

- Used to filter records displayed in a list.

- item is the output (IDs of records to display). There's no input item here as it filters from a potential global set.

C. Operations (Conditional Display)

- Used to show or hide operations based on conditions (e.g., a "Complete Task" button).

- item is the input (current record ID), value is true (show) or false (hide).

D. Business Rules (Triggers/Scenarios)

- Define actions that execute based on specific events (e.g., a field change).

- Can involve complex N3 queries to determine conditions or derive values for actions.

E. Global Functions

- External functions (e.g., written in C#) that can be invoked from N3 queries.

- Allow for code reusability and complex computations not directly expressible in N3.

- Can retrieve data from external services or perform custom logic.

\--------------------------------------------------------------------------------

III. Key Distinctions and Best Practices

- **Calculated Attributes vs. Stored Data:** Calculated attributes are always computed on demand and are never stored in the database. Changes to underlying stored data will trigger re-calculation.

- **Query Optimization:** Begin with highly selective conditions to reduce the size of iterators early in the query execution.

- **Understanding Iterators:** The nested loop nature of N3 query execution means careful structuring can lead to significant performance differences.

- **Contextual Variables:** item, value, current user, now are context-dependent and reserved.

\--------------------------------------------------------------------------------

Quiz: N3 Querying and Ontology

**Instructions:** Answer each question in 2-3 sentences.

1. What is the primary purpose of an "ontology" in the context of information technologies, as described in the source material?

2. How does a "graph database" fundamentally represent data, and what are its two main components?

3. Explain what a "triplet" is and identify its three essential parts in the N3/RDF model.

4. Why is the "directionality" of a relationship important when defining triplets in the N3 database?

5. What is the difference between an "axiom" and a "derived fact" in the N3 database, and how does this relate to "calculated attributes"?

6. Describe the role of "variables" (e.g., ?item, ?value) in N3 queries.

7. How does the sequential and iterative execution model of N3 queries impact their performance?

8. Explain the function of the assert:union operator in N3 queries.

9. In which context would you use the object:findProperty predicate, and what does it return?

10. What is the significance of the if ... else ... conditional structure in N3 queries regarding query execution flow?

\--------------------------------------------------------------------------------

Quiz Answer Key

1. In IT, an ontology is a formal description of a set of objects, their properties, and the relationships between them. Its primary purpose is to provide a structured and machine-readable representation of a specific domain or the real world.

2. A graph database fundamentally represents data using graph structures. Its two main components are "nodes" (representing entities or values) and "edges" (representing relationships between these nodes).

3. A triplet is the fundamental unit of data in the N3/RDF model, representing a single fact. Its three essential parts are the Subject (the resource being described), the Predicate (the property or relationship), and the Object (the value or resource related to the subject).

4. Directionality is crucial because it explicitly defines the flow of a relationship (e.g., Person owns Car). This direction determines which element is the Subject and which is the Object in a triplet, which in turn dictates how queries must be structured to retrieve specific information.

5. An axiom is a fact directly stored in the N3 database, while a derived fact is computed on the fly based on axioms and the query context. Calculated attributes are examples of derived facts; their values are computed at the moment of access and are not permanently stored in the database.

6. Variables in N3 queries (prefixed with ?) are used to represent unknown values that the query aims to discover. When a query is executed, these variables are populated with matching data from the database, often in the form of iterators.

7. The sequential and iterative execution model means queries run line-by-line, and if a line generates multiple results (an iterator), subsequent lines are re-executed for each of those results. This can significantly impact performance, making query optimization (e.g., filtering early) essential.

8. The assert:union operator combines the results of multiple query blocks or iterators into a single, unified iterator. assert:union true specifically indicates a "union all" operation, meaning duplicate values will be included in the combined result.

9. The object:findProperty predicate is used to retrieve the unique identifier (ID) of an attribute within a specific template. It takes the template's system name and the attribute's system name as arguments and returns the corresponding Property ID.

10. The if ... else ... conditional structure controls the flow of query execution. If the if condition evaluates to false and there is no else block, the query's execution path is effectively terminated, and no further triplets in that branch will be processed.

\--------------------------------------------------------------------------------

III. Essay Questions

1. Discuss the relationship between **ontology**, **graph databases**, and **triplets** in the context of the provided platform. Explain how these abstract concepts translate into the practical storage and retrieval of both system metadata and user-defined data.

2. Analyze the **N3 query execution model**, focusing on the concepts of "sequential execution," "iterative processing," and "iterator scope." How do these principles influence the design and optimization of N3 queries for performance, and what are common pitfalls developers might encounter?

3. Compare and contrast the different **types of data (****Qualified Names****,** **Simple Literals****,** **Complex Literals****)** that can be represented as objects in N3 triplets. Provide examples from the source material to illustrate their practical application in defining system properties and user data.

4. Elaborate on the role and practical application of **N3 queries in various platform contexts** such as "calculated attributes," "list filters," and "operation display conditions." For each context, describe how item and value are used and how the query's output is interpreted by the system.

5. Discuss the advantages and disadvantages of **derived facts** (e.g., calculated attributes) as opposed to storing data directly in the database, from both a performance and data integrity perspective. How does the N3 platform's architecture support this distinction, and when would you choose one approach over the other?

\--------------------------------------------------------------------------------

IV. Glossary of Key Terms

- **Axiom:** A fact that is directly stored in the N3 database.

- **assert:union****:** An N3 operator used to combine the results of multiple iterators into a single, unified iterator (similar to SQL's UNION ALL when true is specified).

- **Built-in Predicates:** Special N3 predicates (functions) that perform calculations or operations in memory rather than querying the database (e.g., math:sum, time:dayOfWeek).

- **Calculated Attribute:** A property whose value is not stored but is computed dynamically on demand using an N3 query.

- **Complex Literal:** An N3 object type representing structured data, such as a formula (a set of triplets) or a list (an ordered collection of values).

- **Derived Fact:** A fact that is not directly stored but is computed or inferred based on existing axioms and the current query context.

- **Directionality (of relationships):** The specific orientation of a relationship in a graph or triplet, indicating the flow from subject to object.

- **Edge:** A connection between two nodes in a graph, representing a relationship.

- **Formula (****{ ... }****):** A type of complex literal in N3 representing a block of one or more triplets that are executed as a single unit.

- **Graph Database:** A database that uses nodes and edges to represent and store data, emphasizing relationships between entities.

- **Implicit Subject (****\[ ... \]****):** An N3 syntax construct where square brackets can be used to refer to the subject of the immediately preceding triplet, simplifying query syntax.

- **item****:** A reserved variable in N3 queries, typically representing the ID of the current object or record in the context of the query (e.g., in calculated attributes or operations).

- **Iterator:** A mechanism in N3 query execution that provides a sequence of values, allowing subsequent query lines to be processed for each value in the sequence.

- **List (****( ... )****):** A type of complex literal in N3 representing an ordered collection of values or variables.

- **Match (Query Type):** An N3 query where all parts of a triplet (subject, predicate, object) are known, and the system verifies the existence of that exact fact (returns true or false).

- **Node:** A fundamental component of a graph, representing an entity or a value.

- **N3 (Notation3):** A human-readable and compact syntax for writing RDF (Resource Description Framework) data and logical expressions.

- **object:findProperty****:** A specific built-in predicate used to retrieve the system ID of an attribute, given the system names of its containing template and the attribute itself.

- **ones****:** An N3 operator that, when applied to a query block, ensures only the _first_ successful result is returned, stopping further iteration.

- **Ontology:** In IT, a formal description of a set of objects, their properties, and relationships within a specific domain or the real world.

- **or****:** An N3 operator used in conditional expressions; it evaluates multiple conditions and returns true if any of them are met, stopping evaluation at the first true condition.

- **Predicate:** The part of a triplet that describes the relationship or property between the subject and the object.

- **Prefix (****@prefix****):** A shorthand notation used in N3 to represent long URIs, improving query readability.

- **Qualified Name (QName):** A long, unique identifier (URI) for a resource, often abbreviated with a prefix in N3 for convenience.

- **RDF (Resource Description Framework):** A W3C standard for describing resources on the web, often used as the underlying data model for graph databases.

- **Search (Query Type):** An N3 query where one or more parts of a triplet are variables (?), prompting the system to search the database for matching facts and return iterators.

- **Simple Literal:** A direct value in an N3 triplet, such as a string, number, boolean, or date, that does not represent a complex object or resource.

- **Subject:** The part of a triplet that represents the resource or entity being described.

- **Triplet:** The fundamental data unit in an N3/RDF graph, consisting of a subject, predicate, and object.

- **value****:** A reserved variable in N3 queries, typically representing the output parameter where the result of a query or calculation is stored.

- **Variable (****?****):** A placeholder in N3 queries that represents an unknown value to be retrieved or evaluated (e.g., ?user, ?status).

## Сущности в N3 и графовых базах данных

N3 queries are used in various platform contexts to define and control dynamic behaviors, ranging from calculating attribute values to filtering lists and setting conditions for operations \[1, 2\]. These applications leverage N3's ability to interact directly with the triplet-based data storage model \[2, 3\].

Here are the primary application contexts for N3 queries:

- **Calculated Attributes**

    - **Purpose:** N3 queries are used to **dynamically compute a value for a record template** \[1, 4\]. These values are **not stored in the database**; instead, they are calculated on-the-fly whenever the attribute is requested \[1, 3-7\]. This means that changes to underlying stored data will automatically trigger a recalculation \[1, 6, 8, 9\].

    - **Variables:** In this context, item serves as the **input parameter**, representing the ID of the current object or record \[1, 4, 6, 7, 10-13\], while value is the **output parameter** where the computed attribute value is stored \[1, 4, 6, 10-13\]. For example, a calculated attribute might compute item's title \[14\].

    - **Mechanism:** When the system requests such an attribute, it understands it's a function, supplies the object's ID as item, executes the N3 query, and returns the computed value \[7, 13\].

- **List Filters**

    - **Purpose:** N3 queries are employed to **filter records displayed in a list**, determining which records should appear based on specified conditions \[1, 15\].

    - **Variables:** For list filters, item is the **output parameter**, representing the IDs of the records that should be displayed \[1, 12, 15\]. Unlike calculated attributes, there is no input item in this context, as the query filters from a potential global set of records \[1, 12, 15\].

    - **Mechanism:** The query outputs a set of item IDs, which the system then uses to populate the list view \[16, 17\].

- **Operations (Conditional Display)**

    - **Purpose:** N3 queries control the **conditional display or hiding of operations** (e.g., buttons like "Complete Task") based on certain conditions \[1, 15\]. This allows for dynamic user interface adjustments \[16\].

    - **Variables:** item is the **input parameter**, representing the ID of the current record on which the operation might be performed \[1, 15, 16\]. The value is the **output parameter**, which is set to true (to show the operation) or false (to hide it) \[1, 15, 16\].

    - **Mechanism:** If the N3 query's if condition is false and there is no else block, the query execution path for that operation is terminated, effectively preventing its display \[1, 18, 19\].

- **Business Rules (Triggers/Scenarios)**

    - **Purpose:** N3 queries define **actions that execute based on specific events**, such as a field change on a record \[1, 15, 20\]. These rules can involve complex N3 queries to determine the conditions under which an action should occur or to derive values for subsequent actions \[1, 15\].

    - **Evolution:** These were formerly known as "triggers" and are now being considered for renaming to "scenarios" to better reflect their broader business context \[20\].

    - **Interaction:** They can be used to perform various actions, like sending reminders if tasks are overdue or notifying supervisors \[16, 21\].

- **Global Functions**

    - **Purpose:** N3 queries can **invoke external functions**, often written in languages like C# \[1, 6, 22\]. This mechanism promotes code reusability and allows for complex computations or data retrieval from external services that are not directly expressible within N3 itself \[1, 6, 22, 23\].

    - **Flexibility:** Global functions enable integration with external data sources and custom logic, enhancing the platform's capabilities beyond native N3 operations \[1, 6, 23\]. This means a global function can calculate something like "sum in words" for a financial value, ensuring consistency even if the underlying numbers change \[22, 23\].

In essence, N3 queries serve as the core language for defining dynamic behavior and calculations within the platform, enabling a flexible and context-aware system where information is processed on-demand based on the underlying graph data \[1-3\].

\--------------------------------------------------------------------------------

Запросы N3: Принципы и Оптимизация

**Исполнение запросов N3** является центральным механизмом взаимодействия с данными в графовой базе данных, построенной на триплетах. Запросы N3 служат основным языком для определения динамического поведения и вычислений на платформе, обеспечивая гибкую и контекстно-зависимую обработку информации \[1, 2\].

Основные Принципы Запросов N3

1. **Операции над триплетами** \[3-12\]: Запросы N3 работают непосредственно со структурами триплетов, которые являются фундаментальной единицей хранения данных в базе \[3-12\]. Каждый триплет состоит из **Субъекта**, **Предиката** и **Объекта** \[3-10, 13-18\].

2. **Направленность** \[3-6, 13, 15-23\]: Направленность связей имеет решающее значение в триплетах, поскольку она явно определяет поток отношений (например, "Человек владеет Автомобилем" отличается от "Автомобиль принадлежит Человеку") \[3-6, 13, 15-23\]. Это направление диктует, какой элемент служит Субъектом, а какой — Объектом, что крайне важно для структурирования запросов N3 \[3-6, 13, 15-23\].

3. **Переменные** \[3, 9, 10, 24-28\]: Переменные обозначаются вопросительным знаком (например, ?S, ?P, ?O) и представляют неизвестные значения, которые запрос должен обнаружить \[3, 9, 10, 24-28\]. Когда часть триплета является переменной, система выполняет **поиск** в базе данных, чтобы найти совпадающие факты и заполнить переменные **итераторами** (последовательностями значений) \[3, 5, 6, 8, 9, 11, 12, 29\].

4. **Поиск (Search) против Сопоставления (Match)** \[3, 5, 6, 8, 9, 11, 12, 29\]:

    - **Поиск (Search)**: Используется, когда одна или несколько частей триплета являются переменными. Система находит факты, соответствующие известным частям, и возвращает итератор результатов \[3, 5, 6, 8, 9, 11, 12, 29\].

    - **Сопоставление (Match)**: Происходит, когда все части триплета являются известными значениями. Система просто проверяет наличие этого точного факта в базе данных, возвращая true или false без итератора \[3, 5, 6, 8, 9, 11, 12, 29\]. Это часто используется для валидации или условной логики \[3\].

Модель Выполнения Запросов N3

Выполнение запросов N3 следует определенной модели \[9, 11, 12, 29-31\]:

- **Последовательное выполнение**: Запросы выполняются сверху вниз, строка за строкой \[9, 11, 12, 29-31\].

- **Итеративная обработка**: Если строка (триплет) возвращает итератор (несколько значений), последующие строки **повторно выполняются для каждого значения** в этом итераторе \[9, 11, 12, 29-31\]. Это создает поведение, похожее на вложенные циклы, означающее, что механизм запросов "проходит" по графу от узла к узлу через ребра (предикаты) \[9, 30, 31\].

- **Область действия итератора**: Область действия итератора ограничена формулой/блоком, в котором он был создан \[9, 11, 12, 29-31\]. После завершения блока результат итератора передается как одно значение (или коллекция) на следующий уровень \[9, 11, 12, 29-31\].

Оптимизация Запросов

Последовательный и итеративный характер выполнения запросов N3 **значительно влияет на производительность** \[9, 11, 12, 25, 29, 30\]. Для оптимизации запросов крайне важно начинать с **наиболее ограничивающих условий**, чтобы минимизировать размер начальных итераторов \[9, 11, 12, 16, 18, 25, 29, 30, 32-35\]. Это часто означает "переворачивание" структуры запроса по сравнению с традиционными реляционными базами данных \[9, 11, 12, 25, 29, 30, 33\]. Начиная с высокоселективных условий, уменьшается количество итераций, необходимых для последующих триплетов \[30\].

Контекстные Переменные

В различных контекстах запросов N3 используются зарезервированные переменные, такие как item и value \[9, 25-28, 32, 34-40\]:

- **item**: Обычно представляет собой ID текущего объекта или записи в контексте запроса (например, в вычисляемых атрибутах или операциях) \[9, 25-28, 32, 34-38, 41-45\].

- **value**: Представляет выходной параметр, куда записывается вычисленное значение атрибута или результат запроса \[9, 25-28, 32, 34-45\]. Его ожидаемый тип может варьироваться в зависимости от контекста (например, логическое значение для операций, ID для фильтров списков или литерал для вычисляемых атрибутов) \[25\].

Встроенные Предикаты и Операторы

N3 предоставляет специализированные предикаты и операторы, которые также влияют на выполнение запросов:

- **object:findProperty**: Встроенный предикат для получения ID атрибута по его псевдониму шаблона и псевдониму атрибута \[16, 18, 36, 38-40, 46, 47\]. Он всегда возвращает один ID и высоко оптимизирован \[36, 38-40, 46, 47\].

- **assert:union**: Объединяет результаты нескольких итераторов в один \[16, 18, 36, 38-40, 46-48\]. При использовании assert:union true выполняется операция "union all", включающая дубликаты \[16, 18, 36, 38-40, 46-48\].

- **ones**: Выполняет запрос и возвращает только первый успешный результат, останавливая дальнейшую итерацию после нахождения совпадения \[36, 38-40, 46, 47\].

- **or**: Оценивает несколько условий и возвращает true, если любое из них выполняется, останавливаясь после первого успешного условия \[36, 38-40, 46, 47\].

- **Встроенные функции**: Специальные предикаты (например, math:sum, time:dayOfWeek), которые выполняют вычисления в памяти, а не запрашивают базу данных \[36, 38-40, 46, 47\]. Они могут работать со списками значений \[36, 46\].

\--------------------------------------------------------------------------------

Онтология в Информационных Технологиях и Базах Данных

**Онтология в информационных технологиях (ИТ)** является фундаментальной концепцией для структурирования и понимания данных в графовых базах данных, особенно в контексте семантических запросов \[1-7\].

Определение Онтологии в ИТ

В области информационных технологий **онтология** формально описывается как **набор объектов, их свойств и взаимосвязей между ними** \[1, 2, 4-18\]. Её основная цель — предоставить **структурированное и машиночитаемое представление конкретной предметной области или реального мира** \[1, 2, 4-9, 11-18\]. Философски, онтология занимается изучением бытия, существования и фундаментальных категорий реальности \[1, 2, 4, 6, 7, 19, 20\].

Ключевые Компоненты Онтологической Модели

Онтологическая модель состоит из трёх основных компонентов \[1, 4, 6, 7, 9\]:

- **Объекты (сущности)**: Это основные элементы или "вещи", которые описываются, например, "Пенал" или "Карандаш" \[1, 4, 6, 7, 9, 21\].

- **Характеристики/Свойства (атрибуты)**: Определяют качества или атрибуты объектов, такие как "Материал" и "Вместимость" для "Пенала", или "Цвет", "Состояние" и "Твердость" для "Карандаша" \[1, 4, 6, 7, 9, 21\].

- **Взаимодействия/Отношения (связи)**: Определяют, как объекты связаны друг с другом, например, "Пенал содержит Карандаш" \[1, 4, 6, 7, 9, 21\].

Пример "Пенал содержит Карандаш" иллюстрирует отношение "один-ко-многим", где пенал может содержать несколько карандашей, но карандаш может находиться в одном или ни одном пенале \[1, 4, 6, 7, 21, 22\]. Эта связь показывает, что пенал обладает свойством вмещать карандаши \[1, 7, 22\].

Применение в Графовых Базах Данных

**Графовые базы данных естественным образом представляют онтологические модели** \[1, 5, 7, 11-14, 16, 22-27\]. В этом контексте:

- **Узлы (вершины)** обычно представляют **объекты, классы или экземпляры**, определенные в онтологии \[1, 5, 7, 13, 14, 16, 22, 25-29\]. Например, "Человек" и "Автомобиль" могут быть узлами, представляющими классы, а "Иван Иванович" и "автомобиль Volvo" – узлами, представляющими конкретные экземпляры \[1, 5, 7, 13, 14, 16, 22, 25-29\].

- **Ребра (отношения)** представляют **взаимосвязи** между этими узлами \[1, 5, 7, 13, 14, 16, 22, 25-28\]. Например, "владеет" будет ребром, соединяющим узел "Человек" с узлом "Автомобиль" \[1, 5, 7, 13, 14, 16, 22, 25-28\].

Графовые базы данных поддерживают различные типы графов, включая направленные и ненаправленные, что отражает характер отношений в онтологии \[1, 7, 16, 23, 25, 27\]. Такая структура делает их особенно подходящими для семантических запросов, которые фокусируются на смысле и связях между точками данных \[1, 5, 7, 12, 14, 16, 23, 25-27, 30\].

Связь с Триплетами (N3 и RDF)

Онтологическая модель напрямую трансформируется в фундаментальную единицу хранения данных в графовой базе данных N3/RDF: **триплет** \[1, 5, 7, 14, 19, 23, 31-42\].

- Триплет состоит из трёх частей: **Субъект**, **Предикат** и **Объект** \[1, 7, 15, 17, 23, 33, 34, 36, 37, 39, 43, 44\]. Эта структура напрямую отражает онтологическое утверждение: Субъект — это описываемая сущность, Предикат — её свойство или отношение, а Объект — это значение или связанная сущность \[1, 7, 15, 17, 23, 33, 34, 36, 37, 39, 43\].

- **Направленность является решающим аспектом триплетов**; она явно определяет поток отношения (например, "Человек владеет Автомобилем" отличается от "Автомобиль принадлежит Человеку") \[1, 7, 15, 17, 23, 24, 31, 33, 34, 37, 39, 43-46\]. Эта направленность определяет, какой элемент является Субъектом, а какой Объектом, что крайне важно для структурирования запросов \[1, 7, 15, 17, 23, 24, 31, 33, 34, 37, 39, 43-46\].

Хранение Данных и Системные Модели

**Все данные в базе данных N3**, включая **системные метаданные** (определения классов, свойств и отношений) и **пользовательские данные** (экземпляры и записи), **хранятся исключительно в виде триплетных фактов** \[1, 5, 7, 14, 24, 31, 32, 35, 38, 40, 47-54\].

- Системные модели обычно описываются в файлах с расширением .n3 \[5, 7, 10, 14, 24, 31, 32, 35, 38, 40, 48, 53\], тогда как прикладные данные хранятся в отдельных файлах, таких как data.n3 \[5, 7, 14, 24, 31, 32, 35, 38, 40, 48, 53\].

- Основная системная модель платформы является фиксированной и использует определенные предикаты, однако пользовательские модели также создают триплеты, и их направленность важна для построения запросов \[24, 31, 37, 39\].

- Хотя платформа использует движок SQLite для транзакционных операций, её **основная модель данных и логика сериализации/десериализации** между триплетами и реляционными представлениями **разработаны индивидуально** и запатентованы \[1, 5, 7, 14, 19, 24, 32, 35, 38, 40, 48, 53, 55\]. Такой подход считается ключевым нововведением, обеспечивающим высокую скорость и уникальные принципы обработки данных \[48, 53, 56\].

- Понимание того, как эти базовые факты структурированы в базе данных N3, является **фундаментальным для создания эффективных N3-запросов** \[1, 7, 14, 31, 55\].

\--------------------------------------------------------------------------------

Графовые базы данных: Основы и онтологии

**Базы данных графов** представляют собой специализированный тип баз данных, который использует **графовые структуры** для хранения и представления данных \[1-6\]. Этот подход особенно хорошо подходит для **семантических запросов**, которые фокусируются на значении и взаимосвязях между точками данных \[1-3, 5\].

Основные компоненты Графовых Баз Данных

Графовая база данных фундаментально представляет данные с использованием двух основных компонентов:

- **Узлы (вершины)**: Представляют собой сущности или значения. Это могут быть абстрактные концепции, такие как "Пенал" или "Карандаш", или конкретные экземпляры, например, "Иван Иванович" или "автомобиль Volvo" \[4-9\].

- **Ребра (отношения)**: Представляют **взаимосвязи** между узлами. Ребра могут быть направленными или ненаправленными, обозначая связи, такие как "Пенал содержит Карандаш" или "Человек владеет Автомобилем" \[4-9\].

Графовые базы данных могут поддерживать различные типы графов, включая связанные, изолированные, направленные, ненаправленные, полные, планарные и древовидные \[4-6, 10\].

Применение к Онтологии

Графовые базы данных **естественно представляют онтологические модели** \[2-6, 8, 10-13\]. В информационных технологиях **онтология** формально описывает набор объектов, их свойств и взаимосвязей между ними \[2, 3, 5, 8, 11-16\]. В такой модели узлы обычно представляют объекты, классы или экземпляры, а ребра — отношения между ними \[4-6, 8, 10-13\]. Например, "Человек" и "Автомобиль" могут быть узлами, а "владеет" — ребром, соединяющим их \[4-6, 8, 10-13\].

Взаимосвязь с Триплетами (N3 и RDF)

Онтологическая модель напрямую преобразуется в **фундаментальную единицу хранения данных** в графовой базе данных N3/RDF: **триплет** \[3, 5, 12, 13, 17-25\].

- Триплет состоит из трех основных частей: **Субъект**, **Предикат** и **Объект** \[5, 12, 13, 18, 19, 21-28\]. Субъект — это описываемый ресурс (источник стрелки), Предикат — свойство или отношение (сама стрелка), а Объект — значение или ресурс, к которому относится субъект (назначение стрелки) \[5, 12, 13, 18, 19, 21-28\]. Например, в утверждении "Человек владеет Автомобилем", "Человек" — субъект, "владеет" — предикат, "Автомобиль" — объект \[23, 26, 28\].

- **Направленность является важнейшим аспектом триплетов** \[5, 12, 13, 19, 21, 22, 24, 25, 27, 29-33\]. Она явно определяет поток отношения (например, "Человек владеет Автомобилем" отличается от "Автомобиль принадлежит Человеку"), что имеет решающее значение для структурирования запросов N3 \[5, 12, 13, 19, 21, 22, 24, 25, 27, 29-33\].

Хранение данных и их представление в Триплетах

Все данные в базе данных N3, включая **системные метаданные** (определения классов, свойств и отношений) и **пользовательские данные** (экземпляры и записи), хранятся исключительно в виде этих триплетных фактов \[5, 12, 13, 20, 26, 31, 34-39\].

- Системные модели обычно описываются в файлах .n3, в то время как прикладные данные хранятся в отдельных файлах, таких как data.n3 \[5, 13, 20, 31, 34-40\].

- Хотя платформа использует движок SQLite для транзакционных операций, её **основная модель данных и логика сериализации/десериализации** между триплетами и реляционными представлениями являются **собственной разработкой** \[5, 12, 13, 20, 31, 34, 36-41\]. Этот подход считается ключевым нововведением, обеспечивающим скорость и уникальные принципы обработки данных \[40\].

Данные в триплетах могут быть представлены в нескольких формах \[5, 37, 38, 42-46\]:

- **Квалифицированные имена (QName)**: Сокращенные формы длинных URI, используемые для представления ресурсов \[5, 37, 38, 42-46\].

- **Простые литералы (Simple Literals)**: Прямые, атомарные значения, такие как строки, числа, булевы значения, даты или длительности \[5, 37, 38, 42-46\].

- **Сложные литералы (Complex Literals)**: Представляют собой коллекции фактов или упорядоченные наборы значений, используемые в расширенных запросах, включая **Формулы (****{...}****)** и **Списки (****(...)****)** \[5, 37, 38, 42-46\].

Различаются также два типа фактов \[5, 37, 38, 42, 44-50\]:

- **Аксиомы (Axioms)**: Факты, которые **непосредственно хранятся** в базе данных в виде триплетов \[5, 37, 38, 42, 44-50\].

- **Выводимые факты (Derived Facts)**: Вычисляются на лету на основе аксиом и текущего контекста (например, **вычисляемые атрибуты**) и **не хранятся** в базе данных \[5, 37, 38, 42, 44-50\]. Это гарантирует, что они всегда отражают самые актуальные базовые данные \[42, 47, 50-52\].

Взаимодействие Триплетов с N3-запросами

**N3-запросы** оперируют непосредственно этими триплетными структурами \[3, 5, 27, 31, 53-57\].

- Когда части триплета в запросе являются **переменными** (например, ?S P ?O), система выполняет **поиск (search)** в базе данных для нахождения соответствующих фактов и заполняет переменные **итераторами** (последовательностями значений) \[5, 27, 53-55, 57-59\].

- Если **все части триплета являются известными значениями**, система выполняет **сопоставление (match)** для проверки существования этого точного факта в базе данных, возвращая true или false \[5, 27, 53-55, 57-59\]. Эта операция не возвращает итератор \[5, 27, 53-55, 57-59\].

Выполнение N3-запросов следует **последовательной и итеративной модели**: запросы выполняются сверху вниз, строка за строкой \[55, 57, 59-63\]. Если строка возвращает итератор (несколько значений), последующие строки выполняются для каждого значения в этом итераторе, создавая поведение, подобное вложенным циклам \[55, 57, 59-63\]. Это означает, что N3-запрос эффективно "проходит" граф, перемещаясь от одного узла к другому через ребра (предикаты) \[3, 5, 55, 61, 64\].

**Порядок триплетов существенно влияет на производительность** \[5, 52, 55, 57, 59, 60, 62, 65-70\]. Запросы должны начинаться с **наиболее ограничивающих условий**, чтобы минимизировать размер начальных итераторов, тем самым сокращая количество итераций для последующих триплетов \[5, 52, 55, 57, 59, 60, 62, 66-70\].

\--------------------------------------------------------------------------------

Модель Триплетов в Базах Данных N3/RDF

Модель Триплетов является **фундаментальной единицей хранения данных** в графовых базах данных N3/RDF \[1-18\]. Эти атомарные строительные блоки имеют решающее значение для захвата фактов и взаимосвязей, обеспечивая всеобъемлющее семантическое представление данных и эффективное выполнение запросов \[4, 8, 9, 11, 15, 17, 18\].

Компоненты Триплета

Каждый триплет состоит из трех неотъемлемых частей \[1-3, 5, 8-10, 12-21\]:

- **Субъект (Subject)**: Представляет ресурс, который описывается, и действует как **источник стрелки** в графовой визуализации \[1-3, 5, 8-10, 12-21\].

- **Предикат (Predicate)**: Обозначает **свойство или отношение** между субъектом и объектом, обычно изображаемое как **сама стрелка** в графе \[1-3, 5, 8-10, 12-21\].

- **Объект (Object)**: Является значением или ресурсом, с которым связан субъект, образуя **пункт назначения стрелки** \[1-3, 5, 8-10, 12-21\].

Например, в утверждении "Человек владеет Автомобилем", "Человек" является субъектом, "владеет" — предикатом, а "Автомобиль" — объектом \[5, 13, 15, 17, 21\].

Направленность Триплетов

**Направленность является важнейшим аспектом триплетов** \[1-3, 9, 10, 12-14, 16-28\]. Она явно определяет поток отношения, делая утверждения типа "Человек владеет Автомобилем" отличными от "Автомобиль принадлежит Человеку" \[1-3, 9, 10, 12-14, 16-19, 21, 22, 24, 28\]. Эта внутренняя направленность определяет, какой элемент служит Субъектом, а какой — Объектом, что крайне важно для структурирования N3-запросов для получения конкретной информации \[1-3, 7, 9, 10, 12-14, 16-29\].

Хранение данных и их представление в Триплетах

Все данные в базе данных N3, включая **системные метаданные** (определения классов, свойств и отношений) и **пользовательские данные** (экземпляры и записи), хранятся исключительно в виде этих триплетных фактов \[1, 2, 5, 6, 11, 13, 17, 22-25, 27, 29-43\]. Системные модели обычно описываются в файлах .n3, в то время как прикладные данные (метаданные и экземпляры) хранятся в отдельных файлах, таких как data.n3 \[1, 2, 6, 11, 17, 22-24, 27, 32, 39, 41-43\]. Хотя платформа использует движок SQLite для транзакционных операций, ее основная модель данных и логика сериализации/десериализации между триплетами и реляционными представлениями являются **собственной разработкой** \[1, 2, 6, 7, 11, 13, 17, 22-24, 27, 30, 32, 33, 39, 41-44\]. Такой подход считается ключевым нововведением, обеспечивающим скорость и уникальные принципы обработки данных \[33, 45\].

Данные в триплетах могут быть представлены в нескольких формах для их субъекта, предиката или объекта \[1, 2, 17, 23, 25, 31, 32, 34, 36, 38, 40-43, 46\]:

- **Квалифицированные имена (QName)**: Сокращенные формы длинных URI (Uniform Resource Identifiers), используемые для представления ресурсов, особенно для сложных типов \[1-3, 5, 17, 22, 23, 25, 26, 31, 32, 34, 36, 38, 40-43, 46, 47\]. Например, object:findProperty — это QName, где object является префиксом для более длинного URI \[2, 19, 36, 48, 49\].

- **Простые литералы (Simple Literals)**: Прямые, атомарные значения, такие как строки ("blue"), числа (5), булевы значения (true), даты или длительности \[1, 2, 17, 19, 23-25, 31, 32, 34, 36, 38, 40-43, 46, 47, 50\].

- **Сложные литералы (Complex Literals)**: Представляют собой коллекции фактов или упорядоченные наборы значений, используемые в расширенных запросах \[1, 2, 17, 21, 23, 25, 31, 32, 34, 36, 38, 40-43, 46, 51\].

    - **Формулы (****{...}****)**: Набор триплетов, которые оцениваются вместе как единое целое \[1-3, 6, 17, 21, 23, 25, 31, 32, 34, 36, 38, 40-43, 46, 51-56\].

    - **Списки (****(...)****)**: Упорядоченная коллекция значений или переменных \[1-3, 17, 21, 23, 25, 31, 32, 34, 36, 38, 40-43, 46, 51, 52, 54-56\].

Аксиомы и Выводимые Факты

В базе данных N3 различаются два типа фактов \[1-3, 17, 19, 23, 25, 31-34, 36, 38, 40, 42, 43, 46, 57-70\]:

- **Аксиомы (Axioms)**: Факты, которые **непосредственно хранятся** в базе данных в виде триплетов \[1, 2, 17, 23, 25, 31-34, 36, 38, 40, 42, 43, 46, 57-59, 62, 63, 65-70\]. Они представляют собой постоянно хранимые данные \[40, 57\].

- **Выводимые факты (Derived Facts)**: Вычисляются на лету на основе аксиом и текущего контекста (например, **вычисляемые атрибуты**) и **не хранятся** в базе данных \[1-3, 17, 19, 23, 25, 31-34, 36, 38, 40, 42, 43, 46, 57-72\]. Вычисляемые атрибуты, например, всегда рассчитываются по запросу, гарантируя, что они всегда отражают самые актуальные базовые данные \[1-3, 19, 32, 33, 36, 38, 40, 42, 43, 52, 57-65, 67-76\]. Это означает, что изменения в исходных хранимых данных автоматически вызовут пересчет выводимых фактов при доступе к ним \[1, 3, 52, 62, 67, 72, 73\].

Взаимодействие Триплетов с N3-запросами

N3-запросы оперируют непосредственно этими триплетными структурами \[1, 2, 6, 7, 9, 17, 32, 41, 54, 56, 59\]. Синтаксические элементы языка, такие как терминатор триплета (.), блоки формул ({...}) и списки ((...)), являются фундаментальными для определения и структурирования триплетов в запросах \[6, 9, 52, 54-56, 77\].

- Когда части триплета в запросе являются **переменными** (например, ?S P ?O), система выполняет **поиск (search)** в базе данных для нахождения соответствующих фактов и заполняет переменные **итераторами** (последовательностями значений) \[1, 2, 6, 9, 17, 19, 20, 22, 24, 30, 31, 34, 41, 52, 57, 78-82\].

- Если **все части триплета являются известными значениями**, система выполняет **сопоставление (match)** для проверки существования этого точного факта в базе данных, возвращая true или false \[1, 2, 6, 9, 17, 20, 22, 24, 30, 34, 41, 57, 73, 78, 79, 81-83\]. Эта операция не возвращает итератор \[2, 6, 20, 22, 34, 79, 81, 82\].

Понимание структуры и направленности триплетов является фундаментальным для построения эффективных N3-запросов, поскольку способ хранения данных напрямую влияет на то, как информация может быть извлечена и обработана \[2, 7, 12, 17, 18, 22, 23, 26, 41, 58\]. Последовательная и итеративная модель выполнения N3-запросов означает, что **порядок триплетов существенно влияет на производительность** \[1, 3-7, 9, 17, 19, 22, 27, 31, 36, 41, 59, 62, 64, 65, 67, 68, 73, 77-79, 81, 82, 84-86\]. Запросы должны начинаться с **наиболее ограничивающих условий**, чтобы минимизировать размер начальных итераторов \[1, 3, 6, 7, 17, 22, 26, 31, 36, 38, 41, 59, 62, 64, 65, 67, 68, 73, 77-79, 81, 82, 86, 87\].

\--------------------------------------------------------------------------------

Язык запросов N3: Основы и применение

**Запросы N3** – это **язык, используемый для взаимодействия с данными, хранящимися в графовой базе данных N3/RDF**, которая представляет всю информацию в виде **триплетов** \[1-4\]. Это мощный инструмент для семантических запросов, позволяющий пользователям определять и извлекать сложные взаимосвязи и факты \[1, 2\].

Основные принципы запросов N3

1. **Операции с триплетами**: Запросы N3 оперируют непосредственно **структурами триплетов**, которые составляют фундаментальную единицу хранения данных в базе данных \[1, 5-8\]. Триплет состоит из **субъекта**, **предиката** и **объекта** \[1, 3, 6, 8-10\].

2. **Направленность**: **Направленность связей** имеет решающее значение в триплетах, прямо влияя на то, как должны быть структурированы запросы \[1, 3, 6, 8, 10-16\]. Например, "Человек владеет Автомобилем" отличается от "Автомобиль принадлежит Человеку", и это направление определяет, какой элемент служит субъектом, а какой – объектом \[1, 3, 8, 10-16\].

3. **Переменные**: **Переменные** обозначаются знаком вопроса (например, ?S, ?P, ?O) и представляют собой неизвестные значения, которые запрос стремится обнаружить \[1, 4, 17-20\]. Когда части триплета являются переменными, система выполняет **поиск** в базе данных для нахождения соответствующих фактов и заполняет переменные **итераторами** (последовательностями значений) \[1, 5-8, 18, 21-24\].

4. **Соответствие (Match) против Поиска (Search)**:

    - **Поиск (Search)**: Используется, когда одна или несколько частей триплета являются переменными. Система находит факты, соответствующие известным частям, и возвращает итератор результатов \[1, 5-8, 22-24\].

    - **Соответствие (Match)**: Происходит, когда все части триплета являются известными значениями. Система просто проверяет наличие этого точного факта в базе данных, возвращая true или false без итератора \[1, 5-8, 21-24\]. Это часто используется для проверки или условной логики.

Синтаксис и структура запросов N3

Запросы N3 используют определённый синтаксис для определения триплетов и логических выражений \[4, 17, 19, 20, 25\]:

- **Терминатор триплета (****.****):** Каждый триплет должен заканчиваться точкой \[4, 17, 19, 20, 25\].

- **Блоки формул (****{...}****):** Определяют блок запроса, который выполняется как единое целое, формируя один результат итератора \[4, 17, 19, 20, 25-28\]. Они имеют решающее значение для группировки операций \[25\].

- **Списки (****(...)****):** Используются для определения упорядоченных коллекций значений или переменных \[4, 17, 19, 20, 25-28\]. Могут использоваться для передачи нескольких аргументов встроенным функциям \[25, 29, 30\].

- **Префиксы (****@prefix****):** Определяют сокращения для длинных URI (Uniform Resource Identifiers), улучшая читаемость \[4, 17, 19, 20, 25\].

- **Комментарии (****#****):** Используются для добавления заметок в запросе \[4, 17, 19, 20, 25\].

- **Неявный субъект (****\[...\]****):** Квадратные скобки могут неявно ссылаться на субъект предыдущего триплета, упрощая синтаксис \[4, 17, 19, 20, 25\].

- **Зарезервированные ключевые слова:** a (для rdf:type — "является экземпляром"), is ... of (обратное свойство) \[4, 17, 19, 20, 25\].

- **Присваивание (****\=****):** Присваивает значение одной переменной другой \[4, 17, 19, 20, 25\].

- **Условный оператор (****if ... else ...****):** Управляет потоком запроса. Если условие if ложно и нет блока else, выполнение запроса останавливается \[4, 17, 19, 20, 25, 31\]. Если блок else отсутствует, а условие if не выполняется, выполнение запроса прекращается \[2, 17, 32\].

Модель выполнения запросов N3

Выполнение запросов N3 следует чёткой модели \[7, 23, 24, 33, 34\]:

- **Последовательное выполнение:** Запросы выполняются сверху вниз, строка за строкой \[7, 23, 24, 33, 34\].

- **Итеративная обработка:** Если строка (триплет) возвращает итератор (несколько значений), последующие строки выполняются для каждого значения в этом итераторе \[7, 23, 24, 33, 34\]. Это создаёт поведение вложенного цикла, означающее, что механизм запросов "проходит" граф от узла к узлу через рёбра (предикаты) \[7, 22-24, 33, 34\].

- **Область видимости итератора:** Область видимости итератора ограничена формулой/блоком, в котором он был создан. Как только блок завершается, результат итератора передаётся как одно значение (или коллекция) на следующий уровень \[7, 23, 24, 33, 34\].

- **Оптимизация производительности:** **Порядок триплетов значительно влияет на производительность** \[7, 8, 22-24, 33, 35-40\]. Запросы должны начинаться с **наиболее ограничивающих условий**, чтобы минимизировать размер начальных итераторов, а не следовать традиционной для реляционных баз данных схеме "FROM-WHERE" \[7, 8, 22-24, 33, 35-40\]. Начинать с высокоселективных условий сокращает количество итераций, необходимых для последующих триплетов \[7, 8, 22-24, 33, 38-40\].

Общие шаблоны запросов и операторы

- **object:findProperty**: Встроенный предикат, используемый для получения ID атрибута по его псевдониму шаблона и псевдониму атрибута (например, ("TemplateAlias" "AttributeAlias") object:findProperty ?attributeId) \[29, 30, 41-46\]. Он высоко оптимизирован, поскольку всегда возвращает один ID \[29, 30, 41-44\].

- **assert:union**: Объединяет результаты нескольких итераторов в один итератор \[29, 30, 41-47\]. assert:union true выполняет операцию "union all", включая дубликаты \[29, 30, 41-47\].

- **ones**: Выполняет запрос и возвращает только первый успешный результат, останавливая дальнейшую итерацию после нахождения соответствия \[29, 30, 41-44\].

- **or**: Оценивает несколько условий и возвращает true, если любое из них выполняется, останавливаясь после нахождения первого успешного условия \[29, 30, 41-44\].

- **Встроенные функции**: Специальные предикаты (например, math:sum, time:dayOfWeek), которые выполняют вычисления в памяти, а не запрашивают базу данных \[29, 30, 41-44\]. Они могут работать со списками значений \[29, 30\].

- **item** **и** **value**: Зарезервированные ключевые слова для входных и выходных параметров, соответственно, в выражениях \[18, 29, 30, 36, 41, 43, 44\]. item обычно представляет ID текущего объекта/записи, тогда как value хранит выходные данные запроса \[18, 29, 30, 36, 41, 43, 44\]. Их конкретные значения могут варьироваться в зависимости от контекста применения запроса \[36, 41\].

Представление и хранение данных для запросов N3

Все данные в базе данных N3, включая системные метаданные и пользовательские данные, хранятся в виде триплетов \[8, 26-28, 48-59\]. Эти данные могут принимать несколько форм в рамках триплета \[26-28, 48, 51, 52, 54, 58\]:

- **Квалифицированное имя (QName)**: Сокращённые формы длинных URI, используемые для субъектов, предикатов и объектов, особенно для сложных типов \[26-28, 48, 51, 52, 54, 58\].

- **Простые литералы**: Прямые, атомарные значения, такие как строки, числа, булевы значения, даты или длительности \[26-28, 48, 51, 52, 54, 58\].

- **Комплексные литералы**: Представляют коллекции фактов или упорядоченные наборы значений, используемые в расширенных запросах, а именно **Формулы (****{...}****)** и **Списки (****(...)****)** \[26-28, 48, 51, 52, 54, 58\].

- **Аксиомы против производных фактов**:

    - **Аксиомы** – это факты, напрямую хранящиеся в базе данных в виде триплетов \[26-28, 45, 46, 48, 51, 54, 58, 60, 61\].

    - **Производные факты** вычисляются на лету на основе аксиом и текущего контекста (например, вычисляемые атрибуты) и **не хранятся** в базе данных \[26-28, 37, 39, 40, 45, 46, 48, 51, 54, 58, 60, 61\]. Это гарантирует, что они всегда отражают самые актуальные базовые данные \[26-28, 37, 39, 40, 48, 51, 58, 60, 61\].

Контексты применения запросов N3

Запросы N3 используются в различных функциях платформы для определения динамического поведения \[31, 32, 62-68\]:

- **Вычисляемые атрибуты**: Вычисляют значения динамически для шаблона записи; они не хранятся, но рассчитываются на лету при запросе \[31, 32, 37, 39, 40, 61-65, 67\]. item является входным параметром (ID текущего объекта), а value – выходным параметром \[31, 32, 62-65, 67\].

- **Фильтры списков**: Фильтруют записи, отображаемые в списке \[31, 32, 62-64, 66, 67\]. item является выходным параметром (ID записей для отображения), при этом нет входного item, так как запрос фильтрует из потенциально глобального набора записей \[31, 32, 62-64, 66, 67\].

- **Операции (Условное отображение)**: Управляют отображением или скрытием операций (например, кнопок типа "Завершить задачу") на основе условий \[31, 32, 62-64, 66, 68\]. item является входным параметром (ID текущей записи), а value – выходным параметром, устанавливаемым в true (для отображения) или false (для скрытия) \[31, 32, 62-64, 66, 68\].

- **Бизнес-правила (Триггеры/Сценарии)**: Определяют действия, которые выполняются на основе определённых событий (например, изменение поля), часто с использованием сложных запросов N3 для определения условий или вывода значений для последующих действий \[31, 32, 62-64, 66, 68\]. Ранее они назывались "триггерами", и в настоящее время рассматривается возможность переименования их в "сценарии" для лучшего отражения их более широкого бизнес-контекста \[6, 32\].

- **Глобальные функции**: Внешние функции (например, написанные на C#) могут вызываться из запросов N3 для выполнения сложных вычислений или получения данных из внешних сервисов, которые не могут быть выражены непосредственно в N3 \[31, 32, 62-64, 66, 68\]. Это способствует повторному использованию кода \[25, 32, 36, 42\].

По сути, запросы N3 служат основным языком для определения динамического поведения и вычислений на платформе, обеспечивая гибкую и контекстно-зависимую систему, где информация обрабатывается по требованию на основе базовых графовых данных \[69, 70\]. Разработка среды для запросов N3 постоянно улучшается, разрабатываются новые компиляторы и редакторы для обеспечения лучшей подсветки ошибок и помощи в коде \[71\].

\--------------------------------------------------------------------------------

N3 Query Applications and Dynamic Behaviors

N3 queries are used in various platform contexts to define and control dynamic behaviors, ranging from calculating attribute values to filtering lists and setting conditions for operations \[1, 2\]. These applications leverage N3's ability to interact directly with the triplet-based data storage model \[2, 3\].

Here are the primary application contexts for N3 queries:

- **Calculated Attributes**

    - **Purpose:** N3 queries are used to **dynamically compute a value for a record template** \[1, 4\]. These values are **not stored in the database**; instead, they are calculated on-the-fly whenever the attribute is requested \[1, 3-7\]. This means that changes to underlying stored data will automatically trigger a recalculation \[1, 6, 8, 9\].

    - **Variables:** In this context, item serves as the **input parameter**, representing the ID of the current object or record \[1, 4, 6, 7, 10-13\], while value is the **output parameter** where the computed attribute value is stored \[1, 4, 6, 10-13\]. For example, a calculated attribute might compute item's title \[14\].

    - **Mechanism:** When the system requests such an attribute, it understands it's a function, supplies the object's ID as item, executes the N3 query, and returns the computed value \[7, 13\].

- **List Filters**

    - **Purpose:** N3 queries are employed to **filter records displayed in a list**, determining which records should appear based on specified conditions \[1, 15\].

    - **Variables:** For list filters, item is the **output parameter**, representing the IDs of the records that should be displayed \[1, 12, 15\]. Unlike calculated attributes, there is no input item in this context, as the query filters from a potential global set of records \[1, 12, 15\].

    - **Mechanism:** The query outputs a set of item IDs, which the system then uses to populate the list view \[16, 17\].

- **Operations (Conditional Display)**

    - **Purpose:** N3 queries control the **conditional display or hiding of operations** (e.g., buttons like "Complete Task") based on certain conditions \[1, 15\]. This allows for dynamic user interface adjustments \[16\].

    - **Variables:** item is the **input parameter**, representing the ID of the current record on which the operation might be performed \[1, 15, 16\]. The value is the **output parameter**, which is set to true (to show the operation) or false (to hide it) \[1, 15, 16\].

    - **Mechanism:** If the N3 query's if condition is false and there is no else block, the query execution path for that operation is terminated, effectively preventing its display \[1, 18, 19\].

- **Business Rules (Triggers/Scenarios)**

    - **Purpose:** N3 queries define **actions that execute based on specific events**, such as a field change on a record \[1, 15, 20\]. These rules can involve complex N3 queries to determine the conditions under which an action should occur or to derive values for subsequent actions \[1, 15\].

    - **Evolution:** These were formerly known as "triggers" and are now being considered for renaming to "scenarios" to better reflect their broader business context \[20\].

    - **Interaction:** They can be used to perform various actions, like sending reminders if tasks are overdue or notifying supervisors \[16, 21\].

- **Global Functions**

    - **Purpose:** N3 queries can **invoke external functions**, often written in languages like C# \[1, 6, 22\]. This mechanism promotes code reusability and allows for complex computations or data retrieval from external services that are not directly expressible within N3 itself \[1, 6, 22, 23\].

    - **Flexibility:** Global functions enable integration with external data sources and custom logic, enhancing the platform's capabilities beyond native N3 operations \[1, 6, 23\]. This means a global function can calculate something like "sum in words" for a financial value, ensuring consistency even if the underlying numbers change \[22, 23\].

In essence, N3 queries serve as the core language for defining dynamic behavior and calculations within the platform, enabling a flexible and context-aware system where information is processed on-demand based on the underlying graph data \[1-3\].

\--------------------------------------------------------------------------------

N3 Querying: Principles, Syntax, and Applications

**N3 querying** is the **language used to interact with data stored in an N3/RDF graph database**, which represents all information as **triplets** \[1-6\]. It is a powerful tool for semantic queries, allowing users to define and retrieve complex relationships and facts \[1, 4\].

Core Principles of N3 Querying

1. **Operation on Triplets**: N3 queries operate directly on the **triplet structures** that form the fundamental unit of data storage in the database \[1-6\]. A triplet consists of a **Subject**, a **Predicate**, and an **Object** \[1-3, 5, 7-10\].

2. **Directionality**: The **directionality of relationships** is crucial in triplets, directly influencing how queries must be structured. For example, "Person owns Car" is distinct from "Car owned\_by Person," and this direction dictates which element serves as the Subject and which as the Object \[1-3, 5, 7, 10-12\].

3. **Variables**: **Variables** are denoted by a question mark (e.g., ?S, ?P, ?O) and represent unknown values that the query aims to discover \[3, 10, 13-15\]. When parts of a triplet are variables, the system performs a **search** in the database to find matching facts and populates the variables with **iterators** (sequences of values) \[1, 3, 4, 16-19\].

4. **Match vs. Search**:

    - **Search**: Used when one or more parts of a triplet are variables. The system finds facts that match the known parts and returns an iterator of results \[1, 3, 4, 16, 18-20\].

    - **Match**: Occurs when all parts of a triplet are known values. The system simply checks for the existence of that exact fact in the database, returning true or false without an iterator \[1, 3, 4, 16, 18, 20-22\]. This is often used for validation or conditional logic.

N3 Query Syntax and Structure

N3 queries use a specific syntax to define triplets and logical expressions:

- **Triplet Terminator (****.****):** Every triplet must end with a period \[13-15\].

- **Formula Blocks (****{...}****):** Define a query block that is executed as a single unit, forming a single iterator result \[7, 13-15, 23-28\]. These are crucial for grouping operations.

- **Lists (****(...)****):** Used to define ordered collections of values or variables \[7, 13-15, 23-25, 28-30\]. They can be used to pass multiple arguments to built-in functions \[30\].

- **Prefixes (****@prefix****):** Define shortcuts for long URIs (Uniform Resource Identifiers), improving readability \[13-15, 31-35\].

- **Comments (****#****):** Used to add notes within the query \[13-15, 36\].

- **Implicit Subject (****\[...\]****):** Square brackets can implicitly refer to the subject of the previous triplet, simplifying syntax \[13, 14, 27\].

- **Reserved Keywords:** a (for rdf:type - "is an instance of"), is ... of (inverse property) \[13-15, 36\].

- **Assignment (****\=****):** Assigns a value from one variable to another \[13-15, 24\].

- **Conditional (****if ... else ...****):** Controls query flow. If the if condition is false and there's no else block, the query stops execution \[10, 13, 14, 25, 37, 38\].

N3 Query Execution Model

The execution of N3 queries follows a distinct model:

- **Sequential Execution:** Queries execute top-down, line by line \[3, 13, 27, 39\].

- **Iterative Processing:** If a line (triplet) returns an iterator (multiple values), the subsequent lines are executed for each value in that iterator \[3, 13, 27, 39, 40\]. This creates a nested loop behavior, meaning the query engine "walks" the graph from node to node via edges (predicates) \[1, 3, 41\].

- **Iterator Scope:** An iterator's scope is confined to the formula/block it was created in. Once the block finishes, the iterator's result is passed as a single value (or a collection) to the next level \[3, 13, 27, 40, 42, 43\].

- **Performance Optimization:** The **order of triplets significantly impacts performance** \[1, 3, 16, 40, 41, 44, 45\]. Queries should start with the **most restrictive conditions** to minimize the size of initial iterators, rather than following a traditional relational database's "FROM-WHERE" pattern \[1, 3, 16, 45-47\]. Starting with highly selective conditions reduces the number of iterations required for subsequent triplets \[8\].

Common Query Patterns and Operators

- **object:findProperty**: A built-in predicate used to retrieve the ID of an attribute given its template alias and attribute alias (e.g., ("TemplateAlias" "AttributeAlias") object:findProperty ?attributeId) \[10, 13, 23, 33, 35, 45, 47-49\]. This is highly optimized as it always returns a single ID.

- **assert:union**: Combines the results of multiple iterators into a single iterator. assert:union true performs a "union all" operation, including duplicates \[10, 13, 18, 23, 25, 43, 50\].

- **ones**: Executes a query and returns only the first successful result, stopping further iteration once a match is found \[13, 23, 24, 51\].

- **or**: Evaluates multiple conditions and returns true if any of them are met, stopping once the first successful condition is found \[13, 23, 25, 38, 51\].

- **Built-in Functions**: Special predicates (e.g., math:sum, time:dayOfWeek) that perform calculations in memory rather than querying the database \[4, 13, 23, 26, 30, 52-54\]. They can operate on lists of values.

- **item** **and** **value**: Reserved keywords for input and output parameters, respectively, in expressions \[4, 10, 13, 16, 18, 23, 24, 27, 29, 37, 39, 55-57\]. item typically represents the ID of the current object/record, while value stores the query's output. Their specific meanings can vary depending on the query's application context \[29\].

Data Representation and Storage for N3 Queries

All data in the N3 database, including systemic metadata and user-applied data, is stored as triplets \[1, 2, 4-7, 23, 37, 58, 59\]. This data can take several forms within a triplet:

- **Qualified Name (QName)**: Shortened forms of long URIs used for subjects, predicates, and objects, especially for complex types \[1, 5, 7, 23, 32, 33\].

- **Simple Literals**: Direct, atomic values like strings, numbers, booleans, dates, or durations \[1, 5, 7, 23, 33, 59\].

- **Complex Literals**: Represent collections of facts or ordered sets of values, used in advanced queries, specifically **Formulas (****{...}****)** and **Lists (****(...)****)** \[1, 7, 23, 28, 30\].

- **Axioms vs. Derived Facts**:

    - **Axioms** are facts directly stored as triplets in the database \[1, 7, 10, 23, 24, 56, 57\].

    - **Derived facts** are computed on the fly based on axioms and the current context (e.g., calculated attributes) and are **not stored** in the database \[1, 7, 10, 23, 24, 42, 56, 57, 60-62\]. This ensures they always reflect the most current underlying data \[8, 61\].

Application Contexts for N3 Queries

N3 queries are utilized in various platform features to define dynamic behavior:

- **Calculated Attributes**: Compute values dynamically for a record template, not stored but calculated on-the-fly when requested \[4, 8, 10, 13, 19, 27, 37, 57, 60-62\]. item is the input (current object ID), and value is the output.

- **List Filters**: Filter records displayed in a list. item is the output (IDs of records to display), with no input item \[4, 13, 21, 37, 63, 64\].

- **Operations (Conditional Display)**: Show or hide operations based on conditions. item is the input (current record ID), and value is true (show) or false (hide) \[4, 13, 21, 65\].

- **Business Rules (Triggers/Scenarios)**: Define actions that execute based on specific events (e.g., field change), often involving complex N3 queries for conditions or value derivation \[13, 60, 65\].

- **Global Functions**: External functions (e.g., written in C#) can be invoked from N3 queries to perform complex computations or retrieve data from external services, promoting code reusability \[13, 60, 65-68\].

The development environment for N3 queries is continuously improving, with new compilers and editors being designed to provide better error highlighting and code assistance \[69\].

\--------------------------------------------------------------------------------

N3/RDF Triplet Data: Structure, Storage, and Querying

**Triplet data** serves as the **fundamental unit of data storage** within an **N3/RDF graph database** \[1-3\]. These atomic building blocks are crucial for capturing facts and relationships, enabling a comprehensive semantic data representation and efficient querying \[1, 4\].

Components of a Triplet

Each triplet is comprised of three indispensable parts \[1-3\]:

- **Subject**: This element represents the resource being described and acts as the **source of the arrow** in a graph visualization \[1-3\].

- **Predicate**: This signifies the **property or relationship** between the subject and object, typically depicted as the **arrow itself** in a graph \[1-3\].

- **Object**: This is the value or resource to which the subject is related, forming the **destination of the arrow** \[1-3\].

For instance, in the statement "Person owns Car," "Person" is the subject, "owns" is the predicate, and "Car" is the object \[1\]. The entire database, encompassing both **systemic metadata** (definitions of classes, properties, and relationships) and **user-applied data** (instances and records), is stored exclusively as these triplet facts \[1, 3, 5-10\].

Directionality of Triplets

**Directionality is a crucial aspect of triplets** \[1-3\]. It explicitly defines the flow of a relationship, making statements like "Person owns Car" distinct from "Car owned\_by Person" \[1-3\]. This inherent directionality determines which element functions as the Subject and which as the Object, which is vital for structuring N3 queries to retrieve specific information \[1-3\]. The choice of direction during data modeling can significantly influence how queries are subsequently constructed \[2, 3\]. As discussed, this means that understanding how the platform's core systemic model is designed with specific directions for its attributes is essential, and user-defined models also require careful consideration of directionality for effective querying \[2, 11\].

Data Storage and Representation in Triplets

All data in the N3 database, whether it pertains to system models or user-applied data, is persisted as triplets \[1, 3, 5-7, 9, 10\]. System models are typically defined in .n3 files, while applied data (metadata and instances) is stored in separate files like data.n3 \[1, 5, 6, 9\]. While the platform leverages an SQLite engine for transactional operations, its core data model and the serialization/deserialization logic between triplets and relational views are custom-built \[1, 5, 6, 9, 10\]. This custom approach is considered a key innovation, providing speed and unique data handling principles \[10\].

Triplets can represent data in several forms for their Subject, Predicate, or Object components \[1, 5, 6\]:

- **Qualified Name (QName)**: These are shortened forms of long URIs (Uniform Resource Identifiers) used to represent resources, especially for complex types \[1, 3, 5, 6, 12\]. QNames are commonly employed for subjects, predicates, and objects \[1, 3, 5, 6\]. For example, object:findProperty is a QName where object is a prefix for a longer URI \[5, 13\].

- **Simple Literals**: These represent direct, atomic values such as strings ("blue"), numbers (5), booleans (true), dates, or durations \[1, 5, 6, 13, 14\].

- **Complex Literals**: These are used in advanced queries to represent collections of facts or ordered sets of values \[1, 5, 6, 15\].

    - **Formulas (****{...}****):** A set of triplets that are evaluated together as a single unit \[1, 5, 6, 15, 16\]. This allows for complex logic within a single block.

    - **Lists (****(...)****):** An ordered collection of values or variables \[1, 5, 6, 15\]. These are useful for passing multiple arguments to functions or defining a sequence of items \[17\].

- **Axioms vs. Derived Facts**:

    - **Axioms** are facts directly stored as triplets in the database \[1, 5, 6, 9\]. They represent the persistently stored data \[18\].

    - **Derived facts** are computed on the fly based on axioms and the current context (e.g., calculated attributes) and are **not stored** in the database \[1, 5, 6, 9\]. Calculated attributes, for instance, are always computed on demand when the attribute is requested, ensuring they reflect the most current underlying data \[5, 9, 18-21\]. This on-the-fly computation means that changes to source data automatically trigger re-calculation of derived facts upon access \[19, 21\].

Triplet Interaction with N3 Querying

N3 queries operate directly on these triplet structures \[1, 9\]. The language's syntax elements, such as the triplet terminator (.), formula blocks ({...}), and lists ((...)), are fundamental to defining and structuring triplets within queries \[22\].

- When parts of a triplet in a query are **variables** (e.g., ?S P ?O), the system performs a **search** in the database to find matching facts and populate the variables with iterators (sequences of values) \[1, 23\].

- If **all parts of a triplet are known values**, the system performs a **match** to check for the exact fact's existence, returning true or false \[1, 23\]. This operation does not return an iterator \[23\].

Understanding the structure and directionality of triplets is fundamental for building effective N3 queries, as the way data is stored directly influences how information can be retrieved and processed \[3, 24\]. The sequential and iterative execution model of N3 queries means that the order of triplets significantly impacts performance, as queries should start with the most restrictive conditions to minimize the size of initial iterators \[1, 23\].

\--------------------------------------------------------------------------------

N3 Queries: Graph Database Interaction and Semantics

**N3 (Notation3) queries** are a fundamental aspect of interacting with graph databases that are structured around ontological models and triplets \[1-3\]. N3 is a **compact and human-readable syntax for RDF (Resource Description Framework)**, which also supports logical expressions \[1-4\]. Its design allows it to operate directly on the triplet data structure of the database \[1, 5, 6\].

Core Syntax Elements

N3 queries use several key syntax elements to define and structure their logic \[7\]:

- **Comments (****#****)**: Used for adding notes within the query \[7\].

- **Prefixes (****@prefix****)**: Define shortcuts for long URIs, enhancing readability and making queries more concise \[7\]. For example, object: is a prefix for a longer URI related to object properties \[1, 5, 8\].

- **Variables (****?****)**: Represent unknown values that the query aims to discover. They are denoted by a question mark followed by an alphanumeric name (e.g., ?item, ?value) \[7\].

- **Triplet Terminator (****.****)**: Every triplet expression in an N3 query must end with a period \[7\].

- **Formula Block (****{...}****)**: Defines a query block that is executed as a single unit, forming a single iterator result \[5, 7\].

- **Lists/Arrays (****(...)****)**: Used to define ordered collections of values or variables \[5, 7\].

- **Implicit Subject (****\[...\]****)**: Square brackets can implicitly refer to the subject of the previous triplet, simplifying syntax \[7\].

- **Reserved Keywords**: Include a (for rdf:type, meaning "is an instance of") and is ... of (for inverse properties) \[7\].

- **Assignment (****\=****)**: Assigns a value from one variable to another \[7\].

- **Conditional (****if ... else ...****)**: Controls query flow. If the if condition is false and there's no else block, the query's execution path effectively terminates \[7, 9\].

Triplet Interaction and Query Types

N3 queries operate directly on **triplet structures**, which consist of a **Subject**, a **Predicate**, and an **Object** \[1-4\]. The **directionality** of triplets is crucial, as it dictates which element is the Subject and which is the Object, fundamentally influencing how queries must be structured \[1-4, 8\].

Queries can perform two main types of operations on triplets \[3, 5\]:

- **Search (Unknowns)**: When one or more parts of a triplet in a query are variables (e.g., ?S P ?O), the system performs a search in the database to find matching facts and populates the variables with **iterators** (sequences of values) \[1, 3, 5\]. This is used to discover subjects, objects, or both, based on known predicates or other parts of the triplet \[3, 5\].

- **Match (All Known)**: When all parts of a triplet are known values, the system performs a match to check for the **exact fact's existence** in the database, returning true or false \[1, 3, 5\]. This type of query does not return an iterator \[3, 5\].

Query Execution Model

N3 queries follow a **sequential and iterative execution model** \[1, 3\]:

- **Sequential Execution**: Queries execute top-down, line by line \[3\].

- **Iterative Processing**: If a line (triplet) returns an iterator (multiple values), the subsequent lines are re-executed for each value in that iterator, creating a nested loop-like behavior \[3, 9, 10\].

- **Iterator Scope**: An iterator's scope is confined to the formula or block in which it was created. Once the block finishes, the iterator's result is passed as a single value (or a collection) to the next level \[3\]. This "loop-join" behavior is fundamental to how N3 "walks" the graph to retrieve information \[1, 11, 12\].

Query Optimization

The sequential and iterative nature of N3 query execution significantly impacts performance \[1, 3, 9\]. To optimize queries, it is essential to **start with the most restrictive conditions** to minimize the size of initial iterators \[1, 3, 12, 13\]. This often means "flipping" the query's structure compared to traditional relational database query patterns \[1, 12\].

Contextual Variables

In various N3 query contexts, reserved variables like item and value are used \[7\]:

- **item**: Typically represents the ID of the current object or record in the query's context (e.g., in calculated attributes or operations) \[7, 14, 15\].

- **value**: Represents the output parameter where the result of a query or calculation is stored \[7, 14, 15\]. Its expected type can vary depending on the context (e.g., boolean for operations, ID for list filters, or a literal for calculated attributes) \[16\].

Built-in Predicates and Operators

N3 provides specialized predicates and operators for common tasks \[5\]:

- **object:findProperty**: A built-in predicate used to retrieve the unique ID of an attribute given its template alias and attribute alias (e.g., ("TemplateAlias" "AttributeAlias") object:findProperty ?attributeId) \[1, 5, 9\]. It's highly optimized and returns a single ID \[5\].

- **assert:union**: Combines the results of multiple iterators into a single iterator. assert:union true performs a "union all" operation, including duplicates \[5, 9, 17, 18\].

- **ones**: Executes a query and returns only the first successful result, stopping further iteration once a match is found \[5, 19\].

- **or**: Evaluates multiple conditions and returns true if any are met, stopping once the first successful condition is found \[5, 19, 20\].

- **Built-in Functions**: Special predicates like math:sum or time:dayOfWeek perform calculations in memory rather than querying the database \[5, 21-23\].

Application Contexts for N3 Queries

N3 queries are used across various platform contexts \[15\]:

- **Calculated Attributes**: Define properties whose values are computed dynamically on demand and are not stored in the database \[9, 13, 14, 24-26\]. item is the input (current object ID), and value is the output \[14\].

- **List Filters**: Used to filter records displayed in a list. item represents the output (IDs of records to display), with no input item \[15, 27\].

- **Operations (Conditional Display)**: Used to show or hide operations (like a "Complete Task" button) based on conditions. item is the input (current record ID), and value is true (show) or false (hide) \[15, 27\].

- **Business Rules (Triggers/Scenarios)**: Define actions that execute based on specific events (e.g., a field change), often involving complex N3 queries to determine conditions or derive values \[15, 24\].

- **Global Functions**: External functions (e.g., written in C#) can be invoked from N3 queries to perform complex computations or retrieve data from external services not directly expressible in N3 \[15, 28-30\].

Data Types in Triplets and N3 Queries

N3 queries interact with various data types stored as triplet objects \[1, 5, 8\]:

- **Qualified Name (QName)**: Shortened forms of URIs representing resources, used for subjects, predicates, and objects, especially for complex types \[1, 5, 8, 31\].

- **Simple Literals**: Direct values such as strings, numbers, booleans, dates, or durations \[1, 5, 8, 32, 33\].

- **Complex Literals**: Represent collections of facts or ordered sets of values, used in advanced queries \[1, 5, 8\].

    - **Formulas (****{...}****)**: A set of triplets evaluated together as a single unit \[1, 5, 8, 34\].

    - **Lists (****(...)****)**: An ordered collection of values or variables \[1, 5, 8, 34\].

Axioms vs. Derived Facts

N3 queries distinguish between:

- **Axioms**: Facts directly stored as triplets in the database \[1, 5, 8, 9, 25\].

- **Derived Facts**: Computed on the fly based on axioms and the current query context (e.g., calculated attributes). They are **not stored** in the database but are computed at the moment of access \[1, 5, 8, 9, 13, 24-26\]. This distinction impacts performance and data integrity, as derived facts are always current but require re-computation upon request \[13, 35\].

\--------------------------------------------------------------------------------

The Essence of Triplet Data in N3 Databases

**Triplets** are the **fundamental unit of data storage** in an **N3/RDF graph database** \[1-3\]. They are the atomic building blocks that capture facts and relationships within a graph database, enabling semantic data representation and querying \[4\].

Components of a Triplet

Every triplet consists of three essential parts \[1, 2\]:

- **Subject**: This is the resource being described, acting as the source of the arrow in a graph \[1, 2\].

- **Predicate**: This represents the property or relationship between the subject and object. It is visualized as the arrow itself in a graph \[1, 2\].

- **Object**: This is the value or resource that the subject is related to, forming the destination of the arrow \[1, 2\].

For example, in the statement "Person owns Car," "Person" would be the subject, "owns" the predicate, and "Car" the object \[1\]. The data in an N3 database, including both **systemic metadata** (definitions of classes, properties, and relationships) and **user-applied data** (instances and records), is entirely stored as these triplet facts \[1, 3, 5\].

Directionality of Triplets

**Directionality is crucial for triplets** because it explicitly defines the flow of a relationship \[1, 2, 5\]. For instance, "Person owns Car" is distinct from "Car owned\_by Person" \[1, 5\]. This directionality dictates which element functions as the Subject and which as the Object, which is vital for structuring N3 queries to retrieve specific information \[1, 2, 5\]. The choice of direction when modeling can significantly impact how queries are later built \[6\].

Data Storage and Representation in Triplets

All data within the N3 database, whether it describes system models or applied user data, is stored as triplets \[1, 3\]. System models are typically defined in .n3 files, while applied data is found in separate files like data.n3 \[1, 3\]. Although the platform uses an SQLite engine for transactional aspects, its core data model and the logic for serializing/deserializing data between triplets and relational views are custom-built \[1, 3, 5, 7\].

Triplets can represent data in several forms for their Subject, Predicate, or Object components:

- **Qualified Name (QName)**: These are shortened forms of long URIs (Uniform Resource Identifiers) used to represent resources, especially for complex types \[1, 3, 8\]. QNames are commonly used for subjects, predicates, and objects \[1, 3\]. An example would be object:findProperty where object is a prefix for a longer URI \[3\].

- **Simple Literals**: These are direct values such as strings ("blue"), numbers (5), booleans (true), dates, or durations \[1, 3\].

- **Complex Literals**: These represent collections of facts or ordered sets of values, utilized in advanced queries \[1, 3\].

    - **Formulas (****{...}****):** A set of triplets that are evaluated together as a single unit \[1, 3, 9\].

    - **Lists (****(...)****):** An ordered collection of values or variables \[1, 3, 9\].

- **Axioms vs. Derived Facts**:

    - **Axioms** are facts directly stored as triplets in the database \[1, 3\].

    - **Derived facts** are computed on the fly based on axioms and the current context (e.g., calculated attributes) and are **not stored** in the database \[1, 3, 10-12\]. Calculated attributes, for instance, are always computed on demand when the attribute is requested \[10, 11, 13\].

Triplets and N3 Querying

N3 queries operate directly on these triplet structures \[1, 9\]. The language's syntax elements like the triplet terminator (.), formula blocks ({...}), and lists ((...)) are fundamental to defining and structuring triplets within queries \[9\].

- When parts of a triplet in a query are **variables** (e.g., ?S P ?O), the system performs a **search** in the database to find matching facts and populate the variables with iterators (sequences of values) \[1, 14\].

- If **all parts of a triplet are known values**, the system performs a **match** to check for the exact fact's existence, returning true or false \[1, 14\].

Understanding the structure and directionality of triplets is fundamental for building effective N3 queries, as the way data is stored directly influences how information can be retrieved \[5, 6, 15\].

\--------------------------------------------------------------------------------

Ontology, Graphs, and Triplet Data Models

**Ontological models** serve as the conceptual framework for defining entities and their connections within information systems \[1\]. In the realm of Information Technologies (IT), an ontology is formally described as **a set of objects, their properties, and the relationships between them** \[2-6\]. Its primary purpose is to provide a structured and machine-readable representation of a specific domain or the real world \[4, 6\].

Core Concepts of Ontology

An ontological model fundamentally consists of three main components \[3, 4\]:

- **Objects (Entities)**: These are the core elements or things being described, such as "Pencil Case" or "Pencil" \[3, 4, 7\].

- **Characteristics/Properties (Attributes)**: These define the qualities or attributes of the objects, like "Material" and "Capacity" for a "Pencil Case," or "Color," "Condition," and "Hardness" for a "Pencil" \[3, 4, 7\].

- **Interactions/Relationships (Connections)**: These define how objects are connected to each other, such as "Pencil Case contains Pencil" \[3, 4, 7\].

The "Pencil Case contains Pencil" example illustrates a one-to-many relationship, where a pencil case can hold multiple pencils, but a pencil can be in zero or one pencil case. This relationship signifies that the pencil case possesses the property of containing pencils \[4, 7, 8\].

Application to Graph Databases

**Graph databases naturally represent ontological models** \[2-4\]. In this context:

- **Nodes (Vertices)** typically represent the **objects, classes, or instances** defined in the ontology \[2-4, 9\]. For example, "Person" and "Car" can be nodes representing classes, or "Ivan Ivanovich" and a "Volvo car" can be nodes representing specific instances \[2, 4, 9\].

- **Edges (Relations)** represent the **relationships** between these nodes \[2-4, 9\]. For instance, "owns" would be an edge connecting a "Person" node to a "Car" node \[2, 4, 9\].

Graph databases support various graph types, including directed and undirected graphs, which reflect the nature of relationships in an ontology \[2-4, 10, 11\]. This structure makes them particularly well-suited for semantic queries \[2, 3, 12\].

Relationship with Triplets (N3 and RDF)

The ontological model directly translates into the fundamental unit of data storage in an N3/RDF graph database: the **triplet** \[2-4, 8, 11\].

- A triplet consists of a **Subject**, a **Predicate**, and an **Object** \[2-4, 13, 14\]. This structure directly reflects an ontological statement: the Subject is the entity being described, the Predicate is its property or relationship, and the Object is the value or related entity \[2, 4, 13, 14\].

- **Directionality is crucial for triplets**; it explicitly defines the flow of a relationship (e.g., "Person owns Car" versus "Car owned\_by Person") \[2-4, 14, 15\]. This direction dictates which element serves as the Subject and which as the Object, which in turn significantly influences how queries must be structured to retrieve information \[2-4, 15\].

All data in the N3 database, including **systemic metadata** (definitions of classes, properties, and their relationships) and **user-applied data** (instances, records), is stored as these triplet facts \[2-4, 16, 17\]. System models are described in .n3 files, while applied data is stored in separate files like data.n3 \[2, 3, 16\]. The platform's core systemic model is fixed and uses specific predicates, but user-defined custom models also create triplets, and their directionality is important for query construction \[3, 16\]. Understanding how these underlying facts are structured in the N3 database is fundamental to building effective N3 queries \[4, 15\].

In essence, ontology provides the conceptual framework, graph databases offer the structural means to store this information, and triplets serve as the atomic units that capture these ontological facts, forming the basis for semantic data representation and querying \[1, 4\]. The platform's core data model and the logic for handling data between triplets and relational views are custom-built, even though an SQLite engine is used for transactional aspects \[2-4, 17\].

\--------------------------------------------------------------------------------

System Models and N3 Database Integration

**System models** are a fundamental component of the platform's data architecture, providing a formal and structured description of core entities, their properties, and the relationships between them in the context of information technologies \[1-4\]. These models function as **systemic metadata**, defining elements such as class structures and property types \[3-5\]. They represent the platform's **fixed, core systemic model** \[6\] and are not directly editable by users \[7, 8\].

Here's how system models integrate into the larger context of N3 database data storage:

- **Description in .n3 Files**

    - System models are explicitly **described in dedicated** **.n3** **files** \[1, 3, 9-11\]. These files act as the "dictionary" for the system's foundational elements \[12\].

    - They typically come pre-installed with the platform and can be inspected by users \[11, 12\].

    - The definitions within these .n3 files are largely static, changing primarily with platform upgrades or new versions \[12\]. Adding new parameters or functionalities to these models requires developer intervention \[12\].

- **Integration with N3 Database Data Storage**

    - **Triplet-Based Foundation**: The N3 database stores **all data—both system models (systemic metadata) and user-applied data (instances and records)—as triplets** \[1, 3, 4, 9-11, 13\]. A triplet consists of a Subject, Predicate, and Object, representing a single fact or relationship \[1, 6, 14-17\].

    - **Graph Structure**: This triplet storage naturally forms a **graph structure**, where **nodes** represent entities (like classes defined in system models, e.g., "Person" or "Car") and **edges** represent relationships between these nodes (e.g., "owns") \[1, 2, 4\]. System models directly define these fundamental nodes and edges \[1, 6, 13, 18\].

    - **Crucial Directionality**: The **directionality of relationships** within triplets is critical \[1, 3, 4, 6, 14, 19, 20\]. This direction dictates which element is the Subject and which is the Object, significantly influencing how data is stored and how subsequent queries must be structured to retrieve information \[1, 3, 4, 6, 14, 19, 20\]. This principle applies uniformly to both system-defined and user-defined relationships.

    - **Custom Data Model and SQLite**: While the platform leverages an **SQLite engine for transactional operations** \[1, 3, 4, 9-11\], the **core data model and the logic for converting data between triplets and relational views are custom-built** by the platform developers \[1, 3, 4, 9-11\]. This custom architecture is patented and is central to how the platform stores and manages data \[11\]. N3 queries operate directly on this triplet structure, effectively "walking" the graph to retrieve or verify information \[1, 21\].

    - **File Segregation**: To maintain clarity and separation, system models are stored in .n3 files, distinct from user-applied data (metadata and instances), which reside in separate files such as data.n3 \[1, 3, 9-11\]. This separation underscores the distinction between the fixed, underlying system definitions and the dynamic, user-generated content.

\--------------------------------------------------------------------------------

Graph Databases and N3 Querying Fundamentals

**Graph databases** are a type of database that uses **graph structures** to represent and store data, and they are particularly well-suited for semantic queries \[1-3\]. This data is organized using **nodes**, **edges**, and properties \[1-3\]. **N3 (Notation3) querying** directly interacts with these graph structures by leveraging their fundamental unit of storage: the **triplet** \[1, 4, 5\].

Graph Databases

A graph database fundamentally represents data using **graph structures** \[1\]. Its two main components are:

- **Nodes (Vertices):** These represent entities or values, such as classes, instances, or literal values \[1-3\]. In the platform context, nodes can be abstract concepts like "Pencil Case" or "Pencil," or specific instances like "Ivan Ivanovich" or a "Volvo car" \[1\].

- **Edges (Relations):** These represent **relationships** between nodes. Edges can be either directed or undirected \[1-3\]. They signify how different entities are connected, for example, "Pencil Case contains Pencil" or "Person owns Car" \[1\].

Graph databases can support various types of graphs, including connected, isolated, directed, undirected, complete, planar, and tree-like graphs \[1, 2\].

**Application to Ontology**: Graph databases are naturally suited to represent **ontological models** \[1-3\]. In information technology, an ontology formally describes a set of objects, their properties, and the relationships between them \[1, 3\]. In such a model, **nodes** typically represent objects, classes, or instances, while **edges** represent the relationships between them \[1, 3\]. For instance, "Person" and "Car" could be nodes, and "owns" would be an edge connecting them \[1\].

N3 Querying

The fundamental unit of data storage in an N3/RDF graph database is a **triplet** \[1, 3, 4\]. The entire database, encompassing both **systemic metadata** (definitions of classes, properties, and relationships) and **user-applied data** (instances and records), is stored as these triplet facts \[1, 3, 6\]. System models are described in .n3 files, while applied data is stored in separate files like data.n3 \[1, 6\]. The platform uses an SQLite engine for transactional aspects, but its core data model and the logic for serializing/deserializing data between triplets and relational views are custom \[1, 3, 6\].

**Components of a Triplet**: A triplet consists of three essential parts \[1, 3, 4\]:

- The **Subject**: The resource being described, acting as the source of the arrow in a graph \[1, 4\].

- The **Predicate**: The property or relationship, represented as the arrow itself \[1, 4\].

- The **Object**: The value or resource that the subject is related to, forming the destination of the arrow \[1, 4\].

**Directionality**: **Directionality is crucial for triplets**; it explicitly defines the flow of a relationship (e.g., "Person owns Car" versus "Car owned\_by Person") \[1, 3, 4\]. This direction dictates which element is the Subject and which is the Object, and consequently, how queries must be structured to retrieve information \[1, 3, 4, 7\].

**Types of Data in Triplets**: Data within triplets can be represented in various forms \[1, 6\]:

- **Qualified Name (QName):** These are shortened forms of long URIs (Uniform Resource Identifiers) used to represent resources, especially for complex types. QNames are typically used for subjects, predicates, and objects \[1, 6, 8\].

- **Simple Literals:** These are direct values like strings ("blue"), numbers (5), booleans (true), dates, or durations \[1, 6\].

- **Complex Literals:** These represent collections of facts or ordered sets of values, used in advanced queries \[1, 6\].

    - **Formulas (****{...}****):** A set of triplets that are evaluated together as a single unit \[1, 6\].

    - **Lists (****(...)****):** An ordered collection of values or variables \[1, 6\].

- **Axioms vs. Derived Facts**: **Axioms** are facts directly stored as triplets in the database \[1, 6\]. **Derived facts** are computed on the fly based on axioms and the current context (e.g., calculated attributes) and are **not stored** in the database \[1, 6, 9, 10\]. Calculated attributes, for instance, are always computed on demand \[10, 11\].

**N3 Query Syntax and Execution**: N3 queries operate directly on these triplet structures \[1, 5, 12\]. The language has specific syntax elements like comments (#), prefixes (@prefix), variables (?), and a triplet terminator (.) \[13\]. Reserved keywords include a (for rdf:type) and is ... of (for inverse properties) \[13\]. **item** and **value** are reserved variables often representing the current object ID and the output parameter, respectively \[5, 14-16\].

**Query Execution Model**:

- **Sequential and Iterative**: N3 queries execute top-down, line by line \[17\]. If a line (triplet) returns an **iterator** (multiple values), subsequent lines are executed for each value in that iterator, creating nested loops \[17-19\].

- **Iterator Scope**: An iterator's scope is confined to the formula/block it was created in. Once the block finishes, the iterator's result is passed as a single value (or a collection) to the next level \[17, 18\].

- **Optimization**: The **order of triplets significantly impacts performance** \[11, 12, 17\]. Queries should start with the most restrictive conditions to minimize the size of initial iterators, often requiring "flipping" the query compared to traditional relational database patterns \[1, 11, 12, 17, 20, 21\].

- **Search vs. Match**:

    - When parts of a triplet are **variables** (e.g., ?S P ?O), the system performs a **search** in the database to find matching facts and populate the variables with iterators \[1, 5, 17\].

    - If **all parts of a triplet are known values**, the system performs a **match** to check for the exact fact's existence, returning true or false \[1, 5, 17\].

**Common Query Patterns and Operators**:

- **object:findProperty**: A built-in predicate used to retrieve the unique identifier (ID) of an attribute given its template alias and attribute alias \[5, 21-23\].

- **assert:union**: Combines the results of multiple iterators into a single iterator. assert:union true performs a "union all," meaning duplicates are included \[5, 22-24\].

- **ones**: Executes a query and returns only the first successful result, stopping further iteration once a match is found \[5, 22, 25\].

- **or**: Evaluates multiple conditions and returns true if any of them are met, stopping once the first successful condition is found \[5, 22\].

- **Built-in Functions**: Special predicates like math:sum or time:dayOfWeek perform calculations in memory rather than querying the database \[5, 22\].

**Application Contexts for N3 Queries**: N3 queries are used in various platform contexts to define behavior and derive information \[26, 27\]:

- **Calculated Attributes**: Dynamically compute attribute values on a record template. item is the input (current object ID), and value is the output. These values are not stored in the database \[11, 26\].

- **List Filters**: Filter records displayed in a list. item is the output (IDs of records to display) \[16, 26\].

- **Operations (Conditional Display)**: Control the visibility of operations (e.g., buttons) based on conditions. item is the input (current record ID), and value is true (show) or false (hide) \[27, 28\].

- **Business Rules (Triggers/Scenarios)**: Define actions that execute based on specific events, often involving complex N3 queries to determine conditions or derive values \[9, 27\].

- **Global Functions**: External functions (e.g., written in C#) can be invoked from N3 queries for reusability, complex computations, or retrieving data from external services \[27, 29, 30\].

\--------------------------------------------------------------------------------

Ontology and Graph Database Fundamentals

**Ontology** is a core concept that underpins how data is structured and understood in graph databases, particularly in the context of semantic queries \[1-4\].

Here's a discussion of ontology concepts:

- **Definition of Ontology**

    - Philosophically, ontology is the study of being, existence, and the fundamental categories of reality \[2, 4\].

    - In the realm of **information technologies (IT)**, ontology describes a **formal description of a set of objects, their properties, and the relationships between them** \[1-3, 5, 6\]. Its primary purpose in IT is to provide a structured and machine-readable representation of a specific domain or the real world \[6\].

- **Core Components of Ontology**An ontological model fundamentally consists of three main components \[2, 4\]:

    - **Objects (Entities):** These are the core elements or things being described.

    - **Characteristics/Properties (Attributes):** These define the qualities or attributes of the objects.

    - **Interactions/Relationships (Connections):** These define how objects are connected to each other.

- **Real-world Analogy**To illustrate these concepts, consider the example of "pencils in a pencil case" \[2, 7\]:

    - **Classes:** "Pencil Case" and "Pencil" can be defined as classes \[2, 7\].

    - **Properties:** A "Pencil Case" might have properties like "Material" and "Capacity," while a "Pencil" might have "Color," "Condition" (e.g., sharp, dull), and "Hardness" \[2, 7\].

    - **Relationship:** The relationship could be "Pencil Case contains Pencil." This relationship can be specified as one-to-many, where a pencil case can contain multiple pencils, but a pencil can be in zero or one pencil case \[2, 7\]. This relationship signifies that the pencil case has the property of containing pencils \[8\].

- **Application to Graph Databases** **Graph databases naturally represent ontological models** \[1, 3\]. In this context:

    - **Nodes (Vertices)** typically represent the **objects, classes, or instances** defined in the ontology \[1, 3, 9, 10\]. For example, "Person" and "Car" could be nodes representing classes, or "Ivan Ivanovich" and a "Volvo car" could be nodes representing instances \[1, 10\].

    - **Edges (Relations)** represent the **relationships** between these nodes \[1, 3, 9, 10\]. For instance, "owns" would be an edge connecting a "Person" node to a "Car" node \[1, 9\]. Graph databases can support various graph types, including directed and undirected graphs, which reflect the nature of relationships in an ontology \[1, 3\].

- \*\*Relationship with Triplets (N3 and RDF)\*\*The ontological model translates directly into the fundamental unit of data storage in an N3/RDF graph database: the **triplet** \[9, 11, 12\].

    - A triplet consists of a **Subject**, a **Predicate**, and an **Object** \[9, 11-15\]. This structure directly reflects an ontological statement: the Subject is the entity being described, the Predicate is its property or relationship, and the Object is the value or related entity \[9, 15\].

    - **Directionality is crucial for triplets** \[6, 9, 11, 13, 15, 16\]. It explicitly defines the flow of a relationship (e.g., "Person owns Car" versus "Car owned\_by Person"). This direction dictates which element serves as the Subject and which as the Object, which in turn significantly influences how queries must be structured to retrieve information \[6, 9, 11, 13, 16\].

    - The entire database, including both **systemic metadata** (definitions of classes, properties, and their relationships) and **user-applied data** (instances, records), is stored as these triplet facts \[13, 17-22\]. Understanding how these underlying facts are structured in the N3 database is fundamental to building effective N3 queries \[16, 20\].

    - N3 (Notation3) is a human-readable syntax used for RDF that also supports logical expressions \[9, 11, 23\]. The system's core data model and logic for handling data between triplets and relational views are custom, even though an SQLite engine is used for transactional aspects \[13, 17, 19, 21\].

In essence, ontology provides the conceptual framework for defining entities and their connections, graph databases offer the structural means to store this information, and triplets serve as the atomic units that capture these ontological facts, forming the basis for semantic data representation and querying \[23\].

\--------------------------------------------------------------------------------

N3/RDF: Graph Database Concepts and Querying

Please note: Some terms and names in the sources are in Russian and have been transliterated or translated for clarity in the timeline and character list.

Detailed Timeline of Main Events

The provided sources do not describe a sequential narrative of events but rather explain technical concepts and their application. Therefore, this timeline focuses on the **conceptual progression and development of the N3/RDF graph database and its querying capabilities** as presented in the source material.

- **Ancient Greek Philosophy (Ontology's Origin):** Ontology, as the "study of being, existence, and the fundamental categories of reality," originated from ancient Greek philosophy \[Source: N3 Querying, I.A. Ontology and its Application\].

- **Mathematical Concept of Graphs:** The abstract mathematical concept of graphs, comprising vertices (nodes) and edges (relations), forms the theoretical foundation \[Source: Graph Databases, Types of Graphs; n3 p1\]. Graphs can be connected, isolated, directed, undirected, complete, planar, or tree-like \[Source: Graph Databases, Types of Graphs\].

- **Emergence of Ontology in Information Technologies:** In IT, ontology describes a structured set of objects, their properties, and relationships. It is a formal, machine-readable representation of a domain \[Source: N3 Querying, I.A. Ontology and its Application; Part 1\].

- **Development of Resource Description Framework (RDF):** The World Wide Web Consortium (W3C) developed RDF as a standard for describing web resources, often represented in XML or N3 \[Source: N3 Querying, I.C. Triplets (N3 and RDF); Part 1\].

- **Introduction of Notation3 (N3):** N3 emerged as a compact, human-readable syntax for RDF, supporting logical expressions, designed for describing resources and relationships \[Source: N3 Querying, I.C. Triplets (N3 and RDF); Part 1\].

- **Founding of the Graph Database Concept:** Graph databases are defined as a type of database using graph structures (nodes, edges, properties) to store and represent data, particularly well-suited for semantic queries \[Source: Graph Databases, Definition and Components; N3 Querying, I.B. Graph Databases\].

- **Establishment of Triplets as Fundamental Data Unit:** The triplet (Subject, Predicate, Object) is established as the fundamental unit of data storage in N3/RDF graph databases \[Source: Graph Databases, Relationship with Triplets; N3 Querying, I.C. Triplets (N3 and RDF); Part 1\]. Directionality in triplets is crucial for defining relationships and structuring queries \[Source: Graph Databases, Directionality\].

- **Development of Custom N3 Database Engine:** The platform uses an SQLite engine for transactional aspects, but the core data model and logic for serializing/deserializing data between triplets and relational views are custom-developed and patented \[Source: Graph Databases, Relationship with Triplets; N3 Querying, I.D. Data Storage; Part 1\].

- **Standardization of N3 Query Syntax and Execution:** N3 queries operate directly on triplet structures, supporting sequential and iterative execution, with specific syntax elements for variables, prefixes, formulas, and literals \[Source: Graph Databases, N3 Query Interaction; N3 Querying, II.A & II.B\].

- **Introduction of Axioms and Derived Facts:** The distinction between axioms (directly stored triplets) and derived facts (computed on-the-fly) is established, with calculated attributes being a prime example of derived facts \[Source: Graph Databases, Types of Data in Triplets; N3 Querying, I.D. Data Storage\].

- **Ongoing Development and Optimization (Present):** The platform continues to undergo significant development in N3 querying, including enhancements to built-in predicates, optimization strategies, and the introduction of a new expression compiler in version 3.6, with plans for a more advanced editor (F4.0) and DMN tables in future releases \[Source: Part 2; n3 p1; n3 p2\]. Documentation efforts are also underway to bring terminology into order for version 4.0 \[Source: Part 2\].

Cast of Characters

- **Georgy (Георгий):** The primary speaker and presenter in the "Part 1" and "Part 2" excerpts, responsible for explaining N3 querying, graph databases, and ontology. He is a technical expert, possibly a developer or solution architect, who designed the current N3 course and is familiar with the platform's architecture and optimization techniques. He also mentions developing parts of the system and its compiler.

- **Anatoly (Анатолий):** A participant in the discussion, frequently asking detailed, practical, and challenging questions about N3 querying, its application, performance, and integration with C# code. He seems to have a strong background in databases (relational algebra) and C# development, often referencing specific technical challenges he faces with the platform, such as calculating sums in words or managing processes. He also brings up the need for better documentation and alternative methods for process management.

- **Alexander (Александр):** Another participant who contributes to the discussion, sometimes clarifying Anatoly's questions or echoing concerns about specific features like calculated attributes. He also expresses interest in better process documentation and group work.

- **Pavel (Паша):** Mentioned by Georgy at the end of "Part 2" regarding the progress of activation issues, indicating he is involved in the technical support or development of the platform's licensing/activation mechanisms.

- **Igor (Игорь):** A colleague frequently referenced by Anatoly and Georgy. Igor is mentioned as a source for examples on global functions, C# integration, and specific technical solutions within the platform (e.g., calculated collections). He appears to be a key developer or technical resource.

- **Anna (Анна):** Briefly mentioned by Anatoly as someone, along with Igor, who might have implemented specific features related to process instance IDs in the past.

- **Maxim Viktorovich (Максим Викторович):** Mentioned briefly by Georgy in the context of a separate module for process documentation, indicating he is likely involved in product management or development strategy.

- **Konstantin (Костя):** Referenced as the author of a document ("Kostin's document") that provides examples and explanations, specifically regarding abstract concepts like apple characteristics. This suggests he is a technical writer or documentation specialist.

- **Sergey (Серёжа):** A colleague whose example code for a calculated property is used by Georgy to explain complex N3 expressions and execution flow. He is also mentioned in relation to the formatting of N3 code.

- **Valery (Валерий):** Likely a senior consultant or manager. Anatoly and Georgy frequently address him for strategic decisions, session scheduling, and overall platform direction (e.g., future features, documentation, support). He seems to be in a position of authority regarding coordination between the technical team and user needs.

\--------------------------------------------------------------------------------

Graph Databases and N3 Querying: A Briefing

Detailed Briefing Document: Graph Databases and N3 Querying

1\. Introduction to Graph Databases and Ontology

Graph databases are a specialized type of database that uses graph structures—nodes, edges, and properties—to represent and store data. This model is particularly well-suited for semantic queries, which focus on the meaning and relationships between data points.

1.1. Core Components: Nodes and Edges

- **Nodes (Vertices):** Represent entities or values. These can be abstract concepts like "Pencil Case" and "Pencil" or specific instances such as "Ivan Ivanovich" or a "Volvo car."

- **Edges (Relations):** Represent relationships between nodes. Edges can be directed or undirected, signifying connections like "Pencil Case contains Pencil" or "Person owns Car."

1.2. Application to Ontology

Graph databases naturally represent ontological models. In Information Technology, an **ontology** formally describes a set of objects, their properties, and the relationships between them. In an ontological model, nodes typically represent objects, classes, or instances, while edges represent the relationships between them. For example, "Person" and "Car" could be nodes, and "owns" would be an edge connecting them.

2\. Triplet Fundamentals (N3 and RDF)

The fundamental unit of data storage in an N3/RDF graph database is a **triplet**.

2.1. Triplet Structure

A triplet consists of three essential parts: **Subject**, **Predicate**, and **Object**.

- **Subject:** The resource being described, acting as the source of the arrow in a graph.

- **Predicate:** The property or relationship, represented as the arrow itself.

- **Object:** The value or resource that the subject is related to, forming the destination of the arrow.

**Directionality** is crucial for triplets; it explicitly defines the flow of a relationship (e.g., "Person owns Car" versus "Car owned\_by Person"). This direction dictates which element is the Subject and which is the Object, and consequently, how queries must be structured.

2.2. N3 (Notation3) and RDF (Resource Description Framework)

- **RDF:** A W3C standard for describing resources, often represented in XML or N3.

- **N3:** A compact and human-readable syntax for RDF, supporting logical expressions. All data, whether systemic metadata or user-applied data, is stored as triplets in the the platform's N3 database.

2.3. Data Storage Mechanism

System models are described in .n3 files, while applied data (metadata and instances) are stored in separate files (e.g., data.n3). The platform uses an SQLite engine for transactional aspects, but the core data model and the logic for serializing/deserializing data between triplets and relational views are custom.

2.4. Types of Data in Triplets

- **Qualified Name (QName):** Shortened forms of long URIs (Uniform Resource Identifiers) used to represent resources, especially for complex types. QNames are typically used for subjects, predicates, and objects.

- **Simple Literals:** Direct values like strings ("blue"), numbers (5), booleans (true), dates, or durations.

- **Complex Literals:** Represent collections of facts or ordered sets of values, used in advanced queries.

    - **Formulas (****{...}****):** A set of triplets evaluated together as a single unit.

    - **Lists (****(...)****):** An ordered collection of values or variables.

- **Axioms vs. Derived Facts:**

    - **Axioms:** Facts directly stored as triplets in the database.

    - **Derived Facts:** Computed on the fly based on axioms and the current context (e.g., calculated attributes) and are not stored in the database.

3\. N3 Query Syntax and Execution

N3 queries operate directly on triplet structures, allowing for powerful data retrieval and manipulation within the graph database.

3.1. Core Syntax Elements

- **Comments (****#****):** For adding notes.

- **Prefixes (****@prefix****):** Define shortcuts for long URIs to improve readability.

- **Variables (****?****):** Denoted by a question mark followed by an alphanumeric name (e.g., ?item, ?value). They represent unknown values to be discovered.

- **Triplet Terminator (****.****):** Every triplet must end with a period.

- **Formula Block (****{ ... }****):** Defines a query block executed as a single unit, forming a single iterator result.

- **Lists/Arrays (****( ... )****):** Used to define ordered collections of values.

- **Implicit Subject (****\[ ... \]****):** Square brackets can implicitly refer to the subject of the previous triplet.

- **Reserved Keywords:** a (for rdf:type - "is an instance of"), is ... of (inverse property).

- **Assignment (****\=****):** Assigns a value from one variable to another.

- **Conditional (****if ... else ...****):** Controls query flow. If the if condition is false and there's no else block, the query stops.

3.2. Query Execution Model

- **Sequential Execution:** Queries execute top-down, line by line.

- **Iterative Processing:** If a line (triplet) returns an iterator (multiple values), subsequent lines are executed for each value in that iterator, creating nested loops. An iterator's scope is confined to the formula/block it was created in. Once the block finishes, the iterator's result is passed as a single value (or a collection) to the next level.

- **Optimization:** "The order of triplets matters significantly for performance. Queries should start with the most restrictive conditions to minimize the size of initial iterators." This often means "flipping" the query to start from the most selective conditions rather than following a traditional relational database's "FROM-WHERE" pattern.

- **Match vs. Search:**

    - **Search (unknowns):** When one or more parts of a triplet are variables (e.g., ?S P ?O), the system searches the database for matching facts and populates the variables with iterators.

    - **Match (all known):** When all parts of a triplet are known values, the system checks for the existence of that exact fact in the database, returning true or false. This does not return an iterator.

3.3. Common Query Patterns and Operators

- object:findProperty: A built-in predicate to retrieve the ID of an attribute given its template alias and attribute alias. It always returns a single ID and is highly optimized.

- assert:union: Combines the results of multiple iterators into a single iterator. assert:union true performs a "union all" (duplicates included).

- ones: Executes a query and returns only the first successful result, stopping further iteration once a match is found.

- or: Evaluates multiple conditions and returns true if any are met, stopping at the first successful condition.

- **Built-in Functions:** Special predicates (e.g., math:sum, time:dayOfWeek) that perform calculations in memory rather than querying the database.

- value and item: Reserved keywords for output and input parameters, respectively, in expressions. value stores the output, item refers to the current object in context.

4\. Application Contexts for N3 Queries

N3 queries are used in various platform contexts to enable dynamic behavior and data processing.

- **Calculated Attributes:** Defined on a record template to compute a value dynamically. item is the input (current object ID), value is the output. Calculated on-the-fly and not stored in the database.

- **List Filters:** Used to filter records displayed in a list. item is the output (IDs of records to display).

- **Operations (Conditional Display):** Used to show or hide operations based on conditions (e.g., a "Complete Task" button). item is the input (current record ID), value is true (show) or false (hide).

- **Business Rules (Triggers/Scenarios):** Define actions that execute based on specific events (e.g., a field change).

- **Global Functions:** External functions (e.g., written in C#) that can be invoked from N3 queries. "Allows for code reusability and complex computations not directly expressible in N3." They can retrieve data from external services or perform custom logic.

5\. Key Distinctions and Best Practices

- **Calculated Attributes vs. Stored Data:** "Calculated attributes are always computed on demand and are never stored in the database." They are "computed at the moment of access." Changes to underlying stored data will trigger re-calculation. Axioms are directly stored facts.

- **Query Optimization:** Begin with highly selective conditions to reduce the size of iterators early in the query execution.

- **Understanding Iterators:** The nested loop nature of N3 query execution means careful structuring can lead to significant performance differences.

- **Contextual Variables:** item, value, current user, now are context-dependent and reserved.

This briefing provides a comprehensive overview of graph databases, triplet fundamentals, N3 querying, and its practical applications, drawing directly from the provided source material.

\--------------------------------------------------------------------------------

Graph Databases: N3 Querying Fundamentals Explained

Here's an 8-question FAQ based on the provided sources, with thorough answers:

Frequently Asked Questions about Graph Databases and N3 Querying

What is the primary purpose of an "ontology" in the context of information technologies?

In information technology, an ontology serves as a formal description of a set of objects, their properties, and the relationships between them within a specific domain or the real world. Its primary purpose is to provide a structured, machine-readable representation of knowledge, allowing systems to understand and process information in a more meaningful way. It acts as a blueprint for data organization, defining "what exists" within a given sphere of interest.

How does a "graph database" fundamentally represent data, and what are its two main components?

A graph database fundamentally represents and stores data using **graph structures**, which are exceptionally well-suited for semantic queries. Its two main components are **nodes** (or vertices) and **edges** (or relations). Nodes represent entities or values (such as classes, instances, or literal values), while edges represent the relationships between these nodes. Edges can be either directed or undirected, indicating how different entities are connected (e.g., "Person owns Car"). This structure naturally aligns with ontological models.

Explain what a "triplet" is and identify its three essential parts in the N3/RDF model.

A triplet is the fundamental unit of data storage in an N3/RDF graph database, representing a single fact or statement. It consists of three essential parts:

1. **Subject:** The resource or entity being described, acting as the source of the arrow in a graph.

2. **Predicate:** The property or relationship that connects the subject and object, represented as the arrow itself.

3. **Object:** The value or resource that the subject is related to, forming the destination of the arrow. For example, in the triplet "Person owns Car," "Person" is the Subject, "owns" is the Predicate, and "Car" is the Object.

Why is the "directionality" of a relationship important when defining triplets in the N3 database?

The directionality of a relationship is crucial in N3 triplets because it explicitly defines the flow and meaning of that relationship. For instance, "Person owns Car" has a different meaning than "Car owned\_by Person." This direction determines which element is the Subject and which is the Object in a triplet, directly influencing how data is stored and, consequently, how N3 queries must be structured to retrieve specific information. Understanding directionality is key to correctly constructing queries and interpreting results.

What is the difference between an "axiom" and a "derived fact" in the N3 database, and how does this relate to "calculated attributes"?

In the N3 database, an **axiom** is a fact that is directly stored as a triplet within the database. It represents explicit, persistent data. In contrast, a **derived fact** is not directly stored but is computed or inferred on the fly based on existing axioms and the current context of a query. **Calculated attributes** are a prime example of derived facts; their values are dynamically computed whenever they are requested and are never permanently saved in the database. This distinction allows for dynamic data generation and ensures that certain values are always up-to-date without explicit storage.

Describe the role of "variables" (e.g., ?item, ?value) in N3 queries.

Variables in N3 queries, identified by a question mark prefix (e.g., ?item, ?value), serve as placeholders for unknown values that the query aims to discover or populate. When an N3 query is executed, the system searches the database for triplets that match the known parts of the query pattern and then populates these variables with the corresponding data. If multiple matches are found, variables often return an "iterator," allowing subsequent query lines to process each matching value. ?item and ?value are reserved variables often used for input (current object ID) and output (query result) parameters in specific contexts like calculated attributes or list filters.

How does the sequential and iterative execution model of N3 queries impact their performance?

The sequential and iterative execution model of N3 queries significantly impacts performance. Queries execute top-down, line by line. If a line (or triplet) returns an iterator (multiple values), subsequent lines are executed for _each_ value within that iterator. This creates nested loop-like processing, where deeper iterators cause the upper levels to re-evaluate repeatedly. Therefore, **optimization is crucial**: queries should always start with the most restrictive conditions. By minimizing the size of initial iterators, the overall number of operations performed in subsequent nested loops is drastically reduced, leading to much faster query execution. Failing to do so can lead to substantial performance degradation.

Explain the function of the operator in N3 queries.

The assert:union operator in N3 queries is used to combine the results of multiple query blocks or iterators into a single, unified iterator. When assert:union true is specified, it performs a "union all" operation, meaning that duplicate values from the combined iterators will be included in the final result. This is particularly useful when you need to gather data from different, potentially overlapping, sources or conditions and present them as a single collection, allowing for further processing or filtering on the combined set.

\--------------------------------------------------------------------------------

Graph Databases: Structure, Ontology, and Triplet Fundamentals

**Graph databases** are a type of database that uses **graph structures** to represent and store data, which is particularly well-suited for semantic queries \[1\]. In this context, data is organized using **nodes**, **edges**, and properties \[1\].

Here's a breakdown of graph databases:

- **Definition and Components**

    - A graph database fundamentally represents data using **graph structures** \[1\].

    - Its two main components are: \* **Nodes (Vertices):** These represent entities or values. Examples include classes, instances, or literal values \[1-3\]. In the context of the platform, nodes can represent abstract concepts like "Pencil Case" and "Pencil," or specific instances like "Ivan Ivanovich" or a "Volvo car" \[4, 5\]. \* **Edges (Relations):** These represent **relationships** between nodes. Edges can be either directed or undirected \[1, 2\]. They signify how different entities are connected, such as "Pencil Case contains Pencil" or "Person owns Car" \[4, 5\].

- **Types of Graphs**

    - Graph databases can support various types of graphs, including connected, isolated, directed, undirected, complete, planar, and tree-like graphs \[1, 2\].

- **Application to Ontology**

    - Graph databases naturally represent **ontological models** \[1\]. An ontology, in information technology, describes a set of objects, their properties, and the relationships between them \[4, 6\].

    - In an ontological model, **nodes** typically represent objects, classes, or instances, while **edges** represent the relationships between them \[1, 5, 7\]. For example, "Person" and "Car" could be nodes, and "owns" would be an edge connecting them \[5\].

- **Relationship with Triplets (N3 and RDF)**

    - The fundamental unit of data storage in an N3/RDF graph database is a **triplet** \[8-11\].

    - A triplet consists of three essential parts: **Subject**, **Predicate**, and **Object** \[6, 8, 12, 13\]. \* The **Subject** is the resource being described, acting as the source of the arrow in a graph \[8, 12, 13\]. \* The **Predicate** is the property or relationship, represented as the arrow itself \[8, 12, 13\]. \* The **Object** is the value or resource that the subject is related to, forming the destination of the arrow \[8, 12, 13\].

    - **Directionality** is crucial for triplets; it explicitly defines the flow of a relationship (e.g., "Person owns Car" versus "Car owned\_by Person") \[6, 8, 14\]. This direction dictates which element is the Subject and which is the Object, and consequently, how queries must be structured \[6, 8, 14\].

    - **N3 (Notation3)** is a compact and human-readable syntax used for RDF, which also supports logical expressions \[8, 15\]. All data, whether systemic metadata or user-applied data, is stored as triplets in the N3 database \[9, 10, 16\].

    - In an N3 database, system models are described in .n3 files, while applied data (metadata and instances) are stored in separate files, such as data.n3 \[9, 16\].

    - The platform uses an SQLite engine for transactional aspects, but the core data model and the logic for serializing/deserializing data between triplets and relational views are custom \[9, 16\].

- **Types of Data in Triplets**

    - **Qualified Name (QName):** These are shortened forms of long URIs (Uniform Resource Identifiers) used to represent resources, especially for complex types \[9, 17\]. QNames are typically used for subjects, predicates, and objects \[9, 17, 18\].

    - **Simple Literals:** These are direct values like strings ("blue"), numbers (5), booleans (true), dates, or durations \[9, 19\].

    - **Complex Literals:** These represent collections of facts or ordered sets of values, used in advanced queries \[9\]. \* **Formulas (****{...}****):** A set of triplets that are evaluated together as a single unit \[9, 20-22\]. \* **Lists (****(...)****):** An ordered collection of values or variables \[9, 20, 21, 23\].

    - **Axioms vs. Derived Facts:** \* **Axioms** are facts directly stored as triplets in the database \[9, 20, 24\]. \* **Derived Facts** are computed on the fly based on axioms and the current context (e.g., calculated attributes) and are not stored in the database \[9, 20, 24, 25\].

- **N3 Query Interaction with Graph Databases**

    - N3 queries operate directly on these triplet structures \[16, 26\]. When parts of a triplet are variables (e.g., ?S P ?O), the system performs a **search** in the database to find matching facts and populate the variables with iterators \[26-28\].

    - If all parts of a triplet are known values, the system performs a **match** to check for the exact fact's existence, returning true or false \[26, 28, 29\].

    - The sequential and iterative execution model of N3 queries means that the order of triplets significantly impacts performance, as queries should start with the most restrictive conditions to minimize the size of initial iterators \[26, 30, 31\]. This often means "flipping" the query to start from the most selective conditions rather than following a traditional relational database's "FROM-WHERE" pattern \[32\].

    - An N3 query effectively "walks" the graph, moving from one node to another via edges (predicates) to retrieve or verify information \[31\].

