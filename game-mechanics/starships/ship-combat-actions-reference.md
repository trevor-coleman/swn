# Ship Combat Actions Reference

## Combat Structure

- **Round Length**: ~15 minutes
- **Initiative**: 1d8 + Int/Dex modifier (not rerolled)
- **Department Order**: Captain decides each turn
- **Command Points**: Start at 0, lost at round end

## NPC Ship Command Points
- Fighters/Civilians: 4 CP
- Military/Pirates: 5 CP  
- Native Spacers/Elite: 6 CP
- Finest NPC Crews: 7 CP

## Department Actions

### Bridge Actions

#### Escape Combat (4 CP)
- **Roll**: Opposed Int/Pilot or Dex/Pilot + ship Speed
- **Effect**: On win, enemies gain 1 Escape point
- **Success**: At 3 Escape points, ship escapes that enemy

#### Evasive Maneuvers (2 CP)
- **Roll**: Int/Dex + Pilot vs DC 9
- **Effect**: Add Pilot skill to ship AC until next turn
- **Limit**: Once per round maximum

#### Pursue Target (3 CP)  
- **Roll**: Opposed Int/Pilot or Dex/Pilot + Speed
- **Effect**: Remove 1 Escape point from target

### Captain Actions

#### Into the Fire (0 CP)
- **Effect**: Accept Crew Lost Crisis, gain Lead skill +1 in CP
- **Limit**: Once per round

#### Keep It Together (0 CP)
- **Effect**: Nullify enemy hit, roll Crisis instead
- **Timing**: Instant response to hit
- **Limit**: Once per round

#### Support Department (0 CP)
- **Effect**: One department action costs 2 fewer CP
- **Limit**: Once per round

### Comms Actions

#### Crash Systems (2 CP)
- **Roll**: Opposed Int/Program check
- **Effect**: Target starts next turn with -CP equal to your Program skill

#### Defeat ECM (2 CP)
- **Roll**: Opposed Int/Program check
- **Effect**: Your ship gets +2x Program skill to hit target this round

#### Sensor Ghost (2 CP)
- **Roll**: Int/Program vs DC 9
- **Effect**: Gain Program skill as AC bonus until next turn
- **Limit**: Once per round

### Engineering Actions

#### Boost Engines (2 CP)
- **Roll**: Int/Fix vs DC 8
- **Effect**: +2 Speed until start of next turn

#### Damage Control (3 CP)
- **Roll**: Int/Fix vs DC 7
- **Effect**: Repair HP = Fix skill x2/3/4/6 (fighter/frigate/cruiser/capital)
- **Note**: Each use after first adds +1 difficulty

#### Emergency Repairs (3 CP)
- **Roll**: Int/Fix vs DC 8  
- **Effect**: Repair disabled system or increase degraded drive by 1
- **Note**: Cannot fix destroyed systems

### Gunnery Actions

#### Fire All Guns (3 CP)
- **Effect**: Fire all ship weapons at designated targets

#### Fire One Weapon (2 CP)
- **Effect**: Fire single weapon of choice

#### Target Systems (1 CP)
- **Effect**: Next Fire One Weapon can target specific systems
- **Penalty**: -4 to hit
- **Damage**: Half damage before armor
- **Result**: System disabled or drive degraded if damage penetrates
- **Note**: Can take multiple times for multiple targeted shots

### General Actions (Exclusive)

These prevent any other actions this round:

#### Above and Beyond (0 CP)
- **Roll**: Attribute + Skill vs DC 9 (GM approved)
- **Success**: Gain skill level +1 in CP
- **Failure**: -1 CP

#### Deal With a Crisis (0 CP)
- **Roll**: Relevant skill vs DC 10 (±2 based on plan)
- **Effect**: Resolve one Crisis
- **Alt Use**: Aid another PC or take scene's worth of other actions

#### Do Your Duty (0 CP)
- **Effect**: Ship gains 1 CP
- **Requirement**: Name plausible helpful action
- **Note**: Can't repeat same action two rounds

## Attack Resolution

### Hit Rolls
- Base attack bonus + better of Int/Dex + Shoot skill
- Fighter pilots may use Pilot instead of Shoot
- Warrior luck works once per fight

### Damage
- Roll weapon damage + better of Int/Dex
- Subtract target's Armor (reduced by weapon AP)
- AP cannot add damage beyond reducing armor to 0

### System Targeting
- Requires Target Systems action
- -4 to hit
- Half damage before armor
- Disables system if any damage penetrates
- Disabled systems hit again are destroyed

## Crisis Mechanics

### Accepting Crisis
- Once per round voluntary (not counting captain actions)
- Any department head can request
- Negates the triggering hit completely

### Crisis Resolution  
- Requires Deal With a Crisis action
- Usually DC 10 (±2 based on approach)
- Multiple PCs can cooperate

### Crisis Types
- **Continuing**: Apply penalty until resolved
- **Acute**: Must resolve by end of next round or suffer consequence

## Combat Flow Example

1. **Initiative**: All ships roll, act in order
2. **Ship Turn**:
   - Captain decides department order
   - Departments generate/spend CP
   - All CP lost at turn end
3. **Attacks**: Resolved immediately
4. **Crisis**: Accept instead of damage if desired
5. **Next Ship**: Repeat until all act
6. **New Round**: Return to top of initiative

## Destruction & Escape

### Zero HP
- Fighters: Instantly destroyed
- Larger: Mortally damaged, explodes in 2d6 minutes
- Engineer can prevent explosion: Int/Fix DC 10

### Disabled Engines
- Cannot take Bridge actions
- May be boarded at leisure
- Drive-0 or lower = destroyed engines