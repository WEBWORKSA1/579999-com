"""Generate assets/img/og.png (1200x630 social share image). Requires Pillow."""
import glob, os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1200, 630
im = Image.new("RGB", (W, H), "#8e0c17"); d = ImageDraw.Draw(im)
for i in range(H):
    d.line([(0, i), (W, i)], fill=(int(142 + 37 * i / H), int(12 + 6 * i / H), int(23 + 8 * i / H)))
d.rectangle([24, 24, W - 24, H - 24], outline="#c9a227", width=6)
def font(sz):
    for p in glob.glob("/usr/share/fonts/**/*DejaVuSans-Bold.ttf", recursive=True) + glob.glob("/usr/share/fonts/**/*.ttf", recursive=True):
        try:
            return ImageFont.truetype(p, sz)
        except Exception:
            pass
    return ImageFont.load_default()
d.text((W / 2, 250), "579999", font=font(190), fill="#f3d97a", anchor="mm")
d.text((W / 2, 410), "Lucky Number Exchange", font=font(52), fill="#ffffff", anchor="mm")
d.text((W / 2, 480), "Decode · Value · Trade Chinese lucky numbers", font=font(36), fill="#fde9d6", anchor="mm")
os.makedirs(os.path.join(ROOT, "assets/img"), exist_ok=True)
im.save(os.path.join(ROOT, "assets/img/og.png"), optimize=True)
print("og.png written")
