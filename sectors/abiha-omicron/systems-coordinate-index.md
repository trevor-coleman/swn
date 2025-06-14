# System Coordinate Index

This index provides coordinate-to-system mappings for navigation.

## Coordinate Grid

```
     |    x00    |    x01    |    x02    |    x03    |    x04    |    x05    |    x06    |    x07   
-----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
 y00 |     --     |    Mele    |     --     |    Elis    |  Katalin   |     --     |  Audrima   |  Vilizad  
 y01 |  Erlageus  |     --     |     --     |     --     |     --     |    Hice    |     --     |     --    
 y02 |     --     |     --     |     --     |     --     |     --     |     --     |     --     |     --    
 y03 |  Kandrou   |     --     |     --     |     --     |     --     |     --     |     --     |     --    
 y04 |    Gunn    |  Campera   |   Vello    |  Buruker   |  Sopolych  |     --     |     --     |     --    
 y05 |     --     |     --     |     --     |     --     |  Meliadi   |  Dul-Yaq   |     --     |     --    
 y06 |     --     |  Varadha   |     --     |     --     |     --     |     --     |     --     |     --    
 y07 |     --     |     --     |     --     |   Mardo    |  Idaracl   |     --     |     --     |     --    
 y08 |     --     |     --     |     --     |     --     |   Hrefna   |     --     |     --     |     --    
 y09 |     --     |     --     |     --     |     --     |     --     |  Vallfdi   |     --     |   Tsilas  
```

## Coordinates to System

- **0001**: [Erlageusle](systems/Erlageusle/system.md)
- **0003**: [Kandrou](systems/Kandrou/system.md)
- **0004**: [Gunn](systems/Gunn/system.md)
- **0100**: [Mele](systems/Mele/system.md)
- **0104**: [Campera](systems/Campera/system.md)
- **0106**: [Varadha Shangit XV](systems/Varadha Shangit XV/system.md)
- **0204**: [Vello](systems/Vello/system.md)
- **0300**: [Elis](systems/Elis/system.md)
- **0304**: [Buruker Urdia](systems/Buruker Urdia/system.md)
- **0307**: [Mardo](systems/Mardo/system.md)
- **0400**: [Katalin Fra](systems/Katalin Fra/system.md)
- **0404**: [Sopolyche](systems/Sopolyche/system.md)
- **0405**: [Meliadi VIII](systems/Meliadi VIII/system.md)
- **0407**: [Idaracl](systems/Idaracl/system.md)
- **0408**: [Hrefna](systems/Hrefna/system.md)
- **0501**: [Hice](systems/Hice/system.md)
- **0505**: [Dul-Yaq](systems/Dul-Yaq/system.md)
- **0509**: [Vallfdi](systems/Vallfdi/system.md)
- **0600**: [Audrima](systems/Audrima/system.md)
- **0700**: [Vilizad](systems/Vilizad/system.md)
- **0709**: [Tsilas](systems/Tsilas/system.md)

## System to Coordinates

- **Audrima**: 0600 (x6, y0)
- **Buruker Urdia**: 0304 (x3, y4)
- **Campera**: 0104 (x1, y4)
- **Dul-Yaq**: 0505 (x5, y5)
- **Elis**: 0300 (x3, y0)
- **Erlageusle**: 0001 (x0, y1)
- **Gunn**: 0004 (x0, y4)
- **Hice**: 0501 (x5, y1)
- **Hrefna**: 0408 (x4, y8)
- **Idaracl**: 0407 (x4, y7)
- **Kandrou**: 0003 (x0, y3)
- **Katalin Fra**: 0400 (x4, y0)
- **Mardo**: 0307 (x3, y7)
- **Mele**: 0100 (x1, y0)
- **Meliadi VIII**: 0405 (x4, y5)
- **Sopolyche**: 0404 (x4, y4)
- **Tsilas**: 0709 (x7, y9)
- **Vallfdi**: 0509 (x5, y9)
- **Varadha Shangit XV**: 0106 (x1, y6)
- **Vello**: 0204 (x2, y4)
- **Vilizad**: 0700 (x7, y0)

## Hex Grid Navigation

This is a **flat-top hex grid**. Each system has up to 6 neighbors:

```
    (-1,-1)  (0,-1)
       \      /
(-1,0) - HEX - (+1,0)
       /      \
    (0,+1)  (+1,+1)
```

Neighbor offsets from any hex (x,y):
- Northwest: (x-1, y-1)
- Northeast: (x, y-1)
- West: (x-1, y)
- East: (x+1, y)
- Southwest: (x, y+1)
- Southeast: (x+1, y+1)

## Distance Calculations

For flat-top hex grids, the distance between two hexes (x1,y1) and (x2,y2) is:

```
dx = x2 - x1
dy = y2 - y1

if sign(dx) == sign(dy):
    distance = max(abs(dx), abs(dy))
else:
    distance = abs(dx) + abs(dy)
```

## Space Travel Times

**Spike Drive Travel** (between systems):
- Base time: **6 days per hex**
- Drive-1: 5 days/hex
- Drive-2: 4 days/hex
- Drive-3: 3 days/hex
- Drive-4: 2 days/hex
- Drive-5: 1 day/hex

**In-System Travel**:
- Between planets/stations: 24-48 hours
- To outer system: up to 6 days

*For full travel rules, see [Space Travel Times](../../game-mechanics/space-travel-times.md)*
