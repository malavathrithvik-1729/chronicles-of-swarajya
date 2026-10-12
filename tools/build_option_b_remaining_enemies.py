import os
import math
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw

def draw_pixel_rect(draw, x1, y1, x2, y2, color):
    rx1, rx2 = round(min(x1, x2)), round(max(x1, x2))
    ry1, ry2 = round(min(y1, y2)), round(max(y1, y2))
    draw.rectangle([rx1, ry1, rx2, ry2], fill=color)

def draw_ellipse_soft(draw, cx, cy, rx, ry, color):
    draw.ellipse([round(cx - rx), round(cy - ry), round(cx + rx), round(cy + ry)], fill=color)

# Master Palette Tokens
C = {
    "NONE": (0, 0, 0, 0),
    "OUTLINE": (26, 20, 18, 255),
    "SHADOW_GROUND": (15, 12, 10, 110),
    # Skin Ramps
    "SKIN_HI": (235, 178, 128, 255),
    "SKIN_BASE": (198, 134, 66, 255),
    "SKIN_SHADOW": (141, 91, 45, 255),
    "SKIN_DEEP": (95, 58, 28, 255),
    "HAIR_BASE": (28, 25, 23, 255),
    "EYE_WHITE": (250, 245, 240, 255),
    "EYE_DARK": (15, 15, 15, 255),
    # Leathers
    "LEATHER_HI": (130, 68, 28, 255),
    "LEATHER_BASE": (78, 38, 14, 255),
    "LEATHER_DARK": (48, 22, 8, 255),
    # Steels
    "STEEL_GLINT": (255, 255, 255, 255),
    "STEEL_HI": (230, 236, 245, 255),
    "STEEL_BASE": (160, 175, 195, 255),
    "STEEL_SHADOW": (95, 110, 130, 255),
    "STEEL_DARK": (50, 62, 78, 255),
    "MAIL_BASE": (120, 132, 148, 255),
    "MAIL_DARK": (70, 80, 95, 255),
    # Brass & Gold
    "BRASS_HI": (250, 215, 90, 255),
    "BRASS_BASE": (205, 150, 30, 255),
    "BRASS_DARK": (110, 75, 15, 255),
    # Archer Khaki & Camo
    "ARCHER_KHAKI_HI": (165, 175, 125, 255),
    "ARCHER_KHAKI_BASE": (115, 125, 80, 255),
    "ARCHER_KHAKI_SHADOW": (75, 85, 50, 255),
    "WOOD_BOW": (125, 75, 30, 255),
    "FLETCHING_WHITE": (245, 245, 250, 255),
    # Charging Soldier Heavy Armour & Crimson
    "CHARGE_STEEL_HI": (175, 185, 205, 255),
    "CHARGE_STEEL_BASE": (110, 120, 140, 255),
    "CHARGE_STEEL_SHADOW": (65, 72, 88, 255),
    "CHARGE_SASH": (195, 35, 35, 255),
    # Elite Halberdier Imperial Purple
    "PURPLE_HI": (185, 95, 245, 255),
    "PURPLE_BASE": (125, 45, 185, 255),
    "PURPLE_SHADOW": (75, 20, 120, 255),
    # Spear Soldier Mustard / Saffron
    "SPEAR_MUSTARD_HI": (230, 185, 60, 255),
    "SPEAR_MUSTARD_BASE": (180, 135, 30, 255),
    "SPEAR_MUSTARD_SHADOW": (120, 85, 15, 255),
    "BAMBOO_SHAFT": (195, 155, 85, 255),
    # VFX
    "SLASH_CORE": (255, 255, 255, 250),
    "SLASH_EDGE": (255, 200, 100, 220),
}

# ==============================================================================
# 1. REFINED ARCHER (40 x 56 px cells)
# ==============================================================================
def draw_refined_archer_frame(direction, anim_type, frame_idx, cell_w=40, cell_h=56):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4] if anim_type == "idle" else [0, 1, 0, -1, 0, 1, 0, -1][frame_idx % 8]
    stride = [3, 2, 0, -2, -3, -2, 0, 2][frame_idx % 8] if anim_type == "walk" else 0

    draw_ellipse_soft(draw, cx, cy_base, 11, 3.5, C["SHADOW_GROUND"])
    
    # Boots & Trousers
    leg_top = cy_base - 14 + bob_y
    leg_bot = cy_base - 2 + bob_y
    draw_pixel_rect(draw, cx - 5, leg_top, cx - 2, leg_bot - 1, C["ARCHER_KHAKI_SHADOW"])
    draw_pixel_rect(draw, cx + 2, leg_top, cx + 5, leg_bot - 1, C["ARCHER_KHAKI_SHADOW"])
    draw_pixel_rect(draw, cx - 6 + stride, leg_bot, cx - 1 + stride, leg_bot + 2, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx + 1 - stride, leg_bot, cx + 6 - stride, leg_bot + 2, C["LEATHER_BASE"])

    # Khaki Tunic & Leather Waistbelt
    torso_top = cy_base - 28 + bob_y
    draw_pixel_rect(draw, cx - 6, torso_top, cx + 6, leg_top + 2, C["ARCHER_KHAKI_BASE"])
    draw_pixel_rect(draw, cx - 6, torso_top, cx - 4, leg_top + 2, C["ARCHER_KHAKI_SHADOW"])
    draw_pixel_rect(draw, cx - 6, torso_top + 10, cx + 6, torso_top + 13, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx - 1, torso_top + 10, cx + 1, torso_top + 13, C["BRASS_HI"])

    # Quiver Slung on Back
    draw_pixel_rect(draw, cx + 4, torso_top - 6, cx + 7, torso_top + 12, C["LEATHER_DARK"])
    draw_pixel_rect(draw, cx + 5, torso_top - 9, cx + 6, torso_top - 6, C["FLETCHING_WHITE"])
    draw_pixel_rect(draw, cx + 6, torso_top - 8, cx + 7, torso_top - 6, C["FLETCHING_WHITE"])

    # Head, Face & Camo Turban
    head_top = torso_top - 12
    draw_pixel_rect(draw, cx - 4, head_top + 3, cx + 4, torso_top, C["SKIN_BASE"])
    draw_pixel_rect(draw, cx - 5, head_top - 1, cx + 5, head_top + 4, C["ARCHER_KHAKI_HI"])
    draw_pixel_rect(draw, cx - 4, head_top + 3, cx + 4, head_top + 5, C["ARCHER_KHAKI_SHADOW"])
    if direction != 1:
        draw_pixel_rect(draw, cx - 3, head_top + 5, cx - 2, head_top + 6, C["EYE_DARK"])
        draw_pixel_rect(draw, cx + 2, head_top + 5, cx + 3, head_top + 6, C["EYE_DARK"])

    # Recurve Bow in Hand
    bow_x = cx - 8
    draw.arc([bow_x - 4, torso_top - 6, bow_x + 6, torso_top + 18], start=90, end=270, fill=C["WOOD_BOW"], width=2)
    draw.line([bow_x + 1, torso_top - 5, bow_x + 1, torso_top + 17], fill=C["STEEL_HI"])

    return img

# ==============================================================================
# 2. REFINED CHARGING SOLDIER (44 x 58 px cells)
# ==============================================================================
def draw_refined_charging_soldier_frame(direction, anim_type, frame_idx, cell_w=44, cell_h=58):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4] if anim_type == "idle" else [0, 1, 0, -1, 0, 1, 0, -1][frame_idx % 8]
    stride = [3, 2, 0, -2, -3, -2, 0, 2][frame_idx % 8] if anim_type in ("walk", "charge") else 0
    lean_x = 2 if anim_type == "charge" else 0

    draw_ellipse_soft(draw, cx + lean_x, cy_base, 14, 4.5, C["SHADOW_GROUND"])
    
    # Armoured Plate Greaves
    leg_top = cy_base - 16 + bob_y
    leg_bot = cy_base - 2 + bob_y
    draw_pixel_rect(draw, cx - 7 + lean_x, leg_top, cx - 2 + lean_x, leg_bot - 1, C["CHARGE_STEEL_SHADOW"])
    draw_pixel_rect(draw, cx + 2 + lean_x, leg_top, cx + 7 + lean_x, leg_bot - 1, C["CHARGE_STEEL_SHADOW"])
    draw_pixel_rect(draw, cx - 8 + stride + lean_x, leg_bot, cx - 2 + stride + lean_x, leg_bot + 2, C["STEEL_DARK"])
    draw_pixel_rect(draw, cx + 2 - stride + lean_x, leg_bot, cx + 8 - stride + lean_x, leg_bot + 2, C["STEEL_DARK"])

    # Heavy Solid Steel Cuirass (Chiseled Breastplate)
    torso_top = cy_base - 32 + bob_y
    draw_pixel_rect(draw, cx - 8 + lean_x, torso_top, cx + 8 + lean_x, leg_top + 2, C["CHARGE_STEEL_BASE"])
    draw_pixel_rect(draw, cx - 6 + lean_x, torso_top + 2, cx + 6 + lean_x, torso_top + 14, C["CHARGE_STEEL_HI"])
    draw_pixel_rect(draw, cx - 2 + lean_x, torso_top + 4, cx + 2 + lean_x, torso_top + 10, C["STEEL_GLINT"])
    # Crimson War Sash at Waist
    draw_pixel_rect(draw, cx - 8 + lean_x, torso_top + 14, cx + 8 + lean_x, torso_top + 18, C["CHARGE_SASH"])

    # Heavy Conical Visored Helmet
    head_top = torso_top - 14
    draw_pixel_rect(draw, cx - 6 + lean_x, head_top, cx + 6 + lean_x, torso_top, C["STEEL_BASE"])
    draw_pixel_rect(draw, cx - 2 + lean_x, head_top - 4, cx + 2 + lean_x, head_top, C["STEEL_HI"])
    draw_pixel_rect(draw, cx - 5 + lean_x, head_top + 5, cx + 5 + lean_x, head_top + 7, C["STEEL_DARK"])  # Eye slit

    # Massive 2-Handed Khanda Broadsword
    sw_x = cx + 8 + lean_x
    draw_pixel_rect(draw, sw_x, torso_top + 2, sw_x + 3, torso_top + 6, C["BRASS_HI"])
    draw_pixel_rect(draw, sw_x + 1, torso_top + 6, sw_x + 5, cy_base - 2, C["STEEL_HI"])
    draw_pixel_rect(draw, sw_x + 2, torso_top + 8, sw_x + 4, cy_base - 4, C["STEEL_GLINT"])

    return img

# ==============================================================================
# 3. REFINED ELITE HALBERDIER (48 x 64 px cells)
# ==============================================================================
def draw_refined_halberdier_frame(direction, anim_type, frame_idx, cell_w=48, cell_h=64):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4] if anim_type == "idle" else [0, 1, 0, -1, 0, 1, 0, -1][frame_idx % 8]
    stride = [3, 2, 0, -2, -3, -2, 0, 2][frame_idx % 8] if anim_type == "walk" else 0

    draw_ellipse_soft(draw, cx, cy_base, 15, 5, C["SHADOW_GROUND"])
    
    # Greaves & Armoured Boots
    leg_top = cy_base - 18 + bob_y
    leg_bot = cy_base - 2 + bob_y
    draw_pixel_rect(draw, cx - 7, leg_top, cx - 2, leg_bot - 1, C["STEEL_SHADOW"])
    draw_pixel_rect(draw, cx + 2, leg_top, cx + 7, leg_bot - 1, C["STEEL_SHADOW"])
    draw_pixel_rect(draw, cx - 8 + stride, leg_bot, cx - 2 + stride, leg_bot + 2, C["STEEL_DARK"])
    draw_pixel_rect(draw, cx + 2 - stride, leg_bot, cx + 8 - stride, leg_bot + 2, C["STEEL_DARK"])

    # Imperial Purple Robes with Polished Mirror Cuirass
    torso_top = cy_base - 36 + bob_y
    draw_pixel_rect(draw, cx - 9, torso_top, cx + 9, leg_top + 2, C["PURPLE_BASE"])
    draw_pixel_rect(draw, cx - 7, torso_top + 2, cx + 7, torso_top + 16, C["STEEL_HI"])
    draw_pixel_rect(draw, cx - 3, torso_top + 4, cx + 3, torso_top + 12, C["STEEL_GLINT"])
    draw_pixel_rect(draw, cx - 9, torso_top + 16, cx + 9, torso_top + 20, C["PURPLE_HI"])  # Sash

    # Steel Kulak Helmet with Imperial Purple Plume
    head_top = torso_top - 16
    draw_pixel_rect(draw, cx - 7, head_top, cx + 7, torso_top, C["STEEL_BASE"])
    draw_pixel_rect(draw, cx - 3, head_top - 8, cx + 3, head_top, C["PURPLE_HI"])  # High plume
    draw_pixel_rect(draw, cx - 5, head_top + 6, cx + 5, head_top + 8, C["EYE_DARK"])

    # 6-Foot Steel Halberd (Long Shaft + Crescent Blade + Pike Tip)
    hx = cx + 10
    draw_pixel_rect(draw, hx, 2, hx + 3, cy_base, C["WOOD_BOW"])
    draw_pixel_rect(draw, hx - 1, 0, hx + 4, 10, C["STEEL_GLINT"])  # Pike tip
    draw_pixel_rect(draw, hx + 3, 8, hx + 12, 18, C["STEEL_HI"])   # Axe blade
    draw_pixel_rect(draw, hx - 5, 10, hx, 15, C["STEEL_SHADOW"])   # Rear hook

    return img

# ==============================================================================
# 4. REFINED SPEAR SOLDIER (40 x 56 px cells)
# ==============================================================================
def draw_refined_spearman_frame(direction, anim_type, frame_idx, cell_w=40, cell_h=56):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4] if anim_type == "idle" else [0, 1, 0, -1, 0, 1, 0, -1][frame_idx % 8]
    stride = [3, 2, 0, -2, -3, -2, 0, 2][frame_idx % 8] if anim_type == "walk" else 0

    draw_ellipse_soft(draw, cx, cy_base, 11, 3.5, C["SHADOW_GROUND"])
    
    # Boots & Trousers
    leg_top = cy_base - 14 + bob_y
    leg_bot = cy_base - 2 + bob_y
    draw_pixel_rect(draw, cx - 5, leg_top, cx - 2, leg_bot - 1, C["SPEAR_MUSTARD_SHADOW"])
    draw_pixel_rect(draw, cx + 2, leg_top, cx + 5, leg_bot - 1, C["SPEAR_MUSTARD_SHADOW"])
    draw_pixel_rect(draw, cx - 6 + stride, leg_bot, cx - 1 + stride, leg_bot + 2, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx + 1 - stride, leg_bot, cx + 6 - stride, leg_bot + 2, C["LEATHER_BASE"])

    # Mustard Tunic & Belt
    torso_top = cy_base - 28 + bob_y
    draw_pixel_rect(draw, cx - 6, torso_top, cx + 6, leg_top + 2, C["SPEAR_MUSTARD_BASE"])
    draw_pixel_rect(draw, cx - 5, torso_top + 2, cx + 5, torso_top + 10, C["SPEAR_MUSTARD_HI"])
    draw_pixel_rect(draw, cx - 6, torso_top + 10, cx + 6, torso_top + 13, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx - 1, torso_top + 10, cx + 1, torso_top + 13, C["BRASS_HI"])

    # Helmet with Mail Coif
    head_top = torso_top - 12
    draw_pixel_rect(draw, cx - 5, head_top, cx + 5, torso_top, C["STEEL_BASE"])
    draw_pixel_rect(draw, cx - 2, head_top - 3, cx + 2, head_top, C["BRASS_HI"])
    draw_pixel_rect(draw, cx - 3, head_top + 5, cx - 2, head_top + 6, C["EYE_DARK"])
    draw_pixel_rect(draw, cx + 2, head_top + 5, cx + 3, head_top + 6, C["EYE_DARK"])

    # Bamboo Long Spear (Bhala)
    sp_x = cx + 7
    draw_pixel_rect(draw, sp_x, 4, sp_x + 2, cy_base, C["BAMBOO_SHAFT"])
    draw_pixel_rect(draw, sp_x - 1, 2, sp_x + 3, 10, C["STEEL_GLINT"])  # Steel leaf point

    return img

def build_all_remaining_refined_enemies():
    art_dir = "ChroniclesOfSwarajya_Art/02_Enemies_OptionB"
    enemies = [
        ("archer", 40, 56, draw_refined_archer_frame),
        ("charging_soldier", 44, 58, draw_refined_charging_soldier_frame),
        ("elite_halberdier", 48, 64, draw_refined_halberdier_frame),
        ("spear_soldier", 40, 56, draw_refined_spearman_frame)
    ]
    
    for ename, ew, eh, func in enemies:
        edir = os.path.join(art_dir, ename)
        os.makedirs(edir, exist_ok=True)
        print(f"🎨 Rendering Refined Option B {ename}...")
        
        # Idle (4 cols x 4 rows)
        idle_img = Image.new("RGBA", (ew * 4, eh * 4), (0, 0, 0, 0))
        for r in range(4):
            for c in range(4):
                f = func(r, "idle", c, ew, eh)
                idle_img.paste(f, (c * ew, r * eh), f)
        idle_img.save(os.path.join(edir, f"{ename}_idle.png"))

        # Walk (8 cols x 4 rows)
        walk_img = Image.new("RGBA", (ew * 8, eh * 4), (0, 0, 0, 0))
        for r in range(4):
            for c in range(8):
                f = func(r, "walk", c, ew, eh)
                walk_img.paste(f, (c * ew, r * eh), f)
        walk_img.save(os.path.join(edir, f"{ename}_walk.png"))

        # Attack (6 cols x 4 rows)
        atk_w = ew + 16
        atk_img = Image.new("RGBA", (atk_w * 6, eh * 4), (0, 0, 0, 0))
        for r in range(4):
            for c in range(6):
                f = func(r, "attack", c, ew, eh)
                atk_frame = Image.new("RGBA", (atk_w, eh), (0, 0, 0, 0))
                atk_frame.paste(f, (8, 0), f)
                atk_img.paste(atk_frame, (c * atk_w, r * eh), atk_frame)
        atk_img.save(os.path.join(edir, f"{ename}_attack.png"))
        print(f"  -> Generated {ename} idle, walk, attack.")

if __name__ == "__main__":
    build_all_remaining_refined_enemies()
