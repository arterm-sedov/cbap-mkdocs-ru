"""Unit tests for PHPKB article cloning helpers."""

import sys
import types
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

pathvalidate = types.ModuleType("pathvalidate")
pathvalidate.sanitize_filename = lambda value: value
sys.modules.setdefault("pathvalidate", pathvalidate)

import phpkb_clone


class FakeCursor:
    def __init__(self, fetches=()):
        self.fetches = list(fetches)
        self.calls = []

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
    cursor = FakeCursor(fetches=[("9001",), (7,), (2,), (1,)])
    monkeypatch.setattr(phpkb_clone, "CONNECTION", FakeConnection(cursor))
    monkeypatch.setattr(phpkb_clone, "ARTICLE_MAPPING", {})

    new_article_id = phpkb_clone.cloneArticle("100", "200", "300")

    assert new_article_id == "9001"
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
    cursor = FakeCursor(fetches=[(7,)])
    monkeypatch.setattr(phpkb_clone, "CONNECTION", FakeConnection(cursor))
    monkeypatch.setattr(phpkb_clone, "ARTICLE_MAPPING", {"100": "9001"})

    new_article_id = phpkb_clone.cloneArticle("100", "200", "300")

    assert new_article_id == "9001"
    assert not any("phpkb_attachments" in sql for sql, _ in cursor.calls)
    assert not any("phpkb_custom_data" in sql for sql, _ in cursor.calls)
