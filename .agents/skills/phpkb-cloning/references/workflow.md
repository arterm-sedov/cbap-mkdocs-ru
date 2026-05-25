# PHPKB Cloning Workflow

Use this workflow for the rare task of creating a new PHPKB section for a new product version.

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
2. Run `utilities/phpkb_cloning/phpkb_clone.py` to clone the source category tree or selected articles.
   The script resumes from `.mapping.json` by default. Use `--mapping <path>` for a different mapping file.
   Use `--fresh` only when starting a new clone and refusing to continue from an existing mapping file.
   For V5 to V6 migrations, prefer an explicit versioned file such as `.v6mapping.json`.
   Use `--dry-run` first for a preflight/resume report with no inserts and no mapping writes.
3. Keep the generated mapping JSON; it maps old category/article IDs to new IDs.
4. Run `utilities/phpkb_cloning/phpkb_clone_update_links.py` to rewrite article/category links in cloned PHPKB content.
   Start with dry-run CLI mode, for example:
   `python utilities/phpkb_cloning/phpkb_clone_update_links.py --mapping .v6mapping.json --category-id 900`
   For a V5 to V6 text migration, add `--old-version 5.0 --new-version 6.0`.
   Add `--replace-product-names` only when legacy product-name replacements are still required.
   Add `--write` only after the dry-run output looks correct.
5. Run local Markdown migration helpers only if the workflow includes local docs updates:
   - `utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .v6mapping.json --target all`
6. Verify local file changes with `git status --short` and targeted diffs.

The root-level `phpkb_replace_related_topics.py` is a post-import Markdown
cleanup helper, not part of the PHPKB DB cloning scripts.
The root-level `phpkb_update_article_ids.py` is also a post-import Markdown
lookup prototype, not part of the PHPKB DB cloning scripts.

## Safety Notes

- Treat `phpkb_clone.py` and `phpkb_clone_update_links.py` as DB-mutating scripts.
- Treat `phpkb_clone_rollback.py --write` as destructive; run it only for a deliberate cleanup of cloned rows.
- Do not run DB-mutating scripts as a test.
- Confirm the selected mapping JSON, for example `.v6mapping.json`, before running link updates.

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
## CLI Usage

Without arguments, `phpkb_clone.py` keeps the historical interactive flow.

Scripted category tree clone:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --category-id 798 --target-parent-id 1000
```

Preflight category tree clone:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id 798 --target-parent-id 1000 --dry-run
```

Scripted article clone:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --article-id 4578 --target-category-id 900 --suffix _CLONE
```

Use `--article-id` multiple times to clone several articles into one target category. Add `--show` only when the cloned article should be visible immediately.

Use a separate mapping file when testing or preparing a new per-release migration.
For V5 to V6, prefer `.v6mapping.json`:

``` powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --fresh --category-id 798 --target-parent-id 1000
```
