📘 README.md – Burme-AI

# 🤖 Burme-AI

Burme-AI is a smart Burmese-language AI assistant designed to support chat, image generation, and code generation. Built with Gemini API and Firebase, it provides a modern, user-friendly interface that works across web and mobile platforms.

## 🚀 Features

- 🔐 Firebase Auth (Login / Register / Reset Password)
- 💬 Chatbot (Text, Image, Code generation via Gemini API)
- 🖼️ Image Upload & Display
- 📂 LocalStorage-based chat history
- 🎨 Neon UI with Float3D design
- 🧠 Smart Mode Switching (Text/Image/Code)
- 🌐 Hosted via GitHub Pages / Cloudflare Pages

## 📁 Project Structure
```

burme-ai/ ├── index.html              # 🔐 Login Page ├── register.html           # 📝 Register Page ├── reset.html              # 🔑 Reset Password Page ├── mainchat.html           # 🤖 Chat + Generator UI ├── about.html              # 📘 About Project (Loads README) ├── privacy.html            # 🔐 Privacy Policy & Terms ├── js/ │   ├── auth.js             # 🔐 Firebase Auth Logic │   ├── chat.js             # 💬 ChatBot Logic │   ├── gemini.js           # 🤖 Gemini API Integration │   ├── ui.js               # 🎨 UI + Sidebar + Float3D │   └── markdown.js         # 📘 README rendering ├── css/ │   └── style.css           # 🌈 Global Styles (Responsive + Neon) ├── assets/ │   └── icon.jpg            # 🌐 App Icon ├── .gitignore              # 🔒 Ignores .env and build files ├── README.md               # 📘 You are here!
```
## ⚙️ Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/your-username/burme-ai.git
cd burme-ai

2. Open in GitHub Codespaces

Click Code > Open with Codespaces > Create New

Use integrated terminal inside Codespaces


3. Setup .env (For Gemini API)

# In Codespaces terminal
touch .env

GEMINI_API_KEY=your_api_key_here

Or set as environment variable in Cloudflare/GitHub Secrets.

4. Run Locally

If using Live Server extension or simple python:

python3 -m http.server

Visit: http://localhost:8000

🛠️ Tech Stack

HTML, CSS, JS (Vanilla)

Firebase Auth

Gemini API (Text/Image/Code)

Cloudflare Pages / GitHub Pages


🙋‍♂️ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📄 License

MIT License © 2025 Burme-AI

---

သင့်အတွက် အထူးပြင်ဆင်ဖို့ `App name`, `username`, သို့မဟုတ် `Live URL` စတာတွေရှိရင် ပြောပါ — README ကို ပြန်ပြင်ပေးပါမယ်။  
ဆက်လုပ်ဖို့ `README.md` ကို ဒီနည်းနဲ့ GitHub မှာ commit/push လုပ်နိုင်ပါတယ်:

```bash
git add README.md
git commit -m "📝 Update README with project info"
git push

ပြန်လိုချင်တာများပါက ဆက်မေးနိုင်ပါတယ်။

