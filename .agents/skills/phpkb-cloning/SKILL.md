---
name: phpkb-cloning
description: "Use when working on the PHPKB cloning and post-clone migration workflow in this repository: creating a new PHPKB section for a new product version, cloning PHPKB categories or articles, updating cloned PHPKB article/category links, migrating local docs IDs with clone mappings, fixing related topics after cloning, or analyzing/updating scripts in utilities/phpkb_cloning."
---

# PHPKB Cloning

Use this skill to work safely with the repository scripts that clone PHPKB content and clean up cloned IDs, links, and related-topic markup.

Scripts live in `utilities/phpkb_cloning/`. Run them from the repository root unless the script says otherwise.

## Script Roster

| Script | Purpose | Main side effects |
|---|---|---|
| `utilities/phpkb_cloning/phpkb_clone.py` | Clone PHPKB categories and articles inside the database. Can clone whole category trees or individual articles. | Inserts new DB rows; maintains article/category mapping; clones article attachment and custom data backrefs. |
| `utilities/phpkb_cloning/phpkb_clone_update_links.py` | Update PHPKB article/category links after cloning or migration using mapping JSON. Optional product/version replacements can be enabled explicitly. | Connects to DB; CLI mode is dry-run unless `--write` is passed. |
| `utilities/phpkb_cloning/phpkb_clone_replace_related_topics.py` | Mass-edit related-topic sections in `docs/ru/using_the_system`. Converts bold reference links into italic bullet links inside a wrapper div. | Rewrites matching Markdown files in place. |
| `utilities/phpkb_cloning/phpkb_clone_update_article_ids.py` | Prototype/helper for finding KB article IDs in Markdown links and resolving them via the hyperlinks snippet. | Currently runs immediately on hardcoded `article-2198.md`; no `__main__` guard. |
| `utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py` | Update local docs IDs using a clone mapping. Handles `kbId` frontmatter in `docs/ru` and article/category IDs in `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`. | Dry-run by default; rewrites Markdown files only with `--write`. |

## References

- Read `references/workflow.md` before planning or running the annual cloning workflow.
- Read `references/schema-notes.md` before changing what database rows are cloned.

## Workflow

1. Inspect the target script before running or editing it.
   Use `rg` and `Get-Content` to confirm current inputs, hardcoded paths, prompts, and side effects.

2. Treat DB-mutating scripts as high risk.
   `phpkb_clone.py` and `phpkb_clone_update_links.py` connect to PHPKB through `tools.ssh_kb_ru` and can insert or update production-like database records. Do not run them unless the user explicitly asks to execute the DB operation and understands the target.

3. Verify mapping files before link or ID migration.
   Check `.mapping.json` or another explicit mapping file before using `phpkb_clone_update_links.py` or `phpkb_clone_update_mapped_ids.py`.

4. Treat file-rewriting helpers as batch migrations.
   `phpkb_clone_replace_related_topics.py` and `phpkb_clone_update_mapped_ids.py --write` rewrite Markdown files in place. Before running them, check `git status --short`, inspect the search scope, and confirm it matches the requested files.

5. After running or editing any cloning script, verify with Git.
   Use `git status --short` and targeted diffs for local files. For DB scripts, summarize prompts answered, target categories/articles, and any mapping files affected.

## Common Tasks

### Clone PHPKB Content

- Review `utilities/phpkb_cloning/phpkb_clone.py`.
- Confirm whether the task is a whole category tree clone or a specific article clone.
- Confirm the target category ID when cloning individual articles.
- Expect the script to maintain category/article mapping in JSON and insert rows into PHPKB tables.
- Expect cloned articles to receive copied `phpkb_attachments` and `phpkb_custom_data` rows remapped to the new `article_id`; attachment files are not duplicated.

### Update Links After Cloning

- Review `utilities/phpkb_cloning/phpkb_clone_update_links.py`.
- Load the mapping JSON before making changes.
- Expect replacements for article IDs, category IDs, product names, and selected version strings.
- In CLI mode, run dry-run first:
  `python utilities/phpkb_cloning/phpkb_clone_update_links.py --mapping .mapping.json --category-id <id>`
- Use `--write` only after the dry-run output looks correct.
- Product-name replacements are optional via `--replace-product-names`.
- Version replacements are optional and parameterized, for example `--old-version 5.0 --new-version 6.0`.
- No-argument interactive mode preserves the older prompt-driven behavior, including `4.7` to `5.0` prompts.

### Migrate Local KB IDs

- Review `utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py`.
- Confirm the selected mapping JSON contains the intended `Articles` and `Categories` sections.
- Run dry-run first:
  `python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .mapping.json --target all`
- Use `--write` only after the report looks correct.
- `frontmatter-kbids` updates `kbId:` values in Markdown files under `docs/ru` using `Articles`.
- `hyperlink-map` updates only `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`, using `Articles` for `{{ kbArticleURLPrefix }}` IDs and `Categories` for `{{ kbCategoryURLPrefix }}` IDs.

### Clean Related Topics

- Review `utilities/phpkb_cloning/phpkb_clone_replace_related_topics.py`.
- Confirm the hardcoded directory, currently `docs/ru/using_the_system`.
- Expect matching related-topic sections to be wrapped in `<div class="relatedTopics" markdown="block">` and bold links converted to bullet italic links.

### Work With `phpkb_clone_update_article_ids.py`

- Treat it as a prototype unless updated first.
- It runs `process_markdown_file('article-2198.md')` at import time without an `if __name__ == "__main__"` guard.
- Add a proper entry point or parameters before using it for a broader migration.

## Safety Checklist

- Check `git status --short` before local batch rewrites.
- Read the script and confirm hardcoded paths before execution.
- Do not run DB-mutating scripts as a casual verification step.
- Keep edits narrow and preserve existing interactive safeguards unless the user asks for automation.
- For generated or updated Markdown, follow the repository formatting rules in `AGENTS.md`.
