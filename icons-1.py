import os
import shutil
from PIL import Image

SRC = "www/icon-512.png"
RES = "android/app/src/main/res"
SIZES = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}

# حذف آیکون adaptive پیش‌فرض تا آیکون PNG خودمان استفاده شود
shutil.rmtree(os.path.join(RES, "mipmap-anydpi-v26"), ignore_errors=True)

img = Image.open(SRC).convert("RGBA")
for name, size in SIZES.items():
    folder = os.path.join(RES, "mipmap-" + name)
    os.makedirs(folder, exist_ok=True)
    out = img.resize((size, size), Image.LANCZOS)
    for fn in ("ic_launcher.png", "ic_launcher_round.png", "ic_launcher_foreground.png"):
        out.save(os.path.join(folder, fn))
print("icons done")
