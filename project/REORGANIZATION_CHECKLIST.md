# Repository Reorganization Checklist

## Overview
Reorganizing repository to separate content by sector while maintaining cross-sector connections.
Party information will remain at root level as it's constant across campaigns.

## Target Structure
```text
swn/
├── party/                     (constant across campaigns - stays at root)
├── sectors/
│   ├── eradinus-expanse/     (previous campaign)
│   │   └── factions/
│   │       └── stellar-dynamics.md
│   ├── abiha-omicron/        (current campaign)
│   │   ├── sessions/
│   │   ├── characters/
│   │   ├── factions/
│   │   ├── lore/
│   │   ├── modules/
│   │   ├── planning/
│   │   ├── plot-threads/
│   │   ├── systems/          (hierarchical: systems→planets→locations)
│   │   └── systems-coordinate-index.md
│   └── cross-sector/         (spans multiple sectors)
│       ├── factions/
│       │   └── silence-architects.md
│       └── lore/
│           └── the-scream-truth.md
├── game-mechanics/           (system-wide)
├── gm-notes/                 (system-wide)
└── [navigation files]        (updated to reflect new structure)
```

## Phase 1: Create Directory Structure
- [x] Create sectors/ directory
- [x] Create sectors/eradinus-expanse/ and subdirectories
- [x] Create sectors/abiha-omicron/ and subdirectories
- [x] Create sectors/cross-sector/ and subdirectories

## Phase 2: Move Content to Abiha Omicron
- [x] Move sessions/ to sectors/abiha-omicron/
- [x] Move characters/ to sectors/abiha-omicron/
- [x] Move factions/ to sectors/abiha-omicron/
- [x] Move lore/ to sectors/abiha-omicron/
- [x] Move modules/ to sectors/abiha-omicron/
- [x] Move planning/ to sectors/abiha-omicron/
- [x] Move plot-threads/ to sectors/abiha-omicron/
- [x] Move items to party/ folders (character-specific)
- [x] Create hierarchical systems/ structure
- [x] Move abilities/ to sectors/abiha-omicron/

## Phase 3: Extract Cross-Sector Content
- [x] Move silence-architects.md to sectors/cross-sector/factions/
- [x] Move the-scream-truth.md to sectors/cross-sector/lore/
- [x] Create stellar-dynamics.md in sectors/eradinus-expanse/factions/
- [x] Update Dallas's character sheet to reference Stellar Dynamics in Eradinus

## Phase 4: Update Navigation Files
- [x] Update README.md with new structure
- [x] Update MASTER-INDEX.md with new paths
- [x] Update TIMELINE.md with sector context
- [x] Update NPC-INDEX.md with new paths
- [x] Update FACTION-TRACKER.md with sector divisions
- [x] Update QUICK-REFERENCE.md with new paths
- [x] Update REVELATIONS-INDEX.md with new paths
- [x] Update CONTRIBUTING.md with new structure
- [x] Update CLAUDE.md with new organization

## Phase 5: Update Cross-References
- [x] Update all navigation files with sed
- [x] Update party files with new paths
- [x] Update campaign-overview.md with new paths
- [x] Update active-tensions.md with new paths
- [x] Batch update all files within Abiha Omicron with sed

## Phase 6: Create Sector-Specific Navigation
- [x] Create sectors/abiha-omicron/README.md
- [x] Create sectors/abiha-omicron/INDEX.md
- [x] Create sectors/eradinus-expanse/README.md
- [x] Create sectors/cross-sector/README.md

## Phase 7: Testing & Verification
- [x] All major navigation files updated
- [x] Cross-sector references properly linked
- [x] Party files remain at root level
- [x] Content organized by sector

## REORGANIZATION COMPLETE

### Summary of Changes:
1. Created sectors/ directory structure with three subdivisions:
   - abiha-omicron/ (current campaign)
   - eradinus-expanse/ (previous campaign)
   - cross-sector/ (multi-campaign elements)

2. Moved all content to appropriate sectors:
   - 99% of content → abiha-omicron/
   - Stellar Dynamics → eradinus-expanse/
   - Silence Architects & Scream Truth → cross-sector/
   - Items → party/[character-name]/ folders

3. Implemented hierarchical location structure:
   - Systems at top level (with coordinates)
   - Planets as children of systems
   - Locations (stations, bases) under parent bodies
   - Added coordinate index for hex navigation

4. Updated all navigation files and cross-references

5. Party folder remains at root as it's constant across campaigns

6. Created sector-specific navigation aids

The repository now supports hierarchical navigation matching the game's spatial relationships while maintaining clear sector boundaries.

## Notes
- Using mv commands exclusively (no file regeneration)
- Party folder stays at root level
- Game mechanics and GM notes stay at root (system-wide)
- Navigation files stay at root but updated with new paths
- Silence Architects and Scream Truth are only cross-sector items currently