import sys
from pathlib import Path


repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root / "utilities" / "phpkb_cloning"))

import phpkb_clone_update_links as update_links


def test_remap_phpkb_links_updates_article_and_category_references():
    content = (
        '<a data-value="100">Article</a> '
        "Article-ID:100 "
        "article.php?id=100 "
        "category.php?id=200"
    )
    mapping = {
        "Articles": {"100": "900"},
        "Categories": {"200": "800"},
    }

    updated, changes = update_links.remap_phpkb_links(content, mapping)

    assert updated == (
        '<a data-value="900">Article</a> '
        "Article-ID:900 "
        "article.php?id=900 "
        "category.php?id=800"
    )
    assert len(changes) == 4


def test_product_name_replacements_are_optional():
    content = "Comindware Business Application Platform and Comindware Architect"
    title = "Comindware Business Application Platform"
    options = update_links.UpdateOptions(
        mapping={},
        replace_product_names=False,
    )

    updated_content, updated_title, changes = update_links.migrate_article_content(content, title, options)

    assert updated_content == content
    assert updated_title == title
    assert changes == []


def test_product_name_replacements_can_be_enabled():
    content = "Comindware Business Application Platform and Comindware Architect"
    title = "Comindware Business Application Platform"
    options = update_links.UpdateOptions(
        mapping={},
        replace_product_names=True,
    )

    updated_content, updated_title, changes = update_links.migrate_article_content(content, title, options)

    assert updated_content == "Comindware Platform and «Архитектор»"
    assert updated_title == "Comindware Platform"
    assert len(changes) == 3


def test_version_replacement_is_parameterized_for_v5_to_v6():
    content = "Version 5.0 content\nAnother 5.0 mention"
    title = "Platform 5.0"
    options = update_links.UpdateOptions(
        mapping={},
        old_version="5.0",
        new_version="6.0",
    )

    updated_content, updated_title, changes = update_links.migrate_article_content(content, title, options)

    assert updated_content == "Version 6.0 content\nAnother 6.0 mention"
    assert updated_title == "Platform 6.0"
    assert len(changes) == 2


def test_cli_defaults_to_dry_run():
    args = update_links.parse_args(["--article-id", "100"])

    assert update_links.has_cli_action(args)
    assert args.write is False
    assert args.replace_product_names is False


def test_cli_accepts_programmatic_v5_to_v6_update_options():
    args = update_links.parse_args([
        "--profile",
        "cmw",
        "--mapping",
        ".mapping.json",
        "--category-id",
        "900",
        "--old-version",
        "5.0",
        "--new-version",
        "6.0",
        "--replace-product-names",
        "--write",
    ])

    assert args.profile == "cmw"
    assert args.category_id == "900"
    assert args.old_version == "5.0"
    assert args.new_version == "6.0"
    assert args.replace_product_names is True
    assert args.write is True
