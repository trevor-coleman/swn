# Stars Without Number Campaign Repository

A living campaign repository for Stars Without Number RPG campaigns. Currently active in the Abiha Omicron sector, with historical records from the Eradinus Expanse.

## Sector Selection

- **[Abiha Omicron](sectors/abiha-omicron/)** - Current campaign (isolated sector with ancient mysteries)
- **[Eradinus Expanse](sectors/eradinus-expanse/)** - Previous campaign records
- **[Cross-Sector](sectors/cross-sector/)** - Elements spanning multiple campaigns

## Quick Navigation

- **[Campaign Overview](campaign-overview.md)** - Current state and major plot threads
- **[Active Tensions](sectors/abiha-omicron/plot-threads/active-tensions.md)** - Immediate threats and opportunities
- **[Master Index](MASTER-INDEX.md)** - Complete content directory
- **[Session Timeline](TIMELINE.md)** - Chronological campaign history
- **[NPC Directory](NPC-INDEX.md)** - All characters and their connections
- **[Faction Tracker](FACTION-TRACKER.md)** - Organizations and their activities

## Current Status

**Last Session**: [July 4, 2025 - The Truth of Tokko 8](sectors/abiha-omicron/sessions/2025-07-04-truth-of-tokko-8.md)

**Party Location**: Tokko 8 Research Station, Cou (resting in *Starfall Whisper*)

**Immediate Situation**: 
- Multiple Asset Recovery Teams converging (<1 hour)
- Dr. Sss'theta (Architect) incapacitated for ~6 hours
- 10 refugees formed voluntary psychic network
- Lance and Kaedim made Deep Link contact with the Sleeper
- 65 hours until Sleeper awakens
- Planet-wide civil war erupting

## Quick Start for Session Planning

1. Review [Active Tensions](sectors/abiha-omicron/plot-threads/active-tensions.md)
2. Check [Next Session Planning](sectors/abiha-omicron/planning/next-session/)
3. Reference [Session Planning Pattern](gm-notes/session-planning-pattern.md)
4. Use [Content Generation Style Guide](gm-notes/content-generation-style.md)

## Repository Structure

### 🎮 Active Party
- `party/` - Current PC sheets and ship details (constant across campaigns)

### 🌌 Sector Content
- `sectors/abiha-omicron/` - Current campaign content
- `sectors/eradinus-expanse/` - Previous campaign archives
- `sectors/cross-sector/` - Multi-campaign elements

### 📚 Within Each Sector
- `sessions/` - Dated session summaries
- `characters/` - NPCs encountered
- `factions/` - Major organizations
- `lore/` - History and mysteries
- `plot-threads/` - Ongoing storylines
- `planning/` - Future session materials
- `modules/` - Ready-to-run adventures
- `systems/` - Star systems with hierarchical contents:
  - System files include coordinates, navigation info
  - Planet files as children of their systems
  - Location files (stations, bases) as children of planets/systems
- `systems-coordinate-index.md` - Hex grid navigation reference

### 📖 Reference Materials
- `game-mechanics/` - Rules references
- `gm-notes/` - Templates and guides

## Major Campaign Threads

### 🔴 Critical: The Silence Architects
Universe-level threat - beings who triggered the Scream as deliberate genocide

### ⚡ The Resonance Protocol
Ancient communication system being sought by multiple factions

### 🧠 Neural Enhancement Conspiracy
Military drugs and human augmentation experiments

### 🚀 Aurelius Jump Gate Mystery
Party's arrival method; currently dormant

## Key Mysteries
1. What is the true purpose of the Resonance Protocol?
2. Why did the Silence Architects trigger the Scream?
3. Who manipulated Dallas and Kaedim's meeting?
4. Where is the missing party member Taka?

## Campaign Tools

- **For adding content**: See [Contributing Guide](CONTRIBUTING.md)
- **For detailed instructions**: See [CLAUDE.md](CLAUDE.md)
- **For current campaign**: See [Abiha Omicron Index](sectors/abiha-omicron/README.md)
- **For rules questions**: Check [Game Mechanics](game-mechanics/)
- **For NPC creation**: Use templates in [GM Notes](gm-notes/)

---

*Remember: Maintain clear separation between what has happened (dated sessions), what is about to happen (next-session planning), and what could happen (future planning and ideas).*