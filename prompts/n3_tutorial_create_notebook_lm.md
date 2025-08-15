Read all the provided resources: videos, presentations, guides.

Generate in Russian a beginner tutorial teaching the users to apply N3 (Notation 3/Turtle/RDF) expressions specifically in Comindware Platform.

The tutorial must be based on a concise, useful, and valid end-to-end HR business case (maybe candidate selection or something like this).

The tutorial must fit in 8 hours completion time (reading and completing the tasks).

The tutorial should have the following structure:

- Course description
- Lessons 1-N
- Outro
- Quiz and answer keys

Intro should have the following sections:
- Введение
- Сквозной сценарий
Цели обучения
Результаты обучения
Содержание курса
Ключевые понятия и сущности Comindware Platform
Начало обучения

Each lesson should contain the following sections:
- Введение
- Темы, навыки и задания урока
- Определения
- Lesson content
- Тестирование
- Итоги урока

The outro should contain the following sections:
-Чему вы научились
-Что дальше
-Рекомендуемые ресурсы для самостоятельного изучения
-Темы для дальнейшего изучения возможностей платформы
-Примеры и идеи для самостоятельных экспериментов

# Enhanced N3 Tutorial Creation Prompt for NotebookLM

## Context
You are creating a comprehensive N3 (Notation 3/Turtle/RDF) tutorial for Comindware Platform users. This tutorial should be standalone but loosely connected to the existing HR tutorial for educational continuity.

## Tutorial Specifications

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

### Pedagogical Framework (Diátaxis)
- **Learning-oriented** approach
- **Concrete actions** with visible results
- **Minimal explanation**, maximum doing
- **Confidence building** through success
- **Progressive complexity** from basic to advanced


### Structure Requirements
- **Course description** (intro.md)
- **5 lessons** (lesson_1.md through lesson_5.md)
- **Outro** (outro.md)
- **Quiz and answer keys** (tests.md)

### Time Commitment
- **8 hours total** (reading and completing tasks)
- Approximately 1.5 hours per lesson

## Content Guidelines

### Business Case Foundation
Use the **HR candidate selection and recruitment process** as the business scenario. This provides:
- Familiar business context for users
- Complex data relationships that benefit from N3 queries
- Progressive complexity opportunities
- Real-world applicability

### Pedagogical Approach (Diátaxis Framework)
- **Learning-oriented**, not task-oriented
- Focus on **concrete actions** with **visible results**
- **Minimize explanation**, maximize doing
- Build **confidence through successful completion**
- Use **"we" language** to create teacher-student relationship
- **Progressive complexity** from simple to advanced

## Detailed Structure

### Intro.md Sections
- Введение (Introduction)
- Сквозной сценарий (End-to-end scenario)
- Цели обучения (Learning objectives)
- Результаты обучения (Learning outcomes)
- Содержание курса (Course content)
- Ключевые понятия и сущности Comindware Platform (Key concepts)
- Начало обучения (Getting started)

### Each Lesson Must Include
1. **Введение** - Clear learning objectives
2. **Темы, навыки и задания** - Specific skills and tasks
3. **Определения** - Key concepts and terminology
4. **Основное содержание** - Step-by-step instruction
5. **Тестирование** - 2-3 assessment questions
6. **Итоги урока** - Summary and reinforcement

### Outro.md Sections
- Чему вы научились (What you learned)
- Что дальше (What's next)
- Рекомендуемые ресурсы для самостоятельного изучения (Recommended resources)
- Темы для дальнейшего изучения возможностей платформы (Further platform topics)
- Примеры и идеи для самостоятельных экспериментов (Examples and ideas for self-experimentation)

## N3 Progression
- **Lesson 1**: Basic triples, syntax, simple queries
  - Triples, variables, ?item/?value, basic syntax rules
  
- **Lesson 2**: Joins, filtering, basic relationships  
  - object:findAttribute, basic joins, simple filtering
  
- **Lesson 3**: Conditional logic and iteration
  - if/then/else, or, once, basic iteration patterns
  
- **Lesson 4**: Aggregations and list operations
  - from {} select, math:sum, assert:count, basic list handling
  
- **Lesson 5**: Advanced operations and optimization
  - assert:union, assert:distinct, complex comparisons, performance considerations

## Assessment Strategy
- **2-3 questions per lesson**
- **Answers provided at the bottom** of tests.md
- **Mix of theoretical and practical questions**
- **Progressive difficulty** matching lesson complexity

## Technical Requirements

### Metadata Structure
Each file should include:
```yaml
---
title: '[Lesson Title]'
kbTitle: '[Full KB Title]'
kbId: [empty]
tags: [Relevant tags]
hide: tags
---
```

### Content Formatting
- Use **bold** for important concepts
- Use _italic_ for emphasis
- Use `code blocks` for N3 expressions
- Include practical examples and exercises
- Provide clear step-by-step instructions

### Integration Points
- Reference existing N3 documentation when available
- Include links to related HR tutorial concepts (optional)
- Provide downloadable N3 examples
- Include troubleshooting guidance

## Quality Standards
- **Clear and concise** explanations
- **Practical examples** for every concept
- **Progressive complexity** building confidence
- **Real-world applicability** in HR context
- **Consistent formatting** and structure
- **Comprehensive coverage** of N3 fundamentals

## Output Format
Generate each file as a separate markdown document with proper metadata, clear structure, and comprehensive content that follows the established tutorial patterns while focusing specifically on N3 expression mastery in the context of HR candidate management.

## Quality Assurance Checklist

### Content Quality
- [ ] **Technical accuracy** verified against platform docs
- [ ] **Pedagogical approach** follows Diátaxis principles
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

## Success Criteria
- **Complete tutorial** covering all N3 fundamentals
- **Standalone functionality** without prerequisites
- **Educational continuity** with existing tutorials
- **Practical applicability** in HR business context
- **Progressive skill development** from beginner to intermediate
- **Consistent quality** matching existing tutorial standards