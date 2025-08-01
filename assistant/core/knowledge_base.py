"""Knowledge base queries common facts / FAQ."""

import json
from pathlib import Path
from typing import Any

class KnowledgeBase:
    def __init__(self, kb_path: Path):
        self.data: dict[str, Any] = {}
        if kb_path.exists():
            with open(kb_path, 'r', encoding='utf-8') as fp:
                self.data = json.load(fp)

    def answer(self, question: str) -> str | None:
        return self.data.get(question.lower())
