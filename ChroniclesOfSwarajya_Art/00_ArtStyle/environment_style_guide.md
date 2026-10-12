# Chronicles of Swarajya: The Divine Blade
## Master Environment, Nature & Terrain Style Guide (Phase 2)

---

### 1. Architectural & Environmental Vision
* **Geographical & Historical Setting:** The rugged Sahyadri Western Ghats (Maharashtra), characterized by basalt rock escarpments, steep mountain passes (ghats), lush teak monsoon forests, and formidable Maratha hill forts (Gad & Kille).
* **Perspective & Alignment:** Classic $2.5\text{D}$ top-down view ($\approx 75^\circ$ tilt) strictly aligned with the Phase 1 character sprites.
* **Base Grid Standard:** $16 \times 16\text{ px}$ per fundamental terrain tile. Modular fort modules span $16\times 16$, $32\times 16$, and $32\times 32\text{ px}$. Large Sagwan trees span $32\times 48\text{ px}$ to $40\times 56\text{ px}$.
* **Depth & Occlusion (Y-Sorting):** All large nature assets (trees, pillars, watchtowers, buildings) feature explicitly decoupled collision footprints versus visual canopies. The player walks freely behind the upper canopies while being blocked by the lower trunk/foundation.

---

### 2. Terrain Palette & Material Color Codes

| Token Name | Hex Code | Material Description | Primary In-Game Usage |
|---|---|---|---|
| `GRASS_BASE` | `#3a632a` | Lush Sahyadri forest grass | Standard terrain base |
| `GRASS_DARK` | `#28461d` | Deep forest shadow grass | Shaded groves beneath canopies |
| `GRASS_LIGHT` | `#54873d` | Sunlit grass blades | Field highlights & clearing borders |
| `GRASS_MEADOW` | `#65a30d` | Golden-green highland grass | Elevated plateau clearings |
| `PINE_FLOOR` | `#233818` | Dark mulch & pine needle floor | Dense forest interior ground |
| `MOSS` | `#4d7c0f` | Wet cliff & stone moss | Rock tops & ancient masonry |
| `DIRT_BASE` | `#795538` | Packed red Sahyadri earth | Footpaths, trails, village paths |
| `DIRT_LIGHT` | `#99704e` | Dry worn path center | Trail centerlines & foot-traffic wear |
| `DIRT_DARK` | `#543310` | Moist loam & ditch soil | Path borders & shadow dips |
| `DIRT_MUD` | `#3e240c` | Wet monsoon mud | Riverbank approaches & rainy trails |
| `STONE_GRAY` | `#5e656e` | Sahyadri basalt natural rock | Loose rocks, boulders, cliff tops |
| `STONE_DARK` | `#3c4046` | Shadowed basalt stone | Masonry mortar & rock crevices |
| `STONE_LIGHT` | `#8c939e` | Sunlit stone highlight | Edge bevels on masonry & slabs |
| `STONE_CLIFF` | `#27272a` | Sheer mountain drop face | Impassable mountain wall ridges |
| `FLAGSTONE_BASE` | `#475569` | Dressed fort courtyard stone | Paved courtyards, bastion flooring |
| `FLAGSTONE_TRIM` | `#64748b` | Chiseled parapet edging | Steps, copings, architectural borders |
| `WATER_DEEP` | `#1f487e` | Deep river & moat water | Central river flows, moat depths |
| `WATER_MID` | `#3370b8` | Flowing stream water | Medium-depth streams & cascades |
| `WATER_SHALLOW` | `#60a5fa` | Shoreline shallows | Riverbanks & wading shoals |
| `WATER_FOAM` | `#e0f2fe` | Water crest & splash foam | River edge transitions & rapids |
| `TEAK_BARK` | `#422817` | Sagwan teak tree dark bark | Trunks, timber gates, heavy beams |
| `TEAK_LIGHT` | `#8a5b32` | Teak wood grain highlight | Planks, bridges, wooden carts |
| `SAGWAN_LEAF` | `#65a30d` | Teak broadleaf canopy mid-tone | Sagwan resource tree foliage |
| `SAGWAN_BRIGHT`| `#84cc16` | Fresh monsoon teak shoot | Canopy crown highlights |
| `IRON_CORE` | `#94a3b8` | Raw hematite metallic ore | Harvestable iron ore deposits |
| `GOLD_ORE` | `#f59e0b` | Pyrite/gold mineral vein | Harvestable gold caches & chests |
| `SAFFRON_FLAG` | `#e66012` | Bhagwa Zenda Maratha banner | Fort battlements & shrines |
| `TIMBER_GATE` | `#3b2516` | Ironwood reinforced gate | Heavy bastion portcullis doors |

---

### 3. Layer Hierarchy & Rendering Pipeline

To guarantee visual depth where characters walk naturally behind foliage and walls:

1. **Layer 1: Ground Base** (Walkable floor tiles: grass, dirt paths, water, stone flagstones).
2. **Layer 2: Ground Transitions & Decals** (Grass-dirt blending, fallen leaves, puddles, wild flowers).
3. **Layer 3: Cast Shadows** (Soft elliptical $35\%$ opacity black drop shadows baked onto the ground plane beneath trees, rocks, and buildings).
4. **Layer 4: Impassable Tile Collisions** (Water depths, sheer cliff drops, moat boundaries).
5. **Layer 5: Y-Sorted Entities & Objects** (Player Shivaji, enemies, bosses, tree trunks, boulders, harvestable ore rocks, building base walls). Sorted ascending by `footBaseY = entity.y + entity.collisionH`.
6. **Layer 6: Foreground Overhead Canopies & Roofs** (Sagwan foliage canopies, gatehouse arches, watchtower roofs). Rendered on top of characters when characters walk behind them.
7. **Layer 7: Dynamic Environmental VFX** (Torchlight radial gradients, floating falling leaves, water ripples, windblown dust).

---

### 4. Collision Footprints & Object Specifications

| Asset Name | Visual Size | Collision Footprint (Solid) | Interaction Type | Layer Category |
|---|:---:|:---:|:---:|---|
| **Sagwan Teak Tree** | $32 \times 48\text{ px}$ | $12 \times 8\text{ px}$ at trunk base ($y+40$) | Harvestable (Sagwan Wood) | Y-Sorted Trunk / Overhead Canopy |
| **Forest Broadleaf Tree** | $32 \times 40\text{ px}$ | $10 \times 6\text{ px}$ at trunk base ($y+34$) | Solid Obstacle | Y-Sorted Trunk / Overhead Canopy |
| **Iron Ore Deposit** | $16 \times 16\text{ px}$ | $14 \times 10\text{ px}$ at base ($y+6$) | Harvestable (Iron Ore) | Solid Y-Sorted Object |
| **Gold Mineral Node** | $16 \times 16\text{ px}$ | $14 \times 10\text{ px}$ at base ($y+6$) | Harvestable (Gold) | Solid Y-Sorted Object |
| **Large Basalt Boulder**| $24 \times 20\text{ px}$ | $20 \times 12\text{ px}$ at base | Solid Obstacle | Solid Y-Sorted Object |
| **Fort Battlement Wall**| $32 \times 16\text{ px}$ | $32 \times 16\text{ px}$ full tile | Impassable Barrier | Solid Wall Base |
| **Fort Gatehouse Gate**| $32 \times 32\text{ px}$ | $32 \times 12\text{ px}$ (Locked) / Passable | Level Exit / Milestone | Gate Interactive |
| **Watchtower (Buruj)** | $32 \times 48\text{ px}$ | $28 \times 16\text{ px}$ at base | Solid Structure | Building Structure / Overhead Roof |
| **Armoury / Blacksmith** | $48 \times 40\text{ px}$ | $40 \times 18\text{ px}$ at base | Crafting Station | Building Structure / Overhead Roof |
| **Village Thatched Hut** | $48 \times 40\text{ px}$ | $38 \times 16\text{ px}$ at base | Settlement Landmark | Building Structure / Overhead Roof |
| **Military Pavilion Tent**| $40 \times 32\text{ px}$| $32 \times 14\text{ px}$ at base | Camp Landmark | Y-Sorted Structure |
| **Stone Well** | $20 \times 24\text{ px}$ | $16 \times 12\text{ px}$ at base | Interactive / Obstacle | Y-Sorted Structure |
| **Campfire Ring** | $20 \times 20\text{ px}$ | $12 \times 8\text{ px}$ center | Environmental Light | Ground Decal / Y-Sorted |
| **Wooden Footbridge** | $32 \times 16\text{ px}$ | Passable corridor (borders solid) | Walkway Over Water | Walkable Platform |

---

### 5. Five Regional Biome Themes

1. **Biome A — Sahyadri Forest (Levels 1–15):**
   * Dense teak groves, lush grass meadows, winding red dirt footpaths, clear streams, wild marigold flowers, and rich Sagwan timber deposits.
2. **Biome B — Fortified Settlements (Levels 16–24):**
   * Basalt fort approaches, outer gates, sentry boxes, cobbled flagstone roads, weapon racks, and supply caches.
3. **Biome C — Frontier Wilderness (Levels 26–40):**
   * Rugged rocky passes, sparse vegetation, scree slopes, scout camps, military canvas tents, and iron ore veins.
4. **Biome D — High-Garrison Forts (Levels 41–49):**
   * Heavy stone battlements, round watchtower burujs, cannon emplacements (Topha), flagstone terraces, and iron torch sconces.
5. **Biome E — Raigad Finale (Levels 50–75):**
   * Monumental coronation architecture, carved basalt stone pillars, ceremonial saffron Bhagwa Zenda banners, broad court arenas, and royal throne platforms.
