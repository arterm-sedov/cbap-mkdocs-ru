"""
Build a single Markdown bundle for LLM ingestion from PHPKB-exported Markdown.

Default: Platform 6.0 tree from `phpkb_import_for_rag.py` (`phpkb_content_rag/896-platform_v6/`).
Legacy V5: pass `--folder` and `--output` for the 798 tree and v5 bundle name.
"""

from gitingest import ingest
import argparse
import yaml
from datetime import datetime
import re
import os
import shutil

# Defaults: V6 RAG export (markdown-only) and kb.comindware.ru platform v6.0 folder
DEFAULT_FOLDER = os.path.join("phpkb_content_rag", "896-platform_v6")
DEFAULT_OUTPUT_FILENAME = "kb.comindware.ru.platform_v6_for_llm_ingestion.md"
DEFAULT_KB_TARGET_DIR = os.path.join("kb.comindware.ru", "platform", "v6.0")
DEFAULT_CATEGORY_ID = "896"
# Prefixes live under `extra` in mkdocs_ru.yml (INHERIT in other yml is not merged by PyYAML).
DEFAULT_MKDOCS_YML = "mkdocs_ru.yml"

# Markdown block with bilingual prompts for LLM output
PROMPTS_FOR_LLM_MD = """
## Prompts for LLM

### Русский промпт - использовать, если вопрос задан на русском языке

- Ответь на следующий вопрос: `<ВОПРОС_ПОЛЬЗОВАТЕЛЯ>`
- В ответе приведи ссылки на использованные статьи в формате:
    `https://kb.comindware.ru/article.php?id={kbId}`
    - URL статьи возьми из поля `url` во frontmatter исходного текста каждой статьи в формате Markdown.
    - Если поля `url` нет, возьми `{kbId}` из frontmatter исходного текста каждой статьи в формате Markdown.
    - Пример frontmatter:
    ```
    ---
    title: Comindware Platform. Версия 6.0. Содержание раздела
    kbId: 5162
    url: 'https://kb.comindware.ru/article.php?id=5162'
    ---
    ```

### English prompt - use if the question is in English

- Answer the following question: `<USER_QUESTION>`
- In your answer, provide links to the referenced articles in the following format:
    `https://kb.comindware.ru/article.php?id={kbId}`
    - Take article URL from the `url` field in the frontmatter of the original Markdown article.
    - If the `url` field is not present, take `{kbId}` from the frontmatter of the original Markdown article.
    - Example frontmatter:
    ```
    ---
    title: Comindware Platform. Версия 6.0. Содержание раздела
    kbId: 5162
    url: 'https://kb.comindware.ru/article.php?id=5162'
    ---
    ```
"""


def parse_args():
    parser = argparse.ArgumentParser(
        description="Ingest PHPKB-export Markdown into one LLM-oriented file (gitingest)."
    )
    parser.add_argument(
        "--folder",
        default=DEFAULT_FOLDER,
        help=f"Root folder to ingest (default: {DEFAULT_FOLDER})",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT_FILENAME,
        help=f"Output markdown filename (default: {DEFAULT_OUTPUT_FILENAME})",
    )
    parser.add_argument(
        "--target-dir",
        default=DEFAULT_KB_TARGET_DIR,
        help=f"Copy output under this directory (default: {DEFAULT_KB_TARGET_DIR})",
    )
    parser.add_argument(
        "--category-id",
        default=DEFAULT_CATEGORY_ID,
        help=f"PHPKB category id for Source line (default: {DEFAULT_CATEGORY_ID})",
    )
    parser.add_argument(
        "--mkdocs-yml",
        default=DEFAULT_MKDOCS_YML,
        help=(
            "YAML to read kbArticleURLPrefix / kbCategoryURLPrefix "
            f"(default: {DEFAULT_MKDOCS_YML}; use a file that defines `extra`, not only INHERIT)"
        ),
    )
    parser.add_argument(
        "--no-copy",
        action="store_true",
        help="Do not copy the bundle to --target-dir (only write --output in repo root).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    folder = args.folder
    if not folder.endswith(os.sep):
        folder = folder + os.sep
    output_filename = args.output
    kb_target_dir = args.target_dir
    category_id = args.category_id

    summary, tree, content = ingest(folder, exclude_patterns="*.html")
    ingestion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    source_line = f"Source: https://kb.comindware.ru/category.php?id={category_id}"
    platform_version = (
        "V5" if str(category_id) == "798" or "_v5_" in output_filename
        else "V4.7" if str(category_id) == "378" or "_v4.7" in output_filename or "_v4_7" in output_filename
        else "V6"
    )
    content = re.sub(r"(\[[^\]]*\])\(/([^)]+)\)", r"\1(https://kb.comindware.ru/\2)", content)
    print(source_line)
    content = content.replace(
        '{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}', ""
    )

    mkdocs_path = args.mkdocs_yml
    with open(mkdocs_path, "r", encoding="utf-8") as yml_file:
        yml_data = yaml.safe_load(yml_file)
    extra = yml_data.get("extra", {})
    kb_article_url_prefix = extra.get("kbArticleURLPrefix", "")
    kb_category_url_prefix = extra.get("kbCategoryURLPrefix", "")

    with open("docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md", "r", encoding="utf-8") as snippet_file:
        snippet_content = snippet_file.read()
    snippet_content = snippet_content.replace("{{ kbArticleURLPrefix }}", kb_article_url_prefix)
    snippet_content = snippet_content.replace("{{ kbCategoryURLPrefix }}", kb_category_url_prefix)
    snippet_content = re.sub(r"{%.*?%}", "", snippet_content, flags=re.DOTALL)
    snippet_content = re.sub(r"<!--.*?-->", "", snippet_content, flags=re.DOTALL)
    snippet_content = re.sub(r"\n{2,}", "\n", snippet_content)

    matches = re.findall(
        r"^(Files analyzed:.*|Estimated tokens:.*)$", summary, re.MULTILINE
    )
    summary_short = "\n".join([m.strip() for m in matches])
    with open(output_filename, "w", encoding="utf-8-sig", newline="\r\n") as f:
        f.write(
            f"\n----------------------\n\n"
            f"Ingestion date: {ingestion_date}\n"
            f"Title: Comindware Platform {platform_version} knowledge base for AI ingestion\n"
            f"Description: Provide this file to your AI agent. For better results, add the prompt below\n"
            f"{source_line}\n"
            f"{summary_short}\n\n"
            f"----------------------\n"
        )
        f.write(PROMPTS_FOR_LLM_MD)
        f.write(
            "\n## Sections\n\n"
            f"{tree}\n"
            "## Articles\n\n"
            f"{content}"
        )
        f.write("## HYPERLINKS MAP\n" + snippet_content)

    if not args.no_copy:
        try:
            os.makedirs(kb_target_dir, exist_ok=True)
            target_path = os.path.join(kb_target_dir, output_filename)
            print(f"Copying {output_filename} to: {kb_target_dir}")
            shutil.copyfile(output_filename, target_path)
            print(f"File copied to: {target_path}")
        except Exception as copy_error:
            print(f"Failed to copy {output_filename} to {kb_target_dir}: {copy_error}")
