# Discovery Log

Session discoveries that haven't yet been migrated to durable skills or rules.
Review before starting related work. Move to skills/rules when stable.

## 2026-06-09

- PHPKB examples category ID is `909` (used as `--target-category-id` when cloning new example articles). End-to-end publication sequence: clone → kbId in frontmatter → hyperlink map entry → `mkdocs build -f mkdocs_for_kb_import_ru.yml` → `phpkb_update_articles.py` → `phpkb_import_for_rag.py` → `phpkb_ingest.py` → commit+push sibling repo.
- `{{ product Name }}` with a space silently causes a macros syntax error. Only `{{ productName }}` and `{{ companyName }}` are valid macros from `mkdocs_common.yml`.
- `mkdocs_autorefs` emits `WARNING: Could not find cross-reference target` for links using anchors absent from `hyperlinks_mkdocs_to_kb_map.md`. Always verify all `[text][anchor]` references resolve against the map before publishing.
- Process-task scripts use `void Main(ScriptContext, Entities)` — no return value. Button scripts use `UserCommandResult Main(UserCommandContext, Entities)`. Scenario scripts use `string Main(string ObjectID, [Entities])`. Match the script type to the automation context: process tasks for unattended data import/sync.
- `for_kb_import_ru/` is tracked in this repo — commit generated HTML exports alongside source changes, do not discard them.
