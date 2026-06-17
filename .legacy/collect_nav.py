import os
import yaml

def load_pages_file(file_path):
    """Load and parse a '.pages' file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = yaml.safe_load(file)
    title = content.get('title')
    nav = content.get('nav', [])
    return title, nav

def add_relative_path(current_path, entry):
    """Generate relative path for navigation entries."""
    return os.path.join(current_path, entry).replace('\\', '/')

def contains_md_files(folder_path):
    """Check if a folder contains any '.md' files or subfolders with '.md' files."""
    for root, dirs, files in os.walk(folder_path):
        if 'img' in dirs:
            dirs.remove('img')  # Ignore 'img' directories
        for file in files:
            if file.endswith('.md'):
                return True
    return False

def collect_navigation_structure(root_dir, current_path=''):
    """Recursively collect the navigation structure, respecting '.pages' files if present."""
    folder_path = os.path.join(root_dir, current_path)
    nav_structure = []

    # Check if a '.pages' file exists in the current folder
    pages_file = os.path.join(folder_path, '.pages')
    remaining_files = set(os.listdir(folder_path))

    if os.path.isfile(pages_file):
        title, nav_entries = load_pages_file(pages_file)
        sub_nav = []

        # Process items in the '.pages' 'nav' list
        for entry in nav_entries:
            if isinstance(entry, dict):  # Handle entries with titles
                for key, value in entry.items():
                    if isinstance(value, list):
                        sub_nav_items = []
                        # Process each item in the list
                        for sub_entry in value:
                            if isinstance(sub_entry, str) and not sub_entry.endswith('...'):
                                item_path = os.path.join(folder_path, sub_entry)
                                if os.path.isdir(item_path) and not sub_entry.startswith('.') and sub_entry != '.snippets' and contains_md_files(item_path):
                                    sub_nav_items.extend(collect_navigation_structure(root_dir, os.path.join(current_path, sub_entry)))
                                else:
                                    sub_nav_items.append(add_relative_path(current_path, sub_entry))
                                remaining_files.discard(sub_entry)

                        if key and sub_nav_items:
                            sub_nav.append({key: sub_nav_items})  # Use title with colon if provided
                        elif key:  # Add key without empty list if no items
                            sub_nav.append(key + ':')
                        else:
                            sub_nav.extend(sub_nav_items)  # Append sub_nav directly
            elif isinstance(entry, str):  # If the entry is a simple string
                if not entry.endswith('...'):
                    item_path = os.path.join(folder_path, entry)
                    if os.path.isdir(item_path) and not entry.startswith('.') and entry != '.snippets' and contains_md_files(item_path):
                        sub_nav.extend(collect_navigation_structure(root_dir, os.path.join(current_path, entry)))
                    else:
                        sub_nav.append(add_relative_path(current_path, entry))
                    remaining_files.discard(entry)

        # Append sub_nav to the nav_structure, using the folder title directly if provided
        if title:
            if sub_nav:
                nav_structure.append({title: sub_nav})
            else:
                nav_structure.append(title)
        else:
            nav_structure.extend(sub_nav)

    # First, list all remaining implicit .md files (not in .pages)
    md_files = sorted([item for item in remaining_files if item.endswith('.md') and not item.startswith('.')])
    nav_structure.extend(add_relative_path(current_path, md_file) for md_file in md_files)

    # Then, list all remaining folders
    for item in sorted(remaining_files):
        if item.endswith('.md') or item.startswith('.') or item == '.snippets':
            continue

        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            sub_nav = collect_navigation_structure(root_dir, os.path.join(current_path, item))
            if sub_nav:
                nav_structure.append({item: sub_nav})

    return nav_structure

def build_nav_dict(nav_structure):
    """Create root dictionary structure for mkdocs.yml navigation."""
    nav_dict = {'nav': nav_structure}
    return nav_dict

# Custom YAML Dumper to avoid anchors and aliases
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

# Entry point for creating the navigation structure
root_dir = 'docs/ru'  # Default root directory
nav_structure = collect_navigation_structure(root_dir)
mkdocs_nav = build_nav_dict(nav_structure)

# Write the navigation structure to a YAML file without anchors/aliases
output_file = 'collected_nav.yml'
with open(output_file, 'w', encoding='utf-8') as f:
    yaml.dump(mkdocs_nav, f, allow_unicode=True, default_flow_style=False, sort_keys=False, Dumper=NoAliasDumper)

print(f"Navigation structure saved to {output_file}")
