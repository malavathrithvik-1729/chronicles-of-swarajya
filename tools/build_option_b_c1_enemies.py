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

# Rich Option B Master Enemy Palette (24+ tones per faction)
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
    
    # Leather & Boots
    "LEATHER_HI": (130, 68, 28, 255),
    "LEATHER_BASE": (78, 38, 14, 255),
    "LEATHER_DARK": (48, 22, 8, 255),
    "LEATHER_DEEP": (28, 12, 4, 255),
    
    # Polished Damascus Steel & Chainmail
    "STEEL_GLINT": (255, 255, 255, 255),
    "STEEL_HI": (230, 236, 245, 255),
    "STEEL_BASE": (160, 175, 195, 255),
    "STEEL_SHADOW": (95, 110, 130, 255),
    "STEEL_DARK": (50, 62, 78, 255),
    "STEEL_DEEP": (25, 32, 42, 255),
    "MAIL_BASE": (120, 132, 148, 255),
    "MAIL_DARK": (70, 80, 95, 255),
    
    # Antique Brass & Gold Accents
    "BRASS_GLINT": (255, 248, 180, 255),
    "BRASS_HI": (250, 215, 90, 255),
    "BRASS_BASE": (205, 150, 30, 255),
    "BRASS_SHADOW": (145, 98, 18, 255),
    "BRASS_DARK": (90, 58, 10, 255),
    
    # Swordsman Tunic: Quilted Deccan Deep Emerald & Ochre Turban
    "SWORD_GREEN_HI": (65, 145, 88, 255),
    "SWORD_GREEN_BASE": (32, 92, 52, 255),
    "SWORD_GREEN_SHADOW": (18, 62, 34, 255),
    "SWORD_GREEN_DEEP": (10, 38, 20, 255),
    "SWORD_TURBAN_HI": (245, 185, 55, 255),
    "SWORD_TURBAN_BASE": (205, 140, 25, 255),
    "SWORD_TURBAN_SHADOW": (150, 95, 15, 255),
    "SWORD_TURBAN_DEEP": (95, 55, 8, 255),
    
    # Shield Guard: Heavy Crimson Lamellar, Plate Mirrors & Buffalo Hide
    "SHIELD_RED_HI": (205, 58, 58, 255),
    "SHIELD_RED_BASE": (145, 28, 28, 255),
    "SHIELD_RED_SHADOW": (98, 18, 18, 255),
    "SHIELD_RED_DEEP": (58, 10, 10, 255),
    "HIDE_HI": (72, 55, 45, 255),
    "HIDE_BASE": (45, 34, 28, 255),
    "HIDE_DARK": (28, 20, 16, 255),
    
    # VFX / Attack Trails
    "SLASH_CORE": (255, 255, 255, 250),
    "SLASH_EDGE": (255, 200, 100, 220),
    "SLASH_TRAIL": (210, 110, 30, 140),
    "SLASH_FADE": (160, 50, 15, 60),
    "BASH_DUST": (220, 200, 170, 180),
}

# ==============================================================================
# 1. REFINED DECCAN SWORDSMAN (40 x 56 px standard, 56 x 56 px attack)
# ==============================================================================
def draw_refined_swordsman_frame(direction, anim_type, frame_idx, cell_w=40, cell_h=56):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    
    bob_y = 0
    stride = 0
    arm_swing = 0
    lean_x = 0
    
    if anim_type == "idle":
        # 4-frame rhythmic combat breathing cycle
        bobs = [0, -1, -1, 0]
        bob_y = bobs[frame_idx % 4]
    elif anim_type == "walk":
        # 8-frame natural weight shifting walk
        bobs = [0, 1, 0, -1, 0, 1, 0, -1]
        bob_y = bobs[frame_idx % 8]
        strides = [3, 2, 0, -2, -3, -2, 0, 2]
        stride = strides[frame_idx % 8]
        arm_swing = -stride
        lean_x = 1 if stride > 0 else (-1 if stride < 0 else 0)

    # 1. Ground Shadow
    draw_ellipse_soft(draw, cx, cy_base, 12, 4, C["SHADOW_GROUND"])
    
    # 2. Footwear & Legs (Trousers & Stitched Leather Mojari)
    leg_top = cy_base - 15 + bob_y
    leg_bot = cy_base - 2 + bob_y
    
    if direction == 0:  # South
        # Dark green fitted trousers with inner shadow
        draw_pixel_rect(draw, cx - 6, leg_top, cx - 2, leg_bot - 1, C["SWORD_GREEN_SHADOW"])
        draw_pixel_rect(draw, cx + 2, leg_top, cx + 6, leg_bot - 1, C["SWORD_GREEN_SHADOW"])
        draw_pixel_rect(draw, cx - 5, leg_top, cx - 3, leg_bot - 3, C["SWORD_GREEN_BASE"])
        draw_pixel_rect(draw, cx + 3, leg_top, cx + 5, leg_bot - 3, C["SWORD_GREEN_BASE"])
        
        # Leather boots with toe caps
        l_x = cx - 6 + stride
        r_x = cx + 2 - stride
        draw_pixel_rect(draw, l_x, leg_bot, l_x + 4, leg_bot + 2, C["LEATHER_BASE"])
        draw_pixel_rect(draw, l_x - 1, leg_bot + 1, l_x, leg_bot + 2, C["LEATHER_HI"])
        draw_pixel_rect(draw, r_x, leg_bot, r_x + 4, leg_bot + 2, C["LEATHER_BASE"])
        draw_pixel_rect(draw, r_x + 4, leg_bot + 1, r_x + 5, leg_bot + 2, C["LEATHER_HI"])
        
    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 6, leg_top, cx - 2, leg_bot - 1, C["SWORD_GREEN_DEEP"])
        draw_pixel_rect(draw, cx + 2, leg_top, cx + 6, leg_bot - 1, C["SWORD_GREEN_DEEP"])
        l_x = cx - 6 - stride
        r_x = cx + 2 + stride
        draw_pixel_rect(draw, l_x, leg_bot, l_x + 4, leg_bot + 2, C["LEATHER_DARK"])
        draw_pixel_rect(draw, r_x, leg_bot, r_x + 4, leg_bot + 2, C["LEATHER_DARK"])
        
    else:  # East (2) / West (3)
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 4, leg_top, cx + 4, leg_bot - 1, C["SWORD_GREEN_SHADOW"])
        f_x = cx - 3 + stride * sign
        b_x = cx - 1 - stride * sign
        draw_pixel_rect(draw, f_x, leg_bot, f_x + 5, leg_bot + 2, C["LEATHER_BASE"])
        draw_pixel_rect(draw, f_x + 5 * (1 if sign > 0 else 0), leg_bot + 1, f_x + 6 * (1 if sign > 0 else 0), leg_bot + 2, C["LEATHER_HI"])
        draw_pixel_rect(draw, b_x, leg_bot, b_x + 4, leg_bot + 2, C["LEATHER_DARK"])

    # 3. Quilted Gambeson / Tunic (Body & Belt)
    tunic_top = cy_base - 30 + bob_y
    tunic_bot = leg_top + 3
    
    if direction == 0:  # South
        # Quilted folds
        draw_pixel_rect(draw, cx - 7, tunic_top, cx + 7, tunic_bot, C["SWORD_GREEN_BASE"])
        draw_pixel_rect(draw, cx - 7, tunic_top, cx - 5, tunic_bot, C["SWORD_GREEN_SHADOW"])
        draw_pixel_rect(draw, cx + 5, tunic_top, cx + 7, tunic_bot, C["SWORD_GREEN_SHADOW"])
        draw_pixel_rect(draw, cx - 3, tunic_top + 2, cx - 1, tunic_bot - 2, C["SWORD_GREEN_HI"])
        # Chainmail collar peeking through
        draw_pixel_rect(draw, cx - 3, tunic_top - 1, cx + 3, tunic_top + 3, C["MAIL_BASE"])
        draw_pixel_rect(draw, cx - 2, tunic_top + 1, cx + 2, tunic_top + 2, C["MAIL_DARK"])
        # Crossbody leather baldrick strap
        draw_pixel_rect(draw, cx - 6, tunic_top + 2, cx + 5, tunic_top + 10, C["LEATHER_BASE"])
        draw_pixel_rect(draw, cx - 5, tunic_top + 3, cx + 4, tunic_top + 9, C["LEATHER_HI"])
        # Broad Leather Kamarbandh with Brass Buckle
        sash_y = tunic_top + 12
        draw_pixel_rect(draw, cx - 7, sash_y, cx + 7, sash_y + 4, C["LEATHER_DARK"])
        draw_pixel_rect(draw, cx - 6, sash_y + 1, cx + 6, sash_y + 3, C["LEATHER_BASE"])
        draw_pixel_rect(draw, cx - 2, sash_y, cx + 2, sash_y + 4, C["BRASS_HI"])
        draw_pixel_rect(draw, cx - 1, sash_y + 1, cx + 1, sash_y + 3, C["BRASS_BASE"])
        
    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 7, tunic_top, cx + 7, tunic_bot, C["SWORD_GREEN_SHADOW"])
        draw_pixel_rect(draw, cx - 6, tunic_top + 12, cx + 6, tunic_top + 16, C["LEATHER_DARK"])
        # Scabbard strap across back
        draw_pixel_rect(draw, cx - 5, tunic_top + 3, cx + 5, tunic_top + 11, C["LEATHER_BASE"])
        
    else:  # East / West
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 6, tunic_top, cx + 6, tunic_bot, C["SWORD_GREEN_BASE"])
        draw_pixel_rect(draw, cx - 6 * sign, tunic_top, cx - 3 * sign, tunic_bot, C["SWORD_GREEN_SHADOW"])
        draw_pixel_rect(draw, cx - 6, tunic_top + 12, cx + 6, tunic_top + 16, C["LEATHER_BASE"])
        draw_pixel_rect(draw, cx + 3 * sign, tunic_top + 12, cx + 5 * sign, tunic_top + 16, C["BRASS_HI"])

    # 4. Head, Face & Authentic Deccan Steel-Plated Turban
    head_top = tunic_top - 14
    head_bot = tunic_top
    
    if direction == 0:  # South
        # Face & Neck
        draw_pixel_rect(draw, cx - 4, head_top + 4, cx + 4, head_bot, C["SKIN_BASE"])
        draw_pixel_rect(draw, cx - 4, head_top + 6, cx - 3, head_bot - 1, C["SKIN_SHADOW"])
        # Eyes
        draw_pixel_rect(draw, cx - 3, head_top + 6, cx - 2, head_top + 7, C["EYE_WHITE"])
        draw_pixel_rect(draw, cx - 3, head_top + 6, cx - 3, head_top + 7, C["EYE_DARK"])
        draw_pixel_rect(draw, cx + 2, head_top + 6, cx + 3, head_top + 7, C["EYE_WHITE"])
        draw_pixel_rect(draw, cx + 3, head_top + 6, cx + 3, head_top + 7, C["EYE_DARK"])
        # Thick fierce moustache & beard
        draw_pixel_rect(draw, cx - 4, head_top + 9, cx + 4, head_top + 11, C["HAIR_BASE"])
        draw_pixel_rect(draw, cx - 5, head_top + 8, cx - 4, head_top + 10, C["HAIR_BASE"])
        draw_pixel_rect(draw, cx + 4, head_top + 8, cx + 5, head_top + 10, C["HAIR_BASE"])
        # Deccan Steel Helmet with Turban Wrap (*Top* & *Mandil*)
        # Steel bowl cap
        draw_pixel_rect(draw, cx - 4, head_top - 2, cx + 4, head_top + 3, C["STEEL_BASE"])
        draw_pixel_rect(draw, cx - 3, head_top - 1, cx + 1, head_top + 1, C["STEEL_HI"])
        draw_pixel_rect(draw, cx - 1, head_top - 4, cx + 1, head_top - 2, C["BRASS_HI"])  # Top spike
        # Golden-ochre turban coils wrapped around steel bowl
        draw_pixel_rect(draw, cx - 6, head_top + 1, cx + 6, head_top + 5, C["SWORD_TURBAN_BASE"])
        draw_pixel_rect(draw, cx - 5, head_top + 1, cx + 5, head_top + 3, C["SWORD_TURBAN_HI"])
        draw_pixel_rect(draw, cx - 6, head_top + 4, cx + 6, head_top + 5, C["SWORD_TURBAN_SHADOW"])
        # Mail aventail hanging around ears
        draw_pixel_rect(draw, cx - 6, head_top + 5, cx - 4, head_top + 10, C["MAIL_BASE"])
        draw_pixel_rect(draw, cx + 4, head_top + 5, cx + 6, head_top + 10, C["MAIL_DARK"])
        
    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 5, head_top - 2, cx + 5, head_top + 3, C["STEEL_DARK"])
        draw_pixel_rect(draw, cx - 1, head_top - 4, cx + 1, head_top - 2, C["BRASS_BASE"])
        draw_pixel_rect(draw, cx - 6, head_top + 1, cx + 6, head_top + 5, C["SWORD_TURBAN_SHADOW"])
        # Rear aventail covering neck
        draw_pixel_rect(draw, cx - 5, head_top + 5, cx + 5, head_bot + 1, C["MAIL_DARK"])
        draw_pixel_rect(draw, cx - 4, head_top + 6, cx + 4, head_bot, C["MAIL_BASE"])
        
    else:  # East / West
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 4, head_top + 4, cx + 4, head_bot, C["SKIN_BASE"])
        draw_pixel_rect(draw, cx + 2 * sign, head_top + 6, cx + 4 * sign, head_top + 7, C["EYE_DARK"])
        draw_pixel_rect(draw, cx + 1 * sign, head_top + 9, cx + 5 * sign, head_top + 11, C["HAIR_BASE"])
        # Helmet & Turban profile
        draw_pixel_rect(draw, cx - 5, head_top - 2, cx + 4, head_top + 3, C["STEEL_BASE"])
        draw_pixel_rect(draw, cx - 1, head_top - 4, cx + 1, head_top - 2, C["BRASS_HI"])
        draw_pixel_rect(draw, cx - 6, head_top + 1, cx + 5, head_top + 5, C["SWORD_TURBAN_BASE"])
        draw_pixel_rect(draw, cx - 5 * sign, head_top + 5, cx - 1 * sign, head_bot, C["MAIL_BASE"])

    # 5. Arms, Hands & Curved Talwar with Disc Pommel
    arm_top = tunic_top + 2
    if direction == 0:  # South
        # Left Arm (Holding Scabbard)
        draw_pixel_rect(draw, cx - 9, arm_top, cx - 6, arm_top + 9 + arm_swing, C["SWORD_GREEN_BASE"])
        draw_pixel_rect(draw, cx - 8, arm_top + 9 + arm_swing, cx - 6, arm_top + 12 + arm_swing, C["SKIN_BASE"])
        # Right Arm (Hand resting on Talwar hilt)
        draw_pixel_rect(draw, cx + 6, arm_top, cx + 9, arm_top + 9 - arm_swing, C["SWORD_GREEN_BASE"])
        draw_pixel_rect(draw, cx + 6, arm_top + 9 - arm_swing, cx + 8, arm_top + 12 - arm_swing, C["SKIN_BASE"])
        # Curved Talwar Scabbard on Left Hip
        sw_x = cx - 8
        sw_y = arm_top + 7
        draw_pixel_rect(draw, sw_x - 3, sw_y, sw_x + 1, sw_y + 2, C["BRASS_HI"])  # Disc Pommel
        draw_pixel_rect(draw, sw_x - 1, sw_y - 2, sw_x, sw_y, C["STEEL_GLINT"])  # Spike
        draw_pixel_rect(draw, sw_x - 2, sw_y + 3, sw_x, sw_y + 14, C["LEATHER_BASE"])
        draw_pixel_rect(draw, sw_x - 4, sw_y + 12, sw_x - 2, sw_y + 16, C["LEATHER_DARK"])
        draw_pixel_rect(draw, sw_x - 4, sw_y + 15, sw_x - 2, sw_y + 17, C["BRASS_HI"])  # Tip Chape
        
    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 9, arm_top, cx - 6, arm_top + 9 - arm_swing, C["SWORD_GREEN_SHADOW"])
        draw_pixel_rect(draw, cx + 6, arm_top, cx + 9, arm_top + 9 + arm_swing, C["SWORD_GREEN_SHADOW"])
        
    else:  # East / West
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx + 4 * sign, arm_top + 2, cx + 8 * sign, arm_top + 10, C["SWORD_GREEN_BASE"])
        draw_pixel_rect(draw, cx + 6 * sign, arm_top + 9, cx + 8 * sign, arm_top + 12, C["SKIN_BASE"])
        # Talwar hilt held in hand
        draw_pixel_rect(draw, cx + 8 * sign, arm_top + 7, cx + 11 * sign, arm_top + 9, C["BRASS_HI"])
        draw_pixel_rect(draw, cx + 9 * sign, arm_top + 9, cx + 11 * sign, arm_top + 20, C["STEEL_BASE"])
        draw_pixel_rect(draw, cx + 10 * sign, arm_top + 10, cx + 11 * sign, arm_top + 19, C["STEEL_HI"])
        
    return img

def draw_refined_swordsman_attack_frame(direction, frame_idx, cell_w=56, cell_h=56):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    
    # Ground shadow
    draw_ellipse_soft(draw, cx, cy_base, 14, 4.5, C["SHADOW_GROUND"])
    
    # 6-frame combat strike lifecycle:
    # 0: Stance ready
    # 1: Coil back & raise blade (Telegraph 1)
    # 2: High wind-up peak with glint (Telegraph 2)
    # 3: Explosive forward slash with dynamic curved arc (Active Hit)
    # 4: Overswing follow-through (Momentum)
    # 5: Recovery step back
    
    shift_x = 0
    if direction == 2:  # East
        shift_x = [0, -2, -3, 6, 4, 1][frame_idx % 6]
    elif direction == 3:  # West
        shift_x = [0, 2, 3, -6, -4, -1][frame_idx % 6]
    elif direction == 0:  # South
        shift_x = 0
        
    # Render base warrior
    base = draw_refined_swordsman_frame(direction, "idle", 0, 40, 56)
    paste_x = (cell_w - 40) // 2 + shift_x
    img.paste(base, (paste_x, 0), base)
    
    # Weapon & VFX Overlay
    hx = cx + shift_x
    hy = 24
    
    if frame_idx in (1, 2):  # Telegraph: Coil & raise sword overhead
        sign = 1 if direction == 2 else (-1 if direction == 3 else 1)
        draw_pixel_rect(draw, hx - 4 * sign, hy - 14, hx + 1 * sign, hy - 10, C["BRASS_HI"])
        draw_pixel_rect(draw, hx - 2 * sign, hy - 24, hx + 2 * sign, hy - 14, C["STEEL_HI"])
        # Specular glint on windup tip
        draw_pixel_rect(draw, hx - 1 * sign, hy - 26, hx + 1 * sign, hy - 24, C["STEEL_GLINT"])
        
    elif frame_idx == 3:  # Active Strike: Forward Lunge + Luminous Arc Trail
        if direction in (0, 2):  # South / East
            draw_pixel_rect(draw, hx + 6, hy + 2, hx + 10, hy + 5, C["BRASS_HI"])
            draw_pixel_rect(draw, hx + 10, hy + 2, hx + 25, hy + 6, C["STEEL_GLINT"])
            # Curved dynamic slash arc
            draw.arc([hx - 8, hy - 16, hx + 28, hy + 22], start=270, end=90, fill=C["SLASH_CORE"], width=3)
            draw.arc([hx - 9, hy - 17, hx + 29, hy + 23], start=265, end=95, fill=C["SLASH_EDGE"], width=1)
        elif direction == 3:  # West
            draw_pixel_rect(draw, hx - 10, hy + 2, hx - 6, hy + 5, C["BRASS_HI"])
            draw_pixel_rect(draw, hx - 25, hy + 2, hx - 10, hy + 6, C["STEEL_GLINT"])
            draw.arc([hx - 28, hy - 16, hx + 8, hy + 22], start=90, end=270, fill=C["SLASH_CORE"], width=3)
            draw.arc([hx - 29, hy - 17, hx + 9, hy + 23], start=85, end=275, fill=C["SLASH_EDGE"], width=1)
        elif direction == 1:  # North
            draw_pixel_rect(draw, hx + 4, hy - 18, hx + 8, hy - 14, C["BRASS_HI"])
            draw_pixel_rect(draw, hx + 6, hy - 26, hx + 10, hy - 16, C["STEEL_GLINT"])
            draw.arc([hx - 16, hy - 28, hx + 18, hy + 4], start=180, end=360, fill=C["SLASH_CORE"], width=3)
            
    elif frame_idx == 4:  # Follow-through
        if direction in (0, 2):
            draw_pixel_rect(draw, hx + 4, hy + 8, hx + 8, hy + 11, C["BRASS_BASE"])
            draw_pixel_rect(draw, hx + 8, hy + 8, hx + 20, hy + 12, C["STEEL_BASE"])
            draw.arc([hx - 4, hy - 8, hx + 24, hy + 20], start=310, end=70, fill=C["SLASH_TRAIL"], width=2)
        elif direction == 3:
            draw_pixel_rect(draw, hx - 8, hy + 8, hx - 4, hy + 11, C["BRASS_BASE"])
            draw_pixel_rect(draw, hx - 20, hy + 8, hx - 8, hy + 12, C["STEEL_BASE"])
            draw.arc([hx - 24, hy - 8, hx + 4, hy + 20], start=110, end=230, fill=C["SLASH_TRAIL"], width=2)
            
    return img

# ==============================================================================
# 2. REFINED HEAVY SHIELD GUARD (44 x 58 px standard, 60 x 58 px attack)
# ==============================================================================
def draw_refined_shield_guard_frame(direction, anim_type, frame_idx, cell_w=44, cell_h=58):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    
    bob_y = 0
    stride = 0
    if anim_type == "idle":
        bob_y = [0, -1, -1, 0][frame_idx % 4]
    elif anim_type == "walk":
        bobs = [0, 1, 0, -1, 0, 1, 0, -1]
        bob_y = bobs[frame_idx % 8]
        strides = [2, 1, 0, -1, -2, -1, 0, 1]
        stride = strides[frame_idx % 8]

    # Ground shadow (wider for heavy unit)
    draw_ellipse_soft(draw, cx, cy_base, 14, 4.5, C["SHADOW_GROUND"])
    
    # 1. Armoured Greaves & Iron-Plated Boots
    leg_top = cy_base - 16 + bob_y
    leg_bot = cy_base - 2 + bob_y
    
    if direction == 0:  # South
        draw_pixel_rect(draw, cx - 7, leg_top, cx - 2, leg_bot - 1, C["SHIELD_RED_SHADOW"])
        draw_pixel_rect(draw, cx + 2, leg_top, cx + 7, leg_bot - 1, C["SHIELD_RED_SHADOW"])
        # Iron shin guards
        draw_pixel_rect(draw, cx - 6, leg_top + 2, cx - 3, leg_bot - 2, C["STEEL_SHADOW"])
        draw_pixel_rect(draw, cx + 3, leg_top + 2, cx + 6, leg_bot - 2, C["STEEL_SHADOW"])
        # Heavy leather & steel reinforced boots
        l_x = cx - 7 + stride
        r_x = cx + 2 - stride
        draw_pixel_rect(draw, l_x, leg_bot, l_x + 5, leg_bot + 2, C["LEATHER_BASE"])
        draw_pixel_rect(draw, l_x + 1, leg_bot, l_x + 4, leg_bot + 1, C["STEEL_BASE"])
        draw_pixel_rect(draw, r_x, leg_bot, r_x + 5, leg_bot + 2, C["LEATHER_BASE"])
        draw_pixel_rect(draw, r_x + 1, leg_bot, r_x + 4, leg_bot + 1, C["STEEL_BASE"])
    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 7, leg_top, cx - 2, leg_bot - 1, C["SHIELD_RED_DEEP"])
        draw_pixel_rect(draw, cx + 2, leg_top, cx + 7, leg_bot - 1, C["SHIELD_RED_DEEP"])
        l_x = cx - 7 - stride
        r_x = cx + 2 + stride
        draw_pixel_rect(draw, l_x, leg_bot, l_x + 5, leg_bot + 2, C["LEATHER_DARK"])
        draw_pixel_rect(draw, r_x, leg_bot, r_x + 5, leg_bot + 2, C["LEATHER_DARK"])
    else:  # East / West
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 5, leg_top, cx + 5, leg_bot - 1, C["SHIELD_RED_SHADOW"])
        draw_pixel_rect(draw, cx - 2, leg_top + 2, cx + 2, leg_bot - 2, C["STEEL_SHADOW"])
        f_x = cx - 3 + stride * sign
        draw_pixel_rect(draw, f_x, leg_bot, f_x + 6, leg_bot + 2, C["LEATHER_BASE"])
        draw_pixel_rect(draw, f_x + 2, leg_bot, f_x + 5, leg_bot + 1, C["STEEL_BASE"])

    # 2. Torso: Heavy Char-Aina (Four-Mirror) Plate Armour over Padded Brigandine
    torso_top = cy_base - 32 + bob_y
    torso_bot = leg_top + 2
    
    if direction == 0:  # South
        # Deep crimson padded foundation
        draw_pixel_rect(draw, cx - 8, torso_top, cx + 8, torso_bot, C["SHIELD_RED_BASE"])
        draw_pixel_rect(draw, cx - 8, torso_top, cx - 6, torso_bot, C["SHIELD_RED_SHADOW"])
        draw_pixel_rect(draw, cx + 6, torso_top, cx + 8, torso_bot, C["SHIELD_RED_SHADOW"])
        # Central Rectangular Steel Mirror Plate (*Char-Aina*)
        draw_pixel_rect(draw, cx - 5, torso_top + 4, cx + 5, torso_top + 16, C["STEEL_BASE"])
        draw_pixel_rect(draw, cx - 4, torso_top + 5, cx + 4, torso_top + 15, C["STEEL_HI"])
        draw_pixel_rect(draw, cx - 2, torso_top + 6, cx + 2, torso_top + 12, C["STEEL_GLINT"])
        # Brass border rivets around plate
        for rx, ry in [(-5, 4), (5, 4), (-5, 15), (5, 15), (0, 4), (0, 15)]:
            draw_pixel_rect(draw, cx + rx - 1, torso_top + ry - 1, cx + rx + 1, torso_top + ry + 1, C["BRASS_HI"])
        # Heavy belt with brass studs
        draw_pixel_rect(draw, cx - 8, torso_top + 16, cx + 8, torso_top + 20, C["LEATHER_DARK"])
        draw_pixel_rect(draw, cx - 2, torso_top + 16, cx + 2, torso_top + 20, C["BRASS_HI"])
    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 8, torso_top, cx + 8, torso_bot, C["SHIELD_RED_DEEP"])
        # Back steel mirror plate
        draw_pixel_rect(draw, cx - 5, torso_top + 4, cx + 5, torso_top + 16, C["STEEL_SHADOW"])
        draw_pixel_rect(draw, cx - 4, torso_top + 5, cx + 4, torso_top + 15, C["STEEL_BASE"])
    else:  # East / West
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 7, torso_top, cx + 7, torso_bot, C["SHIELD_RED_BASE"])
        draw_pixel_rect(draw, cx - 3, torso_top + 4, cx + 4, torso_top + 16, C["STEEL_BASE"])
        draw_pixel_rect(draw, cx - 2, torso_top + 5, cx + 3, torso_top + 14, C["STEEL_HI"])

    # 3. Head & Heavy Conical Steel Helmet (*Kulak*) with Chain Aventail & Nasal Bar
    head_top = torso_top - 14
    head_bot = torso_top
    
    if direction == 0:  # South
        # Face under aventail
        draw_pixel_rect(draw, cx - 4, head_top + 4, cx + 4, head_bot, C["SKIN_SHADOW"])
        # Glaring eyes through visor
        draw_pixel_rect(draw, cx - 3, head_top + 6, cx - 2, head_top + 7, C["EYE_WHITE"])
        draw_pixel_rect(draw, cx - 3, head_top + 6, cx - 3, head_top + 7, C["EYE_DARK"])
        draw_pixel_rect(draw, cx + 2, head_top + 6, cx + 3, head_top + 7, C["EYE_WHITE"])
        draw_pixel_rect(draw, cx + 3, head_top + 6, cx + 3, head_top + 7, C["EYE_DARK"])
        # Conical steel helmet
        draw_pixel_rect(draw, cx - 5, head_top - 1, cx + 5, head_top + 4, C["STEEL_BASE"])
        draw_pixel_rect(draw, cx - 3, head_top - 3, cx + 3, head_top - 1, C["STEEL_HI"])
        draw_pixel_rect(draw, cx - 1, head_top - 5, cx + 1, head_top - 3, C["BRASS_HI"])  # Top finial
        # Sliding steel nasal bar
        draw_pixel_rect(draw, cx - 1, head_top + 1, cx + 1, head_top + 9, C["STEEL_GLINT"])
        # Mail aventail curtain covering cheeks and neck
        draw_pixel_rect(draw, cx - 6, head_top + 4, cx - 4, head_bot + 1, C["MAIL_BASE"])
        draw_pixel_rect(draw, cx + 4, head_top + 4, cx + 6, head_bot + 1, C["MAIL_DARK"])
        draw_pixel_rect(draw, cx - 3, head_bot - 2, cx + 3, head_bot + 1, C["MAIL_BASE"])
    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 5, head_top - 1, cx + 5, head_top + 4, C["STEEL_SHADOW"])
        draw_pixel_rect(draw, cx - 3, head_top - 3, cx + 3, head_top - 1, C["STEEL_BASE"])
        draw_pixel_rect(draw, cx - 1, head_top - 5, cx + 1, head_top - 3, C["BRASS_BASE"])
        draw_pixel_rect(draw, cx - 6, head_top + 4, cx + 6, head_bot + 2, C["MAIL_DARK"])
    else:  # East / West
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 5, head_top - 1, cx + 5, head_top + 4, C["STEEL_BASE"])
        draw_pixel_rect(draw, cx - 2, head_top - 4, cx + 2, head_top - 1, C["STEEL_HI"])
        draw_pixel_rect(draw, cx + 2 * sign, head_top + 2, cx + 4 * sign, head_top + 8, C["STEEL_GLINT"])
        draw_pixel_rect(draw, cx - 6 * sign, head_top + 4, cx, head_bot + 1, C["MAIL_BASE"])

    # 4. MASTER CRAFTED DHAL SHIELD (Convex Rhino/Buffalo Hide with 4 Brass Bosses)
    # The shield is prominent, heavy, and dynamically angled
    if direction == 0:  # South: Shield held forward on left arm
        sx = cx - 12
        sy = torso_top + 3
        # Outer Brass Rim
        draw_ellipse_soft(draw, sx + 8, sy + 12, 10, 14, C["BRASS_BASE"])
        draw_ellipse_soft(draw, sx + 8, sy + 12, 9, 13, C["HIDE_BASE"])
        draw_ellipse_soft(draw, sx + 7, sy + 11, 8, 12, C["HIDE_HI"])
        # 4 Polished Brass Bosses (*Katori*)
        for bx, by in [(sx + 5, sy + 8), (sx + 11, sy + 8), (sx + 5, sy + 16), (sx + 11, sy + 16)]:
            draw_pixel_rect(draw, bx - 1, by - 1, bx + 1, by + 1, C["BRASS_HI"])
            draw_pixel_rect(draw, bx, by, bx, by, C["BRASS_GLINT"])
        # Central Crescent Inlay
        draw_pixel_rect(draw, sx + 7, sy + 11, sx + 9, sy + 13, C["BRASS_GLINT"])
        # Right Hand: Firmly gripping Heavy Talwar
        draw_pixel_rect(draw, cx + 7, torso_top + 8, cx + 11, torso_top + 16, C["SHIELD_RED_BASE"])
        draw_pixel_rect(draw, cx + 9, torso_top + 14, cx + 11, torso_top + 17, C["SKIN_BASE"])
        draw_pixel_rect(draw, cx + 10, torso_top + 12, cx + 13, torso_top + 14, C["BRASS_HI"])
        draw_pixel_rect(draw, cx + 11, torso_top + 14, cx + 13, torso_top + 24, C["STEEL_HI"])
        
    elif direction == 1:  # North: Shield strapped to back/left side
        sx = cx - 10
        sy = torso_top + 4
        draw_ellipse_soft(draw, sx + 6, sy + 12, 9, 13, C["HIDE_DARK"])
        draw_pixel_rect(draw, sx + 4, sy + 6, sx + 8, sy + 18, C["LEATHER_BASE"])  # Enarmes straps
        # Weapon in right hand
        draw_pixel_rect(draw, cx + 9, torso_top + 14, cx + 11, torso_top + 24, C["STEEL_DARK"])
        
    elif direction in (2, 3):  # East (2) / West (3)
        sign = 1 if direction == 2 else -1
        # In side view, the shield dominates the leading profile
        sx = cx + (6 if direction == 2 else -16)
        sy = torso_top + 3
        draw_ellipse_soft(draw, sx + 5, sy + 12, 6, 14, C["BRASS_BASE"])
        draw_ellipse_soft(draw, sx + 5, sy + 12, 5, 13, C["HIDE_BASE"])
        # Bosses in perspective
        draw_pixel_rect(draw, sx + 4, sy + 8, sx + 6, sy + 10, C["BRASS_HI"])
        draw_pixel_rect(draw, sx + 4, sy + 14, sx + 6, sy + 16, C["BRASS_HI"])
        # Rear Arm & Weapon
        draw_pixel_rect(draw, cx - 8 * sign, torso_top + 8, cx - 5 * sign, torso_top + 16, C["SHIELD_RED_BASE"])
        draw_pixel_rect(draw, cx - 7 * sign, torso_top + 16, cx - 5 * sign, torso_top + 26, C["STEEL_BASE"])

    return img

def draw_refined_shield_guard_attack_frame(direction, frame_idx, cell_w=60, cell_h=58):
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)
    cx = cell_w // 2
    cy_base = cell_h - 4
    
    draw_ellipse_soft(draw, cx, cy_base, 15, 5, C["SHADOW_GROUND"])
    
    # 6-frame heavy guard sequence:
    # 0: Braced guard stance
    # 1: Coil back shield & raise talwar (Telegraph window)
    # 2: Maximum coiled spring (Telegraph flash)
    # 3: Heavy Shield Bash Thrust (Impact wave & dust)
    # 4: Over-the-shield Talwar downward cleave
    # 5: Return to braced guard
    
    shift_x = 0
    if direction == 2:  # East
        shift_x = [0, -3, -4, 7, 5, 2][frame_idx % 6]
    elif direction == 3:  # West
        shift_x = [0, 3, 4, -7, -5, -2][frame_idx % 6]
        
    base = draw_refined_shield_guard_frame(direction, "idle", 0, 44, 58)
    paste_x = (cell_w - 44) // 2 + shift_x
    img.paste(base, (paste_x, 0), base)
    
    hx = cx + shift_x
    hy = 26
    
    if frame_idx in (1, 2):  # Telegraph: Coil back with glint
        sign = 1 if direction == 2 else (-1 if direction == 3 else 1)
        # Raised talwar high
        draw_pixel_rect(draw, hx - 6 * sign, hy - 16, hx - 2 * sign, hy - 13, C["BRASS_HI"])
        draw_pixel_rect(draw, hx - 5 * sign, hy - 26, hx - 1 * sign, hy - 16, C["STEEL_HI"])
        draw_pixel_rect(draw, hx - 4 * sign, hy - 28, hx - 2 * sign, hy - 26, C["STEEL_GLINT"])
        
    elif frame_idx == 3:  # Shield Bash Shockwave (Heavy Impact)
        if direction in (0, 2):
            draw.arc([hx + 6, hy - 10, hx + 28, hy + 24], start=290, end=70, fill=C["SLASH_CORE"], width=3)
            # Impact spark / dust
            draw_pixel_rect(draw, hx + 24, hy + 2, hx + 28, hy + 6, C["BRASS_GLINT"])
            draw_pixel_rect(draw, hx + 22, hy + 12, hx + 26, hy + 16, C["BASH_DUST"])
        elif direction == 3:
            draw.arc([hx - 28, hy - 10, hx - 6, hy + 24], start=110, end=250, fill=C["SLASH_CORE"], width=3)
            draw_pixel_rect(draw, hx - 28, hy + 2, hx - 24, hy + 6, C["BRASS_GLINT"])
            draw_pixel_rect(draw, hx - 26, hy + 12, hx - 22, hy + 16, C["BASH_DUST"])
            
    elif frame_idx == 4:  # Over-the-shield cleave
        if direction in (0, 2):
            draw_pixel_rect(draw, hx + 8, hy + 4, hx + 12, hy + 7, C["BRASS_HI"])
            draw_pixel_rect(draw, hx + 12, hy + 4, hx + 26, hy + 8, C["STEEL_GLINT"])
            draw.arc([hx - 4, hy - 14, hx + 28, hy + 24], start=280, end=90, fill=C["SLASH_CORE"], width=2)
        elif direction == 3:
            draw_pixel_rect(draw, hx - 12, hy + 4, hx - 8, hy + 7, C["BRASS_HI"])
            draw_pixel_rect(draw, hx - 26, hy + 4, hx - 12, hy + 8, C["STEEL_GLINT"])
            draw.arc([hx - 28, hy - 14, hx + 4, hy + 24], start=90, end=260, fill=C["SLASH_CORE"], width=2)
            
    return img

# ==============================================================================
# MASTER BUILD ROUTINE
# ==============================================================================
def build_c1_enemy_assets():
    art_dir = "ChroniclesOfSwarajya_Art/02_Enemies_OptionB"
    os.makedirs(os.path.join(art_dir, "swordsman"), exist_ok=True)
    os.makedirs(os.path.join(art_dir, "shield_guard"), exist_ok=True)
    
    print("🎨 Rendering Refined Option B Deccan Swordsman...")
    # Idle (4 cols x 4 rows, 40x56)
    idle_sheet = Image.new("RGBA", (40 * 4, 56 * 4), (0, 0, 0, 0))
    for r in range(4):
        for c in range(4):
            f = draw_refined_swordsman_frame(r, "idle", c, 40, 56)
            idle_sheet.paste(f, (c * 40, r * 56), f)
    idle_path = os.path.join(art_dir, "swordsman", "swordsman_idle.png")
    idle_sheet.save(idle_path)
    print(f"  -> Generated: {idle_path} ({idle_sheet.size})")

    # Walk (8 cols x 4 rows, 40x56)
    walk_sheet = Image.new("RGBA", (40 * 8, 56 * 4), (0, 0, 0, 0))
    for r in range(4):
        for c in range(8):
            f = draw_refined_swordsman_frame(r, "walk", c, 40, 56)
            walk_sheet.paste(f, (c * 40, r * 56), f)
    walk_path = os.path.join(art_dir, "swordsman", "swordsman_walk.png")
    walk_sheet.save(walk_path)
    print(f"  -> Generated: {walk_path} ({walk_sheet.size})")

    # Attack (6 cols x 4 rows, 56x56)
    atk_sheet = Image.new("RGBA", (56 * 6, 56 * 4), (0, 0, 0, 0))
    for r in range(4):
        for c in range(6):
            f = draw_refined_swordsman_attack_frame(r, c, 56, 56)
            atk_sheet.paste(f, (c * 56, r * 56), f)
    atk_path = os.path.join(art_dir, "swordsman", "swordsman_attack.png")
    atk_sheet.save(atk_path)
    print(f"  -> Generated: {atk_path} ({atk_sheet.size})")

    print("\n🛡️ Rendering Refined Option B Heavy Shield Guard...")
    # Idle (4 cols x 4 rows, 44x58)
    sg_idle = Image.new("RGBA", (44 * 4, 58 * 4), (0, 0, 0, 0))
    for r in range(4):
        for c in range(4):
            f = draw_refined_shield_guard_frame(r, "idle", c, 44, 58)
            sg_idle.paste(f, (c * 44, r * 58), f)
    sg_idle_path = os.path.join(art_dir, "shield_guard", "shield_guard_idle.png")
    sg_idle.save(sg_idle_path)
    print(f"  -> Generated: {sg_idle_path} ({sg_idle.size})")

    # Walk (8 cols x 4 rows, 44x58)
    sg_walk = Image.new("RGBA", (44 * 8, 58 * 4), (0, 0, 0, 0))
    for r in range(4):
        for c in range(8):
            f = draw_refined_shield_guard_frame(r, "walk", c, 44, 58)
            sg_walk.paste(f, (c * 44, r * 58), f)
    sg_walk_path = os.path.join(art_dir, "shield_guard", "shield_guard_walk.png")
    sg_walk.save(sg_walk_path)
    print(f"  -> Generated: {sg_walk_path} ({sg_walk.size})")

    # Attack (6 cols x 4 rows, 60x58)
    sg_atk = Image.new("RGBA", (60 * 6, 58 * 4), (0, 0, 0, 0))
    for r in range(4):
        for c in range(6):
            f = draw_refined_shield_guard_attack_frame(r, c, 60, 58)
            sg_atk.paste(f, (c * 60, r * 58), f)
    sg_atk_path = os.path.join(art_dir, "shield_guard", "shield_guard_attack.png")
    sg_atk.save(sg_atk_path)
    print(f"  -> Generated: {sg_atk_path} ({sg_atk.size})")

if __name__ == "__main__":
    build_c1_enemy_assets()
