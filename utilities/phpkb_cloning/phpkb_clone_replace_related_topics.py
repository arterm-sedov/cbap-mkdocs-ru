import os
import re

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
        with open(filepath, 'w', encoding='utf-8') as file:
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
