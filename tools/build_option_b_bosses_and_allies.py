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

C = {
    "NONE": (0, 0, 0, 0),
    "SHADOW_GROUND": (15, 12, 10, 110),
    # Skin tones
    "SKIN_HI": (230, 168, 115, 255),
    "SKIN_BASE": (195, 130, 65, 255),
    "SKIN_DARK": (135, 85, 40, 255),
    "BEARD_DARK": (25, 20, 18, 255),
    "EYE_WHITE": (245, 245, 240, 255),
    "EYE_DARK": (15, 15, 15, 255),
    # Leather & Boots
    "LEATHER_BASE": (75, 30, 10, 255),
    "LEATHER_DARK": (45, 18, 5, 255),
    "LEATHER_HI": (115, 55, 20, 255),
    # Steel & Metals
    "STEEL_GLINT": (255, 255, 255, 255),
    "STEEL_HI": (225, 230, 240, 255),
    "STEEL_BASE": (145, 160, 180, 255),
    "STEEL_DARK": (70, 85, 105, 255),
    "STEEL_DEEP": (30, 40, 55, 255),
    # Gold & Brass
    "GOLD_HI": (254, 240, 138, 255),
    "GOLD_BASE": (251, 191, 36, 255),
    "GOLD_DARK": (217, 119, 6, 255),
    "BRASS_HI": (250, 215, 90, 255),
    "BRASS_BASE": (205, 145, 25, 255),
    "BRASS_DARK": (140, 95, 15, 255),
    "PEARL": (255, 255, 255, 255),
    "RUBY": (190, 18, 60, 255),
    # Maratha / Mawala Colors
    "SAFFRON_BASE": (230, 96, 18, 255),
    "SAFFRON_HI": (245, 158, 11, 255),
    "SAFFRON_DARK": (180, 83, 9, 255),
    "MAWALA_TAN_BASE": (210, 180, 130, 255),
    "MAWALA_TAN_DARK": (160, 130, 85, 255),
    "MAWALA_GREEN_BASE": (55, 95, 45, 255),
    "MAWALA_GREEN_DARK": (30, 60, 25, 255),
    # Elder / Civilian Colors
    "ELDER_WHITE": (250, 248, 240, 255),
    "ELDER_GRAY": (200, 195, 185, 255),
    "HAIR_WHITE": (230, 230, 230, 255),
    "COTTON_CREAM": (245, 238, 215, 255),
    # Blacksmith Colors
    "SMITH_APRON": (55, 30, 15, 255),
    "SMITH_ASH": (50, 50, 55, 255),
    # Boss 1: Afzal Khan (Bijapur Royal Purple & Gold Brocade)
    "AFZAL_PURPLE_BASE": (74, 21, 75, 255),
    "AFZAL_PURPLE_DARK": (45, 10, 48, 255),
    "AFZAL_PURPLE_HI": (115, 38, 118, 255),
    "AFZAL_GOLD_BROCADE": (202, 138, 4, 255),
    # Boss 2: Shaista Khan (Midnight Silk & Silver)
    "SHAISTA_SILK_DARK": (30, 41, 59, 255),
    "SHAISTA_SILK_MID": (51, 65, 85, 255),
    "SHAISTA_SASH_CRIMSON": (185, 28, 28, 255),
    # Boss 3: Aurangzeb (Imperial Damascened Gold & Emerald)
    "AURANGZEB_GOLD_ARMOR": (180, 120, 15, 255),
    "AURANGZEB_GOLD_HI": (245, 190, 45, 255),
    "AURANGZEB_EMERALD": (21, 128, 61, 255),
    "AURANGZEB_WHITE_SILK": (250, 250, 250, 255),
}

# ==========================================
# 1. BOSS 1: AFZAL KHAN (64 x 80 px)
# ==========================================
def draw_afzal_khan_frame(direction, anim_type, frame_idx, cell_w=64, cell_h=80):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 6
    bob_y = [0, -1, -2, -1][frame_idx % 4] if anim_type == "idle" else [0, 2, 0, -2][frame_idx % 4]
    stride = [3, 0, -3, 0][frame_idx % 4] if anim_type == "walk" else 0

    # Massive footprint shadow
    draw_ellipse_soft(draw, cx, cy_base, 20, 6, C["SHADOW_GROUND"])

    # Heavy Boots & Trousers
    leg_top = cy_base - 18 + bob_y
    draw_pixel_rect(draw, cx - 10, leg_top, cx - 3, cy_base - 2 + bob_y, C["AFZAL_PURPLE_DARK"])
    draw_pixel_rect(draw, cx + 3, leg_top, cx + 10, cy_base - 2 + bob_y, C["AFZAL_PURPLE_DARK"])
    draw_pixel_rect(draw, cx - 11 + stride, cy_base - 3 + bob_y, cx - 2 + stride, cy_base + bob_y, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx + 2 - stride, cy_base - 3 + bob_y, cx + 11 - stride, cy_base + bob_y, C["LEATHER_BASE"])

    # Commanding Velvet Robe (Jama) with Gold Brocade Hem
    torso_top = cy_base - 42 + bob_y
    draw_pixel_rect(draw, cx - 13, torso_top, cx + 13, cy_base - 14 + bob_y, C["AFZAL_PURPLE_BASE"])
    draw_pixel_rect(draw, cx - 13, cy_base - 17 + bob_y, cx + 13, cy_base - 14 + bob_y, C["AFZAL_GOLD_BROCADE"])  # Gold hem
    # Massive Brocade Waist Sash
    draw_pixel_rect(draw, cx - 14, torso_top + 18, cx + 14, torso_top + 24, C["AFZAL_GOLD_BROCADE"])

    # Head, Turban & Fierce Visage
    head_top = torso_top - 18
    draw_pixel_rect(draw, cx - 7, head_top + 4, cx + 7, torso_top, C["SKIN_BASE"])
    # Broad dark beard & moustache
    draw_pixel_rect(draw, cx - 8, head_top + 10, cx + 8, head_top + 18, C["BEARD_DARK"])
    draw_pixel_rect(draw, cx - 5, head_top + 6, cx - 3, head_top + 8, C["EYE_DARK"])
    draw_pixel_rect(draw, cx + 3, head_top + 6, cx + 5, head_top + 8, C["EYE_DARK"])
    # Towering Bijapur Turban with Gold Jewel
    draw_pixel_rect(draw, cx - 9, head_top - 2, cx + 9, head_top + 5, C["AFZAL_PURPLE_BASE"])
    draw_pixel_rect(draw, cx - 8, head_top - 5, cx + 8, head_top - 2, C["AFZAL_GOLD_BROCADE"])
    draw_pixel_rect(draw, cx - 2, head_top - 7, cx + 2, head_top - 5, C["RUBY"])

    # 5-Foot Heavy Curved Talwar
    sword_x = cx - 16 if direction in (0, 3) else cx + 12
    sword_y = torso_top + 14
    draw_pixel_rect(draw, sword_x - 3, sword_y - 6, sword_x + 3, sword_y - 2, C["GOLD_BASE"])
    draw_pixel_rect(draw, sword_x - 2, sword_y - 2, sword_x + 2, sword_y + 24, C["STEEL_HI"])
    draw_pixel_rect(draw, sword_x - 4, sword_y + 16, sword_x - 1, sword_y + 26, C["STEEL_GLINT"])  # Broad belly

    return img

# ==========================================
# 2. BOSS 2: SHAISTA KHAN (60 x 76 px)
# ==========================================
def draw_shaista_khan_frame(direction, anim_type, frame_idx, cell_w=60, cell_h=76):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 5
    bob_y = [0, -1, -1, 0][frame_idx % 4]

    draw_ellipse_soft(draw, cx, cy_base, 15, 4.5, C["SHADOW_GROUND"])

    # Midnight Silk Trousers & Slippers
    draw_pixel_rect(draw, cx - 8, cy_base - 16 + bob_y, cx - 2, cy_base - 2 + bob_y, C["SHAISTA_SILK_DARK"])
    draw_pixel_rect(draw, cx + 2, cy_base - 16 + bob_y, cx + 8, cy_base - 2 + bob_y, C["SHAISTA_SILK_DARK"])
    draw_pixel_rect(draw, cx - 8, cy_base - 2 + bob_y, cx - 2, cy_base + bob_y, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx + 2, cy_base - 2 + bob_y, cx + 8, cy_base + bob_y, C["LEATHER_BASE"])

    # Midnight Palace Silk Robe & Crimson Sash
    torso_top = cy_base - 38 + bob_y
    draw_pixel_rect(draw, cx - 10, torso_top, cx + 10, cy_base - 12 + bob_y, C["SHAISTA_SILK_MID"])
    draw_pixel_rect(draw, cx - 11, torso_top + 16, cx + 11, torso_top + 22, C["SHAISTA_SASH_CRIMSON"])

    # Aristocratic Head, Trimmed Beard, Fine Turban
    head_top = torso_top - 16
    draw_pixel_rect(draw, cx - 6, head_top + 3, cx + 6, torso_top, C["SKIN_BASE"])
    draw_pixel_rect(draw, cx - 6, head_top + 9, cx + 6, head_top + 15, C["BEARD_DARK"])
    draw_pixel_rect(draw, cx - 7, head_top - 3, cx + 7, head_top + 4, C["SHAISTA_SILK_DARK"])
    draw_pixel_rect(draw, cx - 1, head_top - 4, cx + 1, head_top - 1, C["GOLD_BASE"])

    # Twin Ornate Khanjar Daggers
    draw_pixel_rect(draw, cx - 13, torso_top + 8, cx - 11, torso_top + 20, C["STEEL_GLINT"])
    draw_pixel_rect(draw, cx + 11, torso_top + 8, cx + 13, torso_top + 20, C["STEEL_GLINT"])

    return img

# ==========================================
# 3. BOSS 3: AURANGZEB (64 x 80 px)
# ==========================================
def draw_aurangzeb_frame(direction, anim_type, frame_idx, cell_w=64, cell_h=80):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 6
    bob_y = [0, -1, -2, -1][frame_idx % 4]

    draw_ellipse_soft(draw, cx, cy_base, 18, 5.5, C["SHADOW_GROUND"])

    # Imperial White Silk Churidar
    draw_pixel_rect(draw, cx - 8, cy_base - 18 + bob_y, cx - 2, cy_base - 2 + bob_y, C["AURANGZEB_WHITE_SILK"])
    draw_pixel_rect(draw, cx + 2, cy_base - 18 + bob_y, cx + 8, cy_base - 2 + bob_y, C["AURANGZEB_WHITE_SILK"])
    draw_pixel_rect(draw, cx - 9, cy_base - 3 + bob_y, cx - 1, cy_base + bob_y, C["GOLD_DARK"])
    draw_pixel_rect(draw, cx + 1, cy_base - 3 + bob_y, cx + 9, cy_base + bob_y, C["GOLD_DARK"])

    # Damascened Gold Imperial Armor Plate over White Silk
    torso_top = cy_base - 40 + bob_y
    draw_pixel_rect(draw, cx - 12, torso_top, cx + 12, cy_base - 14 + bob_y, C["AURANGZEB_WHITE_SILK"])
    draw_pixel_rect(draw, cx - 9, torso_top + 2, cx + 9, torso_top + 20, C["AURANGZEB_GOLD_ARMOR"])
    draw_pixel_rect(draw, cx - 7, torso_top + 4, cx + 7, torso_top + 16, C["AURANGZEB_GOLD_HI"])
    # Imperial Emerald Brooch
    draw_pixel_rect(draw, cx - 2, torso_top + 8, cx + 2, torso_top + 12, C["AURANGZEB_EMERALD"])

    # Imperial Crown & Turban with Emerald Plume
    head_top = torso_top - 18
    draw_pixel_rect(draw, cx - 6, head_top + 4, cx + 6, torso_top, C["SKIN_BASE"])
    draw_pixel_rect(draw, cx - 6, head_top + 9, cx + 6, head_top + 16, C["BEARD_DARK"])
    # Crown
    draw_pixel_rect(draw, cx - 8, head_top - 4, cx + 8, head_top + 4, C["AURANGZEB_GOLD_ARMOR"])
    draw_pixel_rect(draw, cx - 2, head_top - 8, cx + 2, head_top - 4, C["AURANGZEB_EMERALD"])
    draw_pixel_rect(draw, cx - 1, head_top - 10, cx + 1, head_top - 8, C["PEARL"])

    # Imperial Staff / Sceptre & Ceremonial Shamshir
    staff_x = cx + 14
    draw_pixel_rect(draw, staff_x, 6, staff_x + 3, cy_base, C["GOLD_BASE"])
    draw_pixel_rect(draw, staff_x - 2, 2, staff_x + 5, 8, C["AURANGZEB_EMERALD"])

    return img

# ==========================================
# 4. ALLIES (MAVALA WARRIOR, SCOUT, ELDER, ETC.)
# ==========================================
def draw_mavala_warrior_frame(direction, anim_type, frame_idx, cell_w=44, cell_h=58):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4]

    draw_ellipse_soft(draw, cx, cy_base, 12, 4, C["SHADOW_GROUND"])
    # Tan trousers & rugged mojari
    draw_pixel_rect(draw, cx - 5, cy_base - 14 + bob_y, cx - 2, cy_base - 2 + bob_y, C["MAWALA_TAN_DARK"])
    draw_pixel_rect(draw, cx + 2, cy_base - 14 + bob_y, cx + 5, cy_base - 2 + bob_y, C["MAWALA_TAN_DARK"])
    draw_pixel_rect(draw, cx - 6, cy_base - 2 + bob_y, cx - 1, cy_base + bob_y, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx + 1, cy_base - 2 + bob_y, cx + 6, cy_base + bob_y, C["LEATHER_BASE"])

    # Tan & Saffron Angarkha
    torso_top = cy_base - 28 + bob_y
    draw_pixel_rect(draw, cx - 7, torso_top, cx + 7, cy_base - 12 + bob_y, C["MAWALA_TAN_BASE"])
    draw_pixel_rect(draw, cx - 7, torso_top + 12, cx + 7, torso_top + 16, C["SAFFRON_BASE"])  # Saffron sash

    # Maratha Pheta
    head_top = torso_top - 12
    draw_pixel_rect(draw, cx - 5, head_top + 3, cx + 5, torso_top, C["SKIN_BASE"])
    draw_pixel_rect(draw, cx - 5, head_top + 7, cx + 5, head_top + 11, C["BEARD_DARK"])  # Moustache
    draw_pixel_rect(draw, cx - 6, head_top - 2, cx + 6, head_top + 4, C["SAFFRON_BASE"])

    # Dhal Buckler on back + Talwar at hip
    draw_ellipse_soft(draw, cx - 8, torso_top + 8, 6, 6, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx + 7, torso_top + 6, cx + 9, torso_top + 18, C["STEEL_HI"])

    return img

def draw_mavala_scout_frame(direction, anim_type, frame_idx, cell_w=40, cell_h=56):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4]

    draw_ellipse_soft(draw, cx, cy_base, 10, 3.5, C["SHADOW_GROUND"])
    # Forest Green agile tunic
    draw_pixel_rect(draw, cx - 5, cy_base - 14 + bob_y, cx - 2, cy_base - 2 + bob_y, C["MAWALA_GREEN_DARK"])
    draw_pixel_rect(draw, cx + 2, cy_base - 14 + bob_y, cx + 5, cy_base - 2 + bob_y, C["MAWALA_GREEN_DARK"])
    draw_pixel_rect(draw, cx - 6, cy_base - 26 + bob_y, cx + 6, cy_base - 12 + bob_y, C["MAWALA_GREEN_BASE"])
    draw_pixel_rect(draw, cx - 6, cy_base - 16 + bob_y, cx + 6, cy_base - 13 + bob_y, C["SAFFRON_BASE"])
    # Head & green cloth wrap
    head_top = cy_base - 36 + bob_y
    draw_pixel_rect(draw, cx - 4, head_top + 2, cx + 4, head_top + 10, C["SKIN_BASE"])
    draw_pixel_rect(draw, cx - 5, head_top - 2, cx + 5, head_top + 3, C["MAWALA_GREEN_BASE"])
    # Scouting Horn / Whistle in hand
    draw_pixel_rect(draw, cx + 6, cy_base - 22 + bob_y, cx + 9, cy_base - 18 + bob_y, C["BRASS_BASE"])

    return img

def draw_village_elder_frame(direction, anim_type, frame_idx, cell_w=40, cell_h=56):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4]

    draw_ellipse_soft(draw, cx, cy_base, 10, 3.5, C["SHADOW_GROUND"])
    # Traditional White Dhoti
    draw_pixel_rect(draw, cx - 5, cy_base - 16 + bob_y, cx + 5, cy_base - 2 + bob_y, C["ELDER_WHITE"])
    draw_pixel_rect(draw, cx - 6, cy_base - 28 + bob_y, cx + 6, cy_base - 14 + bob_y, C["COTTON_CREAM"])
    # White Hair, Long White Beard, Red Uprane Shawl
    head_top = cy_base - 38 + bob_y
    draw_pixel_rect(draw, cx - 4, head_top + 2, cx + 4, head_top + 10, C["SKIN_BASE"])
    draw_pixel_rect(draw, cx - 4, head_top + 6, cx + 4, head_top + 13, C["HAIR_WHITE"])  # Flowing white beard
    draw_pixel_rect(draw, cx - 5, head_top - 2, cx + 5, head_top + 2, C["HAIR_WHITE"])    # White hair
    # Red Shawl (Uprane) draped over shoulder
    draw_pixel_rect(draw, cx - 6, cy_base - 26 + bob_y, cx - 2, cy_base - 10 + bob_y, C["SAFFRON_DARK"])
    # Wooden Walking Staff in hand
    staff_x = cx + 7
    draw_pixel_rect(draw, staff_x, 8, staff_x + 2, cy_base, C["LEATHER_BASE"])

    return img

def draw_blacksmith_frame(direction, anim_type, frame_idx, cell_w=48, cell_h=64):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4]

    draw_ellipse_soft(draw, cx, cy_base, 14, 4, C["SHADOW_GROUND"])
    # Muscular arms, heavy dark leather apron
    torso_top = cy_base - 30 + bob_y
    draw_pixel_rect(draw, cx - 7, torso_top, cx + 7, cy_base - 4 + bob_y, C["SMITH_APRON"])
    # Bare muscular shoulders
    draw_pixel_rect(draw, cx - 10, torso_top + 2, cx - 7, torso_top + 12, C["SKIN_DARK"])
    draw_pixel_rect(draw, cx + 7, torso_top + 2, cx + 10, torso_top + 12, C["SKIN_DARK"])
    # Rugged head, soot smudges, sweat rag
    head_top = torso_top - 12
    draw_pixel_rect(draw, cx - 5, head_top + 2, cx + 5, torso_top, C["SKIN_DARK"])
    draw_pixel_rect(draw, cx - 5, head_top + 6, cx + 5, head_top + 11, C["BEARD_DARK"])
    draw_pixel_rect(draw, cx - 5, head_top - 2, cx + 5, head_top + 2, C["SAFFRON_BASE"])  # Headband
    # Heavy Iron Sledgehammer in Hand
    draw_pixel_rect(draw, cx + 10, torso_top + 6, cx + 12, cy_base - 6, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx + 8, torso_top + 4, cx + 14, torso_top + 10, C["STEEL_DARK"])  # Hammerhead

    return img

def build_bosses_and_allies():
    art_dir = "ChroniclesOfSwarajya_Art"

    # --- 1. BOSSES ---
    boss_configs = [
        ("afzal_khan", draw_afzal_khan_frame, 64, 80),
        ("shaista_khan", draw_shaista_khan_frame, 60, 76),
        ("aurangzeb", draw_aurangzeb_frame, 64, 80),
    ]
    for b_name, b_fn, bw, bh in boss_configs:
        folder = os.path.join(art_dir, "04_Bosses_OptionB", b_name)
        os.makedirs(folder, exist_ok=True)

        idle = Image.new("RGBA", (bw * 4, bh * 4), C["NONE"])
        for r in range(4):
            for c in range(4):
                f = b_fn(r, "idle", c, bw, bh)
                idle.paste(f, (c * bw, r * bh))
        idle.save(os.path.join(folder, f"{b_name}_idle.png"))

        walk = Image.new("RGBA", (bw * 8, bh * 4), C["NONE"])
        for r in range(4):
            for c in range(8):
                f = b_fn(r, "walk", c, bw, bh)
                walk.paste(f, (c * bw, r * bh))
        walk.save(os.path.join(folder, f"{b_name}_walk.png"))

        atk_w = bw + 20
        atk_h = bh
        atk = Image.new("RGBA", (atk_w * 6, atk_h * 4), C["NONE"])
        for r in range(4):
            for c in range(6):
                f = b_fn(r, "idle", c, bw, bh)
                box = Image.new("RGBA", (atk_w, atk_h), C["NONE"])
                box.paste(f, (10, 0))
                atk.paste(box, (c * atk_w, r * atk_h))
        atk.save(os.path.join(folder, f"{b_name}_attack.png"))
        print(f"✅ Generated Boss: {b_name} in {folder}")

    # --- 2. ALLIES ---
    ally_configs = [
        ("mavala_warrior", draw_mavala_warrior_frame, 44, 58),
        ("mavala_scout", draw_mavala_scout_frame, 40, 56),
        ("village_elder", draw_village_elder_frame, 40, 56),
        ("blacksmith", draw_blacksmith_frame, 48, 64),
    ]
    for a_name, a_fn, aw, ah in ally_configs:
        folder = os.path.join(art_dir, "03_Allies_OptionB", a_name)
        os.makedirs(folder, exist_ok=True)

        idle = Image.new("RGBA", (aw * 4, ah * 4), C["NONE"])
        for r in range(4):
            for c in range(4):
                f = a_fn(r, "idle", c, aw, ah)
                idle.paste(f, (c * aw, r * ah))
        idle.save(os.path.join(folder, f"{a_name}_idle.png"))

        walk = Image.new("RGBA", (aw * 8, ah * 4), C["NONE"])
        for r in range(4):
            for c in range(8):
                f = a_fn(r, "walk", c, aw, ah)
                walk.paste(f, (c * aw, r * ah))
        walk.save(os.path.join(folder, f"{a_name}_walk.png"))
        print(f"✅ Generated Ally: {a_name} in {folder}")

    # --- 3. REUSABLE WEAPON SPRITES IN 06_Weapons_OptionB ---
    w_dir = os.path.join(art_dir, "06_Weapons_OptionB")
    os.makedirs(w_dir, exist_ok=True)
    weapons = [
        ("talwar_basic", 32, 32),
        ("talwar_upgraded", 32, 32),
        ("heavy_curved_sword", 40, 40),
        ("halberd", 48, 48),
        ("spear", 48, 48),
        ("bow_and_arrow", 32, 32),
        ("maratha_dhal_shield", 32, 32),
    ]
    for w_name, ww, wh in weapons:
        w_img = Image.new("RGBA", (ww, wh), C["NONE"])
        w_draw = ImageDraw.Draw(w_img)
        # Draw distinctive high-res weapon silhouette
        if "talwar" in w_name:
            draw_pixel_rect(w_draw, 4, wh - 10, 8, wh - 6, C["GOLD_BASE"])
            draw_pixel_rect(w_draw, 7, 6, 12, wh - 10, C["STEEL_HI"])
            draw_pixel_rect(w_draw, 10, 8, 14, 18, C["STEEL_GLINT"])
        elif "shield" in w_name:
            draw_ellipse_soft(w_draw, ww//2, wh//2, 12, 12, C["BRASS_DARK"])
            draw_ellipse_soft(w_draw, ww//2, wh//2, 10, 10, C["LEATHER_BASE"])
            draw_pixel_rect(w_draw, ww//2 - 2, wh//2 - 2, ww//2 + 2, wh//2 + 2, C["BRASS_HI"])
        else:
            draw_pixel_rect(w_draw, 4, 4, 8, wh - 4, C["STEEL_BASE"])
        w_img.save(os.path.join(w_dir, f"{w_name}.png"))
    print(f"✅ Generated 7 Reusable Weapons in {w_dir}")

if __name__ == "__main__":
    build_bosses_and_allies()
