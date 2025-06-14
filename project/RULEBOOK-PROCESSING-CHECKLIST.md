# Rulebook Processing Checklist

## Initial Setup
- [ ] Create directory structure:
  - [ ] Create `rulebook/raw/` directory
  - [ ] Move all existing `.txt` files to `rulebook/raw/`
  - [ ] Create `rulebook/reference/` directory
  - [ ] Create all subdirectories as outlined in structure

## File Processing Checklist

### For Each File in the Following List:

**Files to Process:**
1. adventure-creation.txt / adventure-creation-format.txt (if tables exist)
2. character-creation.txt / character-creation-format.txt
3. equipment-and-vehicles.txt / equipment-and-vehicles-format.txt
4. factions.txt / factions-format.txt
5. game-master-resources.txt
6. heroic-characters.txt
7. index.txt
8. into-the-waiting-night.txt
9. kickstarter-backers.txt (skip - not game content)
10. mechs.txt
11. psionics.txt
12. sector-creation.txt
13. societies.txt
14. space-magic.txt
15. starships.txt / starships-format.txt
16. systems.txt
17. the-history-of-space.txt
18. transhuman-campaigns.txt
19. true-artificial-intelligences.txt
20. xenobestiary.txt / xenobestiary-format.txt

### Processing Steps for Each File:

#### A. Initial Analysis
- [ ] Read first 200 lines of plain text version
- [ ] Identify major sections and subsections
- [ ] Determine if formatted version needed (check for tables, stat blocks)
- [ ] Create processing plan for this specific file

#### B. Content Extraction

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

#### C. File Creation Pattern

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

#### D. Cross-Referencing
- [ ] Add "See Also" sections linking related content
- [ ] Update parent directory README.md with new entry
- [ ] Add to appropriate index/category files

#### E. Validation
- [ ] Verify all game mechanics preserved
- [ ] Check that descriptions are complete
- [ ] Ensure no critical information lost
- [ ] Test that file can be understood in isolation

## Specific File Processing Instructions

### 1. character-creation.txt / character-creation-format.txt
**Use formatted version for:**
- Background table
- Skill list and descriptions
- Focus list with full descriptions
- Starting equipment packages

**Extract:**
- [ ] Each background as separate file
- [ ] Each class (Expert, Psychic, Warrior, Adventurer)
- [ ] Each skill with description
- [ ] Each focus with both levels
- [ ] Character creation process overview
- [ ] Attribute generation rules

### 2. equipment-and-vehicles.txt / equipment-and-vehicles-format.txt
**Use formatted version for:**
- All equipment tables
- Vehicle tables

**Extract:**
- [ ] General equipment rules (encumbrance, money, legality)
- [ ] Each weapon as individual file
- [ ] Each armor type as individual file
- [ ] Equipment by category (survival, medical, etc.)
- [ ] Each vehicle type
- [ ] Tech level descriptions

### 3. systems.txt
**Extract:**
- [ ] Basic mechanics overview
- [ ] Skill check rules
- [ ] Saving throw rules
- [ ] Combat sequence
- [ ] Each combat action
- [ ] Damage and healing rules
- [ ] Environmental hazards

### 4. psionics.txt
**Extract:**
- [ ] Psychic class details
- [ ] Each discipline overview
- [ ] Each technique by level
- [ ] Effort and torching rules
- [ ] Psychic equipment

### 5. starships.txt / starships-format.txt
**Use formatted version for:**
- Ship hull table
- Component tables
- Weapon tables

**Extract:**
- [ ] Ship combat rules
- [ ] Each hull class
- [ ] Each component type
- [ ] Each weapon system
- [ ] Spike drive rules

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
- [ ] Faction turn sequence
- [ ] Each asset type with stats
- [ ] Each goal type
- [ ] Faction creation rules

### 8. xenobestiary.txt / xenobestiary-format.txt
**Use formatted version for:**
- Creature stat blocks

**Extract:**
- [ ] Each creature as separate file
- [ ] Xenobestiary creation rules
- [ ] Creature categories

### 9. adventure-creation.txt
**Extract:**
- [ ] Quick adventure generation
- [ ] Problem templates
- [ ] NPC templates
- [ ] Location templates
- [ ] Reward guidelines

### 10. the-history-of-space.txt
**Extract:**
- [ ] Major historical periods
- [ ] The Scream
- [ ] Mandate era
- [ ] Current era
- [ ] Timeline of events

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