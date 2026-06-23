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

Windows (PowerShell):

```powershell
.\.venv\Scripts\python.exe <script>.py
```

Linux/macOS:

```bash
.venv/bin/python <script>.py
```

Dependencies are listed in `install/requirements.txt`.

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

Skills are under `.agents/skills/<name>/SKILL.md`. Do not duplicate skill content here — load the skill and follow its workflow.

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

For H1 generate a concise semantic anchor in English (might be similar to filename):

{: #article_name }

For H2-H6 generate a concise semantic anchors with H1 anchor as a prefix:

{: #article_name_heading_name }

## Commit messages

Follow the commit message rules given here: .agents/skills/cmwhelp-commit/SKILL.md

## Cherry-picking between platform versions

When cherry-picking commits from one platform version branch to another (e.g., v6 → v5 or v5 → v6):

### Commit separation pattern

Structure changes into **three separate commits** to minimise noise during cross-version cherry-picking:

| # | What | Files | Cherry-pick safe? |
|---|------|-------|-------------------|
| 1 | Source article | `docs/ru/**/*.md` | ✅ Yes — pure content |
| 2 | Generated HTML | `for_kb_import_ru/**/*.html` | ✅ Yes — matches source article |
| 3 | Re-imported artifacts | `phpkb_content/<version>/**/*`, `phpkb_content_rag/<version>/**/*`, `kb.comindware.ru.platform_v*_for_llm_ingestion.md` | ❌ No — rebuild locally on target branch |

**Guidelines:**

- **Commit 1 + 2** together form a minimal cherry-pickable unit for content changes.
- **Commit 3** is version-specific noise. After cherry-picking commits 1-2 to the target branch, run the full regeneration cycle (mkdocs build → phpkb_update → phpkb_import → phpkb_ingest) on that branch to produce correct artifacts.
- **Never bring v6 kbIds into v5 articles.** After cherry-picking, restore all `kbId:` values in `docs/ru/**/*.md` to their v5 originals using `git show platform_v5:<file>` as the source of truth.
- **Cherry-pick is unsafe if kbId changed or a new article was created.** PHPKB article IDs differ between v6, v5, v4.7, v3.5 etc. — same content has different `kbId:` in each version. Always verify `kbId:` after cherry-pick.
- **Keep `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`** at the target branch version. This file maps article anchors to PHPKB article IDs — v6 mappings will break v5 links.
- **Verify `mkdocs_for_kb_import_ru.yml` site_url** matches the target branch (e.g., `v5.0/` not `v6.0/`).
- **Cross-version artifacts are safe** — `phpkb_content/<other-version>/` and `phpkb_content_rag/<other-version>/` (e.g., v5 content in v6's `phpkb_content/798-platform_v5/`) CAN be cherry-picked both ways. Both branches host all published versions, so these are not version-specific.
- **Skill and workflow files** (`.agents/skills/*`, `AGENTS.md`, `discovery_log.md`) cherry-pick safely both ways. They have no version-specific content. Auto-merge is reliable.
- **Empty cherry-pick is not harmful.** If a commit's changes already exist on the target branch, `git cherry-pick` reports "empty" — use `git cherry-pick --skip`.
- **Avoid `toc_depth` changes** unless explicitly required — they cause massive HTML churn across all generated files.
- Use `git rebase --onto <before-bad> <bad-commit> HEAD` to surgically drop a contaminated commit while preserving later ones.
---

## SELF-EVOLUTION — Documenting Discoveries

After completing a non-trivial task, review what was learned and capture it. See the [self-evolution skill](.agents/skills/self-evolution/SKILL.md) for the full methodology.
