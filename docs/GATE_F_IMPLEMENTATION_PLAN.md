# GATE F — STEP-BY-STEP IMPLEMENTATION PLAN
## Transforming Chronicles of Swarajya into a Survival-Exploration Open-World RPG

**Primary Game Engine:** `open_world_game.html`  
**Main Entry Point:** `index.html`  
**Data Registries:** `data/items.json`, `data/crafting_recipes.json`, `data/world_regions.json`, `data/missions.json` → compiled via `tools/build_data_js.py` into `data/data_registries.js`

---

## 1. Architectural Preservation & Core Loop

Before adding new survival systems, the following foundations from Gates B–E remain strictly locked:
- **Approved Option B Visual Identity:** Shivaji Maharaj (`01_Shivaji/`), the 6 refined Deccan enemy archetypes (`02_Enemies_OptionB/`), illustrated dialogue portraits (`05_Portraits_OptionB/`), and 16×16 Sahyadri tiles (`07_TerrainTiles/` – `11_VillageAndCamp/`).
- **Widescreen Pixel Viewport:** Logical $480 \times 270$ canvas with integer scaling and `imageSmoothingEnabled = false`.
- **Tactical Combat & Astra System:** Delta-time enemy AI state machine (`patrol`, `chase`, `windup`, `attack`, `recover`, `stagger`, `defeated`) and starting Divine Astra selection (**Agni**, **Varuna**, **Bhoomi**).
- **Save Key Compatibility:** `swarajya_open_world_save_v1` in `localStorage`.

### The Gate F Survival-Exploration Loop
1. **Explore** connected Sahyadri regions, uncovering fog-of-war on the Minimap and `[M]` World Map.
2. **Gather** surface sticks, stones, herbs, and fibres by hand; craft starter tools (`crude_axe`, `basic_pickaxe`) to harvest Sagwan timber and Hematite iron veins.
3. **Discover** hidden shrines, supply caches, crafting recipes, and the enterable **Highland Abandoned Mine** (`sahyadri_iron_cavern`).
4. **Unlock** Bhavani Nagar's full village services (Blacksmith, Armourer, Healer, Merchant, Elder) and complete regional side quests (`[J]` Quest Journal).
5. **Prepare & Conquer** hostile raider outposts and storm Kot Fort to hoist the Saffron Bhagwa Zenda.

---

## 2. Step-by-Step Execution Milestones

### Step 1 (Milestones F1 & F2): World Architecture, 6 Connected Regions & Map / Fog-of-War System
- **Expand World Dimensions:** Scale the surface world from $80 \times 40$ to $120 \times 70$ tiles ($1920 \times 1120\text{ px}$) plus a $40 \times 25$ subterranean map (`sahyadri_iron_cavern`).
- **Define 6 Distinct Sub-Zones in `data/world_regions.json`:**
  1. `forest_clearing` — **Region A: Sacred Awakening Forest** (Starter grove, surface stone/branch pickups, Sagwan trees, Field Smithing Anvil).
  2. `river_crossing` — **Region B: Expanded Koyna River Valley** (North-to-south river, main timber bridge, northern stone ford, riverbank herbs/clay, Hidden Waterfall Shrine).
  3. `village_bhavani_nagar` — **Region C: Bhavani Nagar & Countryside** (Village well, Elder's Wada, Blacksmith Forge, Armourer Workshop, Healer's Hut, Merchant Stall).
  4. `sahyadri_highlands` — **Region D: Rugged Sahyadri Foothills & Highlands** (Switchback basalt cliffs, iron veins, mountain pass scouts, Ancient Shrine, Abandoned Mine entrance).
  5. `abandoned_iron_mine` — **Region E: Highland Underground Cavern** (Enterable subterranean dungeon with rare Wootz ore, lost blacksmith tools, and cave sentries).
  6. `kot_fort_and_outpost` — **Region F: Deshmukh Raider Outpost & Kot Fort Citadel** (Southern raider camp, fortified stone approach, Dilli Darwaja gate, citadel garrison, and Buruj flagstaff).
- **Minimap & `[M]` World Map Modal:**
  - Add top-right HUD minimap canvas ($76 \times 48\text{ px}$).
  - Add `[M]` full-screen World Map modal rendering discovered sectors, fog-of-war over unvisited areas, player coordinates, quest pins, and station icons.

### Step 2 (Milestone F3 — Part A): Tool Progression & Resource Node Depletion
- **Add Tool Slot & 4 Gathering Tools (`data/items.json`):**
  - `crude_axe` (Tier 1 Axe — fells Sagwan trees)
  - `reinforced_axe` (Tier 2 Axe — fells trees faster with bonus timber yield)
  - `basic_pickaxe` (Tier 1 Pickaxe — mines surface Hematite Iron Ore)
  - `iron_pickaxe` (Tier 2 Pickaxe — mines subterranean Wootz Ore and tough rock)
- **Add New Survival Materials (`data/items.json`):**
  - `wood_twig` (Fallen Teak Branch — hand-gatherable)
  - `stone_rough` (Rough Basalt Stone — hand-gatherable)
  - `plant_fibre` (Wild Hemp Fibre — hand-gatherable)
  - `herb_tulsi` (Sacred Mountain Herb — hand-gatherable)
  - `ore_wootz` (Subterranean Wootz Steel Ore — requires `iron_pickaxe`)
- **Visual Node Depletion & Respawn:**
  - Depleted trees render tree stumps (`stumps_and_fallen_trees.png`); depleted ore nodes render mined rock bases.
  - Surface nodes respawn after $120\text{s}$; rare subterranean nodes persist in save state.

### Step 3 (Milestone F3 — Part B): Recipe Discovery & Multi-Station Crafting
- **Expand `data/crafting_recipes.json`:**
  - Add starter tool recipes (`craft_crude_axe`, `craft_basic_pickaxe`) using hand-gathered `wood_twig`, `stone_rough`, and `plant_fibre`.
  - Add advanced tool recipes (`craft_reinforced_axe`, `craft_iron_pickaxe`) at `village_blacksmith`.
  - Add discoverable recipes (`unlockedByDefault: false`, unlocked by finding scrolls/shrines in the world):
    - `craft_sahyadri_bow` (Unlocked at Hidden Waterfall Shrine)
    - `craft_battle_elixir` (Unlocked in Abandoned Mine scroll)
    - `craft_wootz_talwar` (Unlocked by completing the *Abandoned Mine* quest for the Blacksmith)
- **Categorized Crafting Modal:**
  - Add category filter pills (**All**, **Tools**, **Weapons**, **Armour**, **Supplies**) and display locked recipe hints so players know where to explore.

### Step 4 (Milestone F5 & F6): Bhavani Nagar Village Hub & Services
- **Add Interactive Village NPCs & Stations:**
  - **Elder (`npc_elder`):** Assigns quests and tracks regional liberation.
  - **Blacksmith (`npc_blacksmith`):** Forges weapons and upgraded tools once unlocked.
  - **Armourer (`npc_armourer`):** Crafts Brigandine, Chainmail Zirah, and Reinforced Dhal shields.
  - **Healer (`npc_healer`):** Restores HP and crafts potent herbal remedies.
  - **Merchant (`npc_merchant`):** Opens a Trade Modal allowing players to sell surplus timber/ore for `gold_huns` and buy leather hides, herbs, and salves.

### Step 5 (Milestone F4): Underground Cave Dungeon, Chests, Shrines & Side Quests
- **Subterranean Transition (`enterCave()` / `exitCave()`):**
  - Interacting (`[E]`) with the Highland Mine entrance transitions Shivaji into the $40 \times 25$ underground cavern map and stores `surfaceReturnPos` so exiting places him right outside the mine entrance.
- **Persistent Chests & Shrines:**
  - Add lootable supply caches/chests (`type: 'chest'`) tracked in `worldState.openedChests` (one-time rewards: gold, materials, or recipe scrolls).
  - Add Sacred Bhavani Shrines (`type: 'shrine'`) granting temporary combat blessings and lore.
- **5 Side Quests (`data/missions.json`) & `[J]` Quest Journal Modal:**
  1. *Missing Supplies* (`side_1_missing_supplies`)
  2. *Herbal Remedy* (`side_2_herbal_remedy`)
  3. *The Abandoned Mine* (`side_3_abandoned_mine`)
  4. *The Lost Scout* (`side_4_lost_scout`)
  5. *The Hidden Shrine* (`side_5_hidden_shrine`)

### Step 6 (Milestone F6): Living World Atmosphere & Save Migration
- **Ambient World Effects:**
  - Drifting forest leaves, river water shimmer, flickering village/cave torchlight radials, and a gentle day-to-golden-dusk ambient cycle.
- **Save State Migration (`swarajya_open_world_save_v1`):**
  - Save and restore `equipped.tool`, `discoveredSubZones`, `discoveredCells`, `unlockedRecipes`, `openedChests`, `harvestedNodes`, `activeMapId`, and `activeMissions` with full backwards compatibility for existing saves.

### Step 7 (Milestone F7): End-to-End QA & Verification
- Rebuild `data/data_registries.js` via `python tools/build_data_js.py`.
- Verify all 18 Gate F acceptance criteria in browser (zero console errors, zero 404s, full survival-exploration loop from bare-handed awakening to Kot Fort liberation).
