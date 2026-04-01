from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "generated_images"
OUTPUT_DIR.mkdir(exist_ok=True)

def generate_image(panel_text: str, index: int):
    img = Image.new("RGB", (512, 512), "white")
    draw = ImageDraw.Draw(img)

    # Panel border
    draw.rectangle([10, 10, 502, 502], outline="black", width=3)

    # Speech bubble
    bubble = [60, 60, 460, 200]
    draw.rounded_rectangle(bubble, radius=20, outline="black", width=3)

    # Tail
    draw.polygon([(140, 200), (170, 200), (150, 240)], fill="white", outline="black")

    # Text inside bubble
    draw.text((80, 90), panel_text, fill="black")

    filename = f"panel_{index+1}.png"
    path = OUTPUT_DIR / filename
    img.save(path)

    return path


