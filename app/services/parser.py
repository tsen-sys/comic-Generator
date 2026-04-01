def detect_emotion(dialogue: str) -> str:
    text = dialogue.lower()

    if "!" in text:
        return "angry"
    if "sorry" in text or "late" in text or "broke down" in text:
        return "worried"
    if "thank" in text or "great" in text or "nice" in text:
        return "happy"
    if "?" in text:
        return "confused"
    return "neutral"


def detect_scene(dialogue: str) -> str:
    text = dialogue.lower()

    if "bus" in text or "road" in text:
        return "bus stop on a busy street"
    if "school" in text or "class" in text:
        return "school classroom"
    if "office" in text or "meeting" in text:
        return "modern office room"
    if "home" in text or "house" in text:
        return "home interior"
    return "generic city background"


def detect_time(dialogue: str) -> str:
    text = dialogue.lower()

    if "morning" in text:
        return "morning"
    if "night" in text or "late" in text:
        return "night"
    return "daytime"


def parse_conversation(text: str):
    panels = []

    for line in text.split("\n"):
        if ":" in line:
            speaker, dialogue = line.split(":", 1)
            speaker = speaker.strip()
            dialogue = dialogue.strip()

            emotion = detect_emotion(dialogue)
            scene = detect_scene(dialogue)
            time = detect_time(dialogue)

            prompt = (
                f"A comic panel set in a {scene} during {time}, "
                f"showing {speaker} with a {emotion} expression, "
                f"bold outlines, vibrant colors, expressive face, "
                f"speech bubble saying '{dialogue}'."
            )

            panels.append(
                {
                    "speaker": speaker,
                    "dialogue": dialogue,
                    "emotion": emotion,
                    "scene": scene,
                    "time": time,
                    "prompt": prompt,
                }
            )

    return panels
