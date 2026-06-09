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
- @/phpkb_content/

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

## LINK FORMATTING

**External links:** use `[link title][article_anchor]` not `[link title](article.md)` links. Where `article_anchor` is `h1 anchor` from `article.md`. Take the the anchors as named references from @hyperlinks_mkdocs_to_kb_map.md

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

Follow the commit message rules given here: .cursor/rules/cmwhelp_commit.md

---

## SELF-EVOLUTION — Documenting Discoveries

After completing a non-trivial task, review what was learned and capture it:

### When to document

- A pattern that took debugging to figure out (e.g., silent macro errors, missing anchor warnings).
- A workflow step not covered by existing skills (e.g., which PHPKB category ID to use, which script signature fits which context).
- A recurring gotcha that cost time and would cost again.

### Where to document

- **Process/skill gaps** → update the matching skill under `.agents/skills/<name>/SKILL.md`.
- **Recurring authoring pitfalls** → add a concise rule to this AGENTS.md under the relevant heading.
- **One-off context notes** (e.g., category IDs, naming conventions) → add to the relevant skill's `references/` folder.

### How

1. State the symptom and the fix in 1–2 lines.
2. Add it to the most specific skill or rule file — prefer updating existing docs over creating new ones.
3. Keep it agnostic: no absolute paths, no secrets, no machine-specific notes.

### Discovery log (per session)

<!-- Paste brief findings below; move durable ones to skills/rules periodically -->

- **2026-06-09** — PHPKB examples category ID is `909` (used as `--target-category-id` when cloning new example articles). The end-to-end publication sequence is: clone → kbId in frontmatter → hyperlink map entry → `mkdocs build -f mkdocs_for_kb_import_ru.yml` → `phpkb_update_articles.py` → `phpkb_import_for_rag.py` → `phpkb_ingest.py` → commit+push sibling repo.
- **2026-06-09** — `{{ product Name }}` with a space silently causes a macros syntax error. Only `{{ productName }}` and `{{ companyName }}` are valid macros from `mkdocs_common.yml`.
- **2026-06-09** — `mkdocs_autorefs` emits `WARNING: Could not find cross-reference target` for links using anchors absent from `hyperlinks_mkdocs_to_kb_map.md`. Always verify all `[text][anchor]` references resolve against the map before publishing.
- **2026-06-09** — Process-task scripts use `void Main(Comindware.Process.Api.Data.ScriptContext, Comindware.Entities)` — no return value. Button scripts use `UserCommandResult Main(UserCommandContext, Comindware.Entities)`. Scenario scripts use `string Main(string ObjectID, [Comindware.Entities])`. Match the script type to the automation context: process tasks for unattended data import/sync.
