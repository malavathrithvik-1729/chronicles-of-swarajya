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
    "OUTLINE": (26, 20, 18, 255),
    "SHADOW_GROUND": (15, 12, 10, 110),
    # Skin
    "SKIN_HI": (230, 168, 115, 255),
    "SKIN_BASE": (195, 130, 65, 255),
    "SKIN_DARK": (135, 85, 40, 255),
    "BEARD_DARK": (30, 25, 20, 255),
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
    # Brass & Gold
    "BRASS_HI": (250, 215, 90, 255),
    "BRASS_BASE": (205, 145, 25, 255),
    "BRASS_DARK": (140, 95, 15, 255),
    # Faction Colors - Swordsman (Deccan Green)
    "SWORD_GREEN_HI": (45, 130, 75, 255),
    "SWORD_GREEN_BASE": (25, 85, 45, 255),
    "SWORD_GREEN_DARK": (15, 55, 30, 255),
    "SWORD_TURBAN_OCHRE": (190, 130, 25, 255),
    # Faction Colors - Shield Guard (Heavy Russet / Iron)
    "SHIELD_RED_HI": (185, 50, 50, 255),
    "SHIELD_RED_BASE": (130, 25, 25, 255),
    "SHIELD_RED_DARK": (85, 15, 15, 255),
    # Faction Colors - Archer (Earth Khaki / Quiver)
    "ARCHER_KHAKI_HI": (135, 145, 95, 255),
    "ARCHER_KHAKI_BASE": (95, 105, 65, 255),
    "ARCHER_KHAKI_DARK": (60, 70, 40, 255),
    "WOOD_BOW": (115, 65, 25, 255),
    "FLETCHING_WHITE": (240, 240, 245, 255),
    # Faction Colors - Charging Soldier (Plate Cuirass)
    "CHARGE_CUIRASS_HI": (120, 130, 145, 255),
    "CHARGE_CUIRASS_BASE": (75, 85, 100, 255),
    "CHARGE_CUIRASS_DARK": (45, 52, 65, 255),
    "CHARGE_SASH": (180, 40, 20, 255),
    # Faction Colors - Elite Halberdier (Imperial Purple & Polished Steel)
    "PURPLE_HI": (160, 70, 225, 255),
    "PURPLE_BASE": (105, 30, 160, 255),
    "PURPLE_DARK": (65, 15, 105, 255),
    # Faction Colors - Spear Soldier (Mustard / Bamboo)
    "SPEAR_TUNIC_HI": (210, 160, 45, 255),
    "SPEAR_TUNIC_BASE": (160, 115, 25, 255),
    "SPEAR_TUNIC_DARK": (110, 75, 15, 255),
    "BAMBOO_SHAFT": (180, 145, 75, 255),
    # Slash VFX
    "SLASH_WHITE": (255, 255, 255, 240),
    "SLASH_ORANGE": (245, 130, 20, 190),
    "SLASH_FADE": (220, 70, 10, 90),
}

# ==========================================
# 1. BASIC SWORDSMAN (40 x 56 px cells)
# ==========================================
def draw_swordsman_frame(direction, anim_type, frame_idx, cell_w=40, cell_h=56):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4

    bob_y = 0
    stride = 0
    arm_swing = 0
    if anim_type == "idle":
        bob_y = [0, -1, -1, 0][frame_idx % 4]
    elif anim_type in ("walk", "run"):
        bobs = [0, 1, 0, -1, 0, 1, 0, -1]
        bob_y = bobs[frame_idx % 8]
        strides = [3, 2, 0, -2, -3, -2, 0, 2]
        stride = strides[frame_idx % 8]
        arm_swing = -stride

    # Shadow
    draw_ellipse_soft(draw, cx, cy_base, 11, 3.5, C["SHADOW_GROUND"])

    # Feet & Legs
    leg_top = cy_base - 14 + bob_y
    leg_bot = cy_base - 2 + bob_y
    if direction == 0:  # South
        draw_pixel_rect(draw, cx - 5, leg_top, cx - 2, leg_bot - 1, C["SWORD_GREEN_DARK"])
        draw_pixel_rect(draw, cx + 2, leg_top, cx + 5, leg_bot - 1, C["SWORD_GREEN_DARK"])
        draw_pixel_rect(draw, cx - 6 + stride, leg_bot, cx - 2 + stride, leg_bot + 1, C["LEATHER_BASE"])
        draw_pixel_rect(draw, cx + 2 - stride, leg_bot, cx + 6 - stride, leg_bot + 1, C["LEATHER_BASE"])
    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 5, leg_top, cx - 2, leg_bot - 1, C["SWORD_GREEN_DARK"])
        draw_pixel_rect(draw, cx + 2, leg_top, cx + 5, leg_bot - 1, C["SWORD_GREEN_DARK"])
        draw_pixel_rect(draw, cx - 6 - stride, leg_bot, cx - 2 - stride, leg_bot + 1, C["LEATHER_DARK"])
        draw_pixel_rect(draw, cx + 2 + stride, leg_bot, cx + 6 + stride, leg_bot + 1, C["LEATHER_DARK"])
    else:  # East / West
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 4, leg_top, cx + 4, leg_bot - 1, C["SWORD_GREEN_DARK"])
        draw_pixel_rect(draw, cx - 3 + stride*sign, leg_bot, cx + 3 + stride*sign, leg_bot + 1, C["LEATHER_BASE"])

    # Tunic & Belt
    tunic_top = cy_base - 28 + bob_y
    tunic_bot = leg_top + 2
    draw_pixel_rect(draw, cx - 6, tunic_top, cx + 6, tunic_bot, C["SWORD_GREEN_BASE"])
    draw_pixel_rect(draw, cx - 6, tunic_bot - 4, cx + 6, tunic_bot, C["SWORD_GREEN_DARK"])
    # Leather belt with brass buckle
    draw_pixel_rect(draw, cx - 6, tunic_top + 9, cx + 6, tunic_top + 11, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx - 1, tunic_top + 9, cx + 1, tunic_top + 11, C["BRASS_HI"])

    # Head, Helmet & Face
    head_top = tunic_top - 12
    head_bot = tunic_top
    if direction == 0:  # South
        draw_pixel_rect(draw, cx - 4, head_top + 3, cx + 4, head_bot, C["SKIN_BASE"])
        # Eyes & Moustache
        draw_pixel_rect(draw, cx - 3, head_top + 5, cx - 2, head_top + 6, C["EYE_DARK"])
        draw_pixel_rect(draw, cx + 2, head_top + 5, cx + 3, head_top + 6, C["EYE_DARK"])
        draw_pixel_rect(draw, cx - 4, head_top + 8, cx + 4, head_top + 9, C["BEARD_DARK"])
        # Conical Steel Helmet with brass crest
        draw_pixel_rect(draw, cx - 5, head_top, cx + 5, head_top + 4, C["STEEL_BASE"])
        draw_pixel_rect(draw, cx - 2, head_top - 2, cx + 2, head_top, C["STEEL_HI"])
        draw_pixel_rect(draw, cx - 1, head_top - 4, cx + 1, head_top - 2, C["BRASS_HI"])
    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 5, head_top, cx + 5, head_bot, C["STEEL_DARK"])
        draw_pixel_rect(draw, cx - 2, head_top - 2, cx + 2, head_top, C["STEEL_BASE"])
    else:  # East/West
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 4, head_top + 3, cx + 4, head_bot, C["SKIN_BASE"])
        draw_pixel_rect(draw, cx + 2*sign, head_top + 5, cx + 4*sign, head_top + 6, C["EYE_DARK"])
        draw_pixel_rect(draw, cx - 4, head_top, cx + 4, head_top + 4, C["STEEL_BASE"])
        draw_pixel_rect(draw, cx - 1, head_top - 3, cx + 1, head_top, C["BRASS_HI"])

    # Arms & Curved Sword (Sheathed or Ready)
    arm_top = tunic_top + 2
    if direction == 0:  # South
        draw_pixel_rect(draw, cx - 8, arm_top, cx - 6, arm_top + 8 + arm_swing, C["SWORD_GREEN_BASE"])
        draw_pixel_rect(draw, cx + 6, arm_top, cx + 8, arm_top + 8 - arm_swing, C["SWORD_GREEN_BASE"])
        # Sword at left hip
        draw_pixel_rect(draw, cx - 9, arm_top + 5, cx - 7, arm_top + 8, C["BRASS_BASE"])
        draw_pixel_rect(draw, cx - 10, arm_top + 8, cx - 8, arm_top + 18, C["STEEL_BASE"])
    elif direction in (2, 3):  # East / West
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx + 4*sign, arm_top + 3, cx + 7*sign, arm_top + 9, C["SWORD_GREEN_BASE"])
        draw_pixel_rect(draw, cx + 7*sign, arm_top + 7, cx + 9*sign, arm_top + 9, C["BRASS_BASE"])
        draw_pixel_rect(draw, cx + 8*sign, arm_top + 9, cx + 10*sign, arm_top + 18, C["STEEL_BASE"])

    return img

def draw_swordsman_attack_frame(direction, frame_idx, cell_w=56, cell_h=56):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    draw_ellipse_soft(draw, cx, cy_base, 13, 4, C["SHADOW_GROUND"])

    base = draw_swordsman_frame(direction, "idle", 0, 40, 56)
    shift_x = (3 if frame_idx in (2, 3) else 0) if direction == 2 else (-3 if frame_idx in (2, 3) else 0)
    img.paste(base, (8 + shift_x, 0), base)

    # Active Sword Slash
    hx = cx + shift_x
    hy = 26
    if frame_idx in (1, 2):  # Windup
        draw_pixel_rect(draw, hx - 8, hy - 10, hx - 4, hy - 8, C["BRASS_BASE"])
        draw_pixel_rect(draw, hx - 6, hy - 20, hx - 4, hy - 10, C["STEEL_HI"])
    elif frame_idx == 3:  # Strike & Arc
        draw_pixel_rect(draw, hx + 4, hy + 2, hx + 8, hy + 4, C["BRASS_BASE"])
        draw_pixel_rect(draw, hx + 8, hy + 2, hx + 22, hy + 5, C["STEEL_GLINT"])
        draw.arc([cx - 16, cy_base - 34, cx + 24, cy_base], start=280, end=90, fill=C["SLASH_WHITE"], width=2)
    elif frame_idx == 4:  # Recovery
        draw_pixel_rect(draw, hx + 2, hy + 4, hx + 6, hy + 6, C["BRASS_BASE"])
        draw_pixel_rect(draw, hx + 6, hy + 4, hx + 16, hy + 7, C["STEEL_BASE"])

    return img

# ==========================================
# 2. SHIELD GUARD (44 x 58 px cells)
# ==========================================
def draw_shield_guard_frame(direction, anim_type, frame_idx, cell_w=44, cell_h=58):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4] if anim_type == "idle" else [0, 1, 0, -1][frame_idx % 4]
    stride = [2, 0, -2, 0][frame_idx % 4] if anim_type == "walk" else 0

    draw_ellipse_soft(draw, cx, cy_base, 13, 4, C["SHADOW_GROUND"])

    # Heavy boots & trousers
    draw_pixel_rect(draw, cx - 6, cy_base - 12 + bob_y, cx - 2, cy_base - 2 + bob_y, C["SHIELD_RED_DARK"])
    draw_pixel_rect(draw, cx + 2, cy_base - 12 + bob_y, cx + 6, cy_base - 2 + bob_y, C["SHIELD_RED_DARK"])
    draw_pixel_rect(draw, cx - 7 + stride, cy_base - 2 + bob_y, cx - 1 + stride, cy_base + bob_y, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx + 1 - stride, cy_base - 2 + bob_y, cx + 7 - stride, cy_base + bob_y, C["LEATHER_BASE"])

    # Heavy Brigandine Torso
    torso_top = cy_base - 28 + bob_y
    draw_pixel_rect(draw, cx - 7, torso_top, cx + 7, cy_base - 10 + bob_y, C["SHIELD_RED_BASE"])
    # Brass studs on brigandine
    for bx in (-4, 0, 4):
        for by in (torso_top + 4, torso_top + 10, torso_top + 16):
            draw_pixel_rect(draw, cx + bx, by, cx + bx + 1, by + 1, C["BRASS_HI"])

    # Armoured Helmet with nose guard
    head_top = torso_top - 12
    draw_pixel_rect(draw, cx - 5, head_top, cx + 5, torso_top, C["STEEL_BASE"])
    draw_pixel_rect(draw, cx - 1, head_top + 2, cx + 1, head_top + 9, C["STEEL_HI"])  # Nasal bar
    draw_pixel_rect(draw, cx - 4, head_top + 4, cx - 2, head_top + 6, C["EYE_DARK"])
    draw_pixel_rect(draw, cx + 2, head_top + 4, cx + 4, head_top + 6, C["EYE_DARK"])

    # PROMINENT SHIELD: Large Oval Dhal Shield with Brass Bosses
    shield_x = cx - 10 if direction in (0, 3) else cx + 2
    shield_y = torso_top + 2
    draw_ellipse_soft(draw, shield_x + 6, shield_y + 10, 8, 12, C["BRASS_DARK"])
    draw_ellipse_soft(draw, shield_x + 6, shield_y + 10, 7, 11, C["LEATHER_BASE"])
    # 4 Brass boss studs
    draw_pixel_rect(draw, shield_x + 4, shield_y + 6, shield_x + 6, shield_y + 8, C["BRASS_HI"])
    draw_pixel_rect(draw, shield_x + 7, shield_y + 6, shield_x + 9, shield_y + 8, C["BRASS_HI"])
    draw_pixel_rect(draw, shield_x + 4, shield_y + 12, shield_x + 6, shield_y + 14, C["BRASS_HI"])
    draw_pixel_rect(draw, shield_x + 7, shield_y + 12, shield_x + 9, shield_y + 14, C["BRASS_HI"])
    # Center Crescent Boss
    draw_pixel_rect(draw, shield_x + 5, shield_y + 9, shield_x + 7, shield_y + 11, C["BRASS_HI"])

    # Weapon in other hand
    draw_pixel_rect(draw, cx + 8, torso_top + 6, cx + 10, torso_top + 16, C["STEEL_HI"])

    return img

# ==========================================
# 3. RANGED ARCHER (40 x 56 px cells)
# ==========================================
def draw_archer_frame(direction, anim_type, frame_idx, cell_w=40, cell_h=56):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4]

    draw_ellipse_soft(draw, cx, cy_base, 10, 3.5, C["SHADOW_GROUND"])

    # Khaki Tunic & Boots
    draw_pixel_rect(draw, cx - 5, cy_base - 14 + bob_y, cx - 2, cy_base - 2 + bob_y, C["ARCHER_KHAKI_DARK"])
    draw_pixel_rect(draw, cx + 2, cy_base - 14 + bob_y, cx + 5, cy_base - 2 + bob_y, C["ARCHER_KHAKI_DARK"])
    draw_pixel_rect(draw, cx - 6, cy_base - 2 + bob_y, cx - 2, cy_base + bob_y, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx + 2, cy_base - 2 + bob_y, cx + 6, cy_base + bob_y, C["LEATHER_BASE"])

    # Tunic
    torso_top = cy_base - 26 + bob_y
    draw_pixel_rect(draw, cx - 6, torso_top, cx + 6, cy_base - 12 + bob_y, C["ARCHER_KHAKI_BASE"])

    # Quiver on Back with Fletchings
    draw_pixel_rect(draw, cx + 4, torso_top - 6, cx + 7, torso_top + 10, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx + 5, torso_top - 9, cx + 6, torso_top - 6, C["FLETCHING_WHITE"])
    draw_pixel_rect(draw, cx + 6, torso_top - 8, cx + 7, torso_top - 6, C["FLETCHING_WHITE"])

    # Turban Head
    head_top = torso_top - 10
    draw_pixel_rect(draw, cx - 4, head_top + 2, cx + 4, torso_top, C["SKIN_BASE"])
    draw_pixel_rect(draw, cx - 5, head_top - 2, cx + 5, head_top + 3, C["ARCHER_KHAKI_HI"])  # Wrapped turban
    draw_pixel_rect(draw, cx - 3, head_top + 4, cx - 2, head_top + 5, C["EYE_DARK"])
    draw_pixel_rect(draw, cx + 2, head_top + 4, cx + 3, head_top + 5, C["EYE_DARK"])

    # Composite Bamboo Recurve Bow in Hand
    bow_x = cx - 8
    draw.arc([bow_x - 4, torso_top - 6, bow_x + 6, torso_top + 16], start=90, end=270, fill=C["WOOD_BOW"], width=2)
    # Bowstring
    draw.line([bow_x + 1, torso_top - 5, bow_x + 1, torso_top + 15], fill=C["STEEL_HI"])

    return img

# ==========================================
# 4. CHARGING SOLDIER (44 x 58 px cells)
# ==========================================
def draw_charging_soldier_frame(direction, anim_type, frame_idx, cell_w=44, cell_h=58):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    lean_x = 3 if anim_type == "charge" else 0

    draw_ellipse_soft(draw, cx + lean_x, cy_base, 14, 4, C["SHADOW_GROUND"])

    # Heavy plate boots & greaves
    draw_pixel_rect(draw, cx - 6 + lean_x, cy_base - 14, cx - 2 + lean_x, cy_base - 2, C["CHARGE_CUIRASS_DARK"])
    draw_pixel_rect(draw, cx + 2 + lean_x, cy_base - 14, cx + 6 + lean_x, cy_base - 2, C["CHARGE_CUIRASS_DARK"])
    draw_pixel_rect(draw, cx - 7 + lean_x, cy_base - 2, cx - 1 + lean_x, cy_base, C["STEEL_DARK"])
    draw_pixel_rect(draw, cx + 1 + lean_x, cy_base - 2, cx + 7 + lean_x, cy_base, C["STEEL_DARK"])

    # Heavy Steel Cuirass (Plate Chest)
    torso_top = cy_base - 28
    draw_pixel_rect(draw, cx - 8 + lean_x, torso_top, cx + 8 + lean_x, cy_base - 12, C["CHARGE_CUIRASS_BASE"])
    draw_pixel_rect(draw, cx - 6 + lean_x, torso_top + 2, cx + 6 + lean_x, torso_top + 8, C["CHARGE_CUIRASS_HI"])
    # Crimson War Sash
    draw_pixel_rect(draw, cx - 8 + lean_x, cy_base - 14, cx + 8 + lean_x, cy_base - 10, C["CHARGE_SASH"])

    # Heavy Steel Helmet with Visor
    head_top = torso_top - 12
    draw_pixel_rect(draw, cx - 6 + lean_x, head_top, cx + 6 + lean_x, torso_top, C["STEEL_BASE"])
    draw_pixel_rect(draw, cx - 5 + lean_x, head_top + 4, cx + 5 + lean_x, head_top + 6, C["STEEL_DEEP"])  # Visor slit

    # Massive Curved Broadsword
    draw_pixel_rect(draw, cx + 8 + lean_x, torso_top + 2, cx + 11 + lean_x, torso_top + 5, C["BRASS_BASE"])
    draw_pixel_rect(draw, cx + 10 + lean_x, torso_top + 5, cx + 14 + lean_x, cy_base - 4, C["STEEL_HI"])

    return img

# ==========================================
# 5. ELITE HALBERDIER (48 x 64 px cells)
# ==========================================
def draw_halberdier_frame(direction, anim_type, frame_idx, cell_w=48, cell_h=64):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4]

    draw_ellipse_soft(draw, cx, cy_base, 14, 4, C["SHADOW_GROUND"])

    # Greaves & Boots
    draw_pixel_rect(draw, cx - 6, cy_base - 16 + bob_y, cx - 2, cy_base - 2 + bob_y, C["STEEL_DARK"])
    draw_pixel_rect(draw, cx + 2, cy_base - 16 + bob_y, cx + 6, cy_base - 2 + bob_y, C["STEEL_DARK"])
    draw_pixel_rect(draw, cx - 7, cy_base - 2 + bob_y, cx - 1, cy_base + bob_y, C["STEEL_BASE"])
    draw_pixel_rect(draw, cx + 1, cy_base - 2 + bob_y, cx + 7, cy_base + bob_y, C["STEEL_BASE"])

    # Imperial Purple Robe with Polished Steel Cuirass
    torso_top = cy_base - 32 + bob_y
    draw_pixel_rect(draw, cx - 8, torso_top, cx + 8, cy_base - 14 + bob_y, C["PURPLE_BASE"])
    draw_pixel_rect(draw, cx - 6, torso_top + 2, cx + 6, torso_top + 12, C["STEEL_HI"])
    draw_pixel_rect(draw, cx - 8, cy_base - 16 + bob_y, cx + 8, cy_base - 13 + bob_y, C["PURPLE_HI"])  # Sash

    # Helmet with Imperial Purple Plume
    head_top = torso_top - 14
    draw_pixel_rect(draw, cx - 6, head_top, cx + 6, torso_top, C["STEEL_BASE"])
    draw_pixel_rect(draw, cx - 2, head_top - 6, cx + 2, head_top, C["PURPLE_HI"])  # Royal plume

    # 5-Foot Halberd (Shaft + Crescent Axe + Spear Point)
    halb_x = cx + 8
    draw_pixel_rect(draw, halb_x, 4, halb_x + 2, cy_base, C["WOOD_BOW"])
    # Halberd Head (Axe blade & spear point)
    draw_pixel_rect(draw, halb_x - 1, 2, halb_x + 3, 10, C["STEEL_GLINT"])  # Spear point
    draw_pixel_rect(draw, halb_x + 2, 8, halb_x + 10, 16, C["STEEL_HI"])    # Axe blade
    draw_pixel_rect(draw, halb_x - 4, 10, halb_x, 14, C["STEEL_BASE"])      # Rear hook

    return img

# ==========================================
# 6. SPEAR SOLDIER (40 x 56 px cells)
# ==========================================
def draw_spearman_frame(direction, anim_type, frame_idx, cell_w=40, cell_h=56):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    bob_y = [0, -1, -1, 0][frame_idx % 4]

    draw_ellipse_soft(draw, cx, cy_base, 10, 3.5, C["SHADOW_GROUND"])

    # Trousers & Boots
    draw_pixel_rect(draw, cx - 5, cy_base - 14 + bob_y, cx - 2, cy_base - 2 + bob_y, C["SPEAR_TUNIC_DARK"])
    draw_pixel_rect(draw, cx + 2, cy_base - 14 + bob_y, cx + 5, cy_base - 2 + bob_y, C["SPEAR_TUNIC_DARK"])
    draw_pixel_rect(draw, cx - 6, cy_base - 2 + bob_y, cx - 2, cy_base + bob_y, C["LEATHER_BASE"])
    draw_pixel_rect(draw, cx + 2, cy_base - 2 + bob_y, cx + 6, cy_base + bob_y, C["LEATHER_BASE"])

    # Mustard Tunic
    torso_top = cy_base - 26 + bob_y
    draw_pixel_rect(draw, cx - 6, torso_top, cx + 6, cy_base - 12 + bob_y, C["SPEAR_TUNIC_BASE"])

    # Head & Helmet
    head_top = torso_top - 10
    draw_pixel_rect(draw, cx - 4, head_top, cx + 4, torso_top, C["STEEL_BASE"])
    draw_pixel_rect(draw, cx - 1, head_top - 2, cx + 1, head_top, C["BRASS_HI"])

    # Long Bamboo Spear (held upright)
    spear_x = cx + 7
    draw_pixel_rect(draw, spear_x, 2, spear_x + 2, cy_base, C["BAMBOO_SHAFT"])
    draw_pixel_rect(draw, spear_x - 1, 0, spear_x + 3, 6, C["STEEL_GLINT"])  # Spearhead
    draw_pixel_rect(draw, spear_x, 6, spear_x + 2, 8, C["BRASS_BASE"])       # Collar

    # Small Dhal shield on left arm
    draw_ellipse_soft(draw, cx - 7, torso_top + 6, 5, 5, C["BRASS_DARK"])
    draw_pixel_rect(draw, cx - 8, torso_top + 5, cx - 6, torso_top + 7, C["BRASS_HI"])

    return img

def build_enemy_roster():
    base_dir = os.path.join("ChroniclesOfSwarajya_Art", "02_Enemies_OptionB")
    os.makedirs(base_dir, exist_ok=True)

    configs = [
        ("swordsman", draw_swordsman_frame, 40, 56),
        ("shield_guard", draw_shield_guard_frame, 44, 58),
        ("archer", draw_archer_frame, 40, 56),
        ("charging_soldier", draw_charging_soldier_frame, 44, 58),
        ("elite_halberdier", draw_halberdier_frame, 48, 64),
        ("spear_soldier", draw_spearman_frame, 40, 56),
    ]

    for name, draw_fn, cw, ch in configs:
        folder = os.path.join(base_dir, name)
        os.makedirs(folder, exist_ok=True)

        # 1. Idle (4 dirs x 4 frames)
        idle_sheet = Image.new("RGBA", (cw * 4, ch * 4), C["NONE"])
        for r in range(4):
            for c in range(4):
                f = draw_fn(r, "idle", c, cw, ch)
                idle_sheet.paste(f, (c * cw, r * ch))
        idle_sheet.save(os.path.join(folder, f"{name}_idle.png"))

        # 2. Walk (4 dirs x 8 frames)
        walk_sheet = Image.new("RGBA", (cw * 8, ch * 4), C["NONE"])
        for r in range(4):
            for c in range(8):
                f = draw_fn(r, "walk", c, cw, ch)
                walk_sheet.paste(f, (c * cw, r * ch))
        walk_sheet.save(os.path.join(folder, f"{name}_walk.png"))

        # 3. Attack (4 dirs x 6 frames, using slightly wider cell for weapon reach)
        atk_w = cw + 16
        atk_h = ch
        atk_sheet = Image.new("RGBA", (atk_w * 6, atk_h * 4), C["NONE"])
        for r in range(4):
            for c in range(6):
                f = draw_fn(r, "idle", c, cw, ch)
                # Paste centered into attack frame with weapon extension
                atk_frame = Image.new("RGBA", (atk_w, atk_h), C["NONE"])
                atk_frame.paste(f, (8, 0))
                atk_sheet.paste(atk_frame, (c * atk_w, r * atk_h))
        atk_sheet.save(os.path.join(folder, f"{name}_attack.png"))

        print(f"✅ Generated {name} sprite sheets in {folder}")

if __name__ == "__main__":
    build_enemy_roster()
