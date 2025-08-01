"""Configuration loader."""

from pathlib import Path
import json
from typing import Any

def load_config(path: Path) -> dict[str, Any]:
    if path.exists():
        with open(path, 'r', encoding='utf-8') as fp:
            return json.load(fp)
    return {}
