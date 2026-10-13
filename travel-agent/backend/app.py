
from pathlib import Path
import sys

from flask import Flask, jsonify, request, send_from_directory

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = PROJECT_DIR / "frontend"

# Make travel_agent.py importable from the backend.
sys.path.insert(0, str(PROJECT_DIR))

from travel_agent import TravelAgent

app = Flask(__name__)

# One instance retains memory while the server is running.
agent = TravelAgent()


@app.get("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/style.css")
def stylesheet():
    return send_from_directory(FRONTEND_DIR, "style.css")


@app.get("/script.js")
def javascript():
    return send_from_directory(FRONTEND_DIR, "script.js")


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/api/plan")
def create_plan():
    data = request.get_json(silent=True) or {}

    destination = str(data.get("destination", "")).strip()

    try:
        days = int(data.get("days"))
        people = int(data.get("people"))
    except (TypeError, ValueError):
        return jsonify({
            "error": "Days and people must be whole numbers."
        }), 400

    if not destination:
        return jsonify({"error": "Please enter a destination."}), 400

    if not 1 <= days <= 30:
        return jsonify({
            "error": "Days must be between 1 and 30."
        }), 400

    if not 1 <= people <= 20:
        return jsonify({
            "error": "People must be between 1 and 20."
        }), 400

    result = agent.create_plan(destination, days, people)

    if not isinstance(result, dict):
        return jsonify({"error": result}), 400

    return jsonify(result)


@app.get("/api/memory")
def get_memory():
    return jsonify(agent.memory)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
