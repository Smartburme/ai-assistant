"""Dialog manager controls conversation state."""

from typing import Dict, Any
from .nlp_engine import NLPEngine

class DialogManager:
    def __init__(self, nlp: NLPEngine):
        self.nlp = nlp
        self.state: Dict[str, Any] = {}

    def process(self, user_id: str, text: str) -> str:
        intent = self.nlp.classify_intent(text)
        if intent == 'greet':
            return 'Hello! ငါကိုဘယ်လိုကူညီပေးရမလဲ?'
        return 'စိတ်မရှိပါနဲ့၊ နားလည်မရသေးပါ…'
