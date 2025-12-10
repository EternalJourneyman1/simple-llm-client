
# simple-llm-client — Companion to the Medium article

A minimal, stateful Python CLI client demonstrating simple LLM conversation handling. This repository is a companion to the Medium article [From simple to smart: A Stateful LLM Client (Part 2)](https://demetrious-robinson.medium.com/from-simple-to-smart-part-2-building-a-stateful-llm-client-in-python-with-openrouter-1c16efd35fd2)

---

## 🔧 Configuration ( do this first)

Before running this project you must configure an API key. Create a `.env` file from the example and add your key.

Run this in your terminal in the root of the project:

```bash
# Edit .env and paste your API key in OPENROUTER_API_KEY
cp .env.example .env
```

Notes:
- `OPENROUTER_API_KEY` — the OpenRouter/OpenAI API key used by `main.py`.
- You can change `base_url` and `model` in `main.py` if you want to use a different endpoint/model.

---

## 🧭 Quickstart

1. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux (zsh)
pip install -r requirements.txt
```

2. Ensure `.env` is configured (see Configuration above), then run the CLI:

```bash
python main.py
```

---

## 📝 Usage

- Type messages at the prompt; the program maintains a conversation history.
- Type `exit` or `quit` to end the session.

Example:

```text
AI Agent initialized!
> What is a haiku about coffee?
AI Response: A short, three-line haiku...
```

---

## ⚠️ Notes

- This repository is intentionally minimal; it's intended to illustrate conversation state and API usage rather than production best practices.
- Keep your `.env` file out of version control and use restricted API keys.

---

## 🔗 See the full guide

For the full walkthrough and explanations read the Medium article: ["From simple to smart: A Stateful LLM Client (Part 2)"](https://demetrious-robinson.medium.com/from-simple-to-smart-part-2-building-a-stateful-llm-client-in-python-with-openrouter-1c16efd35fd2)

---
