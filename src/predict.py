import pandas as pd
import joblib

from src.config import *
from src.preprocess import clean_data
from src.decision_engine import decide

def load_models():
    state_model = joblib.load(STATE_MODEL_PATH)
    intensity_model = joblib.load(INTENSITY_MODEL_PATH)
    return state_model, intensity_model


def predict():

    df = pd.read_csv(TEST_PATH)
    df = clean_data(df)

    state_model, intensity_model = load_models()

    X = df[[TEXT_COL] + NUM_COLS + CAT_COLS]

    state_probs = state_model.predict_proba(X)
    intensity_probs = intensity_model.predict_proba(X)

    state_preds = state_model.predict(X)
    intensity_preds = intensity_model.predict(X)

    results = []

    for i in range(len(df)):

        confidence = max(
            state_probs[i].max(),
            intensity_probs[i].max()
        )

        uncertain_flag = 1 if confidence < 0.5 else 0

        stress = df.iloc[i]["stress_level"]
        energy = df.iloc[i]["energy_level"]
        time_of_day = df.iloc[i]["time_of_day"]

        action, when = decide(
            state_preds[i],
            intensity_preds[i],
            stress,
            energy,
            time_of_day
        )

        results.append({
            "id": df.iloc[i]["id"],
            "predicted_state": state_preds[i],
            "predicted_intensity": intensity_preds[i],
            "confidence": float(confidence),
            "uncertain_flag": uncertain_flag,
            "what_to_do": action,
            "when_to_do": when
        })

    output = pd.DataFrame(results)
    output.to_csv("predictions.csv", index=False)

    print("predictions.csv generated successfully.")


if __name__ == "__main__":
    predict()