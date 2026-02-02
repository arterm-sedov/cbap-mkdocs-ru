# Validation: ai_features_guide.md vs modern docs/ru articles

**Reference set:** Articles under `docs/ru` recently updated (git log 2025–2026):  
`adapters.md`, `backup/configure.md`, `count_records_no_archive.md`, `n3_filter_active_tasks.md`,  
`db_migrate_4.2_to_4.7.md`, `send_http_example_csharp.md`, `ad_authentication_configure.md`, and similar.

---

## Frontmatter

| Check | Modern pattern | ai_features_guide | Status |
|-------|----------------|-------------------|--------|
| **title** | Short; may differ from H1 | `Возможности ИИ в платформе` | OK |
| **kbTitle** | Extended; matches H1 when present | `Возможности ИИ в платформе. Настройка адаптера, low-code-агентов и тестирование mock-операций` | OK |
| **kbId** | Present in published KB articles | Missing | Optional: add when article is published to KB |
| **tags** | Sorted, relevant | Present, sorted | OK |
| **hide** | `hide: tags` or `hide: - tags` | `hide: tags` | OK (both forms used in repo) |

---

## Structure and headings

| Check | Modern pattern | ai_features_guide | Status |
|-------|----------------|-------------------|--------|
| **H1** | `# Title. Subtitle {: #anchor }` | Matches kbTitle + `{: #ai_features_guide }` | OK |
| **H2/H3** | Noun/action phrases; no «Инструкция по…» | «Настройка адаптера и операций», «Тестирование операций (mock)» and similar | OK |
| **Anchors** | Semantic, prefixed (e.g. `article_id_heading`) | `ai_features_guide_*` | OK |
| **pageBreakBefore** | On major H2 where needed | Used on main procedure sections | OK |

---

## Introduction

| Check | Modern pattern | ai_features_guide | Status |
|-------|----------------|-------------------|--------|
| **Opening** | «Здесь представлены…» / «В **{{ productName }}**…» | «Здесь представлены пошаговые инструкции…» | OK |
| **TOC / list** | Bullet list with internal links | Dash list with `[Section](#anchor)` | OK |

---

## Body

| Check | Modern pattern | ai_features_guide | Status |
|-------|----------------|-------------------|--------|
| **Numbered steps** | `1.` `2.` for procedures | Used | OK |
| **Bullet lists** | `-` (dash) | Used | OK |
| **Bold** | `**text**` for UI and terms | Used | OK |
| **Italic** | `_text_` for emphasis/terms | Used | OK |
| **Product name** | `**{{ productName }}**` | Used | OK |

---

## End of article

| Check | Modern pattern | ai_features_guide | Status |
|-------|----------------|-------------------|--------|
| **Related block** | `<div class="relatedTopics" markdown="block">` | Present | OK |
| **Snippet** | `--8<-- "related_topics_heading.md"` | Present (resolved from `docs/ru/.snippets/`) | OK |
| **Related links** | `_[Title][ref]_` with refs from map | `_[Адаптеры…][adapters]_` etc. | OK |
| **Hyperlinks include** | `{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}` | Present | OK |

---

## Summary

- **Aligns with modern articles** in: frontmatter (title/kbTitle/tags/hide), H1/H2 wording and anchors, introduction style, step and list formatting, Related block and hyperlinks include.
- **Optional:** add `kbId` when the article is published to the knowledge base.

No mandatory changes; article is consistent with current `docs/ru` conventions.
