/**
 * TypeScript type definitions for Sectors Without Number JSON export
 */

// Base entity properties shared by all entities
interface BaseEntity {
  creator: string;
  created: string;
  updated: string;
  name: string;
  isHidden: boolean;
  parent: string;
  parentEntity: string;
  attributes?: Record<string, any>;
}

// Tag definition
interface Tag {
  name: string;
  description: string;
  enemies: string[];
  friends: string[];
  complications: string[];
  things: string[];
  places: string[];
  creator?: string;
  types?: string[];
}

// System entity
interface System extends BaseEntity {
  parentEntity: 'sector';
  x: number;
  y: number;
  attributes?: {
    tags?: Tag[];
  };
}

// Planet entity
interface Planet extends BaseEntity {
  parentEntity: 'system';
  attributes?: {
    atmosphere?: string;
    temperature?: string;
    biosphere?: string;
    population?: string;
    techLevel?: string;
    tags?: Tag[];
  };
}

// Location base for various space installations
interface Location extends BaseEntity {
  parentEntity: 'system' | 'planet' | 'moon' | 'asteroidBelt';
  attributes?: {
    occupation?: string;
    situation?: string;
  };
}

// Specific location types
interface AsteroidBelt extends BaseEntity {
  parentEntity: 'system';
  attributes?: {
    occupation?: string;
    situation?: string;
  };
}

interface SpaceStation extends Location {
  parentEntity: 'planet' | 'system';
}

interface AsteroidBase extends Location {
  parentEntity: 'asteroidBelt';
}

interface MoonBase extends Location {
  parentEntity: 'moon';
}

interface RefuelingStation extends Location {}
interface ResearchBase extends Location {}
interface DeepSpaceStation extends Location {}
interface OrbitalRuin extends Location {}
interface GasGiantMine extends Location {}

// Moon entity
interface Moon extends BaseEntity {
  parentEntity: 'planet';
  attributes?: {
    tags?: Tag[];
  };
}

// Sector entity
interface Sector extends Omit<BaseEntity, 'parent' | 'parentEntity'> {
  rows: number;
  columns: number;
  attributes?: Record<string, any>;
}

// Note entity (for GM notes)
interface Note extends BaseEntity {
  attributes?: {
    content?: string;
  };
}

// Black hole entity
interface BlackHole extends BaseEntity {
  parentEntity: 'system';
}

// Main sector data structure
interface SectorData {
  sector: Record<string, Sector>;
  system: Record<string, System>;
  planet: Record<string, Planet>;
  asteroidBelt: Record<string, AsteroidBelt>;
  asteroidBase: Record<string, AsteroidBase>;
  blackHole: Record<string, BlackHole>;
  deepSpaceStation: Record<string, DeepSpaceStation>;
  gasGiantMine: Record<string, GasGiantMine>;
  moon: Record<string, Moon>;
  moonBase: Record<string, MoonBase>;
  note: Record<string, Note>;
  orbitalRuin: Record<string, OrbitalRuin>;
  refuelingStation: Record<string, RefuelingStation>;
  researchBase: Record<string, ResearchBase>;
  spaceStation: Record<string, SpaceStation>;
}

// Entity type union for type guards
type Entity = 
  | System 
  | Planet 
  | AsteroidBelt 
  | AsteroidBase
  | BlackHole
  | DeepSpaceStation
  | GasGiantMine
  | Moon
  | MoonBase
  | OrbitalRuin
  | RefuelingStation
  | ResearchBase
  | SpaceStation
  | Note;

// Type guards
export function isSystem(entity: Entity): entity is System {
  return entity.parentEntity === 'sector';
}

export function isPlanet(entity: Entity): entity is Planet {
  return entity.parentEntity === 'system' && 'atmosphere' in (entity.attributes || {});
}

export function isLocation(entity: Entity): entity is Location {
  return 'occupation' in (entity.attributes || {}) || 'situation' in (entity.attributes || {});
}

export type {
  SectorData,
  Sector,
  System,
  Planet,
  Moon,
  AsteroidBelt,
  SpaceStation,
  AsteroidBase,
  MoonBase,
  RefuelingStation,
  ResearchBase,
  DeepSpaceStation,
  OrbitalRuin,
  GasGiantMine,
  BlackHole,
  Note,
  Tag,
  Entity,
  Location
};