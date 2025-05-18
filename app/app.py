from flask import Flask, request, jsonify, abort, redirect
import pickle
import numpy as np
import sys
import json

app = Flask(__name__)


# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400

@app.route("/")
def home():
    return redirect("https://youtu.be/dQw4w9WgXcQ?si=2_n6XLTHgPFGnptv", code=302)

@app.route("/health", methods=["POST"])
def health():
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if "features" not in data:
        abort(400, description="Can't access data.features from data")
    try: 
        if np.array(data["features"]).shape[1] != 4:
            abort(400, description="Invalid data.features format, data.features must be array with shape [n, 4]")
    except:
        abort(400, description="Invalid data.features format, data.features must be array with shape [n, 4]")

    input_features = np.array(data["features"]).reshape(2, -1)
    prediction = model.predict_proba(input_features)
    pred_results = zip(np.argmax(prediction, 1).tolist(), np.max(prediction, 1).tolist())
    json_key = ["prediction", "confidence"]
    return jsonify([dict(zip(json_key, pred)) for pred in pred_results])
