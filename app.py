from flask import Flask, request, jsonify
import os

app = Flask(__name__)

SCENES = {
    "intro": "You find yourself in a dark forest. Two paths lie ahead: one to the left, dimly lit; one to the right, lined with glowing mushrooms.",
    "left_path": "You walk down the left path and stumble upon an ancient well. A strange humming noise rises from within.",
    "right_path": "The right path leads to a clearing where a hooded figure beckons you silently.",
    "unknown": "You wander into the unknown, unsure of what lies ahead."
}

@app.route('/')
def home():
    return "Welcome to AI Dungeon Master!"

@app.route('/start-game', methods=['POST'])
def start_game():
    data = request.get_json()
    name = data.get("player_name", "Adventurer")
    return jsonify({
        "player_name": name,
        "scene": SCENES["intro"]
    })

@app.route('/next-scene', methods=['POST'])
def next_scene():
    data = request.get_json()
    choice = data.get("choice", "").lower()

    if "left" in choice:
        scene = SCENES["left_path"]
    elif "right" in choice:
        scene = SCENES["right_path"]
    else:
        scene = SCENES["unknown"]

    return jsonify({
        "choice": choice,
        "next_scene": scene
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
