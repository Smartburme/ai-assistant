# AI Assistant

ဒီ project က modular Python package တစ်ခုဖြစ်ပြီး CLI, Web, REST API စတဲ့ interface များမှတစ်ဆင့် အသုံးပြုနိုင်ပါသည်။  
**မြန်မာဘာသာဖြင့်** ဖော်ပြထားသည်။

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn assistant.interfaces.web:app --reload
```
