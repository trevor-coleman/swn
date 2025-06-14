# Contributing to the Stars Without Number Campaign Repository

This guide explains how to add new content and maintain the repository's discoverability features.

## Overview

This repository uses a multi-layered indexing system to ensure information remains discoverable as the campaign grows. When adding new content, you'll typically need to:
1. Create the content file in the appropriate directory
2. Update relevant index files
3. Add cross-references to related content
4. Update timeline if session-related

## Directory Structure

### Multi-Sector Organization
- **sectors/** - Content organized by campaign sector
  - **abiha-omicron/** - Current campaign
  - **eradinus-expanse/** - Previous campaign
  - **cross-sector/** - Elements spanning multiple campaigns

### Core Content Directories (Within Each Sector)
- **sessions/** - Dated session summaries (YYYY-MM-DD-description.md)
- **characters/** - NPCs organized by affiliation
- **items/** - Special artifacts and equipment
- **lore/** - World history and mysteries
- **factions/** - Organization details
- **plot-threads/** - Ongoing storylines and tensions
- **planning/** - Future session prep and ideas
- **modules/** - Ready-to-run adventures
- **systems/** - Star systems in the sector
- **planets/** - Planets and their details
- **locations/** - Space stations, asteroid bases, etc.

### Party Organization (Root Level)
- **party/** - PC data organized by player
  - **[character-name]/** - Individual player folder
    - **character-sheet.md** - Character stats and info
    - **[ability-name].md** - Character-specific abilities
    - **[handout-name].md** - Player handouts and notes
  - **starfall-whisper.md** - Shared party ship

## Adding New Content

### 1. Session Summaries

**File Location**: `sectors/abiha-omicron/sessions/YYYY-MM-DD-description.md`

**Format**:
```markdown
# Session [Number]: [Title]
Date: [Date]

## Party Status
[Current party composition and condition]

## Summary
[What happened during the session]

## Key Events
- [Major plot developments]
- [NPC encounters]
- [Discoveries]

## Consequences
[Immediate results of party actions]

## Introduced Elements
- NPCs: [New characters met]
- Locations: [New places visited]
- Items: [New equipment/artifacts found]
- Lore: [New information learned]
```

**After Creating, Update**:
- [ ] TIMELINE.md - Add session entry with key events
- [ ] NPC-INDEX.md - Add any new NPCs
- [ ] FACTION-TRACKER.md - Update faction activities
- [ ] REVELATIONS-INDEX.md - Add any discoveries
- [ ] sectors/abiha-omicron/plot-threads/active-tensions.md - Update ongoing threads

### 2. Player Characters & Handouts

**File Location**: `party/[character-name]/[file-name].md`

**Character Sheet**: Always named `character-sheet.md`

**Handouts/Abilities**: Descriptive names like `network-echo-ability.md` or `theta-outpost-puzzle.md`

**After Creating, Update**:
- [ ] If new ability, update character-sheet.md with reference
- [ ] If plot-relevant, add to active-tensions.md

### 3. NPCs

**File Location**: `sectors/[sector-name]/characters/[affiliation]/[name].md`

**Naming Convention**: Use lowercase with hyphens (e.g., `lance-reynolds.md`)

**Format**:
```markdown
# [Character Name]

## Quick Reference
- **Status**: [Alive/Dead/Missing/Unknown]
- **Affiliation**: [Faction/Group]
- **First Appearance**: [Session reference]
- **Location**: [Last known location]

## Description
[Physical appearance and demeanor]

## Background
[History and motivation]

## Relationships
- [Character]: [Nature of relationship]

## Abilities/Resources
[What they can do or provide]

## Session History
- [Session X]: [What happened]
```

**After Creating, Update**:
- [ ] NPC-INDEX.md - Add to appropriate categories
- [ ] FACTION-TRACKER.md - If faction member
- [ ] Relevant session file - Add to "Introduced Elements"

### 4. Plot Threads

**File Location**: `sectors/[sector-name]/plot-threads/[thread-name].md`

**Format**:
```markdown
# [Thread Title]

## Status
[Active/Resolved/Background]

## Overview
[Brief description of the thread]

## Key Players
- [Character/Faction]: [Their role]

## Timeline
- [Session/Date]: [Development]

## Related Threads
- [Thread Name]: [Connection]

## Unresolved Questions
1. [Question]

## Potential Developments
- [Possibility]
```

**After Creating, Update**:
- [ ] sectors/abiha-omicron/plot-threads/active-tensions.md - Add to appropriate section
- [ ] MASTER-INDEX.md - Add to plot threads section
- [ ] Related character/faction files - Add cross-references

### 5. Locations

**File Location**: `sectors/[sector-name]/locations/[location].md` or `sectors/[sector-name]/planning/future/[location].md`

**Format**:
```markdown
# [Location Name]

## System Information
- **System**: [Parent system]
- **Type**: [Planet/Station/etc]
- **Status**: [Visited/Known/Rumored]

## Description
[Physical and cultural details]

## Notable Features
- [Feature]: [Description]

## Factions Present
- [Faction]: [Their presence/influence]

## Adventure Hooks
- [Hook description]

## Session History
- [Session]: [What happened here]
```

### 6. Items/Artifacts

**File Location**: `sectors/[sector-name]/items/[item-name].md`

**Exception**: Character-specific items may be tracked in `party/[character-name]/` as handouts

**Format**:
```markdown
# [Item Name]

## Status
- **Current Owner**: [Character/Location]
- **Acquired**: [Session reference]

## Description
[Physical appearance and properties]

## Abilities
[What it does]

## History
[Known background]

## Plot Relevance
[Why it matters to the campaign]
```

## Updating Index Files

### MASTER-INDEX.md
Update when adding:
- New plot threads
- New major NPCs
- New significant locations
- New game mechanics or rules

### TIMELINE.md
Update when:
- Completing a session
- Adding historical events
- Planning future events

### NPC-INDEX.md
Update when:
- Adding new NPCs
- Changing NPC status
- Discovering new relationships

### FACTION-TRACKER.md
Update when:
- Faction takes significant action
- Power dynamics change
- New conflicts emerge

### REVELATIONS-INDEX.md
Update when:
- Party makes discovery
- Mystery is resolved
- New questions arise

### QUICK-REFERENCE.md
Update when:
- Party status changes significantly
- Common NPCs change
- New recurring mechanics introduced

## Cross-Referencing Best Practices

### Use Relative Links
```markdown
From party file: See [Captain Reyes](../sectors/abiha-omicron/characters/stellar-dynamics/captain-reyes.md)
From sector file: See [Dallas](../../party/dallas-jacobi/character-sheet.md)
```

### Reference Sections
```markdown
See [Session 12](../sectors/abiha-omicron/sessions/2024-06-15-archive-arrival.md#archive-judgment)
```

### Create Bidirectional Links
When A references B, ensure B also references A where relevant.

### Use Consistent Formatting
- Sessions: `[Session X: Title](../sectors/[sector]/sessions/YYYY-MM-DD-description.md)`
- NPCs: `[Character Name](../sectors/[sector]/characters/affiliation/name.md)`
- PCs: `[Character Name](../party/[character-name]/character-sheet.md)`
- Locations: `[Location Name](../sectors/[sector]/locations/location.md)`

## File Naming Conventions

1. **Use lowercase with hyphens**: `captain-reyes.md` not `Captain_Reyes.md`
2. **Sessions include date**: `2024-06-15-archive-arrival.md`
3. **Be descriptive but concise**: `resonance-protocol.md` not `the-mysterious-ancient-communication-system.md`
4. **Group by affiliation**: `sectors/[sector]/characters/aurelius-consortium/zhou.md`
5. **Player folders use character names**: `party/dallas-jacobi/`

## Maintenance Checklist

### After Each Session
1. [ ] Create session summary
2. [ ] Update TIMELINE.md
3. [ ] Update NPC-INDEX.md with new characters
4. [ ] Update FACTION-TRACKER.md with faction activities
5. [ ] Update REVELATIONS-INDEX.md with discoveries
6. [ ] Update sectors/abiha-omicron/plot-threads/active-tensions.md
7. [ ] Update QUICK-REFERENCE.md party status
8. [ ] Add cross-references to affected files

### Weekly/Regular Maintenance
1. [ ] Review and consolidate planning notes
2. [ ] Update README.md if major campaign shifts
3. [ ] Archive completed plot threads
4. [ ] Verify all cross-references still work

## Common Patterns

### Adding Player Handouts/Abilities
1. Create file in `party/[character-name]/`
2. Update character-sheet.md with reference
3. If plot-relevant, update active-tensions.md
4. Consider if it needs indexing elsewhere

### Adding a Major NPC
1. Create character file
2. Add to NPC-INDEX.md
3. Add to faction file if applicable
4. Update FACTION-TRACKER.md
5. Reference in relevant plot threads
6. Add to session "Introduced Elements"

### Resolving a Plot Thread
1. Update thread file with resolution
2. Move from "Immediate Threats" to "Resolved" in active-tensions.md
3. Update TIMELINE.md with resolution
4. Create new threads for consequences
5. Update affected NPC/faction files

### Planning Future Content
1. Add to sectors/abiha-omicron/planning/future/ or sectors/abiha-omicron/planning/ideas/
2. Reference in relevant plot threads
3. Add hooks to MASTER-INDEX.md if significant
4. Link from current content where foreshadowed

## Tips for Discoverability

1. **Write descriptive headers** - They appear in indices
2. **Include session references** - Makes timeline tracking easier
3. **List relationships explicitly** - Helps with connection mapping
4. **Use consistent status labels** - Enables quick filtering
5. **Add "See Also" sections** - Creates discovery paths
6. **Update indices immediately** - Prevents orphaned content

## Questions or Issues?

If you're unsure where something belongs or how to index it:
1. Check similar existing content
2. Prioritize discoverability over perfect categorization
3. Add to multiple indices if it fits multiple categories
4. Include a note in your commit about indexing decisions