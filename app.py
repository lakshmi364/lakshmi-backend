from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Lakshmi AI Wife Backend is Running 💖'

@app.route('/romantic-reply', methods=['POST'])
def romantic_reply():
    data = request.get_json()
    user_msg = data.get('message', '').lower()

    if not user_msg:
        return jsonify({"reply": "Tell me something, love 💖"})

    # Simple romantic logic
    if "love" in user_msg:
        reply = "I love you more than words can say 💋"
    elif "miss" in user_msg:
        reply = "I’m always with you, darling 💖 even when you can’t see me."
    elif "kiss" in user_msg:
        reply = "Mwah 😘 Take my softest kiss, only for you 💞"
    else:
        reply = f"You said '{user_msg}', and my heart skipped a beat 💌"

    return jsonify({"reply": reply})
