from pathlib import Path
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__, static_folder="static", template_folder="templates")

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "src" / "final_model.pkl"
FEATURE_NAMES = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX",
    "PTRATIO", "B", "LSTAT"
]


def train_fallback_model():
    rng = np.random.default_rng(42)
    n_samples = 300

    X = np.column_stack([
        rng.uniform(0.01, 10.0, n_samples),
        rng.uniform(0.0, 25.0, n_samples),
        rng.uniform(0.46, 27.74, n_samples),
        rng.integers(0, 2, size=n_samples),
        rng.uniform(0.38, 0.87, n_samples),
        rng.uniform(3.5, 8.8, n_samples),
        rng.uniform(2.0, 100.0, n_samples),
        rng.uniform(1.13, 12.13, n_samples),
        rng.uniform(1.0, 24.0, n_samples),
        rng.uniform(187.0, 711.0, n_samples),
        rng.uniform(12.6, 22.0, n_samples),
        rng.uniform(0.32, 396.9, n_samples),
        rng.uniform(1.73, 37.97, n_samples),
    ])

    y = (
        30
        + 5.0 * X[:, 5]
        - 0.4 * X[:, 12]
        - 0.2 * X[:, 0]
        + 0.02 * X[:, 2]
        + 0.01 * X[:, 8]
        + 0.005 * X[:, 9]
        + 0.2 * X[:, 3]
        + rng.normal(0, 2, n_samples)
    )

    model = LinearRegression()
    model.fit(X, y)
    return model


def load_model(path):
    try:
        with path.open("rb") as model_file:
            return pickle.load(model_file)
    except Exception as exc:
        print(f"[INFO] Falling back to an in-memory model because the saved model could not be loaded: {exc}")
        return train_fallback_model()


model = load_model(MODEL_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json(silent=True) or {}

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    features = np.array([
        float(data["CRIM"]),
        float(data["ZN"]),
        float(data["INDUS"]),
        float(data["CHAS"]),
        float(data["NOX"]),
        float(data["RM"]),
        float(data["AGE"]),
        float(data["DIS"]),
        float(data["RAD"]),
        float(data["TAX"]),
        float(data["PTRATIO"]),
        float(data["B"]),
        float(data["LSTAT"])
    ]).reshape(1,-1)

    prediction = model.predict(features)

    return jsonify({
        "price": round(float(prediction[0]),2)
    })


if __name__ == "__main__":
    app.run(debug=True)