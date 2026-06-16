"""Copy PHPKB image assets from MkDocs KB export to the web platform folder."""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent
load_dotenv(REPO_ROOT / ".env")

SERVER_PROFILE = os.getenv("SERVER_PROFILE", "cmw").lower()
PROFILE_PREFIX = {"cmw": "CMW_", "cmwlab": "CMWLAB_"}.get(SERVER_PROFILE, "CMW_")
DEFAULT_KB_REPO_PATH = os.getenv(f"{PROFILE_PREFIX}KB_REPO_PATH", "/var/www/html")

IMAGE_EXTENSIONS = {".png", ".svg", ".jpg", ".jpeg", ".gif"}


def copy_image_files(source_dir, dest_dir, overwrite=False):
    source_dir = Path(source_dir)
    dest_dir = Path(dest_dir)

    if not source_dir.is_dir():
        raise FileNotFoundError(f"The directory '{source_dir}' does not exist.")

    copied = 0
    for root, _, files in os.walk(source_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in IMAGE_EXTENSIONS:
                continue

            src_path = Path(root) / file
            relative_path = src_path.relative_to(source_dir)
            dest_path = dest_dir / relative_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            if dest_path.exists():
                if not overwrite:
                    print(f"Skipped existing file: {dest_path}")
                    continue
                print(f"Overwriting: {dest_path}")

            shutil.copy2(src_path, dest_path)
            print(f"Copied: {src_path} -> {dest_path}")
            copied += 1

    return copied


def git_sync_assets(kb_repo_path: str, version: str, no_ask: bool):
    subprocess.run([
        sys.executable, str(REPO_ROOT / "utilities/git_sync.py"),
        "--repo-path", kb_repo_path,
        "--patterns", f"platform/{version}/",
        "--message", f"Update platform {version} images",
    ] + (["--no-ask"] if no_ask else []))


def ssh_pull_production(no_ask: bool):
    subprocess.run([
        sys.executable, str(REPO_ROOT / "utilities/ssh_pull.py"),
    ] + (["--no-ask"] if no_ask else []))


def parse_args():
    parser = argparse.ArgumentParser(
        description="Copy PHPKB image assets from MkDocs KB export to the web platform folder."
    )
    parser.add_argument(
        "--source-dir",
        default="for_kb_import_ru",
        help="Source directory with MkDocs HTML export (default: for_kb_import_ru)",
    )
    parser.add_argument(
        "--kb-repo-path",
        default=DEFAULT_KB_REPO_PATH,
        help=f"PHPKB repo root path (default: {DEFAULT_KB_REPO_PATH})",
    )
    parser.add_argument(
        "--version",
        default="v6.0",
        choices=["v4.7", "v5.0", "v6.0"],
        help="Platform version target directory (default: v6.0)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        default=True,
        help="Overwrite existing files (default: true)",
    )
    parser.add_argument(
        "--no-overwrite",
        action="store_false",
        dest="overwrite",
        help="Skip existing files",
    )
    parser.add_argument(
        "--git",
        action="store_true",
        help="Git add-commit-push images in the PHPKB repo after copying",
    )
    parser.add_argument(
        "--pull",
        action="store_true",
        help="SSH into production server and git pull after push",
    )
    parser.add_argument(
        "--no-ask",
        action="store_true",
        help="Skip confirmation prompts for git and pull",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    dest_dir = Path(args.kb_repo_path) / "platform" / args.version

    copied = copy_image_files(
        source_dir=args.source_dir,
        dest_dir=dest_dir,
        overwrite=args.overwrite,
    )

    if copied == 0:
        print("No images copied.")
        sys.exit(0)

    if args.git:
        git_sync_assets(args.kb_repo_path, args.version, args.no_ask)

    if args.pull:
        ssh_pull_production(args.no_ask)
