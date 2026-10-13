
from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path

from library_chatbot import load_books, answer_question

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = Flask(
    __name__,
    static_folder=str(FRONTEND_DIR),
    static_url_path="/static"
)

books = load_books()


@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"reply": "Please enter a book name or question."}), 400

    reply = answer_question(message, books)

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
