# Rulebook Processing Checklist

## Important Reference
**Bookmarks File**: `/Users/trevorcoleman/fun/swn/rulebook/raw/bookmarks.txt`
- Contains complete chapter outline from original PDF
- Use to verify all content has been extracted before marking a chapter complete
- Cross-reference bookmark entries with created files

## Quick Reference: File Splitting Commands

```bash
# Check file length
wc -l rulebook/raw/filename.txt

# Create split directory
mkdir -p rulebook/raw/split-temp/filename

# Split file into 450-line chunks
split -l 450 -d -a 3 rulebook/raw/filename.txt rulebook/raw/split-temp/filename/part-

# List split parts
ls -la rulebook/raw/split-temp/filename/

# Clean up after processing
rm -rf rulebook/raw/split-temp/filename
```

## Initial Setup
- [X] Create directory structure:
  - [X] Create `rulebook/raw/` directory
  - [X] Move all existing `.txt` files to `rulebook/raw/`
  - [X] Create `rulebook/reference/` directory
  - [X] Create all subdirectories as outlined in structure

## File Processing Checklist

### For Each File in the Following List:

**Files to Process:**
1. ✓ adventure-creation.txt / adventure-creation-format.txt (if tables exist)
2. ✓ character-creation.txt / character-creation-format.txt
3. X equipment-and-vehicles.txt / equipment-and-vehicles-format.txt
4. X factions.txt / factions-format.txt
5. X game-master-resources.txt
6. X heroic-characters.txt
7. index.txt
8. into-the-waiting-night.txt
9. kickstarter-backers.txt (skip - not game content)
10. X mechs.txt
11. ✓ psionics.txt
12. ✓ sector-creation.txt
13. societies.txt
14. space-magic.txt
15. ✓ starships.txt / starships-format.txt
16. ✓ systems.txt
17. ✓ the-history-of-space.txt
18. transhuman-campaigns.txt
19. true-artificial-intelligences.txt
20. ✓ xenobestiary.txt / xenobestiary-format.txt

### Processing Steps for Each File:

#### A. File Size Check & Splitting
- [ ] Check file length with `wc -l filename.txt`
- [ ] If file > 500 lines:
  - [ ] Create temporary directory: `mkdir -p rulebook/raw/split-temp/[filename]`
  - [ ] Split file into 450-line chunks: `split -l 450 -d -a 3 rulebook/raw/[filename].txt rulebook/raw/split-temp/[filename]/part-`
  - [ ] Process each part sequentially, maintaining context between parts
  - [ ] Note: Content may flow between splits - check last/first lines of adjacent parts
- [ ] If file <= 500 lines:
  - [ ] Process normally without splitting

#### B. Initial Analysis
- [ ] For split files: Read each part sequentially to build full understanding
- [ ] For normal files: Read first 200 lines of plain text version
- [ ] Identify major sections and subsections across all parts
- [ ] Determine if formatted version needed (check for tables, stat blocks)
- [ ] Create processing plan for this specific file

#### C. Content Extraction

**For Split Files:**
- [ ] Maintain a working document to track content across parts
- [ ] Check for incomplete sections at part boundaries
- [ ] Merge related content that was split across files
- [ ] Keep track of table headers that may appear in earlier parts

**For Narrative Content (history, rules explanations):**
- [ ] Extract major sections based on headers
- [ ] Create one markdown file per major topic
- [ ] Preserve section headers as H2/H3
- [ ] Add navigation links to related topics

**For Structured Content (requires formatted version):**
- [ ] Read formatted version to identify table structures
- [ ] Parse tables by identifying column headers
- [ ] Extract individual entries (weapons, armor, foci, etc.)
- [ ] Create one file per entry with complete information
- [ ] For split files: Watch for tables that span multiple parts

#### D. File Creation Pattern

**For Items/Equipment:**
```markdown
# [Item Name]

## Stats
- **Damage**: [damage]
- **Range**: [range]
- **Cost**: [cost] credits
- **Encumbrance**: [enc]
- **TL**: [tech level]
- **Attribute**: [attribute]

## Description
[Full description from text]

## Special Properties
[Any special rules or properties]

## Availability
[Where typically found, legality issues]
```

**For Character Options (Classes, Backgrounds, Foci):**
```markdown
# [Option Name]

## Type
[Class/Background/Focus]

## Requirements
[Any prerequisites]

## Benefits
[What you get]

## Description
[Flavor text and explanation]

## Progression (if applicable)
### Level 1
[Benefits]

### Level 2
[Benefits]
```

**For Creatures:**
```markdown
# [Creature Name]

## Stats
- **HD**: [hit dice]
- **AC**: [armor class]
- **Atk**: [attacks]
- **Dmg**: [damage]
- **Move**: [movement]
- **Save**: [save]
- **ML**: [morale]
- **Skills**: [skills]

## Description
[Physical description and behavior]

## Tactics
[How it fights]

## Loot
[What it drops]
```

#### E. Cross-Referencing
- [ ] Add "See Also" sections linking related content
- [ ] Update parent directory README.md with new entry
- [ ] Add to appropriate index/category files

#### F. Validation
- [ ] Verify all game mechanics preserved
- [ ] Check that descriptions are complete
- [ ] Ensure no critical information lost
- [ ] Test that file can be understood in isolation

#### G. Cleanup (for split files)
- [ ] After successful processing, remove split files: `rm -rf rulebook/raw/split-temp/[filename]`
- [ ] Document any content that was challenging to parse due to splits
- [ ] Note any tables or sections that spanned multiple parts for future reference

#### H. Bookmark Verification
- [ ] Check bookmarks.txt for the current chapter's entries
- [ ] Verify all bookmarked sections have been extracted
- [ ] Cross-reference created files with bookmark hierarchy
- [ ] Note any missing content before marking chapter complete

## Handling Large Formatted Files

**Note**: If formatted versions (-format.txt files) are also > 500 lines:
- [ ] Apply the same splitting process
- [ ] Be extra careful with table parsing across splits
- [ ] Consider creating a mapping document to track which tables appear in which parts
- [ ] Tables may have headers in one part and data in another

## Specific File Processing Instructions

### 1. character-creation.txt / character-creation-format.txt
**Use formatted version for:**
- Background table
- Skill list and descriptions
- Focus list with full descriptions
- Starting equipment packages

**Extract:**
- [X] Character creation process overview
- [X] Attribute generation rules
- [X] Each skill with description
- [X] Each background (organized by category)
- [X] Each class (Expert, Psychic, Warrior, Adventurer)
- [X] Each focus organized by type (combat, non-combat, psychic)
- [X] Equipment packages
- [X] Final character creation steps

### 3. equipment-and-vehicles.txt / equipment-and-vehicles-format.txt
**Use formatted version for:**
- All equipment tables
- Vehicle tables

**Extract:**
- [X] General equipment rules (encumbrance, money, legality)
- [X] Each weapon as individual file (samples created)
- [X] Each armor type as individual file (samples created)
- [X] Equipment by category (survival, medical, etc.)
- [X] Each vehicle type (overview created)
- [X] Tech level descriptions

### 3. systems.txt
**Extract:**
- [X] Basic mechanics overview
- [X] Skill check rules
- [X] Saving throw rules
- [X] Combat sequence
- [X] Each combat action
- [X] Damage and healing rules
- [X] Environmental hazards

### 4. psionics.txt
**Extract:**
- [X] Psychic class details
- [X] Each discipline overview
- [X] Each technique by level
- [X] Effort and torching rules
- [X] Psychic equipment

### 5. starships.txt / starships-format.txt
**Use formatted version for:**
- Ship hull table
- Component tables
- Weapon tables

**Extract:**
- [ ] Ship combat rules (basic structure created)
- [ ] Each hull class (overview and table created)
- [ ] Each component type (structure created)
- [ ] Each weapon system (structure planned)
- [ ] Spike drive rules (in space travel section)

### 6. sector-creation.txt
**Extract:**
- [ ] World generation process
- [ ] Each world tag with full details
- [ ] Society types
- [ ] Atmosphere/Temperature/Biosphere tables
- [ ] Adventure hooks by tag

### 7. factions.txt / factions-format.txt
**Use formatted version for:**
- Asset tables
- Goal tables

**Extract:**
- [X] Faction turn sequence
- [X] Each asset type with stats (overview created, samples shown)
- [X] Each goal type
- [X] Faction creation rules

### 8. xenobestiary.txt / xenobestiary-format.txt
**Use formatted version for:**
- Creature stat blocks

**Extract:**
- [ ] Each creature as separate file
- [ ] Xenobestiary creation rules
- [ ] Creature categories

### 9. adventure-creation.txt
**Extract:**
- [X] Quick adventure generation
- [X] Problem templates
- [X] NPC templates
- [X] Location templates
- [X] Reward guidelines
- [X] Adventure creation example

### 10. the-history-of-space.txt
**Extract:**
- [ ] Major historical periods
- [ ] The Scream
- [ ] Mandate era
- [ ] Current era
- [ ] Timeline of events

## Audit Results & Corrections Required

### Completed Files (Verified Complete)
- ✓ psionics.txt - All 66 techniques and rules extracted
- ✓ sector-creation.txt - All 100 world tags and tables extracted
- ✓ the-history-of-space.txt - Complete history and timeline preserved
- ✓ xenobestiary.txt - All 29 creatures and creation systems extracted
- ✓ adventure-creation.txt - All templates and guidelines extracted

### Files Requiring Corrections

#### character-creation.txt - INCOMPLETE [IN PROGRESS]
**Missing Content:**
- [✓] 18 of 20 backgrounds missing (only Barbarian & Clergy extracted) [COMPLETED]
  - Created: Dilettante, Entertainer, Merchant, Noble, Official, Peasant, Physician, Pilot, Politician, Scholar, Soldier, Spacer, Technician, Thug, Vagabond, Worker
  - Note: Courtesan and Criminal were already created but not noted in checklist
- [✓] All individual skill descriptions (25 skills need descriptions) [COMPLETED]
  - Created all 19 regular skills + 6 psychic skills with full descriptions
- [✓] 8 of 11 equipment packages missing [COMPLETED]
  - Created: Barbarian, Blade, Thief, Gunslinger, Scout, Medic, Technician, Quick Creation
  - All packages now have detailed breakdowns with recommendations
- [✓] Detailed class descriptions for Expert, Warrior, Psychic, Adventurer [ALREADY COMPLETE]
  - All four classes have comprehensive files with abilities, concepts, and build examples
- [✓] Character advancement rules [COMPLETED]
  - Created comprehensive advancement guide with XP table, level benefits, and skill costs

#### systems.txt - COMPLETE
**Missing Content:**
- [✓] Entire hacking system (lines 941-1166 in raw file) [COMPLETED]
  - Created comprehensive hacking guide with all rules, actions, and modifiers
- [✓] Character advancement section (lines 1169-1443) [COMPLETED]
  - Already extracted with character creation content
- [✓] Scenes and durations timing system (lines 102-120) [COMPLETED]
  - Created scenes-and-durations.md with complete explanation
- [✓] Quick reference sheet (lines 1531-1649) [COMPLETED]
  - Created system-quick-reference.md with all quick rules

#### starships.txt - COMPLETE
**Missing Content:**
- [✓] 21 ship weapons need individual files in weapons/ directory [COMPLETED]
  - Fighter weapons: Multifocal Laser, Reaper Battery, Fractal Impact Charge, Polyspectral MES Beam
  - Frigate+ weapons: Sandthrower, Flak Emitter Battery, Torpedo Launcher, Charged Particle Caster, Plasma Beam, Mag Spike Array, Nuclear Missiles
  - Cruiser+ weapons: Spinal Beam Cannon, Smart Cloud, Gravcannon, Spike Inversion Projector
  - Capital weapons: Vortex Tunnel Inductor, Mass Cannon, Lightning Charge Mantle, Singularity Gun
  - All 21 weapons now have comprehensive individual files with full stats, descriptions, and tactical information

### Unprocessed Files Still Needing Work
- [ ] equipment-and-vehicles.txt / equipment-and-vehicles-format.txt
- [ ] factions.txt / factions-format.txt (only partial extraction done)
- [ ] game-master-resources.txt
- [ ] heroic-characters.txt
- [ ] mechs.txt (only partial extraction done)
- [ ] index.txt
- [ ] into-the-waiting-night.txt
- [ ] societies.txt
- [ ] space-magic.txt
- [ ] transhuman-campaigns.txt
- [ ] true-artificial-intelligences.txt

## Final Steps
- [ ] Create master README.md with navigation to all sections
- [ ] Create quick-reference files for common lookups
- [ ] Add search hints for LLMs in README files
- [ ] Test navigation paths
- [ ] Verify no broken links
- [ ] Create RULEBOOK-INDEX.md with alphabetical listing

## Quality Checks
- [ ] Each file can be understood standalone
- [ ] Navigation is intuitive
- [ ] Related content is cross-linked
- [ ] Tables preserved accurately
- [ ] No duplicate information
- [ ] Consistent formatting throughout