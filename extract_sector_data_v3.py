#!/usr/bin/env python3
import json
import os
import argparse
import subprocess
import sys
from collections import defaultdict
from typing import Dict, List, Any, Optional, Tuple

def check_git_status(path: str) -> bool:
    """Check if there are uncommitted changes in the given path or its parent git repo"""
    # Find the git root directory
    current_path = os.path.abspath(path)
    git_root = None
    
    while current_path != '/':
        if os.path.exists(os.path.join(current_path, '.git')):
            git_root = current_path
            break
        current_path = os.path.dirname(current_path)
    
    if not git_root:
        # Not a git repository, so no changes to check
        return True
    
    try:
        # Check if there are any uncommitted changes in the target path
        if os.path.exists(path):
            # Check for uncommitted changes in the specific path
            result = subprocess.run(
                ['git', '-C', git_root, 'status', '--porcelain', os.path.relpath(path, git_root)],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0 and result.stdout.strip():
                # There are uncommitted changes
                return False
        
        return True
    except subprocess.CalledProcessError:
        # Git command failed, assume it's safe to proceed
        return True
    except FileNotFoundError:
        # Git not installed
        print("Warning: Git not found. Skipping uncommitted changes check.")
        return True

def create_directory(path: str) -> None:
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def clean_name(name: str) -> str:
    """Clean name for use in filenames"""
    return name.replace('/', '-').replace('\\', '-').strip()

def format_tag(tag: Dict[str, Any]) -> str:
    """Format a tag object into markdown"""
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

def format_tags_section(tags: List[Any]) -> str:
    """Format a list of tags into a markdown section"""
    if not tags:
        return ""
    
    sections = ["## Tags", ""]
    
    for tag in tags:
        if isinstance(tag, dict):
            sections.append(format_tag(tag))
        else:
            # Handle case where tag might be just a string
            sections.append(f"- {tag}")
            sections.append("")
    
    return '\n'.join(sections)

def get_location_type_display(loc_type: str) -> str:
    """Convert location type to display format"""
    type_map = {
        'asteroidBase': 'Asteroid Base',
        'asteroidBelt': 'Asteroid Belt',
        'deepSpaceStation': 'Deep Space Station',
        'gasGiantMine': 'Gas Giant Mine',
        'moonBase': 'Moon Base',
        'orbitalRuin': 'Orbital Ruin',
        'refuelingStation': 'Refueling Station',
        'researchBase': 'Research Base',
        'spaceStation': 'Space Station'
    }
    return type_map.get(loc_type, loc_type.replace('_', ' ').title())

def extract_sector_data(json_file: str, sector_name: Optional[str] = None, output_root: str = "sectors", force: bool = False) -> None:
    """Extract sector data from JSON and organize into hierarchical markdown files
    
    Creates structure:
    sectors/[sector-name]/systems/
    └── [system-name]/
        ├── system.md
        ├── [planet-name]/
        │   ├── planet.md
        │   ├── moons/
        │   │   └── [moon-name].md
        │   └── locations/
        │       └── [type]--[name].md
        └── [asteroid-belt-name]/
            ├── belt.md
            └── locations/
                └── [type]--[name].md
    """
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Determine sector name
    if not sector_name:
        if 'sector' in data:
            for sector_id, sector in data['sector'].items():
                sector_name = sector.get('name', 'unknown-sector')
                break
        else:
            sector_name = 'unknown-sector'
    
    # Clean sector name for directory
    sector_dir_name = clean_name(sector_name.lower().replace(' ', '-'))
    
    # Create base directory structure
    base_path = os.path.join(output_root, sector_dir_name)
    systems_path = os.path.join(base_path, 'systems')
    
    # Check for uncommitted changes before proceeding
    if not force and not check_git_status(systems_path):
        print(f"\n❌ ERROR: Uncommitted changes detected in {systems_path}")
        print("\nThis import would overwrite existing files. Please either:")
        print("  1. Commit your changes: git add . && git commit -m 'your message'")
        print("  2. Stash your changes: git stash")
        print("  3. Force the import: python3 extract_sector_data_v3.py <json_file> --force")
        print("\nAborting import to prevent data loss.")
        sys.exit(1)
    
    create_directory(base_path)
    create_directory(systems_path)
    
    # Build lookup tables for entities
    entities_by_id = {}
    
    # First pass: collect all entities
    for entity_type in data:
        if entity_type in ['sector', 'note']:
            continue
        for entity_id, entity in data[entity_type].items():
            entities_by_id[entity_id] = {
                'type': entity_type,
                'data': entity,
                'id': entity_id
            }
    
    # Process systems and their contents
    if 'system' in data:
        for system_id, system in data['system'].items():
            system_name = clean_name(system.get('name', 'Unknown System'))
            system_dir = os.path.join(systems_path, system_name)
            create_directory(system_dir)
            
            # Write system file
            with open(os.path.join(system_dir, 'system.md'), 'w') as f:
                f.write(f"# System: {system.get('name', 'Unknown')}\n\n")
                
                if 'attributes' in system:
                    f.write("## Attributes\n")
                    for key, value in system['attributes'].items():
                        if key == 'tags' and isinstance(value, list):
                            # Handle tags separately
                            continue
                        f.write(f"- **{key.replace('_', ' ').title()}**: {value}\n")
                    f.write("\n")
                    
                    # Format tags if present
                    if 'tags' in system['attributes']:
                        f.write(format_tags_section(system['attributes']['tags']))
                
                # Add navigation section
                f.write("## System Contents\n\n")
                f.write("_Navigate to subdirectories to explore this system_\n")
    
    # Process all entities by their parent relationships
    for entity_id, entity_info in entities_by_id.items():
        entity_type = entity_info['type']
        entity = entity_info['data']
        entity_name = entity.get('name', 'Unknown')
        
        # Find parent path
        parent_id = entity.get('parent')
        parent_type = entity.get('parentEntity')
        
        if not parent_id:
            continue
            
        # Determine where to place this entity
        if parent_type == 'system' and parent_id in data.get('system', {}):
            # Direct child of system
            system_name = clean_name(data['system'][parent_id].get('name', 'Unknown'))
            parent_path = os.path.join(systems_path, system_name)
            
            if entity_type == 'planet':
                # Create planet directory
                planet_dir = os.path.join(parent_path, clean_name(entity_name))
                create_directory(planet_dir)
                
                # Write planet file
                with open(os.path.join(planet_dir, 'planet.md'), 'w') as f:
                    f.write(f"# Planet: {entity_name}\n\n")
                    write_entity_content(f, entity, entity_type)
                    
                # Create subdirectories for planet
                create_directory(os.path.join(planet_dir, 'moons'))
                create_directory(os.path.join(planet_dir, 'locations'))
                
            elif entity_type == 'asteroidBelt':
                # Create asteroid belt directory
                belt_name = f"asteroid-belt--{clean_name(entity_name)}"
                belt_dir = os.path.join(parent_path, belt_name)
                create_directory(belt_dir)
                
                # Write belt file
                with open(os.path.join(belt_dir, 'belt.md'), 'w') as f:
                    f.write(f"# Asteroid Belt: {entity_name}\n\n")
                    write_entity_content(f, entity, entity_type)
                    
                # Create locations subdirectory
                create_directory(os.path.join(belt_dir, 'locations'))
                
            else:
                # Other direct system children (space stations, etc.)
                write_location_file(parent_path, entity_type, entity_name, entity)
                
        elif parent_type == 'planet' and parent_id in data.get('planet', {}):
            # Child of a planet
            planet_name = clean_name(data['planet'][parent_id].get('name', 'Unknown'))
            planet_system_id = data['planet'][parent_id].get('parent')
            
            if planet_system_id and planet_system_id in data.get('system', {}):
                system_name = clean_name(data['system'][planet_system_id].get('name', 'Unknown'))
                planet_path = os.path.join(systems_path, system_name, planet_name)
                
                if entity_type == 'moon':
                    # Write moon file
                    moon_file = os.path.join(planet_path, 'moons', f"{clean_name(entity_name)}.md")
                    create_directory(os.path.dirname(moon_file))
                    with open(moon_file, 'w') as f:
                        f.write(f"# Moon: {entity_name}\n\n")
                        write_entity_content(f, entity, entity_type)
                else:
                    # Location on/around planet
                    write_location_file(planet_path, entity_type, entity_name, entity)
                    
        elif parent_type == 'asteroidBelt' and parent_id in data.get('asteroidBelt', {}):
            # Child of an asteroid belt
            belt_name = data['asteroidBelt'][parent_id].get('name', 'Unknown')
            belt_system_id = data['asteroidBelt'][parent_id].get('parent')
            
            if belt_system_id and belt_system_id in data.get('system', {}):
                system_name = clean_name(data['system'][belt_system_id].get('name', 'Unknown'))
                belt_dir_name = f"asteroid-belt--{clean_name(belt_name)}"
                belt_path = os.path.join(systems_path, system_name, belt_dir_name)
                
                # Location in asteroid belt
                write_location_file(belt_path, entity_type, entity_name, entity)
    
    print(f"\nData extracted successfully!")
    print(f"Created hierarchical structure in: {systems_path}/")
    print(f"\nNote: Remember to update the campaign index files:")
    print(f"  - MASTER-INDEX.md")
    print(f"  - NPC-INDEX.md (if new NPCs were imported)")
    print(f"  - TIMELINE.md (if historical events were imported)")

def write_entity_content(f, entity: Dict[str, Any], entity_type: str) -> None:
    """Write common entity content to file"""
    if 'attributes' in entity:
        f.write("## Attributes\n")
        
        # Handle tags separately
        tags = None
        for key, value in entity['attributes'].items():
            if key == 'tags':
                tags = value
            elif key == 'techLevel':
                f.write(f"- **Tech Level**: {value}\n")
            else:
                f.write(f"- **{key.replace('_', ' ').title()}**: {value}\n")
        f.write("\n")
        
        # Format tags section if present
        if tags:
            f.write(format_tags_section(tags))
    
    # Add navigation helper
    f.write("\n## Navigation\n")
    f.write("- [Back to System](../system.md)\n")

def write_location_file(parent_path: str, loc_type: str, name: str, entity: Dict[str, Any]) -> None:
    """Write a location file in the appropriate directory"""
    locations_dir = os.path.join(parent_path, 'locations')
    create_directory(locations_dir)
    
    # Create filename with type prefix
    filename = f"{loc_type}--{clean_name(name)}.md"
    filepath = os.path.join(locations_dir, filename)
    
    with open(filepath, 'w') as f:
        f.write(f"# {get_location_type_display(loc_type)}: {name}\n\n")
        
        if 'attributes' in entity:
            f.write("## Attributes\n")
            for key, value in entity['attributes'].items():
                f.write(f"- **{key.replace('_', ' ').title()}**: {value}\n")
            f.write("\n")
        
        # Add navigation
        f.write("\n## Navigation\n")
        f.write("- [Back to Parent](../)\n")

def main():
    parser = argparse.ArgumentParser(description='Extract sector data from Sectors Without Number JSON export')
    parser.add_argument('json_file', help='Path to the JSON file to import')
    parser.add_argument('-s', '--sector-name', help='Name of the sector (extracted from JSON if not provided)')
    parser.add_argument('-o', '--output-root', default='sectors', help='Root directory for output (default: sectors)')
    parser.add_argument('-f', '--force', action='store_true', help='Force import even with uncommitted changes')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.json_file):
        print(f"Error: File '{args.json_file}' not found!")
        return
    
    extract_sector_data(args.json_file, args.sector_name, args.output_root, args.force)

if __name__ == "__main__":
    main()