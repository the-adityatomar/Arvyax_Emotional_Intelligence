import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from config import *
from preprocess import clean_data


def build_preprocessor():
    return ColumnTransformer([
        ("text", TfidfVectorizer(max_features=5000, ngram_range=(1, 2)), TEXT_COL),
        ("num", StandardScaler(), NUM_COLS),
        ("cat", OneHotEncoder(handle_unknown="ignore"), CAT_COLS)
    ])


def train():

    df = pd.read_csv(TRAIN_PATH)
    df = clean_data(df)

    X = df[[TEXT_COL] + NUM_COLS + CAT_COLS]
    y_state = df[TARGET_STATE]
    y_intensity = df[TARGET_INTENSITY]

    preprocessor = build_preprocessor()

    state_model = Pipeline([
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(max_iter=1000))
    ])

    intensity_model = Pipeline([
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(max_iter=1000))
    ])

    print("Training state model...")
    state_model.fit(X, y_state)

    print("Training intensity model...")
    intensity_model.fit(X, y_intensity)

    joblib.dump(state_model, STATE_MODEL_PATH)
    joblib.dump(intensity_model, INTENSITY_MODEL_PATH)

    print("Models saved successfully.")


if __name__ == "__main__":
    train()