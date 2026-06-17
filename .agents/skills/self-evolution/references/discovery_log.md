# Discovery Log

Session discoveries that haven't yet been migrated to durable skills or rules.
Review before starting related work. Move to skills/rules when stable.

## 2026-06-09

- PHPKB examples category ID is `909` (used as `--target-category-id` when cloning new example articles). End-to-end publication sequence: clone → kbId in frontmatter → hyperlink map entry → `mkdocs build -f mkdocs_for_kb_import_ru.yml` → `phpkb_update_articles.py` → `phpkb_import_for_rag.py` → `phpkb_ingest.py` → commit+push sibling repo.
- `{{ product Name }}` with a space silently causes a macros syntax error. Only `{{ productName }}` and `{{ companyName }}` are valid macros from `mkdocs_common.yml`.
- `mkdocs_autorefs` emits `WARNING: Could not find cross-reference target` for links using anchors absent from `hyperlinks_mkdocs_to_kb_map.md`. Always verify all `[text][anchor]` references resolve against the map before publishing.
- Process-task scripts use `void Main(ScriptContext)` — no return value. Button scripts use `UserCommandResult Main(UserCommandContext)`. Scenario scripts use `string Main(string ObjectID)`. Match the script type to the automation context: process tasks for unattended data import/sync. **Note: `Comindware.Entities entities` parameter is deprecated and removed from the API** — articles updated 2026-06-15 (see 2026-06-15 entry below).
- `for_kb_import_ru/` is tracked in this repo — commit generated HTML exports alongside source changes, do not discard them.

## 2026-06-15

- `Comindware.Entities entities` parameter is deprecated and removed from the platform C# API. All KB C# code examples must strip it from method signatures and body. Three pattern variants in signatures: (A) `, Comindware.Entities entities` as trailing parameter, (B) standalone `Comindware.Entities entities // ...` description lines, (C) `[Comindware.Entities entities]` optional-bracket syntax. Body usages like `entities.ApplicationStatus.Where(...)` need separate handling — the replacement API depends on context. Script at `utilities/remove_entities_param.py` automates signatures; body cleanup is manual.
- PHPKB-imported articles (KBID-prefixed filenames like `5000-*.md`) are raw imports missing H1 anchors, language-tagged code blocks (` ```cs `), and frontmatter tags. Format them to match non-KBID articles. Bold pseudo-headings like `**Section Title**` should be promoted to `## Section Title {: #anchor }`.
- Never manually edit `phpkb_content/` — all changes go in `docs/`.
- When applying the same logical changes across diverged branches (v5, v6), prefer running transformation scripts directly on each branch's files. Cherry-picking creates merge conflicts on every file because both branches receive identical diffs against different bases.

## 2026-06-17

- Zero git churn in `phpkb_content_rag/` after an import means the source articles are already current — that's a good control.
