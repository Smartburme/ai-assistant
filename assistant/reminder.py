"""Reminder skill (placeholder)."""

from datetime import datetime
from typing import Dict

reminders: Dict[str, list[tuple[str, datetime]]] = {}

def add_reminder(user: str, text: str, when: datetime) -> str:
    reminders.setdefault(user, []).append((text, when))
    return f'အကြောင်းကြားခြင်း {text} ကို {when} တွင် သတ်မှတ်ပြီးပါပြီ'

def get_reminders(user: str):
    return reminders.get(user, [])
