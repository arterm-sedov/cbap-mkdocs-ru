# N3 Tutorial Generation Prompt for Cursor

## Mission
Generate a complete, standalone N3 (Notation 3/Turtle/RDF) tutorial for Comindware Platform 5.0 users, loosely integrated with the existing HR tutorial for educational continuity.

## Agentic Capabilities to Utilize

### 1. File System Access
- **Analyze existing tutorial structures** in `/docs/ru/tutorials/`
- **Examine N3 documentation** in `/docs/ru/developer_guide/n3/`
- **Review HR tutorial content** for business context
- **Access platform documentation** for technical accuracy

### 2. Codebase Search & Analysis
- **Search for N3 examples** and use cases in `/docs/ru/examples/`
- **Find HR-related data models** and relationships
- **Identify platform capabilities** and limitations
- **Locate existing N3 tutorials** and guides

### 3. Content Generation & Editing
- **Create new tutorial files** with proper structure
- **Edit existing files** if needed for consistency
- **Generate metadata** and proper formatting
- **Create comprehensive content** for each lesson

### 4. Quality Assurance
- **Validate technical accuracy** against platform docs
- **Ensure consistency** with existing tutorial patterns
- **Check formatting** and structure compliance
- **Verify pedagogical approach** alignment

## Detailed Requirements

### Target Specifications
- **Audience**: Beginner level, standalone completion
- **Platform**: Comindware Platform 5.0
- **Duration**: 8 hours total (5 lessons + intro + outro + tests)
- **Integration**: Loose connection to HR tutorial for context

### Business Context
**HR Candidate Selection Process** providing:
- Candidate data management
- Position requirements and matching
- Interview processes and results
- Offer management and approval workflows
- Complex data relationships for N3 queries

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
# Main Title {: #article_anchor }
## Section Title {: #article_anchor_section_anchor }
### Subsection Title {: #article_anchor_subsection_anchor }
#### Sub-subsection Title {: #article_anchor_sub_subsection_anchor }
```

#### **Text Formatting**
- **Bold text**: Use `**text**` for emphasis and key concepts
- _Italic text_: Use `_text_` for foreign terms, emphasis, and variable names
- `Code snippets`: Use backticks for inline code, N3 expressions, and technical terms
- **Code blocks**: Use triple backticks with language specification for N3 examples

#### **Lists & Organization**
- **Bullet lists**: Use `-` (dash) for unordered lists
- **Numbered lists**: Use `1.` for ordered lists
- **Nested lists**: Separate with single newline between levels
- **Mixed lists**: Separate bullet and numbered lists with double newlines
- **Four spaces**: indent with four spaces, not two

**Example:**
```markdown
1. First numbered item
    
    - Bullet sub-item
        - Nested bullet item
  
2. Second numbered item
```

#### **Anchors & Cross-References**
- **Internal anchors**: Use `{: #anchor_name }` syntax for all headings
- **Cross-references**: Use `[link text](#anchor_name)` for internal navigation
- **External references**: Use `[link text][article_anchor]` format
- **Consistent naming**: Follow pattern `tutorial_n3_[lesson]_[section]`

#### **Hyperlinks & References**
- **Tutorial cross-references**: `[N3 tutorial lesson 1][tutorial_n3_lesson_1]` (using h1 anchors)
- **Internal tutorial links**: `[next lesson](#tutorial_n3_lesson_2)`
- **External documentation**: `[N3 guide][n3_guide]` (using h1 anchors)
- **Platform documentation**: `[ElasticData][elasticdata_description]` (using h1 anchors)

#### **Includes & Snippets**
- **Reusable content**: Include standard tutorial elements and notices:
    **Предусловия:** пройден [урок X «XXXX»][tutorial_n3_lesson_X].
    - **Расчётная продолжительность:** XX мин.
    - **Version notice**: Include platform version notice:
        `{% include-markdown ".snippets/tutorial_version_notice.md" %}`
- **Common definitions**: Include standard terminology and concepts
- **Common snippet**: At the very end of each article add `{% include-markdown ".snippets/filename.md" %}` followed by a new line

#### **Special Elements**
- **Admonitions**: Use `!!! note`, `!!! warning`, `!!! tip`, , `!!! example`  for special notices
- **Code highlighting**: Specify language for all code blocks (`n3`, `yaml`, `markdown`)
- **Images**: Use `_![alt text](img/filename.png)_` format
- **Tables**: Use proper markdown table syntax with alignment

### **File Structure & Metadata**

#### **YAML Front Matter**
```yaml
---
title: '[Lesson Title]'
kbTitle: '[Full KB Title]'
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
  - [specific lesson, relevant N3 and business-oriented]
hide: tags
---
```

#### **Section Structure (Each Lesson)**

```markdown
## Введение {: #tutorial_n3_lesson_X_intro }
    **Предусловия:** — prerequisites
    **Расчётная продолжительность:** — duration
    !!! warning "Бизнес-логика" — business case admonition 
    {% include-markdown ".snippets/tutorial_version_notice.md" %} — version snippet
## Темы, навыки и задания урока {: #tutorial_n3_lesson_X_taxonomy }
## Определения {: #tutorial_n3_lesson_X_definitions }
## Main lesson sections and subsections {: #tutorial_n3_lesson_X_section_anchors }
## Тестирование {: #tutorial_n3_lesson_X_testing }
## Итоги урока {: #tutorial_n3_lesson_X_results }
```

### **Content Organization Patterns**

#### **Learning Objectives Section**
```markdown
### Темы {: #topics }
- [Topic 1]
- [Topic 2]

### Навыки {: #skills }
- [Skill 1]
- [Skill 2]

### Задания {: #tasks }
- [Task 1]
- [Task 2]
```

#### **Definitions Section**
```markdown
<div class="admonition question" markdown="block">

## Определения {: #tutorial_n3_lesson_X_definitions }

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

## Lesson Plan Structure

### Lesson 1: N3 Foundation & Platform Context (1.5 hours)

**Learning Objectives:**
- Understand RDF and graph database concepts
- Master triple structure and basic N3 syntax
- Grasp five types of queries and interpreter behavior
- Learn platform N3 editor usage

**Content:**
- RDF and ElasticData technology overview
- Triple structure with visual examples
- Basic syntax, variables, and `?item`/`?value` parameters
- Simple HR queries (candidate → department)
- Platform N3 editor introduction — very brief

**Assessment:** 2-3 questions on triple structure and basic syntax

### Lesson 2: Data Navigation & Discovery (2 hours)

**Learning Objectives:**
- Master `object:findProperty` for attribute discovery
- Navigate complex data relationships
- Understand system vs. application attributes
- Learn variable assignment patterns and iterator mechanics

**Content:**
- Multi-step navigation (candidate → manager → department)
- URI and namespace concepts
- Variable assignment patterns (3 types from tutorial)
- Iterator mechanics and collection processing
- Practical exercise: Build candidate filtering system

**Assessment:** 2-3 questions on attribute discovery and navigation

### Lesson 3: Advanced Logic & Performance (2 hours)

**Learning Objectives:**
- Implement complex `or` operators for priority, user, or department selection filtering
- Use conditional logic and performance optimization
- Master logical assertions and control flow
- Apply debugging techniques and error handling

**Content:**
- Conditional filtering patterns (`or`)
- Conditional logic (`if-then-else`)
- Performance optimization (`once`, `assert:union`)
- Logical assertions (`assert:count`, `assert:distinct`, `assert:sort`)
- Debugging techniques and common pitfalls

**Assessment:** 2-3 questions on logical operators and performance

### Lesson 4: Collection Processing & Functions (1.5 hours)
**Learning Objectives:**
- Master collection manipulation and aggregation
- Apply mathematical and string functions
- Use date/time operations and list processing
- Implement complex data transformations

**Content:**
- `from-select` construction for data aggregation
- Collection manipulation (`list:append`, `assert:union`)
- Mathematical functions (`w3math`, `cmwmath`)
- String operations (`w3string`, `cmwstring`)
- Date/time functions (`w3time`, `cmwtime`)
- List operations (`w3list`, `cmwlist`)

**Assessment:** 2-3 questions on collection processing and functions

### Lesson 5: Real-World Integration & Best Practices (1 hour)
**Learning Objectives:**
- Integrate all N3 concepts in complete business solution
- Apply performance monitoring and optimization
- Implement role-based access control patterns
- Master common patterns and best practices

**Content:**
- Complete HR candidate management system
- Performance monitoring and optimization
- Common patterns and anti-patterns
- Platform-specific features and capabilities
- Final project: End-to-end candidate selection workflow

**Assessment:** 2-3 questions on integration and best practices

## File Structure to Generate

tutorial_n3/
├── intro.md (Course overview and setup)
├── lesson_1.md (N3 Foundation & Platform Context)
├── lesson_2.md (Data Navigation & Discovery)
├── lesson_3.md (Advanced Logic & Performance)
├── lesson_4.md (Collection Processing & Functions)
├── lesson_5.md (Real-World Integration & Best Practices)
├── outro.md (Summary and next steps)
└── tests.md (Assessment with answers)

## Content Requirements

### Each Lesson Must Include
1. **Введение** - Clear learning objectives
2. **Темы, навыки и задания** - Specific skills and tasks
3. **Определения** - Key concepts and terminology
4. **Основное содержание** - Step-by-step instruction
5. **Тестирование** - 2-3 assessment questions
6. **Итоги урока** - Summary and reinforcement
7. **Переход к следующему уроку** - Navigation link with brief description of next lesson content

### Lesson Transition Format
Each lesson must end with a transition section following this pattern:

```markdown
## Результаты {: #tutorial_n3_lesson_X_results }

[Lesson summary content...]

В [следующем уроке][tutorial_n3_lesson_X_plus_1] вы {brief description of next lesson content}.
```

**Examples:**
- **Lesson 1**: `В [следующем уроке][tutorial_n3_lesson_2] вы научитесь навигации по данным и обнаружению атрибутов.`
- **Lesson 2**: `В [следующем уроке][tutorial_n3_lesson_3] вы освоите продвинутую логику и оптимизацию производительности.`
- **Lesson 3**: `В [следующем уроке][tutorial_n3_lesson_4] вы изучите обработку коллекций и функции.`
- **Lesson 4**: `В [следующем уроке][tutorial_n3_lesson_5] вы интегрируете все концепции N3 в реальное бизнес-решение.`
- **Lesson 5**: `В [итоговом тестировании][tutorial_n3_tests] вы проверите свои знания по всему курсу.`

### Assessment Strategy
- **2-3 questions per lesson** (total: 10-15 questions)
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
- **8-hour completion time** maintained
- **All assessment questions** properly structured with answers