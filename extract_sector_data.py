#!/usr/bin/env python3
"""
Extract Stars Without Number sector data from Sectors Without Number JSON export.

This script creates a hierarchical file structure:
- Systems at the top level
- Planets/asteroids as subdirectories  
- Locations as subdirectories under their parent

All files and directories use kebab-case naming.
"""

import json
import os
import sys
import re
import subprocess
from typing import Dict, List, Any, Tuple, Optional


def clean_name(name: str) -> str:
    """Convert a name to a safe filename in kebab-case"""
    # Remove special characters and convert to lowercase
    name = re.sub(r'[^\w\s-]', '', name.lower())
    # Replace spaces with hyphens
    name = re.sub(r'[-\s]+', '-', name)
    # Remove leading/trailing hyphens
    return name.strip('-')


def create_directory(path: str):
    """Create a directory if it doesn't exist"""
    os.makedirs(path, exist_ok=True)


def format_tag(tag: Dict[str, Any]) -> str:
    """Format a tag object into markdown"""
    sections = []
    sections.append(f"### {tag.get('name', 'Unknown Tag')}")
    sections.append("")
    sections.append(tag.get('description', '_No description available_'))
    sections.append("")
    
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


def check_git_status(path: str) -> bool:
    """Check if there are uncommitted changes in the given path"""
    if not os.path.exists(path):
        return True  # Path doesn't exist yet, safe to proceed
        
    try:
        # Check if we're in a git repository
        result = subprocess.run(['git', 'rev-parse', '--git-dir'], 
                              capture_output=True, text=True, cwd=path)
        if result.returncode != 0:
            return True  # Not a git repo, proceed anyway
        
        # Check for uncommitted changes
        result = subprocess.run(['git', 'status', '--porcelain', path], 
                              capture_output=True, text=True)
        
        if result.stdout.strip():
            return False  # Has uncommitted changes
        return True  # No uncommitted changes
        
    except Exception:
        return True  # On error, proceed anyway


def get_hex_neighbors(x: int, y: int, coordinate_index: Dict[str, Any]) -> Dict[str, Any]:
    """Get neighboring systems in a flat-top hex grid"""
    neighbors = {}
    
    # Flat-top hex neighbor offsets
    # For odd columns (x is odd)
    if x % 2 == 1:
        offsets = [
            ('Northwest', -1, -1),
            ('Northeast', 1, -1),
            ('West', -1, 0),
            ('East', 1, 0),
            ('Southwest', -1, 0),
            ('Southeast', 1, 0)
        ]
    # For even columns (x is even)
    else:
        offsets = [
            ('Northwest', -1, 0),
            ('Northeast', 1, 0),
            ('West', -1, 0),
            ('East', 1, 0),
            ('Southwest', -1, 1),
            ('Southeast', 1, 1)
        ]
    
    for direction, dx, dy in offsets:
        nx, ny = x + dx, y + dy
        hex_coords = f"{nx:02d}{ny:02d}"
        if hex_coords in coordinate_index:
            neighbors[direction] = coordinate_index[hex_coords]
    
    return neighbors


def extract_sector_data(json_file: str, output_root: str = "sectors", 
                       sector_name: Optional[str] = None, force: bool = False):
    """
    Extract sector data from JSON and create markdown files.
    
    Directory structure:
    sectors/[sector-name]/
    └── systems/
        ├── system--[system-name].md
        └── [system-name]/
            ├── planet--[planet-name].md
            ├── [planet-name]/
            │   ├── moons/
            │   │   └── moon--[moon-name].md
            │   └── locations/
            │       └── [type]--[name].md
            └── [asteroid-belt-name]/
                ├── belt--[belt-name].md
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
    sector_dir_name = clean_name(sector_name)
    
    # Create base directory structure
    base_path = os.path.join(output_root, sector_dir_name)
    systems_path = os.path.join(base_path, 'systems')
    
    # Check for uncommitted changes before proceeding
    if not force and not check_git_status(systems_path):
        print(f"\n❌ ERROR: Uncommitted changes detected in {systems_path}")
        print("\nThis import would overwrite existing files. Please either:")
        print("  1. Commit your changes: git add . && git commit -m 'your message'")
        print("  2. Stash your changes: git stash")
        print("  3. Force the import: python3 extract_sector_data_v4.py <json_file> --force")
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
    
    # Process systems and build coordinate index
    systems_processed = 0
    planets_processed = 0
    locations_processed = 0
    coordinate_index = {}  # hex_coords -> system info
    
    for system_id, system in data.get('system', {}).items():
        system_name = system.get('name', 'Unknown System')
        system_dir_name = clean_name(system_name)
        system_file_name = f"system--{system_dir_name}.md"
        system_path = os.path.join(systems_path, system_file_name)
        
        # Extract coordinates (1-indexed in JSON, convert to 0-indexed for display)
        x = system.get('x', 0) - 1
        y = system.get('y', 0) - 1
        hex_coords = f"{x:02d}{y:02d}"
        
        # Add to coordinate index
        coordinate_index[hex_coords] = {
            'name': system_name,
            'path': f"systems/{system_file_name}",
            'x': x,
            'y': y
        }
        
        # Create system directory
        system_dir_path = os.path.join(systems_path, system_dir_name)
        create_directory(system_dir_path)
        
        # Generate system content
        content = [f"# {system_name}"]
        content.append("")
        content.append("## System Information")
        content.append(f"- **Coordinates**: {system.get('x', 0)},{system.get('y', 0)} (1-indexed)")
        content.append(f"- **Hex**: {x:02d},{y:02d} (0-indexed for map)")
        
        # Star information
        primary_star = None
        for star_id in system.get('star', []):
            if star_id in entities_by_id:
                star = entities_by_id[star_id]['data']
                star_name = star.get('name', 'Unknown Star')
                if not primary_star:
                    primary_star = star_name
                    content.append(f"- **Primary Star**: {star_name} ({star.get('classification', 'Unknown')})")
        
        content.append("")
        
        # List celestial bodies
        body_list = []
        
        # Collect all bodies in the system
        for planet_id in system.get('planet', []):
            if planet_id in entities_by_id:
                planet = entities_by_id[planet_id]['data']
                body_list.append(f"- **{planet.get('name', 'Unknown')}** - Planet")
        
        for asteroid_id in system.get('asteroid_belt', []):
            if asteroid_id in entities_by_id:
                belt = entities_by_id[asteroid_id]['data']
                body_list.append(f"- **{belt.get('name', 'Unknown Belt')}** - Asteroid Belt")
        
        for gas_giant_id in system.get('gas_giant_mine', []):
            if gas_giant_id in entities_by_id:
                giant = entities_by_id[gas_giant_id]['data']
                body_list.append(f"- **{giant.get('name', 'Unknown')}** - Gas Giant")
        
        if body_list:
            content.append("## Celestial Bodies")
            content.extend(body_list)
            content.append("")
        
        # Write system file
        with open(system_path, 'w') as f:
            f.write('\n'.join(content))
        
        systems_processed += 1
        
        # Process planets in this system
        for planet_id in system.get('planet', []):
            if planet_id not in entities_by_id:
                continue
                
            planet = entities_by_id[planet_id]['data']
            planet_name = planet.get('name', 'Unknown Planet')
            planet_dir_name = clean_name(planet_name)
            planet_file_name = f"planet--{planet_dir_name}.md"
            
            # Create planet directory
            planet_dir_path = os.path.join(system_dir_path, planet_dir_name)
            create_directory(planet_dir_path)
            
            # Create planet file path
            planet_path = os.path.join(planet_dir_path, planet_file_name)
            
            # Generate planet content
            content = [f"# {planet_name}"]
            content.append("")
            content.append("## Planet Information")
            content.append(f"- **System**: [{system_name}](../system--{system_dir_name}.md)")
            content.append(f"- **Type**: Planet")
            
            # Add attributes
            for attr in ['atmosphere', 'temperature', 'biosphere', 'population', 'tech_level']:
                if attr in planet:
                    display_name = attr.replace('_', ' ').title()
                    content.append(f"- **{display_name}**: {planet[attr]}")
            
            content.append("")
            
            if 'description' in planet:
                content.append("## Description")
                content.append(planet['description'])
                content.append("")
            
            # Process tags
            if 'tags' in planet and planet['tags']:
                content.append("## World Tags")
                content.append("")
                for tag in planet['tags']:
                    content.append(format_tag(tag))
                content.append("")
            
            # Write planet file
            with open(planet_path, 'w') as f:
                f.write('\n'.join(content))
            
            planets_processed += 1
            
            # Create subdirectories for locations
            locations_dir = os.path.join(planet_dir_path, 'locations')
            create_directory(locations_dir)
            
            # Create moons directory if needed
            moons_dir = os.path.join(planet_dir_path, 'moons')
            
            # Process locations on this planet
            for poi_id in planet.get('point_of_interest', []):
                if poi_id not in entities_by_id:
                    continue
                    
                poi = entities_by_id[poi_id]['data']
                poi_name = poi.get('name', 'Unknown Location')
                poi_type = clean_name(poi.get('type', 'location').replace(' ', '-'))
                poi_file_name = f"{poi_type}--{clean_name(poi_name)}.md"
                poi_path = os.path.join(locations_dir, poi_file_name)
                
                # Generate location content
                content = [f"# {poi_name}"]
                content.append("")
                content.append("## Location Information")
                content.append(f"- **Planet**: [{planet_name}](../planet--{planet_dir_name}.md)")
                content.append(f"- **System**: [{system_name}](../../system--{system_dir_name}.md)")
                content.append(f"- **Type**: {poi.get('type', 'Unknown Type')}")
                
                if 'description' in poi:
                    content.append("")
                    content.append("## Description")
                    content.append(poi['description'])
                
                # Write location file
                with open(poi_path, 'w') as f:
                    f.write('\n'.join(content))
                
                locations_processed += 1
        
        # Process asteroid belts in this system
        for belt_id in system.get('asteroid_belt', []):
            if belt_id not in entities_by_id:
                continue
                
            belt = entities_by_id[belt_id]['data']
            belt_name = belt.get('name', 'Unknown Belt')
            belt_dir_name = clean_name(belt_name)
            belt_file_name = f"belt--{belt_dir_name}.md"
            
            # Create belt directory
            belt_dir_path = os.path.join(system_dir_path, belt_dir_name)
            create_directory(belt_dir_path)
            
            # Create belt file
            belt_path = os.path.join(belt_dir_path, belt_file_name)
            
            # Generate belt content
            content = [f"# {belt_name}"]
            content.append("")
            content.append("## Belt Information")
            content.append(f"- **System**: [{system_name}](../system--{system_dir_name}.md)")
            content.append(f"- **Type**: Asteroid Belt")
            
            if 'description' in belt:
                content.append("")
                content.append("## Description")
                content.append(belt['description'])
            
            # Process tags if any
            if 'tags' in belt and belt['tags']:
                content.append("")
                content.append("## Tags")
                content.append("")
                for tag in belt['tags']:
                    content.append(format_tag(tag))
            
            # Write belt file
            with open(belt_path, 'w') as f:
                f.write('\n'.join(content))
            
            # Create locations directory for belt
            locations_dir = os.path.join(belt_dir_path, 'locations')
            create_directory(locations_dir)
            
            # Process locations in this belt
            for poi_id in belt.get('point_of_interest', []):
                if poi_id not in entities_by_id:
                    continue
                    
                poi = entities_by_id[poi_id]['data']
                poi_name = poi.get('name', 'Unknown Location')
                poi_type = clean_name(poi.get('type', 'location').replace(' ', '-'))
                poi_file_name = f"{poi_type}--{clean_name(poi_name)}.md"
                poi_path = os.path.join(locations_dir, poi_file_name)
                
                # Generate location content
                content = [f"# {poi_name}"]
                content.append("")
                content.append("## Location Information")
                content.append(f"- **Belt**: [{belt_name}](../belt--{belt_dir_name}.md)")
                content.append(f"- **System**: [{system_name}](../../system--{system_dir_name}.md)")
                content.append(f"- **Type**: {poi.get('type', 'Unknown Type')}")
                
                if 'description' in poi:
                    content.append("")
                    content.append("## Description")
                    content.append(poi['description'])
                
                # Write location file
                with open(poi_path, 'w') as f:
                    f.write('\n'.join(content))
                
                locations_processed += 1
    
    # Generate coordinate index file
    generate_coordinate_index(base_path, coordinate_index)
    
    print(f"\n✅ Import complete!")
    print(f"   - Systems: {systems_processed}")
    print(f"   - Planets: {planets_processed}")
    print(f"   - Locations: {locations_processed}")
    print(f"   - Output: {base_path}/")


def generate_coordinate_index(base_path: str, coordinate_index: Dict[str, Any]):
    """Generate the systems coordinate index with hex grid visualization"""
    index_path = os.path.join(base_path, 'systems-coordinate-index.md')
    
    # Find bounds of the sector
    if not coordinate_index:
        return
        
    min_x = min(info['x'] for info in coordinate_index.values())
    max_x = max(info['x'] for info in coordinate_index.values())
    min_y = min(info['y'] for info in coordinate_index.values())
    max_y = max(info['y'] for info in coordinate_index.values())
    
    content = ["# Systems Coordinate Index"]
    content.append("")
    content.append("## Navigation")
    content.append("This sector uses a flat-top hexagonal grid. Each system has 6 neighbors.")
    content.append("")
    content.append("## Travel Times")
    content.append("- **Base**: 6 days per hex")
    content.append("- **Drive-1**: 6 days")
    content.append("- **Drive-2**: 3 days")
    content.append("- **Drive-3**: 2 days")
    content.append("- **Drive-4**: 1.5 days")
    content.append("")
    
    # Generate hex grid visualization
    content.append("## Sector Map (0-indexed)")
    content.append("```")
    content.append(f"   {'  '.join(f'{x:02d}' for x in range(min_x, max_x + 1))}")
    
    for y in range(min_y, max_y + 1):
        row = f"{y:02d} "
        for x in range(min_x, max_x + 1):
            hex_coords = f"{x:02d}{y:02d}"
            if hex_coords in coordinate_index:
                # Use first two letters of system name
                name = coordinate_index[hex_coords]['name']
                row += f"{name[:2].upper()} "
            else:
                row += "-- "
        content.append(row)
    
    content.append("```")
    content.append("")
    
    # Generate coordinate-to-system mapping
    content.append("## Coordinate Reference")
    content.append("")
    content.append("| Hex | Coordinates | System | Path |")
    content.append("|-----|-------------|--------|------|")
    
    for hex_coords in sorted(coordinate_index.keys()):
        info = coordinate_index[hex_coords]
        x, y = info['x'], info['y']
        content.append(f"| {x:02d},{y:02d} | {x+1},{y+1} | {info['name']} | [{info['name']}]({info['path']}) |")
    
    content.append("")
    
    # Generate system neighbor reference
    content.append("## System Neighbors")
    content.append("")
    
    for hex_coords in sorted(coordinate_index.keys()):
        info = coordinate_index[hex_coords]
        neighbors = get_hex_neighbors(info['x'], info['y'], coordinate_index)
        
        if neighbors:
            content.append(f"### {info['name']}")
            for direction, neighbor in neighbors.items():
                content.append(f"- {direction}: [{neighbor['name']}]({neighbor['path']})")
            content.append("")
    
    # Write index file
    with open(index_path, 'w') as f:
        f.write('\n'.join(content))
    
    print(f"   - Coordinate index: {index_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 extract_sector_data_v4.py <json_file> [--force]")
        sys.exit(1)
    
    json_file = sys.argv[1]
    force = '--force' in sys.argv
    
    if not os.path.exists(json_file):
        print(f"Error: File '{json_file}' not found")
        sys.exit(1)
    
    extract_sector_data(json_file, force=force)