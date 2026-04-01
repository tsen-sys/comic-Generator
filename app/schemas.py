from pydantic import BaseModel
from typing import List


class Panel(BaseModel):
    speaker: str
    dialogue: str
    emotion: str
    scene: str
    time: str
    prompt: str
    image_base64: str




class ConversationRequest(BaseModel):
    conversation: str


class ComicResponse(BaseModel):
    panels: List[Panel]



