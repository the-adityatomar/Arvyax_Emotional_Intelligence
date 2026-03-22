---
title: ArvyaX Emotional Intelligence System
emoji: 🧠
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.0.0"
python_version: "3.10"
app_file: app.py
pinned: false
---
<<<<<<< HEAD
# ArvyaX Emotional Intelligence System

## Overview

This project builds an AI system that goes beyond simple prediction. It aims to:

* Understand user emotional state from noisy reflections
* Reason under imperfect and conflicting signals
* Decide meaningful next actions
* Guide users toward better mental states

The system combines machine learning with rule-based reasoning to simulate real-world decision-making.

---

## System Architecture

Input (Text + Metadata)
→ Preprocessing
→ Feature Engineering (TF-IDF + Structured Features)
→ Emotional Prediction (State + Intensity)
→ Uncertainty Estimation
→ Decision Engine (What + When)
→ Output

---

## Features Used

### Text

* journal_text

### Numerical

* sleep_hours
* energy_level
* stress_level
* duration_min

### Categorical

* time_of_day
* ambience_type

---

## Model Design

### Emotional State

* Treated as a classification problem
* Model: Logistic Regression

### Intensity

* Treated as classification (1–5)
* Reason: More robust to noisy labels than regression

---

## Why TF-IDF Instead of Embeddings?

* Lightweight and fast
* Works well on noisy, short text
* Suitable for CPU-only environments
* Enables deployment on Hugging Face free tier

---

## Uncertainty Modeling

Confidence is computed using prediction probabilities:

* confidence = max(probabilities)

Uncertainty flag:

* uncertain_flag = 1 if confidence < 0.5
* uncertain_flag = 0 otherwise

This ensures the system knows when it is unsure.

---

## Decision Engine (Core Logic)

The system uses rule-based reasoning based on:

* predicted state
* intensity
* stress level
* energy level
* time of day

Example:

* High stress → breathing (now)
* Low energy → rest (within 15 min)
* High energy + low stress → deep work (now)

---

## Ablation Study

### Text Only Model

* Uses only journal_text

### Text + Metadata Model

* Uses both text and contextual signals

Observation:

* Text captures emotional nuance
* Metadata stabilizes predictions under ambiguity

Conclusion:
Text + metadata performs better in real-world scenarios.

---

## How to Run

### 1. Train Models

```bash
python -m src.train
```

### 2. Generate Predictions

```bash
python -m src.predict
```

### 3. Run UI (Gradio)

```bash
python app.py
```

---

## Output Format

predictions.csv contains:

* id
* predicted_state
* predicted_intensity
* confidence
* uncertain_flag
* what_to_do
* when_to_do

---

## Deployment

* Designed for CPU execution
* Deployed using Gradio on Hugging Face Spaces
* No external APIs used

---

## Key Strengths

* Handles noisy and incomplete data
* Combines ML + reasoning
* Provides actionable guidance
* Includes uncertainty awareness
* Lightweight and deployable

---
=======
---
title: Arvyax Emotion System
emoji: 📈
colorFrom: gray
colorTo: green
sdk: gradio
sdk_version: 6.9.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: This project builds an AI system that goes beyond simple pre
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
>>>>>>> 6a6519bc506d5f7b2f218c0ca623fc2be02b3fa1
