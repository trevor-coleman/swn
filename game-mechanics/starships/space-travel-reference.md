# Space Travel Reference

## Spike Drive Basics

### Requirements
- Must be at edge of solar system (gravity well transition zone)
- Cannot overshoot arrival zones
- Arrive at edge corresponding to origin direction
- Can depart from any edge location

### Drive Ratings & Range
- **Range**: Drive rating in hexes
- **Speed**: 6 days per hex ÷ drive rating
- **Examples**:
  - Drive-1: 1 hex range, 6 days/hex
  - Drive-2: 2 hex range, 3 days/hex
  - Drive-3: 3 hex range, 2 days/hex

## Making a Spike Drill

### Requirements
1. **Fuel**: 1 load (500 credits)
2. **Time**: 30 minutes standard (1 combat round if rushed)
3. **Course Record** (Rutter): Navigation data
4. **Pilot**: Sentient crew (minimum 3 for safety)

### Skill Check
- **Roll**: Int/Pilot
- **Base DC**: 7
- **Auto-Success**: Final DC 6 or less

### Difficulty Modifiers

| Condition | Modifier |
|-----------|----------|
| Uncharted course | +6 |
| Rutter 5+ years old | +2 |
| Rutter 1-5 years old | +1 |
| Rutter <1 year old | +0 |
| Rutter <1 month old | -2 |
| Per 2 full hexes distance | +1 |
| Trimming course | +2 |
| Rushed activation | +2 |

### Course Trimming
- **Effect**: +1 effective drive rating for speed only
- **Cost**: +2 to difficulty
- **Note**: Doesn't increase maximum range

## Spike Drill Mishaps (3d6)

| Roll | Result |
|------|--------|
| 3 | **Catastrophic Incursion**: Emerge at star within 1d6 hexes with all systems destroyed |
| 4-5 | **Shear Surge**: Emerge at nearest star to origin. 50% chance each system disabled |
| 6-8 | **Power Spike**: One system disabled, stuck in transit for full time before retry |
| 9-12 | **Off Course**: Spend full transit time, then retry navigation |
| 13-15 | **Off Course (Detected)**: Make another Pilot check immediately |
| 16-17 | **Slow Success**: Arrive safely but takes 2× base time |
| 18 | **Blind Luck**: Successful arrival on time despite failure |

**Note**: If spike drive disabled on rolls 3-5, treat as catastrophic (roll 3)

## Intra-System Travel

### Regions
- Any significant location = 1 region
- Examples: Planets, stations, asteroid belts, arrival zones

### Base Travel Times
- **Within Region**: 6 hours
- **Between Regions**: 48 hours
- **Speed**: Divide by spike drive rating

### Course Trimming (In-System)
- **Check**: Pilot DC 9
- **Success**: +1 effective drive rating
- **Failure**: Takes 2× normal time

### Examples
- Drive-2 ship, same region: 3 hours
- Drive-3 ship, between regions: 16 hours
- Drive-1 ship with successful trim: 24 hours between regions

## Detection & Stealth

### Detection Lock
- **Check**: Opposed Int/Program
- **Range**: Same region only
- **Active Sensors**: Target knows if locked
- **Passive Sensors**: -2 penalty, undetectable
- **Duration**: Maintained across regions with new check

### Detection Modifiers

**Observer Size**:
- Fighter: +0
- Frigate: +1
- Cruiser: +2
- Capital: +3
- Minor Outpost: +2
- Major Station: +4
- Planet: +5
- Passive Sensors: -2

**Target Size**:
- Fighter: +3
- Frigate: +2  
- Cruiser: +1
- Capital: +0
- Station: -2
- Avoiding Population: +2

### Breaking Detection
1. Leave current region
2. Make new opposed check
3. Observer wins = maintains lock
4. Tie/Loss = lock broken

## Pursuit Mechanics

### Requirements
- Same region as target
- Detection lock on target

### Chase Resolution
1. **Opposed Check**: Int/Pilot + drive rating
2. **Pursuer Wins/Ties**: Forces engagement
3. **Target Wins**: Gains 6 hours ÷ drive difference

### Escape Times by Drive
- Drive-1: 48 hours to new region
- Drive-2: 24 hours to new region
- Drive-3: 16 hours to new region

## Scanning

### Automatic Information
**Ships** (combat range):
- Hull type
- Obvious weapons/damage
- Registered ID

**Planets** (orbit):
- Atmosphere
- Basic geology  
- Energy-using communities
- Other ships in orbit
- Designed surface features

### Interrogation Questions
- **Check**: Int/Program DC 8
- **First Question**: Free
- **Additional**: +1 DC each
- **Failure**: No more questions that day

### Example Questions
**Ships**:
- Specific fittings present?
- Best boarding points?
- World of origin?
- Anything unusual?

**Planets**:
- Capital/spaceport locations?
- Major industrial sites?
- Weather patterns?
- Hidden communities?
- Current news?

### Survey Sensors
- +2 to checks
- Read newsprint from orbit
- Subsurface/interior mapping
- Detailed life form analysis

## Maintenance & Fuel

### Fuel Costs
- 500 credits per load
- Most ships hold 1 load
- Fuel Bunkers add capacity
- No fuel use for in-system travel

### Maintenance Schedule  
- **Cost**: 5% of ship cost every 6 months
- **Penalty**: -1 all checks per missed period
- **At -4**: 10% monthly breakdown chance
- **Time**: 1 day (fighter), 1 week (frigate/cruiser), 1 month (capital)

### Field Repairs
- **Parts**: 1 ton cargo = 10,000 credits supplies
- **Time**: 4× normal at shipyard
- **Hull**: 1,000 credits/HP, Fix skill/day
- **Systems**: 
  - Jury-rig: 10% cost, 1 day/25k
  - Full repair: 25% original cost

## Common Routes

### Safe Drilling
- Recent rutters (<1 month): DC 5
- Known routes ≤2× pilot skill: Auto-success with Drill Course Regulator
- Well-traveled trade routes: Often DC 6 or less

### Dangerous Drilling  
- Uncharted: DC 13+ (often suicidal)
- Old rutters: DC 9-10
- Trimmed routes: +2 DC for speed
- Combat drilling: DC 9-11 rushed

### Emergency Procedures
- **Combat Drill**: 1 round instead of 30 minutes, +2 DC
- **Surface Launch**: Possible with Emergency Drill Activation mod
- **Desperate Solo**: Heavy drugs for 1-week consciousness