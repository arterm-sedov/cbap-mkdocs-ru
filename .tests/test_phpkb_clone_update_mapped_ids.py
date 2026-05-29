import json
import sys
from pathlib import Path


repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root / "utilities" / "phpkb_cloning"))

import phpkb_clone_update_mapped_ids as update_mapped_ids


def test_replace_frontmatter_kbids_updates_only_article_kbids():
    content = "---\nkbId: 4918\ntitle: Test\n---\n\nCategory 871 stays text.\n"

    updated, changes = update_mapped_ids.replace_frontmatter_kbids(content, {"4918": "6001"})

    assert changes == 1
    assert updated == "---\nkbId: 6001\ntitle: Test\n---\n\nCategory 871 stays text.\n"


def test_replace_hyperlink_map_ids_updates_articles_and_categories():
    content = (
        "[article]: {{ kbArticleURLPrefix }}4918\n"
        "[category]: {{ kbCategoryURLPrefix }}871\n"
        "[unchanged]: {{ kbArticleURLPrefix }}9999\n"
    )
    mapping = {
        "Articles": {"4918": "6001"},
        "Categories": {"871": "940"},
    }

    updated, changes = update_mapped_ids.replace_hyperlink_map_ids(content, mapping)

    assert changes == {"Articles": 1, "Categories": 1}
    assert updated == (
        "[article]: {{ kbArticleURLPrefix }}6001\n"
        "[category]: {{ kbCategoryURLPrefix }}940\n"
        "[unchanged]: {{ kbArticleURLPrefix }}9999\n"
    )


def test_dry_run_does_not_write_hyperlink_map(tmp_path):
    hyperlinks_file = tmp_path / "hyperlinks_mkdocs_to_kb_map.md"
    original = "[category]: {{ kbCategoryURLPrefix }}871\n"
    hyperlinks_file.write_text(original, encoding="utf-8")

    result = update_mapped_ids.update_hyperlink_map(
        hyperlinks_file,
        {"Categories": {"871": "940"}},
        write=False,
    )

    assert result == {"files_changed": 1, "article_links": 0, "category_links": 1}
    assert hyperlinks_file.read_text(encoding="utf-8") == original


def test_write_updates_frontmatter_files(tmp_path):
    docs_root = tmp_path / "docs" / "ru"
    docs_root.mkdir(parents=True)
    article = docs_root / "article.md"
    article.write_text("---\nkbId: 4918\n---\n", encoding="utf-8")

    result = update_mapped_ids.update_frontmatter_kbids(
        docs_root,
        {"Articles": {"4918": "6001"}},
        write=True,
    )

    assert result == {"files_scanned": 1, "files_changed": 1, "replacements": 1}
    assert article.read_text(encoding="utf-8") == "---\nkbId: 6001\n---\n"


def test_write_preserves_utf16_markdown_encoding(tmp_path):
    docs_root = tmp_path / "docs" / "ru"
    docs_root.mkdir(parents=True)
    article = docs_root / "article.md"
    article.write_text("---\nkbId: 4918\n---\n", encoding="utf-16-be")
    article.write_bytes(b"\xfe\xff" + article.read_bytes())

    result = update_mapped_ids.update_frontmatter_kbids(
        docs_root,
        {"Articles": {"4918": "6001"}},
        write=True,
    )

    assert result == {"files_scanned": 1, "files_changed": 1, "replacements": 1}
    assert article.read_bytes().startswith(b"\xfe\xff")
    assert article.read_text(encoding="utf-16") == "---\nkbId: 6001\n---\n"


def test_run_hyperlink_map_target_reads_mapping_and_writes(tmp_path, capsys):
    mapping_file = tmp_path / ".mapping.json"
    hyperlinks_file = tmp_path / "hyperlinks_mkdocs_to_kb_map.md"
    mapping_file.write_text(
        json.dumps({"Articles": {"4918": "6001"}, "Categories": {"871": "940"}}),
        encoding="utf-8",
    )
    hyperlinks_file.write_text(
        "[article]: {{ kbArticleURLPrefix }}4918\n[category]: {{ kbCategoryURLPrefix }}871\n",
        encoding="utf-8",
    )
    args = update_mapped_ids.parse_args(
        [
            "--mapping",
            str(mapping_file),
            "--target",
            "hyperlink-map",
            "--hyperlinks-file",
            str(hyperlinks_file),
            "--write",
        ]
    )

    report = update_mapped_ids.run(args)

    assert report["hyperlink-map"] == {"files_changed": 1, "article_links": 1, "category_links": 1}
    assert hyperlinks_file.read_text(encoding="utf-8") == (
        "[article]: {{ kbArticleURLPrefix }}6001\n[category]: {{ kbCategoryURLPrefix }}940\n"
    )
    assert "Hyperlink map:" in capsys.readouterr().out
