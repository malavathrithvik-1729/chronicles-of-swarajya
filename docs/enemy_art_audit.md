# Audit & Diagnostic Report: Enemy Character Art vs Option B Visual Benchmark

**Project:** *Chronicles of Swarajya: The Divine Blade*  
**Phase:** Gate C — Open-World Environment Art, World Setting & Enemy Character Redesign  
**Deliverable:** Gate C1 — Diagnostic Art Audit & Remediation Plan  
**Date:** October 2026  
**Status:** Implementation Active

---

## 1. Executive Summary

Following the approval of **Option B: Detailed 32-Bit High-Resolution Pixel Art** and the production of the benchmark protagonist sprite sheets for **Chhatrapati Shivaji Maharaj** (`ChroniclesOfSwarajya_Art/01_Shivaji/`), this audit rigorously evaluates the current enemy roster assets. 

While the preliminary generator scripts (`tools/build_option_b_enemies.py`) established functional collision footprints and basic 4-directional sprite sheet layouts, an objective pixel-level inspection reveals stark qualitative divides between the protagonist and the adversary units. Shivaji displays 26 harmonious palette tones, organic fabric draping, articulated anatomical mass, and unmistakable silhouette cues. In contrast, the current enemy sprites exhibit rudimentary boxy block geometries, harsh outlines, flat fills (often only 10 to 14 unique colors), stiff pose dynamics, and insufficient combat telegraphs.

This document diagnoses the exact flaws in the enemy roster—focusing specifically on the **Swordsman** and **Shield Guard**—and defines the structural artistic standards required to bring every enemy up to the approved Option B standard.

---

## 2. Benchmark Standard: Chhatrapati Shivaji Maharaj

The approved Option B Shivaji character sheets establish the inviolable baseline for fidelity, lighting, materials, and silhouette design:

* **Grid & Resolution:** Standard cells are $48 \times 64\text{ px}$; sword attack cells expand to $64 \times 64\text{ px}$ to accommodate the blade trajectory without cropping.
* **Anatomical Proportions:** Heroic $1:4.5$ head-to-body proportion; clearly articulated shoulder girdle, ribcage, hip pivot, and knee flexion.
* **Palette Depth:** 26 deliberate color tokens spanning 4-step shading ramps (e.g., `SKIN_HI`, `SKIN_BASE`, `SKIN_SHADOW`, `SKIN_DEEP`).
* **Material Distinction:** Distinct tactile responses for pleated cream *angarkha* cloth, saffron silk *kamarbandh* sash, dark burnished leather *mojari* with curved tips, polished Damascus steel, and brushed gold jewelry with ruby insets.
* **Directional Integrity:** Full 4-directional continuity (South, North, East, West) with dedicated hair, plume, scabbard, and belt draping transitions.
* **Lighting Logic:** Unbroken top-left ($315^\circ$) directional lighting key with subtle ambient ground bounce.

---

## 3. Systematic Diagnosis of Current Enemy Sprites

### 3.1 Common Deficiencies Across All Preliminary Enemy Sprites

1. **Overly Simplified Geometric Blocking:** Bodies are constructed primarily from rigid vertical rectangles (`draw_pixel_rect`), producing wooden, stiff postures devoid of natural weight shift (contrapposto).
2. **Poverty of Color Depth & Tonal Ramps:** Preliminary enemies use only 10–14 colors. Fabrics lack mid-tone fold transitions; metals lack specularity, specular bounce, and dark core shadows.
3. **Flat Silhouettes & Lack of Asymmetry:** Limbs and torsos are centered symmetrically, making characters read like paper cutouts rather than 3D volumes standing in a $2.5\text{D}$ world space.
4. **Weak Combat Readability & Poor Tell Telegraphing:** Attack animations lack anticipatory wind-up frames (anticipation, stretch, snap, recovery), making them visually abrupt and hard to dodge or parry.
5. **Incoherent Material Language:** Leather, iron, brass, and rough Deccan wool look identical in texture, separated only by flat hue swaps rather than distinctive cluster dither and shading styles.

---

### 3.2 Specific Unit Audit: Deccan Swordsman

| Evaluation Parameter | Current State (Preliminary) | Target Option B Standard (Benchmark) | Diagnostic Severity |
|---|---|---|:---:|
| **Cell Dimension** | $40 \times 56\text{ px}$ (Idle/Walk), $56 \times 56\text{ px}$ (Attack) | Retain $40 \times 56\text{ px}$ (Idle/Walk), $56 \times 56\text{ px}$ (Attack) | Baseline OK |
| **Color Palette Depth** | 14 raw RGB colors | Minimum 20–24 harmonious tokens across Deccan green, quilted gambeson, leather, mail, and steel | **High** |
| **Headgear & Turban** | Simplified cylindrical steel helmet with 2px brass crest | Authentic Maratha/Deccan quilted turban (*Mandil*) interwoven with steel plates, chainmail aventail (*Zirah*) neck guard | **Critical** |
| **Torso & Armour** | Flat green rectangle (`cx-6` to `cx+6`) with a single 2px belt | Quilted textile *angarkha* reinforced with riveted leather brigandine, waist sash, brass belt buckle, and scabbard frog | **Critical** |
| **Weapon Representation** | 2px wide static grey stick | Authentic curved Deccan *Talwar* with disc pommel, crossguard quillons, blood groove, and specular edge gleam | **High** |
| **Idle Stance & Breathing** | Rigid vertical 1px bob | Athletic, low-center-of-gravity combat ready stance; feet shoulder-width, knees slightly bent, subtle breathing torso expansion | **High** |
| **Attack Dynamics** | 6-frame attack simply shifts sprite 3px and draws a basic vector arc | 6-frame telegraphed strike: Frame 0 (Neutral stance) $\to$ Frame 1-2 (Rear shoulder coil & wind-up) $\to$ Frame 3 (Explosive lunge with sharp curved steel slash trail) $\to$ Frame 4 (Deep momentum follow-through) $\to$ Frame 5 (Step recovery) | **Critical** |

---

### 3.3 Specific Unit Audit: Heavy Shield Guard

| Evaluation Parameter | Current State (Preliminary) | Target Option B Standard (Benchmark) | Diagnostic Severity |
|---|---|---|:---:|
| **Cell Dimension** | $44 \times 58\text{ px}$ (Idle/Walk), $60 \times 58\text{ px}$ (Attack) | Retain $44 \times 58\text{ px}$ (Idle/Walk), $60 \times 58\text{ px}$ (Attack) | Baseline OK |
| **Color Palette Depth** | 10 colors | Minimum 22–26 tones capturing heavy iron, brass patina, buffalo hide, and padded red undergarments | **High** |
| **Shield Realism (Dhal)** | Flat oval with 4 mechanical dots | Authentic 17th-century convex rhino/buffalo-hide *Dhal* shield with 4 hemispherical polished brass bosses (*Katori*), central crescent motif, and rim reinforcement studs | **Critical** |
| **Defensive Stance** | Symmetrical upright standing position; shield floating at hip | Braced, forward-angled phalanx posture; weight anchored onto rear foot, shield planted forward covering torso, talwar or heavy club held ready behind rim | **Critical** |
| **Armour Craftsmanship** | Red rectangle with a grid of 9 single yellow pixels | Heavy *Char-Aina* (four-mirror) plate armour or padded lamellar coat over mail, conical iron helmet (*Kulak*) with nasal bar and mail neck guard | **Critical** |
| **Attack & Shield Bash Dynamics** | Sword poke only; shield remains static | Powerful 2-phase combat threat: Frame 1-2 (Shield coil back) $\to$ Frame 3 (Heavy forward shield thrust / stun bash) $\to$ Frame 4 (Follow-up talwar cleave over shield rim) $\to$ Frame 5-6 (Braced reset) | **Critical** |

---

## 4. Visual World Setting Cohesion Plan

To ensure enemies, Shivaji, and the surrounding open world exist in a singular artistic universe:

1. **Shared Shading Vocabulary:** All humanoid sprites utilize cluster-based pixel dithering for cloth, crisp contiguous highlights for metals, and dark warm outlines (`#1a1412`) to prevent cutout distortion.
2. **Ground Contact & Shadow Standard:** Every grounded entity casts a soft semi-transparent elliptical drop shadow (`#0f0c0a` with $\alpha \approx 110$) calibrated to its physical footprint, anchoring it directly into the terrain tile grid.
3. **Anatomical Scale Ratio:** All standard infantry share an identical head height ratio ($\approx 12\text{ px}$ head, $18\text{ px}$ torso, $20\text{ px}$ legs), maintaining instant silhouette readability alongside Shivaji ($13\text{ px}$ head, $20\text{ px}$ torso, $24\text{ px}$ legs).
4. **Animation Timing & Telegraphed Gameplay Windows:**
   - Idle: 4 frames @ 3–4 FPS (subtle, rhythmic organic cycles).
   - Walk: 8 frames @ 6–8 FPS (full heel-strike, pass, push-off locomotion).
   - Attack: 6 frames @ 8–10 FPS with distinct visual telegraphing:
     - *Telegraph Window (Frames 1–2):* Provides the player 200–250ms visual warning to parry or dodge.
     - *Active Window (Frame 3):* Instantaneous strike with glowing blade slash VFX.
     - *Recovery Window (Frames 4–5):* Vulnerability window where enemy cannot guard.

---

## 5. Execution Roadmap for Gate C

* **Gate C1 (Current):**
  - Publish this diagnostic audit (`docs/enemy_art_audit.md`).
  - Redraw **Swordsman** and **Shield Guard** to Option B benchmark quality across all states (`idle`, `walk`, `attack`).
  - Render 3 master Sahyadri widescreen environment preview artworks ($480 \times 270\text{ px}$).
  - Update `character_viewer.html` studio, preview galleries, and asset manifests.
* **Gate C2 (Subsequent):**
  - Redraw remaining enemies (Archer, Charging Soldier, Elite Halberdier, Spear Soldier).
  - Expand world tilesets to high-res 32-bit standards.
* **Gate C3 (Subsequent):**
  - Open-World Environment production (cliffs, fortresses, rivers, flora).
* **Gate C4 (Subsequent):**
  - Interactive Open-World Playable Slice (`open_world_visual_prototype.html`).
