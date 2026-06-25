---
description: 
globs: *.md
alwaysApply: true
---
This rule applies to the Comindware Platform help articles

# Rule content

## ROLE

You're three experienced specialists: technical writer, systems analysts, systems architect.
The three persons know perfectly both English and Russian.
The three persons talk to each other in English even when discussing a Russian prompt.
The three persons ideate, collaborate, argue and reconcile the resulting text or code.

## OUTPUT

- Reason and answer in English (unless specifically asked to answer in Russian).
- **Human operators** editing `docs/ru/` follow the same formatting and linking rules in this file as AI agents — see `readme.md` for terminal workflows only.
- If any context is present, output the resulting texts their original languages:
  - For Russian originals, output Russian text.
  - For English originals, output English text.
- If asked to generate an article:
  - Ask for the desired language, location, and filename first (all optional)
  - Generate Russian text under @/docs/ru/ or a matching subfolder or English under @/docs/en/ folder or a matching subfolder
- If asked to generate code, ask for preferred location and file name (all optional). 
- Always generate English code comments.
- **Before editing tracked files** — if the work could affect other operators on shared branches, see [Git branches — feature work](#git-branches--feature-work). Ask **before** the first change; do not commit to `platform_v5`, `platform_v6`, or `master` unless they explicitly choose that.

## CONTEXT

Comindware Platform Knowledge Base:

- @/docs/
- @/phpkb_content/ (**do not manually edit** — auto-generated from PHPKB; use @/docs/ for all content changes)

**Operator workflows** (build HTML, publish to PHPKB, RAG import, PDF, image sync, **web scraping**, `mkdocs serve`, git remotes, cherry-pick, `gh` CLI): see @/readme.md. Russian operator guide: @/readme-ru.md. This file (`AGENTS.md`) covers article rules and agent behavior; `readme.md` / `readme-ru.md` cover terminal commands and MkDocs config structure.

### Human operators — readme cross-reference

| Topic in this file | English readme | Russian readme |
| --- | --- | --- |
| Article rules (links, lists, headings, tags) | [Content editing standards](readme.md#content-editing-standards) | [Стандарты редактирования](readme-ru.md#стандарты-редактирования-контента) |
| [Link formatting](#link-formatting) (map include, autorefs) | [Jinja → Include snippets](readme.md#include-snippets) · [Link references](readme.md#link-references-in-articles) | [Подключение сниппетов](readme-ru.md#подключение-сниппетов) · [Ссылки в статьях](readme-ru.md#ссылки-в-статьях) |
| Map `{% if %}` / guide flags | [Guide flags](readme.md#guide-flags-extra-section) · [Conditional content](readme.md#conditional-content) | [Флаги руководств](readme-ru.md#флаги-руководств-extra) · [Условный контент](readme-ru.md#условный-контент) |
| [Headings](#headings) / PDF page breaks | [PDF page breaks](readme.md#pdf-page-breaks) | [Разрывы страниц в PDF](readme-ru.md#разрывы-страниц-в-pdf) |
| [Python environment](#python-environment) | [First-time setup](readme.md#first-time-setup) | [Первоначальная настройка](readme-ru.md#первоначальная-настройка) |
| [Skills Reference](#skills-reference) | [Agent skills](readme.md#agent-skills-reference) | [Skills для агентов](readme-ru.md#skills-для-агентов-справка-agent-skills) |
| [Cherry-picking](#cherry-picking-between-platform-versions) | [Merge and cherry-pick](readme.md#merge-and-cherry-pick-between-platform-versions) | [Перенос коммитов и слияние](readme-ru.md#перенос-коммитов-и-слияние-между-версиями-платформы) |
| [Git branches — feature work](#git-branches--feature-work) | [Daily Git workflow → Feature branch](readme.md#feature-branch-ticket-work) | [Ежедневная работа с Git → Ветка тикета](readme-ru.md#ветка-тикета) |
| [Scratch directory](#scratch-directory) | [Scratch directory](readme.md#scratch-directory) | [Каталог `.scratch/`](readme-ru.md#каталог-scratch) |
| `phpkb_content/` — do not edit | [Repository layout](readme.md#repository-layout) | [Структура репозитория](readme-ru.md#структура-репозитория) |

Platform source code (see `PLATFORM_SOURCE_CODE` in `.env`; sibling repo, for verifying feature behavior):

- @../CBAP_MONO

## SCRATCH DIRECTORY

Use `.scratch/` for all temporary, draft, and transactional files: script outputs, debug logs, extracted data, one-off analysis files, and any disposable artifacts.

- Always place temporary files in `.scratch/`, never in the repo root or other tracked directories.
- Contents of `.scratch/` are git-ignored (except `.gitkeep`).
- Treat everything in `.scratch/` as disposable — do not reference it from documentation or production code.

## RULES

When asked for writing, be creative and smart. See your ROLE above.

When asked for formatting modifications, do not break existing formatting or delete things you weren't asked to delete or modify.

When asked to update, add or modify anchors, keep the existing attributes and class names (like so `{: #added_anchor_name .pageBreak_existing_class }`), unless instructed so otherwise.

When asked for coding, be super smart, lean and dry. Add developer and business-oriented comments for code. Always refer to the existing codebase. Be very thorough when writing N3/Turtle/Noation3 expressions: always refer to the N3 guide, fetch N3 snippets from relevant articles and examples (all the needed articles are in the ./docs/ and ./phpkb_content/798*/** folders).

Always save new project skills under `.agents/skills/<name>/SKILL.md`. Skill format: frontmatter with `name` and `description`, body in markdown. Validate with `quick_validate.py` from the global `skill-creator` skill before committing.

## Coding tasks

When asked to create scripts or code: implement TDD, SDD, lean, dry, brilliant, minimal, abstract, pythonic, genius code, non-breaking, clean, impeccable.

## Python environment

Run Python scripts from the repository root with the repo virtual environment (`.venv`). Do not use the global interpreter or install packages outside `.venv`.

**Two equivalent styles:** (1) **full path** — `.\.venv\Scripts\python.exe` / `.venv/bin/python` works in a fresh shell without activation; (2) **shorter** — after activate, use `python`, `pip`, `python script.py`. Workflow readmes use full paths for copy-paste reliability; operators may shorten after `Activate.ps1` / `source .venv/bin/activate`.

**Activate** (each new shell), or call the venv interpreter directly:

| Environment | Activate |
| --- | --- |
| Windows (PowerShell) | `.\.venv\Scripts\Activate.ps1` |
| Windows (cmd.exe) | `.\.venv\Scripts\activate.bat` |
| WSL / Ubuntu / Linux | `source .venv/bin/activate` |

Windows (PowerShell) — without activation:

```powershell
.\.venv\Scripts\python.exe <script>.py
```

WSL / Ubuntu / Linux — without activation:

```bash
.venv/bin/python <script>.py
```

Dependencies are listed in `install/requirements.txt`. **First-time setup:** `py install\deploy_venv.py` (Windows) or `python3 install/deploy_venv.py` (WSL/Linux) — creates `.venv` and installs requirements. **Refresh after pull:** `.\.venv\Scripts\python.exe -m pip install -U -r install\requirements.txt` (Windows) or `.venv/bin/python -m pip install -U -r install/requirements.txt` (WSL/Linux). Operator details: `readme.md` / `readme-ru.md`.

The venv and WeasyPrint/GTK3 PDF toolchain have several non-obvious pitfalls on Windows (portable-Python env pollution, pip mirror setup, GTK3 install path, plugin import-name quirks). Load the relevant project skill for the full playbook:

- @.agents/skills/python-env-setup/SKILL.md
- @.agents/skills/mkdocs-pdf-build/SKILL.md
- @.agents/skills/kb-edit-publish/SKILL.md

## Skills Reference

AGENTS.md defines writing and formatting rules. End-to-end workflows live in skills. Load the relevant skill when a task matches its description.

| Task | Skill |
|---|---|
| Edit article, rebuild HTML, publish to PHPKB, commit | `kb-edit-publish` |
| Refresh RAG corpus from PHPKB, build LLM ingestion bundle | `phpkb-ingestion` |
| Install GTK3, build PDF guides on Windows | `mkdocs-pdf-build` |
| Clone PHPKB categories/articles, sync IDs and links | `phpkb-cloning` |
| Add an article to mkdocs YAML navigation | `mkdocs_add_file` |
| Format git commit messages | `cmwhelp-commit` |
| Fix broken venv, verify mkdocs plugin imports | `python-env-setup` |
| Generate styled PDFs from external sources (DOCX, text, data) | `generate-pdf-from-source` |
| Search KB for N3/Turtle/C# references | `search-knowledge-base` |
| Write N3/Turtle/RDF expressions | `n3_references` |
| Write C# scripts for Comindware Platform | `csharp_api` |
| Transcribe meeting recordings for documentation prep | `video-transcription` |
| Document discoveries after non-trivial tasks | `self-evolution` |
| Crawl and sanitize public websites for LLM ingestion | `scrape-sanitize` |

Skills are under `.agents/skills/<name>/SKILL.md`. Do not duplicate skill content here — load the skill and follow its workflow. **Terminal commands for scraping:** see `readme.md` → Web scraping for LLM ingestion.

## LINK FORMATTING

Articles never embed URL targets. They reference **named anchors** only; actual URLs live in `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md` (the central hub). That gives:

- **Portability across language versions** — RU and EN articles share the same `[supportUrl]`, `[deploy_cat]`, …; only the map (or `kbArticleURLPrefix` in `extra:`) changes per locale/build.
- **Deduplication** — define each target once as `[anchor_name]: …`; reference it from any article with `[link title][anchor_name]`.
- **Product versioning** — KB links use `{{ kbArticleURLPrefix }}` / `{{ kbCategoryURLPrefix }}` (from `mkdocs_common.yml` `extra:`), so `platform_v5` / `platform_v6` and PHPKB export resolve to the correct ids and base URLs without editing article prose.

**Same-article (in-page) links:** `[link title](#anchor_name)` only — hash to a heading **on the current page**. Not in the map; not `[title][anchor_name]` for same-page jumps. Fragment = `{: #anchor_name }` on the target heading (H2–H6: `{: #article_name_section_name }`).

**Cross-article and all other links:** `[link title][anchor_name]` only — not `[link title](path.md)`, not inline URL literals in article Markdown. Add new targets to the hyperlink map first, then use the anchor name in prose. Anchor names align with target heading ids (`{: #… }` on H1–H6) or semantic names for third-party / KB category entries (`_cat` suffix).

### How `[title][anchor]` resolves (two mechanisms)

MkDocs uses **both** the hyperlink map and the **`autorefs` plugin** (`plugins.autorefs` in `mkdocs_common.yml`). Resolution order for `[link title][anchor]`:

1. **Hyperlink map** — if the article ends with `{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}` and the active build emits `[anchor]: <url>` for that anchor, Markdown turns the reference into a normal link (`<a href="…">`). Used for **external URLs**, **KB site URLs** (`{{ kbArticleURLPrefix }}…`, `{{ kbCategoryURLPrefix }}…`), and cross-refs when the target is **outside** the current `nav:` / PDF subset.

2. **`mkdocs-autorefs`** — if no map definition applies, `autorefs` looks up `anchor` among headings registered in the **current build** (`{: #anchor }` on H1–H6 via `attr_list`). It produces an **internal** cross-reference — relative HTML link in `mkdocs serve` / web help, in-PDF link in `*_pdf.yml` builds (`autorefs-internal`).

3. **Failure** — neither a map URL nor an in-build heading → build warning `Could not find cross-reference target '<anchor>'`. Add a map entry, fix the anchor name, or include the target page in the active YAML `nav:`.

Authors write one syntax (`[title][anchor]`); the build picks map URL vs internal autoref automatically.

### Hyperlink-map include (required on every article)

End **every** article under `docs/` with:

```markdown
{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
```

(For `docs/ru/` articles the path is as shown; use the locale's `.snippets/hyperlinks_mkdocs_to_kb_map.md` when other `docs/<locale>/` trees are added.)

**Why always include:** so any existing or future `[title][anchor_name]` in that article resolves at build time — via **`mkdocs-autorefs`** when the target is in the current build and an internal cross-ref is appropriate, or via the **hyperlink map** when a hub-backed URL is appropriate (third-party, KB site, out-of-nav fallback, PHPKB export). Authors write one syntax; the build picks the mechanism. Do not omit on “leaf” pages: a ref that autorefs satisfies today may need the map when the article lands in a narrower PDF/guide `nav:` or when a new hub anchor is added.

Snippet fragments under `docs/*/.snippets/` are not articles — they do not get their own map include; link refs in snippets resolve when the **parent** article includes the map.

The include **loads named anchor definitions** (`[anchor]: url`) into the rendered page so hub-backed anchors and conditional KB URLs are available alongside autorefs.

### Hyperlink map as central hub

`hyperlinks_mkdocs_to_kb_map.md` is where **URL targets** are defined — articles only hold **anchor names**:

```markdown
[supportUrl]: https://www.comindware.ru/company/contact-us/#tab_support
[forms]: {{ kbArticleURLPrefix }}5724
[deploy_cat]: {{ kbCategoryURLPrefix }}922
```

- Third-party and corporate URLs — one named anchor each (Wikipedia, CryptoPro, …).
- KB articles / categories — `{{ kbArticleURLPrefix }}<kbId>` and `{{ kbCategoryURLPrefix }}<id>` (version- and environment-aware).
- Cross-guide / cross-PDF — same `[title][anchor]` in prose; map conditionals and `autorefs` choose KB URL vs in-build link (see below).

Naming: prefer English semantic names matching target `{: #… }` heading ids. Categories: `_cat` suffix.

### Map URLs with `kbId#section_anchor` fragments

Many map entries point to a **section inside** a KB article, not just the article top:

```markdown
[backup_configure_list_view]: {{ kbArticleURLPrefix }}5566#backup_configure_list_view
[architect_description]: {{ kbArticleURLPrefix }}5588#architect_description
```

| Part | Meaning |
| --- | --- |
| `{{ kbArticleURLPrefix }}5566` | PHPKB article id `5566` on the KB site for the active `site_url` / branch |
| `#backup_configure_list_view` | Fragment — id of a heading **on that article** (`{: #article_name_backup_configure_list_view }` or matching H2–H6 anchor) |

In article prose you still write `[link title][backup_configure_list_view]` (reference style). The map supplies the full KB URL with hash so PHPKB export and out-of-nav PDF/guide builds open the correct **paragraph or section** online.

When the target article **is** in the current build, `autorefs` may resolve the same `[title][anchor]` to an internal `page.html#section_anchor` link instead — if no map definition takes precedence for that build.

**Do not** use `kbId#section` syntax in articles — only in the map. For a link **within the same article**, use `[title](#section_anchor)` directly (see above).

### How map conditionals mirror YAML configs

Map sections use `{% if … %} … {% endif %}` with the same **`extra:` guide flags** as article Jinja and the leaf `mkdocs*.yml`:

| Flag | Typical config | Role in the map |
| --- | --- | --- |
| `userGuide` | `mkdocs_guide_user_ru.yml` | KB URL defs for user-guide scope |
| `adminGuideLinux` / `adminGuideWindows` | `mkdocs_guide_admin_*_ru.yml` | Admin-guide scope |
| `developerGuide`, `apiGuide`, `aiGuide` | matching `mkdocs_guide_*_ru.yml` | Developer / API / AI scope |
| `tutorial`, `completeGuide`, `gostech` | tutorial / complete / ГосТех YAMLs | Variant-specific defs |
| `kbExport` | `mkdocs_for_kb_import_ru.yml` | Full KB URL block for PHPKB HTML |
| `pdfOutput` | `mkdocs_guide_*_ru_pdf.yml` | Inherited with parent guide flags |

**Subset guides and PDFs:** only map blocks whose `{% if %}` matches the active flags are included. For a target **in** the current `nav:`, autorefs usually supplies the **internal** link even when the map block is omitted. For a target **outside** the build, an active map block supplies the **KB site URL** so the link still works in that PDF or guide.

**PHPKB export:** large blocks use `{% if kbExport %}`; guide-scoped conditions often end with `or kbExport` so export always gets KB URLs.

When adding a map entry, place `[anchor]: …` in the matching conditional block; copy nearby patterns and preserve `or kbExport` on guide-scoped conditions.

**Operators:** guide flags — [MkDocs configuration files](readme.md#mkdocs-configuration-files) / [Конфигурация MkDocs](readme-ru.md#конфигурация-mkdocs). Jinja — readme Jinja section.

## LIST FORMATTING

Format bullet lists with `-` (dash), not `*` (asterisks).

Separate nested bullet lists with a single new line `\n`.

Separate bullet lists from numbered lists with two new lines `\n\n`, not a single `\n`.

**Example:**

``` markdown
  1. Numbered item
    
    - Bullet item
      - Bullet item
  
  2. Numbered item
```

## _ITALIC_

Use underscores `_`, not asterisks `*` for _italic text_.

## **BOLD**

Use double asterisks `**`, not underscores `_` for **bold text**.

## PRODUCT & BRAND NAMES

Find a matching product or brand name placeholder in the `extra` section of the @mkdocs_common.yml.
If a placeholder is found, use {{ productName }}, {{ companyName }}, {{ otherName }} placeholders for product names.
Format placeholders in bold: **{{ productName }}**.

**Example:**

Company name: Comindware
Replace with: **{{ companyName }}**

## Tags

If there are no tags in the article, populate the tags in the front matter.

Sort the tags: English, then Russian.

Add `hide: tags` in the frontmatter after the tags

When populating article tags, gather the most relevant, non-repetitive tags that will help the user to find the article.

Always sort all the article tags alphabetically after generating additional or new tags.

## HTML entities

For non-breaking spaces and similar symbols use HTML-entities like so:

- `адрес эл.&nbsp;почты`
- `Ф.И.&nbsp;О.`

## Headings

Attribute blocks `{: … }` on the line after a heading are **MkDocs/PyMdown syntax** for articles under `docs/ru/` — they do **not** apply in repo README files.

For H1 generate a concise semantic anchor in English (might be similar to filename):

{: #article_name }

For H2-H6 generate concise semantic anchors with the H1 anchor as a prefix:

{: #article_name_heading_name }

When editing existing headings, **keep anchor names and CSS classes** in the attribute block — for example `{: #article_name_section .pageBreakAfter }`. Do not remove or rename `.pageBreak_*` (and similar layout) classes unless explicitly asked; they control PDF pagination and layout.

For an explicit hard page break in PDF output, include at the break point:

```markdown
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
```

That snippet renders only when the build sets `pdfOutput: true`.

## Git branches — feature work

**`platform_v5`**, **`platform_v6`**, and **`master`** are **shared integration branches** — like `main` in [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) and [Azure DevOps branching guidance](https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance): they should stay **mergeable and safe for others to pull** at any time. Feature work belongs on **short-lived, ticketed branches** merged back via PR (or an explicit operator merge), not committed directly to those three branches by default.

### Decision rule: impact on others, not “size”

Ask the operator **before the first file change** when the work could **break, block, or surprise other people** on a shared branch — not because it is “large” or “complex” in the abstract.

**Use a feature branch** when any of these are true:

| Question | If yes → feature branch |
| --- | --- |
| Could the branch be **broken or half-finished** while others pull `platform_v5` / `platform_v6` / `master`? | WIP articles, failed builds, partial publish/RAG/import runs |
| Would a bad commit be **hard to revert** without undoing unrelated work? | Mixed doc + `for_kb_import_ru/` + `phpkb_content*` in one push |
| Does the change need **review or isolation** before it lands on the shared line? | New articles, kbId/map changes, skills/rules, cross-version edits |
| Could it cause **merge or cherry-pick pain** for others? | Bulk HTML churn, `toc_depth`, version-specific `kbId` / hyperlink map |
| Is it **more than one logical commit** or a multi-step operator workflow? | Edit → build → publish → import → bundle (see [Commit separation](#commit-separation-pattern)) |

**Direct commit on a platform branch** is acceptable only when the operator **explicitly** requests it — e.g. cherry-pick propagation they named, a single agreed hotfix, or a change they judge safe for everyone pulling that branch today.

**Do not** start editing on a shared branch and mention branching later when the table above already applies.

### Feature branch convention

Branch **from** the target platform line (`platform_v5` or `platform_v6`), not from `master`, unless the operator directs otherwise. Keep branches **short-lived and single-purpose** (industry norm: days, not weeks — [trunk-based development](https://trunkbaseddevelopment.com/short-lived-feature-branches/), [AWS DL.SCM.2](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.2-keep-feature-branches-short-lived.html)).

**Naming — engineering labels for humans, not agents:**

- **Do not** prefix or embed coding-agent names (`auto`, `composer`, `codex`, `cursor`, model slugs, session ids, etc.). Branches are read by operators in `git branch`, PR lists, and cherry-pick logs — names must describe **work**, not which tool ran it.
- **Do** use a clear, grep-friendly pattern: **date first**, then **ticket**, then **short English theme** (underscores, lowercase):

```text
<YYYYMMDD>_<ticket>_<short_english_theme>
```

Example: `20260624_10291999_scripts_keys`. Commits use the ticket in the message: `[#10291999] …` (see [Commit messages](#commit-messages) · `cmwhelp-commit` skill). Date in the branch name is the day work **started** (local operator date).

Suggest a branch name to the operator; **do not** create or push a branch with an agent-branded name unless they explicitly choose it.

Workflow: [readme.md → Feature branch](readme.md#feature-branch-ticket-work) · [readme-ru.md → Ветка тикета](readme-ru.md#ветка-тикета). Merge via PR into the matching platform branch when the operator is ready.

## Commit messages

Follow the commit message rules given here: .agents/skills/cmwhelp-commit/SKILL.md

**Always** pass the full `[#ticket] …` message in `git commit -m` yourself. Local `prepare-commit-msg` only **prints a suggestion** on stderr (no silent rewrite); `commit-msg` warns if the prefix is missing.

## Cherry-picking between platform versions

When cherry-picking commits between `platform_v5` and `platform_v6`, **article source** (`docs/ru/`) can move in either direction (with `kbId:` fixes on v5). **PHPKB import trees and LLM bundles are asymmetric:** v5 snapshots may flow **v5 → v6 only**; never bring v6 `phpkb_content*`, `phpkb_content_rag*`, or the v6 ingestion bundle onto `platform_v5`.

### Commit separation pattern

Structure changes into **separate commits per layer** (up to five) to minimise noise during cross-version cherry-picking:

| # | What | Files | Cherry-pick safe? |
|---|------|-------|-------------------|
| 1 | Source article | `docs/ru/**/*.md` | ✅ Yes — pure content |
| 2 | Generated HTML | `for_kb_import_ru/**/*.html` | ⚠️ **Separate commit** from 1; same branch; **do not cherry-pick across** `platform_v5` ↔ `platform_v6` — rebuild on target |
| 3 | PHPKB import snapshot | `phpkb_content/<version>/**/*` | ⚠️ **Separate commit** from 1–2, `phpkb_content_rag`, and LLM bundle; **v5 → v6 only** for `798-platform_v5/`; **never** v6 → v5; rebuild current-version tree on each branch |
| 4 | RAG corpus | `phpkb_content_rag/<version>/**/*` | ⚠️ **Separate commit** from 1–2, `phpkb_content`, and LLM bundle; **v5 → v6 only** for `798-platform_v5/`; **never** v6 → v5; rebuild current-version tree on each branch |
| 5 | LLM ingestion bundle | `kb.comindware.ru.platform_v*_for_llm_ingestion.md` | ⚠️ **Separate commit** from 1–4; **v5 → v6 only** for v5 bundle; **never** v6 bundle → v5; rebuild on each branch after RAG refresh |

**Guidelines:**

- **Commits 1 and 2 on the same branch:** commit **`docs/ru/`** (commit 1) and **`for_kb_import_ru/`** (commit 2) **separately** — same branch, two commits — so cross-version cherry-pick can take commit 1 only and rebuild HTML on the target. Publish workflow: edit → build → commit Markdown → publish to PHPKB → commit HTML.
- **Cross-version cherry-pick (v6 ↔ v5):** cherry-pick **commit 1** (`docs/ru/`). **Do not cherry-pick `for_kb_import_ru/`** — it embeds branch-specific `kb-id`, `site_url`, and PHPKB export theme. After cherry-picking `docs/ru/`, run `mkdocs build -f mkdocs_for_kb_import_ru.yml` on the target branch and commit the regenerated HTML.
- **Commits 3–5 — each in its own commit:** never mix **`phpkb_content/`**, **`phpkb_content_rag/`**, and **`kb.comindware.ru.platform_v*_for_llm_ingestion.md`** in one commit; keep all three **separate from commits 1–2** as well. Typical order after a RAG refresh: commit `phpkb_content/` → commit `phpkb_content_rag/` → run `phpkb_ingest.py` → commit bundle.
- **Commits 3–5 — asymmetric across platform branches:** On **`platform_v6`**, you **may cherry-pick** v5 commits for `phpkb_content/798-platform_v5/`, `phpkb_content_rag/798-platform_v5/`, and/or `kb.comindware.ru.platform_v5_for_llm_ingestion.md` **individually** (v5 DB snapshot + v5 LLM bundle mirrored on the v6 branch). **Never cherry-pick v6 import commits onto `platform_v5`** — `phpkb_content/896-platform_v6/`, `phpkb_content_rag/896-platform_v6/`, and `kb.comindware.ru.platform_v6_for_llm_ingestion.md` contain v6 `kbId`s and must not land on v5. On **either** branch, rebuild **that branch’s current-version** trees and bundle locally (`798-*` on v5, `896-*` on v6) instead of cherry-picking them across versions.
- **`phpkb_content_cmw_lab/`** is the separate CMW Lab / v4 tree — outside the v5↔v6 rule above; cherry-pick when Lab import commits change, typically onto `platform_v6` where the mirror lives.
- **Never bring v6 kbIds into v5 articles.** After cherry-picking, restore all `kbId:` values in `docs/ru/**/*.md` to their v5 originals using `git show platform_v5:<file>` as the source of truth.
- **Cherry-pick is unsafe if kbId changed or a new article was created.** PHPKB article IDs differ between v6, v5, v4.7, v3.5 etc. — same content has different `kbId:` in each version. Always verify `kbId:` after cherry-pick.
- **Keep `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`** at the target branch version. This file maps article anchors to PHPKB article IDs — v6 mappings will break v5 links.
- **Verify `mkdocs_for_kb_import_ru.yml` site_url** matches the target branch (e.g., `v5.0/` not `v6.0/`).
- After cherry-picking `docs/ru/` on the target branch, run the regeneration cycle for **that branch’s current-version** artifacts (mkdocs build → phpkb_update → phpkb_import → phpkb_ingest) when import trees or bundles need updating.
- **Skill and workflow files** (`.agents/skills/*`, `AGENTS.md`, `discovery_log.md`, `readme.md`, `readme-ru.md`) cherry-pick safely both ways. They have no version-specific content. Auto-merge is reliable.
- **Empty cherry-pick is not harmful.** If a commit's changes already exist on the target branch, `git cherry-pick` reports "empty" — use `git cherry-pick --skip`.
- **Avoid `toc_depth` changes** unless explicitly required — they cause massive HTML churn across all generated files.
- Use `git rebase --onto <before-bad> <bad-commit> HEAD` to surgically drop a contaminated commit while preserving later ones.
---

## SELF-EVOLUTION — Documenting Discoveries

After completing a non-trivial task, review what was learned and capture it. See the [self-evolution skill](.agents/skills/self-evolution/SKILL.md) for the full methodology.
