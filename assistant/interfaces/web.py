"""FastAPI web interface (simple)."""

from fastapi import FastAPI
from pydantic import BaseModel
from assistant.core.nlp_engine import NLPEngine
from assistant.core.dialog_manager import DialogManager

app = FastAPI(title='AI Assistant')

nlp = NLPEngine()
dialog = DialogManager(nlp)

class Message(BaseModel):
    user_id: str
    text: str

@app.post('/chat')
def chat(msg: Message):
    reply = dialog.process(msg.user_id, msg.text)
    return {'reply': reply}
