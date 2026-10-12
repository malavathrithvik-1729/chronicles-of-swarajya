import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw, ImageFilter

def draw_pixel_rect(draw, x1, y1, x2, y2, color):
    rx1, rx2 = round(min(x1, x2)), round(max(x1, x2))
    ry1, ry2 = round(min(y1, y2)), round(max(y1, y2))
    draw.rectangle([rx1, ry1, rx2, ry2], fill=color)

def draw_ellipse_soft(draw, cx, cy, rx, ry, color):
    draw.ellipse([round(cx - rx), round(cy - ry), round(cx + rx), round(cy + ry)], fill=color)

def create_stylized_bust(output_path, name, title, base_color, accent_color, is_young=False):
    """Creates a high-res illustrated portrait bust matching the studio style."""
    w, h = 1024, 1024
    img = Image.new("RGB", (w, h), (18, 14, 12))
    draw = ImageDraw.Draw(img)

    # Atmospheric background gradient
    for y in range(h):
        factor = y / h
        r = int(18 * (1 - factor) + 10 * factor)
        g = int(14 * (1 - factor) + 8 * factor)
        b = int(12 * (1 - factor) + 6 * factor)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Archway frame in background
    draw.arc([160, 80, 864, 800], start=180, end=360, fill=(60, 45, 30), width=6)
    draw.line([(160, 440), (160, 900)], fill=(60, 45, 30), width=6)
    draw.line([(864, 440), (864, 900)], fill=(60, 45, 30), width=6)

    # Warm rim light glow
    draw.ellipse([400, 200, 624, 424], fill=(80, 50, 25))

    # Shoulders & Tunic
    draw.polygon([(260, 960), (360, 680), (664, 680), (764, 960)], fill=base_color)
    draw.polygon([(440, 680), (512, 850), (584, 680)], fill=accent_color)  # Collar sash

    # Neck
    draw_pixel_rect(draw, 450, 560, 574, 700, (195, 130, 65))

    # Head / Jaw
    draw_ellipse_soft(draw, 512, 450, 140, 160, (215, 145, 80))

    # Facial Features
    # Eyes
    draw_ellipse_soft(draw, 450, 420, 18, 10, (245, 245, 240))
    draw_ellipse_soft(draw, 450, 420, 9, 9, (20, 20, 20))
    draw_ellipse_soft(draw, 574, 420, 18, 10, (245, 245, 240))
    draw_ellipse_soft(draw, 574, 420, 9, 9, (20, 20, 20))
    # Brow
    draw.line([(420, 395), (480, 400)], fill=(30, 25, 20), width=8)
    draw.line([(544, 400), (604, 395)], fill=(30, 25, 20), width=8)
    # Nose
    draw.line([(512, 410), (505, 480)], fill=(160, 100, 50), width=6)
    draw.line([(505, 480), (525, 485)], fill=(160, 100, 50), width=5)
    # Moustache & Beard
    if not is_young:
        draw_ellipse_soft(draw, 512, 530, 80, 25, (30, 25, 20))
        draw_ellipse_soft(draw, 512, 580, 65, 40, (30, 25, 20))
    else:
        draw_ellipse_soft(draw, 512, 520, 50, 15, (30, 25, 20))

    # Turban (Pheta)
    draw_ellipse_soft(draw, 512, 280, 170, 120, accent_color)
    draw_ellipse_soft(draw, 512, 240, 140, 90, base_color)
    draw.line([(380, 310), (644, 290)], fill=(251, 191, 36), width=8)  # Gold trim

    # Border vignette
    draw.rectangle([0, 0, w, 20], fill=(24, 18, 14))
    draw.rectangle([0, h-80, w, h], fill=(24, 18, 14))
    draw.rectangle([0, 0, 20, h], fill=(24, 18, 14))
    draw.rectangle([w-20, 0, w, h], fill=(24, 18, 14))

    # Name Banner
    draw.rectangle([100, h - 70, w - 100, h - 16], fill=(40, 28, 20), outline=(217, 119, 6), width=2)

    img.save(output_path)
    print(f"✅ Generated Illustrated Portrait: {output_path}")

def build_galleries():
    art_dir = "ChroniclesOfSwarajya_Art"
    prev_dir = os.path.join(art_dir, "07_Previews_OptionB")
    os.makedirs(prev_dir, exist_ok=True)

    # 1. ENEMY ROSTER GALLERY (960 x 420 px)
    eg_w, eg_h = 960, 420
    eg = Image.new("RGBA", (eg_w, eg_h), (16, 12, 10, 255))
    e_draw = ImageDraw.Draw(eg)
    # Header
    draw_pixel_rect(e_draw, 0, 0, eg_w, 42, (30, 20, 16, 255))
    draw_pixel_rect(e_draw, 0, 40, eg_w, 42, (180, 83, 9, 255))

    enemies = [
        ("swordsman", 40, 56),
        ("shield_guard", 44, 58),
        ("archer", 40, 56),
        ("charging_soldier", 44, 58),
        ("elite_halberdier", 48, 64),
        ("spear_soldier", 40, 56),
    ]
    for idx, (ename, ew, eh) in enumerate(enemies):
        panel_x = 20 + idx * 155
        draw_pixel_rect(e_draw, panel_x, 56, panel_x + 145, eg_h - 20, (24, 18, 14, 255))
        draw_pixel_rect(e_draw, panel_x, 56, panel_x + 145, eg_h - 20, (75, 45, 25, 255))

        idle_path = os.path.join(art_dir, "02_Enemies_OptionB", ename, f"{ename}_idle.png")
        if os.path.exists(idle_path):
            img = Image.open(idle_path)
            # Crop frame 0, row 0 (South)
            frame_s = img.crop((0, 0, ew, eh)).resize((ew * 2, eh * 2), Image.NEAREST)
            eg.paste(frame_s, (panel_x + (145 - ew*2)//2, 80), frame_s)
            # Crop frame 0, row 2 (East)
            frame_e = img.crop((0, 2 * eh, ew, 3 * eh)).resize((ew * 2, eh * 2), Image.NEAREST)
            eg.paste(frame_e, (panel_x + (145 - ew*2)//2, 220), frame_e)

    eg_path = os.path.join(prev_dir, "enemy_roster_gallery.png")
    eg.save(eg_path)
    print(f"✅ Generated Enemy Gallery: {eg_path}")

    # 2. BOSS ROSTER GALLERY (840 x 440 px)
    bg_w, bg_h = 840, 440
    bg = Image.new("RGBA", (bg_w, bg_h), (16, 12, 10, 255))
    b_draw = ImageDraw.Draw(bg)
    draw_pixel_rect(b_draw, 0, 0, bg_w, 42, (30, 20, 16, 255))
    draw_pixel_rect(b_draw, 0, 40, bg_w, 42, (180, 83, 9, 255))

    bosses = [
        ("afzal_khan", 64, 80),
        ("shaista_khan", 60, 76),
        ("aurangzeb", 64, 80),
    ]
    for idx, (bname, bw, bh) in enumerate(bosses):
        panel_x = 20 + idx * 270
        draw_pixel_rect(b_draw, panel_x, 56, panel_x + 250, bg_h - 20, (24, 18, 14, 255))
        draw_pixel_rect(b_draw, panel_x, 56, panel_x + 250, bg_h - 20, (85, 40, 50, 255))

        idle_path = os.path.join(art_dir, "04_Bosses_OptionB", bname, f"{bname}_idle.png")
        if os.path.exists(idle_path):
            img = Image.open(idle_path)
            frame_s = img.crop((0, 0, bw, bh)).resize((bw * 2, bh * 2), Image.NEAREST)
            bg.paste(frame_s, (panel_x + 20, 90), frame_s)
            frame_e = img.crop((0, 2 * bh, bw, 3 * bh)).resize((bw * 2, bh * 2), Image.NEAREST)
            bg.paste(frame_e, (panel_x + bw*2 + 10, 90), frame_e)

    bg_path = os.path.join(prev_dir, "boss_roster_gallery.png")
    bg.save(bg_path)
    print(f"✅ Generated Boss Gallery: {bg_path}")

    # 3. ALLIES ROSTER GALLERY (740 x 360 px)
    ag_w, ag_h = 740, 360
    ag = Image.new("RGBA", (ag_w, ag_h), (16, 12, 10, 255))
    a_draw = ImageDraw.Draw(ag)
    draw_pixel_rect(a_draw, 0, 0, ag_w, 42, (30, 20, 16, 255))
    draw_pixel_rect(a_draw, 0, 40, ag_w, 42, (180, 83, 9, 255))

    allies = [
        ("mavala_warrior", 44, 58),
        ("mavala_scout", 40, 56),
        ("village_elder", 40, 56),
        ("blacksmith", 48, 64),
    ]
    for idx, (aname, aw, ah) in enumerate(allies):
        panel_x = 20 + idx * 175
        draw_pixel_rect(a_draw, panel_x, 56, panel_x + 160, ag_h - 20, (24, 18, 14, 255))
        draw_pixel_rect(a_draw, panel_x, 56, panel_x + 160, ag_h - 20, (40, 65, 35, 255))

        idle_path = os.path.join(art_dir, "03_Allies_OptionB", aname, f"{aname}_idle.png")
        if os.path.exists(idle_path):
            img = Image.open(idle_path)
            frame_s = img.crop((0, 0, aw, ah)).resize((aw * 2, ah * 2), Image.NEAREST)
            ag.paste(frame_s, (panel_x + (160 - aw*2)//2, 100), frame_s)

    ag_path = os.path.join(prev_dir, "allies_roster_gallery.png")
    ag.save(ag_path)
    print(f"✅ Generated Allies Gallery: {ag_path}")

    # 4. WEAPONS GALLERY (640 x 240 px)
    wg_w, wg_h = 640, 240
    wg = Image.new("RGBA", (wg_w, wg_h), (16, 12, 10, 255))
    w_draw = ImageDraw.Draw(wg)
    draw_pixel_rect(w_draw, 0, 0, wg_w, 36, (30, 20, 16, 255))

    w_files = [
        ("talwar_basic", 32, 32),
        ("talwar_upgraded", 32, 32),
        ("heavy_curved_sword", 40, 40),
        ("halberd", 48, 48),
        ("spear", 48, 48),
        ("bow_and_arrow", 32, 32),
        ("maratha_dhal_shield", 32, 32)
    ]
    for idx, (wname, ww, wh) in enumerate(w_files):
        px = 20 + idx * 86
        draw_pixel_rect(w_draw, px, 50, px + 80, wg_h - 20, (24, 18, 14, 255))
        w_path = os.path.join(art_dir, "06_Weapons_OptionB", f"{wname}.png")
        if os.path.exists(w_path):
            w_img = Image.open(w_path)
            res = w_img.resize((ww * 2, wh * 2), Image.NEAREST)
            wg.paste(res, (px + (80 - ww*2)//2, 80), res)

    wg_path = os.path.join(prev_dir, "weapons_gallery.png")
    wg.save(wg_path)
    print(f"✅ Generated Weapons Gallery: {wg_path}")

def main():
    port_dir = os.path.join("ChroniclesOfSwarajya_Art", "05_Portraits_OptionB")
    os.makedirs(port_dir, exist_ok=True)

    # Generate remaining portraits
    create_stylized_bust(os.path.join(port_dir, "mavala_scout.png"), "Mavala Scout", "Scout of the Sahyadri", (35, 75, 30), (55, 120, 45), is_young=True)
    create_stylized_bust(os.path.join(port_dir, "village_leader.png"), "Village Patil", "Settlement Administrator", (160, 100, 40), (210, 140, 50))
    create_stylized_bust(os.path.join(port_dir, "messenger.png"), "Royal Messenger", "Courier of Swarajya", (180, 80, 20), (230, 120, 30), is_young=True)

    # Build galleries
    build_galleries()

if __name__ == "__main__":
    main()
