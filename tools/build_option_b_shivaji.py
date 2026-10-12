import os
import math
from PIL import Image, ImageDraw

# Master Option B Color Palette Tokens
C = {
    "NONE": (0, 0, 0, 0),
    "OUTLINE": (26, 20, 18, 255),
    "SHADOW_GROUND": (15, 12, 10, 110),
    # Skin
    "SKIN_HI": (235, 178, 128, 255),
    "SKIN_BASE": (198, 134, 66, 255),
    "SKIN_SHADOW": (141, 91, 45, 255),
    "SKIN_DEEP": (95, 58, 28, 255),
    # Hair / Beard
    "HAIR_BASE": (28, 25, 23, 255),
    "HAIR_HI": (44, 40, 38, 255),
    "EYE_WHITE": (250, 245, 240, 255),
    "EYE_DARK": (15, 15, 15, 255),
    "TIKKA_RED": (220, 38, 38, 255),
    # Pheta (Turban)
    "PHETA_RED": (185, 28, 28, 255),
    "PHETA_RED_DARK": (127, 29, 29, 255),
    "PHETA_RED_DEEP": (75, 16, 16, 255),
    "SAFFRON_HI": (245, 158, 11, 255),
    "SAFFRON_BASE": (230, 96, 18, 255),
    "SAFFRON_DARK": (180, 83, 9, 255),
    "SAFFRON_DEEP": (120, 53, 15, 255),
    # Gold & Jewels
    "GOLD_HI": (254, 240, 138, 255),
    "GOLD_BASE": (251, 191, 36, 255),
    "GOLD_DARK": (217, 119, 6, 255),
    "GOLD_DEEP": (146, 64, 14, 255),
    "PEARL": (255, 255, 255, 255),
    "RUBY": (190, 18, 60, 255),
    # Angarkha (Tunic)
    "ANGARKHA_HI": (254, 243, 199, 255),
    "ANGARKHA_BASE": (245, 232, 180, 255),
    "ANGARKHA_SHADOW": (214, 195, 142, 255),
    "ANGARKHA_DARK": (175, 155, 105, 255),
    # Churidar
    "CHURIDAR_BASE": (235, 222, 180, 255),
    "CHURIDAR_SHADOW": (190, 175, 135, 255),
    # Footwear (Mojari) & Leather
    "MOJARI_HI": (120, 53, 15, 255),
    "MOJARI_BASE": (69, 26, 3, 255),
    "MOJARI_DARK": (45, 16, 2, 255),
    "LEATHER_HI": (120, 53, 15, 255),
    "LEATHER_BASE": (69, 26, 3, 255),
    "LEATHER_DARK": (45, 16, 2, 255),
    # Talwar & Steel
    "STEEL_GLINT": (255, 255, 255, 255),
    "STEEL_HI": (226, 232, 240, 255),
    "STEEL_BASE": (148, 163, 184, 255),
    "STEEL_DARK": (71, 85, 105, 255),
    "STEEL_DEEP": (30, 41, 59, 255),
    # VFX Sword Slash
    "SLASH_CORE": (255, 255, 255, 245),
    "SLASH_GOLD": (251, 191, 36, 220),
    "SLASH_ORANGE": (249, 115, 22, 180),
    "SLASH_FADE": (234, 88, 12, 100),
}

def create_palette_swatch_image(output_path):
    """Generates the official Option B master color swatch image."""
    swatches = [
        ("SAFFRON_BASE", C["SAFFRON_BASE"]), ("SAFFRON_HI", C["SAFFRON_HI"]), ("SAFFRON_DARK", C["SAFFRON_DARK"]),
        ("PHETA_RED", C["PHETA_RED"]), ("PHETA_RED_DARK", C["PHETA_RED_DARK"]), ("RUBY", C["RUBY"]),
        ("GOLD_BASE", C["GOLD_BASE"]), ("GOLD_HI", C["GOLD_HI"]), ("GOLD_DARK", C["GOLD_DARK"]),
        ("ANGARKHA_BASE", C["ANGARKHA_BASE"]), ("ANGARKHA_HI", C["ANGARKHA_HI"]), ("ANGARKHA_DARK", C["ANGARKHA_DARK"]),
        ("SKIN_BASE", C["SKIN_BASE"]), ("SKIN_HI", C["SKIN_HI"]), ("SKIN_SHADOW", C["SKIN_SHADOW"]),
        ("HAIR_BASE", C["HAIR_BASE"]), ("MOJARI_BASE", C["MOJARI_BASE"]), ("STEEL_HI", C["STEEL_HI"]),
        ("STEEL_BASE", C["STEEL_BASE"]), ("STEEL_DARK", C["STEEL_DARK"])
    ]
    img = Image.new("RGBA", (320, 160), (20, 16, 14, 255))
    draw = ImageDraw.Draw(img)
    cell_w, cell_h = 32, 32
    cols = 8
    for i, (name, col) in enumerate(swatches):
        r = i // cols
        c_idx = i % cols
        x = 16 + c_idx * 36
        y = 16 + r * 46
        draw.rectangle([x-1, y-1, x + cell_w + 1, y + cell_h + 1], fill=(45, 30, 20, 255))
        draw.rectangle([x, y, x + cell_w, y + cell_h], fill=col)
    img.save(output_path)
    print(f"Generated master palette swatch: {output_path}")

def draw_pixel_rect(draw, x1, y1, x2, y2, color):
    rx1, rx2 = round(min(x1, x2)), round(max(x1, x2))
    ry1, ry2 = round(min(y1, y2)), round(max(y1, y2))
    draw.rectangle([rx1, ry1, rx2, ry2], fill=color)

def draw_ellipse_soft(draw, cx, cy, rx, ry, color):
    draw.ellipse([round(cx - rx), round(cy - ry), round(cx + rx), round(cy + ry)], fill=color)

def draw_shivaji_frame(direction, anim_type, frame_idx, total_frames, cell_w=48, cell_h=64):
    """
    Renders an authentic, highly detailed 32-bit pixel art frame of Chhatrapati Shivaji Maharaj.
    direction: 0=South (Front), 1=North (Back), 2=East (Right), 3=West (Left)
    cell_w x cell_h: 48 x 64 (or 64 x 64 for attack)
    """
    img = Image.new("RGBA", (cell_w, cell_h), C["NONE"])
    draw = ImageDraw.Draw(img)

    # Base positioning & offsets
    cx = cell_w // 2
    cy_base = 58  # Ground contact plane

    # Animation Cycle Offsets
    bob_y = 0
    stride = 0
    arm_swing = 0
    turban_tilt = 0

    if anim_type == "idle":
        # 4-frame subtle breathing cycle
        # frame 0: neutral, 1: inhale rise, 2: peak, 3: exhale
        cycle = [0, -1, -1, 0]
        bob_y = cycle[frame_idx % 4]
        turban_tilt = 1 if frame_idx == 2 else 0

    elif anim_type == "walk":
        # 8-frame natural stride
        # bob goes down on contact (f0, f4), up on pass (f2, f6)
        bobs = [0, 1, 0, -1, 0, 1, 0, -1]
        bob_y = bobs[frame_idx % 8]
        # stride parameter: positive = right foot forward, negative = left foot forward
        strides = [3, 2, 0, -2, -3, -2, 0, 2]
        stride = strides[frame_idx % 8]
        arm_swing = -stride

    elif anim_type == "attack":
        # Attack anim has 6 frames
        pass

    # 1. Soft Ground Shadow
    shadow_rx = 13 if anim_type != "attack" else 15
    shadow_ry = 4
    draw_ellipse_soft(draw, cx, cy_base, shadow_rx, shadow_ry, C["SHADOW_GROUND"])

    # 2. Footwear & Legs (Mojari & Churidar)
    leg_y_top = 46 + bob_y
    leg_y_bot = 56 + bob_y

    if direction == 0:  # SOUTH (Facing Front)
        l_foot_x = cx - 5 + (stride if anim_type == "walk" else 0)
        r_foot_x = cx + 5 - (stride if anim_type == "walk" else 0)
        l_foot_y = leg_y_bot
        r_foot_y = leg_y_bot

        # Churidar Trousers
        draw_pixel_rect(draw, cx - 6, leg_y_top, cx - 2, leg_y_bot - 1, C["CHURIDAR_BASE"])
        draw_pixel_rect(draw, cx + 2, leg_y_top, cx + 6, leg_y_bot - 1, C["CHURIDAR_BASE"])
        draw_pixel_rect(draw, cx - 6, leg_y_top + 4, cx - 4, leg_y_bot - 1, C["CHURIDAR_SHADOW"])
        draw_pixel_rect(draw, cx + 4, leg_y_top + 4, cx + 6, leg_y_bot - 1, C["CHURIDAR_SHADOW"])

        # Leather Mojari Shoes with pointed curved tip
        draw_pixel_rect(draw, l_foot_x - 3, l_foot_y, l_foot_x + 2, l_foot_y + 2, C["MOJARI_BASE"])
        draw_pixel_rect(draw, l_foot_x - 4, l_foot_y + 1, l_foot_x - 3, l_foot_y + 2, C["MOJARI_HI"])  # Curled toe
        draw_pixel_rect(draw, r_foot_x - 2, r_foot_y, r_foot_x + 3, r_foot_y + 2, C["MOJARI_BASE"])
        draw_pixel_rect(draw, r_foot_x + 3, r_foot_y + 1, r_foot_x + 4, r_foot_y + 2, C["MOJARI_HI"])

    elif direction == 1:  # NORTH (Facing Back)
        l_foot_x = cx - 5 - (stride if anim_type == "walk" else 0)
        r_foot_x = cx + 5 + (stride if anim_type == "walk" else 0)
        draw_pixel_rect(draw, cx - 6, leg_y_top, cx - 2, leg_y_bot - 1, C["CHURIDAR_SHADOW"])
        draw_pixel_rect(draw, cx + 2, leg_y_top, cx + 6, leg_y_bot - 1, C["CHURIDAR_SHADOW"])
        draw_pixel_rect(draw, l_foot_x - 3, leg_y_bot, l_foot_x + 2, leg_y_bot + 2, C["MOJARI_DARK"])
        draw_pixel_rect(draw, r_foot_x - 2, leg_y_bot, r_foot_x + 3, leg_y_bot + 2, C["MOJARI_DARK"])

    elif direction in (2, 3):  # EAST (2) / WEST (3)
        sign = 1 if direction == 2 else -1
        f_x1 = cx - 3 + (stride * sign if anim_type == "walk" else 0)
        f_x2 = cx + 3 - (stride * sign if anim_type == "walk" else 0)
        draw_pixel_rect(draw, min(f_x1, f_x2) - 2, leg_y_top, max(f_x1, f_x2) + 2, leg_y_bot - 1, C["CHURIDAR_BASE"])
        draw_pixel_rect(draw, f_x1 - 3, leg_y_bot, f_x1 + 3, leg_y_bot + 2, C["MOJARI_BASE"])
        # Toe curve in travel direction
        draw_pixel_rect(draw, f_x1 + 3 * sign, leg_y_bot + 1, f_x1 + 4 * sign, leg_y_bot + 2, C["MOJARI_HI"])
        draw_pixel_rect(draw, f_x2 - 2, leg_y_bot, f_x2 + 2, leg_y_bot + 2, C["MOJARI_DARK"])

    # 3. Royal Angarkha Skirt / Pleats
    skirt_top = 34 + bob_y
    skirt_bot = 48 + bob_y
    skirt_sway = stride // 2 if anim_type == "walk" else 0

    if direction == 0:  # South
        # Saffron & Cream Pleated flare
        draw_pixel_rect(draw, cx - 9, skirt_top, cx + 9, skirt_bot, C["ANGARKHA_BASE"])
        # Deep folds
        draw_pixel_rect(draw, cx - 9, skirt_top + 2, cx - 7, skirt_bot, C["ANGARKHA_SHADOW"])
        draw_pixel_rect(draw, cx + 7, skirt_top + 2, cx + 9, skirt_bot, C["ANGARKHA_SHADOW"])
        draw_pixel_rect(draw, cx - 2, skirt_top + 4, cx - 1, skirt_bot, C["ANGARKHA_SHADOW"])
        draw_pixel_rect(draw, cx + 1, skirt_top + 4, cx + 2, skirt_bot, C["ANGARKHA_SHADOW"])
        # Golden Embroidered Hem Border
        draw_pixel_rect(draw, cx - 9, skirt_bot - 1, cx + 9, skirt_bot, C["GOLD_BASE"])
        draw_pixel_rect(draw, cx - 8, skirt_bot - 2, cx + 8, skirt_bot - 2, C["SAFFRON_BASE"])

    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 9, skirt_top, cx + 9, skirt_bot, C["ANGARKHA_SHADOW"])
        draw_pixel_rect(draw, cx - 9, skirt_bot - 1, cx + 9, skirt_bot, C["GOLD_DARK"])

    elif direction in (2, 3):  # East / West
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 7 + skirt_sway, skirt_top, cx + 7 + skirt_sway, skirt_bot, C["ANGARKHA_BASE"])
        draw_pixel_rect(draw, cx - 7 * sign + skirt_sway, skirt_top, cx - 4 * sign + skirt_sway, skirt_bot, C["ANGARKHA_SHADOW"])
        draw_pixel_rect(draw, cx - 7 + skirt_sway, skirt_bot - 1, cx + 7 + skirt_sway, skirt_bot, C["GOLD_BASE"])

    # 4. Waist Kamarbandh (Rich Sash with Gold Trim & Draped Tails)
    sash_y = 31 + bob_y
    sash_h = 5
    if direction == 0:  # South
        draw_pixel_rect(draw, cx - 8, sash_y, cx + 8, sash_y + sash_h, C["SAFFRON_BASE"])
        draw_pixel_rect(draw, cx - 8, sash_y + 1, cx + 8, sash_y + 2, C["GOLD_BASE"])
        draw_pixel_rect(draw, cx - 8, sash_y + sash_h - 1, cx + 8, sash_y + sash_h, C["SAFFRON_DARK"])
        # Draped sash ribbon hanging down on right hip
        draw_pixel_rect(draw, cx + 4, sash_y + sash_h, cx + 7, sash_y + sash_h + 7, C["SAFFRON_BASE"])
        draw_pixel_rect(draw, cx + 4, sash_y + sash_h + 6, cx + 7, sash_y + sash_h + 7, C["GOLD_BASE"])

    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 8, sash_y, cx + 8, sash_y + sash_h, C["SAFFRON_DARK"])
        draw_pixel_rect(draw, cx - 8, sash_y + 1, cx + 8, sash_y + 2, C["GOLD_DARK"])

    elif direction in (2, 3):
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 7, sash_y, cx + 7, sash_y + sash_h, C["SAFFRON_BASE"])
        draw_pixel_rect(draw, cx - 7, sash_y + 1, cx + 7, sash_y + 2, C["GOLD_BASE"])
        # Sash tail flutter
        draw_pixel_rect(draw, cx - 4 * sign, sash_y + sash_h, cx - 1 * sign, sash_y + sash_h + 6, C["SAFFRON_BASE"])

    # 5. Sheathed Talwar at Hip (when not attacking)
    if anim_type != "attack":
        if direction in (0, 2):  # South or East (Sword on left hip, visible)
            sword_x = cx - 8
            sword_y = sash_y + 2
            # Golden Spiked Basket Hilt & Pommel
            draw_pixel_rect(draw, sword_x - 3, sword_y - 4, sword_x + 1, sword_y - 2, C["GOLD_BASE"])
            draw_pixel_rect(draw, sword_x - 1, sword_y - 6, sword_x, sword_y - 4, C["STEEL_GLINT"])  # Spike
            # Curved Scabbard extending down-back
            draw_pixel_rect(draw, sword_x - 2, sword_y - 1, sword_x, sword_y + 2, C["LEATHER_BASE"])
            draw_pixel_rect(draw, sword_x - 3, sword_y + 3, sword_x - 1, sword_y + 8, C["LEATHER_BASE"])
            draw_pixel_rect(draw, sword_x - 4, sword_y + 9, sword_x - 2, sword_y + 13, C["LEATHER_BASE"])
            draw_pixel_rect(draw, sword_x - 4, sword_y + 12, sword_x - 2, sword_y + 14, C["GOLD_DARK"])  # Chape tip
        elif direction == 3:  # West (facing left, hilt on near hip)
            sword_x = cx + 5
            sword_y = sash_y + 2
            draw_pixel_rect(draw, sword_x - 1, sword_y - 4, sword_x + 3, sword_y - 2, C["GOLD_BASE"])
            draw_pixel_rect(draw, sword_x + 1, sword_y - 6, sword_x + 2, sword_y - 4, C["STEEL_GLINT"])
            draw_pixel_rect(draw, sword_x, sword_y - 1, sword_x + 2, sword_y + 2, C["LEATHER_BASE"])
            draw_pixel_rect(draw, sword_x + 1, sword_y + 3, sword_x + 3, sword_y + 8, C["LEATHER_BASE"])
            draw_pixel_rect(draw, sword_x + 2, sword_y + 9, sword_x + 4, sword_y + 13, C["LEATHER_BASE"])

    # 6. Upper Torso & Angarkha (Fitted Royal Jacket)
    torso_top = 20 + bob_y
    torso_bot = sash_y
    if direction == 0:  # South
        draw_pixel_rect(draw, cx - 8, torso_top, cx + 8, torso_bot, C["ANGARKHA_BASE"])
        # Right-side diagonal overlap (Purdah angarkha closure)
        draw_pixel_rect(draw, cx - 2, torso_top, cx + 4, torso_bot, C["ANGARKHA_HI"])
        draw_pixel_rect(draw, cx + 4, torso_top, cx + 5, torso_bot, C["GOLD_BASE"])  # Gold piping
        # Royal Pearl and Ruby Necklace (Kanthi)
        draw_pixel_rect(draw, cx - 5, torso_top + 2, cx - 4, torso_top + 4, C["PEARL"])
        draw_pixel_rect(draw, cx + 4, torso_top + 2, cx + 5, torso_top + 4, C["PEARL"])
        draw_pixel_rect(draw, cx - 3, torso_top + 5, cx + 3, torso_top + 6, C["PEARL"])
        draw_pixel_rect(draw, cx - 1, torso_top + 6, cx + 1, torso_top + 8, C["RUBY"])  # Royal pendant brooch
        # Sleeves & Arms
        draw_pixel_rect(draw, cx - 10, torso_top + 2, cx - 8, torso_top + 10 + arm_swing, C["ANGARKHA_BASE"])
        draw_pixel_rect(draw, cx + 8, torso_top + 2, cx + 10, torso_top + 10 - arm_swing, C["ANGARKHA_BASE"])
        # Hands (resting on hilt / belt)
        draw_pixel_rect(draw, cx - 10, torso_top + 10 + arm_swing, cx - 8, torso_top + 12 + arm_swing, C["SKIN_BASE"])
        draw_pixel_rect(draw, cx + 8, torso_top + 10 - arm_swing, cx + 10, torso_top + 12 - arm_swing, C["SKIN_BASE"])

    elif direction == 1:  # North
        draw_pixel_rect(draw, cx - 8, torso_top, cx + 8, torso_bot, C["ANGARKHA_SHADOW"])
        draw_pixel_rect(draw, cx - 10, torso_top + 2, cx - 8, torso_top + 10 - arm_swing, C["ANGARKHA_SHADOW"])
        draw_pixel_rect(draw, cx + 8, torso_top + 2, cx + 10, torso_top + 10 + arm_swing, C["ANGARKHA_SHADOW"])

    elif direction in (2, 3):  # East / West
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 6, torso_top, cx + 6, torso_bot, C["ANGARKHA_BASE"])
        draw_pixel_rect(draw, cx + 2 * sign, torso_top, cx + 4 * sign, torso_bot, C["ANGARKHA_HI"])
        # Near arm
        draw_pixel_rect(draw, cx - 2 * sign, torso_top + 2, cx + 1 * sign, torso_top + 11 + arm_swing * sign, C["ANGARKHA_BASE"])
        draw_pixel_rect(draw, cx - 2 * sign, torso_top + 11 + arm_swing * sign, cx + 1 * sign, torso_top + 13 + arm_swing * sign, C["SKIN_BASE"])

    # 7. Head, Face & Regal Features
    head_y = 11 + bob_y
    head_h = 10
    if direction == 0:  # South (Front Face)
        # Face base
        draw_pixel_rect(draw, cx - 5, head_y, cx + 5, head_y + head_h, C["SKIN_BASE"])
        draw_pixel_rect(draw, cx - 4, head_y + 1, cx + 4, head_y + 4, C["SKIN_HI"])  # Brow highlight
        # Eyes
        draw_pixel_rect(draw, cx - 4, head_y + 3, cx - 2, head_y + 4, C["EYE_WHITE"])
        draw_pixel_rect(draw, cx - 3, head_y + 3, cx - 2, head_y + 4, C["EYE_DARK"])
        draw_pixel_rect(draw, cx + 2, head_y + 3, cx + 4, head_y + 4, C["EYE_WHITE"])
        draw_pixel_rect(draw, cx + 2, head_y + 3, cx + 3, head_y + 4, C["EYE_DARK"])
        # Forehead Chandrakor Tikka (Crescent symbol)
        draw_pixel_rect(draw, cx - 1, head_y + 1, cx + 1, head_y + 2, C["TIKKA_RED"])
        # Nose bridge
        draw_pixel_rect(draw, cx, head_y + 3, cx, head_y + 5, C["SKIN_SHADOW"])
        # Iconic Upturned Moustache
        draw_pixel_rect(draw, cx - 5, head_y + 6, cx + 5, head_y + 7, C["HAIR_BASE"])
        draw_pixel_rect(draw, cx - 6, head_y + 5, cx - 5, head_y + 6, C["HAIR_BASE"])  # Upturned tip L
        draw_pixel_rect(draw, cx + 5, head_y + 5, cx + 6, head_y + 6, C["HAIR_BASE"])  # Upturned tip R
        # Neat Maratha Trimmed Beard & Chin
        draw_pixel_rect(draw, cx - 4, head_y + 8, cx + 4, head_y + head_h, C["HAIR_BASE"])
        draw_pixel_rect(draw, cx - 2, head_y + head_h, cx + 2, head_y + head_h + 1, C["HAIR_BASE"])

    elif direction == 1:  # North (Back of Head)
        draw_pixel_rect(draw, cx - 5, head_y, cx + 5, head_y + head_h, C["HAIR_BASE"])
        draw_pixel_rect(draw, cx - 4, head_y + 7, cx + 4, head_y + head_h + 1, C["SKIN_SHADOW"])  # Neck

    elif direction in (2, 3):  # East / West Profile
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 4, head_y, cx + 4, head_y + head_h, C["SKIN_BASE"])
        # Nose profile extending outward
        draw_pixel_rect(draw, cx + 4 * sign, head_y + 3, cx + 6 * sign, head_y + 5, C["SKIN_BASE"])
        draw_pixel_rect(draw, cx + 2 * sign, head_y + 3, cx + 3 * sign, head_y + 4, C["EYE_DARK"])
        # Moustache profile
        draw_pixel_rect(draw, cx + 1 * sign, head_y + 6, cx + 6 * sign, head_y + 7, C["HAIR_BASE"])
        draw_pixel_rect(draw, cx + 5 * sign, head_y + 5, cx + 6 * sign, head_y + 6, C["HAIR_BASE"])
        # Beard & jawline
        draw_pixel_rect(draw, cx - 2 * sign, head_y + 7, cx + 4 * sign, head_y + head_h, C["HAIR_BASE"])

    # 8. Chhatrapati Pheta (Crimson Turban with Saffron Folds & Golden Sirpech Plume)
    turban_y = 2 + bob_y
    turban_h = 11

    if direction == 0:  # South (Front Turban)
        # Main Turban Dome
        draw_pixel_rect(draw, cx - 7, turban_y + 2, cx + 7, turban_y + turban_h, C["PHETA_RED"])
        # Saffron Overlapping Wraps
        draw_pixel_rect(draw, cx - 7, turban_y + 4, cx + 7, turban_y + 6, C["SAFFRON_BASE"])
        draw_pixel_rect(draw, cx - 6, turban_y + 7, cx + 6, turban_y + 8, C["SAFFRON_HI"])
        draw_pixel_rect(draw, cx - 7, turban_y + turban_h - 1, cx + 7, turban_y + turban_h, C["PHETA_RED_DARK"])
        # Crown fan crest (Turra)
        draw_pixel_rect(draw, cx - 3 + turban_tilt, turban_y, cx + 4 + turban_tilt, turban_y + 3, C["SAFFRON_HI"])
        # Golden Sirpech Brooch (Left brow) with Ruby Setting
        sirpech_x = cx - 4 + turban_tilt
        draw_pixel_rect(draw, sirpech_x - 1, turban_y + 3, sirpech_x + 2, turban_y + 7, C["GOLD_BASE"])
        draw_pixel_rect(draw, sirpech_x, turban_y + 4, sirpech_x + 1, turban_y + 5, C["RUBY"])
        # Rising Sirpech Plume (Kalgi feather)
        draw_pixel_rect(draw, sirpech_x, turban_y - 2, sirpech_x + 1, turban_y + 3, C["PEARL"])
        draw_pixel_rect(draw, sirpech_x + 1, turban_y - 1, sirpech_x + 2, turban_y + 1, C["GOLD_HI"])
        # Hanging Pearl Strand
        draw_pixel_rect(draw, sirpech_x - 1, turban_y + 7, sirpech_x, turban_y + 10, C["PEARL"])

    elif direction == 1:  # North (Back of Turban with Pleated Fan Tail)
        draw_pixel_rect(draw, cx - 7, turban_y + 2, cx + 7, turban_y + turban_h, C["PHETA_RED_DARK"])
        draw_pixel_rect(draw, cx - 6, turban_y + 4, cx + 6, turban_y + 6, C["SAFFRON_DARK"])
        # Pleated tail (Shimli) hanging down neck
        draw_pixel_rect(draw, cx - 2, turban_y + turban_h, cx + 3, turban_y + turban_h + 8, C["SAFFRON_BASE"])
        draw_pixel_rect(draw, cx - 2, turban_y + turban_h + 7, cx + 3, turban_y + turban_h + 8, C["GOLD_BASE"])

    elif direction in (2, 3):  # East / West Profile Turban
        sign = 1 if direction == 2 else -1
        draw_pixel_rect(draw, cx - 6, turban_y + 2, cx + 6, turban_y + turban_h, C["PHETA_RED"])
        draw_pixel_rect(draw, cx - 5, turban_y + 4, cx + 5, turban_y + 7, C["SAFFRON_BASE"])
        # Plume on front-facing side
        plume_x = cx + 2 * sign
        draw_pixel_rect(draw, plume_x, turban_y - 2, plume_x + 1, turban_y + 4, C["PEARL"])
        draw_pixel_rect(draw, plume_x - 1 * sign, turban_y + 3, plume_x + 1 * sign, turban_y + 6, C["GOLD_BASE"])

    return img

def draw_shivaji_attack_frame(direction, frame_idx, cell_size=64):
    """
    Renders Shivaji's 6-frame sword attack in the chosen direction on a 64x64 cell.
    Frames:
    0: Anticipation / Stance Draw
    1: Deep Windup (talwar raised back, stance coiled)
    2: Apex Windup / Telegraph Gleam
    3: Active Strike Phase (explosive slash + brilliant arc)
    4: Follow-Through (extended blade tip, fading trail)
    5: Recovery into guard
    """
    img = Image.new("RGBA", (cell_size, cell_size), C["NONE"])
    draw = ImageDraw.Draw(img)

    cx = cell_size // 2
    cy_base = 58
    # Render shadow
    draw_ellipse_soft(draw, cx, cy_base, 16, 5, C["SHADOW_GROUND"])

    # Draw body base with attack stance adjustments
    # Let's render the body slightly shifted based on attack momentum
    shift_x = 0
    shift_y = 0
    if direction == 0:  # South
        shift_y = 1 if frame_idx in (2, 3) else 0
    elif direction == 1:  # North
        shift_y = -1 if frame_idx in (2, 3) else 0
    elif direction == 2:  # East
        shift_x = 3 if frame_idx in (3, 4) else (-1 if frame_idx == 1 else 0)
    elif direction == 3:  # West
        shift_x = -3 if frame_idx in (3, 4) else (1 if frame_idx == 1 else 0)

    # Use base drawing logic into a temporary 48x64 buffer and blit
    base_body = draw_shivaji_frame(direction, "attack", frame_idx, 6, cell_w=48, cell_h=64)
    # Paste base body onto 64x64 canvas centered at (8 + shift_x, shift_y)
    img.paste(base_body, (8 + shift_x, shift_y), base_body)

    # Now draw the active Talwar and luminous slash arc on the 64x64 canvas!
    blade_len = 16

    if direction == 0:  # SOUTH ATTACK (Slashing Down-Forward)
        hand_x = cx + shift_x
        hand_y = 36 + shift_y

        if frame_idx == 0:  # Draw anticipation
            draw_pixel_rect(draw, hand_x - 8, hand_y - 6, hand_x - 5, hand_y - 4, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x - 12, hand_y - 12, hand_x - 8, hand_y - 6, C["STEEL_HI"])
        elif frame_idx in (1, 2):  # Overhead Windup
            draw_pixel_rect(draw, hand_x - 4, hand_y - 12, hand_x - 1, hand_y - 10, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x - 2, hand_y - 24, hand_x + 1, hand_y - 12, C["STEEL_GLINT"])
            if frame_idx == 2:  # Telegraph glint
                draw_ellipse_soft(draw, hand_x, hand_y - 24, 4, 4, C["GOLD_HI"])
                draw_pixel_rect(draw, hand_x - 1, hand_y - 25, hand_x + 1, hand_y - 23, C["PEARL"])
        elif frame_idx == 3:  # Explosive Downward Cleave
            draw_pixel_rect(draw, hand_x - 4, hand_y + 2, hand_x - 1, hand_y + 4, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x - 2, hand_y + 4, hand_x + 1, hand_y + 18, C["STEEL_GLINT"])
            # Crescent Slash Arc VFX
            draw.arc([cx - 20, cy_base - 28, cx + 20, cy_base + 4], start=20, end=160, fill=C["SLASH_CORE"], width=3)
            draw.arc([cx - 22, cy_base - 30, cx + 22, cy_base + 6], start=15, end=165, fill=C["SLASH_GOLD"], width=2)
            draw.arc([cx - 24, cy_base - 32, cx + 24, cy_base + 8], start=10, end=170, fill=C["SLASH_ORANGE"], width=2)
        elif frame_idx == 4:  # Follow through
            draw_pixel_rect(draw, hand_x - 4, hand_y + 4, hand_x - 1, hand_y + 6, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x - 1, hand_y + 6, hand_x + 2, hand_y + 16, C["STEEL_BASE"])
            draw.arc([cx - 18, cy_base - 22, cx + 18, cy_base + 2], start=40, end=140, fill=C["SLASH_FADE"], width=2)
        elif frame_idx == 5:  # Recovery into guard
            draw_pixel_rect(draw, hand_x - 6, hand_y - 2, hand_x - 3, hand_y, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x - 5, hand_y, hand_x - 1, hand_y + 10, C["STEEL_BASE"])

    elif direction == 1:  # NORTH ATTACK (Slashing Upward)
        hand_x = cx + shift_x
        hand_y = 30 + shift_y

        if frame_idx in (1, 2):
            draw_pixel_rect(draw, hand_x + 4, hand_y + 4, hand_x + 7, hand_y + 6, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x + 6, hand_y + 6, hand_x + 9, hand_y + 16, C["STEEL_BASE"])
        elif frame_idx == 3:  # Upward Strike
            draw_pixel_rect(draw, hand_x + 2, hand_y - 8, hand_x + 5, hand_y - 6, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x + 3, hand_y - 22, hand_x + 6, hand_y - 8, C["STEEL_GLINT"])
            # Arc above head
            draw.arc([cx - 20, 4, cx + 20, 36], start=200, end=340, fill=C["SLASH_CORE"], width=3)
            draw.arc([cx - 22, 2, cx + 22, 38], start=195, end=345, fill=C["SLASH_GOLD"], width=2)
        elif frame_idx == 4:
            draw_pixel_rect(draw, hand_x + 2, hand_y - 6, hand_x + 5, hand_y - 4, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x + 3, hand_y - 18, hand_x + 5, hand_y - 6, C["STEEL_BASE"])
            draw.arc([cx - 16, 8, cx + 16, 32], start=210, end=330, fill=C["SLASH_FADE"], width=2)
        elif frame_idx == 5:
            draw_pixel_rect(draw, hand_x + 2, hand_y, hand_x + 5, hand_y + 2, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x + 3, hand_y + 2, hand_x + 5, hand_y + 10, C["STEEL_BASE"])

    elif direction == 2:  # EAST ATTACK (Lunge & Horizontal Slash Right)
        hand_x = cx + shift_x + 6
        hand_y = 34 + shift_y

        if frame_idx in (1, 2):  # Coiled back
            draw_pixel_rect(draw, hand_x - 14, hand_y - 2, hand_x - 11, hand_y, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x - 26, hand_y - 1, hand_x - 14, hand_y + 2, C["STEEL_BASE"])
            if frame_idx == 2:
                draw_ellipse_soft(draw, hand_x - 26, hand_y, 4, 4, C["GOLD_HI"])
        elif frame_idx == 3:  # Sweeping Forward Thrust
            draw_pixel_rect(draw, hand_x, hand_y - 2, hand_x + 3, hand_y, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x + 3, hand_y - 2, hand_x + 22, hand_y + 1, C["STEEL_GLINT"])
            # Horizontal Arc VFX
            draw.arc([cx - 4, cy_base - 40, cx + 32, cy_base - 4], start=280, end=80, fill=C["SLASH_CORE"], width=3)
            draw.arc([cx - 6, cy_base - 42, cx + 34, cy_base - 2], start=275, end=85, fill=C["SLASH_GOLD"], width=2)
            draw.arc([cx - 8, cy_base - 44, cx + 36, cy_base], start=270, end=90, fill=C["SLASH_ORANGE"], width=2)
        elif frame_idx == 4:
            draw_pixel_rect(draw, hand_x - 2, hand_y - 1, hand_x + 1, hand_y + 1, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x + 1, hand_y - 1, hand_x + 18, hand_y + 1, C["STEEL_BASE"])
            draw.arc([cx, cy_base - 36, cx + 30, cy_base - 8], start=290, end=70, fill=C["SLASH_FADE"], width=2)
        elif frame_idx == 5:
            draw_pixel_rect(draw, hand_x - 4, hand_y, hand_x - 1, hand_y + 2, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x - 1, hand_y + 1, hand_x + 10, hand_y + 3, C["STEEL_BASE"])

    elif direction == 3:  # WEST ATTACK (Mirrored Left)
        hand_x = cx + shift_x - 6
        hand_y = 34 + shift_y

        if frame_idx in (1, 2):
            draw_pixel_rect(draw, hand_x + 11, hand_y - 2, hand_x + 14, hand_y, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x + 14, hand_y - 1, hand_x + 26, hand_y + 2, C["STEEL_BASE"])
            if frame_idx == 2:
                draw_ellipse_soft(draw, hand_x + 26, hand_y, 4, 4, C["GOLD_HI"])
        elif frame_idx == 3:
            draw_pixel_rect(draw, hand_x - 3, hand_y - 2, hand_x, hand_y, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x - 22, hand_y - 2, hand_x - 3, hand_y + 1, C["STEEL_GLINT"])
            # Left Arc
            draw.arc([cx - 32, cy_base - 40, cx + 4, cy_base - 4], start=100, end=260, fill=C["SLASH_CORE"], width=3)
            draw.arc([cx - 34, cy_base - 42, cx + 6, cy_base - 2], start=95, end=265, fill=C["SLASH_GOLD"], width=2)
            draw.arc([cx - 36, cy_base - 44, cx + 8, cy_base], start=90, end=270, fill=C["SLASH_ORANGE"], width=2)
        elif frame_idx == 4:
            draw_pixel_rect(draw, hand_x - 1, hand_y - 1, hand_x + 2, hand_y + 1, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x - 18, hand_y - 1, hand_x - 1, hand_y + 1, C["STEEL_BASE"])
            draw.arc([cx - 30, cy_base - 36, cx, cy_base - 8], start=110, end=250, fill=C["SLASH_FADE"], width=2)
        elif frame_idx == 5:
            draw_pixel_rect(draw, hand_x + 1, hand_y, hand_x + 4, hand_y + 2, C["GOLD_BASE"])
            draw_pixel_rect(draw, hand_x - 10, hand_y + 1, hand_x + 1, hand_y + 3, C["STEEL_BASE"])

    return img

def build_all_option_b_assets():
    """Generates all Option B sprite sheets and outputs."""
    base_dir = "ChroniclesOfSwarajya_Art"
    os.makedirs(os.path.join(base_dir, "00_ArtStyle"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "01_Shivaji"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "06_Previews"), exist_ok=True)

    # 1. Option B Master Palette PNG
    palette_path = os.path.join(base_dir, "00_ArtStyle", "option_b_palette.png")
    create_palette_swatch_image(palette_path)

    # 2. Shivaji Idle: 4 directions x 4 frames, 48x64 cells -> 192 x 256 px
    idle_sheet = Image.new("RGBA", (48 * 4, 64 * 4), C["NONE"])
    for row in range(4):  # S, N, E, W
        for col in range(4):
            f = draw_shivaji_frame(row, "idle", col, 4, 48, 64)
            idle_sheet.paste(f, (col * 48, row * 64))
    idle_path = os.path.join(base_dir, "01_Shivaji", "shivaji_idle.png")
    idle_sheet.save(idle_path)
    print(f"Generated shivaji_idle: {idle_path} ({idle_sheet.size[0]}x{idle_sheet.size[1]})")

    # 3. Shivaji Walk: 4 directions x 8 frames, 48x64 cells -> 384 x 256 px
    walk_sheet = Image.new("RGBA", (48 * 8, 64 * 4), C["NONE"])
    for row in range(4):  # S, N, E, W
        for col in range(8):
            f = draw_shivaji_frame(row, "walk", col, 8, 48, 64)
            walk_sheet.paste(f, (col * 48, row * 64))
    walk_path = os.path.join(base_dir, "01_Shivaji", "shivaji_walk.png")
    walk_sheet.save(walk_path)
    print(f"Generated shivaji_walk: {walk_path} ({walk_sheet.size[0]}x{walk_sheet.size[1]})")

    # 4. Shivaji Attack: 4 directions x 6 frames, 64x64 cells -> 384 x 256 px
    atk_sheet = Image.new("RGBA", (64 * 6, 64 * 4), C["NONE"])
    for row in range(4):  # S, N, E, W
        for col in range(6):
            f = draw_shivaji_attack_frame(row, col, 64)
            atk_sheet.paste(f, (col * 64, row * 64))
    atk_path = os.path.join(base_dir, "01_Shivaji", "shivaji_attack.png")
    atk_sheet.save(atk_path)
    print(f"Generated shivaji_attack: {atk_path} ({atk_sheet.size[0]}x{atk_sheet.size[1]})")

    # 5. Visual Comparison & Animation Gallery
    # Showcase: Old Phase 1 (24x32) vs New Option B (48x64) + Full Cycle Previews
    gallery_w, gallery_h = 760, 480
    gallery = Image.new("RGBA", (gallery_w, gallery_h), (16, 12, 10, 255))
    g_draw = ImageDraw.Draw(gallery)

    # Header title background
    draw_pixel_rect(g_draw, 0, 0, gallery_w, 42, (30, 20, 16, 255))
    draw_pixel_rect(g_draw, 0, 40, gallery_w, 42, (180, 83, 9, 255))

    # Old vs New Side-by-Side Panel
    draw_pixel_rect(g_draw, 20, 56, 360, 240, (24, 18, 14, 255))
    draw_pixel_rect(g_draw, 20, 56, 360, 240, (75, 40, 20, 255)) # border

    # Load old sprite if available
    old_path = os.path.join(base_dir, "01_Shivaji_Phase1_Legacy", "shivaji_idle.png")
    if os.path.exists(old_path):
        old_img = Image.open(old_path)
        # Crop single 24x32 frame
        old_f = old_img.crop((0, 0, 24, 32))
        old_2x = old_f.resize((48, 64), Image.NEAREST)
        old_4x = old_f.resize((96, 128), Image.NEAREST)
        gallery.paste(old_4x, (44, 96))

    # New 48x64 Shivaji frame 4x
    new_f = idle_sheet.crop((0, 0, 48, 64))
    new_2x = new_f.resize((96, 128), Image.NEAREST)
    gallery.paste(new_2x, (210, 96))

    # Right Panel: 4-Directional Idle Showcase
    draw_pixel_rect(g_draw, 380, 56, 740, 240, (24, 18, 14, 255))
    dirs_names = ["South (Front)", "North (Back)", "East (Right)", "West (Left)"]
    for d in range(4):
        f_dir = idle_sheet.crop((0, d * 64, 48, (d + 1) * 64))
        f_dir_2x = f_dir.resize((72, 96), Image.NEAREST)
        gallery.paste(f_dir_2x, (395 + d * 84, 110))

    # Bottom Panel: Attack combo sequence
    draw_pixel_rect(g_draw, 20, 260, 740, 460, (24, 18, 14, 255))
    for f in range(6):
        atk_f = atk_sheet.crop((f * 64, 0, (f + 1) * 64, 64))
        atk_2x = atk_f.resize((96, 96), Image.NEAREST)
        gallery.paste(atk_2x, (40 + f * 115, 310))

    gallery_path = os.path.join(base_dir, "06_Previews", "shivaji_animation_gallery.png")
    gallery.save(gallery_path)
    print(f"Generated animation gallery: {gallery_path}")

if __name__ == "__main__":
    build_all_option_b_assets()
