"""Weather skill — returns simple weather info."""

from typing import Optional
import requests
import os

API_KEY = os.getenv('WEATHER_API_KEY', '')

def get_weather(city: str) -> Optional[str]:
    if not API_KEY:
        return 'Weather API key မလိုအပ်သေးပါ'
    # Placeholder
    return f'{city} မြို့မှာ ရာသီဥတုအခြေအနေကို စစ်ဆေးနေပါသည်…'
