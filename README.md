# Zed-Bot 🧠💬

Zed-Bot is a terminal-based AI chatbot built using LangChain and OpenAI. It leverages session-based memory with `RunnableWithMessageHistory` and provides a clean CLI using `click`.

---

## 📜 Features

- Persistent session-based memory using `InMemoryChatMessageHistory`
- Stateless conversation logic with LangChain
- CLI interaction with commands:
  - `exit` — quit the session
  - `wipe` — clear session memory
- Secure configuration with `.env` and OpenAI integration

---

## 📦 Requirements

- Python 3.10+
- OpenAI API key in `.env` file

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install langchain langchain-openai python-dotenv click
```

### 2. Create your `.env` file

```env
OPENAI_API_KEY=your-api-key-here
```

### 3. Run the chatbot

```bash
python bot.py
```

---
##📁 Project Structure

Zed-bot/
├── zedchat.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
---

## 🧪 Usage

```bash
$ python bot.py
🤖 Zed: Hello! Ask me anything. Type 'exit' to quit. Type 'wipe' to wipe memory
You: Hello!
Zed: Hi there! How can I help you today?

You: wipe
 Memory wiped!

You: exit
 Adios!
```

