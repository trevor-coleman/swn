#!/usr/bin/env bun
/**
 * Extract Stars Without Number sector data from Sectors Without Number JSON export.
 *
 * This script creates a hierarchical file structure:
 * - Systems at the top level
 * - Planets/asteroids as subdirectories  
 * - Locations as subdirectories under their parent
 *
 * All files and directories use kebab-case naming.
 */

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';
import { join } from 'path';
import { execSync } from 'child_process';
import type { 
  SectorData, 
  Entity, 
  System, 
  Planet, 
  AsteroidBelt,
  Tag,
  Location
} from './sector-types';

/**
 * Convert a name to a safe filename in kebab-case
 */
function cleanName(name: string): string {
  // Remove special characters and convert to lowercase
  let cleaned = name.toLowerCase().replace(/[^\w\s-]/g, '');
  // Replace spaces with hyphens
  cleaned = cleaned.replace(/[-\s]+/g, '-');
  // Remove leading/trailing hyphens
  return cleaned.replace(/^-+|-+$/g, '');
}

/**
 * Create a directory if it doesn't exist
 */
function createDirectory(path: string): void {
  mkdirSync(path, { recursive: true });
}

/**
 * Format a tag object into markdown
 */
function formatTag(tag: Tag): string {
  const sections: string[] = [];
  sections.push(`### ${tag.name || 'Unknown Tag'}`);
  sections.push('');
  sections.push(tag.description || '_No description available_');
  sections.push('');
  
  const tagLists: Array<[keyof Tag, string]> = [
    ['enemies', 'Enemies'],
    ['friends', 'Friends'],
    ['complications', 'Complications'],
    ['things', 'Things'],
    ['places', 'Places']
  ];
  
  for (const [fieldName, displayName] of tagLists) {
    const field = tag[fieldName];
    if (Array.isArray(field) && field.length > 0) {
      sections.push(`**${displayName}:**`);
      for (const item of field) {
        sections.push(`- ${item}`);
      }
      sections.push('');
    }
  }
  
  return sections.join('\n');
}

/**
 * Check if there are uncommitted changes in the given path
 */
function checkGitStatus(path: string): boolean {
  if (!existsSync(path)) {
    return true; // Path doesn't exist yet, safe to proceed
  }
  
  try {
    // Check if we're in a git repository
    try {
      execSync('git rev-parse --git-dir', { cwd: path });
    } catch {
      return true; // Not a git repo, proceed anyway
    }
    
    // Check for uncommitted changes
    const result = execSync(`git status --porcelain ${path}`, { encoding: 'utf8' });
    
    if (result.trim()) {
      return false; // Has uncommitted changes
    }
    return true; // No uncommitted changes
  } catch {
    return true; // On error, proceed anyway
  }
}

interface CoordinateInfo {
  name: string;
  path: string;
  x: number;
  y: number;
}

/**
 * Get neighboring systems in a flat-top hex grid
 */
function getHexNeighbors(x: number, y: number, coordinateIndex: Record<string, CoordinateInfo>): Record<string, CoordinateInfo> {
  const neighbors: Record<string, CoordinateInfo> = {};
  
  // Flat-top hex neighbor offsets
  let offsets: Array<[string, number, number]>;
  
  // For odd columns (x is odd)
  if (x % 2 === 1) {
    offsets = [
      ['Northwest', -1, -1],
      ['Northeast', 1, -1],
      ['West', -1, 0],
      ['East', 1, 0],
      ['Southwest', -1, 0],
      ['Southeast', 1, 0]
    ];
  } else {
    // For even columns (x is even)
    offsets = [
      ['Northwest', -1, 0],
      ['Northeast', 1, 0],
      ['West', -1, 0],
      ['East', 1, 0],
      ['Southwest', -1, 1],
      ['Southeast', 1, 1]
    ];
  }
  
  for (const [direction, dx, dy] of offsets) {
    const nx = x + dx;
    const ny = y + dy;
    const hexCoords = `${nx.toString().padStart(2, '0')}${ny.toString().padStart(2, '0')}`;
    if (hexCoords in coordinateIndex) {
      neighbors[direction] = coordinateIndex[hexCoords];
    }
  }
  
  return neighbors;
}

interface EntityInfo {
  type: keyof SectorData;
  data: Entity;
  id: string;
}

interface ChildInfo {
  type: keyof SectorData;
  id: string;
  data: Entity;
}

/**
 * Generate the systems coordinate index with hex grid visualization
 */
function generateCoordinateIndex(basePath: string, coordinateIndex: Record<string, CoordinateInfo>): void {
  const indexPath = join(basePath, 'systems-coordinate-index.md');
  
  // Find bounds of the sector
  if (Object.keys(coordinateIndex).length === 0) {
    return;
  }
  
  const coords = Object.values(coordinateIndex);
  const minX = Math.min(...coords.map(c => c.x));
  const maxX = Math.max(...coords.map(c => c.x));
  const minY = Math.min(...coords.map(c => c.y));
  const maxY = Math.max(...coords.map(c => c.y));
  
  const content: string[] = ['# Systems Coordinate Index'];
  content.push('');
  content.push('## Navigation');
  content.push('This sector uses a flat-top hexagonal grid. Each system has 6 neighbors.');
  content.push('');
  content.push('## Travel Times');
  content.push('- **Base**: 6 days per hex');
  content.push('- **Drive-1**: 6 days');
  content.push('- **Drive-2**: 3 days');
  content.push('- **Drive-3**: 2 days');
  content.push('- **Drive-4**: 1.5 days');
  content.push('');
  
  // Generate hex grid visualization
  content.push('## Sector Map (0-indexed)');
  content.push('```');
  const headerRow = Array.from({ length: maxX - minX + 1 }, (_, i) => 
    (minX + i).toString().padStart(2, '0')
  ).join('  ');
  content.push(`   ${headerRow}`);
  
  for (let y = minY; y <= maxY; y++) {
    let row = `${y.toString().padStart(2, '0')} `;
    for (let x = minX; x <= maxX; x++) {
      const hexCoords = `${x.toString().padStart(2, '0')}${y.toString().padStart(2, '0')}`;
      if (hexCoords in coordinateIndex) {
        // Use first two letters of system name
        const name = coordinateIndex[hexCoords].name;
        row += `${name.substring(0, 2).toUpperCase()} `;
      } else {
        row += '-- ';
      }
    }
    content.push(row);
  }
  
  content.push('```');
  content.push('');
  
  // Generate coordinate-to-system mapping
  content.push('## Coordinate Reference');
  content.push('');
  content.push('| Hex | Coordinates | System | Path |');
  content.push('|-----|-------------|--------|------|');
  
  for (const hexCoords of Object.keys(coordinateIndex).sort()) {
    const info = coordinateIndex[hexCoords];
    const { x, y } = info;
    content.push(`| ${x.toString().padStart(2, '0')},${y.toString().padStart(2, '0')} | ${x+1},${y+1} | ${info.name} | [${info.name}](${info.path}) |`);
  }
  
  content.push('');
  
  // Generate system neighbor reference
  content.push('## System Neighbors');
  content.push('');
  
  for (const hexCoords of Object.keys(coordinateIndex).sort()) {
    const info = coordinateIndex[hexCoords];
    const neighbors = getHexNeighbors(info.x, info.y, coordinateIndex);
    
    if (Object.keys(neighbors).length > 0) {
      content.push(`### ${info.name}`);
      for (const [direction, neighbor] of Object.entries(neighbors)) {
        content.push(`- ${direction}: [${neighbor.name}](${neighbor.path})`);
      }
      content.push('');
    }
  }
  
  // Write index file
  writeFileSync(indexPath, content.join('\n'));
  
  console.log(`   - Coordinate index: ${indexPath}`);
}

/**
 * Extract sector data from JSON and create markdown files.
 * 
 * Directory structure:
 * sectors/[sector-name]/
 * └── systems/
 *     ├── system--[system-name].md
 *     └── [system-name]/
 *         ├── planet--[planet-name].md
 *         ├── [planet-name]/
 *         │   ├── moons/
 *         │   │   └── moon--[moon-name].md
 *         │   └── locations/
 *         │       └── [type]--[name].md
 *         └── [asteroid-belt-name]/
 *             ├── belt--[belt-name].md
 *             └── locations/
 *                 └── [type]--[name].md
 */
function extractSectorData(
  jsonFile: string, 
  outputRoot = 'sectors',
  sectorName?: string,
  force = false
): void {
  const jsonContent = readFileSync(jsonFile, 'utf8');
  const data = JSON.parse(jsonContent) as SectorData;
  
  // Determine sector name
  if (!sectorName) {
    if ('sector' in data && Object.keys(data.sector).length > 0) {
      const firstSector = Object.values(data.sector)[0];
      sectorName = firstSector.name || 'unknown-sector';
    } else {
      sectorName = 'unknown-sector';
    }
  }
  
  // Clean sector name for directory
  const sectorDirName = cleanName(sectorName);
  
  // Create base directory structure
  const basePath = join(outputRoot, sectorDirName);
  const systemsPath = join(basePath, 'systems');
  
  // Check for uncommitted changes before proceeding
  if (!force && !checkGitStatus(systemsPath)) {
    console.error(`\n❌ ERROR: Uncommitted changes detected in ${systemsPath}`);
    console.error('\nThis import would overwrite existing files. Please either:');
    console.error('  1. Commit your changes: git add . && git commit -m "your message"');
    console.error('  2. Stash your changes: git stash');
    console.error('  3. Force the import: bun run src/extract-sector-data.ts <json_file> --force');
    console.error('\nAborting import to prevent data loss.');
    process.exit(1);
  }
  
  createDirectory(basePath);
  createDirectory(systemsPath);
  
  // Build lookup tables for entities
  const entitiesById: Record<string, EntityInfo> = {};
  const childrenByParent: Record<string, ChildInfo[]> = {};
  
  // First pass: collect all entities and build parent-child relationships
  for (const [entityType, entities] of Object.entries(data) as Array<[keyof SectorData, Record<string, any>]>) {
    if (entityType === 'sector' || entityType === 'note') {
      continue;
    }
    
    for (const [entityId, entity] of Object.entries(entities)) {
      entitiesById[entityId] = {
        type: entityType,
        data: entity as Entity,
        id: entityId
      };
      
      // Build parent-child mapping
      const parentId = entity.parent;
      if (parentId) {
        if (!childrenByParent[parentId]) {
          childrenByParent[parentId] = [];
        }
        childrenByParent[parentId].push({
          type: entityType,
          id: entityId,
          data: entity as Entity
        });
      }
    }
  }
  
  // Process systems and build coordinate index
  let systemsProcessed = 0;
  let planetsProcessed = 0;
  let locationsProcessed = 0;
  const coordinateIndex: Record<string, CoordinateInfo> = {};
  
  for (const [systemId, system] of Object.entries(data.system || {})) {
    const systemName = system.name || 'Unknown System';
    const systemDirName = cleanName(systemName);
    const systemFileName = `system--${systemDirName}.md`;
    
    // Create system directory first
    const systemDirPath = join(systemsPath, systemDirName);
    createDirectory(systemDirPath);
    
    // System file goes INSIDE the system directory
    const systemPath = join(systemDirPath, systemFileName);
    
    // Extract coordinates (1-indexed in JSON, convert to 0-indexed for display)
    const x = (system.x || 1) - 1;
    const y = (system.y || 1) - 1;
    const hexCoords = `${x.toString().padStart(2, '0')}${y.toString().padStart(2, '0')}`;
    
    // Add to coordinate index
    coordinateIndex[hexCoords] = {
      name: systemName,
      path: `systems/${systemDirName}/${systemFileName}`,
      x,
      y
    };
    
    // Generate system content
    const content: string[] = [`# ${systemName}`];
    content.push('');
    content.push('## System Information');
    content.push(`- **Coordinates**: ${system.x || 0},${system.y || 0} (1-indexed)`);
    content.push(`- **Hex**: ${x.toString().padStart(2, '0')},${y.toString().padStart(2, '0')} (0-indexed for map)`);
    
    // Star information
    let primaryStar: string | null = null;
    const stars = (system as any).star || [];
    for (const starId of stars) {
      if (starId in entitiesById) {
        const star = entitiesById[starId].data;
        const starName = star.name || 'Unknown Star';
        if (!primaryStar) {
          primaryStar = starName;
          const classification = (star as any).classification || 'Unknown';
          content.push(`- **Primary Star**: ${starName} (${classification})`);
        }
      }
    }
    
    content.push('');
    
    // List celestial bodies
    const bodyList: string[] = [];
    
    // Collect all bodies in this system using parent-child relationships
    if (systemId in childrenByParent) {
      for (const child of childrenByParent[systemId]) {
        const childType = child.type;
        const childData = child.data;
        const childName = childData.name || 'Unknown';
        
        switch (childType) {
          case 'planet':
            bodyList.push(`- **${childName}** - Planet`);
            break;
          case 'asteroidBelt':
            bodyList.push(`- **${childName}** - Asteroid Belt`);
            break;
          case 'gasGiantMine':
            bodyList.push(`- **${childName}** - Gas Giant`);
            break;
          case 'blackHole':
            bodyList.push(`- **${childName}** - Black Hole`);
            break;
        }
      }
    }
    
    if (bodyList.length > 0) {
      content.push('## Celestial Bodies');
      content.push(...bodyList);
      content.push('');
    }
    
    // Write system file
    writeFileSync(systemPath, content.join('\n'));
    systemsProcessed++;
    
    // Process planets in this system
    if (systemId in childrenByParent) {
      for (const child of childrenByParent[systemId]) {
        if (child.type !== 'planet') {
          continue;
        }
        
        const planetId = child.id;
        const planet = child.data as Planet;
        const planetName = planet.name || 'Unknown Planet';
        const planetDirName = cleanName(planetName);
        const planetFileName = `planet--${planetDirName}.md`;
        
        // Create planet directory
        const planetDirPath = join(systemDirPath, planetDirName);
        createDirectory(planetDirPath);
        
        // Create planet file path
        const planetPath = join(planetDirPath, planetFileName);
        
        // Generate planet content
        const content: string[] = [`# ${planetName}`];
        content.push('');
        content.push('## Planet Information');
        content.push(`- **System**: [${systemName}](../../${systemFileName})`);
        content.push('- **Type**: Planet');
        
        // Add attributes
        if (planet.attributes) {
          const attrs = planet.attributes;
          const attrList = ['atmosphere', 'temperature', 'biosphere', 'population', 'techLevel'] as const;
          for (const attr of attrList) {
            if (attr in attrs) {
              const displayName = attr.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
              content.push(`- **${displayName}**: ${attrs[attr]}`);
            }
          }
        }
        
        content.push('');
        
        if ('description' in planet) {
          content.push('## Description');
          content.push(planet.description || '');
          content.push('');
        }
        
        // Process tags
        if (planet.attributes?.tags && planet.attributes.tags.length > 0) {
          content.push('## World Tags');
          content.push('');
          for (const tag of planet.attributes.tags) {
            content.push(formatTag(tag));
          }
          content.push('');
        }
        
        // Write planet file
        writeFileSync(planetPath, content.join('\n'));
        planetsProcessed++;
        
        // Create subdirectories for locations
        const locationsDir = join(planetDirPath, 'locations');
        createDirectory(locationsDir);
        
        // Process locations on this planet
        if (planetId in childrenByParent) {
          for (const locChild of childrenByParent[planetId]) {
            const locationType = locChild.type;
            if (!['spaceStation', 'moonBase', 'researchBase', 'refuelingStation', 'orbitalRuin', 'asteroidBase'].includes(locationType)) {
              continue;
            }
            
            const poi = locChild.data as Location;
            const poiName = poi.name || 'Unknown Location';
            const poiType = cleanName(locationType.replace(/([A-Z])/g, '-$1').toLowerCase());
            const poiFileName = `${poiType}--${cleanName(poiName)}.md`;
            const poiPath = join(locationsDir, poiFileName);
            
            // Generate location content
            const content: string[] = [`# ${poiName}`];
            content.push('');
            content.push('## Location Information');
            content.push(`- **Planet**: [${planetName}](../${planetFileName})`);
            content.push(`- **System**: [${systemName}](../../../${systemFileName})`);
            content.push(`- **Type**: ${poiType.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}`);
            
            if (poi.attributes) {
              if (poi.attributes.occupation) {
                content.push(`- **Occupation**: ${poi.attributes.occupation}`);
              }
              if (poi.attributes.situation) {
                content.push(`- **Situation**: ${poi.attributes.situation}`);
              }
            }
            
            if ('description' in poi) {
              content.push('');
              content.push('## Description');
              content.push(poi.description || '');
            }
            
            // Write location file
            writeFileSync(poiPath, content.join('\n'));
            locationsProcessed++;
          }
        }
      }
      
      // Process asteroid belts in this system
      for (const child of childrenByParent[systemId]) {
        if (child.type !== 'asteroidBelt') {
          continue;
        }
        
        const beltId = child.id;
        const belt = child.data as AsteroidBelt;
        const beltName = belt.name || 'Unknown Belt';
        const beltDirName = cleanName(beltName);
        const beltFileName = `belt--${beltDirName}.md`;
        
        // Create belt directory
        const beltDirPath = join(systemDirPath, beltDirName);
        createDirectory(beltDirPath);
        
        // Create belt file
        const beltPath = join(beltDirPath, beltFileName);
        
        // Generate belt content
        const content: string[] = [`# ${beltName}`];
        content.push('');
        content.push('## Belt Information');
        content.push(`- **System**: [${systemName}](../../${systemFileName})`);
        content.push('- **Type**: Asteroid Belt');
        
        if (belt.attributes) {
          if (belt.attributes.occupation) {
            content.push(`- **Occupation**: ${belt.attributes.occupation}`);
          }
          if (belt.attributes.situation) {
            content.push(`- **Situation**: ${belt.attributes.situation}`);
          }
        }
        
        if ('description' in belt) {
          content.push('');
          content.push('## Description');
          content.push(belt.description || '');
        }
        
        // Process tags if any
        if (belt.attributes?.tags && belt.attributes.tags.length > 0) {
          content.push('');
          content.push('## Tags');
          content.push('');
          for (const tag of belt.attributes.tags) {
            content.push(formatTag(tag));
          }
        }
        
        // Write belt file
        writeFileSync(beltPath, content.join('\n'));
        
        // Create locations directory for belt
        const locationsDir = join(beltDirPath, 'locations');
        createDirectory(locationsDir);
        
        // Process locations in this belt
        if (beltId in childrenByParent) {
          for (const locChild of childrenByParent[beltId]) {
            const locationType = locChild.type;
            if (!['asteroidBase', 'spaceStation', 'refuelingStation'].includes(locationType)) {
              continue;
            }
            
            const poi = locChild.data as Location;
            const poiName = poi.name || 'Unknown Location';
            const poiType = cleanName(locationType.replace(/([A-Z])/g, '-$1').toLowerCase());
            const poiFileName = `${poiType}--${cleanName(poiName)}.md`;
            const poiPath = join(locationsDir, poiFileName);
            
            // Generate location content
            const content: string[] = [`# ${poiName}`];
            content.push('');
            content.push('## Location Information');
            content.push(`- **Belt**: [${beltName}](../${beltFileName})`);
            content.push(`- **System**: [${systemName}](../../../${systemFileName})`);
            content.push(`- **Type**: ${poiType.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}`);
            
            if (poi.attributes) {
              if (poi.attributes.occupation) {
                content.push(`- **Occupation**: ${poi.attributes.occupation}`);
              }
              if (poi.attributes.situation) {
                content.push(`- **Situation**: ${poi.attributes.situation}`);
              }
            }
            
            if ('description' in poi) {
              content.push('');
              content.push('## Description');
              content.push(poi.description || '');
            }
            
            // Write location file
            writeFileSync(poiPath, content.join('\n'));
            locationsProcessed++;
          }
        }
      }
    }
  }
  
  // Generate coordinate index file
  generateCoordinateIndex(basePath, coordinateIndex);
  
  console.log('\n✅ Import complete!');
  console.log(`   - Systems: ${systemsProcessed}`);
  console.log(`   - Planets: ${planetsProcessed}`);
  console.log(`   - Locations: ${locationsProcessed}`);
  console.log(`   - Output: ${basePath}/`);
}

// Main execution
if (import.meta.main) {
  const args = process.argv.slice(2);
  
  if (args.length < 1) {
    console.error('Usage: bun run src/extract-sector-data.ts <json_file> [--force]');
    process.exit(1);
  }
  
  const jsonFile = args[0];
  const force = args.includes('--force');
  
  if (!existsSync(jsonFile)) {
    console.error(`Error: File '${jsonFile}' not found`);
    process.exit(1);
  }
  
  extractSectorData(jsonFile, 'sectors', undefined, force);
}