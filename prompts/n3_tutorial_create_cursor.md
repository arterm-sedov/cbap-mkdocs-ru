# N3 Tutorial Generation Prompt for Cursor

## Mission

Generate a complete, standalone N3 (Notation 3/Turtle/RDF) tutorial for Comindware Platform 5.0 users. Loosely integrated with the existing @/tutorial_hr for educational continuity.

## Lesson Plan Structure

### Lesson 1: Introduction to N3 (1.5 hours)

**Learning Objectives:**

- Understand RDF, knowledge graphs, and ElasticData
- Master triple structure, core N3 syntax and shorthands
- Learn five types of queries and interpreter behavior
- Know `?item`/`?value` I/O and execution context across entities
- See N‑Triples vs N3 mapping and Formula → N3 refactor

**Content:**

- RDF model, graphs, ontologies, ontology structure, and data model
- ElasticData overview and mapping to RDF/N3 ([ElasticData][elasticdata_description])
- Triples with visuals; syntax: variables, `{}`, `.`, `a`, `[]`, `()`, `=`; note if `=>` is used in platform context
- Five query types and order of evaluation; reasoner overview
- Execution context and I/O per entity; add subsection "Контекст и ввод-вывод по сущностям" with anchor `{: #tutorial_n3_lesson_1_io_context }`
- N‑Triples vs N3; one‑line mapping example; Formula → N3 mini‑refactor
- Platform N3 editor brief intro; glossary of terms
- Simple HR data query walk‑through (candidate → department)
- Common mistakes mini‑box: missing dot, braces, variable reuse
- Sources:
  - `docs/ru/developer_guide/n3/n3_tutorial.md` — baseline tutorial narrative
  - `docs/ru/developer_guide/n3/n3_guide.md` — syntax, five query types, built‑ins, I/O matrix
  - `docs/ru/developer_guide/n3/n3_notation.md` — N3 notation fundamentals
  - `docs/ru/developer_guide/n3/n3_graphs.md` — graph concepts and visuals
  - `docs/ru/developer_guide/n3/n3_knowledge_graphs.md` — knowledge graph context
  - `docs/ru/developer_guide/n3/n3_model.md` — data model mapping to N3
  - `docs/ru/developer_guide/n3/n3_ontology.md` — ontology principles
  - `docs/ru/developer_guide/n3/n3_ontology_structure.md` — ontology structure details
  - `docs/ru/developer_guide/n3/n3_glossary.md` — terminology
  - `docs/ru/developer_guide/n3/sources/presentation_converted_from_pdf.md` — slides → text with N‑Triples emphasis
  - `docs/ru/developer_guide/n3/sources/n3_tutorial_intro.md` — course intro framing
  - `docs/ru/developer_guide/n3/sources/n3_tutorial_summary.md` — high‑level summary
  - `docs/ru/developer_guide/n3/sources/n3_video_transcript_complete_notebook_lm.md` — consolidated instructor insights
  - `docs/ru/developer_guide/n3/sources/n3_video_part_1_transcript_gemini.md` — basics and context
  - `docs/ru/developer_guide/n3/sources/n3_video_part_2_transcript_gemini.md` — syntax and queries
  - `docs/ru/developer_guide/n3/sources/n3_video_part_3_transcript_gemini.md` — logic and performance
  - `docs/ru/developer_guide/n3/sources/n3_video_part_4_transcript_gemini.md` — collections and functions
  - `docs/ru/developer_guide/n3/sources/n3_notebook_lm_audio_summary_transcript_2.md` — condensed recap (audio)
  - `docs/ru/developer_guide/n3/sources/n3_notebook_lm_audio_summary_transcript.md` — condensed recap (audio)
  - `docs/ru/developer_guide/n3/sources/n3_notebook_lm_notes_2.md` — study notes 2
  - `docs/ru/developer_guide/n3/sources/n3_notebook_lm_notes.md` — study notes 1
  - `docs/ru/developer_guide/n3/sources/n3_notebook_lm_video_summary_transcript.md` — video summary transcript
  - `docs/ru/developer_guide/n3/sources/n3_notebook_lm_video_summary.md` — video summary
  - `docs/ru/developer_guide/n3/sources/n3_presentation_summary_notebook_lm.md` — presentation summary

**Assessment in tests.md:** 2–3 questions on triples,  basic syntax, and I/O

### Lesson 2: Core Syntax, Variables, Query Types (1 hour)

**Learning Objectives:**

- Use variables and core syntax correctly (`{}`, `.`, `?variable`)
- Apply `?item`/`?value` across contexts
- Practice five query types with minimal examples

**Content:**

- Triples anatomy; variable naming guidance
- `?item`/`?value` usage patterns and type discipline
- Five query types with tiny runnable snippets
- Error hygiene: dots, braces, case sensitivity
- Formula → N3 refactor (simple)
- Sources:
  - `docs/ru/developer_guide/n3/n3_guide.md` — five forms, I/O matrix, syntax
  - `docs/ru/developer_guide/n3/n3_tutorial.md` — beginner examples
  - `docs/ru/developer_guide/n3/sources/n3_video_part_1_transcript_gemini.md` — basics
  - `docs/ru/developer_guide/n3/sources/presentation_converted_from_pdf.md` — mapping examples

**Assessment in tests.md:** 2–3 questions on syntax and `?item`/`?value`

### Lesson 3: Prefixes, URIs, Property Discovery (1 hour)

**Learning Objectives:**

- Understand URIs, QNames, and prefixes
- Use `object:findProperty` to resolve attribute URIs
- Distinguish application vs system attributes

**Content:**

- Prefix declarations and URI/QName rationale
- `object:findProperty` patterns; mapping to predicates
- Variable assignment variants (subject/object/predicate known)
- Sources:
  - `docs/ru/developer_guide/n3/n3_guide.md` — prefixes, `object:findProperty`
  - `docs/ru/developer_guide/n3/n3_tutorial.md` — property discovery walkthroughs
  - `docs/ru/developer_guide/n3/sources/n3_video_part_2_transcript_gemini.md` — discovery details

**Assessment in tests.md:** 2 questions on prefixes and property lookup

### Lesson 4: Data Navigation & Variable Assignment (1 hour)

**Learning Objectives:**

- Navigate multi‑hop relations safely
- Apply three variable assignment patterns
- Name intermediates clearly for readability

**Content:**

- Multi‑step navigation (candidate → manager → department)
- Three assignment variants; exact‑match checks
- Formula → N3 refactor (link traversal)
- Practical exercise: Build candidate filtering system
- Sources:
  - `docs/ru/developer_guide/n3/n3_tutorial.md` — three assignment patterns
  - `docs/ru/examples/n3_collection_join_filter.md` — join & filter pattern
  - `docs/ru/examples/n3_collection_join_filter_hierarchy.md` — hierarchical joins
  - `docs/ru/examples/n3_collection_join_string.md` — joins to strings
  - `docs/ru/tutorials/tutorial_architect/lesson_2.md` — UI task context tie‑ins

**Assessment in tests.md:** 2 questions on navigation patterns

### Lesson 5: Iterator & Performance Basics (1 hour)

**Learning Objectives:**

- Explain iterator behavior and fan‑out
- Use `once {}` safely; order triples by selectivity
- Use negation `not { ... }` for emptiness checks

**Content:**

- Iterator semantics and selection rules; break on `false`
- Performance hygiene; safe `once {}` cases
- Negation and default conjunction between triples
- Sources:
  - `docs/ru/developer_guide/n3/n3_tutorial.md` — iterator deep dive
  - `docs/ru/developer_guide/n3/n3_guide.md` — `once`, `not`, conjunction
  - `docs/ru/developer_guide/n3/sources/n3_video_part_3_transcript_gemini.md` — performance tips

**Assessment in tests.md:** 2 questions on iterator and negation

### Lesson 6: Conditional Logic and Small OR (1 hour)

**Learning Objectives:**

- Use `or {}` (2–3 branches) and `if … then … else` correctly
- Combine results with `assert:union`; count and distinct

**Content:**

- Small OR patterns; avoid long chains (prefer sets + `w3list:in`)
  
  - Ultra-simple OR examples (2–3 branches):
    - Attribute A OR B is present
    - Assignee OR Creator equals current user
    - Department is IT OR Sales
- `if/then/else` control flow; triaging logic early
- `assert:union`, `assert:count`, `assert:distinct`, `assert:sort`
- Sources:
  - `docs/ru/developer_guide/n3/n3_guide.md` — operators and asserts
  - `docs/ru/examples/n3_collection_select_conditional.md` — conditional selection
  - `docs/ru/examples/n3_filter_active_tasks.md` — OR filter example
  - `docs/ru/examples/n3_calculate_active_task_accounts.md` — union pattern

**Assessment in tests.md:** 2 questions on `or` and `if`

### Lesson 7: Collections, from/select, Last Item (1 hour)

**Learning Objectives:**

- Build lists with `from { } select` and aggregate
- Get last item via `w3list:last` or `assert:sort`

**Content:**

- `from/select` construction and list types
- Aggregations and list utilities
- Sources:
  - `docs/ru/examples/n3_collection_get_selected_ids.md` — building lists
  - `docs/ru/examples/n3_collection_join_filter.md` — list from joins
  - `docs/ru/examples/n3_periodic_task_notifications.md` — sorting/last
  - `docs/ru/developer_guide/n3/n3_guide.md` — `w3list:*`, `assert:sort`

**Assessment in tests.md:** 2 questions on `from/select` and last item

### Lesson 8: Math, String, Time, List, Nullable (1.5 hours)

**Learning Objectives:**

- Apply `w3math`/`cmwmath`, `w3string`/`cmwstring`, `w3time`/`cmwtime`
- Use `w3list`/`cmwlist` and `cmwnullable:*` safely

**Content:**

- Practical function recipes and data types
- Nullable‑safe comparisons and arithmetic
- Sources:
  - `docs/ru/developer_guide/n3/n3_guide.md` — function catalogs
  - `docs/ru/examples/attribute_date_time_value_format.md` — date/time formatting
  - `docs/ru/examples/n3_collection_join_string.md` — strings & joins
  - `docs/ru/examples/attribute_enum_value_filter.md` — list filters
  - `docs/ru/developer_guide/n3/sources/n3_video_part_4_transcript_gemini.md` — function usage
  - `docs/ru/tutorials/tutorial_architect/lesson_8.md` — UI tasks (cross‑domain)

**Assessment in tests.md:** 2–3 questions on functions and nullable

### Lesson 9: Patterns, Security Context, Debugging (1 hour)

**Learning Objectives:**

- Implement role‑based filters and security context patterns
- Apply reusable N3 patterns and troubleshooting steps

**Content:**

- Security context and current user; role filters
- Pattern cards: small OR, set unions, collection pipelines
- Debug checklist; reduce to minimal triple; error handling patterns
- Sources:
  - `docs/ru/developer_guide/n3/n3_guide.md` — security context, asserts
  - `docs/ru/examples/n3_filter_active_tasks.md` — role/user filters
  - `docs/ru/examples/autonumerating_related_records.md` — pattern reuse
  - `docs/ru/developer_guide/n3/sources/n3_presentation_summary_notebook_lm.md` — pattern highlights

**Assessment in tests.md:** 2 questions on security and debugging

### Lesson 10: Integration & Best Practices (1 hour)

**Learning Objectives:**

- Integrate N3 into end‑to‑end solutions (HR example)
- Use messaging and data I/O patterns in expressions

**Content:**

- Complete candidate selection workflow; performance monitoring
- Email/HTTP/SQL integration touchpoints where expressions apply
- Capstone exercise scaffolding
- Self‑study (optional): deep schema exploration (e.g., `cmw:UserTask`); nullable helpers overview (`cmwnullable:*`)
- Sources:
  - `docs/ru/examples/document_clone_scenario_n3.md` — end‑to‑end cloning flow
  - `docs/ru/examples/autonumerating_records.md` — numbering pattern
  - `docs/ru/examples/n3_periodic_task_notifications.md` — notification logic
  - `docs/ru/examples/n3_calculate_active_task_assignee.md` — assignee logic
  - `docs/ru/examples/attribute_document_add_file_n3.md` — file add via N3
  - `docs/ru/examples/attribute_document_get_file_n3.md` — file get via N3
  - `docs/ru/examples/attribute_enum_compare_value_n3.md` — enum compare
  - `docs/ru/examples/attribute_enum_filter_value_n3.md` — enum filter
  - `docs/ru/examples/attribute_enum_get_data_localized_n3.md` — localized enums
  - `docs/ru/examples/attribute_enum_get_data_n3.md` — enum data
  - `docs/ru/examples/attribute_enum_set_value_n3.md` — enum set value
  - `docs/ru/examples/scenario_verify_data.md` — data verification scenario
  - `docs/ru/examples/scenario_receive_email.md` — receive email
  - `docs/ru/examples/scenario_send_email.md` — send email
  - `docs/ru/examples/http_receive_file.md` — HTTP receive file
  - `docs/ru/examples/http_send_file.md` — HTTP send file
  - `docs/ru/examples/receive_http_example.md` — HTTP receive example
  - `docs/ru/examples/sql_receive_connection.md` — SQL receive
  - `docs/ru/examples/sql_send_connection.md` — SQL send
  - `docs/ru/examples/architect_example.md` — architect example
  - `docs/ru/examples/variables.md` — variables overview
  - `docs/ru/examples/scenario_variables.md` — scenario variables
  - `docs/ru/examples/process_error_monitor.md` — process error checks
  - `docs/ru/examples/index.md` — examples index for cross‑links

**Assessment in tests.md:** 2–3 questions on integration patterns and best practices

## File Structure to Generate

tutorial_n3/
├── intro.md (Course overview and setup)
├── lesson_1.md (Introduction to N3 — All‑in overview)
├── lesson_2.md (Core Syntax, Variables, Query Types)
├── lesson_3.md (Prefixes, URIs, Property Discovery)
├── lesson_4.md (Data Navigation & Variable Assignment)
├── lesson_5.md (Iterator & Performance Basics)
├── lesson_6.md (Conditional Logic and Small OR)
├── lesson_7.md (Collections, from/select, Last Item)
├── lesson_8.md (Math, String, Time, List, Nullable)
├── lesson_9.md (Patterns, Security Context, Debugging)
├── lesson_10.md (Integration & Best Practices)
├── outro.md (Summary and next steps)
└── tests.md (Assessment with answers)

## Agentic Capabilities to Utilize

### File System Access

- **Analyze existing tutorial structures** in `/docs/ru/tutorials/`
- **Examine N3 documentation** in `/docs/ru/developer_guide/n3/`
- **Review HR tutorial content** for business context
- **Access platform documentation** for technical accuracy

### Codebase Search & Analysis

- **Search for N3 examples** and use cases in `/docs/ru/examples/`
- **Find HR-related data models** and relationships
- **Identify platform capabilities** and limitations
- **Locate existing N3 tutorials** and guides

### Content Generation & Editing

- **Create new tutorial files** with proper structure
- **Edit existing files** if needed for consistency
- **Generate metadata** and proper formatting
- **Create comprehensive content** for each lesson

### Quality Assurance

- **Validate technical accuracy** against platform docs
- **Ensure consistency** with existing tutorial patterns
- **Check formatting** and structure compliance
- **Verify pedagogical approach** alignment

## Detailed Requirements

### Target Specifications

- **Audience**: Beginner level, standalone completion
- **Platform**: Comindware Platform 5.0
- **Duration**: 12 hours total (10 lessons + intro + outro + tests)
- **Integration**: HR business logic, loose connection to @/tutorial_hr for context

### Business Context

**HR Candidate Selection Process** providing:

- Candidate data management
- Position requirements and matching
- Interview processes and results
- Offer management and approval workflows
- Data relationships for N3 queries

### Pedagogical Framework (Diátaxis + Computer Science Best Practices)

- **Learning-oriented** approach with concrete actions
- **Progressive complexity** from basic to advanced
- **Performance awareness** and optimization from start
- **Practical application** with real-world problem solving
- **Error handling** and common pitfalls addressed

## Technical Formatting & Structure Requirements

### **Markdown Formatting Standards**

#### **Headings & Structure**

```markdown
# Main Title {: #tutorial_n3_h1_anchor }
## Section Title {: #tutorial_n3_h1_anchor_section_anchor }
### Subsection Title {: #tutorial_n3_h1_anchor_subsection_anchor }
#### Sub-subsection Title {: #tutorial_n3_h1_anchor_sub_subsection_anchor }
```

#### **Text Formatting**

- **Bold text**: Use `**text**` for emphasis and key concepts
- _Italic text_: Use `_text_` for foreign terms, emphasis, and variable names
- `Code snippets`: Use backticks for inline code, N3 expressions, and technical terms
- **Code blocks**: Use triple backticks with language specification for N3 examples, separate language code with a space, e.g. ``` yaml

#### **Lists & Organization**

- **Bullet lists**: Use `-` (dash) for unordered lists
- **Numbered lists**: Use `1.`, `2.`, `N.` for ordered lists
- **Nested lists**: Separate with single newline between levels
- **Mixed lists**: Separate bullet and numbered lists with double newlines
- **Four spaces**: indent with four spaces, not two

**Example:**

``` markdown
1. First numbered item
    
    - Bullet sub-item
        - Nested bullet item
  
2. Second numbered item
```

#### **Anchors & Cross-References**

- **Internal anchors**: Add `{: #tutorial_n3_lesson_X_anchor_name }` for all headings
- **Cross-references**: Use `[link text](#anchor_name)` for internal navigation
- **External references**: Use `[link text][article_anchor]` format
- **Consistent naming**: Follow pattern `tutorial_n3_[lesson]_[section]`

#### **Hyperlinks & References**

- **Tutorial cross-references**: `[N3 tutorial lesson 1][tutorial_n3_lesson_1]` (using h1 anchors)
- **Internal tutorial links**: `[next lesson](#tutorial_n3_lesson_2)`
- **External documentation**: `[N3 guide][n3_guide]` (using h1 anchors)
- **Platform documentation**: `[ElasticData][elasticdata_description]` (using h1 anchors)

#### **Includes & Snippets**

- **Reusable content**: In the Intro section, include standard tutorial elements and notices:
    **Предусловия:** пройден [урок X «XXXX»][tutorial_n3_lesson_X].
    - **Расчётная продолжительность:** XX мин.
    - **Version notice**: `{% include-markdown ".snippets/tutorial_version_notice.md" %}`
- **Hyperlinks snippet**: At the very end of each article add `{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}` followed by a new line

#### **Special Elements**

- **Admonitions**: Use `!!! note "Примечание"`, `!!! warning "Бизнес-логика"`, `!!! tip "Совет"`, `!!! question "Определения"`, `!!! example "Практический пример"`, `!!! example "Практическое задание"`  for special notices
- **Code highlighting**: Specify language for all code blocks (`n3`, `yaml`, `markdown`)
- **Images**: Use `_![alt text](img/tutorial_n3_lesson_3_filename.png)_` format for illustration placeholders.
- **Tables**: Use proper markdown table syntax with alignment

### **File Structure & Metadata**

#### **YAML Front Matter**

``` yaml
---
title: '[Lesson Title in single quotes]'
kbTitle: '[Full KB Title  in single quotes]'
kbId: [Empty]
tags:
  # Common tutorial_n3 tags
  - N3
  - Notation3
  - RDF
  - Turtle
  - ElasticData
  - выражения
  - разработка
  - обучение
  - учебник
  - уроки
  - платформа
  # Lesson-specific tags
  - [specific for lesson, relevant N3 and business-oriented]
hide: tags
---
```

#### **Section Structure (Each Lesson)**

``` markdown
## Введение {: #tutorial_n3_lesson_X_intro }
    **Предусловия:** — prerequisites
    **Расчётная продолжительность:** — duration
    !!! warning "Бизнес-логика" — business case admonition 
    {% include-markdown ".snippets/tutorial_version_notice.md" %} — version snippet
## Темы, навыки и задания урока {: #tutorial_n3_lesson_X_taxonomy }
## Определения {: #tutorial_n3_lesson_X_definitions } — Include standard terminology and concepts
## Main lesson sections and subsections {: #tutorial_n3_lesson_X_section_anchors }
## Практическое задание {: #tutorial_n3_lesson_X_practical_task } — Include a short task to practice the lesson concepts in the Platform
## Итоги урока {: #tutorial_n3_lesson_X_summary } — Include lesson summary and transition to the next lesson
```

### **Content Organization Patterns**

#### Темы, навыки и задания урока — **Learning Objectives Section**

```markdown
### Темы {: #tutorial_n3_lesson_X_topics }
- [Topic 1]
- [Topic 2]

### Навыки {: #tutorial_n3_lesson_X_skills }
- [Skill 1]
- [Skill 2]

### Задания {: #tutorial_n3_lesson_X_tasks }
- [Task 1]
- [Task 2]
```

#### **Pattern Cards (reusable snippets to include where relevant)**

- Multi-step navigation: subject → link → target (name intermediates clearly)
- Small OR: two or three branches only; otherwise use sets + `assert:union` + `w3list:in`
- Collection to list to aggregate: `from-select` → list op (sum/sort/last)

#### **Definitions Section**

```markdown
<div class="admonition question" markdown="block">

## Определения {: .admonition-title #tutorial_n3_lesson_X_definitions}

- **Term 1** — Definition with proper formatting
- **Term 2** — Definition with proper formatting

</div>
```

#### **Content Sections**

- **Step-by-step instructions** with numbered lists
- **Code examples** in proper N3 syntax blocks
- **Practical exercises** with clear objectives
- **Troubleshooting tips** for common issues
- **Performance considerations** where relevant

#### **Assessment Section**

- **2-3 questions per lesson** with progressive difficulty
- **Mix of theoretical and practical** questions
- **Clear question formatting** with proper markdown
- **Answers provided** in tests.md file

### **Navigation & Cross-References**

#### **Lesson Navigation**

- **Previous lesson**: `[предыдущий урок][tutorial_n3_lesson_X_minus_1]`
- **Next lesson**: `[следующий урок][tutorial_n3_lesson_X_plus_1]`
- **Course overview**: `[обзор курса][tutorial_n3_intro]`
- **Final assessment**: `[итоговое тестирование][tutorial_n3_tests]`

#### **External References**

- **N3 documentation**: Link to relevant N3 guides and examples
- **Platform features**: Reference ElasticData and expression capabilities
- **Further learning**: Links to advanced topics and resources

### **Quality Standards**

#### **Formatting Consistency**

- **Consistent heading levels** throughout all lessons
- **Uniform anchor naming convention** {: #tutorial_n3_lesson_X }
- **Standardized list formatting and spacing**
- **Consistent code block formatting** with language specification

#### **Content Structure**

- **Logical progression** from basic to advanced concepts
- **Clear learning objectives** for each section
- **Practical examples** for every concept
- **Assessment alignment** with learning objectives

#### **Technical Accuracy**

- **N3 syntax validation** against platform documentation
- **Correct terminology** usage throughout
- **Accurate examples** that work in Comindware Platform
- **Proper error handling** and troubleshooting guidance

## Content Requirements

### Each Lesson Must Include

1. **Введение** - Clear learning objectives
2. **Темы, навыки и задания** - Specific skills and tasks
3. **Определения** - Key concepts and terminology
4. **Основное содержание** - Step-by-step instruction
5. **Практическое задание** - Include a short task to practice the lesson concepts in the Platform
6. **Итоги урока** - Summary and reinforcement, followed by a navigation link with brief description of next lesson content

### Lesson Transition Format

Each lesson must end with a transition section following this pattern:

```markdown
## Итоги урока {: #tutorial_n3_lesson_X_summary }

[Lesson summary content...]

В ходе [следующего урока][tutorial_n3_lesson_X_plus_1] вы {brief description of next lesson content}.
```

**Examples:**
- **Lesson 1**: `В ходе [следующего урока][tutorial_n3_lesson_2] вы закрепите синтаксис и формы запросов.`
- **Lesson 2**: `В ходе [следующего урока][tutorial_n3_lesson_3] вы изучите префиксы, URI и поиск атрибутов.`
- **Lesson 3**: `В ходе [следующего урока][tutorial_n3_lesson_4] вы освоите навигацию по данным и присвоение переменных.`
- **Lesson 4**: `В ходе [следующего урока][tutorial_n3_lesson_5] вы разберётесь с итератором и производительностью.`
- **Lesson 5**: `В ходе [следующего урока][tutorial_n3_lesson_6] вы проработаете условную логику и короткие OR.`
- **Lesson 6**: `В ходе [следующего урока][tutorial_n3_lesson_7] вы научитесь работать со списками и from/select.`
- **Lesson 7**: `В ходе [следующего урока][tutorial_n3_lesson_8] вы примените функции для чисел, строк и дат, а также nullable.`
- **Lesson 8**: `В ходе [следующего урока][tutorial_n3_lesson_9] вы отработаете паттерны, безопасность и отладку.`
- **Lesson 9**: `В ходе [следующего урока][tutorial_n3_lesson_10] вы интегрируете N3 в полноценное решение.`
- **Lesson 10**: `В [итоговом тестировании][tutorial_n3_tests] вы проверите свои знания по всему курсу.`

### Assessment Strategy

- **2-3 questions per lesson** (total: 20-30 questions)
- **Answers provided at bottom** of `tests.md`
- **Mix of theoretical and practical**
- **Progressive difficulty** matching lesson complexity

## Technical Implementation

### Content Standards
- **Clear Russian language** with proper technical terms
- **Code blocks** for all N3 expressions
- **Practical examples** for every concept
- **Step-by-step instructions** with screenshots if needed
- **Troubleshooting guidance** for common issues

### Integration Points
- **Reference existing N3 docs** when available
- **Link to HR tutorial concepts** (optional, not required)
- **Include downloadable examples** and templates
- **Provide resource links** for further learning
- **Tie-in example sources** (use as references or exercises):
  - `docs/ru/examples/n3_calculate_active_task_accounts.md`
  - `docs/ru/examples/n3_calculate_active_task_assignee.md`
  - `docs/ru/examples/n3_collection_get_selected_ids.md`
  - `docs/ru/examples/n3_collection_join_filter_hierarchy.md`
  - `docs/ru/examples/n3_collection_join_filter.md`
  - `docs/ru/examples/n3_collection_join_string.md`
  - `docs/ru/examples/n3_collection_select_conditional.md`
  - `docs/ru/examples/n3_filter_active_tasks.md`
  - `docs/ru/examples/n3_periodic_task_notifications.md`
- **Theory sources** (use for definitions, diagrams, and foundational explanations):
  - `docs/ru/developer_guide/n3/n3_guide.md`
  - `docs/ru/developer_guide/n3/n3_tutorial.md`
  - `docs/ru/developer_guide/n3/n3_knowledge_graphs.md`
  - `docs/ru/developer_guide/n3/n3_model.md`
  - `docs/ru/developer_guide/n3/n3_ontology.md`
  - `docs/ru/developer_guide/n3/n3_notation.md`
  - `docs/ru/developer_guide/n3/n3_ontology_structure.md`
  - `docs/ru/developer_guide/n3/n3_graphs.md`
  - `docs/ru/developer_guide/n3/n3_glossary.md`
  - `docs/ru/developer_guide/n3/sources/presentation_converted_from_pdf.md`
  - `docs/ru/developer_guide/n3/sources/n3_tutorial_plan_angelina_t.md`
  - `docs/ru/developer_guide/n3/sources/n3_video_transcript_complete_notebook_lm.md`

### Debug Checklist (include a short note where troubleshooting applies)
- Validate prefixes and anchors
- Reduce to minimal failing triple; add back incrementally
- Check iterator fan-out; move selective triples up
- Use `once {}` only when safe (no multivalued links)
- Verify dots and braces; confirm variable reuse is intentional

## Quality Assurance Checklist

### Content Quality

- [ ] **Technical accuracy** verified against platform docs
- [ ] **Pedagogical approach** follows approved lesson plan
- [ ] **Progressive complexity** properly implemented
- [ ] **Practical examples** provided for all concepts
- [ ] **Business context** consistently applied

### Structure Quality

- [ ] **Metadata** properly formatted
- [ ] **Sections** follow established patterns
- [ ] **Navigation** and linking implemented
- [ ] **Formatting** consistent throughout
- [ ] **Assessment** properly structured

### Integration Quality

- [ ] **Platform capabilities** accurately represented
- [ ] **N3 syntax** follows platform specifications
- [ ] **Business logic** realistic and applicable
- [ ] **Resource links** functional and relevant
- [ ] **Tutorial independence** maintained

## Execution Instructions

1. **Follow approved lesson plan** exactly as specified
2. **Analyze existing tutorials** for structure and patterns
3. **Research N3 documentation** for technical accuracy
4. **Generate metadata** and file structure
5. **Create content** following established patterns
6. **Implement progressive complexity** in N3 concepts
7. **Include practical exercises** and examples
8. **Generate assessment questions** with answers
9. **Validate consistency** with existing content
10. **Ensure standalone completeness** while maintaining continuity
11. **Final quality check** and formatting verification

## Success Criteria

- **Complete tutorial** covering all N3 fundamentals
- **Standalone functionality** without prerequisites
- **Educational continuity** with existing tutorials
- **Practical applicability** in HR business context
- **Progressive skill development** from beginner to intermediate
- **Consistent quality** matching existing tutorial standards
- **12-hour completion time** maintained
- **All assessment questions** properly structured with answers
