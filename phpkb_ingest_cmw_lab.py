from gitingest import ingest
import subprocess
import yaml
from datetime import datetime
import re

# def get_git_info():
#     try:
#         current_branch = subprocess.check_output(
#             ["git", "rev-parse", "--abbrev-ref", "HEAD"], encoding="utf-8"
#         ).strip()
#     except Exception:
#         current_branch = "unknown"

#     try:
#         repo_address = subprocess.check_output(
#             ["git", "config", "--get", "remote.origin.url"], encoding="utf-8"
#         ).strip()
#     except Exception:
#         # Try to get the first available remote
#         try:
#             remotes = subprocess.check_output(
#                 ["git", "remote"], encoding="utf-8"
#             ).strip().splitlines()
#             if remotes:
#                 repo_address = subprocess.check_output(
#                     ["git", "config", "--get", f"remote.{remotes[0]}.url"], encoding="utf-8"
#                 ).strip()
#             else:
#                 repo_address = "unknown"
#         except Exception:
#             repo_address = "unknown"

#     return repo_address, current_branch

if __name__ == "__main__":
    folder = "phpkb_content_cmw_lab/29. CMW Platform"
    summary, tree, content = ingest(folder, exclude_patterns="*.html")
    # repo_address, current_branch = get_git_info()
    ingestion_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #source_line = f"Source: {repo_address.strip('.git')}/tree/{current_branch}"
    source_line = "Source: https://kb.cmwlab.com/category.php?id=29"
    # Add 'https://kb.cmwlab.com' prefix to all image sources starting with '](/platform/' using simple replace
    content = re.sub(r'(\[[^\]]*\])\(/([^)]+)\)', r'\1(https://kb.cmwlab.com/\2)', content)
    print(source_line)
    # Remove include-markdown directive from content using replace for efficiency
    content = content.replace('{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}', "")
    # Read mkdocs_ru.yml to get the URL prefixes
    with open("mkdocs_ru.yml", "r", encoding="utf-8") as yml_file:
        yml_data = yaml.safe_load(yml_file)
    extra = yml_data.get("extra", {})
    kb_article_url_prefix = extra.get("kbArticleURLPrefix", "")
    kb_category_url_prefix = extra.get("kbCategoryURLPrefix", "")

    with open("docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md", "r", encoding="utf-8") as snippet_file:
        snippet_content = snippet_file.read()
    # Replace placeholders with actual values
    snippet_content = snippet_content.replace("{{ kbArticleURLPrefix }}", kb_article_url_prefix)
    snippet_content = snippet_content.replace("{{ kbCategoryURLPrefix }}", kb_category_url_prefix)
    # Remove all Jinja markup (lines or blocks with {% ... %})
    snippet_content = re.sub(r'{%.*?%}', '', snippet_content, flags=re.DOTALL)
    # Remove all HTML comments (<!-- ... -->)
    snippet_content = re.sub(r'<!--.*?-->', '', snippet_content, flags=re.DOTALL)
    # Replace three or more newlines with just two newlines
    snippet_content = re.sub(r'\n{2,}', '\n', snippet_content)
    # Extract only the 'Files analyzed' and 'Estimated tokens' lines from the summary using regex
    matches = re.findall(r'^(Files analyzed:.*|Estimated tokens:.*)$', summary, re.MULTILINE)
    summary_short = "\n".join([m.strip() for m in matches])# if len(matches) == 2 else summary
    with open("kb.cmwlab.com.platform_v4_for_llm_ingestion.md", "w", encoding="utf-8") as f:
        f.write(
            f"\n----------------------\n\n"
            f"Ingestion date: {ingestion_date}\n"
            f"Title: Comindware Platform V4 knowledge base for AI ingestion\n"
            f"Description: Provide this file to your AI agent. For better results, add the prompt below\n"
            f"{source_line}\n"
            f"{summary_short}\n\n"
            f"----------------------\n\n"
        )
        # Insert the bilingual instruction after the summary frontmatter
        f.write(
            "## Prompting instructions\n\n"
            "### EN Prompt example\n\n"
            "- Answer the following question: <YOUR_QUESTION>\n"
            "- In your answer, provide links to the referenced articles in the format:\n"
            "  `https://kb.cmwlab.com/article.php?id={kbId}`\n"
            "  Take `{kbId}` from the frontmatter of the original Markdown articles.\n\n"
            "### RU Пример промпта\n\n"
            "- Ответь на следующий вопрос: <ВАШ_ВОПРОС>\n"
            "- В ответе приведи ссылки на использованные статьи в формате:\n"
            "  `https://kb.cmwlab.com/article.php?id={kbId}`\n"
            "  `{kbId}` возьми из frontmatter исходного текста статей в формате Markdown.\n\n"
        )
        f.write(
            "## Sections\n\n"
            f"{tree}\n"
            "## Articles\n\n"
            f"{content}"
        )
        # f.write("## HYPERLINKS MAP\n" + snippet_content)