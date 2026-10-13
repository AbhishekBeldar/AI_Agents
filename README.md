# AI Agents

This repository contains independent AI agents, with each agent maintained in its own folder.

## Available Agents

### College Library Chatbot

A chatbot application for interacting with a college library system.

- **Folder:** `college-library-chatbot/`
- **Backend:** Flask and Python
- **Frontend:** HTML, CSS, and JavaScript
- **Configuration:** `config/`
- **Dependencies:** `requirements.txt`
- **Environment template:** `.env.example`

## How to Run

1. Open the `college-library-chatbot/` folder.
2. Read its `README.md` for setup instructions.
3. Install the required Python dependencies.
4. Configure environment variables using `.env.example` if required.
5. Start the application using the instructions in the agent's README.

## Repository Structure

```text
AI_Agents/
├── README.md
├── .gitignore
└── college-library-chatbot/
    ├── backend/
    ├── config/
    ├── frontend/
    ├── .env.example
    ├── .gitignore
    ├── requirements.txt
    └── README.md
```

## Independence

Each agent should have its own frontend, backend, configuration, dependencies, and documentation wherever applicable. New agents can be added as separate folders.

## Security

Never commit real API keys, passwords, or other secrets. Use `.env.example` to document required environment variables without exposing their values.