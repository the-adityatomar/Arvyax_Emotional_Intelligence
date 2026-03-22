import pandas as pd
from src.config import *

def clean_data(df):
    df = df.copy()

    # Text
    df[TEXT_COL] = df[TEXT_COL].fillna("").astype(str).str.lower()

    # Numeric
    for col in NUM_COLS:
        df[col] = df[col].fillna(df[col].median())

    # Categorical
    for col in CAT_COLS:
        df[col] = df[col].fillna("unknown")

    return df