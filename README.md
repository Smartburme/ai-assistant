# 🧠 AI Assistant

AI Assistant is a modular, extensible Python-based assistant framework that uses NLP and a skill-based architecture to respond to user input. It supports command-line, REST API, and web-based interfaces, and comes with a set of built-in skills such as weather lookup, calculations, and reminders.

---

## ✨ Features

- 🧠 Intent classification using a lightweight NLP engine
- 💬 Dialog management and context handling
- 📚 Knowledge base querying (JSON, SQLite)
- 🔧 Built-in skills (weather, calculator, reminder)
- 🧪 Pytest-based unit & integration testing
- 🌐 REST API via FastAPI
- 🖥️ CLI interface & web server
- 🚀 CI/CD via GitHub Actions

---

## 🗂️ Project Structure
```

ai-assistant/
│
├── .github/                ← GitHub Actions (CI/CD)
│   ├── workflows/
│   │   ├── tests.yml       ← Pytest run on push/PR
│   │   └── deploy.yml      ← Build & deploy automation
│   └── ISSUE_TEMPLATE/     ← GitHub Issue templates
│       └── bug_report.md
│
├── assistant/              ← Main Python package
│   ├── core/               ← Core assistant logic
│   │   ├── nlp_engine.py       ← Basic NLP intent classifier
│   │   ├── dialog_manager.py  ← Handles conversation flow
│   │   └── knowledge_base.py  ← Simple QA knowledge lookup
│   │
│   ├── skills/             ← Modular skills (can expand)
│   │   ├── weather.py          ← Weather info (dummy now)
│   │   ├── calculator.py       ← Math operations
│   │   └── reminder.py         ← Reminder storage
│   │
│   ├── utils/              ← Helper functions
│   │   ├── logger.py           ← Logger setup
│   │   ├── config.py           ← Load config from file
│   │   └── helpers.py          ← Math/utils
│   │
│   ├── interfaces/         ← Input/output interfaces
│   │   ├── cli.py              ← Command Line Chat
│   │   ├── web.py              ← FastAPI Web Server
│   │   └── api.py              ← REST API (uses web.py)
│   │
│   └── __init__.py         ← Defines package
│
├── data/                   ← Static data files
│   ├── models/             ← Trained ML models (ignored)
│   │   └── nlp_model.h5        ← Dummy placeholder
│   ├── knowledge/          ← Knowledge base info
│   │   ├── faq.json             ← Common Q&A
│   └── training/
│       └── intents.json         ← For training NLP
│
├── tests/                  ← Pytest suite
│   ├── unit/               ← Individual function tests
│   │   ├── test_nlp.py
│   │   └── test_skills.py
│   └── integration/        ← Whole-system tests
│       ├── test_dialog.py
│       └── test_api.py
│
├── docs/                   ← Markdown documentation
│   ├── architecture.md         ← System design overview
│   ├── api.md                  ← REST API routes
│   └── skills/
│       ├── weather.md
│       └── calculator.md
│
├── notebooks/              ← Jupyter notebooks
│   ├── nlp_training.ipynb      ← NLP training notes
│   └── analysis.ipynb          ← Performance results
│
├── scripts/                ← Utility scripts
│   ├── setup_env.sh            ← Set up virtualenv
│   └── train_model.py          ← Dummy model trainer
│
├── .env.example            ← Sample env variables
├── .gitignore              ← Ignore compiled/cache files
├── pyproject.toml          ← Python project setup config
├── requirements.txt        ← Dependency list
├── README.md               ← Project overview
└── LICENSE                 ← MIT License
# Project overview
```
---

## 🚀 Getting Started

### 🔧 Installation

#### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-assistant.git
cd ai-assistant

2. Set up a virtual environment

python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Set up environment variables

cp .env.example .env


---

💬 Usage

1. Command Line Interface

python assistant/interfaces/cli.py

2. Run the Web API (FastAPI)

uvicorn assistant.interfaces.web:app --reload

Then open http://localhost:8000/docs to try the REST API.


---

🧪 Running Tests

Run all unit and integration tests using pytest:

pytest


---

⚙️ CI/CD

This project uses GitHub Actions:

.github/workflows/tests.yml: runs tests on push/pull requests

.github/workflows/deploy.yml: deployment pipeline (customizable)



---

📚 Documentation

Documentation is located in the /docs directory:

architecture.md: system design

api.md: REST API details

skills/: skill-specific docs


Jupyter notebooks for model training and analysis are in /notebooks.


---

📦 Packaging

This project uses pyproject.toml. You can build it using:

pip install build
python -m build


---

🧩 Extending Skills

To add a new skill:

1. Create a new .py file in assistant/skills/


2. Define a handle() function with the expected signature


3. Register the skill in the dialog manager or skill router



See calculator.py and reminder.py as examples.


---

🤝 Contributing

Contributions are welcome!
Please open issues, submit pull requests, or suggest features.


---

📝 License

This project is licensed under the MIT License. See the LICENSE file for details.


---

📌 Author

Developed by [Your Name or Organization]
© 2025 AI Assistant Project

---

### ✍️ Note:

- If you're using **Poetry** for packaging, the `pyproject.toml` will be your main config.
- If deploying with **Docker**, you might want to add a `Dockerfile` and update the README accordingly.
- You can customize the `Author`, `GitHub link`, and any project-specific setup or skills.

ပြန်ပြင်ချင်တဲ့ section တစ်ခုတင်ရေးပေးလို့ရပါတယ် — ပြောပါ။

