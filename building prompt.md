For this game, the smartest approach is to design the entire visual world first, then build the game engine around those designs. That way, Shivaji, the soldiers, forts, trees, rocks, resources, and UI all share one consistent pixel-art style.

You don't need to master every game-development skill before starting. You need a clear art pipeline, a technical specification, and a sequence of small, testable milestones.

# 1. Skills needed to build the game

[Ultimate Pixel Top Down Character Pack – Godot Assets Marketplace](https://images.openai.com/static-rsc-4/-5Ag548Ql8oBM9ztzQ6HZ1QNVrNlJdCHN2RWNJ8tqae7V1CISvYKbYvVoWKpiZQZQRN38NbZDjnRue4zf7DiUXtHM9eVlZR-tm6qkYF5oAW5RHVPBpGqAeoEcLPGOcG7p9EjD4rCeTKv1ySla5x3qSwTcekvD1_DXJH3otjI33I?purpose=inline)

1\. Pixel-art and sprite design

Start here

Design Shivaji Maharaj, enemies, bosses, trees, rocks, resource nodes, weapons, and animation frames. Learn consistent proportions, outlines, limited palettes, and transparent backgrounds.

[FREE 2D Pixel Art for RPG Maker Games by PixelGameResources on DeviantArt](https://images.openai.com/static-rsc-4/-0yFyxE9vF5ALmgSTAck88DrsivhbS2Llh8-m2116am2YnQG5gVKCvPRkZED03oX9voR8JmygeHjsgBnvVv2CYXPoUtUxh0iggiDgTjSi766Bi_bhNsrkWQRIPFFgEqi2PuC61oZkaCmkY63jbeLJMFbSVV9nNWjbrm_TrvRz68?purpose=inline)

2\. Tilesets and level design

Design reusable terrain tiles, forest paths, mountain passes, fort walls, courtyards, and gates. Make sure tiles connect seamlessly.

[Cloudscape by konitama](https://images.openai.com/static-rsc-4/CFcCTdk0czXXK1MTwyfm09OGQJUCDzaZ4jPVbntckF7BZn3ARmO46DBqA-Vkh9J6Fu9Sz_CDLKu_3jPsP8m4-srU7yNiNxjDHlCSqYZC6sh1qqOkg9kanEtj2JMBbruW-3UkRdlPRHEstiiu2gq7HjQ7afFKR4BY3RU7DMdS9zw?purpose=inline)

3\. Game UI/UX design

Design health bars, inventory, crafting screens, Astra selection, boss health bars, mobile buttons, and the main menu. Keep text readable at small sizes.

[Pixel Art Slam: Blue Portal Design | AI Art Generator | Easy-Peasy.AI](https://images.openai.com/static-rsc-4/9G64eqUDXfNE4sENCwvfxty5u1Yn8lakhXQnuEoczMxdq14fWWhVu4xM1HdziNclew1TKejPz-6X5973qg_S8ljf-bVrw1MSKhVFX3xzpkqjoQxl0LmApcP-t20fe_6WBqfp8WF7YsoY3OkNKzGxhSVUp6n_H7ztO0d7xbUFU7o?purpose=inline)

4\. World and mission design

Plan routes, enemy placement, resources, gates, secret paths, boss arenas, and safe areas. Make each region feel distinct.

[PixelBox - Free AI Pixel Art Sprite Animation Generator | Create Game Sprites Instantly](https://images.openai.com/static-rsc-4/ilcWeudNUTl37uIxwpje_sUOKtaZ4mwGhcu2_bhaKN5unSRlttJVacH5bphsQM5yg1ztB4C8Co80MZV62neSJDcUCN8pSvn0gj4fBK4UIcvpJbCSXE2nmzTRJJx6KRQkJkpWCbT2_illqdnAcnqwNyJmoBS3u3f4XL2FsrG6ihc?purpose=inline)

5\. Animation and visual effects

Create walking, sword attacks, damage reactions, Astra activation, enemy defeat, gate opening, and victory effects.

[30 Amazing Games Made Only With HTML5 - Tutorialzine](https://images.openai.com/static-rsc-4/xAlLF_IyH9bOHDvKDihfs1_9sIgzXQ3uYs9_LmO0e8SoPxtUNDhEi1WQUw4FmnzXXxrYmyXF5KnmKyP2e18t11-MuIZkn9gQpkg39aXPEC--rD3nhlYgz9sxVXWyyhLJm6angsWQ0zitp56UbwekHgF_UmosNqPaDcY6ytfT5Fc?purpose=inline)

6\. Technical game development

Learn JavaScript, Canvas 2D, collision detection, enemy AI, game loops, procedural maps, saving, touch input, and performance optimisation.

You can use AI to assist with all six areas. The important part is to keep the art consistent and verify that every designed asset can actually be used by the game.

# 2. First prompt: design the complete visual world

Use this prompt first, before asking an AI to develop the game. Its job is to establish the art style, character designs, map tiles, objects, and animation specifications.

# VISUAL ASSET DESIGN MASTER PROMPT

## Chronicles of Swarajya: The Divine Blade

Act as a professional pixel-art game artist, character designer, environment artist, sprite-sheet designer, and art director specialising in top-down 2D retro action RPGs.

I am developing a browser-based game called **Chronicles of Swarajya: The Divine Blade**, inspired by the era of Chhatrapati Shivaji Maharaj, the Sahyadri mountains, Maratha forts, and mythological elemental fantasy.

Before any game programming begins, create a complete and consistent visual asset specification for the game.

IMPORTANT: Do not develop the game engine or write JavaScript in this stage. Focus exclusively on designing the visual assets and documenting how each asset should be used later.

## A. Global art direction

Create a deliberately low-resolution, retro pixel-art style inspired by classic 16-bit top-down adventure games.

The game should look simple, atmospheric, historically inspired, and visually consistent.

Requirements:

- Native design grid: 16 × 16 pixels per standard terrain tile.
- Character sprites: approximately 16 × 24 or 24 × 32 pixels, depending on the design.
- Boss sprites: approximately 32 × 40 or 48 × 48 pixels.
- Logical game resolution: 160 × 160 pixels.
- Limited, coordinated colour palette.
- Crisp pixel edges with no blur.
- No photorealism.
- No 3D models.
- No glossy modern mobile-game graphics.
- No excessive visual detail that becomes unreadable at small sizes.
- No emoji used as substitute sprites.

Treat the dimensions as starting specifications, not absolute restrictions. A sprite may occupy multiple tiles.

Create a visual style guide defining:

1. The master colour palette.
2. Character proportions.
3. Outline thickness.
4. Light and shadow rules.
5. Material colours for wood, stone, iron, cloth, water, and fire.
6. Environmental perspective.
7. Pixel density and detail limits.
8. Animation style.
9. Rules for keeping every asset consistent.

Use a top-down perspective with enough visible front and side details to distinguish characters, buildings, resources, and obstacles.

## B. Asset group 1 — Shivaji Maharaj

Design the principal playable character respectfully, using historical references where available.

Create:

- Idle sprite.
- Walking sprites facing up, down, left, and right.
- Sword attack sprites.
- Damage reaction sprite.
- Dodge or dash animation.
- Astra activation pose.
- Victory pose.

Requirements:

- Recognisable saffron or earthy-coloured attire.
- Historically inspired turban.
- Sword with a clear silhouette.
- Simple armour details.
- Consistent proportions across all poses.
- Readable facial and clothing details at low resolution.

Provide a sprite specification for every animation, including frame dimensions, frame count, frame order, and suggested frame duration.

If generating sprite sheets, use a transparent background, a uniform grid, and clearly separated frames. Do not merge unrelated characters into the same sheet.

## C. Asset group 2 — Enemy soldiers

Design five visually distinguishable enemy classes:

1. Basic swordsman.
2. Shielded guard.
3. Ranged attacker.
4. Charging soldier.
5. Elite fortress guard.

For each class, specify:

- Idle animation.
- Walking animation.
- Attack animation.
- Damage animation.
- Defeat animation.
- Primary colours.
- Equipment and silhouette.
- Relative sprite dimensions.

Enemies must be visually distinguishable even when viewed at the game's small native resolution.

Avoid using the same sprite recoloured for every enemy class.

## D. Asset group 3 — Major bosses

Design three major bosses.

**Afzal Khan — Level 25**

A powerful commander with a large silhouette, distinctive clothing, heavy weaponry, and intimidating combat animations.

**Shaista Khan — Level 50**

A commander suited to the Lal Mahal night infiltration mission, with distinct clothing, equipment, and attack animations.

**Aurangzeb — Level 75**

The final antagonist of the game's fictional alternate-history fantasy finale, with a recognisable royal appearance and distinctive combat animations.

For every boss, provide:

- Idle sprite.
- Movement sprites.
- Three or more attack animations.
- Damage reaction.
- Phase transition effect.
- Defeat animation.
- Recommended hitbox.
- Recommended sprite dimensions.
- Distinct colour palette.

Keep the character designs stylised and suitable for a respectful historical fantasy game.

## E. Asset group 4 — Environment tileset

Create a modular top-down tileset containing:

**Forest terrain**

- Grass.
- Dark grass.
- Forest floor.
- Dirt path.
- Mud.
- Fallen leaves.
- Small flowers.
- Bushes.

**Mountain terrain**

- Stone.
- Rocky ground.
- Cliff edges.
- Mountain walls.
- Narrow passes.
- Loose stones.

**Water terrain**

- Shallow water.
- Deep water.
- River edges.
- Small water animations.

**Fort terrain**

- Stone floor.
- Fort walls.
- Wall corners.
- Wall ends.
- Wooden doors.
- Closed gates.
- Open gates.
- Courtyard floor.
- Stairs and elevated platforms where suitable.

Each standard tile must align to a 16 × 16 pixel grid.

Specify which tiles are walkable, which are solid, and which require special interaction.

## F. Asset group 5 — Trees, rocks, and harvestable resources

Design individual reusable objects for:

- Sagwan trees.
- Small trees.
- Large trees.
- Bushes.
- Dead trees.
- Rock formations.
- Iron Ore deposits.
- Gold deposits.
- Rare mineral nodes.
- Fallen logs.
- Wooden crates.
- Treasure chests.
- Supply containers.

Sagwan trees and Iron Ore deposits must have distinct silhouettes.

Create at least three visual states for harvestable resources:

1. Full resource.
2. Partially harvested.
3. Depleted or removed.

These states will help the game show that a resource has actually been collected.

## G. Asset group 6 — Buildings and structures

Design:

- Small village houses.
- Village huts.
- Blacksmith workshop.
- Healer or restoration station.
- Shrine dedicated to Goddess Bhavani.
- Fort entrance.
- Fort gatehouse.
- Watchtower.
- Storage building.
- Palace courtyard structures.
- Raigad Fort landmarks.

Keep the structures modular wherever practical.

Create separate wall segments, doors, roofs, corners, and decorative elements so that the game can construct different fort layouts without drawing an entirely new building for each level.

## H. Asset group 7 — Weapons, armour, and inventory icons

Design pixel-art icons for:

- Basic sword.
- Improved sword.
- Legendary sword.
- Armour tiers.
- Sagwan Wood.
- Iron Ore.
- Gold.
- Rare crafting material.
- Health restoration.
- Agni Astra.
- Varuna Astra.
- Bhoomi Astra.
- Boss rewards.
- Mission rewards.

Each inventory icon should remain recognisable at 16 × 16 or 24 × 24 pixels.

Create a consistent icon border, lighting style, and background treatment.

## I. Asset group 8 — Divine Astra effects

Create visual specifications for:

**Agni Astra:** A red-orange radial flame wave with small embers and a brief burning effect.

**Varuna Astra:** A blue water ring, flowing droplets, and a restorative visual pulse.

**Bhoomi Astra:** An expanding earth-coloured shockwave, ground cracks, and small stone particles.

For each ability, specify:

- Animation frames.
- Frame duration.
- Effect radius.
- Colour palette.
- Spawn position relative to the player.
- Visual start and end states.
- Maximum particle count.
- Rules for keeping effects readable on a small screen.

The effects must not obscure the player or hide important enemy attack warnings.

## J. Asset group 9 — World map and interface graphics

Create a visual design specification for:

- Main menu background.
- Campaign map.
- Fort icons.
- Mission markers.
- Player health bar.
- Boss health bar.
- Astra ability icons.
- Inventory panel.
- Upgrade panel.
- Pause menu.
- Game-over screen.
- Level-complete screen.
- Final victory screen.

Use a restrained Indian historical-fantasy visual identity, incorporating stone, parchment, forest, and saffron-inspired colours.

Ensure that interface elements remain readable on mobile screens.

## K. Asset group 10 — Environment variations

Create separate visual themes for:

1. Sahyadri forest.
2. Mountain passes.
3. Occupied villages.
4. Ordinary forts.
5. Pratapgad boss arena.
6. Lal Mahal at night.
7. High mountain fortifications.
8. Raigad finale.

Each theme should reuse the same core art style while changing terrain colours, decoration, building shapes, and atmospheric details.

## L. Required output format

Deliver the visual specification in this order:

1. Master art bible.
2. Colour palette with hexadecimal colour values.
3. Character design sheets.
4. Character animation specifications.
5. Enemy and boss sprite specifications.
6. Terrain tileset.
7. Trees, rocks, and resource objects.
8. Buildings and fort modules.
9. Weapon, armour, and inventory icons.
10. Astra effects.
11. UI graphics.
12. Regional environment variations.
13. Asset manifest describing every asset's name, dimensions, frame count, and intended use.

When generating actual artwork, create separate, properly aligned transparent sprite sheets or individual assets. Never place multiple unrelated objects into a single illustration unless the output is explicitly an asset overview sheet.

If the artwork tool cannot create a technically usable sprite sheet, provide individual images and document their dimensions and intended filenames.

Do not claim that an image is a production-ready sprite sheet unless its frames, transparency, dimensions, and alignment have been checked.

The final result must be a coherent visual asset library that can be integrated into a lightweight HTML5 Canvas game without changing the art style halfway through development.

## 3. Next: the technical development prompt

After the artwork is designed, give your coding AI this second prompt. Its job is to turn the assets into a functioning engine.

# TECHNICAL GAME ENGINE PROMPT

## Chronicles of Swarajya: The Divine Blade

Act as a senior HTML5 Canvas game-engine developer and JavaScript architect.

I have a visual design specification for a low-resolution top-down action RPG titled "Chronicles of Swarajya: The Divine Blade".

Your task is to develop the game engine that will render these assets and implement the gameplay.

Do not redesign the art style or substitute placeholder shapes for available approved artwork.

## 1. Before implementation

First inspect the provided asset library and its manifest.

Identify:

- Every character sprite sheet.
- Frame dimensions and animation layouts.
- Terrain tiles.
- Fort modules.
- Resource objects.
- Weapons and inventory icons.
- Astra effects.
- UI assets.
- Missing or unusable assets.

Produce a concise asset integration report before writing code.

If assets are missing, identify them explicitly. Do not silently pretend they exist. Use temporary procedural sprites only for genuinely missing assets, keeping them visually consistent with the approved art style.

## 2. Technical stack

Use:

- HTML5.
- CSS3.
- Vanilla JavaScript ES6+.
- Canvas 2D.
- requestAnimationFrame.
- localStorage for campaign persistence.

The final deliverable must be a self-contained `index.html`, with no build system or external JavaScript libraries.

All assets must be embedded in the file or drawn procedurally if necessary. Do not create runtime dependencies on remote images, external fonts, CDNs, or APIs.

## 3. Rendering

Use a logical 160 × 160 game canvas with crisp pixel rendering.

Scale the game to the available viewport without distorting the aspect ratio.

Implement:

- Camera following.
- Tilemap rendering.
- Sprite-sheet animation.
- Layered environmental objects.
- Correct character depth sorting.
- Animation timing.
- Limited particle effects.
- Responsive UI.

Render objects in the correct order so that the player can move behind trees and walls when appropriate.

Avoid blurring, stretched sprites, and inconsistent pixel sizes.

## 4. Core engine

Implement distinct systems for:

- Game states.
- Keyboard and touch input.
- Player movement.
- Collision detection.
- Enemy AI.
- Combat.
- Boss encounters.
- Resource harvesting.
- Inventory.
- Crafting and upgrades.
- Astra abilities.
- Level generation.
- Missions.
- Saving and loading.
- UI rendering.
- Audio, if implemented.

Use a fixed-step or otherwise frame-rate-independent simulation.

Pause gameplay when the game is paused or a blocking menu is open.

Ensure that each level transition properly clears old enemies, projectiles, effects, and resource objects.

## 5. Gameplay integration

Implement the complete campaign progression:

- Level 1: Select one starting Astra.
- Level 25: Afzal Khan encounter and unlock a missing second Astra.
- Level 50: Lal Mahal infiltration, Shaista Khan encounter, and unlock the final Astra.
- Level 75: Raigad finale and final victory.

Generate varied ordinary levels between major milestones.

Every ordinary level must contain a playable map, reachable resources, appropriate enemies, a Fort Keeper, and a working exit gate.

Use authored maps for major boss encounters.

## 6. Mobile interface

Implement:

- Virtual joystick or directional pad.
- Attack button.
- Astra button.
- Upgrade button.
- Pause button.
- Responsive health and resource HUD.
- Touch cancellation handling.
- Prevention of accidental page scrolling during joystick use.

Support both portrait and landscape layouts.

Keep important combat information visible and avoid placing touch controls over the player's central combat area.

## 7. Persistence

Use a validated, versioned save structure.

Save campaign progress, equipment, resources, unlocked Astras, completed missions, and settings.

Validate data before loading it.

Prevent invalid save data from breaking the game.

## 8. Testing requirements

Test:

- Asset loading.
- Sprite-sheet frame alignment.
- Animation playback.
- Collision detection.
- Resource collection.
- Upgrade cost validation.
- Enemy attacks.
- Astra cooldowns.
- Boss phase transitions.
- Exit gate conditions.
- Campaign saving.
- Mobile touch input.
- Final victory.

Create a playable first level before expanding to all 75 levels. Verify the first level's complete gameplay loop before adding further complexity.

Do not report a test as passed unless it has actually been performed.

## 9. Delivery

Deliver the complete HTML file and a short report explaining:

- How to run the game.
- How assets are integrated.
- Which features are complete.
- Which features still need work.
- Any known bugs.

Prioritise correctness, performance, and playable gameplay over unnecessary complexity.

The result must be a functional game using the approved visual assets, not merely a visual prototype.

## 4. The asset creation order I recommend

Do not try to generate every tree, weapon, boss, and effect in one enormous image-generation request. Generate them in batches and verify the results.

[Ultimate Pixel Top Down Character Pack – Godot Assets Marketplace](https://images.openai.com/static-rsc-4/nf_hGijCZho8VJvnkYr8dITNaUJO69U2vqg_Rhk2RZBM7xnk3NVu46cRhZCdk6YvxuncTLoUZ-88s4X1HWI-eQ1wpu-n2IoYxLAqR9Rr-siRXHvuXXw4-cNCRdY1vZMF6vqYR1d-yN9dLiSAfVJpvwhjWLGufP_TEqPyBQtjr1w?purpose=inline)

Batch 1 — Shivaji Maharaj

Idle, four-direction movement, sword attack, damage, dodge.

[⚡ TileMaker | Sorceress](https://images.openai.com/static-rsc-4/RqNQdeQZ7_nizzg3MRCARkj3vDvy9JOp_-T1peNmJJyXYTUM4xBdFfQn7pOKpq2OD79njw5ZQ8_BJELmdj3L04Bq2Rl4F4H9FQCqsBMq9UYxc_Is8QikZhrhmKEQOK1j5jMuMpbPOn1-25hfDiNoCHbGkwYC54r2nFiEGQeQgcs?purpose=inline)

Batch 2 — Terrain and trees

Grass, dirt, paths, Sagwan trees, rocks, water, mountain edges.

[Pixel Art Top Down - Basic | 2D Environments | Unity Asset Store | Pixel art, Art, Pixel](https://images.openai.com/static-rsc-4/qk7AfjWmxHSVj1YU80P40vh1ESAsD8UAZ6y85cARfYqozxnfBkv88tCBfbM7ACO982k83_6OA3D2hYf-vuZjKb8hV39ENYbONSBS_dmaclcvRhj5BOqzrdTkWPS3Q_2YaBae-wzROWydys-5SAb86_y-IV1SVWSxip9zMExVGjw?purpose=inline)

Batch 3 — Fort construction kit

Walls, corners, gates, courtyards, houses, shrines, towers.

[Set of sprites from above for a top-down dungeon crawler 2d game. From above is very important. Barbarian, knight, ranger, adventurer.](https://images.openai.com/static-rsc-4/rXf2eUHd-L-SWI3hUh_KVG3Dqbnl11gPpJKTnn7DMujlruq-ZjmXnKvR75ZyTiF11nhli5xJ596CQU8Ht52pY4lCx1pXSFeq1Hd8NZku05eUnW_KqLJMRCTu8hYBTU7h4daFhsSN3e2AtgkEECeWe2HOYfZ9J_xpw8X5h0KoZVk?purpose=inline)

Batch 4 — Enemies and bosses

Five ordinary enemy types, followed by three individually designed bosses.

[GPT Image v2 API - AI Text to Image | each::labs](https://images.openai.com/static-rsc-4/VlITrmTASPrV-sJdh8zHTJjDsJ0xDSXE1AzMA-QNOXelGGBa3TRCAD9XXXpASlO69JoxM0-b2SW8IFRdU_FdlfuEntL8LBtf6A8xuqPAUGmfHZZG3UCVe3u0ap6AZeSaPqNvCvcQB7KTYNTtXEc4YoKcd6Ug02x3MG6epV-pSsc?purpose=inline)

Batch 5 — Resources and abilities

Harvestable nodes, inventory icons, Astra effects, crafting items.

[Chapter 2 Sneak Peek #103: Adding Side Quests, Part 7 - Alchemica - Crafting RPG by Crunchy Bit Games](https://images.openai.com/static-rsc-4/PVskhOAqSIwGnGMvdF4FjBKndpK-6KJA1FaPyaY12yDxqRWZf71dMgqKSL5Lfrt5Dai8QPUjIv8hbASY3aDNvikZU6sD997U-J6RH2Hqff2ZdfElQIDEJ7H8xnBJf8vb7csxGlReDgM-mGal4iipD1YBOKn6cCKF4xFUz0b3jsU?purpose=inline)

Batch 6 — Interface

Main menu, Astra selection, HUD, upgrades, map, pause and victory screens.

## 5. The most important technical choice: individual assets or one image?

For a game engine, individual assets and properly aligned sprite sheets are much more useful than a single giant concept-art image.

| Asset                | Recommended format                         | Why                         |
| -------------------- | ------------------------------------------ | --------------------------- |
| Shivaji and soldiers | Transparent PNG sprite sheets              | Supports animation          |
| Trees and rocks      | Individual transparent PNGs                | Easy to place independently |
| Terrain              | Tile atlas or tileset PNG                  | Reusable map construction   |
| Fort walls           | Modular transparent sprites or tiles       | Procedural fort layouts     |
| Inventory icons      | Individual PNGs or an aligned icon sheet   | Easy UI integration         |
| Astra effects        | Sprite sheets or procedural effects        | Animation and timing        |
| UI                   | CSS-drawn interface or individual graphics | Responsive mobile design    |

A concept image showing a forest with a fort and a warrior is useful for visual direction, but it is not automatically a usable game map: it may have inconsistent perspective, non-aligned objects, or no collision information.

For every asset, maintain a manifest with its filename, pixel dimensions, frame layout, and collision properties where applicable.

## 6. Your development roadmap

Stage 1 — Visual design

Finalise Shivaji's appearance, one forest tileset, trees, rocks, one enemy, and a small fort kit.

Stage 2 — A single playable map

Build a small forest and fort. Add player movement, walls, camera, resource collection, and the first enemy.

Stage 3 — Combat and upgrades

Add sword combat, the first Astra, the Fort Keeper, crafting, armour, and a functioning exit gate.

Stage 4 — Mobile adaptation

Test the joystick, touch buttons, viewport scaling, HUD, and upgrade menu on a real phone.

Stage 5 — Full campaign

Add regional map variations, all 75 levels, special bosses, mission rewards, saving, and the ending.

My advice: begin with just Shivaji's sprite, a forest tileset, three tree variations, a few rocks, and a simple fort entrance. Once those assets look consistent and work correctly in the game, expand the library. That gives you a reliable visual foundation instead of 75 levels built from mismatched graphics.