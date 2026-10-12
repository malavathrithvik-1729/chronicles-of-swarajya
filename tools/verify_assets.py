import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image

def verify():
    checks = [
        {
            "name": "Option B Palette",
            "file": "ChroniclesOfSwarajya_Art/00_ArtStyle/option_b_palette.png",
            "expected_dims": (320, 160),
            "expected_mode": "RGBA"
        },
        {
            "name": "Shivaji Idle",
            "file": "ChroniclesOfSwarajya_Art/01_Shivaji/shivaji_idle.png",
            "expected_dims": (192, 256),  # 4 cols x 48, 4 rows x 64
            "cell": (48, 64),
            "cols": 4, "rows": 4,
            "expected_mode": "RGBA"
        },
        {
            "name": "Shivaji Walk",
            "file": "ChroniclesOfSwarajya_Art/01_Shivaji/shivaji_walk.png",
            "expected_dims": (384, 256),  # 8 cols x 48, 4 rows x 64
            "cell": (48, 64),
            "cols": 8, "rows": 4,
            "expected_mode": "RGBA"
        },
        {
            "name": "Shivaji Attack",
            "file": "ChroniclesOfSwarajya_Art/01_Shivaji/shivaji_attack.png",
            "expected_dims": (384, 256),  # 6 cols x 64, 4 rows x 64
            "cell": (64, 64),
            "cols": 6, "rows": 4,
            "expected_mode": "RGBA"
        },
        {
            "name": "Shivaji Portrait",
            "file": "ChroniclesOfSwarajya_Art/04_Portraits/shivaji_portrait.png",
            "min_size": (512, 512),
        },
        {
            "name": "Shivaji Animation Gallery",
            "file": "ChroniclesOfSwarajya_Art/06_Previews/shivaji_animation_gallery.png",
            "expected_dims": (760, 480),
        }
    ]

    print("=== STARTING ASSET INTEGRITY QA AUDIT ===")
    all_passed = True
    for c in checks:
        path = c["file"]
        if not os.path.exists(path):
            print(f"❌ FAIL: File missing: {path}")
            all_passed = False
            continue

        try:
            img = Image.open(path)
            w, h = img.size
            mode = img.mode

            if "expected_dims" in c and (w, h) != c["expected_dims"]:
                print(f"❌ FAIL {c['name']}: Dimensions ({w}x{h}) != expected {c['expected_dims']}")
                all_passed = False
                continue

            if "expected_mode" in c and mode != c["expected_mode"]:
                print(f"❌ FAIL {c['name']}: Mode {mode} != expected {c['expected_mode']}")
                all_passed = False
                continue

            # Alpha channel transparency test for sprite sheets
            if mode == "RGBA" and "cell" in c:
                has_transparent = False
                has_visible = False
                # Sample corners of first cell
                for x in range(c["cell"][0]):
                    for y in range(c["cell"][1]):
                        p = img.getpixel((x, y))
                        if p[3] == 0:
                            has_transparent = True
                        elif p[3] > 0:
                            has_visible = True
                if not (has_transparent and has_visible):
                    print(f"❌ FAIL {c['name']}: Alpha channel invalid (transparent={has_transparent}, visible={has_visible})")
                    all_passed = False
                    continue

            print(f"✅ PASS: {c['name']} ({path}) -> {w}x{h} px [{mode}]")

        except Exception as e:
            print(f"❌ EXCEPTION loading {path}: {e}")
            all_passed = False

    print("=========================================")
    if all_passed:
        print("🎉 ALL 6 ASSETS VERIFIED PERFECTLY!")
    else:
        print("⚠️ SOME CHECKS FAILED!")

if __name__ == "__main__":
    verify()
