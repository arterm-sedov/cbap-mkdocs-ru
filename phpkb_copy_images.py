import os
import shutil

def copy_image_files(source_dir, dest_dir, overwrite=False):
    image_extensions = {'.png', '.svg', '.jpg', '.jpeg', '.gif'}
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in image_extensions:
                src_path = os.path.join(root, file)
                relative_path = os.path.relpath(src_path, source_dir)
                dest_path = os.path.join(dest_dir, relative_path)
                
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                if os.path.exists(dest_path):
                    if not overwrite:
                        print(f"Skipped existing file: {dest_path}")
                        continue
                    print(f"Overwriting: {dest_path}")

                shutil.copy2(src_path, dest_path)
                print(f"Copied: {src_path} -> {dest_path}")

if __name__ == "__main__":
    copy_image_files(
        source_dir="for_kb_import_ru/",
        dest_dir="kb.comindware.ru/platform/v5.0",
        overwrite=True
    )