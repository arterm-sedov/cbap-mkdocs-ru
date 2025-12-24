
Руководство по нотации 3 в Comindware
00:00:00 Введение в Notation Three
• Знакомство с мощным языком запросов Notation Three в Common Platform.

• Цель: раскрыть потенциал данных.

00:00:35 Новый подход к данным
• Данные воспринимаются как взаимосвязанный граф, а не как таблицы.

• Графическая база данных описывает мир через последовательность простых утверждений.

00:01:27 Структура триплета
• Триплет — основная концепция языка, аналогичная простому предложению.

• Пример триплета: «мама мыла рамку».

 00:02:04 Синтаксис Notation Three
• Синтаксис отражает структуру триплета: подлежащее, предикат, объект.

• Каждое утверждение заканчивается точкой.

00:02:49 Итератор и его роль
• Итератор — ключевой элемент для эффективных запросов.

• Порядок строк в запросе влияет на скорость обработки.

• Золотое правило: начинать с наиболее конкретных и ограничивающих строк.

00:04:06 Практический запрос
• Пример запроса: подсчёт уникальных товаров в заказе.

• Использование фигурных скобок для объединения операций.

• Предикат для фильтрации дубликатов.

• Функция assert count для подсчёта уникальных элементов.

00:05:15 Заключение
• Notation Three позволяет взаимодействовать с данными как с информацией.

• Вопрос: что вы собираетесь построить с помощью этих знаний?### Сводка

Это видео представляет собой подробное руководство по Notation 3 (N3), языку запросов, используемому в платформе Comindware. Руководство разделено на пять ключевых частей:

*   **1. Данные как сеть:** Этот раздел представляет новый подход к данным. В N3 данные рассматриваются не как жесткие таблицы, а как взаимосвязанный граф или паутина отношений. Этот подход, являющийся центральным для графовых баз данных, представляет данные в виде набора простых, связанных фактов, что упрощает формулирование сложных реляционных вопросов.
*   **2. Атомарный строительный блок:** Ключевое понятие языка N3 — «Триплет». Это фундаментальная единица данных со структурой простого предложения: **Субъект**, **Предикат** (действие или отношение) и **Объект**. Любая информация в системе может быть разложена на эту простую и изящную структуру.
*   **3. Язык триплетов:** В этой части рассматривается базовый синтаксис N3. Синтаксис напрямую отражает структуру Триплета. Здесь объясняется, как определять субъекты, предикаты и объекты, а также вводится использование переменных (обозначаемых знаком `?`) для постановки вопросов и поиска неизвестных значений. Каждое утверждение в N3 заканчивается точкой.
*   **4. Как на самом деле работают запросы:** Критически важное для написания эффективных запросов понятие — «Итератор». Система обрабатывает запросы последовательно, строка за строкой. Первая строка создает список потенциальных совпадений (итератор), который затем фильтруется последующими строками. «Золотое правило» гласит: первые строки запроса должны быть максимально конкретными и ограничивающими, чтобы создать небольшой начальный итератор, что кардинально повышает скорость и эффективность выполнения запроса.
*   **5. Анатомия запроса:** В этом разделе приводится практический, реальный пример запроса для подсчета количества уникальных товаров в заказе. Запрос разбирается пошагово, объясняется использование блоков формул (`{}`) и встроенных функций (специальных предикатов), таких как `assert:distinct` для удаления дубликатов и `assert:count` для получения итогового числа.

---

### Транскрипция

**00:00** Добро пожаловать в наш эксплейнер.
**00:02** Сегодня мы погружаемся в довольно мощный язык запросов, используемый внутри платформы Comindware.
**00:08** Notation 3, или, как его еще называют, N3.
**00:11** Послушайте, если вы когда-либо хотели раскрыть истинный потенциал ваших данных, это именно тот способ.
**00:16** Итак, вот что мы собираемся сделать.
**00:17** Сначала мы заставим вас взглянуть на данные совершенно по-новому.
**00:21** Затем мы разберем абсолютный ключевой компонент этого языка.
**00:25** После этого мы изучим базовый синтаксис, посмотрим, как на самом деле "думает" движок,
**00:29** и, наконец, мы разберем на части реальный запрос.
**00:32** Хорошо, давайте начнем.
**00:34** Прежде всего, чтобы по-настоящему понять N3, вам потребуется немного изменить свое мышление.
**00:39** Вы должны перестать думать о своих данных как о чем-то, что хранится в жестких таблицах, ну, знаете, как в электронных таблицах.
**00:44** Вместо этого начните видеть их как этот огромный, взаимосвязанный граф, как паутину отношений, где все связано со всем остальным.
**00:53** Да, а что если вместо строк и столбцов ваши данные были бы просто огромной коллекцией простых фактов?
**01:00** Именно в этом и заключается вся идея графовой базы данных.
**01:04** Она описывает мир как серию простых, связанных утверждений.
**01:08** И когда вы это делаете, задавать действительно сложные реляционные вопросы становится гораздо интуитивнее и, честно говоря, намного мощнее.
**01:15** Так как же мы на самом деле представляем эти факты?
**01:19** Что ж, вся система, абсолютно вся, построена на одной прекрасной и простой структуре.
**01:24** Это действительно ключевая концепция всего языка.
**01:27** Она называется Триплет.
**01:29** И знаете что? Он работает так же, как простое предложение.
**01:32** Что-то, это субъект, делает что-то, это предикат, с чем-то еще, это объект.
**01:38** Это фундаментальный атом, из которого будут построены все наши молекулы данных.
**01:43** А теперь взгляните на это, потому что это действительно интересно.
**01:47** Любой факт, и я имею в виду абсолютно любую часть информации, можно разложить таким образом.
**01:52** От простой реальной вещи, такой как "Мама мыла раму", до сложных данных внутри вашей платформы, например, "Этот пенал содержит синий карандаш".
**02:01** Эта структура субъект-предикат-объект — это всё.
**02:04** Хорошо, теперь, когда мы поняли строительный блок, давайте изучим язык, который мы используем для описания и запроса этих триплетов.
**02:12** Именно здесь мы начинаем говорить на Notation 3.
**02:14** Самое классное в том, что синтаксис напрямую отражает ту структуру Триплета, которую мы только что видели.
**02:19** Вы указываете свой субъект, затем предикат или свойство, которое вас интересует,
**02:23** а затем вы либо даете конкретный объект для проверки, либо используете переменную.
**02:28** Это вопросительный знак, чтобы найти то, что вы ищете.
**02:31** И так же, как предложение в английском языке, каждое утверждение заканчивается точкой.
**02:34** Все просто.
**02:35** Хорошо, будьте очень внимательны, потому что следующая концепция —
**02:39** это единственный и самый важный ключ к написанию эффективных, быстрых запросов.
**02:44** Понимание этого полностью изменит ваш подход к каждому запросу, который вы будете писать в будущем.
**02:49** Мы говорим о секретном оружии движка — итераторе.
**02:54** Хорошо, давайте посмотрим на этот запрос на экране.
**02:56** Цель проста, верно?
**02:58** Найти пользователя по имени Иванов И.И.
**03:01** Вы можете подумать, что система просто идет и находит этого пользователя напрямую, но это не то, что происходит.
**03:07** Движок обрабатывает это строка за строкой, и порядок, в котором вы это пишете, абсолютно критичен.
**03:13** Итак, вот что на самом деле делает движок.
**03:15** Он создает список потенциальных совпадений из первой строки запроса, и этот список называется итератором.
**03:22** В этом случае, с этим неэффективным запросом, он выполняет первую, очень общую строку и получает список абсолютно всех пользователей в системе.
**03:30** Затем он проходит по этому огромному списку, один за другим, проверяя каждого пользователя по второй строке.
**03:36** Если элемент не проходит проверку, он отбрасывается. Если проходит, он движется дальше, пока не останутся только конечные результаты.
**03:42** Вы можете представить, насколько медленным это может быть, верно?
**03:44** Итак, это подводит нас к Золотому Правилу.
**03:46** Вы должны структурировать свой запрос так, чтобы самые конкретные, самые ограничивающие строки шли первыми.
**03:51** В примере, который мы только что видели, нужно просто поменять строки местами.
**03:54** Начните с имени, которое, вероятно, соответствует только одному человеку, а затем подтвердите, что это пользователь.
**03:59** Это сокращает ваш начальный итератор почти до нуля и делает весь процесс значительно быстрее и намного эффективнее.
**04:06** Хорошо, давайте соберем все это вместе.
**04:08** Пришло время испачкать руки и разобрать практический запрос, который вы действительно могли бы использовать на платформе, и увидеть все эти принципы в действии.
**04:16** Итак, вот наш запрос.
**04:18** Цель здесь — решить очень распространенную проблему: подсчитать количество уникальных товаров в заказе.
**04:25** Вы знаете, как это бывает. В заказе может быть множество строк, и один и тот же товар может появляться несколько раз.
**04:31** Мы просто хотим знать, сколько там различных товаров.
**04:34** Итак, для начала у нас есть этот блок в фигурных скобках.
**04:38** Система рассматривает все это как единую операцию.
**04:42** Итератор начинает с нашего элемента, нашего заказа, находит все его строки позиций, а затем для каждой из этих строк он извлекает товар.
**04:50** В итоге вы получаете один гигантский итератор — просто длинный список всех товаров из каждой строки, включая дубликаты.
**04:58** Дальше начинается магия.
**05:01** Видите этот `assert:distinct`? Это специальный предикат.
**05:04** Думайте о нем как о встроенной функции.
**05:06** Он берет весь тот список, который мы только что создали, со всеми дубликатами, и фильтрует его, возвращая новый, чистый итератор, содержащий только уникальные товары.
**05:15** И наконец, последняя функция, `assert:count`, берет наш хороший, чистый список уникальных элементов, делает именно то, что следует из названия — подсчитывает их,
**05:24** и помещает итоговое число в нашу выходную переменную, `?value`.
**05:28** И вот так просто, проблема решена.
**05:30** Итак, поняв простую силу триплета и освоив логику итератора, вы действительно открыли совершенно новый способ взаимодействия с вашими данными.
**05:37** Это уже не столько поиск записи в таблице, сколько ведение настоящего диалога с вашей информацией.
**05:43** Так что единственный оставшийся вопрос — что вы с этим создадите?

Summary
This video provides a comprehensive guide to Notation 3 (N3), the query language used in the Comindware platform. The guide is broken down into five key parts:
1. Data as a Web: This section introduces a new way of thinking about data. Instead of rigid tables, N3 treats data as an interconnected graph or web of relationships. This approach, central to graph databases, represents data as a collection of simple, connected facts, making it easier to ask complex relational questions.
2. The Atomic Building Block: The core concept of the N3 language is the "Triplet." This is the fundamental unit of data, structured like a simple sentence with a Subject, a Predicate (the action or relationship), and an Object. Every piece of information in the system can be broken down into this beautifully simple structure.
3. Speaking in Triplets: This part covers the basic syntax of N3. The syntax directly mirrors the Triplet structure. It explains how to define subjects, predicates, and objects, and introduces the use of variables (denoted by a ?) to ask questions and find unknown values. Every statement in N3 ends with a period.
4. How Queries Really Work: A critical concept for writing efficient queries is the "Iterator." The system processes queries line-by-line, sequentially. The first line creates a list of potential matches (the iterator), which subsequent lines then filter. The "Golden Rule" is to make the first lines of a query as specific and restrictive as possible to create a small initial iterator, which dramatically improves query speed and efficiency.
5. Anatomy of a Query: This section provides a practical, real-world example of a query designed to count the number of unique products in an order. It breaks down the query step-by-step, explaining the use of formula blocks ({}), and built-in functions (special predicates) like assert:distinct to remove duplicates and assert:count to get the final number.
Transcription
00:00 Welcome to the explainer.
00:02 Today we're diving into the pretty powerful query language used inside the Comindware platform.
00:08 Notation 3, or you'll just hear it called N3.
00:11 Look, if you've ever wanted to unlock the true potential of your data, this is how you do it.
00:16 So here's what we're going to do.
00:17 First, we'll get you thinking about data in a whole new way.
00:21 Then, we'll break down the language's absolute core component.
00:25 After that, we'll learn the basic syntax, see how the engine actually thinks,
00:29 and finally, we're going to tear apart a real-world query.
00:32 All right, let's get into it.
00:34 First things first, to really get N3, you need a bit of a mental shift.
00:39 You have to stop thinking about your data living in these rigid tables, you know, like spreadsheets.
00:44 Instead, start seeing it as this huge, interconnected graph, like a web of relationships where everything is connected to everything else.
00:53 Yeah, what if, instead of rows and columns, your data was just a huge collection of simple facts?
01:00 This right here is the whole idea behind a graph database.
01:04 It describes the world as a series of simple connected statements.
01:08 And when you do that, asking really complex relational questions becomes way more intuitive, and honestly, a lot more powerful.
01:15 So, how do we actually represent these facts?
01:19 Well, the entire system, the whole thing is built on one beautifully simple structure.
01:24 This is really the core concept of the entire language.
01:27 It's called a Triplet.
01:29 And you know what? It works just like a basic sentence.
01:32 Something, that's the subject, does something, that's the predicate, to something else, that's the object.
01:38 It's the fundamental atom from which all of our data molecules are going to be built.
01:43 Now, take a look at this, because this is really interesting.
01:47 Any fact, and I mean any piece of information, can be broken down this way.
01:52 From a simple real-world thing like "Mom washed the frame," all the way to complex data inside your platform like "This Pencil Case contains a blue pencil."
02:01 This subject, predicate, object structure, it is everything.
02:04 Okay, so now we understand the building block, let's learn the language we use to actually describe and query these triplets.
02:12 This is where we start speaking Notation 3.
02:14 The really cool thing is, the syntax directly mirrors that Triplet structure we just saw.
02:19 You state your subject, then the predicate or property you're interested in,
02:23 and then you either give it a specific object you're checking for, or you use a variable.
02:28 That's the question mark, to find what you're looking for.
02:31 And just like a sentence in English, every statement ends with a period.
02:34 Simple as that.
02:35 Okay, pay close attention because this next concept,
02:39 this is the single most important key to writing efficient, fast queries.
02:44 Understanding this will totally change how you approach every query you write from now on.
02:49 We are talking about the engine's secret weapon, the iterator.
02:54 Okay, let's look at this query on the screen.
02:56 The goal is simple, right?
02:58 Find a user named Ivanov I.I.
03:01 Now, you might think the system just goes and finds that user directly, but that's not what happens.
03:07 The engine processes this line by line, and the order you write it in is absolutely critical.
03:13 So here's what the engine actually does.
03:15 It creates a list of potential matches from the first line of the query, and this list is called the iterator.
03:22 In this case, with this inefficient query, it runs that first very general line and gets a list of every single user in the system.
03:30 Then it goes through that massive list one by one, testing each user against the second line.
03:36 If an item fails, it's tossed out. If it passes, it moves on until only the final results are left.
03:42 You can see how slow that could be, right?
03:44 So, this brings us to the Golden Rule.
03:46 You have to structure your query so the most specific, most restrictive lines come first.
03:51 For the example we just saw, you just flip the lines.
03:54 Start with the name, which probably only matches one person, and then confirm it's a user.
03:59 This shrinks your initial iterator down to almost nothing and makes the whole thing dramatically faster and way more efficient.
04:06 Okay, let's put all this together.
04:08 It's time to get our hands dirty and break down a practical query, something you might actually use on the platform, and see all these principles in action.
04:16 All right, here's our query.
04:18 The goal here is to solve a really common problem: counting the number of unique products inside an order.
04:25 You know how it is. An order might have tons of lines, and the same product could pop up multiple times.
04:31 We just want to know how many distinct products there are.
04:34 So, first up, we have this block in curly braces.
04:38 The system treats that whole thing as a single operation.
04:42 The iterator starts with our item, our order, finds all its position lines, and then for each of those lines, it grabs the product item.
04:50 What you end up with is one giant iterator, just a long list of all the products from every single line, duplicates and all.
04:58 Next comes the magic.
05:01 See that assert:distinct? That's a special predicate.
05:04 Think of it like a built-in function.
05:06 It takes that entire list we just made, all the duplicates included, and it filters it, returning a new, clean iterator that has only the unique products.
05:15 And finally, the last function, assert:count, takes our nice clean list of unique items, does exactly what it sounds like, it counts them,
05:24 and it puts that final number into our output variable, ?value.
05:28 And just like that, problem solved.
05:30 So, by understanding the simple power of the triplet and getting the logic of the iterator, you've really unlocked a completely new way to interact with your data.
05:37 It's less about finding a record in a table and more like having a real conversation with your information.
05:43 So the only question left is, what are you going to build with it?
