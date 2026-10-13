# College Library Chatbot

## Overview
The College Library Chatbot is a Python-based chatbot that answers questions about book availability in a college library. It provides a simple web interface for students to check whether a book is available, borrowed, or not in the library inventory.

## Features
- Checks whether a book exists in the library inventory.
- Reports whether a book is available or currently borrowed.
- Informs users when a requested book is not in the library.
- Provides a web-based chat interface.
- Uses a JSON file to store book information.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript
- JSON

## Project Structure
- `backend/` — Python chatbot logic and Flask API.
- `frontend/` — HTML, CSS, and JavaScript interface.
- `config/books.json` — Library book inventory.
- `.env.example` — Example environment configuration.
- `requirements.txt` — Python dependencies.

## Setup Instructions

### 1. Install dependencies
Run this command from the project root:

    python -m pip install -r requirements.txt

### 2. Start the web application
Run:

    python backend/app.py

### 3. Open the chatbot
Open this address in your browser:

    http://127.0.0.1:5000

## Example Questions
- Do you have The Hobbit?
- Do you have The Little Prince?
- Do you have Percy Jackson?

## Notes
This project uses a predefined book inventory. It does not require an external AI API key.

## Future Improvements
- Add more books to the inventory.
- Improve book-title matching.
- Add a database for managing library records.
- Add an administrative interface for updating book availability.