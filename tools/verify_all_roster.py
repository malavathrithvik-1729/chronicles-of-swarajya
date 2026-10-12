import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image

def verify_all():
    print("=== MASTER QA VERIFICATION: OPTION B CHARACTER ROSTER ===")
    art_dir = "ChroniclesOfSwarajya_Art"
    
    total_files = 0
    total_bytes = 0
    failures = 0

    expected_folders = [
        "01_Shivaji",
        "02_Enemies_OptionB",
        "03_Allies_OptionB",
        "04_Bosses_OptionB",
        "05_Portraits_OptionB",
        "06_Weapons_OptionB",
        "07_Previews_OptionB",
    ]

    for fld in expected_folders:
        full_fld = os.path.join(art_dir, fld)
        if not os.path.exists(full_fld):
            print(f"❌ Missing expected directory: {full_fld}")
            failures += 1
            continue
        
        file_count = 0
        for root, dirs, files in os.walk(full_fld):
            for file in files:
                if not file.endswith(".png") and not file.endswith(".jpg"):
                    continue
                path = os.path.join(root, file)
                total_files += 1
                file_count += 1
                size = os.path.getsize(path)
                total_bytes += size

                try:
                    img = Image.open(path)
                    w, h = img.size
                    mode = img.mode
                    # Verify image has valid dimensions
                    if w <= 0 or h <= 0:
                        print(f"❌ Invalid dimensions for {path}: {w}x{h}")
                        failures += 1
                except Exception as e:
                    print(f"❌ Failed to decode {path}: {e}")
                    failures += 1
        
        print(f"✅ Verified Folder: {fld:<25} ({file_count} image files)")

    print("=========================================================")
    print(f"Total Option B Asset Files Checked : {total_files}")
    print(f"Total Measured File Size           : {total_bytes / (1024*1024):.2f} MB")
    print(f"Verification Status                : {'🎉 100% PASSED (0 FAILURES)' if failures == 0 else f'⚠️ {failures} FAILURES'}")

if __name__ == "__main__":
    verify_all()
