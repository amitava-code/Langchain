# 🦜 LangChain Exploration

A hands-on repository documenting my journey learning LangChain — from basic LLM integrations to building a functional terminal chatbot.

---

## 📁 Structure

```
Langchain/
├── Google-GenAI/       # LangChain with Google Gemini
├── Mistral-AI/         # LangChain with Mistral AI
└── lc-chatbot/         # Terminal chatbot project
```

---

## 🔵 Google-GenAI

Exploring LangChain with Google's Gemini model.

**Model used:** `gemini-2.5-flash`

```python
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
response = model.invoke("Hello gemini")
print(response.text)
```

**Setup:**
```bash
pip install langchain-google-genai python-dotenv
```

Add your API key to `.env`:
```
GOOGLE_API_KEY=your_key_here
```

---

## 🟠 Mistral-AI

Exploring LangChain with Mistral AI's chat model.

**Model used:** `mistral-small-latest`

```python
from langchain_mistralai.chat_models import ChatMistralAI

model = ChatMistralAI(model="mistral-small-latest")
response = model.invoke("Hello Mistral")
print(response.text)
```

**Setup:**
```bash
pip install langchain-mistralai python-dotenv
```

Add your API key to `.env`:
```
MISTRAL_API_KEY=your_key_here
```

---

## 🤖 lc-chatbot

A terminal-based conversational chatbot built with LangChain and Google Gemini. Maintains full chat history across the session so the model remembers previous messages.

**Model used:** `gemini-2.5-flash`

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, AIMessage

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
messages = []

while True:
    userInput = input("Enter Prompt ......")
    messages.append(HumanMessage(userInput))
    response = model.invoke(messages)
    messages.append(AIMessage(response.content))
    print(response.text)
```

**Run it:**
```bash
cd lc-chatbot
pip install -r requirements.txt
python main.py
```

---

## ⚙️ General Setup

1. Clone the repo:
```bash
git clone https://github.com/amitava-code/Langchain.git
cd Langchain
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # Git Bash on Windows
```

3. Install dependencies and add your API keys to a `.env` file in the relevant folder.

---

## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/)
- [Google Gemini](https://ai.google.dev/)
- [Mistral AI](https://mistral.ai/)
- Python 3.11+