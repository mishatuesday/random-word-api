from flask import Flask, jsonify
import random

app = Flask(__name__)

# Load words from words.txt
with open("words.txt", "r") as file:
    words = [line.strip() for line in file if line.strip()]

@app.route("/random")
def random_word():
    if not words:
        return jsonify({"error": "No words available"}), 500
    return jsonify({"word": random.choice(words)})

if __name__ == "__main__":
    # Run directly on Render, port 10000
    app.run(host="0.0.0.0", port=10000)