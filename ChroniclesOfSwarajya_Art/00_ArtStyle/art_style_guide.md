# Chronicles of Swarajya: The Divine Blade
## Master Art Style Guide & Pixel-Art Specification (Phase 1)

---

### 1. Global Visual Philosophy & Art Direction
* **Genre Inspiration:** 16-bit retro top-down action RPGs (classic SNES/Mega Drive era).
* **Setting:** 17th-century Sahyadri mountain ranges, Maratha hill forts (Gad & Kille), forested ghats, and royal Maratha strongholds.
* **Respectful Authenticity:** Shivaji Maharaj is depicted with authentic Maratha regalia—saffron and crimson pheta (turban), golden sirpech, regal angarkha, gold kamarbandh sash, white dhoti, dark leather mojari footwear, and a steel Talwar.
* **Pixel Density & Grid:**
  * Base terrain grid: $16 \times 16\text{ px}$.
  * Standard characters (Shivaji): $24 \times 32\text{ px}$ cell size.
  * Standard enemies: $16 \times 24\text{ px}$ to $22 \times 28\text{ px}$.
  * Major Bosses: $28 \times 36\text{ px}$ to $36 \times 44\text{ px}$.
  * Logical Game Canvas: $160 \times 160\text{ px}$ (crisp integer nearest-neighbor scaling).

---

### 2. Master Color Palette Specifications

| Category | Swatch / Token | Hex Value | Primary Application |
|---|---|:---:|---|
| **Maratha Regalia** | `SAFFRON` | `#e66012` | Primary royal angarkha (tunic), banners |
| | `SAFFRON_LIGHT`| `#f59e0b` | Tunic highlights, sash accents |
| | `SAFFRON_DARK` | `#b45309` | Cloth folds, shadow drapery |
| | `TURBAN_RED` | `#b91c1c` | Traditional pheta foundation, sash edge |
| | `RUBY` | `#7f1d1d` | Turban jewel, royal brooch |
| | `GOLD` | `#fbbf24` | Sirpech feather pin, hilt accents |
| | `DHOTI` | `#fef3c7` | Traditional pleats & trousers |
| | `MOJARI` | `#451a03` | Leather footwear & belt scabbards |
| **Anatomy & Metal** | `SKIN` | `#c68642` | Skin base tone |
| | `SKIN_LIGHT` | `#dfa064` | Brow & nose highlights |
| | `SKIN_DARK` | `#8d5b2d` | Shadow beneath turban & chin |
| | `BEARD` | `#1c1917` | Moustache, beard & hair |
| | `STEEL` | `#e2e8f0` | Talwar blade, helmet rims |
| | `STEEL_LIGHT` | `#ffffff` | Blade slash glare, edge glint |
| | `STEEL_DARK` | `#64748b` | Blade core, chainmail backing |
| **Adversaries** | `MUGHAL_GREEN` | `#166534` | Basic swordsman & archer uniforms |
| | `MUGHAL_DARK` | `#14532d` | Shadow folds in enemy tunics |
| | `BRASS` | `#ca8a04` | Shield guard kite shield, buckles |
| | `BRIGANDINE_RED`| `#991b1b`| Charging soldier heavy brigandine |
| | `CHARGER_HORN` | `#fde047`| Warning horned crest on chargers |
| | `ELITE_ARMOR` | `#475569`| Fortress elite polished plate armor |
| | `ELITE_PURPLE` | `#581c87`| Elite garrison ceremonial plumes |
| **Bosses** | `AFZAL_PURPLE` | `#4a154b`| Afzal Khan's royal Bijapur velvet robe |
| | `AFZAL_GOLD` | `#ca8a04`| Brocade gold hem & massive talwar trim |
| | `SHAISTA_DARK` | `#1e293b`| Lal Mahal night robes, stealth silk |
| | `AURANGZEB_GOLD`| `#b45309`| Imperial Mughal throne armor |
| | `AURANGZEB_CROWN`| `#15803d`| Imperial crown emerald setting |
| **Astra VFX** | `FIRE_CORE` | `#ffffff`| Agni inner incandescent core |
| | `FIRE_YELLOW` | `#fde047`| Agni mid flame |
| | `FIRE_ORANGE` | `#f97316`| Agni expanding flame perimeter |
| | `WATER_CYAN` | `#38bdf8`| Varuna swirling torrent & shield |
| | `WATER_BLUE` | `#0284c7`| Varuna deep restorative pulse |
| | `EARTH_OCHRE` | `#d97706`| Bhoomi seismic dust cloud |
| | `EARTH_CRACK` | `#451a03`| Bhoomi ground fissure outline |

---

### 3. Lighting, Perspective & Outline Rules
1. **Perspective:** Classical $2.5\text{D}$ top-down view ($\approx 75^\circ$ tilt). The front of characters (turban, face, chest, belt, footwear) is clearly visible while their foot base defines their spatial ground plane.
2. **Lighting Direction:** Top-left celestial key light. Highlights appear on the upper-left of turbans, shoulders, and blade edges; cast shadows fall directly beneath character feet ($3\text{px}$–$5\text{px}$ elliptical dark drop shadow with $35\%$ opacity).
3. **Outlines:**
   * Selective black/dark outlines (`#1c1917` and `#451a03`) around character silhouettes.
   * Internal boundaries use dark tones of the respective material (e.g. `SAFFRON_DARK` for tunic folds, never stark black lines across clothing).
   * Weapon edges use white glints (`#ffffff`) on the active cutting side.

---

### 4. Animation Timing & Frame Rates

| Action | Frame Count | Recommended FPS | Duration | Anticipation / Action / Recovery |
|---|:---:|:---:|:---:|---|
| **Idle** | 2 frames | 2 FPS | 1.0s loop | Subtle 1px vertical breathing bob |
| **Walk (4-Dir)** | 4 frames | 6 FPS | 0.67s loop | Contact (L) $\to$ Pass $\to$ Contact (R) $\to$ Pass |
| **Sword Attack** | 3 frames | 8 FPS | 0.38s | 1f Windup $\to$ 1f Active Blade Arc $\to$ 1f Follow-through |
| **Dodge Roll** | 3 frames | 10 FPS | 0.30s | 1f Crouch $\to$ 1f Mid-Roll $\to$ 1f Landing Recovery |
| **Astra Cast** | 3 frames | 6 FPS | 0.50s | 1f Elemental Charge $\to$ 1f Mudra Elevation $\to$ 1f Burst |
| **Hurt / Stagger** | 2 frames | 6 FPS | 0.33s | 1f Recoil $\to$ 1f Stagger Return |
| **Victory Pose**| 2 frames | 3 FPS | 0.67s loop | Talwar hoisted high in royal salute |

---

### 5. Naming & Directory Conventions

```text
ChroniclesOfSwarajya_Art/
├── 00_ArtStyle/
│   ├── art_style_guide.md       # This comprehensive specification
│   ├── palette.png              # 160x80 color swatch table
│   └── asset_manifest.json      # Complete machine-readable animation manifest
├── 01_Shivaji/
│   ├── shivaji_idle.png         # 48x128 (4 directions x 2 frames, 24x32 cells)
│   ├── shivaji_walk.png         # 96x128 (4 directions x 4 frames, 24x32 cells)
│   ├── shivaji_attack.png       # 72x128 (4 directions x 3 frames, 24x32 cells)
│   ├── shivaji_dodge.png        # 72x128 (4 directions x 3 frames, 24x32 cells)
│   ├── shivaji_astra_cast.png   # 72x96 (3 Astras x 3 frames, 24x32 cells)
│   └── shivaji_hurt_victory.png # 48x64 (2 states x 2 frames, 24x32 cells)
├── 02_Enemies/
│   ├── swordsman.png            # 64x96 (4 states x 4 frames, 16x24 cells)
│   ├── shield_guard.png         # 72x96 (4 states x 4 frames, 18x24 cells)
│   ├── archer.png               # 64x96 (4 states x 4 frames, 16x24 cells)
│   ├── charging_soldier.png     # 80x96 (4 states x 4 frames, 20x24 cells)
│   └── elite_guard.png          # 88x112 (4 states x 4 frames, 22x28 cells)
├── 03_Bosses/
│   ├── afzal_khan.png           # 108x176 (4 states x 3 frames, 36x44 cells)
│   ├── shaista_khan.png         # 84x144 (4 states x 3 frames, 28x36 cells)
│   └── aurangzeb.png            # 108x176 (4 states x 3 frames, 36x44 cells)
├── 04_AstraEffects/
│   ├── agni_effects.png         # 128x64 (8 frames, 32x32 cells)
│   ├── varuna_effects.png       # 128x64 (8 frames, 32x32 cells)
│   └── bhoomi_effects.png       # 128x64 (8 frames, 32x32 cells)
├── 05_Weapons/
│   ├── talwar_basic.png         # 16x16 transparent weapon icon
│   ├── talwar_upgraded.png      # 16x16 transparent weapon icon
│   ├── halberd_elite.png        # 16x24 transparent weapon icon
│   ├── bow_and_arrow.png        # 16x16 transparent weapon icon
│   ├── shield_guard.png         # 16x16 transparent shield icon
│   ├── sword_slash_arc.png      # 24x24 blade swing arc overlay
│   ├── arrow_projectile.png     # 12x6 projectile sprite
│   └── hit_flash.png            # 16x16 impact spark
└── 06_Previews/
    └── character_gallery.png    # Complete side-by-side roster showcase
```
