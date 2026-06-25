"""Post-import formatter for related-topic blocks in local Markdown docs.

This root-level helper is for local Markdown cleanup after PHPKB import or
documentation migration. It is not part of the PHPKB cloning DB workflow: it
does not connect to PHPKB, does not use `.mapping.json`, and does not remap
article/category IDs.

Current behavior:
- walks the hardcoded `docs/ru/using_the_system` directory;
- finds sections that start with the related-topics snippet marker:
  `--8<-- "related_topics_heading.md"`;
- wraps the detected related-topic block in
  `<div class="relatedTopics" markdown="block">`;
- converts standalone bold reference links like
  `**[Title][reference]**`
  into italic bullet links like
  `- _[Title][reference]_`;
- rewrites matching Markdown files in place.

The script rewrites files in place. Before broadening it, add CLI arguments
for the root directory and dry-run/write mode, then test the exact block
boundaries on representative Markdown files.
"""

import os
import re

from tools.text_io import open_text_write

# Define the directory to search for markdown files
directory = 'docs/ru/using_the_system'

# Define patterns for identifying the section and transforming the bold links
section_start_pattern = r'(--8<-- "related_topics_heading\.md")'
bold_link_pattern = r'^\*\*(\[[^\]]+\]\[[^\]]+\])\*\*$'
replacement_format = r'- _\1_'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Flags to track if we're in the target section and if modifications occur
    inside_section = False
    modified = False
    output_lines = []

    # Process each line to look for the section start and bold links
    for line in lines:
        # Check for the start of the target section
        if re.match(section_start_pattern, line):
            inside_section = True
            first_new_line_in_section = True
            previous_line_found = False
            output_lines.append('<div class="relatedTopics" markdown="block">\n\n')
            output_lines.append(line)  # Keep the section header as is
            modified = True
            continue
        
        # If inside the section, convert bold links to bullet points
        if inside_section:
            print("inside section")
            if first_new_line_in_section or previous_line_found:
                first_new_line_in_section = False
                previous_line_found = False
                output_lines.append(line)
                print(line)
                continue
            else:
                # Stop processing the section once a non-bold link line is found
                if not re.match(bold_link_pattern, line):
                    inside_section = False
                    output_lines.append('\n</div>\n\n')
                    print(line)
                else:
                    line = re.sub(bold_link_pattern, replacement_format, line.strip())
                    previous_line_found = True
                print(line)
        
        output_lines.append(line)
        

    # If modifications were made, write the updated content back to the file
    if modified:
        with open_text_write(filepath) as file:
            file.writelines(output_lines)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

def main():
    
    # Traverse the directory and process each .md file
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                process_file(filepath)

if __name__ == "__main__":
    main()
