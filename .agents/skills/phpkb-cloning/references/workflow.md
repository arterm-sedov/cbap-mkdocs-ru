# PHPKB Cloning Workflow

Use this workflow for creating a new PHPKB section for a new product release.

## Script Location

Run scripts from the repository root:

- `utilities/phpkb_cloning/phpkb_clone.py`
- `utilities/phpkb_cloning/phpkb_clone_rollback.py`
- `utilities/phpkb_cloning/phpkb_clone_update_links.py`
- `utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py`

## Profile Selection

DB scripts use `tools.ssh_kb_ru.establish_connection_interactive()`.

- `SERVER_PROFILE=cmw` targets `comindware.ru` credentials with the `CMW_` prefix.
- `SERVER_PROFILE=cmwlab` targets `cmwlab.com` credentials with the `CMWLAB_` prefix.

Keep clone and post-clone update scripts on the same profile.

## Recommended Order

1. Set and verify `.env` `SERVER_PROFILE`.
2. Create and verify a complete `phpkbv9` database backup on the PHPKB server.
3. Run `utilities/phpkb_cloning/phpkb_clone.py` to clone the source category tree or selected articles.
   `--mapping` is required on every run.
   **Version migrations:** repo-root tracked files such as `.v7mapping.json` or `.v6.5mapping.json` — durable artifacts like `.v5mapping.json` / `.v6mapping.json`, not under `.scratch/`.
   **One-off clones:** `.scratch/<purpose>_mapping.json` only.
   All cloning scripts require `--mapping`; pass the same `.vNmapping.json` (or explicit `.mapping.json` for local scratch) on clone, link update, ID migration, and rollback.
   Use `--fresh` only when starting a new clone and refusing to continue from an existing mapping file.
   Use `--dry-run` first for a preflight/resume report with no inserts and no mapping writes.
4. Keep the generated mapping JSON; it maps old category/article IDs to new IDs.
5. Verify the completed clone before post-clone rewrites.
   Check mapped category/article counts, confirm there are no unmapped rows in
   the clone ID ranges, and verify mapped article-category relations. Unique
   mapped article rows can be fewer than article-category placements because
   one article can be linked under multiple categories.
6. Run `utilities/phpkb_cloning/phpkb_clone_update_links.py` to rewrite article/category links in cloned PHPKB content.
   Start with dry-run CLI mode, for example:
   `python utilities/phpkb_cloning/phpkb_clone_update_links.py --mapping .v7mapping.json --category-id 900`
   Here `--category-id` is the cloned category tree to update, not the original source category.
   For a version-string rewrite, add `--old-version <source> --new-version <target>`, for example `--old-version 6.0 --new-version 6.5`.
   Add `--replace-product-names` only when legacy product-name replacements are still required.
   Add `--write` only after the dry-run output looks correct.
7. Run local Markdown migration helpers only if the workflow includes local docs updates:
   - `utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .v7mapping.json --target all`
8. Verify local file changes with `git status --short` and targeted diffs.

## Sync Changed Articles (Git-Diff Batch)

Use after editing existing articles in `docs/ru` that already have `kbId:` in front matter.

1. `git status --short docs/ru/` — confirm which source articles changed.
2. `.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml`
3. `git diff --name-only for_kb_import_ru/` — list rebuilt HTML paths.
4. For each path, read `kb-id` from line 1; collect only numeric IDs (omit empty `kb-id=""`).
5. `.\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw -y --article-id <id> …` — one flag per article.
6. Verify script output: `Found content for article <id>` and `Updated article <id>` for each ID.
7. Article URL for reviewers: `https://kb.comindware.ru/article.php?id=<id>`
8. Commit source (and export if tracked) only when requested.

## PHPKB HTML Export And Images

- Build RU PHPKB HTML from the repository root:
  `.\\.venv\\Scripts\\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml`
- On `platform_v6` branch, `mkdocs_for_kb_import_ru.yml` uses
  `site_url: https://kb.comindware.ru/platform/v6.0/` so exported HTML image
  paths point at the V6 web asset folder.
- Rebuild `for_kb_import_ru/` after doc or `kbId` changes.
- Copy exported images into the PHPKB web tree with root-level
  `phpkb_copy_images.py` (`for_kb_import_ru/` →
  `kb.comindware.ru/platform/v6.0`; paths are fixed per branch).

## Publish A New MkDocs Article By Cloning An Adjacent PHPKB Article

Use this workflow when a local Markdown article has no PHPKB article yet and
must be published as a new article. Do not reuse an existing `kbId` unless the
task is explicitly to update that existing PHPKB article.

1. Identify the target PHPKB category and an adjacent source article in that
   category. For example, a new V6 changelog article can be cloned from an
   adjacent changelog article into category `915`.
2. Use a dedicated one-off mapping under `.scratch/`. Do not write one-off article mappings
   into a repo-root per-release migration file such as `.v7mapping.json` or `.v6mapping.json`.
3. Run a dry-run first:

   ``` powershell
   python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .scratch/new_article_mapping.json --fresh --article-id <source-article-id> --target-category-id <target-category-id> --suffix "" --dry-run
   ```

4. If the dry-run scope is correct, run the real clone with the same command and
   no `--dry-run`. Omit `--show`; one-off article clones stay hidden until the
   publish step.
5. Read the new PHPKB article ID from the clone output or from the one-off
   mapping file, for example:

   ``` json
   {
     "Articles": {
       "5435": "5741"
     }
   }
   ```

6. Add the new ID to the local Markdown front matter:

   ``` yaml
   kbId: 5741
   ```

7. If the article has or needs a reusable reference link, add its H1 anchor to
   `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md` with the new `kbId`.
8. Rebuild `for_kb_import_ru/`:

   ``` powershell
   .\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
   ```

9. Publish only the new article:

    ``` powershell
    python phpkb_update_articles.py --profile cmw --article-id <new-article-id> --yes
    ```

    The script can also be run interactively by omitting `--article-id`. When run interactively, answer `Y` to "Update specific articles?", enter the new article ID, confirm the update, then enter `E`.

10. `phpkb_update_articles.py` updates the PHPKB row from the generated HTML
    whose body contains `kb-id="<new-article-id>"`. It updates title, content,
    tags, `unlisted`, `article_status='approved'`, and `article_show='yes'`.
11. (Optional) Refresh RAG and AI ingestion so the new article appears in the LLM bundle:

    ``` powershell
    .\.venv\Scripts\python.exe phpkb_import_for_rag.py --category-id 896
    .\.venv\Scripts\python.exe phpkb_ingest.py
    ```

    Then commit the RAG artifact and the updated bundle in both this repo and the sibling `kb.comindware.ru` repo.

12. Commit the generated `for_kb_import_ru/` HTML alongside the source Markdown —
     this repo tracks `for_kb_import_ru/` under version control. Delete the
     `.scratch/` one-off mapping after publish unless audit is needed.

### Real-world Example: Publishing "Работа с ИИ" (ai_features_guide.md)

1. Identified category `976` (Разработка приложений) as the correct target category.
2. Selected `5643` (Приложения. Определения и настройка) as an adjacent source article in category `976`.
3. Performed dry run with a dedicated mapping file `.scratch/ai_features_guide_mapping.json`:
   ``` powershell
   python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .scratch/ai_features_guide_mapping.json --fresh --article-id 5643 --target-category-id 976 --suffix "" --dry-run
   ```
4. Ran the actual clone to produce the new article ID `5742`:
   ``` powershell
   python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .scratch/ai_features_guide_mapping.json --fresh --article-id 5643 --target-category-id 976 --suffix ""
   ```
5. Updated front matter of `docs/ru/business_apps/ai/ai_features_guide.md` with `kbId: 5742`.
6. Added `[ai_feature_guide]: {{ kbArticleURLPrefix }}5742` to `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`.
7. Rebuilt `for_kb_import_ru/`:
   ``` powershell
   .venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
   ```
8. Published with:
    ``` powershell
    python phpkb_update_articles.py --profile cmw --article-id 5742 --yes
    ```
9. Committed the generated `for_kb_import_ru/` HTML along with source changes and pushed to all remotes.

The root-level `phpkb_replace_related_topics.py` is a post-import Markdown
cleanup helper, not part of the PHPKB DB cloning scripts.
The root-level `phpkb_update_article_ids.py` is also a post-import Markdown
lookup prototype, not part of the PHPKB DB cloning scripts.

## Safety Notes

- Treat `phpkb_clone.py` and `phpkb_clone_update_links.py` as DB-mutating scripts.
- Treat `phpkb_clone_rollback.py --write` as destructive; run it only for a deliberate cleanup of cloned rows.
- Do not run DB-mutating scripts as a test.
- Create and verify a full DB backup before any production clone or rollback run.
- Confirm the selected mapping JSON, for example `.v7mapping.json`, before running link updates.

## Database Backup

When working directly on the PHPKB server over SSH, create a full `phpkbv9`
dump before any production clone or rollback run:

``` bash
sudo mysqldump \
  --default-character-set=utf8mb4 \
  --routines \
  --triggers \
  --events \
  --lock-tables \
  --databases phpkbv9 \
  > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql
```

Use `--lock-tables` because the PHPKB tables use MyISAM in the current schema
notes; `--single-transaction` is not enough for a consistent MyISAM backup.

Verify the backup exists and looks plausible:

``` bash
ls -lh phpkbv9_backup_before_v6_clone_*.sql
head -40 phpkbv9_backup_before_v6_clone_*.sql
```

Expected sanity checks:

- the file is large enough for the current database, for example around `1.5G`;
- the header names `Database: phpkbv9`;
- the dump contains `CREATE DATABASE` and `USE \`phpkbv9\``;
- PHPKB tables such as `phpkb_api_keys` or `phpkb_articles` appear in the dump.

## Rollback

If a clone run must be removed, start with a dry-run report:

``` powershell
python utilities/phpkb_cloning/phpkb_clone_rollback.py --profile cmw --mapping .v7mapping.json
```

Delete cloned rows only after checking the counts:

``` powershell
python utilities/phpkb_cloning/phpkb_clone_rollback.py --profile cmw --mapping .v7mapping.json --write --confirm-delete-cloned-content
```

The rollback deletes only mapped target IDs from the mapping values. It cleans
attachment/custom data rows first, then relations, articles, and categories.

For cleanup after an interrupted clone, do not edit the real clone mapping.
Create a temporary mapping that contains only the unmapped orphan target IDs,
run rollback dry-run against that temporary mapping, then delete the temporary
mapping file after the orphan rows are removed and verified.

## Post-Clone Verification Findings

In the V5 to V6 clone run, source category `798` was cloned adjacent as category
`896`. The final verified mapping contained:

- `84` categories;
- `498` unique article rows;
- `616` article-category relation pairs.

This is expected: some PHPKB articles are linked under more than one category.
Verify relation pairs, not only article counts, before running link rewrites.

Interrupted attempts can leave duplicate rows that are not present in the real
mapping. In that run, orphan rows were isolated into a temporary
`.v6mapping_orphans.json`, dry-run through `phpkb_clone_rollback.py`, removed,
and verified with zero unmapped article/category rows remaining in the clone ID
ranges.

## Clone Visibility Rules

`phpkb_clone.py` uses different defaults for category-tree clones and one-off article clones.

| PHPKB field | Category-tree clone (default) | With `--include-private` |
| --- | --- | --- |
| `category_status='private'` | skipped | included |
| `category_show='no'` | skipped | skipped |
| `article_show='no'` | skipped | skipped |
| `unlisted=1` | included when `article_show='yes'` | same |

- Russian scope: child categories require `language_id = 2`. Articles are selected by
  category relations, not by `phpkb_articles.language_id`.
- `--include-private` affects `--category-id` dry-run and write the same way.
- There is no bulk flag for hidden articles. Clone them with `--article-id` if needed.

### `--show` (article clones only)

`--show` applies only to `--article-id`, not to `--category-id`.

- Without `--show`, a one-off cloned article is inserted with `article_show='no'`. It stays
  out of KB navigation until an editor publishes it.
- With `--show`, the clone is visible immediately (`article_show='yes'`).
- Category-tree clones do not use `--show`. They keep visible articles visible because the
  walk already selects `article_show='yes'` rows and copies the rest of each article row.

Use `--show` when you intentionally clone a draft or hidden source article into a target
category and want it live right away. Omit it for test copies and staged migrations.

## CLI Usage

All cloning scripts require `--mapping`. Interactive category browsing still works when you pass `--mapping` and omit `--category-id` / `--article-id`:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v7mapping.json
python utilities/phpkb_cloning/phpkb_clone_update_links.py --profile cmw --mapping .v7mapping.json
```

Scripted category tree clone:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v7mapping.json --category-id 896 --target-parent-id 1000
```

`--category-id` is the source category tree to clone. `--target-parent-id` is
the destination parent category for the cloned root category. If
`--target-parent-id` is omitted, the cloned root category keeps the source
category's parent ID, so the clone is created adjacent to the source category.

Preflight category tree clone:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v7mapping.json --category-id 896 --target-parent-id 1000 --dry-run
```

Private category subtrees (still skips hidden categories and articles):

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v7mapping.json --category-id 896 --include-private --dry-run
```

Scripted article clone:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --article-id 4578 --target-category-id 900 --suffix _CLONE
```

`--article-id` is the source article to clone. `--target-category-id` is the
category that should receive the cloned article relation. If
`--target-category-id` is omitted, the clone is related to the source article's
first category. Use `--article-id` multiple times to clone several articles
into one target category. Add `--show` only when the cloned article should be
visible immediately.

Use a separate repo-root mapping file when starting a new per-release migration.
For the next release, pick a dedicated tracked name at the repository root such as `.v7mapping.json` or `.v6.5mapping.json`:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v7mapping.json --fresh --category-id 896 --target-parent-id 1000
```
