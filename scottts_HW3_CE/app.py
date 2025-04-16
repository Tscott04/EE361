
from flask import Flask, request, jsonify
import numpy as np
import joblib
import os
from FrontEnd import data
from BackEnd import train_all_user_models

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask ML TouchAuth API running!", 200

@app.route('/authenticate/<user_id>', methods=['POST'])
def authenticate(user_id):
    try:
        swipe = request.get_json()
        required_fields = [
            'averageDirection', 'averageVelocity', 'directionEndToEnd',
            'midStrokeArea', 'midStrokePressure', 'pairwiseVelocityPercentile',
            'startX', 'startY', 'stopX', 'stopY', 'strokeDuration'
        ]

        if not all(field in swipe for field in required_fields):
            return jsonify({"message": "Invalid features provided"}), 400

        model_path = f"models/knn_model_{user_id}.pkl"
        if not os.path.exists(model_path):
            print(f"Model not found for user {user_id}. Retraining all models...")
            train_all_user_models(data)

        if not os.path.exists(model_path):
            return jsonify({"message": "Unable to train model for user."}), 500

        model = joblib.load(model_path)
        features = np.array([[swipe[field] for field in required_fields]])
        prediction = model.predict(features)

        return jsonify({
            "match": bool(prediction[0]),
            "message": "Matched" if prediction[0] == 1 else "Not matched"
        }), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
