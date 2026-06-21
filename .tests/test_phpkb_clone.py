"""Unit tests for PHPKB article cloning helpers."""

import sys
import types
from pathlib import Path

repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root / "utilities" / "phpkb_cloning"))

pathvalidate = types.ModuleType("pathvalidate")
pathvalidate.sanitize_filename = lambda value: value
sys.modules.setdefault("pathvalidate", pathvalidate)

import phpkb_clone


class FakeCursor:
    def __init__(self, fetches=(), lastrowid=0):
        self.fetches = list(fetches)
        self.calls = []
        self.lastrowid = lastrowid

    def execute(self, sql, params=None):
        self.calls.append((" ".join(sql.split()), params))

    def fetchone(self):
        return self.fetches.pop(0)


class FakeConnection:
    def __init__(self, cursor):
        self._cursor = cursor

    def cursor(self, buffered=False):
        return self._cursor


def test_clone_article_child_rows_remaps_article_backref_without_copying_files():
    cursor = FakeCursor(fetches=[(2,)])
    spec = {
        "table": "phpkb_attachments",
        "columns": ("article_id", "file_guid", "file_name", "file_type", "file_views", "file_status"),
    }

    cloned = phpkb_clone.clone_article_child_rows(cursor, "100", "9001", spec)

    assert cloned == 2
    assert cursor.calls == [
        ("SELECT COUNT(*) FROM `phpkb_attachments` WHERE `article_id`=%s", ("100",)),
        (
            "INSERT INTO `phpkb_attachments` (`article_id`, `file_guid`, `file_name`, `file_type`, `file_views`, `file_status`) "
            "SELECT %s, `file_guid`, `file_name`, `file_type`, `file_views`, `file_status` "
            "FROM `phpkb_attachments` WHERE `article_id`=%s",
            ("9001", "100"),
        ),
    ]


def test_clone_article_child_rows_skips_empty_sources():
    cursor = FakeCursor(fetches=[(0,)])
    spec = {
        "table": "phpkb_custom_data",
        "columns": ("field_id", "article_id", "field_data"),
    }

    cloned = phpkb_clone.clone_article_child_rows(cursor, "100", "9001", spec)

    assert cloned == 0
    assert cursor.calls == [
        ("SELECT COUNT(*) FROM `phpkb_custom_data` WHERE `article_id`=%s", ("100",)),
    ]


def test_clone_article_clones_dependents_once_for_new_article(monkeypatch):
    cursor = FakeCursor(fetches=[(7,), (0,), (2,), (1,)], lastrowid=9001)
    mapping_saves = []
    monkeypatch.setattr(phpkb_clone, "CONNECTION", FakeConnection(cursor))
    monkeypatch.setattr(phpkb_clone, "ARTICLE_MAPPING", {})
    monkeypatch.setattr(phpkb_clone, "updateMappingJson", lambda: mapping_saves.append("saved"))

    new_article_id = phpkb_clone.cloneArticle("100", "200", "300")

    assert new_article_id == "9001"
    assert mapping_saves == ["saved"]
    assert not any("SELECT MAX(article_id)" in sql for sql, _ in cursor.calls)
    assert (
        "INSERT INTO phpkb_relations (article_id, category_id, article_priority) VALUES (9001, 300, 7);",
        None,
    ) in cursor.calls
    assert (
        "INSERT INTO `phpkb_attachments` (`article_id`, `file_guid`, `file_name`, `file_type`, `file_views`, `file_status`) "
        "SELECT %s, `file_guid`, `file_name`, `file_type`, `file_views`, `file_status` "
        "FROM `phpkb_attachments` WHERE `article_id`=%s",
        ("9001", "100"),
    ) in cursor.calls
    assert (
        "INSERT INTO `phpkb_custom_data` (`field_id`, `article_id`, `field_data`) "
        "SELECT `field_id`, %s, `field_data` FROM `phpkb_custom_data` WHERE `article_id`=%s",
        ("9001", "100"),
    ) in cursor.calls


def test_clone_article_does_not_duplicate_dependents_for_mapped_article(monkeypatch):
    cursor = FakeCursor(fetches=[(7,), (0,)])
    monkeypatch.setattr(phpkb_clone, "CONNECTION", FakeConnection(cursor))
    monkeypatch.setattr(phpkb_clone, "ARTICLE_MAPPING", {"100": "9001"})

    new_article_id = phpkb_clone.cloneArticle("100", "200", "300")

    assert new_article_id == "9001"
    assert not any("phpkb_attachments" in sql for sql, _ in cursor.calls)
    assert not any("phpkb_custom_data" in sql for sql, _ in cursor.calls)


def test_clone_article_skips_existing_relation_for_mapped_article(monkeypatch):
    cursor = FakeCursor(fetches=[(7,), (1,)])
    monkeypatch.setattr(phpkb_clone, "CONNECTION", FakeConnection(cursor))
    monkeypatch.setattr(phpkb_clone, "ARTICLE_MAPPING", {"100": "9001"})

    new_article_id = phpkb_clone.cloneArticle("100", "200", "300")

    assert new_article_id == "9001"
    assert not any("INSERT INTO phpkb_relations" in sql for sql, _ in cursor.calls)


def test_clone_category_uses_lastrowid_and_updates_mapping(monkeypatch):
    cursor = FakeCursor(lastrowid=8001)
    mapping_saves = []
    monkeypatch.setattr(phpkb_clone, "CONNECTION", FakeConnection(cursor))
    monkeypatch.setattr(phpkb_clone, "CATEGORY_MAPPING", {})
    monkeypatch.setattr(phpkb_clone, "updateMappingJson", lambda: mapping_saves.append("saved"))

    new_category_id = phpkb_clone.cloneCategory("700", "800")

    assert new_category_id == "8001"
    assert phpkb_clone.CATEGORY_MAPPING == {"700": "8001"}
    assert mapping_saves == ["saved"]
    assert not any("SELECT MAX(category_id)" in sql for sql, _ in cursor.calls)


def test_clone_category_reuses_loaded_mapping(monkeypatch):
    cursor = FakeCursor()
    monkeypatch.setattr(phpkb_clone, "CONNECTION", FakeConnection(cursor))
    monkeypatch.setattr(phpkb_clone, "CATEGORY_MAPPING", {"700": "8001"})

    new_category_id = phpkb_clone.cloneCategory("700", "999")

    assert new_category_id == "8001"
    assert cursor.calls == []


def test_initialize_mapping_loads_existing_mapping(tmp_path):
    mapping_file = tmp_path / ".mapping.json"
    mapping_file.write_text(
        '{"Categories": {"700": 8001}, "Articles": {"100": 9001}}',
        encoding="utf-8",
    )

    phpkb_clone.initializeMapping(str(mapping_file))

    assert phpkb_clone.CATEGORY_MAPPING == {"700": "8001"}
    assert phpkb_clone.ARTICLE_MAPPING == {"100": "9001"}
    assert phpkb_clone.MAPPING_FILE == str(mapping_file)


def test_initialize_mapping_fresh_refuses_existing_mapping(tmp_path):
    mapping_file = tmp_path / ".mapping.json"
    mapping_file.write_text("{}", encoding="utf-8")

    try:
        phpkb_clone.initializeMapping(str(mapping_file), fresh=True)
    except FileExistsError:
        pass
    else:
        raise AssertionError("Expected FileExistsError for --fresh with an existing mapping")


def test_update_mapping_json_prints_compact_summary(tmp_path, monkeypatch, capsys):
    mapping_file = tmp_path / ".mapping.json"
    monkeypatch.setattr(phpkb_clone, "MAPPING_FILE", str(mapping_file))
    monkeypatch.setattr(phpkb_clone, "CATEGORY_MAPPING", {"798": "896"})
    monkeypatch.setattr(phpkb_clone, "ARTICLE_MAPPING", {"4578": "5162", "4579": "5161"})
    monkeypatch.setattr(phpkb_clone, "MAPPING", {})

    phpkb_clone.updateMappingJson()

    output = capsys.readouterr().out
    assert "Saved mapping" in output
    assert "categories=1" in output
    assert "articles=2" in output
    assert '"Articles"' not in output
    assert mapping_file.exists()


def test_category_child_where_defaults_to_public_visible_russian_categories():
    assert phpkb_clone.category_child_where() == (
        "category_show='yes' AND category_status = 'public' AND phpkb_categories.language_id = 2"
    )


def test_category_child_where_include_private_drops_public_only_filter():
    assert phpkb_clone.category_child_where(include_private=True) == (
        "category_show='yes' AND phpkb_categories.language_id = 2"
    )


def test_parse_args_requires_mapping():
    try:
        phpkb_clone.parse_args(["--category-id", "798"])
    except SystemExit:
        pass
    else:
        raise AssertionError("Expected SystemExit when --mapping is omitted")


def test_parse_args_accepts_scripted_article_clones():
    args = phpkb_clone.parse_args([
        "--profile", "cmwlab",
        "--mapping", ".clone.json",
        "--fresh",
        "--dry-run",
        "--article-id", "100",
        "--article-id", "101",
        "--target-category-id", "900",
        "--suffix", "_V5",
        "--show",
    ])

    assert args.profile == "cmwlab"
    assert args.mapping == ".clone.json"
    assert args.fresh is True
    assert args.dry_run is True
    assert args.article_id == ["100", "101"]
    assert args.target_category_id == "900"
    assert args.suffix == "_V5"
    assert args.show is True
    assert phpkb_clone.has_cli_action(args) is True


def test_run_cli_clones_articles_without_prompting(monkeypatch):
    calls = []
    args = phpkb_clone.parse_args([
        "--mapping", ".scratch/test_mapping.json",
        "--article-id", "100",
        "--article-id", "101",
        "--target-category-id", "900",
        "--suffix", "_V5",
        "--show",
    ])

    monkeypatch.setattr(
        phpkb_clone,
        "clone_specific_article_to",
        lambda article_id, target_category_id=None, suffix="_CLONE", show=False: calls.append(
            (article_id, target_category_id, suffix, show)
        ) or True,
    )

    assert phpkb_clone.run_cli(args) is True
    assert calls == [
        ("100", "900", "_V5", True),
        ("101", "900", "_V5", True),
    ]


def test_run_cli_clones_category_tree_with_target_parent(monkeypatch):
    calls = []
    args = phpkb_clone.parse_args(["--mapping", ".v6mapping.json", "--category-id", "798", "--target-parent-id", "1000"])

    monkeypatch.setattr(phpkb_clone, "fetchCategory", lambda category_id: (category_id, "Version", "1"))
    monkeypatch.setattr(
        phpkb_clone,
        "cloneCategoryChildren",
        lambda category, target_parent_id="", include_private=False: calls.append(
            (category, target_parent_id, include_private)
        ) or [],
    )

    assert phpkb_clone.run_cli(args) is True
    assert calls == [(("798", "Version", "1"), "1000", False)]


def test_run_cli_passes_include_private_to_category_clone(monkeypatch):
    calls = []
    args = phpkb_clone.parse_args(["--mapping", ".v6mapping.json", "--category-id", "798", "--include-private"])

    monkeypatch.setattr(phpkb_clone, "fetchCategory", lambda category_id: (category_id, "Version", "1"))
    monkeypatch.setattr(
        phpkb_clone,
        "cloneCategoryChildren",
        lambda category, target_parent_id="", include_private=False: calls.append(include_private) or [],
    )

    assert phpkb_clone.run_cli(args) is True
    assert calls == [True]


def test_count_article_child_rows_counts_supported_backrefs():
    cursor = FakeCursor(fetches=[(3,), (2,)])

    counts = phpkb_clone.count_article_child_rows(cursor, "100")

    assert counts == {"attachments": 3, "custom data": 2}
    assert cursor.calls == [
        ("SELECT COUNT(*) FROM `phpkb_attachments` WHERE `article_id`=%s", ("100",)),
        ("SELECT COUNT(*) FROM `phpkb_custom_data` WHERE `article_id`=%s", ("100",)),
    ]


def test_count_article_child_rows_for_articles_counts_in_bulk():
    cursor = FakeCursor(fetches=[(5,), (3,)])

    counts = phpkb_clone.count_article_child_rows_for_articles(cursor, ("100", "101"))

    assert counts == {"attachments": 5, "custom data": 3}
    assert cursor.calls == [
        ("SELECT COUNT(*) FROM `phpkb_attachments` WHERE `article_id` IN (%s, %s)", ("100", "101")),
        ("SELECT COUNT(*) FROM `phpkb_custom_data` WHERE `article_id` IN (%s, %s)", ("100", "101")),
    ]


def test_plan_specific_article_reports_reused_article_without_backref_counts(monkeypatch):
    cursor = FakeCursor(fetches=[("200",)])
    monkeypatch.setattr(phpkb_clone, "CONNECTION", FakeConnection(cursor))
    monkeypatch.setattr(phpkb_clone, "ARTICLE_MAPPING", {"100": "9001"})

    plan = phpkb_clone.plan_specific_article_to("100", target_category_id="300")

    assert plan["articles_seen"] == 1
    assert plan["articles_reused"] == 1
    assert plan["articles_would_clone"] == 0
    assert plan["relations_to_create"] == 1
    assert not any("phpkb_attachments" in sql for sql, _ in cursor.calls)


def test_plan_specific_article_counts_backrefs_for_unmapped_article(monkeypatch):
    cursor = FakeCursor(fetches=[("200",), (3,), (2,)])
    monkeypatch.setattr(phpkb_clone, "CONNECTION", FakeConnection(cursor))
    monkeypatch.setattr(phpkb_clone, "ARTICLE_MAPPING", {})

    plan = phpkb_clone.plan_specific_article_to("100", target_category_id="300")

    assert plan["articles_seen"] == 1
    assert plan["articles_would_clone"] == 1
    assert plan["articles_reused"] == 0
    assert plan["attachment_rows"] == 3
    assert plan["custom_data_rows"] == 2


def test_run_cli_dry_run_category_uses_plan_without_cloning(monkeypatch):
    args = phpkb_clone.parse_args(["--mapping", ".v6mapping.json", "--category-id", "798", "--target-parent-id", "1000", "--dry-run"])
    calls = []

    monkeypatch.setattr(phpkb_clone, "fetchCategory", lambda category_id: (category_id, "Version", "1"))
    monkeypatch.setattr(
        phpkb_clone,
        "planCategoryChildren",
        lambda category, newParentId="", include_private=False: calls.append(
            (category, newParentId, include_private)
        ) or {
            **phpkb_clone.empty_clone_plan(),
            "categories_seen": 1,
            "categories_would_clone": 1,
        },
    )
    monkeypatch.setattr(
        phpkb_clone,
        "cloneCategoryChildren",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(AssertionError("dry-run must not clone")),
    )

    assert phpkb_clone.run_cli(args) is True
    assert calls == [(("798", "Version", "1"), "1000", False)]
