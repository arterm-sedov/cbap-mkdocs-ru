# PHPKB Cloning Workflow

Use this workflow for the rare task of creating a new PHPKB section for a new product version.

## Script Location

Run scripts from the repository root:

- `utilities/phpkb_cloning/phpkb_clone.py`
- `utilities/phpkb_cloning/phpkb_clone_update_links.py`
- `utilities/phpkb_cloning/phpkb_clone_replace_related_topics.py`
- `utilities/phpkb_cloning/phpkb_clone_update_article_ids.py`
- `utilities/phpkb_cloning/phpkb_clone_update_kbids_to_v5.py`

## Profile Selection

DB scripts use `tools.ssh_kb_ru.establish_connection_interactive()`.

- `SERVER_PROFILE=cmw` targets `comindware.ru` credentials with the `CMW_` prefix.
- `SERVER_PROFILE=cmwlab` targets `cmwlab.com` credentials with the `CMWLAB_` prefix.

Keep clone and post-clone update scripts on the same profile.

## Recommended Order

1. Set and verify `.env` `SERVER_PROFILE`.
2. Run `utilities/phpkb_cloning/phpkb_clone.py` to clone the source category tree or selected articles.
3. Keep the generated `.mapping.json`; it maps old category/article IDs to new IDs.
4. Run `utilities/phpkb_cloning/phpkb_clone_update_links.py` to rewrite article/category links in cloned PHPKB content.
5. Run local Markdown migration helpers only if the workflow includes local docs updates:
   - `utilities/phpkb_cloning/phpkb_clone_update_kbids_to_v5.py`
   - `utilities/phpkb_cloning/phpkb_clone_replace_related_topics.py`
   - `utilities/phpkb_cloning/phpkb_clone_update_article_ids.py`
6. Verify local file changes with `git status --short` and targeted diffs.

## Safety Notes

- Treat `phpkb_clone.py` and `phpkb_clone_update_links.py` as DB-mutating scripts.
- Do not run DB-mutating scripts as a test.
- Confirm `.mapping.json` before running link updates.
- The scripts are interactive and do not currently expose a stable CLI argument interface.
