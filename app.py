import gradio as gr
import pandas as pd
import joblib

from src.config import *
from src.preprocess import clean_data
from src.decision_engine import decide


state_model = joblib.load(STATE_MODEL_PATH)
intensity_model = joblib.load(INTENSITY_MODEL_PATH)


def run_pipeline(
    journal_text,
    sleep_hours,
    energy_level,
    stress_level,
    duration_min,
    time_of_day,
    ambience_type
):

    # Create input dataframe
    input_df = pd.DataFrame([{
        "journal_text": journal_text,
        "sleep_hours": sleep_hours,
        "energy_level": energy_level,
        "stress_level": stress_level,
        "duration_min": duration_min,
        "time_of_day": time_of_day,
        "ambience_type": ambience_type
    }])

    input_df = clean_data(input_df)

    X = input_df[[TEXT_COL] + NUM_COLS + CAT_COLS]

    # Predictions
    state_probs = state_model.predict_proba(X)[0]
    intensity_probs = intensity_model.predict_proba(X)[0]

    state_pred = state_model.predict(X)[0]
    intensity_pred = intensity_model.predict(X)[0]

    confidence = float(max(state_probs.max(), intensity_probs.max()))
    uncertain_flag = 1 if confidence < 0.5 else 0

    # Decision Engine
    action, when = decide(
        state_pred,
        intensity_pred,
        stress_level,
        energy_level,
        time_of_day
    )

    return {
        "predicted_state": state_pred,
        "predicted_intensity": int(intensity_pred),
        "confidence": round(confidence, 3),
        "uncertain_flag": uncertain_flag,
        "what_to_do": action,
        "when_to_do": when
    }


# -------------------------
# Gradio UI
# -------------------------
iface = gr.Interface(
    fn=run_pipeline,

    inputs=[
        gr.Textbox(label="Journal Reflection"),

        gr.Slider(0, 12, step=0.5, label="Sleep Hours"),
        gr.Slider(1, 10, step=1, label="Energy Level"),
        gr.Slider(1, 10, step=1, label="Stress Level"),
        gr.Slider(0, 120, step=5, label="Session Duration (min)"),

        gr.Dropdown(
            ["morning", "afternoon", "evening", "night"],
            label="Time of Day"
        ),

        gr.Dropdown(
            ["forest", "ocean", "rain", "mountain", "cafe", "unknown"],
            label="Ambience Type"
        ),
    ],

    outputs=gr.JSON(label="AI Output"),

    title="ArvyaX Emotional Intelligence System",

    description=(
        "Analyze emotional state, intensity, and receive actionable guidance "
        "based on your reflection and contextual signals."
    )
)


# -------------------------
# Launch
# -------------------------
if __name__ == "__main__":
    iface.launch()