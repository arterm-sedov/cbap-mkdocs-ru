"""Tests for PHPKB import filename helpers."""

import re
import sys
from pathlib import Path

repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root))

LEGACY_PREFIX_PATTERN = re.compile(r"^(\d+)-(.+)$")


def normalize_import_stem(article_id, stem):
    article_id = str(article_id)
    stem = str(stem).strip()
    match = LEGACY_PREFIX_PATTERN.match(stem)
    if match and match.group(1) != article_id:
        return match.group(2)
    return stem


def build_import_base_name(article_id, stem):
    stem = normalize_import_stem(article_id, stem)
    article_id = str(article_id)
    if stem.startswith(f"{article_id}-"):
        return stem
    return f"{article_id}-{stem}"


def test_normalize_import_stem_strips_legacy_prefix():
    assert normalize_import_stem("5270", "4943-filter_records_param") == "filter_records_param"


def test_normalize_import_stem_keeps_current_prefix():
    assert normalize_import_stem("5270", "5270-filter_records_param") == "5270-filter_records_param"


def test_build_import_base_name_adds_v6_prefix_once():
    assert build_import_base_name("5270", "4943-filter_records_param") == "5270-filter_records_param"


def parse_mapping_file(mapping_json):
    if not mapping_json:
        return {}, {}
    if isinstance(mapping_json, dict) and (
        "Articles" in mapping_json or "Categories" in mapping_json
    ):
        return mapping_json.get("Articles") or {}, mapping_json.get("Categories") or {}
    return mapping_json, {}


def build_category_dir_name(category_id, title, category_folder_map, sanitize_filename):
    category_id = str(category_id)
    slug = (category_folder_map or {}).get(category_id)
    if slug:
        return sanitize_filename(f"{category_id}-{slug}")
    return sanitize_filename(f"{category_id}-{title}")


def test_parse_mapping_file_structured():
    articles, categories = parse_mapping_file(
        {"Articles": {"1": "a"}, "Categories": {"896": "platform_v6"}}
    )
    assert articles == {"1": "a"}
    assert categories == {"896": "platform_v6"}


def test_parse_mapping_file_flat_legacy():
    articles, categories = parse_mapping_file({"5270": "filter_records_param"})
    assert articles == {"5270": "filter_records_param"}
    assert categories == {}


def test_build_category_dir_name_uses_slug():
    name = build_category_dir_name(
        896,
        "Версия 6.0. Текущая рекомендованная",
        {"896": "platform_v6"},
        lambda value: value,
    )
    assert name == "896-platform_v6"
