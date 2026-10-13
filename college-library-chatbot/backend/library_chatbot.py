
import json
from pathlib import Path

# Find the book inventory file
BASE_DIR = Path(__file__).resolve().parent.parent
BOOKS_FILE = BASE_DIR / "config" / "books.json"


def load_books():
    """Load book information from the JSON configuration file."""
    with open(BOOKS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["books"]


def answer_question(question, books):
    """Answer questions using only the library inventory."""
    question = question.lower()

    for book in books:
        if book["title"].lower() in question:
            if book["available"]:
                return "The book is available."
            else:
                return "The book is currently borrowed."

    return "That book is not available in our library."


def main():
    books = load_books()

    print("Welcome to the College Library Chatbot!")
    print("Ask about a book, or type 'exit' to stop.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = answer_question(question, books)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()
