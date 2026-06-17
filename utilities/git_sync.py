"""Git add-commit-push for the PHPKB assets repo with interactive ticket prompt."""

import argparse
import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(REPO_ROOT / ".env")

SERVER_PROFILE = os.getenv("SERVER_PROFILE", "cmw").lower()
PROFILE_PREFIX = {"cmw": "CMW_", "cmwlab": "CMWLAB_"}.get(SERVER_PROFILE, "CMW_")

DEFAULT_KB_REPO_PATH = os.getenv(f"{PROFILE_PREFIX}KB_REPO_PATH", "/var/www/html")


def prompt_ticket(default_message: str) -> str:
    ticket = input(f"Commit message: {default_message}\nTicket number? (Enter to keep 'auto', or type a number): ").strip()
    if not ticket:
        ticket = "auto"
    return f"[#{ticket}] {default_message}"


def git_sync(repo_path: str, patterns: list[str], message: str, no_ask: bool = False) -> bool:
    repo = Path(repo_path).resolve()
    if not (repo / ".git").is_dir():
        print(f"Not a git repository: {repo}")
        return False

    for pattern in patterns:
        subprocess.run(
            ["git", "-C", str(repo), "add", pattern],
            capture_output=True, text=True
        )

    result = subprocess.run(
        ["git", "-C", str(repo), "diff", "--cached", "--quiet"],
        capture_output=True
    )
    if result.returncode == 0:
        print("Nothing staged — no changes to commit.")
        subprocess.run(["git", "-C", str(repo), "reset"], capture_output=True)
        return False

    if not no_ask:
        message = prompt_ticket(message)

    result = subprocess.run(
        ["git", "-C", str(repo), "commit", "-m", message],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Commit failed: {result.stderr.strip()}")
        subprocess.run(["git", "-C", str(repo), "reset"], capture_output=True)
        return False
    print(result.stdout.strip())

    result = subprocess.run(
        ["git", "-C", str(repo), "push"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Push failed: {result.stderr.strip()}")
        return False
    print(result.stdout.strip())
    return True


def parse_args():
    parser = argparse.ArgumentParser(
        description="Git add-commit-push for the PHPKB assets repo."
    )
    parser.add_argument(
        "--repo-path",
        default=DEFAULT_KB_REPO_PATH,
        help=f"PHPKB repo path (default: {DEFAULT_KB_REPO_PATH})",
    )
    parser.add_argument(
        "--patterns",
        nargs="+",
        required=True,
        help="File patterns to stage (e.g. platform/v5.0/ platform/v5.0/*.md)",
    )
    parser.add_argument(
        "--message",
        default="Update platform assets",
        help="Default commit message (ticket prompt shown unless --no-ask)",
    )
    parser.add_argument(
        "--no-ask",
        action="store_true",
        help="Skip ticket prompt and use the default message as-is",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    sys.exit(0 if git_sync(args.repo_path, args.patterns, args.message, args.no_ask) else 1)
