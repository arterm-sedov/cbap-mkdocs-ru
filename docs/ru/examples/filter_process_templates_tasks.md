---
title: Фильтр списка по задачам из нескольких шаблонов процесса
kbId: 5281
tags:
    - N3
    - выражение на N3
    - пример
    - процессы
hide: tags
---

# Фильтр списка по задачам из нескольких шаблонов процесса {: #filter_process_templates_tasks }

Для того чтобы получить список всех задач из определенных Шаблонов процесса в настроенном Шаблоне записи, введите следующее выражение:

```turtle
@prefix cmw: <http://comindware.com/logics#>.
@prefix container: <http://comindware.com/ontology/container#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
@prefix session: <http://comindware.com/ontology/session#>.
{
  (
    {
      ?cont1 container:alias "Proverkadokumentov".
        ?item cmw:container ?cont1.
      ?item a cmw:UserTask.
    }
{
      ?cont2 container:alias "Podpisaniedogovora".
        ?item cmw:container ?cont2.
      ?item a cmw:UserTask.
    }
)
    assert:union true.

}
```

**Здесь:**

| Значение | Описание |
| -------- | -------- |
| `Proverkadokumentov, Podpisaniedogovora` | Системные имена Шаблонов процесса. |

В данном примере указано два Шаблона процесса для вывода задач, однако их может быть и больше.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
