import os
import math
from PIL import Image, ImageDraw

# Master Option B Color Palette
PALETTE = {
    "TRANSPARENT": (0, 0, 0, 0),
    # Skin
    "SKIN_LIGHT": (230, 168, 115, 255),
    "SKIN_BASE": (198, 134, 66, 255),
    "SKIN_DARK": (141, 91, 45, 255),
    "SKIN_SHADOW": (95, 58, 28, 255),
    # Hair & Beard
    "BEARD_BLACK": (28, 25, 23, 255),
    "BEARD_DARK": (41, 37, 36, 255),
    "EYE_WHITE": (245, 245, 244, 255),
    "EYE_PUPIL": (15, 15, 15, 255),
    # Pheta (Turban) & Sash
    "PHETA_RED": (185, 28, 28, 255),
    "PHETA_RED_DARK": (127, 29, 29, 255),
    "PHETA_RED_DEEP": (85, 18, 18, 255),
    "SAFFRON_LIGHT": (245, 158, 11, 255),
    "SAFFRON_BASE": (230, 96, 18, 255),
    "SAFFRON_DARK": (180, 83, 9, 255),
    "SAFFRON_DEEP": (120, 53, 15, 255),
    # Gold & Jewelry
    "GOLD_LIGHT": (254, 240, 138, 255),
    "GOLD_BASE": (251, 191, 36, 255),
    "GOLD_DARK": (217, 119, 6, 255),
    "PEARL_WHITE": (255, 255, 255, 255),
    "RUBY_RED": (190, 18, 60, 255),
    # Angarkha (Royal Tunic)
    "ANGARKHA_LIGHT": (254, 243, 199, 255),
    "ANGARKHA_BASE": (245, 232, 180, 255),
    "ANGARKHA_SHADOW": (214, 195, 142, 255),
    "ANGARKHA_DARK": (175, 155, 105, 255),
    # Lower Garments (Churidar)
    "CHURIDAR_BASE": (235, 225, 185, 255),
    "CHURIDAR_SHADOW": (195, 180, 140, 255),
    # Mojari (Footwear) & Leather
    "LEATHER_LIGHT": (120, 53, 15, 255),
    "LEATHER_BASE": (69, 26, 3, 255),
    "LEATHER_DARK": (45, 16, 2, 255),
    # Talwar & Steel
    "STEEL_GLINT": (255, 255, 255, 255),
    "STEEL_LIGHT": (226, 232, 240, 255),
    "STEEL_BASE": (148, 163, 184, 255),
    "STEEL_DARK": (71, 85, 105, 255),
    "STEEL_DEEP": (30, 41, 59, 255),
    # VFX Sword Slash
    "SLASH_CORE": (255, 255, 255, 240),
    "SLASH_GOLD": (251, 191, 36, 210),
    "SLASH_ORANGE": (249, 115, 22, 170),
    "SLASH_FADE": (234, 88, 12, 90),
    # Outlines
    "OUTLINE_DARK": (25, 20, 18, 255),
}

print("Palette defined with", len(PALETTE), "tones.")
