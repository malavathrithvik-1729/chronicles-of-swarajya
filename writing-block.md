# MASTER GAME DEVELOPMENT PROMPT
## Chronicles of Swarajya: The Divine Blade

Act as a senior 2D game developer, game engine architect, pixel-art game designer, gameplay programmer, UI/UX designer, and QA engineer.

Your task is to design and develop a complete, playable browser-based action-survival RPG titled **"Chronicles of Swarajya: The Divine Blade."**

This must be a real game, not a static mockup, visual demonstration, or collection of disconnected screens.

The game must feature a historically inspired Indian setting, mythological fantasy elements, retro pixel-art graphics, 75 campaign levels, resource gathering, equipment crafting, divine Astra abilities, intelligent enemy behaviour, major boss battles, mobile touch controls, and a complete ending.

Do not start by generating code immediately. First understand the complete story, gameplay systems, interface requirements, and technical constraints specified below. Then implement the game as a coherent system.

---

# PART 1 — THE GAME'S IDENTITY

## 1.1 Game overview

**Title:** Chronicles of Swarajya: The Divine Blade

**Genre:** 2D top-down action-survival RPG with exploration, combat, crafting, boss fights, and campaign progression.

**Setting:** The Sahyadri mountains, forests, villages, forts, and occupied territories of the Indian subcontinent during the era of Chhatrapati Shivaji Maharaj.

**Art style:** Low-resolution 16-bit-inspired retro pixel art. Use deliberately simple graphics with a limited colour palette, blocky textures, clear silhouettes, and readable animations.

**Target platforms:**
- Desktop and laptop browsers.
- Android mobile browsers.
- iOS mobile browsers where supported.
- Offline play after the single HTML file has loaded.

**Technology:** HTML5, CSS3, Vanilla JavaScript ES6+, and the HTML5 Canvas 2D API.

**Deliverable:** One complete `index.html` file containing all HTML, CSS, JavaScript, game logic, procedural pixel-art rendering, interface components, and touch controls.

Do not use React, Phaser, Unity, external game engines, external JavaScript libraries, remote image assets, or external font dependencies.

The game should be lightweight, responsive, and playable through VS Code Live Server or by opening the HTML file in a compatible browser.

## 1.2 Creative direction

The game should feel like a combination of:
- A classic top-down action RPG.
- An Indian historical adventure.
- A mythological fantasy journey.
- A survival and crafting game.
- A fort-conquest campaign.

Keep the graphics intentionally low-resolution. Do not attempt photorealism, 3D rendering, excessive particle effects, or elaborate high-resolution textures.

However, simple graphics must not mean poor presentation. The game should have carefully designed sprites, atmospheric lighting effects created with simple shapes, coherent environments, responsive controls, and readable interfaces.

The game should run efficiently on an ordinary student laptop and mid-range mobile devices.

---

# PART 2 — COMPLETE STORY AND NARRATIVE

## 2.1 Prologue: The Sacred Vow

The campaign begins in the Sahyadri mountains, where young Shivaji stands before the shrine of Goddess Bhavani.

The land is troubled by oppression, insecurity, and the suffering of ordinary people. Shivaji makes a sacred vow to establish Hindavi Swarajya, a realm in which people can live with greater freedom, dignity, and security.

Moved by the spirit of his vow, Goddess Bhavani grants him the opportunity to choose one of three fictional divine Astras.

The player must select one Astra before beginning the first level.

### The three Astras

**Agni Astra — Fire**

- Element: Fire.
- Primary purpose: Offensive combat.
- Ability: Releases a radial wave of fire around Shivaji.
- Effect: Damages nearby enemies and briefly burns them.
- Strength: Effective against groups of enemies.
- Limitation: Requires a cooldown and careful positioning.

**Varuna Astra — Water**

- Element: Water.
- Primary purpose: Healing and survival.
- Ability: Releases a magical torrent that restores Shivaji's health.
- Effect: Instantly restores a limited amount of health and can later provide temporary protection through mastery upgrades.
- Strength: Excellent for surviving difficult encounters.
- Limitation: Cannot restore more health than the player's maximum HP and has a cooldown.

**Bhoomi Astra — Earth**

- Element: Earth.
- Primary purpose: Crowd control and defence.
- Ability: Sends a seismic shockwave through the ground.
- Effect: Damages nearby enemies, interrupts certain attacks, and stuns ordinary enemies briefly.
- Strength: Useful when surrounded or facing charging enemies.
- Limitation: Has a cooldown and should not become a permanent source of invulnerability.

These Astras are fictional gameplay abilities inspired by mythological elemental themes. Present them as fantasy elements rather than claiming that these events occurred in documented history.

## 2.2 Act I: Gathering the Realm — Levels 1–24

Shivaji begins his journey with basic equipment and limited resources.

He travels through dense forests, mountain passes, occupied settlements, rocky valleys, and guarded fort approaches.

At first, he cannot simply defeat every enemy by attacking continuously. He must learn to move, dodge, strike, collect materials, upgrade equipment, and use his chosen Astra intelligently.

### Story progression

Levels 1–5 introduce movement, attacks, gathering, basic enemies, and simple crafting.

Levels 6–12 introduce stronger soldiers, narrow passages, environmental obstacles, and more valuable resources.

Levels 13–18 introduce elite guards, optional rescue missions, treasure, and more complicated forts.

Levels 19–24 introduce advanced enemies, improved equipment, and increasingly dangerous encounters in preparation for Pratapgad.

Each ordinary level represents a distinct section of the campaign. The map layout, enemy composition, resource placement, and environmental decoration should vary.

### Resources

Shivaji can collect:

- Sagwan Wood.
- Iron Ore.
- Gold.
- Rare crafting materials unlocked in later regions.

Sagwan Wood and Iron Ore are collected by approaching resource nodes and pressing the attack/interact control.

Collected resources remain in the player's inventory and can be used to craft better weapons and armour.

### Ordinary fort encounters

Each level should contain an enclosed fort or fortified outpost.

The player must defeat guards, overcome the Fort Keeper, and unlock the exit gate.

Some missions may include alternative objectives, optional treasure, or rescued villagers.

## 2.3 Act II: The Trial of Pratapgad — Level 25

Afzal Khan's expedition becomes a major threat to Shivaji's growing campaign.

The player reaches Pratapgad and encounters a major boss battle.

### Boss encounter

Afzal Khan is a large, powerful commander with a unique appearance, attack animations, and multiple combat phases.

The battle takes place in a larger arena than ordinary encounters.

The encounter includes a force of 25 elite soldiers, but they must not all crowd the screen simultaneously. Use manageable waves, reinforcements, or groups that enter the arena in stages.

Afzal Khan's attack patterns should include:
- A powerful melee strike.
- A telegraphed charging attack.
- A ground impact with an area of effect.
- A recovery period after heavy attacks.

The player must move strategically, use the environment, and time Astra abilities rather than simply holding the attack button.

When Afzal Khan is defeated, display a victory sequence, grant a unique crafting reward, and unlock the next chapter.

### The second Astra

At Level 25, automatically unlock one of the two Astras that the player did not select initially.

Do not grant an Astra the player already possesses.

The player now has two Astras and can switch between them.

## 2.4 Act III: Expansion and Resistance — Levels 26–49

Shivaji's campaign expands into increasingly fortified territory.

Enemy soldiers use more varied tactics, and equipment upgrades become important for survival.

Introduce:
- Elite swordsmen.
- Shielded guards.
- Ranged attackers.
- Charging enemies.
- Fort defenders who reinforce one another.
- Optional missions to rescue villagers and escort messengers.
- Hidden paths through mountains and forests.
- Rare materials used for advanced crafting.

The player should have to make strategic decisions about whether to upgrade weapons, improve armour, increase maximum health, or invest in Astra mastery.

Ordinary missions should remain varied. Do not simply increase enemy health indefinitely.

## 2.5 Act IV: Midnight at Lal Mahal — Level 50

Shaista Khan occupies Lal Mahal in Pune.

Shivaji must undertake a special infiltration mission to penetrate the stronghold, navigate its guarded courtyards, and confront the Mughal viceroy.

### Special mission mechanics

This level should differ from ordinary fort encounters.

Include:
- A night-time visual palette.
- Narrow passages and courtyard spaces.
- Guards with limited vision or detection ranges.
- An optional stealth approach.
- An alarm or reinforcement mechanic.
- A unique boss arena.

The player should be able to succeed through careful movement and combat rather than being forced to fight every guard simultaneously.

Shaista Khan should have multiple attack patterns and an appropriate final defeat sequence.

### The third Astra

Upon completing Level 50, automatically unlock the final Astra that the player does not yet possess.

Shivaji now has all three Astras: Agni, Varuna, and Bhoomi.

## 2.6 Act V: The March to Raigad — Levels 51–74

The final campaign chapter tests everything the player has learned.

Shivaji travels through dangerous mountain routes, heavily guarded settlements, and elite fortifications.

The player must:
- Master all three Astras.
- Collect rare crafting materials.
- Complete advanced optional missions.
- Craft powerful weapons and armour.
- Learn the attack patterns of elite enemies.
- Prepare for the final confrontation.

The last ten levels should be especially challenging, with more demanding layouts and enemies that require different tactics.

However, the game must remain fair. Stronger enemies should have readable attacks, clear warning animations, and opportunities for the player to respond.

## 2.7 Final Act: The Grand Sovereign at Raigad — Level 75

The final battle takes place at Raigad Fort.

In this alternate-history fantasy finale, Aurangzeb appears as the final campaign antagonist. This confrontation is fictional and should be presented as creative alternate history rather than a documented historical event.

### Final boss mechanics

The final boss must be significantly more challenging than previous bosses.

Use three phases:

**Phase One — The Imperial Guard**

The player must defeat a small group of elite defenders before confronting the final antagonist.

**Phase Two — The Final Duel**

The antagonist uses powerful melee attacks, charging attacks, area attacks, and summoned reinforcements.

**Phase Three — The Final Stand**

At low health, the boss changes attack patterns and becomes more aggressive. The player must use all available equipment, movement skills, and Astra abilities to win.

The player should not be required to own every optional upgrade. Skilled play must remain a viable path to victory.

### Ultimate Astra

Upon defeating the final boss, trigger a special cinematic-style sequence in which the three elements combine into a single ultimate ability.

Use a short screen transition, simple pixel particles, a flash effect, and an appropriate celebratory sound if sound is available.

### Epilogue: Hindavi Swarajya Established!

The final screen shows Raigad Fort, Maratha banners, a peaceful landscape, and a coronation-inspired scene.

Display the title:

**HINDAVI SWARAJYA ESTABLISHED!**

Show:
- Total campaign levels completed.
- Total forts liberated.
- Final weapon and armour levels.
- Number of optional missions completed.
- Total resources collected.
- Time spent playing, if reliably tracked.

Provide buttons for restarting the campaign and viewing campaign statistics.

The ending should feel earned and meaningful.

---

# PART 3 — COMPLETE GAMEPLAY SYSTEM

## 3.1 The main gameplay loop

Every ordinary level should support the following loop:

1. Enter a new region.
2. Explore the map.
3. Collect wood, ore, gold, and available special materials.
4. Fight or avoid enemies.
5. Complete optional objectives when useful.
6. Return to safety or open the upgrade panel.
7. Improve weapons, armour, or abilities.
8. Defeat the Fort Keeper.
9. Open the exit gate.
10. Advance to the next level.

The loop must work repeatedly without requiring the page to reload.

Boss levels and special missions may use modified versions of this loop.

## 3.2 Player character

Create a top-down pixel-art sprite representing Shivaji Maharaj as a stylized historical fantasy protagonist.

The sprite should have:
- A recognizable saffron or earthy-coloured outfit.
- A turban and simple armour.
- A sword.
- Clear facing direction.
- Walking animations.
- Attack animations.
- Damage feedback.
- A brief dodge animation.
- A visible distinction between normal and empowered states.

Do not rely on emoji as the final player sprite.

Draw sprites using canvas rectangles, small pixel clusters, simple polygons, and carefully arranged shapes. Keep a consistent pixel grid.

The player must be recognizable at the native resolution of the game.

## 3.3 Movement

Desktop controls:

- W, A, S, D: Movement.
- Arrow keys: Alternative movement.
- Spacebar: Attack or interact with nearby resources.
- Shift: Activate the selected Astra.
- U: Open the equipment upgrade panel.
- Escape: Pause or close an appropriate menu.
- 1, 2, 3: Select an Astra when available and when the player is not entering text into a menu.

Movement should be responsive and normalized diagonally so that diagonal movement is not faster than horizontal or vertical movement.

The player must not move through walls or solid obstacles.

On mobile, use a virtual joystick or directional pad for movement and touch buttons for combat.

## 3.4 Combat

Implement a reliable combat system with:
- Player attack damage.
- Attack cooldown.
- Attack range.
- Enemy health.
- Enemy damage.
- Knockback where appropriate.
- Damage feedback.
- Death and removal logic.
- Collision detection.
- Astra cooldowns.
- Invulnerability frames after certain damage events.

The attack button should never collect a resource through a wall or strike an enemy outside the intended attack range.

Resource interactions should use a separate interaction check even if the same button handles both actions.

## 3.5 Divine Astra mechanics

Implement the three Astras as distinct abilities.

Agni Astra:
- Area-of-effect damage.
- Brief burning effect.
- Fire-coloured particles.
- Clear activation animation.

Varuna Astra:
- Instant health restoration.
- Blue water-wave animation.
- Respect the maximum health limit.
- Optional mastery upgrade for a brief protective effect.

Bhoomi Astra:
- Area-of-effect damage.
- Temporary stun for eligible enemies.
- Earth-coloured ground shockwave.
- Clear visual warning before major boss effects.

All abilities must have cooldowns. Display cooldown progress in the HUD.

Bosses may resist certain effects. Never allow repeated stuns to permanently prevent a boss from attacking.

## 3.6 Astra mastery

Each Astra should have three upgrade branches or mastery levels.

Example:

Agni:
- Increase damage.
- Increase effective radius.
- Improve burning duration.

Varuna:
- Increase healing.
- Reduce cooldown.
- Unlock temporary protection.

Bhoomi:
- Increase shockwave radius.
- Increase damage.
- Improve the duration of eligible enemy stuns.

Mastery must be unlocked through gameplay rewards or a defined progression resource.

Do not introduce a complicated skill tree that makes the interface unreadable on mobile.

---

# PART 4 — RESOURCES, CRAFTING AND UPGRADES

## 4.1 Resource system

Maintain a clear player inventory containing:
- Sagwan Wood.
- Iron Ore.
- Gold.
- Rare crafting materials.
- Special boss rewards.

Resource nodes must appear at sensible locations.

Wood nodes should look like trees or timber sources, while ore nodes should look like mineral deposits or rocky veins.

Each node must have:
- A unique identity.
- A resource type.
- A resource amount.
- A harvesting cooldown or removal state.
- A visual indicator when harvestable.

Once collected, the node should disappear or change appearance.

The player must receive the correct resources only once per node.

## 4.2 Weapon upgrades

Create four equipment tiers.

Tier 1: Basic Iron.

Tier 2: Forged Steel.

Tier 3: Royal Forging.

Tier 4: Divine Forging.

The names are game progression categories, not claims about exact historical equipment.

Weapon upgrades can improve:
- Damage.
- Attack speed within reasonable limits.
- Attack range in selected tiers.
- Special combat effects at milestone tiers.

The weapon upgrade panel must show the current tier, next tier, benefits, and crafting costs.

The Upgrade button must actually deduct the required materials and apply the upgrade only when the player has sufficient resources.

## 4.3 Armour upgrades

Armour upgrades can improve:
- Damage reduction.
- Maximum health.
- Resistance to selected enemy attacks.

Do not make the player invulnerable through excessive armour stacking.

When maximum health increases, preserve the player's current health proportionally or grant a clearly communicated restoration benefit.

## 4.4 Example economy

Use the following only as starting balance values, then tune through testing.

| Upgrade | Example cost | Benefit |
|---|---|---|
| Weapon upgrade I | 5 wood, 4 ore | Basic damage increase |
| Weapon upgrade II | 10 wood, 10 ore, 15 gold | Greater damage |
| Armour upgrade I | 6 wood, 5 ore | Better defence |
| Armour upgrade II | 12 wood, 12 ore, 20 gold | More health and defence |
| Astra mastery | Rare material and gold | Improve one ability |

Scale costs gradually rather than exponentially.

Each normal level should provide opportunities to gain useful resources. Do not force excessive grinding just to complete the campaign.

## 4.5 Blacksmith and upgrade menu

Create a dedicated equipment interface containing:
- Weapon icon and current tier.
- Armour icon and current tier.
- Current health and maximum health.
- Available materials.
- Upgrade costs.
- Preview of the resulting benefit.
- Upgrade confirmation.
- Close or resume button.

Pause combat while the upgrade interface is open.

Prevent accidental purchases from touch input.

---

# PART 5 — ENEMIES, BOSSES AND DIFFICULTY

## 5.1 Ordinary enemy types

Create at least five enemy archetypes.

**Basic Guard:** Approaches and attacks at close range.

**Shielded Guard:** Blocks frontal attacks and requires positioning or a suitable ability.

**Ranged Attacker:** Maintains distance and fires projectiles.

**Charging Soldier:** Telegraphs a fast charge that can be dodged.

**Elite Guard:** Combines stronger attacks with greater durability.

Enemies must not all use identical movement and attack behaviour.

## 5.2 Enemy AI

Implement a lightweight finite-state machine for enemies.

Useful states include:
- Idle.
- Patrol.
- Chase.
- Attack.
- Recover.
- Stunned.
- Dead.

Enemies should detect the player within a defined radius, pursue when appropriate, and attack only when conditions permit.

Avoid expensive pathfinding for every enemy every frame. Use simple navigation, local collision avoidance, short movement decisions, and sensible update intervals.

Enemies must not remain permanently stuck against walls or attack continuously without cooldowns.

## 5.3 Fort Keeper bosses

Every ordinary level should have a Fort Keeper or equivalent final defender.

The Fort Keeper must be stronger than ordinary guards and have a recognizable health bar.

Possible abilities include:
- Heavy strike.
- Short charge.
- Area attack.
- Defensive stance.
- Summoning limited reinforcements.

Use only a small selection of these abilities per boss to keep combat readable.

After the Fort Keeper is defeated:
- Stop spawning new enemies for that encounter.
- Unlock the gate.
- Display a short victory message.
- Enable the exit interaction.
- Award the level-completion rewards.

## 5.4 Major boss requirements

Level 25: Afzal Khan.

Level 50: Shaista Khan.

Level 75: Aurangzeb in the game's fictional alternate-history finale.

Each must have:
- A distinct sprite.
- A unique health bar.
- At least three distinguishable attack patterns.
- Attack telegraphs.
- Recovery periods.
- Phase transitions where appropriate.
- A unique reward.
- A clear victory animation.

Boss fights must be winnable through skill and fair equipment progression.

---

# PART 6 — DESIGN ALL 75 LEVELS

Do not implement 75 copies of the same room.

Use a procedural campaign generator with handcrafted rules for the major milestone encounters.

Divide the campaign into five regions:

Region 1: Levels 1–15 — Forests and mountain paths.

Region 2: Levels 16–24 — Fortified approaches and elite outposts.

Region 3: Levels 26–40 — Rugged imperial frontier and advanced forts.

Region 4: Levels 41–49 — Heavily defended territories and difficult encounters.

Region 5: Levels 51–74 — High mountain passes, elite fortifications, and the final approach to Raigad.

Levels 25, 50, and 75 must be dedicated major encounters.

### Procedural variation

Vary the following:
- Terrain layout.
- Fort wall placement.
- Gate location.
- Resource locations.
- Enemy types.
- Number of guards.
- Optional mission objectives.
- Treasure locations.
- Decorative features.
- Difficulty and rewards.

Generate a 20 × 20 logical tile map for each level, or a similarly lightweight map structure if required for correct rendering.

Represent the world using compact numeric tile identifiers.

Suggested tile types:
- Grass.
- Forest floor.
- Path.
- Rock.
- Water.
- Wall.
- Fort floor.
- Gate.
- Resource node.
- Decorative tile.

Use collision rules that prevent walking through walls, solid rocks, and other solid objects.

Procedural generation must produce playable layouts. Do not place the player inside a wall, create an unreachable boss, block the only exit, or put all resources outside the accessible map.

Use a seeded pseudorandom generator so the same level can be reproduced when needed.

For levels 25, 50, and 75, use specifically designed layouts rather than relying entirely on random generation.

---

# PART 7 — MISSIONS AND KINGDOM RESTORATION

Add optional missions to make the campaign more than a sequence of fights.

Possible mission types:
- Rescue villagers.
- Escort a messenger.
- Recover a lost supply cache.
- Defend a settlement.
- Discover a hidden mountain route.
- Collect a rare relic.
- Complete a fort without triggering an alarm.

Optional missions should provide resources, gold, mastery rewards, or permanent kingdom-restoration progress.

### Swarajya restoration

Track the number of liberated forts and rescued settlements.

After certain milestones, show a simple world-map or settlement indicator reflecting the player's progress.

Possible rewards:
- Blacksmith access.
- A healer or restoration station.
- Better resource availability.
- Additional lore entries.
- Special crafting recipes.

These systems should remain lightweight. Do not attempt to simulate an entire living kingdom.

---

# PART 8 — PIXEL-ART VISUAL DESIGN

## 8.1 Native rendering resolution

Use a native game canvas of 160 × 160 pixels.

Scale it to fit the available screen while preserving the intended pixel-art appearance.

Use CSS pixelated rendering and disable image smoothing for the game canvas.

A 640 × 640 CSS display can be used on suitable desktop layouts, but it must not be forced onto every mobile screen.

Use responsive scaling based on the available viewport.

On mobile, allow the game world to use the available screen space without distorting the pixel aspect ratio.

Do not stretch the canvas independently in the horizontal and vertical directions.

## 8.2 Visual quality target

Use a restrained palette:
- Forest greens.
- Earthy browns.
- Stone greys.
- Muted mountain blues.
- Saffron accents.
- Red-orange fire effects.
- Blue water effects.
- Earthy green or ochre earth effects.

The art should be simple and recognizable at a glance.

Create a small number of reusable pixel-art drawing functions for:
- Trees.
- Rocks.
- Grass.
- Walls.
- Gates.
- Forts.
- Villagers.
- Soldiers.
- Bosses.
- Player characters.
- Resource nodes.
- Weapons.
- Astra effects.

Use canvas drawing commands and procedural sprites instead of external image downloads.

Avoid relying on large numbers of random pixels to represent scenery.

## 8.3 Animation

Implement lightweight animations:
- Walking frame changes.
- Sword swings.
- Astra activation.
- Projectile movement.
- Enemy damage flashes.
- Death or defeat effects.
- Gate opening.
- Boss phase transitions.
- Resource harvesting.
- Victory celebration.

Animations must be readable but brief.

Use small pools of particles and reuse them instead of creating an unlimited number of new objects.

## 8.4 Environment design

Every region should have a distinct atmosphere.

Forests: Darker greens, trees, winding paths, and scattered rocks.

Mountain passes: Stone terrain, narrow paths, cliffs, and sparse vegetation.

Ordinary forts: Stone walls, gatehouses, courtyards, and wooden structures.

Lal Mahal: Night-time colours, courtyards, guard positions, and narrow passages.

Raigad: Elevated stone pathways, mountain scenery, a grand fort, and a celebratory final scene.

Keep important gameplay objects visually distinguishable from decoration.

---

# PART 9 — MOBILE-FIRST INTERFACE

The mobile interface is a core requirement, not an optional addition.

## 9.1 Gameplay orientation

Support both portrait and landscape viewports.

Prefer landscape orientation for action combat when the available device orientation permits it.

Do not force an orientation lock that may fail or inconvenience users.

In portrait mode, adapt the layout and keep all essential controls accessible. Do not simply shrink a landscape interface until it becomes unusable.

## 9.2 Mobile controls

Bottom-left:
- Virtual joystick or directional pad.
- Clear centre and directional indicators.
- Smooth movement response.

Bottom-right:
- ATTACK button.
- ASTRA button.
- UPGRADE button.
- Optional DODGE button if the movement mechanic is implemented.

The joystick should be translucent but visible.

Buttons must have clear pressed states and adequate spacing.

Support pointer and touch events, including touch cancellation and release.

Prevent the game canvas from scrolling the page during active gameplay.

Do not rely exclusively on hover interactions.

## 9.3 HUD

The heads-up display should show:
- Current level.
- Player health and maximum health.
- Weapon tier.
- Armour tier.
- Wood count.
- Iron Ore count.
- Gold.
- Active Astra.
- Astra cooldown.
- Current mission objective.

Keep the HUD compact.

On small mobile screens, use short labels and icons with optional explanatory tooltips or expandable details.

Never let the HUD cover the central player character or important boss attack warnings.

## 9.4 Menus

Create the following screens:

1. Main menu.
2. New campaign screen.
3. Astra selection screen.
4. Gameplay screen.
5. Pause menu.
6. Inventory and upgrade menu.
7. World map and campaign progress.
8. Mission complete screen.
9. Game over screen.
10. Final victory screen.

The main menu must display the title, a short description, a START button, a CONTINUE button when a valid save exists, and a controls/help option.

The Astra selection screen must clearly describe each ability and allow selection through mouse, keyboard, or touch.

The pause menu should include Resume, Restart Level, Controls, and Main Menu options.

Ask for confirmation before restarting a campaign or deleting saved progress.

---

# PART 10 — SOUND AND FEEDBACK

Sound is optional, but the game must work without external audio files.

If practical, use the Web Audio API to generate simple effects for:
- Sword strikes.
- Resource collection.
- Astra activation.
- Boss damage.
- Gate opening.
- Level completion.

Audio must begin only after appropriate user interaction and should respect browser autoplay restrictions.

Provide a mute option.

Avoid loud, repetitive, or excessive audio.

Visual feedback must remain sufficient even when sound is disabled.

---

# PART 11 — TECHNICAL ARCHITECTURE

Implement the game in a single HTML file with clearly separated internal sections.

Use readable, maintainable Vanilla JavaScript.

Organize the code into logical components, even though they are all contained in one file.

Recommended components:

**GameState:** Tracks the current screen and gameplay mode.

**InputManager:** Handles keyboard, pointer, and touch input.

**Renderer:** Draws the map, sprites, particles, and HUD.

**Player:** Manages movement, health, attacks, inventory, equipment, and Astra abilities.

**Enemy:** Handles ordinary enemy behaviour and combat.

**Boss:** Adds boss phases, attack patterns, and boss health.

**ResourceManager:** Manages resource nodes and harvesting.

**InventorySystem:** Tracks wood, ore, gold, rare materials, and crafting.

**UpgradeSystem:** Validates costs and applies upgrades.

**LevelGenerator:** Creates reproducible ordinary levels.

**MissionManager:** Tracks main and optional objectives.

**SaveManager:** Saves and restores campaign progress.

**AudioManager:** Handles optional sound effects.

**UIManager:** Handles menus, HUD, overlays, and button feedback.

These can be classes or well-organized objects and functions. Do not create unnecessary abstractions that make a small game harder to maintain.

## 11.1 Game state machine

Implement explicit states:

- MAIN_MENU.
- SELECT_ASTRA.
- PLAYING.
- PAUSED.
- UPGRADING.
- LEVEL_COMPLETE.
- GAME_OVER.
- VICTORY.

The game must not run active combat while paused, upgrading, or displaying a blocking results screen.

The selected starting Astra must be validated before the campaign begins.

Level transitions must clean up the previous level's enemies, projectiles, particles, and resource nodes.

## 11.2 Game loop

Use requestAnimationFrame.

Separate simulation updates from rendering.

Use elapsed time or a fixed-step accumulator so movement and combat do not depend directly on the monitor's frame rate.

Clamp unusually large elapsed-time values after a background tab resumes.

Avoid running duplicate animation loops when restarting or changing screens.

## 11.3 Collision detection

Implement axis-aligned bounding-box collision checks or another lightweight suitable approach.

Support:
- Player versus solid tiles.
- Player versus enemies.
- Player versus resource nodes.
- Enemy versus solid tiles.
- Player attacks versus enemies.
- Projectiles versus valid targets.
- Boss attacks versus the player.
- Gate interactions.

Resolve movement collisions on each axis separately where appropriate to prevent the player from sticking against walls.

## 11.4 Performance and memory

The game must remain lightweight.

Requirements:
- Avoid unnecessary allocations inside the main rendering loop.
- Reuse particles and projectiles where practical.
- Remove defeated enemies and expired effects.
- Maintain only the active level in memory.
- Store campaign summaries rather than all historical map objects.
- Use compact tile identifiers.
- Limit simultaneous particles.
- Avoid expensive full-map processing every frame.
- Keep UI updates separate from unnecessary full-screen DOM rebuilding.

Aim for smooth performance on ordinary hardware, while recognizing that actual frame rate depends on the device and browser.

## 11.5 Save system

Use localStorage for campaign persistence.

Save:
- Current campaign level.
- Selected and unlocked Astras.
- Weapon and armour tiers.
- Player health and maximum health.
- Inventory and crafting materials.
- Completed missions.
- Liberated forts.
- Relevant campaign flags.
- Settings such as mute and control preferences.

Use a save schema version so the format can be updated later.

Validate loaded data and recover gracefully from malformed or incomplete saves.

Do not overwrite a valid save with invalid data.

Save after meaningful milestones such as completing a level, purchasing an upgrade, unlocking an Astra, or defeating a major boss.

Include a way to restart the campaign after confirmation.

---

# PART 12 — DEVELOPMENT STRATEGY

Do not attempt to create all systems simultaneously without testing.

Follow this development sequence internally, while still delivering the complete game.

## Phase 1: Foundation

Implement:
- Canvas and responsive scaling.
- Pixel-art rendering setup.
- Main menu.
- Astra selection.
- Player movement.
- Tile collisions.
- Keyboard controls.
- Basic mobile controls.
- State management.

Test movement and collision before continuing.

## Phase 2: First playable level

Implement:
- One procedurally generated ordinary level.
- Player attacks.
- Basic enemies.
- Resource nodes.
- Wood and ore collection.
- Fort Keeper.
- Gate unlocking.
- Level completion.

The first level must be completable from beginning to end.

## Phase 3: Progression systems

Implement:
- Inventory.
- Weapon and armour upgrades.
- Astra cooldowns.
- Healing and defensive mechanics.
- Gold and crafting costs.
- HUD.
- Save and load.

Verify that resources are deducted correctly and that upgrades have measurable effects.

## Phase 4: Campaign generation

Implement:
- Region-based map generation.
- Enemy scaling.
- Resource distribution.
- Distinct ordinary level layouts.
- Exit gates.
- Optional missions.
- Campaign progression.

Ensure that all 75 levels are reachable in the intended order.

## Phase 5: Major encounters

Implement:
- Afzal Khan at Level 25.
- Shaista Khan at Level 50.
- Aurangzeb at Level 75.

Each must have its own layout, attacks, rewards, and victory transition.

## Phase 6: World and story features

Implement:
- Liberated-fort tracking.
- Village rescue missions.
- Blacksmith or healer unlocks.
- Mission notifications.
- Region-specific decoration.
- Story transitions.
- The final coronation-inspired epilogue.

## Phase 7: Polish and mobile adaptation

Implement:
- Responsive HUD.
- Portrait and landscape layouts.
- Touch input fixes.
- Visual feedback.
- Audio settings.
- Pause menu.
- Restart confirmation.
- Victory statistics.

## Phase 8: Testing

Play through the campaign logically and test every major transition.

Do not claim that the game has been fully tested in a real browser unless actual execution and testing have taken place.

---

# PART 13 — REQUIRED ACCEPTANCE TESTS

The final game must satisfy all of the following.

### Starting a campaign
- The main menu appears.
- The player can select any of the three starting Astras.
- The selected Astra is correctly assigned.
- Keyboard and touch controls work.

### Movement and combat
- The player cannot pass through solid walls.
- Diagonal movement is normalized.
- Enemies can chase and attack.
- The player can defeat enemies.
- Health and damage are applied correctly.
- Attacks and abilities respect cooldowns.

### Resource gathering
- The player can collect Sagwan Wood and Iron Ore.
- Resources cannot be collected repeatedly from a depleted node.
- Inventory counts update correctly.
- Gathering does not work through solid obstacles.

### Upgrades
- Upgrade costs are displayed.
- Upgrades fail safely when resources are insufficient.
- Successful upgrades deduct the correct costs.
- Weapon and armour improvements affect actual gameplay.
- The upgrade panel pauses combat.

### Level completion
- Every ordinary level has a functioning Fort Keeper.
- Defeating the Fort Keeper opens the gate.
- The player can enter the exit and advance.
- The previous level's active entities are cleaned up.
- The next level generates a valid map.

### Astra progression
- Level 25 unlocks the second missing Astra.
- Level 50 unlocks the final missing Astra.
- The player's starting selection does not create duplicate unlocks.
- Cooldowns and mastery upgrades work.
- The ultimate Astra combination is available at the final victory sequence.

### Major bosses
- Level 25 contains Afzal Khan and a manageable sequence of elite soldiers.
- Level 50 contains the unique Lal Mahal infiltration encounter and Shaista Khan.
- Level 75 contains the final Raigad encounter.
- Boss health, phases, attacks, defeat conditions, and rewards function correctly.

### Saving
- Progress survives a page refresh.
- Inventory and equipment are restored.
- Completed levels remain completed.
- Invalid save data does not crash the game.

### Mobile
- The joystick moves the player.
- Attack, Astra, and upgrade controls work.
- Buttons do not remain stuck after a touch ends or is cancelled.
- The game does not scroll the page during active joystick movement.
- The interface remains usable on narrow and wide viewports.
- Essential controls remain visible.

### Final victory
- Completing Level 75 triggers the victory state.
- The campaign cannot accidentally continue into Level 76.
- The final screen shows campaign statistics.
- Restart and new-campaign actions work correctly.

---

# PART 14 — FINAL DELIVERY REQUIREMENTS

Produce the complete `index.html` file containing the entire game.

The file must be ready to run in VS Code Live Server without requiring a build process, npm installation, external assets, or additional source files.

Deliver the following:

1. Complete HTML structure.
2. Responsive CSS.
3. Full Vanilla JavaScript implementation.
4. Canvas renderer and procedural pixel-art sprites.
5. Complete gameplay state machine.
6. All 75 campaign levels and progression rules.
7. Player, enemies, bosses, projectiles, and particles.
8. Resource harvesting and crafting.
9. Weapon and armour upgrades.
10. All three Astras and progression unlocks.
11. Mobile touch controls.
12. Menus, HUD, and campaign map.
13. Save/load support.
14. Final victory and restart systems.
15. A concise explanation of how to run and test the game.

Do not provide pseudocode in place of essential gameplay systems.

Do not leave placeholder buttons, fake level transitions, nonfunctional upgrades, missing boss encounters, or comments saying that major features will be implemented later.

Do not claim that a feature works if it is only visually represented.

If output limits make it impossible to provide the entire implementation in one response, divide the implementation into explicitly numbered, contiguous parts. Preserve the same architecture and state exactly across parts, avoid duplicate declarations, and give clear assembly instructions. Never silently omit required systems.

Prioritize a complete, stable, playable game over unnecessary code complexity.

The final objective is to create a lightweight, visually coherent, historically inspired fantasy RPG in which the player progresses from a young warrior with one divine Astra to a master of all three elements, liberates forts across 75 levels, develops the strength of Swarajya, and earns a memorable victory at Raigad.

**Build the actual game, not merely a demonstration of what the game could look like.**