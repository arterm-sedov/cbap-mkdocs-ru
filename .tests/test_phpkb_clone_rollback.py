import sys
from pathlib import Path


repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root / "utilities" / "phpkb_cloning"))

import phpkb_clone_rollback as rollback


class FakeCursor:
    def __init__(self, counts):
        self.counts = list(counts)
        self.calls = []

    def execute(self, sql, params=None):
        self.calls.append((" ".join(sql.split()), params))

    def fetchone(self):
        return (self.counts.pop(0),)


class FakeConnection:
    def __init__(self, cursor):
        self._cursor = cursor
        self.committed = False

    def cursor(self, buffered=False):
        return self._cursor

    def commit(self):
        self.committed = True


def test_mapped_target_ids_use_mapping_values_only():
    mapping = {
        "Articles": {"100": "900", "101": "901"},
        "Categories": {"200": "800"},
    }

    assert rollback.mapped_target_ids(mapping, "Articles") == ("901", "900")
    assert rollback.mapped_target_ids(mapping, "Categories") == ("800",)


def test_build_delete_steps_uses_dependency_order():
    mapping = {
        "Articles": {"100": "900"},
        "Categories": {"200": "800"},
    }

    steps = rollback.build_delete_steps(mapping)

    assert [(step.table, step.where) for step in steps] == [
        ("phpkb_attachments", "article_id"),
        ("phpkb_custom_data", "article_id"),
        ("phpkb_relations", "article_id"),
        ("phpkb_relations", "category_id"),
        ("phpkb_articles", "article_id"),
        ("phpkb_categories", "category_id"),
    ]


def test_run_rollback_dry_run_counts_without_deleting():
    cursor = FakeCursor(counts=[2, 1, 3, 4, 1, 1])
    connection = FakeConnection(cursor)
    mapping = {
        "Articles": {"100": "900"},
        "Categories": {"200": "800"},
    }

    report = rollback.run_rollback(connection, mapping, write=False)

    assert [item["count"] for item in report] == [2, 1, 3, 4, 1, 1]
    assert all(call[0].startswith("SELECT COUNT(*)") for call in cursor.calls)
    assert connection.committed is False


def test_run_rollback_write_deletes_in_safe_order_and_commits():
    cursor = FakeCursor(counts=[2, 1, 3, 4, 1, 1])
    connection = FakeConnection(cursor)
    mapping = {
        "Articles": {"100": "900"},
        "Categories": {"200": "800"},
    }

    rollback.run_rollback(connection, mapping, write=True)

    delete_calls = [sql for sql, _params in cursor.calls if sql.startswith("DELETE")]
    assert delete_calls == [
        "DELETE FROM `phpkb_attachments` WHERE `article_id` IN (%s)",
        "DELETE FROM `phpkb_custom_data` WHERE `article_id` IN (%s)",
        "DELETE FROM `phpkb_relations` WHERE `article_id` IN (%s)",
        "DELETE FROM `phpkb_relations` WHERE `category_id` IN (%s)",
        "DELETE FROM `phpkb_articles` WHERE `article_id` IN (%s)",
        "DELETE FROM `phpkb_categories` WHERE `category_id` IN (%s)",
    ]
    assert connection.committed is True


def test_parse_args_requires_mapping():
    try:
        rollback.parse_args(["--write"])
    except SystemExit:
        pass
    else:
        raise AssertionError("Expected SystemExit when --mapping is omitted")


def test_write_requires_explicit_delete_confirmation():
    try:
        rollback.main(["--mapping", ".mapping.json", "--write"])
    except SystemExit as error:
        assert str(error) == "--write requires --confirm-delete-cloned-content"
    else:
        raise AssertionError("Expected SystemExit when --write lacks destructive confirmation")


def test_parse_args_accepts_confirmed_write():
    args = rollback.parse_args([
        "--profile",
        "cmw",
        "--mapping",
        ".v6mapping.json",
        "--write",
        "--confirm-delete-cloned-content",
    ])

    assert args.profile == "cmw"
    assert args.mapping == ".v6mapping.json"
    assert args.write is True
    assert args.confirm_delete_cloned_content is True
