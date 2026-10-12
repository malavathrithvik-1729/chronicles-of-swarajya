import os
import math
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw

# Master Environment Color Tokens from environment_style_guide.md
E = {
    # Sky & Distant Atmosphere
    "SKY_DEEP": (45, 78, 120, 255),
    "SKY_MID": (95, 145, 195, 255),
    "SKY_HORIZON": (175, 205, 225, 255),
    "MIST_LIGHT": (210, 225, 235, 160),
    "MIST_WARM": (230, 215, 195, 120),
    
    # Grass & Flora
    "GRASS_BASE": (58, 99, 42, 255),      # #3a632a
    "GRASS_DARK": (40, 70, 29, 255),      # #28461d
    "GRASS_LIGHT": (84, 135, 61, 255),    # #54873d
    "GRASS_MEADOW": (101, 163, 13, 255),  # #65a30d
    "FLOWER_YELLOW": (250, 204, 21, 255), # #facc15
    "FLOWER_ORANGE": (234, 88, 12, 255),  # #ea580c
    "MOSS": (77, 124, 15, 255),
    
    # Earth & Dirt Paths
    "DIRT_BASE": (121, 85, 56, 255),      # #795538
    "DIRT_LIGHT": (153, 112, 78, 255),    # #99704e
    "DIRT_DARK": (84, 51, 16, 255),       # #543310
    "DIRT_MUD": (62, 36, 12, 255),        # #3e240c
    
    # Sahyadri Basalt Stone & Cliffs
    "STONE_CLIFF": (39, 39, 42, 255),     # #27272a
    "STONE_DARK": (60, 64, 70, 255),      # #3c4046
    "STONE_BASE": (94, 101, 110, 255),    # #5e656e
    "STONE_LIGHT": (140, 147, 158, 255),  # #8c939e
    "FLAGSTONE_BASE": (71, 85, 105, 255), # #475569
    "FLAGSTONE_TRIM": (100, 116, 139, 255),
    
    # Water Ramps
    "WATER_DEEP": (31, 72, 126, 255),     # #1f487e
    "WATER_MID": (51, 112, 184, 255),     # #3370b8
    "WATER_SHALLOW": (96, 165, 250, 255), # #60a5fa
    "WATER_CREST": (147, 197, 253, 255),
    "WATER_FOAM": (224, 242, 254, 255),   # #e0f2fe
    
    # Sagwan Teak Trees & Timber
    "TEAK_BARK": (66, 40, 23, 255),       # #422817
    "TEAK_LIGHT": (138, 91, 50, 255),     # #8a5b32
    "SAGWAN_LEAF": (101, 163, 13, 255),   # #65a30d
    "SAGWAN_BRIGHT": (132, 204, 22, 255), # #84cc16
    "CANOPY_SHADOW": (30, 63, 20, 255),
    
    # Fort Elements & Saffron Bhagwa Zenda
    "SAFFRON_FLAG": (230, 96, 18, 255),   # #e66012
    "SAFFRON_HI": (245, 158, 11, 255),
    "GOLD_FINIAL": (251, 191, 36, 255),
    "TORCH_FIRE": (249, 115, 22, 255),
    "TORCH_GLOW": (254, 240, 138, 80),
    "IRON_REINFORCE": (30, 41, 59, 255),
}

def draw_rect(draw, x1, y1, x2, y2, color):
    draw.rectangle([round(min(x1, x2)), round(min(y1, y2)), round(max(x1, x2)), round(max(y1, y2))], fill=color)

def draw_sagwan_tree(img, draw, root_x, root_y, scale=1.0):
    """Renders an authentic Sahyadri Sagwan (Teak) tree with broadleaf canopy and textured trunk."""
    trunk_w = int(14 * scale)
    trunk_h = int(50 * scale)
    canopy_rx = int(36 * scale)
    canopy_ry = int(30 * scale)
    canopy_cy = root_y - trunk_h + int(10 * scale)
    
    # Soft drop shadow on ground
    draw.ellipse([root_x - int(24 * scale), root_y - int(6 * scale), root_x + int(24 * scale), root_y + int(6 * scale)], fill=(15, 12, 10, 90))
    
    # Gnarled trunk
    tx1 = root_x - trunk_w // 2
    tx2 = root_x + trunk_w // 2
    draw.rectangle([tx1, canopy_cy + int(10 * scale), tx2, root_y], fill=E["TEAK_BARK"])
    draw.rectangle([tx1 + 2, canopy_cy + int(10 * scale), tx1 + int(5 * scale), root_y], fill=E["TEAK_LIGHT"])
    
    # Layered broadleaf teak canopy (shadow -> mid -> highlight clusters)
    draw.ellipse([root_x - canopy_rx, canopy_cy - canopy_ry + 6, root_x + canopy_rx, canopy_cy + canopy_ry + 6], fill=E["CANOPY_SHADOW"])
    draw.ellipse([root_x - canopy_rx, canopy_cy - canopy_ry, root_x + canopy_rx, canopy_cy + canopy_ry], fill=E["SAGWAN_LEAF"])
    # Highlights top-left
    draw.ellipse([root_x - canopy_rx + int(8 * scale), canopy_cy - canopy_ry + int(4 * scale), root_x + int(10 * scale), canopy_cy + int(10 * scale)], fill=E["SAGWAN_BRIGHT"])
    draw.ellipse([root_x - int(10 * scale), canopy_cy - canopy_ry + int(2 * scale), root_x + int(20 * scale), canopy_cy], fill=E["SAGWAN_BRIGHT"])

# ==============================================================================
# ENVIRONMENT 1: DENSE SAHYADRI TEAK FOREST & RIVER CROSSING
# ==============================================================================
def render_env_forest_river(w=480, h=270):
    img = Image.new("RGBA", (w, h), E["GRASS_DARK"])
    draw = ImageDraw.Draw(img)
    
    # Base Lush Grass Layer
    draw.rectangle([0, 0, w, h], fill=E["GRASS_BASE"])
    
    # Dappled forest light & meadow patches
    for y in range(0, h, 8):
        for x in range(0, w, 8):
            v = math.sin(x * 0.04) * math.cos(y * 0.05)
            if v > 0.4:
                draw.rectangle([x, y, x + 7, y + 7], fill=E["GRASS_MEADOW"])
            elif v < -0.4:
                draw.rectangle([x, y, x + 7, y + 7], fill=E["GRASS_DARK"])

    # Winding River flowing from upper right to lower left
    for y in range(h):
        center_x = int(w * 0.45 + math.sin(y * 0.025) * 55 + (y * 0.2))
        river_w = int(50 + math.sin(y * 0.03) * 12)
        # Deep river bed
        draw.rectangle([center_x - river_w // 2, y, center_x + river_w // 2, y], fill=E["WATER_MID"])
        draw.rectangle([center_x - river_w // 4, y, center_x + river_w // 4, y], fill=E["WATER_DEEP"])
        # Shoreline shallows & foam
        draw.rectangle([center_x - river_w // 2, y, center_x - river_w // 2 + 5, y], fill=E["WATER_SHALLOW"])
        draw.rectangle([center_x + river_w // 2 - 5, y, center_x + river_w // 2, y], fill=E["WATER_SHALLOW"])
        if (y % 6) == 0:
            draw.rectangle([center_x - river_w // 2, y, center_x - river_w // 2 + 2, y], fill=E["WATER_FOAM"])
            draw.rectangle([center_x + river_w // 2 - 2, y, center_x + river_w // 2, y], fill=E["WATER_FOAM"])
            
    # Red Sahyadri Dirt Trail crossing the river via wooden footbridge
    trail_y = int(h * 0.6)
    trail_h = 24
    draw.rectangle([0, trail_y, w, trail_y + trail_h], fill=E["DIRT_BASE"])
    draw.rectangle([0, trail_y + 4, w, trail_y + trail_h - 4], fill=E["DIRT_LIGHT"])
    # Mud at riverbanks
    bridge_cx = int(w * 0.45 + math.sin(trail_y * 0.025) * 55 + (trail_y * 0.2))
    draw.rectangle([bridge_cx - 45, trail_y - 4, bridge_cx - 28, trail_y + trail_h + 4], fill=E["DIRT_MUD"])
    draw.rectangle([bridge_cx + 28, trail_y - 4, bridge_cx + 45, trail_y + trail_h + 4], fill=E["DIRT_MUD"])

    # Heavy Timber Footbridge across River
    bw = 64
    bx1 = bridge_cx - bw // 2
    bx2 = bridge_cx + bw // 2
    by1 = trail_y - 2
    by2 = trail_y + trail_h + 2
    # Shadow under bridge
    draw.rectangle([bx1, by1 + 6, bx2, by2 + 8], fill=(10, 25, 45, 140))
    # Wooden bridge planks
    for px in range(bx1, bx2, 5):
        draw.rectangle([px, by1, px + 4, by2], fill=E["TEAK_LIGHT"])
        draw.rectangle([px + 3, by1, px + 4, by2], fill=E["TEAK_BARK"])
    # Top & bottom handrails
    draw.rectangle([bx1 - 2, by1 - 2, bx2 + 2, by1 + 2], fill=E["TEAK_BARK"])
    draw.rectangle([bx1 - 2, by2 - 2, bx2 + 2, by2 + 2], fill=E["TEAK_BARK"])

    # Wildflowers and mossy rocks on riverbanks
    for fx, fy in [(60, 40), (110, 90), (140, 180), (380, 50), (410, 140), (430, 220), (220, 230)]:
        draw.rectangle([fx, fy, fx + 2, fy + 2], fill=E["FLOWER_YELLOW"])
        draw.rectangle([fx + 8, fy + 4, fx + 10, fy + 6], fill=E["FLOWER_ORANGE"])
    # Basalt river boulders
    for rx, ry, rw, rh in [(bx1 - 35, trail_y - 30, 22, 16), (bx2 + 25, trail_y + 40, 26, 18), (180, 45, 20, 14)]:
        draw.ellipse([rx - 2, ry + rh - 4, rx + rw + 2, ry + rh + 4], fill=(15, 12, 10, 100))
        draw.ellipse([rx, ry, rx + rw, ry + rh], fill=E["STONE_BASE"])
        draw.ellipse([rx + 2, ry + 2, rx + rw - 6, ry + rh - 6], fill=E["STONE_LIGHT"])
        draw.rectangle([rx + 4, ry + 2, rx + 12, ry + 6], fill=E["MOSS"])

    # Teak Forest Tree Groves (Y-Sorted)
    trees = [
        (45, 55, 1.1), (130, 40, 0.9), (340, 45, 1.0), (435, 60, 1.2),
        (55, 150, 1.0), (395, 175, 1.15), (75, 255, 1.2), (440, 250, 1.25),
        (290, 255, 0.95), (25, 220, 1.05)
    ]
    trees.sort(key=lambda t: t[1])
    for tx, ty, sc in trees:
        draw_sagwan_tree(img, draw, tx, ty, sc)
        
    return img

# ==============================================================================
# ENVIRONMENT 2: JAVALI MOUNTAIN PASS & BASALT ESCARPMENT OVERLOOK
# ==============================================================================
def render_env_mountain_pass(w=480, h=270):
    img = Image.new("RGBA", (w, h), E["SKY_DEEP"])
    draw = ImageDraw.Draw(img)
    
    # 1. Distant Sahyadri Sky & Dawn Atmosphere
    for y in range(int(h * 0.45)):
        ratio = y / (h * 0.45)
        r = int(E["SKY_DEEP"][0] * (1 - ratio) + E["SKY_HORIZON"][0] * ratio)
        g = int(E["SKY_DEEP"][1] * (1 - ratio) + E["SKY_HORIZON"][1] * ratio)
        b = int(E["SKY_DEEP"][2] * (1 - ratio) + E["SKY_HORIZON"][2] * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))
        
    # Rising mist bands in valleys
    draw.rectangle([0, int(h * 0.28), w, int(h * 0.42)], fill=E["MIST_LIGHT"])
    draw.rectangle([0, int(h * 0.35), w, int(h * 0.45)], fill=E["MIST_WARM"])
    
    # 2. Distant Sahyadri Mountain Ridges & Peaks
    for x in range(w):
        peak1 = int(h * 0.22 + math.sin(x * 0.015) * 18 + math.cos(x * 0.035) * 10)
        draw.line([(x, peak1), (x, int(h * 0.45))], fill=E["STONE_DARK"])
        peak2 = int(h * 0.30 + math.sin(x * 0.02 + 1.2) * 22)
        draw.line([(x, peak2), (x, int(h * 0.45))], fill=E["STONE_BASE"])

    # 3. Sheer Basalt Escarpment Cliff (Foreground & Midground Ridge)
    cliff_y = int(h * 0.42)
    draw.rectangle([0, cliff_y, w, h], fill=E["STONE_CLIFF"])
    
    # Stratified basalt rock cliff faces
    for y in range(cliff_y, h):
        for x in range(0, w, 16):
            if ((x // 16) + (y // 12)) % 2 == 0:
                draw.rectangle([x, y, x + 15, y + 10], fill=E["STONE_DARK"])
            else:
                draw.rectangle([x, y, x + 15, y + 10], fill=E["STONE_BASE"])
                
    # Sunlit cliff edge rim highlights
    for x in range(w):
        draw.rectangle([x, cliff_y, x, cliff_y + 3], fill=E["STONE_LIGHT"])
        if (x % 24) < 14:
            draw.rectangle([x, cliff_y + 3, x, cliff_y + 6], fill=E["MOSS"])

    # Narrow Winding Ghat Path (Pass carved into the cliff)
    for y in range(cliff_y + 20, h):
        curve_x = int(w * 0.55 + math.sin(y * 0.03) * 60 - ((y - cliff_y) * 0.4))
        path_w = int(45 + math.sin(y * 0.05) * 8)
        draw.rectangle([curve_x - path_w // 2, y, curve_x + path_w // 2, y], fill=E["DIRT_BASE"])
        draw.rectangle([curve_x - path_w // 2 + 4, y, curve_x + path_w // 2 - 4, y], fill=E["DIRT_LIGHT"])
        # Inner mountain wall shadow
        draw.rectangle([curve_x - path_w // 2, y, curve_x - path_w // 2 + 6, y], fill=E["DIRT_DARK"])

    # Wooden & Basalt Guard Watchpoint & Wooden Palisades
    draw.rectangle([int(w * 0.15), cliff_y + 30, int(w * 0.32), cliff_y + 90], fill=E["STONE_BASE"])
    draw.rectangle([int(w * 0.15) - 2, cliff_y + 28, int(w * 0.32) + 2, cliff_y + 34], fill=E["STONE_LIGHT"])
    # Heavy teak palisade stakes protecting sheer edge
    for px in range(int(w * 0.72), int(w * 0.98), 8):
        draw.rectangle([px, cliff_y + 24, px + 5, cliff_y + 48], fill=E["TEAK_BARK"])
        draw.rectangle([px + 1, cliff_y + 20, px + 4, cliff_y + 24], fill=E["TEAK_LIGHT"])  # Sharpened stake tip
        
    # High Saffron Flag (*Bhagwa Zenda*) fluttering in mountain gusts
    flag_x = int(w * 0.22)
    flag_y = cliff_y + 8
    # Timber staff
    draw.rectangle([flag_x, flag_y - 42, flag_x + 2, flag_y], fill=E["TEAK_BARK"])
    draw.rectangle([flag_x - 1, flag_y - 44, flag_x + 3, flag_y - 42], fill=E["GOLD_FINIAL"])
    # Swallowtail Maratha flag
    for fy in range(flag_y - 42, flag_y - 24):
        len_x = int(28 - (fy - (flag_y - 42)) * 0.8)
        draw.line([(flag_x + 3, fy), (flag_x + 3 + len_x, fy)], fill=E["SAFFRON_FLAG"])
        draw.rectangle([flag_x + 3, fy, flag_x + 8, fy], fill=E["SAFFRON_HI"])

    # High Altitude Teak & Pines clinging to rocky outcrops
    trees = [(70, cliff_y + 70, 0.9), (30, cliff_y + 110, 1.1), (420, cliff_y + 90, 1.05), (455, cliff_y + 160, 1.2)]
    for tx, ty, sc in trees:
        draw_sagwan_tree(img, draw, tx, ty, sc)
        
    return img

# ==============================================================================
# ENVIRONMENT 3: PRATAPGAD FORTIFIED APPROACH & BASTION GATE
# ==============================================================================
def render_env_fort_bastion(w=480, h=270):
    img = Image.new("RGBA", (w, h), E["GRASS_DARK"])
    draw = ImageDraw.Draw(img)
    
    # 1. Base Plateau Grass & Flagstones
    draw.rectangle([0, 0, w, h], fill=E["GRASS_BASE"])
    
    # Lower approach trail paved with worn flagstones
    for y in range(int(h * 0.45), h):
        for x in range(int(w * 0.28), int(w * 0.72)):
            if ((x // 12) + (y // 10)) % 2 == 0:
                draw.rectangle([x, y, x + 10, y + 8], fill=E["FLAGSTONE_BASE"])
            else:
                draw.rectangle([x, y, x + 10, y + 8], fill=E["FLAGSTONE_TRIM"])
                
    # 2. Monumental Semi-Circular Basalt Bastions (*Buruj*)
    # Left Bastion (Maha-Buruj)
    lb_cx, lb_cy = int(w * 0.20), int(h * 0.38)
    lb_r = 70
    draw.ellipse([lb_cx - lb_r, lb_cy - lb_r, lb_cx + lb_r, lb_cy + lb_r], fill=E["STONE_CLIFF"])
    draw.ellipse([lb_cx - lb_r + 4, lb_cy - lb_r + 4, lb_cx + lb_r - 4, lb_cy + lb_r - 4], fill=E["STONE_BASE"])
    draw.ellipse([lb_cx - lb_r + 8, lb_cy - lb_r + 8, lb_cx + lb_r - 8, lb_cy + lb_r - 8], fill=E["STONE_DARK"])
    
    # Right Bastion (Maha-Buruj)
    rb_cx, rb_cy = int(w * 0.80), int(h * 0.38)
    rb_r = 70
    draw.ellipse([rb_cx - rb_r, rb_cy - rb_r, rb_cx + rb_r, rb_cy + rb_r], fill=E["STONE_CLIFF"])
    draw.ellipse([rb_cx - rb_r + 4, rb_cy - rb_r + 4, rb_cx + rb_r - 4, rb_cy + rb_r - 4], fill=E["STONE_BASE"])
    draw.ellipse([rb_cx - rb_r + 8, rb_cy - rb_r + 8, rb_cx + rb_r - 8, rb_cy + rb_r - 8], fill=E["STONE_DARK"])

    # 3. Connecting Fortification Curtain Wall (*Tatbandi*) with Merlons & Machicolations
    wall_y = int(h * 0.22)
    wall_h = 44
    draw.rectangle([lb_cx + 20, wall_y, rb_cx - 20, wall_y + wall_h], fill=E["STONE_DARK"])
    draw.rectangle([lb_cx + 20, wall_y, rb_cx - 20, wall_y + 6], fill=E["STONE_LIGHT"])  # Wall top coping
    # Battlement Merlons (*Kanguras*)
    for mx in range(lb_cx + 24, rb_cx - 24, 16):
        draw.rectangle([mx, wall_y - 12, mx + 10, wall_y], fill=E["STONE_BASE"])
        draw.rectangle([mx, wall_y - 12, mx + 10, wall_y - 10], fill=E["STONE_LIGHT"])
        # Arrow slits (*Jharokhas*)
        draw.rectangle([mx + 4, wall_y - 8, mx + 6, wall_y - 3], fill=E["STONE_CLIFF"])

    # 4. Monumental Pointed Archway & Iron-Spiked Teak Gate (*Dilli Darwaja*)
    gate_cx = w // 2
    gate_w = 68
    gate_h = 72
    gx1 = gate_cx - gate_w // 2
    gx2 = gate_cx + gate_w // 2
    gy1 = wall_y + 10
    gy2 = gy1 + gate_h
    
    # Outer carved stone portal arch
    draw.rectangle([gx1 - 8, gy1 - 6, gx2 + 8, gy2], fill=E["STONE_LIGHT"])
    draw.rectangle([gx1 - 4, gy1 - 2, gx2 + 4, gy2], fill=E["STONE_DARK"])
    # Deep recess shadow
    draw.rectangle([gx1, gy1, gx2, gy2], fill=E["STONE_CLIFF"])
    # Heavy Teak Doors
    draw.rectangle([gx1 + 3, gy1 + 6, gx2 - 3, gy2], fill=E["TEAK_BARK"])
    draw.rectangle([gx1 + 5, gy1 + 8, gx2 - 5, gy2], fill=E["TEAK_LIGHT"])
    # Center seam
    draw.rectangle([gate_cx - 1, gy1 + 6, gate_cx + 1, gy2], fill=E["TEAK_BARK"])
    # Anti-Elephant Iron Spikes (*Kile*)
    for sy in range(gy1 + 18, gy2 - 6, 12):
        for sx in [gx1 + 14, gx1 + 26, gx2 - 26, gx2 - 14]:
            draw.rectangle([sx - 1, sy - 1, sx + 1, sy + 1], fill=E["IRON_REINFORCE"])
            draw.rectangle([sx, sy - 3, sx, sy - 1], fill=E["STONE_LIGHT"])

    # 5. Bastion Torches with Atmospheric Glow Gradients
    for tx, ty in [(lb_cx + 35, wall_y + 12), (rb_cx - 35, wall_y + 12)]:
        # Sconce iron bracket
        draw.rectangle([tx - 2, ty, tx + 2, ty + 8], fill=E["IRON_REINFORCE"])
        # Fire flame
        draw.rectangle([tx - 3, ty - 6, tx + 3, ty], fill=E["TORCH_FIRE"])
        draw.rectangle([tx - 1, ty - 8, tx + 1, ty - 4], fill=E["GOLD_FINIAL"])
        # Radial light glow
        draw.ellipse([tx - 20, ty - 20, tx + 20, ty + 20], fill=E["TORCH_GLOW"])

    # 6. Saffron Bhagwa Zenda Banners atop Left and Right Bastions
    for bx, by in [(lb_cx - 20, lb_cy - 45), (rb_cx + 20, rb_cy - 45)]:
        draw.rectangle([bx, by - 40, bx + 2, by], fill=E["TEAK_BARK"])
        draw.rectangle([bx - 1, by - 42, bx + 3, by - 40], fill=E["GOLD_FINIAL"])
        for fy in range(by - 40, by - 22):
            len_x = int(24 - (fy - (by - 40)) * 0.7)
            draw.line([(bx + 3, fy), (bx + 3 + len_x, fy)], fill=E["SAFFRON_FLAG"])
            draw.rectangle([bx + 3, fy, bx + 7, fy], fill=E["SAFFRON_HI"])

    # Flanking Sagwan Trees framing the fortified gatehouse
    draw_sagwan_tree(img, draw, 45, int(h * 0.75), 1.2)
    draw_sagwan_tree(img, draw, w - 45, int(h * 0.75), 1.2)
    
    return img

def build_c1_environment_previews():
    out_dir = "ChroniclesOfSwarajya_Art/07_Previews_OptionB"
    os.makedirs(out_dir, exist_ok=True)
    
    print("🌲 Rendering Environment 1: Dense Sahyadri Teak Forest & River Crossing...")
    env1 = render_env_forest_river(480, 270)
    p1 = os.path.join(out_dir, "sahyadri_forest_river_crossing.png")
    env1.save(p1)
    print(f"  -> Generated: {p1} ({env1.size})")

    print("\n⛰️ Rendering Environment 2: Javali Mountain Pass & Basalt Escarpment...")
    env2 = render_env_mountain_pass(480, 270)
    p2 = os.path.join(out_dir, "javali_mountain_pass_overlook.png")
    env2.save(p2)
    print(f"  -> Generated: {p2} ({env2.size})")

    print("\n🏰 Rendering Environment 3: Pratapgad Fortified Approach & Bastion Gate...")
    env3 = render_env_fort_bastion(480, 270)
    p3 = os.path.join(out_dir, "pratapgad_fortified_bastion_gate.png")
    env3.save(p3)
    print(f"  -> Generated: {p3} ({env3.size})")

if __name__ == "__main__":
    build_c1_environment_previews()
