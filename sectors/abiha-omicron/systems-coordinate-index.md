# Systems Coordinate Index

## Navigation
This sector uses a flat-top hexagonal grid. Each system has 6 neighbors.

## Travel Times
- **Base**: 6 days per hex
- **Drive-1**: 6 days
- **Drive-2**: 3 days
- **Drive-3**: 2 days
- **Drive-4**: 1.5 days

## Sector Map (0-indexed)
```text
   00  01  02  03  04  05  06  07
00 -- ME -- EL KA -- AU VI 
01 ER -- -- -- -- HI -- -- 
02 -- -- -- -- -- -- -- -- 
03 KA -- -- -- -- -- -- -- 
04 GU CA VE BU SO -- -- -- 
05 -- -- -- -- ME DU -- -- 
06 -- VA -- -- -- -- -- -- 
07 -- -- -- MA ID -- -- -- 
08 -- -- -- -- HR -- -- -- 
09 -- -- -- -- -- VA -- TS 
```

## Coordinate Reference

| Hex | Coordinates | System | Path |
|-----|-------------|--------|------|
| 00,01 | 1,2 | Erlageusle | [Erlageusle](systems/erlageusle/system--erlageusle.md) |
| 00,03 | 1,4 | Kandrou | [Kandrou](systems/kandrou/system--kandrou.md) |
| 00,04 | 1,5 | Gunn | [Gunn](systems/gunn/system--gunn.md) |
| 01,00 | 2,1 | Mele | [Mele](systems/mele/system--mele.md) |
| 01,04 | 2,5 | Campera | [Campera](systems/campera/system--campera.md) |
| 01,06 | 2,7 | Varadha Shangit XV | [Varadha Shangit XV](systems/varadha-shangit-xv/system--varadha-shangit-xv.md) |
| 02,04 | 3,5 | Vello | [Vello](systems/vello/system--vello.md) |
| 03,00 | 4,1 | Elis | [Elis](systems/elis/system--elis.md) |
| 03,04 | 4,5 | Buruker Urdia | [Buruker Urdia](systems/buruker-urdia/system--buruker-urdia.md) |
| 03,07 | 4,8 | Mardo | [Mardo](systems/mardo/system--mardo.md) |
| 04,00 | 5,1 | Katalin Fra | [Katalin Fra](systems/katalin-fra/system--katalin-fra.md) |
| 04,04 | 5,5 | Sopolyche | [Sopolyche](systems/sopolyche/system--sopolyche.md) |
| 04,05 | 5,6 | Meliadi VIII | [Meliadi VIII](systems/meliadi-viii/system--meliadi-viii.md) |
| 04,07 | 5,8 | Idaracl | [Idaracl](systems/idaracl/system--idaracl.md) |
| 04,08 | 5,9 | Hrefna | [Hrefna](systems/hrefna/system--hrefna.md) |
| 05,01 | 6,2 | Hice | [Hice](systems/hice/system--hice.md) |
| 05,05 | 6,6 | Dul-Yaq | [Dul-Yaq](systems/dul-yaq/system--dul-yaq.md) |
| 05,09 | 6,10 | Vallfdi | [Vallfdi](systems/vallfdi/system--vallfdi.md) |
| 06,00 | 7,1 | Audrima | [Audrima](systems/audrima/system--audrima.md) |
| 07,00 | 8,1 | Vilizad | [Vilizad](systems/vilizad/system--vilizad.md) |
| 07,09 | 8,10 | Tsilas | [Tsilas](systems/tsilas/system--tsilas.md) |

## System Neighbors

### Kandrou
- Southeast: [Campera](systems/campera/system--campera.md)

### Gunn
- Northeast: [Campera](systems/campera/system--campera.md)
- East: [Campera](systems/campera/system--campera.md)

### Campera
- Northwest: [Kandrou](systems/kandrou/system--kandrou.md)
- West: [Gunn](systems/gunn/system--gunn.md)
- East: [Vello](systems/vello/system--vello.md)
- Southwest: [Gunn](systems/gunn/system--gunn.md)
- Southeast: [Vello](systems/vello/system--vello.md)

### Vello
- Northwest: [Campera](systems/campera/system--campera.md)
- Northeast: [Buruker Urdia](systems/buruker-urdia/system--buruker-urdia.md)
- West: [Campera](systems/campera/system--campera.md)
- East: [Buruker Urdia](systems/buruker-urdia/system--buruker-urdia.md)

### Elis
- East: [Katalin Fra](systems/katalin-fra/system--katalin-fra.md)
- Southeast: [Katalin Fra](systems/katalin-fra/system--katalin-fra.md)

### Buruker Urdia
- West: [Vello](systems/vello/system--vello.md)
- East: [Sopolyche](systems/sopolyche/system--sopolyche.md)
- Southwest: [Vello](systems/vello/system--vello.md)
- Southeast: [Sopolyche](systems/sopolyche/system--sopolyche.md)

### Mardo
- East: [Idaracl](systems/idaracl/system--idaracl.md)
- Southeast: [Idaracl](systems/idaracl/system--idaracl.md)

### Katalin Fra
- Northwest: [Elis](systems/elis/system--elis.md)
- West: [Elis](systems/elis/system--elis.md)
- Southeast: [Hice](systems/hice/system--hice.md)

### Sopolyche
- Northwest: [Buruker Urdia](systems/buruker-urdia/system--buruker-urdia.md)
- West: [Buruker Urdia](systems/buruker-urdia/system--buruker-urdia.md)
- Southeast: [Dul-Yaq](systems/dul-yaq/system--dul-yaq.md)

### Meliadi VIII
- Northeast: [Dul-Yaq](systems/dul-yaq/system--dul-yaq.md)
- East: [Dul-Yaq](systems/dul-yaq/system--dul-yaq.md)

### Idaracl
- Northwest: [Mardo](systems/mardo/system--mardo.md)
- West: [Mardo](systems/mardo/system--mardo.md)

### Hrefna
- Southeast: [Vallfdi](systems/vallfdi/system--vallfdi.md)

### Hice
- Northwest: [Katalin Fra](systems/katalin-fra/system--katalin-fra.md)
- Northeast: [Audrima](systems/audrima/system--audrima.md)

### Dul-Yaq
- Northwest: [Sopolyche](systems/sopolyche/system--sopolyche.md)
- West: [Meliadi VIII](systems/meliadi-viii/system--meliadi-viii.md)
- Southwest: [Meliadi VIII](systems/meliadi-viii/system--meliadi-viii.md)

### Vallfdi
- Northwest: [Hrefna](systems/hrefna/system--hrefna.md)

### Audrima
- Northeast: [Vilizad](systems/vilizad/system--vilizad.md)
- East: [Vilizad](systems/vilizad/system--vilizad.md)
- Southwest: [Hice](systems/hice/system--hice.md)

### Vilizad
- West: [Audrima](systems/audrima/system--audrima.md)
- Southwest: [Audrima](systems/audrima/system--audrima.md)
