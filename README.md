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
## 🟣 AI-Tools

Exploring **LangChain Tools, LLM hallucinations, and tool calling workflows** using Mistral.

This module demonstrates how to overcome one of the biggest limitations of LLMs — **lack of real-time awareness** — by integrating external tools.

---

### ❗ Problem: LLM Hallucination

LLMs like Mistral:

* Do **not know real-time data**
* Can generate **incorrect or guessed answers**

Example:

```python
model.invoke("What is today's date?")
```

➡️ May return a **wrong date**

---

### ✅ Solution: Tool Integration

We define a tool to fetch real-time data:

```python
from langchain.tools import tool
from datetime import date

@tool
def getCurrentDate():
    """Returns current date"""
    return str(date.today())
```

---

### ⚙️ Tool Calling with Mistral

Bind tool to model:

```python
model = ChatMistralAI(model="mistral-small").bind_tools([getCurrentDate])
```

---

### 🔁 Execution Flow

```python
response = model.invoke("today's date ?")

tool_result = getCurrentDate.invoke(response.tool_calls[0]["args"])

final_response = model.invoke(
    ["Human:- Today's Date", "Tool result := " + tool_result]
)

print(final_response.text)
```

---

### 🔄 How It Works

1. User asks a question
2. LLM decides to call a tool
3. Tool executes (`getCurrentDate`)
4. Result is passed back to LLM
5. LLM generates **accurate final answer**

---

### 🎯 Key Learnings

* Tools solve **hallucination for dynamic data**
* LLM + Tools = **more reliable systems**
* This is the foundation of **AI agents**

---

### 📌 Future Scope

* Automate tool execution loop
* Add multiple tools
* Build full agent using `AgentExecutor`


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