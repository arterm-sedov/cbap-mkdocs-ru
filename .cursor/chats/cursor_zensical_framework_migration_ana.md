# Zensical framework migration analysis
_Exported on 3/11/2026 at 18:08:14 GMT+3 from Cursor (2.6.13)_

---

**User**

deeply analyze https://github.com/zensical/zensical  and https://zensical.org/docs/get-started/ and https://zensical.org/docs/setup/basics/#theme-variant-mkdocsyml 
and https://zensical.org/docs  and see if we can migrate current repo or maybe have the two frameworks working on the same set of files, eg. PDF generation is done by mkdocs and the rest is done by zensical, or maybe we can even rewrite the PDF generation plugin and other missing parts for Zensical?


---

**Cursor**

I’ll first inspect your MkDocs configuration to see how deeply you rely on hooks/plugins, then map that against what Zensical supports and outline migration/coexistence options and what would need to be rewritten (especially for PDF and HTML cleanup).

### High‑level answer

**You should not fully migrate this repo to Zensical today.**  
However, you **can realistically run MkDocs and Zensical side‑by‑side on the same Markdown source**, with MkDocs continuing to handle PDF generation and your HTML cleanup/export pipeline, while you experiment with Zensical for the web site. Re‑implementing your hooks and PDF generation natively in Zensical is theoretically possible but would require non‑trivial custom development and watching Zensical’s plugin story mature.

Below is the detailed reasoning and a concrete coexistence/migration plan.

---

### 1. What Zensical actually offers (vs your current setup)

From the repo and docs:

- **Core concept**: “A modern static site generator built by the creators of Material for MkDocs” [`zensical/zensical`](https://github.com/zensical/zensical), [Get started docs](https://zensical.org/docs/get-started/).
- **Tech stack**: Rust + Python, distributed as a Python package (`pip install zensical` or `uv add --dev zensical`) [Get started](https://zensical.org/docs/get-started/).
- **Config**:
  - Native: `zensical.toml` with `[project]` scope [`Basics`](https://zensical.org/docs/setup/basics/#the-project-scope).
  - Transitional: **can read `mkdocs.yml` directly** to ease migration from MkDocs [`Basics – Transition from MkDocs`](https://zensical.org/docs/setup/basics/#transition-from-mkdocs).
- **Theme & HTML**:
  - Two theme variants: `modern` (default) and `classic`, selected via `[project.theme] variant = "classic"` in `zensical.toml` or `theme.variant: classic` in `mkdocs.yml` [`Basics – Theme variant`](https://zensical.org/docs/setup/basics/#theme-variant-mkdocsyml).
  - HTML structure is intentionally compatible with Material for MkDocs (your current theme), so existing **CSS/JS customizations should mostly work**.
- **Settings parity**:
  - Supports the usual `site_name`, `site_url`, `docs_dir`, `site_dir`, `extra`, `use_directory_urls`, `dev_addr` either in TOML or YAML [`Basics – Settings`](https://zensical.org/docs/setup/basics/).
  - **Unsupported (important!) MkDocs settings** include: `remote_branch`, `remote_name`, `exclude_docs`, `draft_docs`, `not_in_nav`, `validation`, `strict`, `hooks`, `watch` [`Basics – Unsupported settings`](https://zensical.org/docs/setup/basics/#unsupported-settings).

That last bullet is key for you: **`hooks` are not supported**, and `exclude_docs` is explicitly called out as unsupported. Both are used heavily in your current configuration.

---

### 2. Your current MkDocs usage and what it implies

From your `mkdocs_*.yml` and hook:

- **Config structure**:
  - `mkdocs.yml` for local RU authoring, inheriting `mkdocs_guide_complete_ru.yml`.
  - `mkdocs_guide_complete_ru.yml` → `INHERIT: mkdocs_ru.yml` and defines the big navigation tree and `exclude_docs`.
  - `mkdocs_ru.yml` → `INHERIT: mkdocs_common.yml`, sets `docs_dir: docs/ru`, `site_dir: compiled_help`, Russian site name, and RU‑specific plugin options (PDF, `extra` for KB, etc.).
  - `mkdocs_common.yml` holds:
    - **Material theme** setup (`theme.name: material`, `language: ru`, custom palette, `overrides`).
    - **Lots of plugins**: `search`, `awesome-pages`, `include-markdown`, `em-img2fig`, `autolinks`, `autorefs`, `macros`, `minify`, `tags`, `glightbox`, `htmlproofer`, `with-pdf`, etc.
    - **Markdown extensions** (attr_list, md_in_html, pymdownx.*, snippets, custom slugify, etc.).
    - Large `exclude_docs:` block.

- **Custom HTML post‑processing for KB**: `kb_html_cleanup_hook.py` defines an **MkDocs build hook**:

  - Rewrites admonition classes to KB‑specific `notice-*`.
  - Deletes redundant `<h1>`, empty `<p>`, HTML comments.
  - Adds `&zwnj;` with comments to Font Awesome icons.
  - Forces `class="colored_numbers_list"` on `ol`.
  - Sets `table` width style, class on `figure`/`figcaption`.
  - Rewrites `<img src>` to KB‑specific paths based on `config.site_name` and `page.abs_url`.
  - Tags all `<a>` with `"mkdocs_imported_link"`.
  - Massages `<pre>` code blocks into a PHPKB‑friendly structure.
  - Turns `<body>` into `<div class="md-body">` with `kb-title` handling, cleans `&zwnj;` escaping and excess newlines.
  - Returns the transformed HTML for KB import.

This is **deeply coupled to MkDocs’ hook API (`on_post_page`) and its page/config objects**.

- **PDF generation**:
  - `with-pdf` plugin in `mkdocs_common.yml` plus RU‑specific overrides in `mkdocs_ru.yml`. You rely on this for **full PDF export** of the guide.

- **MkDocs‑specific features that matter**:
  - `hooks`: used for `kb_html_cleanup_hook` (and likely `kb_html_cleanup_hook_v4.7.py`).
  - `exclude_docs`: used heavily in `mkdocs_guide_complete_ru.yml` to keep internal or WIP content out.
  - A rich plugin ecosystem (`with-pdf`, `awesome-pages`, `macros`, etc.).

---

### 3. Zensical vs this project: fit and gaps

#### 3.1. What should “just work” or mostly work

Because Zensical:

- Can read `mkdocs.yml` directly.
- Mirrors Material’s HTML structure.
- Supports `site_name`, `docs_dir`, `site_dir`, `extra`, etc.

You can reasonably expect:

- **Your Markdown files under `docs/ru` to render correctly in Zensical**, including:
  - Material‑style navigation and search (depending on how far Zensical has cloned Material’s behavior),
  - The same HTML structure and theme, especially if you choose `variant: classic`.
- **Basic `mkdocs.yml`/`mkdocs_ru.yml` configuration** (site name, docs_dir, extra, theme name) to be understood.

However, there are caveats.

#### 3.2. Things that definitely do *not* map 1:1 today

Based on Zensical docs, plus what we see in your configs:

- **No `hooks` support**:
  - Your `kb_html_cleanup_hook.py` (and v4.7) **will simply not run** in Zensical. The [Unsupported settings](https://zensical.org/docs/setup/basics/#unsupported-settings) explicitly list `hooks`.
  - Any part of your workflow that relies on this hook (KB export HTML reshaping) is currently **MkDocs‑only**.

- **`exclude_docs` unsupported**:
  - You use a big `exclude_docs` list in `mkdocs_guide_complete_ru.yml`.
  - Zensical lists `exclude_docs` under unsupported MkDocs settings. So:
    - **You cannot rely on that mechanism to hide content** when configuring Zensical via `mkdocs.yml`.
    - You’d need another mechanism (e.g., nav‑only site, filters when exporting KB, or whatever Zensical might add later).

- **Plugins**:
  - Zensical has its own extension story (see “Extensions” in the docs), but it’s not a drop‑in replacement for **arbitrary MkDocs third‑party plugins**.
  - In particular:
    - `with-pdf`: Zensical docs do not advertise a built‑in PDF exporter yet. You cannot assume this plugin will work.
    - `awesome-pages`, `em-img2fig`, `macros`, `glightbox`, `htmlproofer`, etc. may not exist or may behave differently. You’d have to map each plugin:
      - If the behavior is just Markdown extensions (e.g. admonitions, code blocks), Zensical can often replace them with built‑in support.
      - But **custom plugin behavior** (like your KB export step) will be missing.

---

### 4. Can we have MkDocs and Zensical share the same Markdown?

**Yes, and this is actually the most pragmatic strategy right now.**

Given:

- Your source docs are clean Markdown under `docs/ru/`.
- Zensical supports `mkdocs.yml` (for transition) and matches Material’s HTML.
- Zensical doesn’t yet do everything your MkDocs + plugin + hook stack does.

A **dual‑pipeline architecture** is very realistic:

- **MkDocs remains the “canonical builder” for:**
  - PDF generation via `with-pdf`.
  - KB export via `kb_html_cleanup_hook.py` and any other hooks.
  - Any MkDocs‑only features/plugins you rely on.

- **Zensical becomes an “additional builder” for:**
  - A fast, modern HTML site (possibly public docs, staging, or internal).
  - Experimentation with the `modern` theme while keeping stable output for PDFs/KB.

Concretely:

- Keep your existing `mkdocs_*.yml` files as they are.
- Introduce a **Zensical config** side‑by‑side:
  - Option A: start with `zensical.toml` that points to `docs/ru`, `site-dir-zensical`.
  - Option B: initially let Zensical read `mkdocs_ru.yml` and iterate from there.

Build commands would be something like:

```bash
# Existing
py -m mkdocs build -f mkdocs_ru.yml  # for KB/PDF pipeline

# New
zensical build  # reads zensical.toml
```

You can also:

- Put Zensical output into a different directory (e.g. `site_zensical`), so nothing interferes with your existing `compiled_help` and `for_kb_import_ru` structure.
- Keep links within Markdown identical, because both MkDocs and Zensical will interpret paths under `docs/ru` the same way as long as `use_directory_urls` is consistent.

---

### 5. What about PDF generation in Zensical?

#### 5.1. Using Zensical as‑is

Right now, Zensical docs only talk about:

- Serving and building HTML, not PDFs.
- There is no mention of a native PDF pipeline comparable to `with-pdf` in the parts you provided or in the basic docs [Get started](https://zensical.org/docs/get-started/), [Basics](https://zensical.org/docs/setup/basics/).

So:

- **There is no drop‑in `with-pdf` equivalent yet.**
- You would have to:
  - Keep using MkDocs+with‑pdf, or
  - Build your own PDF step **outside** Zensical (e.g. `wkhtmltopdf`, `weasyprint`, or `pandoc` run on Zensical’s HTML output).

Given your existing stable workflow and the importance of KB‑quality PDFs, **staying with MkDocs for PDF is the lowest risk in the near term**.

#### 5.2. Rewriting a PDF generator for Zensical

Technically possible, but:

- Requires understanding Zensical’s extension API (likely Rust core + Python bindings).
- You’d need:
  - A plugin/hook mechanism that can:
    - Hook into the build per page or overall site.
    - Access page HTML and metadata.
  - A PDF engine (probably reusing whatever with‑pdf uses under the hood or moving to `wkhtmltopdf`/`weasyprint`).
- This is **non‑trivial** and will be brittle until Zensical’s plugin API stabilizes.

Given Zensical is at `0.0.26` as of March 2026 with active development [`zensical/zensical`](https://github.com/zensical/zensical), investing in a custom PDF plugin right now would be **early adopter work**. Feasible, but high effort with unclear maintenance cost.

---

### 6. Rewriting your HTML cleanup hook for Zensical

For the KB export step:

- Today: MkDocs `on_post_page` hook (`kb_html_cleanup_hook.py`) transforms each page’s HTML into PHPKB‑friendly shape.
- Zensical: `hooks` are explicitly not supported when using `mkdocs.yml` config; Zensical’s own extension story is still evolving.

Options:

1. **Keep MkDocs as the “KB exporter” only.**
   - Continue running MkDocs build with your hook to produce `for_kb_import_ru/*.html` (or similar).
   - Use Zensical only for the “pretty web site”, not for KB export.
   - This is the simplest and safest, and requires **no immediate rewrite**.

2. **Externalize the KB cleanup as a standalone post‑processor.**
   - Instead of relying on MkDocs hooks, you can:
     - Export raw HTML pages from Zensical (or MkDocs).
     - Run a Python script (basically your existing BeautifulSoup logic) **over those HTML files as a separate step** to produce KB‑ready HTML.
   - That script can:
     - Read a directory of HTML (from Zensical build).
     - Apply exactly the same transformations (admonitions, lists, images, code blocks, etc.).
     - Output “KB HTML” for import.
   - Pros:
     - Decouples from MkDocs `on_post_page` API.
     - Could be pointed at either MkDocs or Zensical output.
   - Cons:
     - You lose direct access to `page` and `config` objects (e.g. `config.site_name`, `page.abs_url`), so you’d need to reconstruct paths from the output directory structure.
   - For you this is quite feasible: your existing hook is already ~90% pure HTML transforms; it could be refactored as a “file‑based” batch script.

3. **Wait for Zensical’s hook/plugin story and then port.**
   - When Zensical offers a per‑page hook API analogous to `on_post_page`, you can port `kb_html_cleanup_hook.py` to that model.
   - Until then, plan for the **external batch processor** instead of trying to embed it.

Given constraints, I’d recommend 1 now, and 2 as a medium‑term refactor if you want to decouple from MkDocs entirely.

---

### 7. Recommended strategy for you

#### 7.1. Short term (0–1 month): Safe coexistence

- **Keep MkDocs as the authoritative builder** for:
  - PDFs (via `with-pdf`).
  - KB export and HTML cleanup (`kb_html_cleanup_hook.py`).
  - Any existing automation (`buildhelp.ps1`, `buildhelp.py`, etc.).

- **Introduce Zensical in parallel**:
  - Add `zensical.toml`, something like:

    ```toml
    [project]
    site_name = "Comindware Platform. База знаний"
    docs_dir = "docs/ru"
    site_dir = "site_zensical"
    use_directory_urls = true  # or false, but be consistent with your linking strategy

    [project.theme]
    variant = "classic"  # to match current Material look
    ```

    Then refine once you explore their setup sections for colors, languages, etc.

  - Or start by letting Zensical read `mkdocs_ru.yml` and iteratively converting that to TOML when ready.

- **Do not try to port hooks or `with-pdf` yet.**
  - Treat Zensical as “read‑only rendering” of existing content.
  - Verify that:
    - Global navigation renders correctly.
    - RU language and features like admonitions, content tabs, code blocks behave as expected.
    - Your `overrides/` templates are compatible.

#### 7.2. Medium term (1–3 months): Decouple KB export and PDF from MkDocs

If you want to reduce your dependence on MkDocs:

- **Refactor `kb_html_cleanup_hook.py` into a standalone “HTML → KB HTML” batch processor**:
  - Inputs: directory with raw HTML pages (from **either** MkDocs or Zensical).
  - Output: KB‑shaped HTML.
  - Replace `page.abs_url` and `config.site_name` with logic based on:
    - The HTML file path.
    - A simple config JSON/YAML that gives the KB root path, etc.

- **Consider an external PDF pipeline**:
  - Use `wkhtmltopdf`, `weasyprint`, or `pandoc` to:
    - Take a Zensical (or MkDocs) HTML rendering of your docs.
    - Produce PDFs per section or as a combined manual.
  - This sidesteps the need for `with-pdf` inside Zensical.

At this point, Zensical could become the primary HTML builder, with MkDocs either:

- Kept only as a fallback, or
- Retired once your external pipelines are robust.

#### 7.3. Long term: Native Zensical plugins (if/when available)

Once Zensical stabilizes:

- Re‑evaluate:
  - Whether it exposes a plugin/hook API with per‑page HTML access.
  - Whether an official or third‑party PDF plugin exists.
- Then you can:
  - Port the refactored HTML cleanup logic into a Zensical plugin.
  - Port the PDF generation to a native Zensical plugin (or adopt an official one).

Until then, I would **not** attempt to rewrite your entire hook and PDF stack directly against Zensical internals; it’s too early.

---

### 8. Direct answers to your questions

- **“Can we migrate current repo to Zensical?”**  
  **Not fully today**, if “migrate” means “drop MkDocs and get the exact same features” (hooks, `exclude_docs`, `with-pdf`, third‑party plugins). You can migrate **core docs + navigation + theme** fairly easily, but not the full automation stack.

- **“Can we have MkDocs and Zensical working on the same set of files (e.g. PDFs by MkDocs, rest by Zensical)?”**  
  **Yes, this is the recommended path right now.**  
  Keep `docs/ru` as the single source of truth, run two builds with different configs/output dirs.

- **“Can we rewrite the PDF plugin and missing parts for Zensical?”**  
  - **In principle, yes**, by:
    - Writing an external PDF generator that runs on Zensical’s HTML output; or
    - Waiting for Zensical’s plugin API and implementing a native plugin.
  - **In practice today**, this is significant engineering work with an immature target API. It’s more pragmatic to:
    - Keep MkDocs + `with-pdf` for PDFs, and
    - Extract your HTML transformations into a reusable external tool.

If you’d like, next step I can sketch a concrete `zensical.toml` tailored to your existing `mkdocs_*.yml` and a simple PowerShell or Python script that runs both pipelines (MkDocs for PDFs/KB, Zensical for site) from one command.

