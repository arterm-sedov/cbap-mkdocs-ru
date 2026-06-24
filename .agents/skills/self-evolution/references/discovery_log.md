# Discovery Log

Session discoveries that haven't yet been migrated to durable skills or rules.

**Order: newest first** — agents read from the top; put today's `## YYYY-MM-DD` block directly below this intro (one heading per day). Review before starting related work. Move stable items to skills/rules and prune absorbed entries.

<<<<<<< HEAD
=======
## 2026-06-22

- **Standalone PDF generation from external documents.** Created `generate-pdf-from-source` skill for converting DOCX/text into Comindware-styled PDFs outside the docs/ru tree. Target folder structure: `build.ps1` + `mkdocs.yml` + `docs/` (markdown + img) + `.site/` (build output) + output PDF. YAML uses `INHERIT: !ENV [MKDOCS_COMMON, <relative_fallback>]` with env vars set by build script. `docs_dir` and `site_dir` must be siblings (not parent-child). `output_path` in `with-pdf` is relative to `site_dir`; use `../` to place PDF in folder root. `exclude_docs: | *.md !<article>.md` builds only the target article.
- **Image auto-figcaption via italic wrapping.** `_![alt](path)_` triggers `mkdocs-em-img2fig-plugin` to generate `<figure>` + `<figcaption>` from alt text. No manual `*Рис. N.*` lines needed.
- **DOCX conversion with python-docx.** Images extracted via `rel.target_part.blob` to `docs/img/`. List paragraphs have `style.name == "List Paragraph"`. Headings detected by bold + font size ≥ 14pt. Runs preserve bold/italic/underline via `run.font` properties.
- **`kbId:` lookup for grep/grouping only** — not article link syntax. Frontmatter `kbId:` maps to PHPKB article id; use grep to find articles and group by category. Article links use named anchors per `AGENTS.md` → Link formatting.
- **Build script path navigation.** `$reposRoot = $scriptDir; for ($i=0; $i -lt N; $i++) { $reposRoot = $reposRoot.Parent }; $cbapRoot = Join-Path $reposRoot.FullName "Documents\cbap-mkdocs-ru"`. Loop count depends on folder depth relative to user's home.
- **UTF-8 for mkdocs on Windows.** Must set `$env:PYTHONIOENCODING="utf-8"` and `$env:PYTHONUTF8="1"` (User-level env vars + PowerShell profile). Without this, colorama crashes on Unicode box-drawing characters in mkdocs-material output.
- **`git config core.longpaths true`** required globally on Windows for repos with long Russian filenames in paths (phpkb_content/, phpkb_content_rag/).

>>>>>>> 74c982cfe ([#6] Restructure discovery log and expand self-evolution skill)
## 2026-06-20

- **Generic/infra commits without a customer ticket default to `#6` (v6) or `#5` (v5).** The `cmwhelp-commit` skill already handles this via branch name fallback, but the convention should be explicit: non-feature, repo-level tasks (tooling, CI, formatting, refactoring) use the version number as ticket reference. Always ask the user for the session ticket number first — only fall back to `#6`/`#5` when the user confirms there is no customer ticket.
- **`platform_v6` branch hosts `phpkb_content_rag/` for ALL versions — consumed by RAG engine.** The RAG ingestion pipeline fetches the corpus from the `platform_v6` branch. Both v5 (`798-platform_v5`) and v6 (`896-platform_v6`) category folders live there. Other repos pull RAG corpora from this branch. This is why v5 phpkb_content/phpkb_content_rag/ingestion bundle changes are cherry-picked to v6 — they must be available at a single source of truth.

## 2026-06-19

- **SSH key auth setup for repo tunnel scripts.** Each dev generates `id_ed25519_{username}`, copies pubkey to `~/.ssh/authorized_keys` on both `kb.comindware.ru:8223` and `kb.cmwlab.com:22`. Add `IdentityFile` to `~/.ssh/config` (use absolute path — Windows OpenSSH doesn't support `~` in `IdentityFile`). The `ssh_kb_ru.py` `_detect_ssh_keys()` reads `IdentityFile` from SSH config, so config-based key setup works automatically.
- **Python keyring for MySQL passwords.** `ssh_kb_ru.py` uses `keyring` library (service `ssh_kb_ru`, key format `ssh_kb_ru:{profile}:sql_password`). Each user stores their own MySQL password via `keyring.set_password("ssh_kb_ru", "ssh_kb_ru:cmw:sql_password", "their_pw")`. On Windows the backend is `WinVaultKeyring` (Windows Credential Manager).
- **`ssl_disabled` for MySQL is now configurable per `.env`.** Added `CMW_SQL_SSL_DISABLED=true/false` and `CMWLAB_SQL_SSL_DISABLED=true/false`. Default is `false` (SSL on). Users with `mysql_native_password` auth plugin can set `true`. Users with `caching_sha2_password` need SSL (`false` or unset).
- **MariaDB 10.3 `ALTER USER ... IDENTIFIED WITH mysql_native_password` (without `BY`) resets the password.** Use only with `BY 'password'` to preserve control. To change plugin without touching password on MariaDB 10.3, use `UPDATE mysql.user SET plugin='mysql_native_password' WHERE ...` via root/sudo access.
- **`auth_socket` plugin users cannot authenticate through SSH tunnel (TCP).** Must change to `mysql_native_password` with a password.
- **`sudo mysql` requires TTY on both servers.** Workaround: `echo 'password' | sudo -S mysql -e "SQL"` via paramiko `invoke_shell()`.
- **Keychain key format reference:** `ssh_kb_ru:{cmw|cmwlab}:{ssh_password|sql_password}`. Two profiles: `cmw` (comindware.ru) and `cmwlab` (cmwlab.com).
- **`ssh_kb_ru.py` doesn't use system SSH config for paramiko keys by default.** Must pass `key_filename` explicitly or rely on `IdentityFile` from `_parse_ssh_config()` → `_detect_ssh_keys()` flow.
- **Bold and italic markers go OUTSIDE hyperlinks, not inside.** `**[text][anchor]**` not `[**text**][anchor]`. Same for guillemets: `**«text»**` not `«**text**»` — bold wraps the guillemets.
- **C# classes and methods imported from PHPKB may have translit identifiers** (`Parametr`→`Parameter`, `tekst`→`text`, `begaemvAD`→`QueryAD`). These require manual verification of each reference in the code block — no cascading cross-file impact since code blocks are self-contained.
- **C# code blocks use 4-space indentation consistently.** Imported blocks may have `\xa0` (nbsp) or mixed tabs. Normalize to spaces.
- **Russian comments in C# code blocks are intentional** — the audience is Russian-speaking developers. Comments should be in legible Russian, not pseudo-English translit (`серчер`→`поисковый запрос`, `проперти`→`атрибуты`).
- **`***bold-italic***` is not used in the codebase.** SQL keywords get `` `backticks` ``, key terms get `**bold**`, standalone section headers get `## H2 {: #anchor }`.
- **Heading numbering (`1.`, `1.1.`, etc.) is removed from all headings.** Numbers are not used in H1-H6 text; semantic numbering is implied by the heading level hierarchy.
- **Anchors are always lowercase, underscore-separated, English-only.** No Cyrillic in anchors. Run-on CamelCase (`templatesystemname`) is split with underscores (`template_system_name`).
- **Opening code fence is labeled with language** (` ```cs `, ` ```sql `, ` ```turtle `). Unlabeled fence is a bug. ` ```text ` is not used — bare fences suffice for URL examples.
- **`hide: tags` has two forms in frontmatter:** simple `hide: tags` or list `hide:\n  - tags`. Only one should exist. Never add the simple form if the list form is already present.
- **Cherry-picking YAML nav commits between version branches overwrites version-specific entries** (release notes filenames, v6-only sections like AI). After accepting formatting changes, manually restore v5 release-note paths and drop v6-only nav blocks. Hyperlinks map `kbId` entries are branch-specific — see `AGENTS.md` → Cherry-picking.

## 2026-06-18

- **Import scripts update the article-map file.** After import, new articles get their filename stems added to `.article_id_filename_map_v{version}.json`. This file is git-tracked and should be committed after import.
- **`phpkb_content/` changes must be committed after `phpkb_import.py`.** Unlike `for_kb_import_ru/` which is the MkDocs build output, `phpkb_content/` is written directly by the import script and is git-tracked. Always `git add phpkb_content/` and commit after running the import.
- **Two repos, two commits for the ingestion bundle.** `phpkb_ingest.py` copies the bundle to both the root repo (tracked) and `CMW_KB_REPO_PATH/platform/v5.0/` (KB assets repo). Both are separate git repos — each needs its own `git add + commit + push`.
- **`phpkb_content/` and `phpkb_content_rag/` are generated from PHPKB DB, not from each other.** The RAG import does not read from `phpkb_content/` — it independently connects to PHPKB. One can be regenerated without the other.
- **Multiple git remotes for cbap-mkdocs-ru.** `git push` sends to all configured origins — all must succeed for the push to complete.
- **Full import timeout.** A full category-798 import (606 articles) takes 5-10 minutes. Agent tooling needs timeout ≥600000ms for these scripts.

## 2026-06-17

- **PowerShell `git checkout --theirs` during cherry-pick:** use `git checkout --theirs -- <file>` directly on the path — do not pipe file lists from `git diff`, which can trigger `StandardErrorEncoding` errors on Windows PowerShell.
- **`git diff --cached` shows staged changes, `git diff` shows unstaged.** After `git add`, use `git diff --cached` to verify what will be committed. After `git reset HEAD`, use `git diff` to see working tree changes.
- **Zero git churn in `phpkb_content_rag/` after an import** means the source articles are already current — that's a good control.

## 2026-06-15

- `Comindware.Entities entities` parameter is deprecated and removed from the platform C# API. All KB C# code examples must strip it from method signatures and body. Three pattern variants in signatures: (A) `, Comindware.Entities entities` as trailing parameter, (B) standalone `Comindware.Entities entities // ...` description lines, (C) `[Comindware.Entities entities]` optional-bracket syntax. Body usages like `entities.ApplicationStatus.Where(...)` need separate handling — the replacement API depends on context. Script at `utilities/remove_entities_param.py` automates signatures; body cleanup is manual.
- PHPKB-imported articles (KBID-prefixed filenames like `5000-*.md`) are raw imports missing H1 anchors, language-tagged code blocks (` ```cs `), and frontmatter tags. Format them to match non-KBID articles. Bold pseudo-headings like `**Section Title**` should be promoted to `## Section Title {: #anchor }`.
- When applying the same logical changes across diverged branches (v5, v6), prefer running transformation scripts directly on each branch's files. Cherry-picking creates merge conflicts on every file because both branches receive identical diffs against different bases.

## 2026-06-09

- PHPKB examples category ID is `909` (used as `--target-category-id` when cloning new example articles). End-to-end publication sequence: clone → kbId in frontmatter → hyperlink map entry → `mkdocs build -f mkdocs_for_kb_import_ru.yml` → `phpkb_update_articles.py` → `phpkb_import_for_rag.py` → `phpkb_ingest.py` → commit+push sibling repo.
- `{{ product Name }}` with a space silently causes a macros syntax error. Only `{{ productName }}` and `{{ companyName }}` are valid macros from `mkdocs_common.yml`.
- **`[text][anchor]` resolution:** `mkdocs-autorefs` for in-build headings; hyperlink map for hub-backed URLs and out-of-nav targets. Warning `Could not find cross-reference target` means neither applied — fix anchor name, add map entry, or include target in `nav:`. Full rules: `AGENTS.md` → Link formatting.
- Process-task scripts use `void Main(ScriptContext)` — no return value. Button scripts use `UserCommandResult Main(UserCommandContext)`. Scenario scripts use `string Main(string ObjectID)`. Match the script type to the automation context: process tasks for unattended data import/sync. **`Comindware.Entities entities` is removed from the API** — see 2026-06-15 entry.
- `for_kb_import_ru/` is tracked in this repo — commit generated HTML exports alongside source changes, do not discard them.
