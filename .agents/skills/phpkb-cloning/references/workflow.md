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
   The script resumes from `.mapping.json` by default. Use `--mapping <path>` for a different mapping file.
   Use `--fresh` only when starting a new clone and refusing to continue from an existing mapping file.
   For V5 to V6 migrations, prefer an explicit versioned file such as `.v6mapping.json`.
   Use `--dry-run` first for a preflight/resume report with no inserts and no mapping writes.
4. Keep the generated mapping JSON; it maps old category/article IDs to new IDs.
5. Verify the completed clone before post-clone rewrites.
   Check mapped category/article counts, confirm there are no unmapped rows in
   the clone ID ranges, and verify mapped article-category relations. Unique
   mapped article rows can be fewer than article-category placements because
   one article can be linked under multiple categories.
6. Run `utilities/phpkb_cloning/phpkb_clone_update_links.py` to rewrite article/category links in cloned PHPKB content.
   Start with dry-run CLI mode, for example:
   `python utilities/phpkb_cloning/phpkb_clone_update_links.py --mapping .v6mapping.json --category-id 900`
   Here `--category-id` is the cloned category tree to update, not the original source category.
   For a V5 to V6 text migration, add `--old-version 5.0 --new-version 6.0`.
   Add `--replace-product-names` only when legacy product-name replacements are still required.
   Add `--write` only after the dry-run output looks correct.
7. Run local Markdown migration helpers only if the workflow includes local docs updates:
   - `utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .v6mapping.json --target all`
8. Verify local file changes with `git status --short` and targeted diffs.

The root-level `phpkb_replace_related_topics.py` is a post-import Markdown
cleanup helper, not part of the PHPKB DB cloning scripts.
The root-level `phpkb_update_article_ids.py` is also a post-import Markdown
lookup prototype, not part of the PHPKB DB cloning scripts.

## Safety Notes

- Treat `phpkb_clone.py` and `phpkb_clone_update_links.py` as DB-mutating scripts.
- Treat `phpkb_clone_rollback.py --write` as destructive; run it only for a deliberate cleanup of cloned rows.
- Do not run DB-mutating scripts as a test.
- Create and verify a full DB backup before any production clone or rollback run.
- Confirm the selected mapping JSON, for example `.v6mapping.json`, before running link updates.

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
python utilities/phpkb_cloning/phpkb_clone_rollback.py --profile cmw --mapping .v6mapping.json
```

Delete cloned rows only after checking the counts:

``` powershell
python utilities/phpkb_cloning/phpkb_clone_rollback.py --profile cmw --mapping .v6mapping.json --write --confirm-delete-cloned-content
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

Without arguments, `phpkb_clone.py` keeps the historical interactive flow.

Scripted category tree clone:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --category-id 798 --target-parent-id 1000
```

`--category-id` is the source category tree to clone. `--target-parent-id` is
the destination parent category for the cloned root category. If
`--target-parent-id` is omitted, the cloned root category keeps the source
category's parent ID, so the clone is created adjacent to the source category.

Preflight category tree clone:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id 798 --target-parent-id 1000 --dry-run
```

Private category subtrees (still skips hidden categories and articles):

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id 798 --include-private --dry-run
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

Use a separate mapping file when testing or preparing a new per-release migration.
For V5 to V6, prefer `.v6mapping.json`:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --fresh --category-id 798 --target-parent-id 1000
```
