# Discovery Log

Session discoveries that haven't yet been migrated to durable skills or rules.
Review before starting related work. Move to skills/rules when stable.

## 2026-06-18

- **`--article-map` is required for both `phpkb_import.py` and `phpkb_import_for_rag.py`.** The full-refresh examples in `phpkb-ingestion` skill (lines 127, 134) omit `--article-map`, which would cause the script to error. Always pass `--article-map .article_id_filename_map_v{version}.json`.
- **Import scripts update the article-map file.** After import, new articles get their filename stems added to `.article_id_filename_map_v{version}.json`. This file is git-tracked and should be committed after import.
- **`phpkb_content/` changes must be committed after `phpkb_import.py`.** Unlike `for_kb_import_ru/` which is the MkDocs build output, `phpkb_content/` is written directly by the import script and is git-tracked. Always `git add phpkb_content/` and commit after running the import.
- **Two repos, two commits for the ingestion bundle.** `phpkb_ingest.py` copies the bundle to both the root repo (tracked) and `CMW_KB_REPO_PATH/platform/v5.0/` (KB assets repo). Both are separate git repos — each needs its own `git add + commit + push`.
- **`phpkb_content/` and `phpkb_content_rag/` are generated from PHPKB DB, not from each other.** The RAG import does not read from `phpkb_content/` — it independently connects to PHPKB. One can be regenerated without the other.
- **Multiple git remotes for cbap-mkdocs-ru.** `git push` sends to all configured origins — all must succeed for the push to complete.
- **Full import timeout.** A full category-798 import (606 articles) takes 5-10 minutes. Agent tooling needs timeout ≥600000ms for these scripts.
- **Empty cherry-pick is not harmful.** If a commit's content already exists on the target branch, `git cherry-pick` reports "empty, possibly due to conflict resolution" — `git cherry-pick --skip` discards nothing.
- **Skill docs cherry-pick both ways safely.** `.agents/skills/*.md` and discovery_log.md auto-merge between v5/v6 without version-specific contamination.

## 2026-06-17

- **Cherry-picking between platform_v5 and platform_v6: kbId contamination.** Cherry-picking commits from v6 into v5 brings v6 kbIds into article frontmatter. The `hyperlinks_mkdocs_to_kb_map.md` file also gets v6 anchor→kbId mappings. Always restore `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md` to v5 after cherry-picking, and run a script to restore all `kbId:` values in `docs/ru/**/*.md` to their v5 originals.
- **mkdocs_for_kb_import_ru.yml site_url contamination.** The v6 version has `site_url: https://kb.comindware.ru/platform/v6.0/`. Cherry-picking this into v5 silently changes the output URL structure. Always verify `site_url` matches the target branch version after cherry-picking.
- **toc_depth: 2-3 causes massive HTML churn.** Adding `toc_depth: 2-3` to `mkdocs_for_kb_import_ru.yml` changes the TOC sidebar structure in every generated HTML file (H1–H6 → H2–H3 only). This caused ~66 extra files to show as changed in `for_kb_import_ru/`. Keep v5 defaults unless explicitly required.
- **Commit phpkb_content/ and phpkb_content_rag/ separately from article changes.** The commit `[#6] chore: publish 122 updated articles to PHPKB, refresh phpkb_content and phpkb_content_rag` mixed article HTML changes with RAG bundle regeneration. This creates unnecessary churn when cherry-picking. Keep article content changes and RAG/PHPKB export updates in separate commits.
- **git rebase --onto to drop a contaminated commit.** When a cherry-picked commit contains unwanted contamination (e.g., v6 kbIds), use `git rebase --onto <commit-before-bad> <bad-commit> HEAD` to surgically remove it while preserving later commits.
- **git checkout --theirs for cherry-pick conflicts.** When cherry-picking from v6 to v5 and you want the v6 content for a file, use `git checkout --theirs -- <file>` during conflict resolution. For bulk resolution: `git checkout --theirs -- $(git diff --name-only --diff-filter=U)`.
- **PowerShell `git checkout --theirs` fails with `StandardErrorEncoding` error.** On Windows PowerShell, `git checkout --theirs -- .` or piping file lists to it can fail with `StandardErrorEncoding is only supported when standard error is redirected`. Workaround: `git checkout --theirs -- .` works directly without piping.
- **`git diff --cached` shows staged changes, `git diff` shows unstaged.** After `git add`, use `git diff --cached` to verify what will be committed. After `git reset HEAD`, use `git diff` to see working tree changes.

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

## 2026-06-19

- **SSH key auth setup for repo tunnel scripts.** Each dev generates `id_ed25519_{username}`, copies pubkey to `~/.ssh/authorized_keys` on both `kb.comindware.ru:8223` and `kb.cmwlab.com:22`. Add `IdentityFile` to `~/.ssh/config` (use absolute path — Windows OpenSSH doesn't support `~` in `IdentityFile`). The `ssh_kb_ru.py` `_detect_ssh_keys()` reads `IdentityFile` from SSH config, so config-based key setup works automatically.
- **Python keyring for MySQL passwords.** `ssh_kb_ru.py` uses `keyring` library (service `ssh_kb_ru`, key format `ssh_kb_ru:{profile}:sql_password`). Each user stores their own MySQL password via `keyring.set_password("ssh_kb_ru", "ssh_kb_ru:cmw:sql_password", "their_pw")`. On Windows the backend is `WinVaultKeyring` (Windows Credential Manager).
- **`ssl_disabled` for MySQL is now configurable per `.env`.** Added `CMW_SQL_SSL_DISABLED=true/false` and `CMWLAB_SQL_SSL_DISABLED=true/false`. Default is `false` (SSL on). Users with `mysql_native_password` auth plugin can set `true`. Users with `caching_sha2_password` need SSL (`false` or unset).
- **MariaDB 10.3 `ALTER USER ... IDENTIFIED WITH mysql_native_password` (without `BY`) resets the password.** Use only with `BY 'password'` to preserve control. To change plugin without touching password on MariaDB 10.3, use `UPDATE mysql.user SET plugin='mysql_native_password' WHERE ...` via root/sudo access.
- **`auth_socket` plugin users cannot authenticate through SSH tunnel (TCP).** Must change to `mysql_native_password` with a password.
- **`sudo mysql` requires TTY on both servers.** Workaround: `echo 'password' | sudo -S mysql -e "SQL"` via paramiko `invoke_shell()`.
- **Keychain key format reference:** `ssh_kb_ru:{cmw|cmwlab}:{ssh_password|sql_password}`. Two profiles: `cmw` (comindware.ru) and `cmwlab` (cmwlab.com).
- **`ssh_kb_ru.py` doesn't use system SSH config for paramiko keys by default.** Must pass `key_filename` explicitly or rely on `IdentityFile` from `_parse_ssh_config()` → `_detect_ssh_keys()` flow.
