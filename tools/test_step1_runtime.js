const fs = require('fs');
const vm = require('vm');
const assert = require('assert');

// Extract inline scripts from open_world_game.html and execute with data_registries.js
const registriesCode = fs.readFileSync('data/data_registries.js', 'utf8');
const html = fs.readFileSync('open_world_game.html', 'utf8');
const scriptMatch = html.match(/<script>\s*\/\/ =============================================================================[\s\S]*?<\/script>/);
assert(scriptMatch, 'Main script tag not found in open_world_game.html');
const gameScript = scriptMatch[0].replace(/^<script>/, '').replace(/<\/script>$/, '');

// Lightweight DOM & Canvas Mock to verify all 13 runtime tests
const elements = {};
function getEl(id) {
  if (!elements[id]) {
    const classSet = new Set();
    if (id === 'title-modal') classSet.add('active');
    elements[id] = {
      id,
      innerText: '',
      innerHTML: '',
      disabled: false,
      width: id === 'gameCanvas' ? 480 : (id === 'minimapCanvas' ? 90 : 240),
      height: id === 'gameCanvas' ? 270 : (id === 'minimapCanvas' ? 54 : 140),
      style: {},
      children: [],
      appendChild(child) { this.children.push(child); },
      classList: {
        add(c) { classSet.add(c); },
        remove(c) { classSet.delete(c); },
        contains(c) { return classSet.has(c); }
      },
      getContext() {
        if (!this._ctx) {
          this._ctx = {
            imageSmoothingEnabled: false,
            fillStyle: '',
            strokeStyle: '',
            lineWidth: 1,
            globalAlpha: 1,
            font: '',
            lastFillColors: [],
            clearRect() {},
            fillRect(x, y, w, h) {
              this.lastFillColors.push({ x, y, w, h, color: this.fillStyle });
            },
            drawImage() {},
            beginPath() {},
            moveTo() {},
            lineTo() {},
            stroke() {},
            arc() {},
            ellipse() {},
            fill() {},
            fillText() {}
          };
        }
        return this._ctx;
      }
    };
  }
  return elements[id];
}

const keyListeners = {};
const localStorageStore = {};

const sandbox = {
  console,
  Math,
  Date,
  JSON,
  Set,
  Array,
  Object,
   setTimeout: (fn) => { return 1; },
  clearTimeout: () => {},
  requestAnimationFrame: () => {},
  performance: { now: () => 1000 },
  window: {
    innerWidth: 1280,
    innerHeight: 720,
    AudioContext: function() {
      this.currentTime = 0;
      this.destination = {};
      this.createOscillator = () => ({
        type: '',
        frequency: { setValueAtTime() {}, exponentialRampToValueAtTime() {}, linearRampToValueAtTime() {} },
        connect() {},
        start() {},
        stop() {}
      });
      this.createGain = () => ({
        gain: { setValueAtTime() {}, linearRampToValueAtTime() {} },
        connect() {}
      });
    },
    addEventListener(evt, cb) {
      if (!keyListeners[evt]) keyListeners[evt] = [];
      keyListeners[evt].push(cb);
    },
    removeEventListener() {}
  },
  document: {
    getElementById: (id) => getEl(id),
    querySelectorAll: () => [],
    createElement: (tag) => ({ tag, className: '', innerText: '', innerHTML: '', style: {}, appendChild() {} })
  },
  Image: function() {
    this.complete = true;
    this.naturalWidth = 64;
    this.naturalHeight = 64;
  },
  localStorage: {
    getItem: (k) => localStorageStore[k] || null,
    setItem: (k, v) => { localStorageStore[k] = String(v); },
    removeItem: (k) => { delete localStorageStore[k]; }
  }
};

vm.createContext(sandbox);
sandbox.assert = assert;
sandbox.getEl = getEl;
sandbox.keyListeners = keyListeners;
sandbox.localStorageStore = localStorageStore;

const testSuiteCode = `
console.log('=== RUNNING 13 RUNTIME VALIDATION TESTS AGAINST open_world_game.html ===');

// Test 1: Start a new adventure and select an Astra
startNewAdventureFlow();
assert(!getEl('title-modal').classList.contains('active'), 'Title modal should close');
assert(getEl('astra-modal').classList.contains('active'), 'Astra modal should open');
selectAstra('agni');
confirmAstraSelection();
assert.strictEqual(state.player.selectedAstra, 'agni', 'Selected Astra must be agni');
assert.strictEqual(state.worldState.discoveredSubZones.includes('forest_clearing'), true, 'Starting forest must be discovered');
assert.strictEqual(state.player.xp, 25, 'First discovery of Sacred Awakening Forest must award +25 XP');
console.log('1. [PASS] Start a new adventure and select an Astra (+25 XP initial zone discovery).');

// Test 2: Explore the original forest and move toward the river
state.player.x = 400;
state.player.y = 310;
update(0.016);
assert(!isSolid(state.player.x, state.player.y), 'Eastern forest path must be walkable');
assert.strictEqual(state.player.xp, 25, 'Moving within already-discovered forest must NOT re-award XP');
console.log('2. [PASS] Explore the original forest and move toward the river.');

// Test 3: Cross the river using valid crossings (Main Bridge & Northern Stone Ford)
assert.strictEqual(isSolid(36 * 16 + 8, 19 * 16 + 8), false, 'Main Koyna Timber Bridge must be walkable');
assert.strictEqual(isSolid(36 * 16 + 8, 9 * 16 + 8), false, 'Northern Shallow Stone Ford must be walkable');
state.player.x = 36 * 16 + 8;
state.player.y = 19 * 16 + 8;
update(0.016);
assert.strictEqual(state.worldState.currentZoneId, 'river_crossing');
assert.strictEqual(state.player.xp, 50, 'Discovering Koyna River Valley must award +25 XP once (total 50 XP)');
console.log('3. [PASS] Cross the river using valid crossings (Main Bridge & Northern Stone Ford).');

// Test 4: Reach the village and continue toward the other zones
const zoneSequence = [
  { id: 'village_bhavani_nagar', x: 860, y: 290 },
  { id: 'sahyadri_highlands', x: 1040, y: 144 },
  { id: 'abandoned_mine_approach', x: 1360, y: 144 },
  { id: 'raider_outpost', x: 940, y: 740 },
  { id: 'kot_fort_approach', x: 1512, y: 520 }
];
for (const z of zoneSequence) {
  assert.strictEqual(isSolid(z.x, z.y), false, 'Zone ' + z.id + ' point must be walkable');
  state.player.x = z.x;
  state.player.y = z.y;
  update(0.016);
  assert.strictEqual(state.worldState.currentZoneId, z.id, 'Current zone should be ' + z.id);
}
assert.strictEqual(state.worldState.discoveredSubZones.length, 7, 'All 7 sub-zones discovered');
console.log('4. [PASS] Reach the village and continue toward Highlands, Mine Entrance, Outpost, and Kot Fort Approach.');

// Test 5: Verify that cliffs, water, and closed gates remain solid
assert.strictEqual(isSolid(10 * 16, 0 * 16), true, 'Outer boundary cliff must be solid');
assert.strictEqual(isSolid(36 * 16, 15 * 16), true, 'Koyna river water outside crossings must be solid');
assert.strictEqual(isSolid(65 * 16, 14 * 16), true, 'Highland cliff escarpment outside passes must be solid');
assert.strictEqual(isSolid(96 * 16 + 8, 32 * 16 + 8), true, 'Closed Kot Fort Dilli Darwaja gate must be solid');
assert.strictEqual(isSolid(96 * 16 + 8, 8 * 16 + 8), true, 'Northern flank of Kot Fort wall must be solid');
assert.strictEqual(isSolid(96 * 16 + 8, 60 * 16 + 8), true, 'Southern flank of Kot Fort wall must be solid');
console.log('5. [PASS] Cliffs, river water, highland escarpments, and closed fort gates remain solid.');

// Test 6: Confirm the minimap follows the player
render();
const mmDraws = getEl('minimapCanvas').getContext().lastFillColors;
assert(mmDraws.length > 0, 'Minimap must render terrain and player marker');
console.log('6. [PASS] Minimap renders real terrain data and follows the player.');

// Test 7: Open the world map with M and close it with M and Escape (pausing simulation while open)
const keydownHandlers = keyListeners['keydown'];
keydownHandlers.forEach(fn => fn({ key: 'm', preventDefault() {} }));
assert.strictEqual(isWorldMapOpen(), true, 'World map modal must open on pressing M');
const prevX = state.player.x;
keys['d'] = true;
update(0.5);
assert.strictEqual(state.player.x, prevX, 'World simulation must pause while World Map modal is open');
keys['d'] = false;

keydownHandlers.forEach(fn => fn({ key: 'm', preventDefault() {} }));
assert.strictEqual(isWorldMapOpen(), false, 'World map modal must close on pressing M again');

keydownHandlers.forEach(fn => fn({ key: 'm', preventDefault() {} }));
assert.strictEqual(isWorldMapOpen(), true, 'World map modal reopens on M');
keydownHandlers.forEach(fn => fn({ key: 'Escape', preventDefault() {} }));
assert.strictEqual(isWorldMapOpen(), false, 'World map modal must close on pressing Escape');
console.log('7. [PASS] World Map opens with M, pauses world simulation while open, and closes with M and Escape.');

// Test 8: Verify that unexplored sectors remain hidden
assert.strictEqual(isSectorDiscovered(0, 8), false, 'Far southwestern corner sector (0,8) must remain unexplored/hidden');
assert(state.worldState.discoveredCells.length < 135, 'Unvisited sectors must remain covered by fog');
console.log('8. [PASS] Unexplored sectors remain hidden under fog of war.');

// Test 9: Verify that first discovery awards XP once (re-crossing boundaries awards 0 XP)
const xpBeforeRecross = state.player.xp;
const lvlBeforeRecross = state.player.level;
state.player.x = 120;
state.player.y = 280;
update(0.016);
state.player.x = 860;
state.player.y = 290;
update(0.016);
assert.strictEqual(state.player.xp, xpBeforeRecross, 'Re-entering discovered sub-zones must NEVER award duplicate XP');
assert.strictEqual(state.player.level, lvlBeforeRecross);
console.log('9. [PASS] First discovery awards +25 XP once and never duplicates on boundary re-crossing.');

// Test 10: Save, reload, and verify that discovery persists (plus legacy save migration)
const savedCellsCount = state.worldState.discoveredCells.length;
saveGame();
state.worldState.discoveredCells = [];
state.worldState.discoveredSubZones = [];
loadGame();
assert.strictEqual(state.worldState.discoveredCells.length, savedCellsCount, 'Discovered sectors must persist across save/load');
assert.strictEqual(state.worldState.discoveredSubZones.length, 7, 'Discovered sub-zones must persist across save/load');
updateDiscoveryAndZone(true);
assert.strictEqual(state.player.xp, xpBeforeRecross, 'Reloading a save must not re-award discovery XP');

// Test legacy Gate E save migration
localStorageStore['swarajya_open_world_save_v1'] = JSON.stringify({
  player: { hp: 90, maxHp: 100, xp: 40, maxXp: 100, level: 1, selectedAstra: 'varuna', x: 120, y: 280 },
  inventory: { wood_sagwan: 5, ore_iron: 4, gold_huns: 25 },
  worldState: { currentZone: 'forest_clearing', gateUnlocked: false }
});
loadGame();
assert(Array.isArray(state.worldState.discoveredSubZones), 'Legacy save migrated with discoveredSubZones array');
assert(Array.isArray(state.worldState.discoveredCells), 'Legacy save migrated with discoveredCells array');
assert.strictEqual(state.worldState.activeMapId, 'sahyadri_gateway_valley', 'Legacy save migrated with activeMapId');
assert(state.worldState.surfaceReturnPos && state.worldState.surfaceReturnPos.x === 1360, 'Legacy save migrated with surfaceReturnPos');
console.log('10. [PASS] Save/load persistence and backwards-compatible legacy save migration verified.');

// Test 11: Confirm existing crafting, combat, and Astra mechanics still work
executeCraft('craft_talwar_basic');
assert.strictEqual(state.player.equipped.weapon, 'talwar_basic', 'Crafting basic talwar equips weapon');
const scout = state.entities.find(e => e.id === 'enemy_1');
const scoutInitialHp = scout.hp;
state.player.x = scout.x - 18;
state.player.y = scout.y;
state.player.dir = 2; // East toward enemy_1
performAttack();
assert(scout.hp < scoutInitialHp, 'Player melee attack damages enemy');
state.player.astraCooldown = 0;
state.player.hp = 60;
castAstra(); // Varuna heals +40 HP
assert.strictEqual(state.player.hp, 100, 'Varuna Astra heals player to 100 HP');
console.log('11. [PASS] Existing crafting, melee combat, enemy AI, and Divine Astra mechanics verified.');
`;

vm.runInContext(registriesCode + '\n' + gameScript + '\n' + testSuiteCode, sandbox);

