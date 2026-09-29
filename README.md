# Basic ADK Chatbot

A minimal conversational agent built with the Google Agent Development Kit (ADK)
and Gemini. It defines a single `root_agent` ("basic_chatbot") with a short
system instruction to answer clearly and politely. It is a starting template for
ADK agents: no tools, no memory beyond the ADK session.

## Tech stack

- Python 3.10+
- [Google ADK](https://google.github.io/adk-docs/) (`google-adk`)
- Gemini (model `gemini-3.5-flash`, set in `agent.py`)
- `python-dotenv`

## Project structure

```
AGENTS/
├── agent.py          # Defines root_agent (the ADK agent)
├── main.py           # Placeholder terminal loop (does not call the model)
├── requirements.txt
└── .env.example
```

## Prerequisites

- Python 3.10 or newer
- A Gemini API key from Google AI Studio

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt

copy .env.example .env          # cp .env.example .env on macOS / Linux
```

| Variable | Required | Where to get it |
|----------|----------|-----------------|
| `GOOGLE_API_KEY` | Yes | [Google AI Studio](https://aistudio.google.com/apikey) |
| `GOOGLE_GENAI_USE_VERTEXAI` | No | Keep `FALSE` to use the AI Studio key |

## Run

ADK discovers agents as sub-folders of the directory you run it from, so run the
ADK CLI from the **parent** of this folder:

```bash
cd ..
adk web            # browser UI at http://localhost:8000, then pick "AGENTS"
# or
adk run AGENTS     # chat in the terminal
```

`python main.py` only prints a placeholder message; it does not send anything to
the model. Use `adk web` or `adk run` to actually chat.

## Usage

Example prompts:

- "Explain what an API is in two sentences."
- "Give me three tips for writing a good README."
