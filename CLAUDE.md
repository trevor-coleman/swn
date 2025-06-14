
# Stars Without Number Campaign Assistant

## Session Planning Process

See @gm-notes/session-planning-pattern.md for the detailed workflow

## Content Generation Style

See @gm-notes/content-generation-style.md for how to format modules and descriptions

## ‼️ IMPORTANT: Adding New Content

See @CONTRIBUTING.md for instructions on adding and indexing new information

## Purpose
This is a living campaign repository for Stars Without Number RPG campaigns across multiple sectors. The repository serves as both a historical record of past sessions and a planning tool for future adventures. Claude helps track the complex interconnected plot threads, NPCs, factions, and mysteries while maintaining consistency across campaigns.

## Organization Structure

### Sector Organization
- **sectors/abiha-omicron/** - Current campaign (isolated sector)
- **sectors/eradinus-expanse/** - Previous campaign archives
- **sectors/cross-sector/** - Elements spanning multiple campaigns

### Within Each Sector
- **sessions/** - Dated session summaries in chronological order
- **characters/** - NPCs organized by affiliation
- **items/** - Special items and artifacts
- **factions/** - Major organizations
- **lore/** - Important concepts and mysteries
- **plot-threads/** - Active tensions and storylines
- **planning/** - Future session prep and ideas
- **modules/** - Ready-to-run adventures
- **systems/** - Star systems in the sector
- **planets/** - Planets and their details
- **locations/** - Space stations, asteroid bases, etc.

### Party Organization (Root Level)
- **party/** - PC data organized by player
  - **[character-name]/character-sheet.md** - Character stats
  - **[character-name]/[ability].md** - Special abilities
  - **[character-name]/[handout].md** - Player-specific information
  - **starfall-whisper.md** - Shared party ship

### Meta Information
- **game-mechanics.md** - SWN rules reference
- **campaign-overview.md** - High-level campaign summary
- **gm-notes/** - Templates and style guides

## Current Campaign Status
- **Active Sector**: Abiha Omicron
- See @campaign-overview.md for the big picture
- See @sectors/abiha-omicron/plot-threads/active-tensions.md for immediate concerns
- See @sectors/abiha-omicron/README.md for sector overview

## Navigation Aids
- @README.md - Entry point and current status
- @MASTER-INDEX.md - Complete content directory
- @TIMELINE.md - Chronological campaign events
- @NPC-INDEX.md - All characters and connections
- @FACTION-TRACKER.md - Organization activities
- @QUICK-REFERENCE.md - GM screen for sessions
- @REVELATIONS-INDEX.md - Key discoveries tracker

## Key Principles

### Temporal Separation
Always maintain clear separation between:
- What has already happened (sessions with dates)
- What is about to happen (planning/next-session)
- What could happen (planning/future and planning/ideas)

### Sector Separation
Maintain clear boundaries between:
- Sector-specific content (in appropriate sector folder)
- Cross-sector elements (in cross-sector folder)
- Player information (in party folder)

### Player Organization
Each player has their own folder containing:
- Character sheet (always named character-sheet.md)
- Character-specific abilities and items
- Handouts and personal notes
- Information they've discovered or been given

This ensures players can easily find all their relevant information and prevents confusion about the current state of the campaign.
