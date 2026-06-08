"""Copy PHPKB image assets from MkDocs KB export to the web platform folder."""

import os
import shutil
from pathlib import Path

SOURCE_DIR = "for_kb_import_ru"
TARGET_DIR = "kb.comindware.ru/platform/v6.0"
IMAGE_EXTENSIONS = {".png", ".svg", ".jpg", ".jpeg", ".gif"}


def copy_image_files(source_dir, dest_dir, overwrite=False):
    source_dir = Path(source_dir)
    dest_dir = Path(dest_dir)

    if not source_dir.is_dir():
        raise FileNotFoundError(f"The directory '{source_dir}' does not exist.")

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


if __name__ == "__main__":
    copy_image_files(
        source_dir=SOURCE_DIR,
        dest_dir=TARGET_DIR,
        overwrite=True,
    )
