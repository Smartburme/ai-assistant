from fastapi import APIRouter, Request
from pydantic import BaseModel
from assistant.core.dialog_manager import handle_message

router = APIRouter()

class ChatRequest(BaseModel):
    user_input: str

@router.post("/message")
def chat_message(req: ChatRequest):
    response = handle_message(req.user_input)
    return {"response": response}
