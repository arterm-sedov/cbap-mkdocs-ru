---
name: phpkb-cloning
description: "Use when working on the PHPKB cloning and post-clone migration workflow in this repository: creating a new PHPKB section for a new product version, publishing a new MkDocs article by cloning an adjacent PHPKB article, syncing changed for_kb_import_ru HTML back to PHPKB by kb-id (git diff batch), cloning PHPKB categories or articles, updating cloned PHPKB article/category links, migrating local docs IDs with clone mappings, fixing related topics after cloning, or analyzing/updating scripts in utilities/phpkb_cloning."
---

# PHPKB Cloning

Use this skill to work safely with the repository scripts that clone PHPKB content, publish new MkDocs articles into PHPKB, and clean up cloned IDs, links, and related-topic markup.

Scripts live in `utilities/phpkb_cloning/`. Run them from the repository root unless the script says otherwise. Skill references live beside this file under `.agents/skills/phpkb-cloning/references/`; resolve `references/workflow.md` and `references/schema-notes.md` relative to the skill folder, not relative to `utilities/phpkb_cloning/`.

## Script Roster

| Script | Purpose | Main side effects |
| --- | --- | --- |
| `utilities/phpkb_cloning/phpkb_clone.py` | Clone PHPKB categories and articles inside the database. Can clone whole category trees or individual articles. | Inserts new DB rows; maintains article/category mapping; clones article attachment and custom data backrefs. |
| `utilities/phpkb_cloning/phpkb_clone_rollback.py` | Delete cloned PHPKB rows using the mapped target IDs from a clone mapping JSON. | Dry-run by default; deletes DB rows only with `--write --confirm-delete-cloned-content`. |
| `utilities/phpkb_cloning/phpkb_clone_update_links.py` | Update PHPKB article/category links after cloning or migration using mapping JSON. Optional product/version replacements can be enabled explicitly. | Connects to DB; CLI mode is dry-run unless `--write` is passed. |
| `utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py` | Update local docs IDs using a clone mapping. Handles `kbId` frontmatter in `docs/ru` and article/category IDs in `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`. | Dry-run by default; rewrites Markdown files only with `--write`. |
| `phpkb_update_articles.py` | Publish rebuilt MkDocs HTML from `for_kb_import_ru` into existing PHPKB article rows by `kbId`. | Connects to DB; supports interactive menus or CLI flags `--profile`, `--article-id`, `--category-id`, and `--yes` for automated syncs. |

## References

- Read `references/workflow.md` before planning or running the per-release cloning workflow.
- Read `references/schema-notes.md` before changing what database rows are cloned.

## Workflow

1. Inspect the target script before running or editing it.
   Use `rg` and `Get-Content` to confirm current inputs, hardcoded paths, prompts, and side effects.

2. Treat DB-mutating scripts as high risk.
   `phpkb_clone.py` and `phpkb_clone_update_links.py` connect to PHPKB through `tools.ssh_kb_ru` and can insert or update production-like database records. Do not run them unless the user explicitly asks to execute the DB operation and understands the target.

3. Verify mapping files before link or ID migration.
   Check `.mapping.json` or another explicit mapping file before using `phpkb_clone_update_links.py` or `phpkb_clone_update_mapped_ids.py`.

4. Treat file-rewriting helpers as batch migrations.
   `phpkb_clone_update_mapped_ids.py --write` rewrites Markdown files in place. Before running it, check `git status --short`, inspect the search scope, and confirm it matches the requested files.

5. After running or editing any cloning script, verify with Git.
   Use `git status --short` and targeted diffs for local files. For DB scripts, summarize prompts answered, target categories/articles, and any mapping files affected.

## Common Tasks

### Clone PHPKB Content

- Review `utilities/phpkb_cloning/phpkb_clone.py`.
- Confirm whether the task is a whole category tree clone or a specific article clone.
- For category tree clones, `--category-id` is the source category to clone.
- For category tree clones, `--target-parent-id` is the destination parent category for the cloned root category.
- If `--target-parent-id` is omitted, the cloned root category uses the source category's parent, so it is created adjacent to the source category.
- Confirm the target category ID when cloning individual articles.
- Use `--dry-run` first for scripted clones to get a preflight scope report without inserts or mapping writes.
- Expect the script to load an existing mapping JSON and resume by default.
- For V5 to V6 migrations, prefer `--mapping .v6mapping.json` and pass that same file to post-clone update scripts.
- Use `--fresh` only when starting a new clone and refusing to reuse an existing mapping file.
- Expect the script to maintain category/article mapping in JSON and insert rows into PHPKB tables.
- Expect newly generated article/category IDs to be read from `cursor.lastrowid`, not from global `MAX(...)` queries.
- Expect mapping saves to be compact progress lines, not full JSON dumps, during long production runs.
- Expect cloned articles to receive copied `phpkb_attachments` and `phpkb_custom_data` rows remapped to the new `article_id`; attachment files are not duplicated.
- Treat clone dry-run as a preflight/resume report. It cannot predict final new IDs because those are generated only by real inserts.
- After a real clone, verify both unique mapped articles and article-category relations. A source tree can contain fewer unique article rows than article-category placements because one article can be linked under multiple categories.
- Category-tree clones walk Russian child categories (`language_id=2`) that are visible (`category_show='yes'`) and public (`category_status='public'`) unless `--include-private` is set. Hidden categories and `article_show='no'` articles are never bulk-cloned.
- PHPKB `unlisted` is copied with the article row and is not a clone filter. MkDocs `unlisted: true` in `docs/ru` is pushed to PHPKB only through root-level `phpkb_update_articles.py` and export HTML `kb-unlisted="1"`.
- `--show` is only for `--article-id` clones. Without it, one-off clones default to `article_show='no'` so they stay hidden until reviewed.

### Publish A New MkDocs Article To PHPKB

- Use this when a local Markdown article has no `kbId` and must become a new PHPKB article, not an update of an existing article.
- Pick an adjacent source PHPKB article in the same target category and clone it with `phpkb_clone.py --article-id`.
- Use a dedicated one-off mapping file, for example `.release_notes_6_new_article_mapping.json`, not `.v6mapping.json`, so the release migration mapping stays clean.
- Always run the clone dry-run first:
  `python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping <one-off-mapping>.json --fresh --article-id <source-article-id> --target-category-id <target-category-id> --suffix "" --dry-run`
- Run the real clone with the same arguments and no `--dry-run`; omit `--show` so the placeholder stays hidden until `phpkb_update_articles.py` publishes it.
- Read the new article ID from the clone output or from `mapping["Articles"][source_article_id]`.
- Add `kbId: <new-article-id>` to the local Markdown front matter.
- If the article has or needs a reusable reference link, add its H1 anchor to `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md` with the new `kbId`.
- Rebuild the PHPKB HTML export with the repo virtual environment:
  `.\\.venv\\Scripts\\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml`
- Publish only the new article using the script's command-line flags:
  `python phpkb_update_articles.py --profile cmw --article-id <new-article-id> --yes`
- The script can also be run interactively by omitting `--article-id`. It reads `for_kb_import_ru`, finds `<div ... kb-id="<new-article-id>" ...>`, and updates the PHPKB row with the MkDocs title, HTML content, tags, `unlisted`, `article_status='approved'`, and `article_show='yes'`.
- After the new ID is written to the Markdown front matter, reusable hyperlink-map entries point to the new `{{ kbArticleURLPrefix }}` URL, and the article is successfully published, delete one-off mapping files such as `.release_notes_6_new_article_mapping.json` unless the user asks to keep them for audit. Keep durable migration mappings such as `.v6mapping.json`.
- If several sibling articles are cloned from the same source article, use a separate one-off mapping file for each new target article. A mapping stores one source-to-target article pair, so reusing it for siblings would resume the first clone instead of creating another article.
- In this repository, keep the generated `for_kb_import_ru` HTML for new and updated articles under version control. Clean generated export files only when they are accidental, unrelated to the requested publish scope, or the user explicitly asks not to keep them.

### Sync Changed Articles To PHPKB (Git-Diff Batch)

Use this when `docs/ru` Markdown was edited and existing PHPKB articles must be refreshed from the rebuilt HTML export—not when creating a new article (use **Publish A New MkDocs Article To PHPKB** above).

1. Rebuild the export tree:

   ```powershell
   .\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
   ```

2. List changed HTML files (scope to the export folder or a subtree):

   ```powershell
   git diff --name-only for_kb_import_ru/
   git status --short for_kb_import_ru/
   ```

3. Read `kb-id` from the first line of each changed `.html` file (`<div class="md-body" … kb-id="…" …>`). Skip files with `kb-id=""`—they have no PHPKB row yet; set `kbId:` in the source `.md` (or clone first) before publishing.

   ```powershell
   Select-String -Path for_kb_import_ru\administration\deploy\script_keys.html -Pattern 'kb-id="(\d+)"' | ForEach-Object { $_.Matches.Groups[1].Value }
   ```

4. Publish all numeric IDs in one non-interactive run (repeat `--article-id` per article):

   ```powershell
   .\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw -y `
     --article-id 5451 --article-id 5558
   ```

   The script matches `for_kb_import_ru/**` by `kb-id`, then updates PHPKB `article_title`, `article_content`, `article_keywords` (from `kb-tags`, max 250 chars), and `unlisted` (from `kb-unlisted="1"` when present).

5. Share direct article links: `https://kb.comindware.ru/article.php?id=<kb-id>` (same as `{{ kbArticleURLPrefix }}` in `mkdocs_ru.yml`).

6. Optional Git commit for the source docs and/or export (only when the user asks to commit): stage `docs/ru/…` and, if you keep the export in the repo, the matching `for_kb_import_ru/…` paths.

### Copy PHPKB Image Assets

- `phpkb_copy_images.py` copies every image from `for_kb_import_ru` to `kb.comindware.ru/platform/v6.0` with overwrite enabled; it is a broad asset sync, not an article-scoped helper.
- In the MkDocs repo, `kb.comindware.ru/platform/v5.0` and `kb.comindware.ru/platform/v6.0` should point at the matching version folders in the external PHPKB asset repo. Verify `Get-Item ... | Format-List LinkType,Target` before copying images.
- After copying images, inspect and commit from the external PHPKB repo root, not from the MkDocs repo. Scope staging to the intended version folder, for example `git add -- platform/v6.0`.
- If only one article's images should be published, do not run the broad copy script blindly; copy or stage only the exact image paths referenced by the generated article HTML.
- Before committing, confirm there are no accidental `platform/v5.0` changes with `git status --short -- platform/v5.0` and `git diff --name-status -- platform/v5.0`.

See `references/workflow.md` → **Sync changed articles (git-diff batch)** for the full checklist.

### Verify A Completed Clone

- Confirm the mapping counts: categories, articles, and source root mapping.
- Confirm every mapped target category/article exists in PHPKB.
- Confirm there are no unmapped rows in the new clone ID ranges. If interrupted attempts left duplicate rows outside the real mapping, put only those target IDs into a temporary orphan mapping and dry-run `phpkb_clone_rollback.py`.
- Confirm article-category placement preservation by comparing source `(article_id, category_id)` pairs mapped through `.v6mapping.json` against actual target `phpkb_relations`.
- For the V5 to V6 run, source category `798` cloned adjacent as category `896`; the verified clone had `84` mapped categories, `498` unique mapped articles, and `616` mapped article-category relations.

### Update Links After Cloning

- Review `utilities/phpkb_cloning/phpkb_clone_update_links.py`.
- Load the mapping JSON before making changes.
- `--category-id` is the cloned category tree whose article links should be updated.
- `--article-id` can be repeated to update selected cloned articles.
- Expect replacements for article IDs, category IDs, product names, and selected version strings.
- In CLI mode, run dry-run first:
  `python utilities/phpkb_cloning/phpkb_clone_update_links.py --mapping .v6mapping.json --category-id <cloned-category-id>`
- Use `--write` only after the dry-run output looks correct.
- Product-name replacements are optional via `--replace-product-names`.
- Version replacements are optional and parameterized, for example `--old-version 5.0 --new-version 6.0`.
- No-argument interactive mode preserves the older prompt-driven behavior, including `4.7` to `5.0` prompts.

### Roll Back A Bad Clone

- Review `utilities/phpkb_cloning/phpkb_clone_rollback.py`.
- Confirm the selected mapping JSON contains only the clone run that should be removed.
- The script deletes only mapped target IDs, that is, mapping values, never source IDs from mapping keys.
- Run dry-run first:
  `python utilities/phpkb_cloning/phpkb_clone_rollback.py --mapping .v6mapping.json`
- Use `--write --confirm-delete-cloned-content` only after the reported counts match the intended rollback.
- Expect deletes in dependency order: attachment/custom data rows, relations, articles, then categories.
- For aborted-run orphan cleanup, use a separate temporary mapping that contains only orphan target IDs. Delete that temporary mapping after cleanup and verification.

### Migrate Local KB IDs

- Review `utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py`.
- Confirm the selected mapping JSON contains the intended `Articles` and `Categories` sections.
- Run dry-run first:
  `python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .v6mapping.json --target all`
- Use `--write` only after the report looks correct.
- `frontmatter-kbids` updates `kbId:` values in Markdown files under `docs/ru` using `Articles`.
- `hyperlink-map` updates only `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`, using `Articles` for `{{ kbArticleURLPrefix }}` IDs and `Categories` for `{{ kbCategoryURLPrefix }}` IDs.

### Clean Related Topics

- Use root-level `phpkb_replace_related_topics.py` for post-import Markdown cleanup, not for DB cloning.
- Confirm the hardcoded directory, currently `docs/ru/using_the_system`.
- Expect matching related-topic sections to be wrapped in `<div class="relatedTopics" markdown="block">` and bold links converted to bullet italic links.

### Work With Article ID Lookup

- Use root-level `phpkb_update_article_ids.py` as a post-import Markdown lookup prototype, not for DB cloning.
- It runs `process_markdown_file('article-2198.md')` at import time without an `if __name__ == "__main__"` guard.
- Add a proper entry point or parameters before using it for real cleanup.

## Safety Checklist

- Check `git status --short` before local batch rewrites.
- Read the script and confirm hardcoded paths before execution.
- Before production clone or rollback runs, create and verify a full `phpkbv9` DB backup as described in `references/workflow.md`.
- Do not run DB-mutating scripts as a casual verification step.
- Keep edits narrow and preserve existing interactive safeguards unless the user asks for automation.
- For generated or updated Markdown, follow the repository formatting rules in `AGENTS.md`.
