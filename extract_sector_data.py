#!/usr/bin/env python3
import json
import os
from collections import defaultdict

def create_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def clean_name(name):
    """Clean name for use in filenames"""
    return name.replace('/', '-').replace('\\', '-').strip()

def extract_sector_data(json_file):
    """Extract sector data from JSON and organize into markdown files"""
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Create main directories
    create_directory('sector-data')
    create_directory('sector-data/systems')
    create_directory('sector-data/planets')
    create_directory('sector-data/factions')
    create_directory('sector-data/locations')
    create_directory('sector-data/npcs')
    
    # Track relationships
    system_contents = defaultdict(list)
    planet_contents = defaultdict(list)
    
    # Process sector overview
    if 'sector' in data:
        for sector_id, sector in data['sector'].items():
            with open('sector-data/sector-overview.md', 'w') as f:
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
            filename = f"sector-data/systems/{clean_name(name)}.md"
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
            filename = f"sector-data/planets/{clean_name(name)}.md"
            planets_index.append((name, filename))
            
            # Track for system contents
            system_contents[parent_system].append(f"- Planet: [{name}](../../planets/{clean_name(name)}.md)")
            
            with open(filename, 'w') as f:
                f.write(f"# Planet: {name}\n\n")
                f.write(f"**System**: {parent_system}\n\n")
                
                if 'attributes' in planet:
                    f.write("## Attributes\n")
                    for key, value in planet['attributes'].items():
                        f.write(f"- **{key.replace('_', ' ').title()}**: {value}\n")
                    f.write("\n")
                
                if 'tags' in planet:
                    f.write("## Tags\n")
                    for tag in planet['tags']:
                        f.write(f"- {tag}\n")
                    f.write("\n")
    
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
                
                filename = f"sector-data/locations/{clean_name(name)}.md"
                locations_index.append((name, loc_type, filename))
                
                # Track for parent contents
                if parent_type == 'system':
                    system_contents[parent].append(f"- {loc_type.title()}: [{name}](../../locations/{clean_name(name)}.md)")
                elif parent_type == 'planet':
                    planet_contents[parent].append(f"- {loc_type.title()}: [{name}](../../locations/{clean_name(name)}.md)")
                elif parent_type == 'asteroidBelt':
                    # Find the asteroid belt's parent system
                    if 'asteroidBelt' in data and parent in data['asteroidBelt']:
                        belt_parent = data['asteroidBelt'][parent].get('parent', 'Unknown')
                        system_contents[belt_parent].append(f"  - {loc_type.title()}: [{name}](../../locations/{clean_name(name)}.md)")
                
                with open(filename, 'w') as f:
                    f.write(f"# {loc_type.replace('_', ' ').title()}: {name}\n\n")
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
            filename = f"sector-data/systems/{clean_name(name)}.md"
            
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
            filename = f"sector-data/planets/{clean_name(name)}.md"
            
            contents_list = planet_contents.get(planet_id, [])
            if contents_list:
                with open(filename, 'a') as f:
                    f.write("## Planet Contents\n")
                    for item in contents_list:
                        f.write(f"{item}\n")
                    f.write("\n")
    
    # Create index files
    with open('sector-data/index.md', 'w') as f:
        f.write("# Sector Data Index\n\n")
        f.write("## Navigation\n")
        f.write("- [Sector Overview](sector-overview.md)\n")
        f.write("- [Systems](systems-index.md)\n")
        f.write("- [Planets](planets-index.md)\n")
        f.write("- [Locations](locations-index.md)\n")
        f.write("- [Quick Reference](quick-reference.md)\n")
    
    # Create systems index
    if systems_index:
        with open('sector-data/systems-index.md', 'w') as f:
            f.write("# Systems Index\n\n")
            for name, path in sorted(systems_index):
                f.write(f"- [{name}]({path.replace('sector-data/', '')})\n")
    
    # Create planets index
    if planets_index:
        with open('sector-data/planets-index.md', 'w') as f:
            f.write("# Planets Index\n\n")
            for name, path in sorted(planets_index):
                f.write(f"- [{name}]({path.replace('sector-data/', '')})\n")
    
    # Create locations index
    if locations_index:
        with open('sector-data/locations-index.md', 'w') as f:
            f.write("# Locations Index\n\n")
            by_type = defaultdict(list)
            for name, loc_type, path in locations_index:
                by_type[loc_type].append((name, path))
            
            for loc_type, items in sorted(by_type.items()):
                f.write(f"\n## {loc_type.replace('_', ' ').title()}\n")
                for name, path in sorted(items):
                    f.write(f"- [{name}]({path.replace('sector-data/', '')})\n")
    
    # Create quick reference with plot hooks
    with open('sector-data/quick-reference.md', 'w') as f:
        f.write("# Quick Reference - Plot Hooks & Situations\n\n")
        
        # Collect all situations and interesting attributes
        situations = []
        
        for entity_type in data:
            if entity_type in ['sector', 'note', 'blackHole']:
                continue
            for entity_id, entity in data[entity_type].items():
                if 'attributes' in entity and 'situation' in entity['attributes']:
                    name = entity.get('name', 'Unknown')
                    situation = entity['attributes']['situation']
                    situations.append(f"- **{name}** ({entity_type}): {situation}")
        
        if situations:
            f.write("## Current Situations\n")
            for situation in sorted(situations):
                f.write(f"{situation}\n")
    
    print(f"Data extracted successfully!")
    print(f"Created directories: sector-data/")
    print(f"  - systems/")
    print(f"  - planets/")
    print(f"  - locations/")

if __name__ == "__main__":
    extract_sector_data("Abiha Omicron - June 12, 2025.json")