# Ship Crisis Reference

## Crisis Mechanics

### When to Accept Crisis
- **Voluntary**: Once per round maximum (not counting captain actions)
- **Trigger**: Immediately after damage is rolled
- **Authority**: Any department head can request
- **Effect**: Completely negates the triggering hit

### Captain Crisis Actions
- **Keep It Together**: Nullify hit, roll Crisis (once/round)
- **Into the Fire**: Accept Crew Lost Crisis for Command Points
- These don't count against voluntary Crisis limit

### Crisis Types
- **Continuing**: Apply ongoing penalty until resolved
- **Acute**: No immediate penalty, but consequence if not resolved by end of next round

## Crisis Table (d10)

### 1. Armor Loss (Continuing)
**Description**: Hit melted armor patch, cracked support, or exposed sensitive system
**Effect**: Ship's Armor rating halved (round down)
**Example Descriptions**:
- "Molten armor plating is peeling away from the hull"
- "Internal supports buckled, leaving systems exposed"
- "Critical armor junction compromised"

### 2. Cargo Loss (Acute)
**Description**: Hit gored open cargo bay, threatening to dump hold
**Effect**: If not resolved by end of next round, lose d10×10% of cargo
**Example Descriptions**:
- "Cargo bay doors blown off, contents venting to space"
- "Gravity plates failed, cargo breaking free"
- "Hull breach in forward cargo hold"

### 3. Crew Lost (Acute)
**Description**: Brave crew risk lives to keep damaged systems operating
**Effect**: If not resolved by end of next round:
- Lose 10% of max crew (not counting Extended Life Support)
- Half are dead/permanently disabled
- Half return to duty in 1 week
- Extended Medbay halves casualties
- If no NPC crew left: Random PC rolls Physical save
  - Success: Lose half HP
  - Failure: Mortally wounded (must stabilize by end of turn or die)
**Example Descriptions**:
- "Damage control team trapped in burning engine room"
- "Hull breach threatening to decompress crew quarters"
- "Radiation leak in engineering section"

### 4. Engine Lock (Continuing)
**Description**: Engine jammed or control circuits non-responsive
**Effect**: No bridge actions possible (pilot can still do general actions)
**Example Descriptions**:
- "Navigation controls frozen, helm not responding"
- "Drive plasma conduits fused shut"
- "Maneuvering thrusters offline"

### 5. Fuel Bleed (Acute)  
**Description**: Fuel tanks holed or emergency vents force-triggered
**Effect**: If not resolved by end of next round, lose all fuel except minimum for in-system operation
**Example Descriptions**:
- "Fuel tanks ruptured, hydrogen streaming into space"
- "Emergency purge sequence activated"
- "Micrometeor pierced primary fuel bunker"

### 6. Haywire Systems (Continuing)
**Description**: Critical command links damaged or disordered
**Effect**: Ship starts each round at -2 Command Points
**Note**: Multiple Crises stack this penalty
**Example Descriptions**:
- "Main computer rebooting constantly"
- "Power fluctuations disrupting all systems"
- "Command pathways severed between departments"

### 7. Hull Breach (Acute)
**Description**: Hull damaged, about to tear open important compartment
**Effect**: If not resolved by end of next round, take damage ignoring Armor:
- Fighter: 1d10
- Frigate: 2d10
- Cruiser: 3d10  
- Capital: 4d10
**Example Descriptions**:
- "Stress fractures spreading across hull plating"
- "Bulkhead about to blow out"
- "Support beam cracking under strain"

### 8. System Damage (Continuing)
**Description**: Ship system cooked by hit
**Effect**: GM randomly picks weapon/fitting/engine:
- System disabled (as if targeted shot hit)
- Drives lose 1 level
- Already disabled systems are destroyed
- Drive-0 or below = destroyed
**Example Descriptions**:
- "Plasma surge fried the [system]"
- "Feedback loop burned out [system] controls"
- "Impact shock disabled [system]"

### 9. Target Decalibration (Continuing)
**Description**: Gunnery computers hopelessly confused
**Effect**: Cannot lock weapons on target
**Example Descriptions**:
- "Targeting sensors showing ghost images"
- "Fire control computer crashed"
- "Weapon alignment servos jammed"

### 10. VIP Imperiled (Acute)  
**Description**: Damage threatens random PC or important NPC
**Effect**: 
- Victim immediately rolls Physical save
  - Success: Lose half HP
  - Failure: Mortally wounded
- NPC crew get free stabilization attempt
- If NPC fails, PC must Deal With Crisis to save by end of turn or victim dies
**Example Descriptions**:
- "Explosion in [character]'s compartment!"
- "[Character] caught in decompression!"
- "Falling debris about to crush [character]!"

## Resolving Crises

### Deal With a Crisis Action
- **Who**: Any PC can attempt
- **How**: Describe solution approach
- **Roll**: Relevant skill vs DC 10
- **Modifiers**: ±2 based on plan quality
- **Success**: Crisis resolved immediately
- **Multiple PCs**: Can cooperate using aid rules

### Example Resolutions

**Armor Loss**:
- Fix: "Rerouting power to emergency armor fields" (Int/Fix)
- Program: "Recalibrating defensive grid patterns" (Int/Program)
- Exert: "Manually welding emergency patches" (Str/Exert)

**Crew Lost**:
- Lead: "Organizing evacuation of danger zone" (Cha/Lead)
- Fix: "Sealing bulkheads and venting fires" (Int/Fix)
- Heal: "Setting up emergency triage station" (Int/Heal)

**Engine Lock**:
- Fix: "Bypassing damaged control circuits" (Int/Fix)
- Program: "Hacking nav computer to restore control" (Int/Program)  
- Pilot: "Manual override through auxiliary systems" (Dex/Pilot)

**Hull Breach**:
- Fix: "Emergency force field generators" (Int/Fix)
- Telekinesis: "Holding hull plates together" (Psychic power)
- Exert: "Bracing support beams manually" (Str/Exert)

## GM Guidelines

### Describing Crises
1. Make it concrete and visual
2. Locate it somewhere specific on ship
3. Create immediate tension
4. Suggest (but don't require) possible solutions

### Setting Difficulty
- **Base**: DC 10
- **Good Plan**: DC 8 (-2)
- **Excellent Plan**: DC 8 with advantage
- **Poor Plan**: DC 12 (+2)
- **Terrible Plan**: DC 12 with disadvantage

### NPC Ships
- Rarely accept more than 1 Crisis per combat
- Usually just take damage until facing destruction
- Simplifies combat tracking

## Crisis Stacking

- Same Crisis can occur multiple times
- Continuing penalties stack (especially Haywire Systems)
- Empty cargo holds/dry fuel tanks may have no effect
- System Damage on destroyed system rerolls