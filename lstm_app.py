# lstm_app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    coin = data.get("coin", "BTC")

    # Mock LSTM prediction
    predicted_price = round(random.uniform(10000, 70000), 2)
    trend = random.choice(["up", "down", "sideways"])

    return jsonify({
        "coin": coin,
        "predicted_price": predicted_price,
        "trend": trend
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
