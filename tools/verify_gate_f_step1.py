import json
import os
import re
import sys
from collections import deque

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORLD_COLS = 120
WORLD_ROWS = 70
TILE_SIZE = 16

def build_collision_map(gate_unlocked=False):
    col_map = []
    for r in range(WORLD_ROWS):
        row = []
        for c in range(WORLD_COLS):
            if r <= 1 or r >= WORLD_ROWS - 2 or c == 0 or c == WORLD_COLS - 1:
                row.append(1)
                continue

            isCentralForestToVillageRoad = (18 <= r <= 21 and 6 <= c <= 65)
            isNorthernForestToMineTrail = (8 <= r <= 10 and 14 <= c <= 87)
            isForestNorthSouthConnector = (14 <= c <= 16 and 8 <= r <= 21)
            isHighlandVillageOutpostSpine = (58 <= c <= 60 and 8 <= r <= 50)
            isVillageToKotFortApproachRoad = (31 <= r <= 34 and 58 <= c <= 95)
            isMineToFortMountainRoad = (84 <= c <= 86 and 8 <= r <= 48)
            isOutpostToFortMilitaryRoad = (46 <= r <= 48 and 58 <= c <= 86)

            if 35 <= c <= 38:
                if 18 <= r <= 21 or 8 <= r <= 10:
                    row.append(0)
                else:
                    row.append(2)
                continue

            if c == 96 and (r < 12 or r > 54):
                row.append(1)
                continue
            if 96 <= c <= 115 and 12 <= r <= 54:
                if c == 96 and 31 <= r <= 34:
                    row.append(0 if gate_unlocked else 1)
                elif c == 96 or c == 115 or r == 12 or r == 54:
                    row.append(1)
                else:
                    row.append(0)
                continue

            if 47 <= c <= 92 and r <= 14:
                if r == 14:
                    if isHighlandVillageOutpostSpine or isMineToFortMountainRoad:
                        row.append(0)
                    else:
                        row.append(1)
                    continue
                if r <= 4 and 50 <= c <= 90:
                    row.append(1)
                    continue
                row.append(0)
                continue

            if 47 <= c <= 76 and 15 <= r <= 37:
                if c == 55 and r == 23:
                    row.append(1)
                else:
                    row.append(0)
                continue

            row.append(0)
        col_map.append(row)
    return col_map

def bfs_reachable(col_map, start_tile, target_tile):
    sc, sr = start_tile
    tc, tr = target_tile
    if col_map[sr][sc] != 0 or col_map[tr][tc] != 0:
        return False
    visited = set([(sc, sr)])
    q = deque([(sc, sr)])
    while q:
        c, r = q.popleft()
        if (c, r) == (tc, tr):
            return True
        for dc, dr in [(1,0), (-1,0), (0,1), (0,-1)]:
            nc, nr = c + dc, r + dr
            if 0 <= nc < WORLD_COLS and 0 <= nr < WORLD_ROWS:
                if (nc, nr) not in visited and col_map[nr][nc] == 0:
                    visited.add((nc, nr))
                    q.append((nc, nr))
    return False

def to_tile(x, y):
    return (int(x // TILE_SIZE), int(y // TILE_SIZE))

def main():
    print("=== GATE F STEP 1: WORLD ARCHITECTURE & WALKABILITY VERIFICATION ===")
    with open('data/world_regions.json', 'r', encoding='utf-8') as f:
        wr = json.load(f)['regions']

    valley = wr['sahyadri_gateway_valley']
    assert valley['worldWidth'] == 120 and valley['worldHeight'] == 70, "World size must be 120x70"
    assert valley['sectorCols'] == 15 and valley['sectorRows'] == 9, "Sector grid must be 15x9"

    # 1. Verify exact partition of 120x70 tiles across subZones (no overlaps, no gaps)
    sub_zones = valley['subZones']
    for r in range(WORLD_ROWS):
        for c in range(WORLD_COLS):
            matches = [sz['id'] for sz in sub_zones if sz['bounds']['x1'] <= c <= sz['bounds']['x2'] and sz['bounds']['y1'] <= r <= sz['bounds']['y2']]
            assert len(matches) == 1, f"Tile ({c},{r}) matched {matches} subZones (expected 1)"
    print(f"✅ All {WORLD_COLS * WORLD_ROWS} surface tiles partitioned cleanly across {len(sub_zones)} non-overlapping sub-zones.")

    # 2. Verify registered interior cave metadata
    cave = wr['sahyadri_iron_cavern']
    assert cave['isInterior'] is True and cave['worldWidth'] == 40 and cave['worldHeight'] == 25
    print("✅ Interior region 'sahyadri_iron_cavern' (40x25) registered with entrance & return metadata.")

    # 3. Verify Walkability & Barrier Integrity (Gate Closed vs Gate Open)
    cmap_closed = build_collision_map(gate_unlocked=False)
    cmap_open = build_collision_map(gate_unlocked=True)

    spawn = to_tile(120, 280)
    anvil = to_tile(200, 300)
    north_ford = (36, 9)
    main_bridge = (36, 19)
    elder = to_tile(860, 290)
    forge = to_tile(980, 290)
    highlands = to_tile(1040, 144)
    mine_entrance = to_tile(1360, 144)
    outpost = to_tile(940, 740)
    fort_approach = to_tile(1512, 520)
    flag_inside_fort = to_tile(1760, 520)

    for label, pt in [
        ("Spawn", spawn), ("Field Anvil", anvil), ("North Ford", north_ford),
        ("Main Bridge", main_bridge), ("Village Elder", elder), ("Village Forge", forge),
        ("Sahyadri Highlands", highlands), ("Mine Entrance", mine_entrance),
        ("Raider Outpost", outpost), ("Kot Fort Approach", fort_approach)
    ]:
        assert cmap_closed[pt[1]][pt[0]] == 0, f"{label} at tile {pt} is on solid terrain!"
        assert bfs_reachable(cmap_closed, spawn, pt), f"{label} at tile {pt} is NOT reachable from Spawn!"
    print("✅ BFS Connectivity Confirmed: Spawn -> Both River Crossings -> Village -> Highlands -> Mine Entrance -> Outpost -> Fort Approach.")

    # Verify River water cannot be crossed outside crossings
    for r in range(2, 68):
        if not (8 <= r <= 10 or 18 <= r <= 21):
            assert cmap_closed[r][36] == 2, f"River at row {r} is not solid water!"
    print("✅ River barrier integrity confirmed (solid water except at Northern Stone Ford and Main Timber Bridge).")

    # Verify Fort Enclosure when gate is closed vs open
    assert not bfs_reachable(cmap_closed, spawn, flag_inside_fort), "Fort courtyard should be unreachable while gate is locked!"
    assert bfs_reachable(cmap_open, spawn, flag_inside_fort), "Fort courtyard must be reachable once Dilli Darwaja gate is unlocked!"
    print("✅ Kot Fort enclosure confirmed: Impassable when gate is locked, reachable through Dilli Darwaja when unlocked.")

    # 4. Verify all ASSETS in open_world_game.html exist on disk
    with open('open_world_game.html', 'r', encoding='utf-8') as f:
        html = f.read()
    asset_paths = re.findall(r"'(ChroniclesOfSwarajya_Art/[^']+\.png)'", html)
    for p in asset_paths:
        assert os.path.exists(p), f"Missing asset file: {p}"
    print(f"✅ All {len(asset_paths)} referenced PNG assets in open_world_game.html exist on disk.")

if __name__ == "__main__":
    main()
