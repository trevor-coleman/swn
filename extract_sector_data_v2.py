#!/usr/bin/env python3
import json
import os
import argparse
import subprocess
import sys
from collections import defaultdict
from typing import Dict, List, Any, Optional

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
        # First, check if the path exists and has tracked files
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

def resolve_system_name(system_id: str, systems_data: Dict[str, Any]) -> str:
    """Resolve system ID to system name"""
    if system_id in systems_data:
        return systems_data[system_id].get('name', system_id)
    return system_id

def extract_sector_data(json_file: str, sector_name: Optional[str] = None, output_root: str = "sectors", force: bool = False) -> None:
    """Extract sector data from JSON and organize into markdown files
    
    Creates structure:
    sectors/[sector-name]/
    ├── systems/
    ├── planets/
    ├── locations/
    └── factions/
    """
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Determine sector name
    if not sector_name:
        # Try to extract from sector data
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
    
    # Check for uncommitted changes before proceeding
    if not force and not check_git_status(base_path):
        print(f"\n❌ ERROR: Uncommitted changes detected in {base_path}")
        print("\nThis import would overwrite existing files. Please either:")
        print("  1. Commit your changes: git add . && git commit -m 'your message'")
        print("  2. Stash your changes: git stash")
        print("  3. Force the import: python3 extract_sector_data_v2.py <json_file> --force")
        print("\nAborting import to prevent data loss.")
        sys.exit(1)
    
    create_directory(base_path)
    create_directory(os.path.join(base_path, 'systems'))
    create_directory(os.path.join(base_path, 'planets'))
    create_directory(os.path.join(base_path, 'locations'))
    
    # Track relationships
    system_contents = defaultdict(list)
    planet_contents = defaultdict(list)
    
    # Build systems lookup for name resolution
    systems_lookup = {}
    if 'system' in data:
        systems_lookup = data['system']
    
    # Process sector overview
    if 'sector' in data:
        for sector_id, sector in data['sector'].items():
            with open(os.path.join(base_path, 'sector-overview.md'), 'w') as f:
                f.write(f"# Sector: {sector.get('name', 'Unknown')}\n\n")
                if 'attributes' in sector:
                    f.write("## Attributes\n")
                    for key, value in sector['attributes'].items():
                        f.write(f"- **{key.replace('_', ' ').title()}**: {value}\n")
                f.write("\n")
    
    # Process systems
    if 'system' in data:
        systems_index = []
        for system_id, system in data['system'].items():
            name = system.get('name', 'Unknown System')
            filename = os.path.join(base_path, 'systems', f"{clean_name(name)}.md")
            systems_index.append((name, filename))
            
            with open(filename, 'w') as f:
                f.write(f"# System: {name}\n\n")
                f.write(f"**ID**: {system_id}\n\n")
                
                if 'attributes' in system:
                    f.write("## Attributes\n")
                    for key, value in system['attributes'].items():
                        f.write(f"- **{key.replace('_', ' ').title()}**: {value}\n")
                    f.write("\n")
                
                # We'll add contents later
                f.write("## System Contents\n")
                f.write("_Contents will be listed below_\n\n")
    
    # Process planets
    if 'planet' in data:
        planets_index = []
        for planet_id, planet in data['planet'].items():
            name = planet.get('name', 'Unknown Planet')
            parent_system = planet.get('parent', 'Unknown')
            parent_system_name = resolve_system_name(parent_system, systems_lookup)
            filename = os.path.join(base_path, 'planets', f"{clean_name(name)}.md")
            planets_index.append((name, filename))
            
            # Track for system contents
            system_contents[parent_system].append(f"- Planet: [{name}](../planets/{clean_name(name)}.md)")
            
            with open(filename, 'w') as f:
                f.write(f"# Planet: {name}\n\n")
                f.write(f"**System**: [{parent_system_name}](../systems/{clean_name(parent_system_name)}.md)\n\n")
                
                if 'attributes' in planet:
                    f.write("## Attributes\n")
                    
                    # Handle tags separately
                    tags = None
                    for key, value in planet['attributes'].items():
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
    
    # Process moons
    if 'moon' in data:
        for moon_id, moon in data['moon'].items():
            name = moon.get('name', 'Unknown Moon')
            parent_planet = moon.get('parent', 'Unknown')
            planet_contents[parent_planet].append(f"- Moon: {name}")
    
    # Process space stations
    if 'spaceStation' in data:
        for station_id, station in data['spaceStation'].items():
            name = station.get('name', 'Unknown Station')
            parent = station.get('parent', 'Unknown')
            parent_type = station.get('parentEntity', 'unknown')
            
            if parent_type == 'system':
                system_contents[parent].append(f"- Space Station: {name}")
            elif parent_type == 'planet':
                planet_contents[parent].append(f"- Space Station: {name}")
    
    # Process other locations
    location_types = ['asteroidBelt', 'asteroidBase', 'deepSpaceStation', 'gasGiantMine', 
                     'moonBase', 'orbitalRuin', 'refuelingStation', 'researchBase']
    
    locations_index = []
    for loc_type in location_types:
        if loc_type in data:
            for loc_id, location in data[loc_type].items():
                name = location.get('name', f'Unknown {loc_type}')
                parent = location.get('parent', 'Unknown')
                parent_type = location.get('parentEntity', 'unknown')
                
                filename = os.path.join(base_path, 'locations', f"{clean_name(name)}.md")
                locations_index.append((name, loc_type, filename))
                
                # Track for parent contents
                if parent_type == 'system':
                    system_contents[parent].append(f"- {loc_type.replace('_', ' ').title()}: [{name}](../locations/{clean_name(name)}.md)")
                elif parent_type == 'planet':
                    planet_contents[parent].append(f"- {loc_type.replace('_', ' ').title()}: [{name}](../locations/{clean_name(name)}.md)")
                elif parent_type == 'asteroidBelt':
                    # Find the asteroid belt's parent system
                    if 'asteroidBelt' in data and parent in data['asteroidBelt']:
                        belt_parent = data['asteroidBelt'][parent].get('parent', 'Unknown')
                        system_contents[belt_parent].append(f"  - {loc_type.replace('_', ' ').title()}: [{name}](../locations/{clean_name(name)}.md)")
                
                with open(filename, 'w') as f:
                    f.write(f"# {loc_type.replace('_', ' ').title()}: {name}\n\n")
                    
                    # Resolve parent name if it's a system
                    if parent_type == 'system':
                        parent_name = resolve_system_name(parent, systems_lookup)
                        f.write(f"**Parent System**: [{parent_name}](../systems/{clean_name(parent_name)}.md)\n\n")
                    else:
                        f.write(f"**Parent**: {parent}\n\n")
                    
                    if 'attributes' in location:
                        f.write("## Attributes\n")
                        for key, value in location['attributes'].items():
                            f.write(f"- **{key.replace('_', ' ').title()}**: {value}\n")
                        f.write("\n")
    
    # Update system files with contents
    if 'system' in data:
        for system_id, system in data['system'].items():
            name = system.get('name', 'Unknown System')
            filename = os.path.join(base_path, 'systems', f"{clean_name(name)}.md")
            
            # Read existing content
            with open(filename, 'r') as f:
                content = f.read()
            
            # Replace the placeholder with actual contents
            contents_list = system_contents.get(system_id, [])
            if contents_list:
                contents_str = '\n'.join(contents_list)
                content = content.replace("_Contents will be listed below_", contents_str)
            else:
                content = content.replace("_Contents will be listed below_", "_No registered contents_")
            
            # Write back
            with open(filename, 'w') as f:
                f.write(content)
    
    # Update planet files with contents
    if 'planet' in data:
        for planet_id, planet in data['planet'].items():
            name = planet.get('name', 'Unknown Planet')
            filename = os.path.join(base_path, 'planets', f"{clean_name(name)}.md")
            
            contents_list = planet_contents.get(planet_id, [])
            if contents_list:
                with open(filename, 'a') as f:
                    f.write("## Planet Contents\n")
                    for item in contents_list:
                        f.write(f"{item}\n")
                    f.write("\n")
    
    print(f"\nData extracted successfully!")
    print(f"Created sector data in: {base_path}/")
    print(f"  - systems/")
    print(f"  - planets/")
    print(f"  - locations/")
    print(f"\nNote: Remember to update the campaign index files:")
    print(f"  - MASTER-INDEX.md")
    print(f"  - NPC-INDEX.md (if new NPCs were imported)")
    print(f"  - TIMELINE.md (if historical events were imported)")

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