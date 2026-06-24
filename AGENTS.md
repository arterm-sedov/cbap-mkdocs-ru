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

- Reason and answer in English (uless specifically asked to answer in Russian).
- **Human operators** editing `docs/ru/` follow the same formatting and linking rules in this file as AI agents — see `readme.md` for terminal workflows only.
- If any context is present, output the resulting texts their original languages:
  - For Russian originals, output Russian text.
  - For English originals, output English text.
- If asked to generate an article:
  - Ask for the desired language, location, and filename first (all optional)
  - Generate Russian text under @/docs/ru/ or a matching subfolder or English under @/docs/en/ folder or a matching subfolder
- If asked to generate code, ask for preferred location and file name (all optional). 
- Always generate English code comments.

## CONTEXT

Comindware Platform Knowledge Base:

- @/docs/
- @/phpkb_content/ (**do not manually edit** — auto-generated from PHPKB; use @/docs/ for all content changes)

**Operator workflows** (build HTML, publish to PHPKB, RAG import, PDF, image sync, **web scraping**, `mkdocs serve`, git remotes, cherry-pick, `gh` CLI): see @/readme.md. Russian operator guide: @/readme-ru.md. This file (`AGENTS.md`) covers article rules and agent behavior; `readme.md` / `readme-ru.md` cover terminal commands and MkDocs config structure.

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

**External links:** use `[link title][article_anchor]` not `[link title](article.md)` links. Where `article_anchor` is `h1 anchor` from `article.md`. Take the the anchors as named references from @hyperlinks_mkdocs_to_kb_map.md

**All absolute URLs must go through `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`** — never use bare inline URLs in articles. The hyperlinks map is the single source of truth:

- Portable: maps resolve to correct KB instance per environment
- Versionable: link targets can be updated in one place
- Localizable: supports conditional `{% if kbExport %}` blocks
- Conditionable: PDF builds can distinguish internal vs external links
- Maintainable: one file to update when URLs change

When adding a new link, always add its target to the map first, then reference it by anchor name in articles.

**Internal links:** use `[link title](#article_anchor)` format.

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

If there are no tags in the article populate the gags in the front matter.

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

## Commit messages

Follow the commit message rules given here: .agents/skills/cmwhelp-commit/SKILL.md

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
