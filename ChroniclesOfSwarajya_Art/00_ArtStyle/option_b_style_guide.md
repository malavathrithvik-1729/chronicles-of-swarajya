# Chronicles of Swarajya: The Divine Blade
## Option B Style Guide: 32-Bit High-Resolution Pixel-Art Production

---

### 1. Global Visual Identity & Resolution Standards
* **Art Direction:** Detailed 32-bit high-resolution pixel art inspired by modern retro masterpieces (*Sea of Stars*, *Eastward*, *Chrono Trigger*).
* **Setting:** Authentic 17th-century Western Ghats (Sahyadri), Maratha hill fortresses (*Gad & Kille*), and Deccan sultanate architecture.
* **Canvas Grid & Proportions:**
  * **Protagonist (Shivaji Maharaj):** $48 \times 64\text{ px}$ cell standard. Heroic $1:4.5$ anatomical head-to-body proportion.
  * **Combat / Extended Slash Cell:** $64 \times 64\text{ px}$ cell to accommodate extended curved talwar arc clearance without edge clipping.
  * **Standard Soldiers:** $40 \times 56\text{ px}$ to $44 \times 60\text{ px}$ cells.
  * **Elite Halberdiers & Commanders:** $48 \times 64\text{ px}$ cells.
  * **Major Bosses (Afzal Khan, Aurangzeb):** $64 \times 80\text{ px}$ bespoke cells.
  * **Target Virtual Viewport:** $480 \times 270\text{ px}$ (16:9 widescreen), scaling via integer nearest-neighbor to $1920 \times 1080$ ($4\times$) and $3840 \times 2160$ ($8\times$).

---

### 2. Character Design Specification: Chhatrapati Shivaji Maharaj
* **Pheta (Turban):**
  * Deep crimson base foundation (`#B91C1C`) with overlapping royal saffron folds (`#E66012` and `#F59E0B`).
  * Golden *Sirpech* brooch pinned to the front-left brow (`#FBBF24`), set with a ruby gem (`#BE123C`), white pearl drop pendant, and rising royal plume feather (`#FFFFFF` and `#FEF08A`).
  * Rear *Shimli* tail drape on north/back animations.
* **Facial Features & Grooming:**
  * Clean, dignified Maratha facial silhouette with warm medium skin tones (`#C68642` / `#EBB280`).
  * Forehead adorned with the auspicious red *Chandrakor Tikka* (crescent mark).
  * Prominent, upturned Maratha moustache and neatly trimmed beard framing a resolute jawline.
  * Calm, determined eyes with 1px sclera highlight and dark pupil.
* **Angarkha (Royal Tunic):**
  * Pleated off-white/cream royal cloth (`#FEF3C7` / `#F5E8B4`) with subtle saffron seam accents.
  * Asymmetrical right-chest overlap closure (*Purdah*) with delicate gold trim piping (`#FBBF24`).
  * Double-strand pearl necklace (*Kanthi*) draped around the collar with a central ruby medallion.
* **Kamarbandh (Waist Sash) & Weaponry:**
  * Saffron and gold brocade waist sash (`#E66012` / `#FBBF24`) binding the waist, with a draped sash ribbon hanging down the right hip.
  * Curved steel *Talwar* with a disc-pommel spiked basket hilt and dark leather scabbard (`#451A03` / `#78350F`) slung on the left hip.
* **Lower Garments & Footwear:**
  * Pleated *Churidar* trousers in matching cream tone.
  * Dark brown leather *Mojari* shoes (`#451A03`) featuring traditional curled, pointed toe caps.

---

### 3. Master Animation Pipeline & State Definitions

| Action State | Dimensions | Layout | Frame Count & FPS | Loop | Pivot Anchor | Gameplay Mechanics & Windows |
|---|---|---|---|---|---|---|
| **Idle** | $48 \times 64\text{ px}$ | 4 cols $\times$ 4 rows ($192 \times 256$) | 4 frames @ 3 FPS | Yes | $(24, 58)$ | Subtle breathing bob, ambient cloth sway, hand resting on talwar hilt. |
| **Walk** | $48 \times 64\text{ px}$ | 8 cols $\times$ 4 rows ($384 \times 256$) | 8 frames @ 8 FPS | Yes | $(24, 58)$ | Full athletic stride: contact $\to$ absorption $\to$ passing $\to$ push-off. Angarkha hem sway, arm counter-swing. |
| **Attack (Sword)** | $64 \times 64\text{ px}$ | 6 cols $\times$ 4 rows ($384 \times 256$) | 6 frames @ 10 FPS | No | $(32, 58)$ | Frame 0: Draw $\to$ Frame 1-2: Windup telegraph $\to$ Frame 3: Active hit frame with luminous saffron-gold arc $\to$ Frame 4: Follow-through $\to$ Frame 5: Recovery. |
| **Dodge / Evade** | $48 \times 64\text{ px}$ | 5 cols $\times$ 4 rows ($240 \times 256$) | 5 frames @ 12 FPS | No | $(24, 58)$ | Rapid low sidestep dash with motion silhouette; 0.24s invulnerability window. |
| **Defend / Guard** | $48 \times 64\text{ px}$ | 4 cols $\times$ 4 rows ($192 \times 256$) | 4 frames @ 6 FPS | Hold | $(24, 58)$ | Talwar hilt brought across torso to deflect melee and block projectiles. |
| **Astra Invocation**| $64 \times 64\text{ px}$ | 6 cols $\times$ 3 rows ($384 \times 192$) | 6 frames @ 8 FPS | No | $(32, 58)$ | Mudra elevation, divine blade resonance, elemental burst ring (Agni/Varuna/Bhoomi). |

---

### 4. Directional Conventions (Row Ordering)
Standardized across all multi-directional sprite sheets:
* **Row 0:** South (Facing Forward / Camera)
* **Row 1:** North (Facing Away / Up)
* **Row 2:** East (Facing Right)
* **Row 3:** West (Facing Left)

---

### 5. Dialogue & Cutscene Illustrated Portraits
* Separate high-resolution illustrated character busts ($1024 \times 1024\text{ px}$ painted digital art).
* Preserves costume details, dignified expression, and lighting matching the in-game sprite.
* Rendered in UI dialogue cards and opening cinematic scenes.
