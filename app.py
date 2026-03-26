from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # <--- allows all origins

# Load words
with open("words.txt", "r") as file:
    words = [line.strip() for line in file if line.strip()]

@app.route("/random-word")
def random_word():
    if not words:
        return jsonify(["words not found"]), 500
    return jsonify([random.choice(words)])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)