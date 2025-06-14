# Repository Reorganization Checklist

## Overview
Reorganizing repository to separate content by sector while maintaining cross-sector connections.
Party information will remain at root level as it's constant across campaigns.

## Target Structure
```
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
│   │   ├── items/
│   │   ├── lore/
│   │   ├── modules/
│   │   ├── planning/
│   │   ├── plot-threads/
│   │   └── sector-data/
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
- [ ] Create sectors/ directory
- [ ] Create sectors/eradinus-expanse/ and subdirectories
- [ ] Create sectors/abiha-omicron/ and subdirectories
- [ ] Create sectors/cross-sector/ and subdirectories

## Phase 2: Move Content to Abiha Omicron
- [ ] Move sessions/ to sectors/abiha-omicron/
- [ ] Move characters/ to sectors/abiha-omicron/
- [ ] Move factions/ to sectors/abiha-omicron/
- [ ] Move items/ to sectors/abiha-omicron/
- [ ] Move lore/ to sectors/abiha-omicron/
- [ ] Move modules/ to sectors/abiha-omicron/
- [ ] Move planning/ to sectors/abiha-omicron/
- [ ] Move plot-threads/ to sectors/abiha-omicron/
- [ ] Move sector-data/ to sectors/abiha-omicron/
- [ ] Move abilities/ to sectors/abiha-omicron/

## Phase 3: Extract Cross-Sector Content
- [ ] Move silence-architects.md to sectors/cross-sector/factions/
- [ ] Move the-scream-truth.md to sectors/cross-sector/lore/
- [ ] Create stellar-dynamics.md in sectors/eradinus-expanse/factions/
- [ ] Update Dallas's character sheet to reference Stellar Dynamics in Eradinus

## Phase 4: Update Navigation Files
- [ ] Update README.md with new structure
- [ ] Update MASTER-INDEX.md with new paths
- [ ] Update TIMELINE.md with sector context
- [ ] Update NPC-INDEX.md with new paths
- [ ] Update FACTION-TRACKER.md with sector divisions
- [ ] Update QUICK-REFERENCE.md with new paths
- [ ] Update REVELATIONS-INDEX.md with new paths
- [ ] Update CONTRIBUTING.md with new structure
- [ ] Update CLAUDE.md with new organization

## Phase 5: Update Cross-References
- [ ] Update all session files with new paths
- [ ] Update all character files with new paths
- [ ] Update all faction files with new paths
- [ ] Update all lore files with new paths
- [ ] Update all plot thread files with new paths
- [ ] Update campaign-overview.md with new paths
- [ ] Update active-tensions.md with new paths

## Phase 6: Create Sector-Specific Navigation
- [ ] Create sectors/abiha-omicron/README.md
- [ ] Create sectors/abiha-omicron/INDEX.md
- [ ] Create sectors/eradinus-expanse/README.md
- [ ] Create sectors/cross-sector/README.md

## Phase 7: Testing & Verification
- [ ] Test all links in navigation files
- [ ] Verify cross-sector references work
- [ ] Check that party files remain accessible
- [ ] Ensure all content is findable
- [ ] Update .claudeignore if needed

## Notes
- Using mv commands exclusively (no file regeneration)
- Party folder stays at root level
- Game mechanics and GM notes stay at root (system-wide)
- Navigation files stay at root but updated with new paths
- Silence Architects and Scream Truth are only cross-sector items currently