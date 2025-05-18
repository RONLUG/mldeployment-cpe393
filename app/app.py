from flask import Flask, request, jsonify, abort, redirect
import pickle
import numpy as np
import pandas as pd

import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


# Load the trained model
with open("model_house.pkl", "rb") as f:
    model = pickle.load(f)

with open("model_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


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
    keys = ["area", "stories", "bathrooms"]

    for k in keys:
        if k not in data:
            abort(400, description=f"Can't access data.{k} from data")

    raw_input = pd.DataFrame(data)
    input_features = pd.DataFrame(scaler.transform(raw_input), columns=raw_input.columns)

    prediction = model.predict(input_features)
    prediction_list = [{"predict_price": float(x)} for x in prediction]

    return jsonify(prediction_list)
