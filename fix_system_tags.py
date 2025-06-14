#!/usr/bin/env python3
"""Quick script to fix tags in system files"""
import os
import glob
import re
import ast

def format_tag(tag):
    """Format a tag object into markdown"""
    if isinstance(tag, str):
        return f"- {tag}\n"
    
    sections = []
    
    # Tag name and description
    sections.append(f"### {tag.get('name', 'Unknown Tag')}")
    sections.append("")
    sections.append(tag.get('description', '_No description available_'))
    sections.append("")
    
    # Format each list section
    tag_lists = [
        ('enemies', 'Enemies'),
        ('friends', 'Friends'),
        ('complications', 'Complications'),
        ('things', 'Things'),
        ('places', 'Places')
    ]
    
    for field_name, display_name in tag_lists:
        if field_name in tag and tag[field_name]:
            sections.append(f"**{display_name}:**")
            for item in tag[field_name]:
                sections.append(f"- {item}")
            sections.append("")
    
    return '\n'.join(sections)

def fix_tags_in_file(filepath):
    """Fix tags in a single file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Look for tags line with raw Python dict
    pattern = r'- \*\*Tags\*\*: \[(.*?)\]\n'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        try:
            # Extract and parse the tags
            tags_str = '[' + match.group(1) + ']'
            # Safely evaluate the Python literal
            tags = ast.literal_eval(tags_str)
            
            # Format tags properly
            tags_section = "## Tags\n\n"
            for tag in tags:
                tags_section += format_tag(tag) + "\n"
            
            # Replace the line with a proper tags section
            new_content = content[:match.start()]
            # Remove the tags from attributes section
            remaining_content = content[match.end():]
            # Find end of attributes section
            next_section = remaining_content.find('\n##')
            if next_section != -1:
                new_content += remaining_content[:next_section] + '\n' + tags_section + remaining_content[next_section:]
            else:
                new_content += remaining_content + '\n' + tags_section
            
            # Write back
            with open(filepath, 'w') as f:
                f.write(new_content)
            
            print(f"Fixed: {filepath}")
            return True
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            return False
    
    return False

def main():
    # Fix all system files
    system_files = glob.glob('sectors/abiha-omicron/sector-data/systems/*.md')
    
    fixed_count = 0
    for filepath in system_files:
        if fix_tags_in_file(filepath):
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} files")

if __name__ == "__main__":
    main()