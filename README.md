# AI Agents

This repository contains independent AI agents, with each agent maintained in its own folder.

## Available Agents

### 1. College Library Chatbot

A chatbot application for interacting with a college library system.

- **Folder:** `college-library-chatbot/`
- **Backend:** Flask and Python
- **Frontend:** HTML, CSS, and JavaScript
- **Configuration:** `config/`
- **Dependencies:** `requirements.txt`
- **Environment template:** `.env.example`

### 2. TravelMate – Mini Autonomous Travel Agent

A travel planning application that generates a basic travel plan based on the user's destination, trip duration, and number of travellers.

- **Folder:** `travel-agent/`
- **Backend:** Flask and Python
- **Frontend:** HTML, CSS, and JavaScript
- **Core Logic:** Python-based travel planning
- **Features:** Suggested tourist attractions, predefined weather information, and estimated travel budget
- **Dependencies:** `requirements.txt`

**Supported destinations:** Chikmagalur, Mysuru, Coorg, and Bengaluru.

**Note:** Weather information and budget estimates are based on predefined data and calculations, not live services.

## How to Run

Each agent has its own setup instructions and dependencies.

### College Library Chatbot

1. Open the `college-library-chatbot/` folder.
2. Read its `README.md` for setup instructions.
3. Install the required Python dependencies.
4. Configure environment variables using `.env.example` if required.
5. Start the application using the instructions in the agent's README.

### TravelMate – Travel Agent

1. Open the `travel-agent/` folder.
2. Read its `README.md` for setup instructions.
3. Install the required dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python -m backend.app
   ```

5. Open `http://127.0.0.1:5000` in your browser.

## Repository Structure

```text
AI_Agents/
├── README.md
├── .gitignore
├── college-library-chatbot/
│   ├── backend/
│   ├── config/
│   ├── frontend/
│   ├── .env.example
│   ├── .gitignore
│   ├── requirements.txt
│   └── README.md
└── travel-agent/
    ├── backend/
    │   ├── __init__.py
    │   └── app.py
    ├── frontend/
    │   ├── index.html
    │   ├── style.css
    │   └── script.js
    ├── travel_agent.py
    ├── requirements.txt
    └── README.md
```

## Independence

Each agent should have its own frontend, backend, configuration, dependencies, and documentation wherever applicable. New agents can be added as separate folders without affecting existing projects.

## Security

Never commit real API keys, passwords, or other secrets. Use `.env.example` to document required environment variables without exposing their values.