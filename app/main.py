from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.schemas import ConversationRequest
from app.services.parser import parse_conversation
from app.services.image_generator import generate_image
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Conversation to Comic API")

app.mount(
    "/images",
    StaticFiles(directory="app/generated_images"),
    name="images"
)



# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
GENERATED_DIR = BASE_DIR / "generated_images"
GENERATED_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# App
# -----------------------------
app = FastAPI(title="Conversation to Comic API")

# -----------------------------
# Static files
# -----------------------------
app.mount(
    "/images",
    StaticFiles(directory=GENERATED_DIR),
    name="images"
)

# -----------------------------
# API Endpoint ✅
# -----------------------------
@app.post("/generate-comic")
def generate_comic(request: ConversationRequest):
    panels = parse_conversation(request.conversation)

    image_paths = []

    # 👇 PASTE HERE (inside the function, inside the loop)
    for i, panel in enumerate(panels, start=1):
        panel_text = f"{panel.get('speaker', '')}: {panel.get('text') or panel.get('dialogue')}"
        image_path = generate_image(panel_text, i)
        image_paths.append(f"/images/{image_path.name}")

    return {
        "message": "Comic generated successfully",
        "images": image_paths
    }

    return {
        "message": "Comic generated successfully",
        "images": image_paths
    }
